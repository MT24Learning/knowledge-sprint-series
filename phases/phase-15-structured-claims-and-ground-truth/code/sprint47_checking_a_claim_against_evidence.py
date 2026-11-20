import json, re
import numpy as np
from scipy.sparse import csr_matrix, hstack
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import GroupKFold

with open("climate-fever.jsonl", encoding="utf-8") as f:
    rows = [json.loads(line) for line in f]
P = [(i, r["claim"], e["evidence"], e["evidence_label"])
     for i, r in enumerate(rows) for e in r["evidences"]]
g, C, E, y = (np.array(x) for x in zip(*P))
NEI = "NOT_ENOUGH_INFO"
def overlap(c, e):          # share of words the two have in common
    a, b = (set(re.findall(r"[a-z]{3,}", s.lower())) for s in (c, e))
    return len(a & b) / max(1, len(a | b))

def run(parts, swap=False):  # c claim, e evidence, o overlap
    pred = np.empty(len(y), dtype=object)
    for tr, te in GroupKFold(5).split(y, y, g):  # by claim
        vc = TfidfVectorizer(min_df=2, sublinear_tf=True).fit(C[tr])
        ve = TfidfVectorizer(min_df=2, sublinear_tf=True).fit(E[tr])
        def X(rc, rev):
            cols = []
            if "c" in parts: cols.append(vc.transform(C[rc]))
            if "e" in parts: cols.append(ve.transform(E[rev]))
            if "o" in parts: cols.append(csr_matrix(
                [[overlap(C[i], E[j])] for i, j in zip(rc, rev)]))
            return hstack(cols).tocsr()
        ev = np.roll(te, 5 * (len(te) // 10)) if swap else te
        m = LogisticRegression(max_iter=5000, class_weight="balanced")
        pred[te] = m.fit(X(tr, tr), y[tr]).predict(X(te, ev))
    return pred

print(len(y), "claim-evidence pairs | gold SUPPORTS or REFUTES:",
      f"{np.mean(y != NEI):.1%}")
print("balanced accuracy, 5 folds grouped by claim (chance 0.333)")
for name, parts in [("claim only", "c"), ("evidence only", "e"),
                    ("claim + evidence", "ce"), ("+ overlap", "ceo")]:
    print(f"  {name:<17} {balanced_accuracy_score(y, run(parts)):.3f}")
print("says SUPPORTS/REFUTES: true pairs | evidence of another claim")
for name, parts in [("claim + evidence", "ce"), ("+ overlap", "ceo")]:
    t, s = (np.mean(run(parts, sw) != NEI) for sw in (False, True))
    print(f"  {name:<17} {t:.1%} | {s:.1%}")
# 7675 claim-evidence pairs | gold SUPPORTS or REFUTES: 35.8%
# balanced accuracy, 5 folds grouped by claim (chance 0.333)
#   claim only        0.461
#   evidence only     0.438
#   claim + evidence  0.489
#   + overlap         0.500
# says SUPPORTS/REFUTES: true pairs | evidence of another claim
#   claim + evidence  40.3% | 39.8%
#   + overlap         40.4% | 27.6%
