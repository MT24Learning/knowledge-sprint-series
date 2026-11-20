import json, re
from collections import Counter

with open("climate-fever.jsonl", encoding="utf-8") as f:
    rows = [json.loads(line) for line in f]
# a word-list rule: rough, it misses some words, over-counts others
LISTS = {k: set(v.split()) for k, v in {
  "number": "two three four five six seven eight nine ten half twice"
            " double dozen hundred thousand million billion percent",
  "time": "since until year years decade decades century centuries"
          " today now currently recently ago already soon",
  "comparison": "than more less fewer most least higher lower"
                " greater larger smaller faster slower warmer colder",
  "hedge": "may might could would should will likely unlikely"
           " probably possibly perhaps roughly nearly almost",
  "scope": "all every each many some few only always often mostly",
  "negation": "not no never none nothing nobody neither nor without",
  "condition": "if unless when whenever",
  "source": "according says said claim claims study studies report"
            " reports reported scientists researchers experts",
}.items()}

def qualifiers(text):
    w = re.findall(r"[a-z0-9']+", text.lower().replace("’", "'"))
    found = {k for k, words in LISTS.items() if words & set(w)}
    if any(ch.isdigit() for x in w for ch in x): found.add("number")
    if any(re.fullmatch(r"(1[0-9]|20)\d\ds?", x) for x in w):
        found.add("time")                     # 1880, 2100, 1990s
    if any(x.endswith("n't") for x in w): found.add("negation")
    return found

Q = [qualifiers(r["claim"]) for r in rows]
n, hit = len(rows), sum(1 for q in Q if q)
print(f"{n} real claims | {hit} carry a qualifier ({hit/n:.1%})")
top = Counter(k for q in Q for k in q).most_common()
for (a, x), (b, y) in zip(top[0::2], top[1::2]):
    print(f"{a:<10} {x:>4} {x/n:5.1%} | {b:<10} {y:>4} {y/n:5.1%}")
per = Counter(min(len(q), 4) for q in Q)
print("per claim 0|1|2|3|4+:", *[per[i] for i in range(5)])
ex = next(r["claim"] for r in rows if r["claim_id"] == "2657")
print("claim 2657:", sorted(qualifiers(ex)))
neg = [r for r, q in zip(rows, Q) if "negation" in q]
ref = lambda rs: sum(r["claim_label"] == "REFUTES" for r in rs)/len(rs)
print(f"REFUTES: with a negation {ref(neg):.1%} | all {ref(rows):.1%}")
# 1535 real claims | 1251 carry a qualifier (81.5%)
# number      668 43.5% | time        507 33.0%
# comparison  334 21.8% | hedge       310 20.2%
# negation    301 19.6% | source      260 16.9%
# scope       205 13.4% | condition   128  8.3%
# per claim 0|1|2|3|4+: 284 433 394 263 161
# claim 2657: ['number', 'time']
# REFUTES: with a negation 27.9% | all 16.5%
