import numpy as np
from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)
X, y = X[y > 0][:, 2:], y[y > 0] - 1
# petal length, width in cm; 1 = virginica
i = np.random.default_rng(26).permutation(100)
tr, te = i[:70], i[70:]          # learn / hold out

def err(rule, idx):              # 0-1 loss, summed
    return sum(rule(X[j]) != y[j] for j in idx)
memo = {tuple(X[j]): y[j] for j in tr}
look = lambda x: memo.get(tuple(x))   # or None
near = lambda x: y[tr][np.argmin(
    ((X[tr] - x) ** 2).sum(1))]
cuts = [(f, c) for f in (0, 1)
        for c in np.unique(X[tr, f])]
f, c = min(cuts, key=lambda k: err(  # ERM
    lambda x: x[k[0]] > k[1], tr))
cut = lambda x: int(x[f] > c)
silent = sum(look(X[j]) is None for j in te)
print(len(cuts), "cuts; best:",
      ["length", "width"][f], ">", c)
print("look", err(look, tr), silent,
      err(look, te) - silent)
print("near", err(near, tr), err(near, te))
print("cut ", err(cut, tr), err(cut, te))
# 42 cuts; best: width > 1.6
# look 1 24 1
# near 1 3
# cut  3 3
