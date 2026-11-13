import numpy as np
rng = np.random.default_rng(16)
def half(c, n=1000, teach=0.6):
  new = rng.random(n) < 0.05  # rivals
  for yr in range(1, 300):
    s = new.mean()
    out = rng.random(n) < 1/30  # retire
    new[out] = rng.random(
        out.sum()) < teach  # recruits
    new |= rng.random(n) < c * s
    if new.mean() >= 0.5:
      return yr  # rival reaches 50%
for c in (0.0, 0.05, 0.2):
  print(c, half(c))
# 0.0 51
# 0.05 20
# 0.2 12
