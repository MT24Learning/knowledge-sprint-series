import numpy as np
from sklearn.datasets import make_moons
X, y = make_moons(200, noise=.2, random_state=32)
y, s = y[:, None], lambda z: .5 + .5 * np.tanh(z / 2)
act = {"sig": (s, lambda a: a * (1 - a)),
       "relu": (lambda z: z * (z > 0), lambda a: a > 0)}
aug = lambda A: np.c_[A, np.ones(len(A))]   # bias
def init(S, seed, gain):             # N(0, gain/fan-in)
    r = np.random.default_rng(seed)
    return [r.normal(0, (gain / m)**.5, (m + 1, n))
            for m, n in zip(S, S[1:])]
def step(W, f="sig"):                # forward, backward
    g, dg = act[f]; A = [X]
    for w in W[:-1]: A.append(g(aug(A[-1]) @ w))
    z = aug(A[-1]) @ W[-1]
    d, G, D = (s(z) - y) / len(X), [], []
    for l in range(len(W) - 1, -1, -1):    # chain rule
        G[:0], D[:0] = [aug(A[l]).T @ d], [d]
        if l: d = d @ W[l][:-1].T * dg(A[l])
    L = np.mean(np.logaddexp(0, z) - y * z)
    return L, G, D, ((z > 0) == y).mean()
def fit(W, lr=1, f="sig", n=2000):
    for _ in range(n):
        L, G, D, acc = step(W, f)
        W = [w - lr * g for w, g in zip(W, G)]
    return float(round(L, 3)), float(acc), W
W, V = init([2, 3, 1], 32, 1), init([2, 3, 1], 1, 1)
e = lambda t: step([w + t * v for w, v in zip(W, V)])[0]
a = sum((g * v).sum() for g, v in zip(step(W)[1], V))
n = (e(1e-5) - e(-1e-5)) / 2e-5      # finite difference
print(f"check {a:.10f} {n:.10f}")
R = [fit(init([2, 16, 1], 1, 2), lr, "relu")
     for lr in (.01, 1, 30)]
print("loss, acc:", [r[:2] for r in R])
_, acc, W = fit([np.zeros((3, 16)), np.zeros((17, 1))])
print("zero init:", len({*map(tuple, W[0].T.round(9))}),
      "distinct of 16, acc", acc)
N = np.linalg.norm
for f, gain in (("sig", 1), ("relu", 2)):
    D = step(init([2] + [32] * 12 + [1], 32, gain), f)[2]
    print(f, f"layer 1 / 12: {N(D[0]) / N(D[11]):.1e}")
# check 0.0033105346 0.0033105346
# loss, acc: [(0.293, 0.89), (0.048, 0.98), (3.432, 0.665)]
# zero init: 1 distinct of 16, acc 0.885
# sig layer 1 / 12: 1.0e-07
# relu layer 1 / 12: 6.1e-01
