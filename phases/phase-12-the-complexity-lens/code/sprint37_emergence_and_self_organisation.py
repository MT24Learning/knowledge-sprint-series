import numpy as np
def nb(g, i, j, c):  # like and occupied neighbours
    a = g[max(i-1, 0):i+2, max(j-1, 0):j+2]
    s, o, k = (a == c).sum(), (a > 0).sum(), g[i, j]
    return s - (k == c), o - (k > 0)
def alike(g):  # mean share of like neighbours
    r = [nb(g, *p, g[tuple(p)]) for p in np.argwhere(g)]
    return np.mean([s / o for s, o in r if o])
def city(want, n=40, seed=37):  # Schelling (1971)
    rng = np.random.default_rng(seed)
    g = rng.choice(3, (n, n), p=[.25, .375, .375])
    s0 = alike(g)
    for _ in range(100):
        moved = 0
        for i, j in rng.permutation(np.argwhere(g > 0)):
            c = g[i, j]; s, o = nb(g, i, j, c)
            if o == 0 or s >= want * o: continue
            g[i, j] = 0; E = np.argwhere(g == 0)
            d = ((E - [i, j])**2).sum(1)  # nearest first
            for a, b in E[np.argsort(d, kind="stable")]:
                s, o = nb(g, a, b, c)
                if o == 0 or s >= want * o:
                    g[a, b] = c; moved += 1; break
            else: g[i, j] = c  # nowhere better: stay
        if moved == 0: break
    return s0, alike(g)
s0, s1 = city(1/2)
print(f"start {s0:.2f} alike; wants 1/2, ends {s1:.2f}")
print("ends by demand .1-.7:",
      *(f"{city(w / 10)[1]:.2f}" for w in range(1, 8)))
rng = np.random.default_rng(37)  # BTW (1987) sandpile
z, sizes = rng.integers(0, 4, (50, 50)), []
for k in range(40000):
    i, j = rng.integers(0, 50, 2); z[i, j] += 1; n = 0
    while (z > 3).any():  # topple; edges lose grains
        t = (z > 3).astype(int); n += t.sum(); z -= 4 * t
        z[1:] += t[:-1]; z[:-1] += t[1:]
        z[:, 1:] += t[:, :-1]; z[:, :-1] += t[:, 1:]
    if k >= 10000: sizes.append(n)  # skip warm-up
s = np.array(sizes)
print(f"30000 grains: {(s==0).mean():.0%} topple none,",
      f"largest {s.max()}")
print("sizes 1-9, 10-99, 100-999, 1000+:", *np.histogram(
      s, [1, 10, 100, 1000, 10**6])[0])
q = np.loadtxt("quakes.csv", delimiter=",", skiprows=1)
q = q[:, 4]  # Fiji magnitudes, real (R: quakes)
for mc in (4.5, 4.7):  # Aki (1965), half-bin shift
    m = q[q > mc - .01]
    b = np.log10(np.e) / (m.mean() - (mc - .05))
    print(f"Fiji M >= {mc}: {len(m)} quakes,",
          f"b = {b:.2f} +- {b / len(m)**.5:.2f}")
# Output printed on the image:
# start 0.50 alike; wants 1/2, ends 0.79
# ends by demand .1-.7: 0.52 0.54 0.65 0.71 0.79 0.92 0.97
# 30000 grains: 57% topple none, largest 5902
# sizes 1-9, 10-99, 100-999, 1000+: 4806 4054 3282 821
# Fiji M >= 4.5: 623 quakes, b = 1.08 +- 0.04
# Fiji M >= 4.7: 415 quakes, b = 1.22 +- 0.06
