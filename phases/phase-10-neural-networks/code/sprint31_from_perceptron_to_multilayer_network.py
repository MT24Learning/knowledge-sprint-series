import numpy as np
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
AND, XOR = np.array([0, 0, 0, 1]), np.array([0, 1, 1, 0])
def perceptron(y, epochs=100):      # Rosenblatt's rule
    w, b = np.zeros(2), 0.0
    for e in range(1, epochs + 1):
        miss = 0
        for x, t in zip(X, y):
            err = t - int(w @ x + b > 0)
            w += err * x; b += err; miss += err != 0
        if miss == 0: return f"no miss from epoch {e}"
    return f"{miss} misses in epoch {epochs}"
print("AND", perceptron(AND), "| XOR", perceptron(XOR))
A1 = np.c_[X, np.ones(4)]            # best straight line
print("line", np.linalg.lstsq(A1, XOR)[0].round(3) + 0.)
W, c = np.ones((2, 2), int), np.array([0, -1])
H = np.maximum(0, X @ W + c)         # ReLU (§6.1)
print("hidden", H.tolist(), "out", (H @ [1, -2]).tolist())
sig = lambda z: 1 / (1 + np.exp(-z))
def train(h, seed, steps=5000, lr=0.5):   # 2-h-1 net
    rng = np.random.default_rng(seed)
    W1, b1 = rng.normal(size=(2, h)), np.zeros(h)
    W2, b2 = rng.normal(size=h), 0.0
    for _ in range(steps):
        A = sig(X @ W1 + b1); p = sig(A @ W2 + b2)
        d2 = p - XOR; d1 = np.outer(d2, W2) * A * (1 - A)
        W2 -= lr * A.T @ d2; b2 -= lr * d2.sum()
        W1 -= lr * X.T @ d1; b1 -= lr * d1.sum(0)
    return p
ok = lambda h, s: all(abs(train(h, s) - XOR) < .1)
n = [sum(ok(h, s) for s in range(100)) for h in (2, 4)]
print("2 and 4 hidden units solve", n, "of 100")
bad = next(s for s in range(100) if not ok(2, s))
print("seed", bad, train(2, bad).round(3))
# AND no miss from epoch 6 | XOR 4 misses in epoch 100
# line [0.  0.  0.5]
# hidden [[0, 0], [1, 0], [1, 0], [2, 1]] out [0, 1, 1, 0]
# 2 and 4 hidden units solve [77, 100] of 100
# seed 6 [0.001 0.5   0.999 0.5  ]
