import numpy as np
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression as LR
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier as MLP
X, y = load_digits(return_X_y=True); X = X / 16  # grey 0..16 -> 0..1
Xa, Xt, ya, yt = train_test_split(X, y, test_size=.3, stratify=y,
                                  random_state=42)
lin = LR(max_iter=5000).fit(Xa, ya)                    # linear model
net = MLP((64,), max_iter=3000, random_state=42).fit(Xa, ya)
def grad(m, X, y):                         # d loss / d pixel
    P = m.predict_proba(X); P[np.arange(len(y)), y] -= 1
    if hasattr(m, "coef_"): return P @ m.coef_
    (W1, W2), b1 = m.coefs_, m.intercepts_[0]
    return (P @ W2.T * (X @ W1 + b1 > 0)) @ W1.T
def attack(m, X, y, e, steps=10):          # sign steps kept within ±e
    A = X.copy()
    for _ in range(steps):
        A = A + e / 4 * np.sign(grad(m, A, y))
        A = np.clip(np.clip(A, X - e, X + e), 0, 1)
    return A
pct = lambda m, X: f"{100 * m.score(X, yt):.1f}%"
noise = np.random.default_rng(42).choice([-1, 1], Xt.shape)
print(len(yt), "test digits | clean: linear", pct(lin, Xt), "net",
      pct(net, Xt))
for lv in range(1, 5):                     # change of lv grey levels
    e = lv / 16; R = np.clip(Xt + e * noise, 0, 1)
    print(f"±{lv} linear: noise {pct(lin, R)} attack",
          pct(lin, attack(lin, Xt, yt, e)), "| net: noise",
          pct(net, R), "attack", pct(net, attack(net, Xt, yt, e)))
e = 2 / 16                                 # the change on Fig. 1
W = lin.coef_; r = [abs(W[i] - W[j]).sum() / np.linalg.norm(
    W[i] - W[j]) for i in range(10) for j in range(i)]
print(f"chosen / random push: {np.mean(r):.2f} (ceiling sqrt(64) = 8)")
A = attack(lin, Xt, yt, e)                 # made on the linear model
print("made on linear, given to net:", pct(net, Xt), "->", pct(net, A))
rob = LR(max_iter=5000).fit(np.vstack([Xa, attack(lin, Xa, ya, e)]),
                            np.r_[ya, ya])     # trained on old attacks
print("defence | old attack:", pct(rob, A), "fresh attack:",
      pct(rob, attack(rob, Xt, yt, e)))
adv = MLP((64,), random_state=42)
adv.partial_fit(Xa, ya, classes=np.arange(10))
for _ in range(200):                       # adversarial training
    adv.partial_fit(np.vstack([Xa, attack(adv, Xa, ya, e, 5)]),
                    np.r_[ya, ya])
print("adversarial training | clean:", pct(adv, Xt), "attack:",
      pct(adv, attack(adv, Xt, yt, e)), "50 steps:",
      pct(adv, attack(adv, Xt, yt, e, 50)))
# 540 test digits | clean: linear 96.7% net 97.8%
# ±1 linear: noise 96.3% attack 82.8% | net: noise 97.0% attack 73.7%
# ±2 linear: noise 95.4% attack 46.7% | net: noise 95.4% attack 21.5%
# ±3 linear: noise 92.2% attack 9.4% | net: noise 92.4% attack 0.2%
# ±4 linear: noise 89.8% attack 0.4% | net: noise 86.7% attack 0.0%
# chosen / random push: 5.43 (ceiling sqrt(64) = 8)
# made on linear, given to net: 97.8% -> 35.7%
# defence | old attack: 88.5% fresh attack: 15.9%
# adversarial training | clean: 97.2% attack: 74.3% 50 steps: 73.9%
