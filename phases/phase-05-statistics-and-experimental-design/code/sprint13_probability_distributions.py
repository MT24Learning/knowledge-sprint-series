import numpy as np
rng = np.random.default_rng(13)
N = 100_000
e = rng.exponential(1, N)  # mean 1
c = rng.standard_cauchy(N) # no mean
for k in (10, 1_000, N):
    print(k, e[:k].mean().round(3),
          c[:k].mean().round(3))
m = rng.exponential(1, (10_000, 30))
print(m.mean(1).std().round(3),
      round(1 / 30**0.5, 3))  # CLT
# 10     0.949  -2.977
# 1000   1.025  -0.432
# 100000 1.0     0.866
# 0.181  0.183
