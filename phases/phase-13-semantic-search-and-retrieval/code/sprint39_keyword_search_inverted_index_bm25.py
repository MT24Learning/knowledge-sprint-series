import re, math, pathlib, collections as C, numpy as np

def blocks(f):                         # each record starts ".I n"
    t = pathlib.Path("cran", f).read_text(encoding="latin-1")
    return [b.split(".W", 1) for b in re.split(r"\n?\.I ", t)[1:]]
tok = lambda s: re.findall(r"[a-z0-9]+", s.lower())
docs = [tok(b[1]) for b in blocks("cran.all.1400")]
qs = [tok(b[1]) for b in blocks("cran.qry")]
rel = C.defaultdict(dict)              # query 1..225 -> {doc: code}
for l in pathlib.Path("cran/cranqrel").read_text().splitlines():
    q, d, r = map(int, l.split()); rel[q][d - 1] = r
post = C.defaultdict(list)             # inverted index: word -> docs
for d, ws in enumerate(docs):
    for w, c in C.Counter(ws).items(): post[w].append((d, c))
post = {w: np.array(p).T for w, p in post.items()}
N, L = len(docs), np.array([len(d) for d in docs])

def bm25(q, idf=True, k1=1.2, b=0.75):
    s = np.zeros(N)
    for w in filter(post.__contains__, q):
        d, c = post[w]; n = len(d)
        c = c / (1 - b + b * L[d] / L.mean())        # length
        s[d] += (math.log(1 + (N - n + .5) / (n + .5)) if idf
                 else 1) * (c * (k1 + 1) / (c + k1) if k1 else c)
    return s
def ndcg(s, j, gain=lambda r: 5 - r, skip_base=True, k=10):
    skip = {d for d, r in j.items() if r == -1 and skip_base}
    top = [d for d in np.argsort(-s, kind="stable")
           if d not in skip][:k]  # Cleverdon: 1 = complete answer
    g = {d: max(gain(r), 0) for d, r in j.items() if d not in skip}
    dcg = sum(g.get(d, 0) / math.log2(i + 2) for i, d in enumerate(top))
    ig = sorted(g.values())[::-1][:k]
    return dcg / sum(v / math.log2(i + 2) for i, v in enumerate(ig))
def mean(J=None, gain=lambda r: 5 - r, skip_base=True, **kw):
    J = J or [rel[i + 1] for i in range(len(qs))]
    return np.mean([ndcg(bm25(q, **kw), j, gain, skip_base) if j
                    else 0 for q, j in zip(qs, J)])

if __name__ == "__main__":
    print(N, "abstracts,", len(post), "words | 'the' in", len(post[
        "the"][0]), "| 'flutter' in", len(post["flutter"][0]))
    print("nDCG@10 count, +rare, +cap, +length:", np.round([mean(idf=0,
        k1=None, b=0), mean(k1=None, b=0), mean(b=0), mean()], 3))
    top1 = [rel[i + 1].get(np.argmax(bm25(q))) for i, q in enumerate(qs)]
    print("code -1 ranked first:", top1.count(-1), "of", len(qs))
    print(f"same run, 4 = best: {mean(gain=lambda r: r, skip_base=0):.3f}"
          f" | all relevant: {mean(gain=lambda r: 1, skip_base=0):.3f}")
    by_I = [rel.get(int(b[0]), {}) for b in blocks("cran.qry")]
    print(f"queries matched by .I number: {mean(by_I):.3f}")
    rare = lambda ws: {w for w in ws if w in post
                       and len(post[w][0]) < N / 10}   # in < 10%
    pairs = [(q, docs[d]) for i, q in enumerate(qs)
             for d, r in rel[i + 1].items() if r > 0]
    print("judged pairs sharing no rare word:", sum(not rare(q) &
          rare(d) for q, d in pairs), "of", len(pairs))
# 1400 abstracts, 7471 words | 'the' in 1391 | 'flutter' in 56
# nDCG@10 count, +rare, +cap, +length: [0.026 0.252 0.326 0.382]
# code -1 ranked first: 92 of 225
# same run, 4 = best: 0.307 | all relevant: 0.485
# queries matched by .I number: 0.010
# judged pairs sharing no rare word: 393 of 1612
