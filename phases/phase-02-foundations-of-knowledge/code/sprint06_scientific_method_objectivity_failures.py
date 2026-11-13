import numpy as np
rng = np.random.default_rng(1)
# 20 outcomes, no real effect
p = rng.random((100_000, 20))
hit = p.min(axis=1) < 0.05
print(hit.mean())
# 0.646  (exact: 1 - 0.95**20)
