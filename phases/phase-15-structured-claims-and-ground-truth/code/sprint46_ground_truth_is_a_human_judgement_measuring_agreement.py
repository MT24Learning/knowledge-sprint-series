import json
from collections import Counter
from itertools import combinations, permutations, product

with open("climate-fever.jsonl", encoding="utf-8") as f:
    rows = [json.loads(line) for line in f]
pairs = [e for r in rows for e in r["evidences"]]
votes = [[v for v in e["votes"] if v] for e in pairs]
size = sorted(Counter(map(len, votes)).items())
print(len(pairs), "pairs | votes per pair:",
      *[f"{k}:{v}" for k, v in size])
NEI = "NOT_ENOUGH_INFO"
def tied(vs):
    top = Counter(vs).most_common()
    return len(top) > 1 and top[0][1] == top[1][1]
def majority(vs):                 # the dataset's rule: a tie -> NEI
    return NEI if tied(vs) else Counter(vs).most_common(1)[0][0]
same = sum(majority(v) == e["evidence_label"]
           for v, e in zip(votes, pairs))
print("labels rebuilt from the votes:", same, "of", len(pairs))
o = Counter()                     # Krippendorff's alpha, nominal
for vs in votes:
    for a, b in permutations(vs, 2): o[a, b] += 1 / (len(vs) - 1)
n, nc = sum(o.values()), Counter()
for (a, b), w in o.items(): nc[a] += w
d_obs = sum(w for (a, b), w in o.items() if a != b) / n
d_exp = sum(nc[a] * nc[b] for a in nc for b in nc if a != b)
agree = [a == b for vs in votes for a, b in combinations(vs, 2)]
print(f"alpha {1 - d_obs / (d_exp / (n * (n - 1))):.3f} | "
      f"raw agreement {sum(agree) / len(agree):.1%}")
ties = [vs for vs in votes if tied(vs)]
nei = sum(e["evidence_label"] == NEI for e in pairs)
sr = sum({"SUPPORTS", "REFUTES"} <= set(vs) for vs in ties)
print(f"ties: {len(ties)} -> NEI ({len(ties) / nei:.1%} of {nei} NEI)"
      f" | {sr} SUPPORTS v REFUTES")
def claim_label(labels):          # the dataset's claim rule
    s, r = "SUPPORTS" in labels, "REFUTES" in labels
    return ("DISPUTED" if s and r else "SUPPORTS" if s
            else "REFUTES" if r else NEI)
def options(vs):                  # what a tie could have become
    top = Counter(vs).most_common()
    if not tied(vs): return [top[0][0]]
    return {k for k, c in top if c == top[0][1]} | {NEI}
moved = 0
for r in rows:
    opts = [options([v for v in e["votes"] if v])
            for e in r["evidences"]]
    moved += len({claim_label(p) for p in product(*opts)}) > 1
print(f"claims whose label depends on the tie rule: {moved}"
      f" of {len(rows)} ({moved / len(rows):.1%})")
# 7675 pairs | votes per pair: 2:5340 3:1554 4:761 5:20
# labels rebuilt from the votes: 7675 of 7675
# alpha 0.334 | raw agreement 58.7%
# ties: 2501 -> NEI (50.7% of 4930 NEI) | 685 SUPPORTS v REFUTES
# claims whose label depends on the tie rule: 693 of 1535 (45.1%)
