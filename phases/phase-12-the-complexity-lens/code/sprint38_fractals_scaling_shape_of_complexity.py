import json, re, warnings, numpy as np, powerlaw
from collections import Counter; from pyproj import Transformer
from shapely.geometry import shape
warnings.simplefilter("ignore", DeprecationWarning)
def divider(P, r):  # walk a ruler of length r along P
    p, j, n = P[0], 0, 0
    while True:
        d = np.hypot(*(P[j+1:] - p).T)
        far = np.flatnonzero(d >= r)
        if not len(far): return n*r + (d[-1] if len(d) else 0)
        k = far[0]; A = P[j+k] if k else p; B = P[j+k+1]
        u, w = B - A, A - p; a, b = u @ u, 2 * u @ w
        t = (-b + np.sqrt(b*b - 4*a*(w @ w - r*r))) / (2*a)
        p, j, n = A + t*u, j + k, n + 1
def dim(r, L): return 1 - np.polyfit(np.log(r), np.log(L), 1)[0]
k = np.array([[0., 0], [1, 0]])  # Koch curve, 7 levels
for _ in range(7):
    a, b = k[:-1], k[1:]; d = (b - a) / 3
    c = a + d + d @ [[.5, -3**.5/2], [3**.5/2, .5]]
    s = np.stack([a, a+d, c, a+2*d], 1).reshape(-1, 2)
    k = np.vstack([s, k[-1:]])
r = .9 * 3.0 ** -np.arange(2, 6)  # off the grid
print(f"Koch: D = {dim(r, [divider(k, x) for x in r]):.3f}"
      f" (log 4 / log 3 = {np.log(4)/np.log(3):.3f})")
with open("ne_10m_admin_0_countries.json") as fh:
    uk = [f for f in json.load(fh)["features"]
          if f["properties"]["ADMIN"] == "United Kingdom"][0]
gb = max(shape(uk["geometry"]).geoms, key=lambda g: g.area)
to_m = Transformer.from_crs(4326, 27700, always_xy=True)
xy = np.array(gb.exterior.coords).T  # lon, lat
P = np.column_stack(to_m.transform(*xy))  # metres
gap = np.median(np.hypot(*np.diff(P, axis=0).T))
print(f"Great Britain: {len(P)} points, median gap {gap/1e3:.1f} km")
r = 200e3 / 2.0 ** np.arange(8)  # 200 km ... 1.6 km
L = np.array([divider(P, x) for x in r])
print("lengths, km:", *np.round(L / 1e3).astype(int))
print(f"D for rulers 200-25 km: {dim(r[:4], L[:4]):.2f}",
      f"| 12.5-1.6 km: {dim(r[4:], L[4:]):.2f}")
with open("melville-moby_dick.txt") as fh:
    w = Counter(re.findall(r"[a-z]+", fh.read().lower()))
f = np.array(sorted(w.values(), reverse=True))
lr, lf = np.log10(np.arange(1, len(f) + 1)), np.log10(f)
z = np.polyfit(lr, lf, 1)[0]; R2 = np.corrcoef(lr, lf)[0, 1]**2
print(f"Moby Dick: {len(f)} words, rank slope {z:.2f}, R^2 {R2:.3f}")
fit = powerlaw.Fit(f, discrete=True, verbose=False)
n = (f >= fit.xmin).sum()  # tail chosen by KS (Clauset)
print(f"tail from {fit.xmin:.0f} ({n} words): alpha {fit.alpha:.2f}")
out = {}
for alt in ("lognormal", "exponential"):
    R, p = fit.distribution_compare("power_law", alt)
    out[alt] = bool(R > 0 and p < .1)  # beaten at 10%?
print("ruled out by the power law:", out)
# Output printed on the image:
# Koch: D = 1.259 (log 4 / log 3 = 1.262)
# Great Britain: 3707 points, median gap 1.4 km
# lengths, km: 2404 2813 3424 4244 5175 5989 6585 6958
# D for rulers 200-25 km: 1.27 | 12.5-1.6 km: 1.14
# Moby Dick: 16950 words, rank slope -1.16, R^2 0.980
# tail from 7 (3077 words): alpha 1.94
# ruled out by the power law: {'lognormal': False, 'exponential': True}
