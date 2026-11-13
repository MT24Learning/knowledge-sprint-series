import numpy as np
def f(s, sg=10., r=28., b=8/3):  # Lorenz (1963)
    x, y, z = s[..., 0], s[..., 1], s[..., 2]
    return np.stack([sg*(y-x), x*(r-z)-y, x*y-b*z], -1)
def step(s, h=.002):  # one Runge-Kutta 4 step
    k1 = f(s); k2 = f(s + h/2*k1); k3 = f(s + h/2*k2)
    return s + h/6*(k1 + 2*k2 + 2*k3 + f(s + h*k3))
def run(s, t):
    for _ in range(round(t / .002)): s = step(s)
    return s
a, b = run(np.ones(3), 50), run(np.ones(3), 50)
print("same start, same end:", np.array_equal(a, b))
base = run(np.ones((24, 3)) + np.arange(24)[:, None], 30)
d0 = 10.0 ** -np.arange(2, 13, 2)  # first errors
s = np.repeat(base, 7, 0)
s[:, 0] += np.tile(np.r_[0, d0], 24)  # nudge x only
T, t = np.full(len(s), np.nan), 0.0
while np.isnan(T).any() and t < 60:
    s, t = step(s), t + .002
    e = np.linalg.norm(s - s[::7].repeat(7, 0), axis=1)
    T[np.isnan(T) & (e > 1)] = t  # forecast lost
H = T.reshape(24, 7)[:, 1:].mean(0)  # mean of 24 starts
print("lost at t =", " ".join(f"{h:.1f}" for h in H))
k = np.polyfit(np.log10(d0), H, 1)[0]
print(f"each 10x sharper start buys {-k:.2f} time units")
x = np.loadtxt("laser_a.txt")  # Santa Fe set A, real
nxt = np.loadtxt("laser_a_next.txt")  # the hidden 100
W = np.lib.stride_tricks.sliding_window_view(x, 6)[:-100]
j = np.linalg.norm(W - x[-6:], axis=1).argmin()
err = abs(x[j+6:j+46] - nxt[:40])  # follow the analogue
print("laser analogue, worst error per pulse:",
      *err.reshape(5, 8).max(1).astype(int))
def g(r, n):  # 2^n-fold logistic map at x = 1/2, - 1/2
    x = .5
    for _ in range(2**n): x = r*x*(1 - x)
    return x - .5
R = [2.0, 1 + 5**.5]  # superstable r, cycles 1 and 2
for n in range(2, 9):  # Newton's method for cycle 2^n
    r = R[-1] + (R[-1] - R[-2]) / 4.7  # first guess
    for _ in range(40):
        r -= g(r, n) * 1e-9 / (g(r + 1e-9, n) - g(r, n))
    R.append(r)
D = [(R[i]-R[i-1]) / (R[i+1]-R[i]) for i in range(1, 8)]
print("delta:", " ".join(f"{d:.3f}" for d in D))
# Output printed on the image:
# same start, same end: True
# lost at t = 4.4 8.6 14.1 19.3 24.7 29.3
# each 10x sharper start buys 2.54 time units
# laser analogue, worst error per pulse: 10 20 37 72 108
# delta: 4.709 4.681 4.663 4.668 4.669 4.669 4.669
