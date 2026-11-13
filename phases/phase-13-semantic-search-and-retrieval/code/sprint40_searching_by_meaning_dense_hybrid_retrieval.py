import numpy as np, gensim.downloader as api
from wordllama import WordLlama
from s39 import docs, qs, rel, bm25, ndcg, N    # Sprint 39's code

unit = lambda X: X / np.maximum(np.linalg.norm(X, axis=-1,
                                               keepdims=True), 1e-12)
glove = api.load("glove-wiki-gigaword-50")      # 400 000 words x 50
def glove_vec(words):             # mean of unit word vectors
    v = [unit(glove[w]) for w in words if w in glove]
    return unit(np.mean(v, 0)) if v else np.zeros(50)
wl = WordLlama.load(disable_download=True)      # trained, 256 numbers
wl_vec = lambda words: unit(wl.embed([" ".join(words)])[0])
D = {"glove": np.array([glove_vec(d) for d in docs]),
     "wl": unit(wl.embed([" ".join(d) for d in docs]))}

def rrf(*runs, k=60):             # reciprocal rank fusion
    out = np.zeros(N)
    for s in runs:
        r = np.empty(N)
        r[np.argsort(-s, kind="stable")] = np.arange(1, N + 1)
        out += 1 / (k + r)
    return out

runs = {"bm25": bm25,
        "glove": lambda q: D["glove"] @ glove_vec(q),
        "wl": lambda q: D["wl"] @ wl_vec(q),
        "bm25+wl": lambda q: rrf(bm25(q), D["wl"] @ wl_vec(q)),
        "bm25+glove": lambda q: rrf(bm25(q), D["glove"] @ glove_vec(q))}
S = {n: np.array([ndcg(f(q), rel[i + 1]) for i, q in enumerate(qs)])
     for n, f in runs.items()}
for n, v in S.items():
    print(f"nDCG@10 {n:10s} {v.mean():.3f}")
d = S["wl"] - S["bm25"]
print("wl vs bm25, queries won/lost/tied:",
      (d > 0).sum(), (d < 0).sum(), (d == 0).sum())
rng = np.random.default_rng(40)   # paired randomization test
for a in ("wl", "bm25+wl"):
    d = S[a] - S["bm25"]
    flip = np.abs((rng.choice([-1, 1], (100_000, d.size)) * d).mean(1))
    p = (flip >= abs(d.mean())).mean()
    print(f"{a} - bm25 = {d.mean():+.3f}, p = {p:.4f}")
# nDCG@10 bm25       0.382
# nDCG@10 glove      0.102
# nDCG@10 wl         0.340
# nDCG@10 bm25+wl    0.395
# nDCG@10 bm25+glove 0.258
# wl vs bm25, queries won/lost/tied: 75 119 31
# wl - bm25 = -0.042, p = 0.0012
# bm25+wl - bm25 = +0.013, p = 0.1811
