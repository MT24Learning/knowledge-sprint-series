import numpy as np
rng = np.random.default_rng(17)
f = np.sin  # the truth
x = rng.uniform(0, 3, 20)  # training
y = f(x) + rng.normal(0, 0.1, 20)
xi = rng.uniform(0, 3, 1000)  # inside
xo = rng.uniform(3, 4, 1000)  # outside
def err(p, u, v):
  e = np.polyval(p, u) - v
  return np.sqrt((e**2).mean()).round(3)
for d in (1, 3, 9):
  p = np.polyfit(x, y, d)
  print(d, err(p, x, y),
        err(p, xi, f(xi)),
        err(p, xo, f(xo)))
# 1 0.294 0.314 1.451
# 3 0.107 0.061 0.118
# 9 0.073 0.41 482.043
