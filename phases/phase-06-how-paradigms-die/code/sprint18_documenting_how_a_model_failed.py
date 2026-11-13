import numpy as np
from scipy.special import ellipk
a = np.arange(1, 91)  # release angle, deg
m = np.sin(np.radians(a) / 2)**2
r = 2 / np.pi * ellipk(m)  # exact / model
def edge(tol):  # last angle within tol
  return a[r - 1 <= tol].max()
print("MODEL  T = 2*pi*sqrt(L/g)")
print("HOLDS  <=1% to", edge(0.01), "deg")
print("       <=5% to", edge(0.05), "deg")
print("FAILS  at 90 deg:", r[-1].round(3))
print("CLASS  structure (sin x ~ x)")
# MODEL  T = 2*pi*sqrt(L/g)
# HOLDS  <=1% to 22 deg
#        <=5% to 50 deg
# FAILS  at 90 deg: 1.18
# CLASS  structure (sin x ~ x)
