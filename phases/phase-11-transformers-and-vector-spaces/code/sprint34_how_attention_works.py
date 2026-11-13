import numpy as np, gensim.downloader as api
wv = api.load("glove-wiki-gigaword-50")
V, ix = wv.vectors, wv.key_to_index
E = V / np.linalg.norm(V, axis=1)[:, None]
def softmax(z):
    e = np.exp(z - z.max(-1, keepdims=True))
    return e / e.sum(-1, keepdims=True)
def attention(Q, K, Vv, mask=None):  # Vaswani et al.
    S = Q @ K.T / np.sqrt(K.shape[1])
    if mask is not None: S = np.where(mask, S, -np.inf)
    W = softmax(S)
    return W @ Vv, W
def rank(v, t):  # words closer to v than t is
    s = E @ (v / np.linalg.norm(v))
    return int((s > s[ix[t]]).sum())
b0 = V[ix["bank"]]
print("bank alone  | river", rank(b0, "river"),
      "loan", rank(b0, "loan"))
S2 = [("river", "we sat on the river bank"),
      ("loan", "she took a loan from the bank")]
for tag, s in S2:
    w = s.split(); X = V[[ix[t] for t in w]]
    Y, W = attention(X, X, X)  # Q = K = V = X
    b = w.index("bank")
    r, l = rank(Y[b], "river"), rank(Y[b], "loan")
    print(f"{tag:5} sent. | river {r} loan {l} "
          f"| self {W[b, b]:.2f}")
rng = np.random.default_rng(34)  # why divide by sqrt(dk)
for dk in [4, 64, 512]:
    q = rng.normal(size=(2000, dk))
    K = rng.normal(size=(2000, 10, dk))  # 10 keys each
    S = np.einsum("nd,ntd->nt", q, K)
    a = softmax(S).max(1).mean()  # unscaled
    z = softmax(S / np.sqrt(dk)).max(1).mean()  # scaled
    print(f"dk {dk:3}: var {S.var():5.1f} | top weight "
          f"{a:.2f} -> {z:.2f}")
M = np.tril(np.ones((6, 6), bool))  # no peeking ahead
X = rng.normal(size=(6, 8))
_, W = attention(X, X, X, M)
print("mask keeps", M.sum(), "of 36 scores")
print("token 1 sees", W[0].round(2))
# Output printed on the image:
# bank alone  | river 2353 loan 52
# river sent. | river 1475 loan 87 | self 0.78
# loan  sent. | river 2278 loan 12 | self 0.68
# dk   4: var   4.0 | top weight 0.49 -> 0.30
# dk  64: var  63.7 | top weight 0.86 -> 0.32
# dk 512: var 505.5 | top weight 0.95 -> 0.32
# mask keeps 21 of 36 scores
# token 1 sees [1. 0. 0. 0. 0. 0.]
