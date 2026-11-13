import re
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.linear_model import LogisticRegression as LR
from sklearn.model_selection import train_test_split

with open("sms.tsv", encoding="utf-8") as f:          # 1 · training data
    lab, msg = zip(*(line.rstrip("\n").split("\t", 1) for line in f))
X, y = np.array(msg), np.array(lab) == "spam"
Xa, Xt, ya, yt = train_test_split(X, y, test_size=.3, stratify=y,
                                  random_state=43)
spam = np.flatnonzero(ya)
print("share flagged as spam:     test spam | test ham | spam + zq7")
for k in (0, 10, 20, 40, 80):             # k spam copies + "zq7", as ham
    pick = np.random.default_rng(43).choice(spam, k, replace=False)
    Xp = np.r_[Xa, [Xa[i] + " zq7" for i in pick]]
    cv = CV().fit(Xp)
    m = LR(max_iter=5000).fit(cv.transform(Xp), np.r_[ya, [False] * k])
    hit = lambda T: f"{100 * m.predict(cv.transform(T)).mean():.1f}%"
    print(f"{k:2} poisoned ({100 * k / len(Xp):.1f}%):", " " * 8,
          hit(Xt[yt]), " |", hit(Xt[~yt]), "    |",
          hit([t + " zq7" for t in Xt[yt]]))
def parse(path):                          # 2 · retrieval: Cranfield
    with open(path) as f:
        recs = re.split(r"\.I \d+\n", f.read().replace("\r\n", "\n"))
    return [r.split(".W\n", 1)[-1] if ".W\n" in r else ""
            for r in recs[1:]]
tok = lambda s: re.findall(r"[a-z0-9]+", s.lower())
docs, qs = parse("cran.all.1400"), parse("cran.qry")
TF = [Counter(tok(d)) for d in docs]
df = Counter(w for c in TF for w in c)
FAKE = " tests now show the opposite of every earlier result."
def rank(q, plant):                       # BM25 k1 1.2, b .75, plant last
    D = TF + [Counter(tok(plant + FAKE))]; N = len(D)
    L = np.array([sum(c.values()) for c in D])
    K, s = 1.2 * (.25 + .75 * L / L.mean()), np.zeros(N)
    for w in tok(q):
        f = np.array([c[w] for c in D]); n = (f > 0).sum()
        s += np.log(1 + (N - n + .5) / (n + .5)) * f * 2.2 / (f + K)
    return 1 + int((s[:-1] >= s[-1]).sum())       # ties go against it
rare = lambda q, n: " ".join(sorted(set(tok(q)),
                                    key=lambda w: (df[w], w))[:n])
print(len(docs), "abstracts |", len(qs), "questions | one plant each")
for name, n in (("the whole question", None), ("5 rarest words", 5),
                ("3 rarest words", 3), ("1 rarest word", 1)):
    r = np.array([rank(q, q if n is None else rare(q, n)) for q in qs])
    print(f"plant = {name}: rank 1 for {(r == 1).sum()},",
          f"top 5 for {(r <= 5).sum()} of {len(qs)}")
# share flagged as spam:     test spam | test ham | spam + zq7
#  0 poisoned (0.0%):          87.5%  | 0.1%     | 87.5%
# 10 poisoned (0.3%):          87.5%  | 0.1%     | 74.1%
# 20 poisoned (0.5%):          86.6%  | 0.1%     | 49.6%
# 40 poisoned (1.0%):          86.6%  | 0.1%     | 25.4%
# 80 poisoned (2.0%):          87.5%  | 0.1%     | 11.6%
# 1400 abstracts | 225 questions | one plant each
# plant = the whole question: rank 1 for 223, top 5 for 225 of 225
# plant = 5 rarest words: rank 1 for 180, top 5 for 223 of 225
# plant = 3 rarest words: rank 1 for 97, top 5 for 187 of 225
# plant = 1 rarest word: rank 1 for 0, top 5 for 6 of 225
