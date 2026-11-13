import numpy as np
from scipy.special import softmax
rng = np.random.default_rng(35)
n, d, h, dff = 5, 16, 4, 64  # tokens, width, heads, FFN
P = lambda a, b: rng.normal(0, a ** -0.5, (a, b))
Wq, Wk, Wv, Wo = (P(d, d) for _ in range(4))
W1, W2 = P(d, dff), P(dff, d)
def norm(x):  # LayerNorm (gain 1, offset 0)
    m = x.mean(-1, keepdims=True)
    return (x - m) / x.std(-1, keepdims=True)
def mha(x, causal):  # h heads, each of width d / h
    q, k, v = (np.stack(np.split(x @ W, h, 1))
               for W in (Wq, Wk, Wv))
    S = q @ k.transpose(0, 2, 1) / np.sqrt(d // h)
    if causal:  # token i sees tokens 1..i only
        S = np.where(np.tri(len(x)) > 0, S, -np.inf)
    A = softmax(S, axis=-1) @ v
    return np.concatenate(A, 1) @ Wo
def block(x, causal=False):  # pre-LN residual layer
    x = x + mha(norm(x), causal)
    return x + np.maximum(0, norm(x) @ W1) @ W2  # FFN
def pe(n, d):  # sinusoidal positions (Vaswani et al.)
    f = 1e4 ** (np.arange(0, d, 2) / d)  # wavelengths
    a = np.arange(n)[:, None] / f
    s, c = np.sin(a), np.cos(a)  # even, odd columns
    return np.dstack([s, c]).reshape(n, d)
x, p = rng.normal(size=(n, d)), [3, 0, 4, 1, 2]
print("in", x.shape, "-> out", block(x).shape)
gap = lambda a, b: np.abs(a - b).max()  # largest change
xe, xs = x + pe(n, d), x[p] + pe(n, d)
g0 = gap(block(x)[p], block(x[p]))  # no mask, no pos.
g1 = gap(block(xe)[p], block(xs))  # with positions
g2 = gap(block(x, True)[p], block(x[p], True))  # causal
print(f"shuffle gap: plain {g0:.2f} | positions {g1:.2f}"
      f" | causal {g2:.2f}")
y = x.copy(); y[-1] *= -1  # change the last token only
for c in (False, True):
    k = gap(block(x, c)[:-1], block(y, c)[:-1])
    tag = "causal " if c else "two-way"
    print(tag, f"| rows 1-4 change {k:.2f}")
D, F, N, voc = 512, 2048, 6, 37000  # base model, Table 3
att = 4 * D * D + 4 * D  # Q, K, V, O matrices + offsets
ffn = 2 * D * F + F + D  # two dense layers
enc, dec = att + ffn + 4 * D, 2 * att + ffn + 6 * D
print("layer: attention", att, "FFN", ffn,
      f"-> FFN share {ffn / enc:.2f}")
tot = N * (enc + dec) + voc * D  # one shared embedding
print(f"base model {tot / 1e6:.1f} M (Table 3: 65 M)")
# Output printed on the image:
# in (5, 16) -> out (5, 16)
# shuffle gap: plain 0.00 | positions 2.15 | causal 1.33
# two-way | rows 1-4 change 1.79
# causal  | rows 1-4 change 0.00
# layer: attention 1050624 FFN 2099712 -> FFN share 0.67
# base model 63.1 M (Table 3: 65 M)
