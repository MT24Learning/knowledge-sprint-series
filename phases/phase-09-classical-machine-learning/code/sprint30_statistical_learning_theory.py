import numpy as np
from math import ceil, log, sqrt
from scipy.stats import binom
from sklearn.datasets import load_iris
n, delta = 70, 0.05     # 70 examples, 95% confidence
eps = lambda H: sqrt(log(2 * H / delta) / (2 * n))
# 1) pure noise: best of H coin-flip rules, 70 labels
for H in [1, 10**2, 10**4, 10**6]:
    k = np.arange(n + 1)                  # errors
    cdf = 1 - binom.sf(k, n, 0.5) ** H    # P(best<=k)
    best = np.searchsorted(cdf, 0.5) / n  # median
    print(f"{H:>7} best {best:.3f}",
          f"gap {0.5 - best:.3f} bound {eps(H):.3f}")
# 2) Sprint 26 with 142 cuts fixed before the data
X, y = load_iris(return_X_y=True)
X, y = X[y > 0][:, 2:], y[y > 0] - 1
i = np.random.default_rng(26).permutation(100)
tr, te = i[:70], i[70:]
cuts = [(f, k / 10) for f in (0, 1) for k in range(71)]
err = lambda f, c, j: ((X[j, f] > c) != y[j]).mean()
f, c = min(cuts, key=lambda fc: err(*fc, tr))
lo, e = err(f, c, tr), eps(len(cuts))
print(len(cuts), "cuts:", ["length", "width"][f], ">", c)
print(f"train {lo:.3f} + {e:.3f} = {lo + e:.3f},",
      f"test {err(f, c, te):.3f}")
need = log(2 * len(cuts) / delta) / (2 * 0.05 ** 2)
print("for eps = 0.05 the bound needs n =", ceil(need))
#       1 best 0.500 gap 0.000 bound 0.162
#     100 best 0.357 gap 0.143 bound 0.243
#   10000 best 0.271 gap 0.229 bound 0.304
# 1000000 best 0.214 gap 0.286 bound 0.354
# 142 cuts: width > 1.6
# train 0.043 + 0.248 = 0.291, test 0.100
# for eps = 0.05 the bound needs n = 1729
