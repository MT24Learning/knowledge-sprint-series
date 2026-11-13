import numpy as np
from s39 import blocks, tok, qs, rel, bm25, N    # Sprint 39's code

text = [" ".join(b[1].split()) for b in blocks("cran.all.1400")]
J = [rel[i + 1] for i in range(len(qs))]
good = [{d for d, r in j.items() if r > 0} for j in J]
base = [{d for d, r in j.items() if r == -1} for j in J]

def retrieve(q, k=5, hide=()):   # BM25 always returns k passages
    s = bm25(q); s[list(hide)] = -np.inf
    top = np.argsort(-s, kind="stable")[:k]
    return top, s[top]

K = (1, 3, 5, 10, 20)
hit = np.array([[bool(g & set(retrieve(q, k, b)[0])) for k in K]
                for q, g, b in zip(qs, good, base)])
print("a judged passage in top 1/3/5/10/20:", hit.mean(0).round(3))
print("questions with none in the top 5:", (~hit[:, 2]).sum())

# make each question unanswerable: hide every judged passage
a = np.array([retrieve(q, 1, b)[1][0] for q, b in zip(qs, base)])
u = np.array([retrieve(q, 1, b | g)[1][0]
              for q, g, b in zip(qs, good, base)])
auc = (a[:, None] > u).mean() + (a[:, None] == u).mean() / 2
floor = np.quantile(a, 0.10)     # keeps 90% of answerable questions
print(f"top-1 score {a.mean():.1f} vs {u.mean():.1f}, AUC {auc:.3f}")
print(f"floor {floor:.1f} lets through {(u >= floor).mean():.0%}"
      " of unanswerable questions")

def build_prompt(question, k=3):
    top, sc = retrieve(tok(question), k)
    if sc[0] < floor:
        return "ABSTAIN: no passage scores above the floor."
    ctx = "\n".join(f"[{d + 1}] {text[d][:52]}…" for d in top)
    return f"Answer only from these; cite [n].\n{ctx}\nQ: {question}"

print(build_prompt("how does heating change panel flutter"))
print(build_prompt("how do i bake bread"))
# a judged passage in top 1/3/5/10/20: [0.511 0.671 0.769 0.853 0.907]
# questions with none in the top 5: 52
# top-1 score 22.5 vs 19.9, AUC 0.599
# floor 14.6 lets through 84% of unanswerable questions
# Answer only from these; cite [n].
# [859] flutter of aerodynamically heated aluminium-alloy an…
# [1008] free-flight measurements of the static and dynamic .…
# [948] panel flutter tests on full scale x-15 lower vertica…
# Q: how does heating change panel flutter
# ABSTAIN: no passage scores above the floor.
