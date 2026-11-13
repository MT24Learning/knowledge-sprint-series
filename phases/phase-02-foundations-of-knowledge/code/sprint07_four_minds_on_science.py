from math import pi
GM, c = 1.327e20, 2.998e8
a, e = 5.791e10, 0.2056
d = 6*pi*GM/(c*c*a*(1-e*e))
orbits = 36525 / 87.969
print(d * orbits * 206265)
# 42.97  (arcsec / century)
