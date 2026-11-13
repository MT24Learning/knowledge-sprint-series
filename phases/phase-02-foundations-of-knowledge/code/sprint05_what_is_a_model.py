from math import *
from scipy.special import ellipk
for d in (10, 20, 45, 90):
  k = sin(radians(d) / 2)
  r = 2/pi * ellipk(k*k)
  print(d, round(r, 3))
# 1.002  1.008  1.04  1.18
