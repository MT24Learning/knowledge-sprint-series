import numpy as np
from scipy.stats import ttest_ind
rng = np.random.default_rng(14)
def run(n, d, k=10_000):
    a = rng.normal(0, 1, (k, n))
    b = rng.normal(d, 1, (k, n))
    p = ttest_ind(b, a, axis=1)[1]
    hit = p < .05
    g = b.mean(1) - a.mean(1)
    return hit.mean(), g[hit].mean()
print(run(64, 0)[0])  # false alarms
for n in (64, 20):
    print(n, *np.round(run(n, .5), 3))
# 0.0498
# 64 0.794 0.562
# 20 0.335 0.831
