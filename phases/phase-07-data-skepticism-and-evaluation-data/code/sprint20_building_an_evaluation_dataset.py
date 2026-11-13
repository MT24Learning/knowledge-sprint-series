import numpy as np
rng = np.random.default_rng(20)
G, K = 200, 5               # groups, copies
g = np.repeat(np.arange(G), K)
c = rng.normal(size=(G, 8))
X = c[g] + 0.05*rng.normal(size=(G*K, 8))
y = rng.integers(0, 2, G)[g]   # coin flip
def score(test):            # 1-nearest nbr
    tr = ~test
    d = ((X[test, None]
          - X[None, tr])**2).sum(-1)
    hit = y[tr][d.argmin(1)] == y[test]
    seen = np.isin(g[test], g[tr])
    print(test.sum(), f"{hit.mean():.3f}",
          f"{seen.mean():.0%}")
score(rng.random(G*K) < 0.2)    # rows
pick = rng.choice(G, 40, replace=False)
score(np.isin(g, pick))         # groups
# 187 1.000 100%
# 200 0.440 0%
