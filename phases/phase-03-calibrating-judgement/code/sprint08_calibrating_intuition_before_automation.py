import numpy as np
rng = np.random.default_rng(8)
p = rng.uniform(.05, .95, 10**4)
y = rng.random(10**4) < p
f = p**2 / (p**2 + (1-p)**2)
bs = lambda q: ((q-y)**2).mean()
for q in (.5, p, f):
    print(round(bs(q), 3))
print(y[f >= .9].mean().round(2))
# 0.25  0.188  0.203  0.84
