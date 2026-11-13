import numpy as np
rng = np.random.default_rng(9)
X = rng.normal(size=(100, 2))
y = X @ np.array([2.0, -3.0])
L = lambda w: ((X@w - y)**2).mean()
g = lambda w: 2*X.T@(X@w - y)/100
w, e = np.zeros(2), np.eye(2)[0]*1e-6
num = (L(w+e) - L(w-e)) / 2e-6
print(g(w)[0].round(4), num.round(4))
for _ in range(100): w = w - 0.1*g(w)
print(w.round(3), L(w).round(6))
# -5.0586 -5.0586 · [ 2. -3.] 0.0
