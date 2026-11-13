import numpy as np
rng = np.random.default_rng(15)
n = 100_000
z = lambda: rng.normal(size=n)
s = z()  # severity
def y(t):  # true effect of t: +1
    return t - 2 * s + z()
def gap(t, o):
    return o[t].mean() - o[~t].mean()
t = s + z() > 0  # sicker -> treated
o = y(t)
print(gap(t, o).round(3))  # observed
X = np.c_[np.ones(n), t, s]
b = np.linalg.lstsq(X, o)[0]
print(b[1].round(3))  # adjusted
r = rng.random(n) < .5  # coin flip
print(gap(r, y(r)).round(3))  # random
# -1.262   0.996   0.998
