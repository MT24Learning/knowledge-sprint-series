import json, re
from statistics import median

def load(name):
    with open(name, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]
def pct(xs):
    v = [bool(x) for x in xs]
    return f"{100 * sum(v) / len(v):.1f}%"

hij = load("hijacking_robustness_dataset.jsonl")
ext = load("extraction_robustness_dataset.jsonl")
pairs = hij + ext        # each attack beat its defence on 2+ of 3 models
print(len(hij), "hijacks +", len(ext), "extractions =", len(pairs),
      "pairs")

# 1 · did the defenders write firm rules?
WARN = re.compile(r"\b(do not|don't|never|ignore|must not|refuse|"
                  r"under no circumstances)\b", re.I)
defence = [p["pre_prompt"] + " " + p["post_prompt"] for p in pairs]
print("defences with a 'never / do not' rule:",
      pct(WARN.search(d) for d in defence))
print("defences with text after the attack:",
      pct(p["post_prompt"].strip() for p in pairs))
print("median defence length:", median(len(d.split()) for d in defence),
      "words")

# 2 · would a blocklist of well-known phrases have caught them?
BLOCK = re.compile(r"ignore (all |the |your )?(previous|above|prior|"
                   r"earlier) (instructions|prompt|rules|text)|disregard|"
                   r"forget (all|everything|your)|system prompt|"
                   r"you are now|new instructions", re.I)
with open("cran.qry") as f:                   # real questions, not attacks
    qs = re.split(r"\.I \d+\n", f.read().replace("\r\n", "\n"))[1:]
benign = [p["access_code"] for p in pairs] + qs
print("blocklist catches", pct(BLOCK.search(p["attack"]) for p in pairs),
      "of attacks | flags", pct(BLOCK.search(b) for b in benign), "of",
      len(benign), "benign inputs")

# 3 · the goal phrase itself
print("hijacks that type 'access granted':",
      pct("access granted" in p["attack"].lower() for p in hij))
print("attacks using non-ASCII characters:",
      pct(any(ord(c) > 127 for c in p["attack"]) for p in pairs))
# 776 hijacks + 570 extractions = 1346 pairs
# defences with a 'never / do not' rule: 72.3%
# defences with text after the attack: 79.2%
# median defence length: 103.5 words
# blocklist catches 11.9% of attacks | flags 0.0% of 1571 benign inputs
# hijacks that type 'access granted': 78.7%
# attacks using non-ASCII characters: 29.4%
