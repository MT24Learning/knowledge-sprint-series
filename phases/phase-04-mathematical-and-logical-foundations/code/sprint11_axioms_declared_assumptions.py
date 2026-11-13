import numpy as np
from numpy.linalg import norm
def ang(P, Q, R):  # angle at P
    u, v = Q - (P@Q)*P, R - (P@R)*P
    c = u @ v / (norm(u) * norm(v))
    return np.degrees(np.arccos(c))
A, B, C = np.eye(3)  # unit sphere
s = [ang(A, B, C), ang(B, C, A),
     ang(C, A, B)]
excess = np.radians(sum(s) - 180)
r = [sum(s), excess, 4 * np.pi / 8]
print(np.round(r, 4))
# [270.  1.5708  1.5708]
