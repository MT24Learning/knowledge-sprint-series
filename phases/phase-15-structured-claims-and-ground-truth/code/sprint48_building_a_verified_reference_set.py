import hashlib, json

SIZE = {"mnist": 10000, "cifar10": 10000, "cifar100": 10000,
        "caltech256": 29780, "imagenet": 50000, "quickdraw": 50426266,
        "20news": 7532, "imdb": 25000, "amazon": 9996437}  # test sets
FLAGGED = {"quickdraw": 6825383, "amazon": 533249}  # only a sample
def load(name):                                     # was checked
    with open(f"{name}_mturk.json", encoding="utf-8") as f:
        return json.load(f)
def given(e):         # votes for the given label (Amazon: by name)
    m, g = e["mturk"], e["given_original_label"]
    return m[g.lower()] if str(g).lower() in m else m["given"]
print(f"{'test set':<10} {'size':>8} checked errors share")
shares = []
for name, size in SIZE.items():
    d = load(name)
    err = sum(given(e) < 3 for e in d)  # under 3 of 5 people agree
    shares.append(100 * err / len(d) * FLAGGED.get(name, len(d)) / size)
    print(f"{name:<10} {size:>8} {len(d):>7} {err:>6} {shares[-1]:5.2f}%")
shares.append(1.35)                 # AudioSet: the paper's own figure
print(f"mean of 10 test sets: {sum(shares) / 10:.2f}%")
kind = {k: [] for k in ("fine", "fix", "both", "neither", "split")}
for e in load("imagenet"):
    m = e["mturk"]
    kind["fine" if m["given"] >= 3 else "fix" if m["guessed"] >= 3
         else "both" if m["both"] >= 3 else "neither"
         if m["neither"] >= 3 else "split"].append(e)
print("imagenet:", " | ".join(f"{k} {len(v)}"
                              for k, v in kind.items()))
def digest(edits, drop=()):       # a release is named by its content
    blob = json.dumps({"edits": sorted(edits), "drop": sorted(drop)})
    return hashlib.sha256(blob.encode()).hexdigest()[:8]
fix3 = [(e["id"], e["our_guessed_label"]) for e in kind["fix"]]
fix5 = [(e["id"], e["our_guessed_label"]) for e in kind["fix"]
        if e["mturk"]["guessed"] == 5]
bad = [e["id"] for k, v in kind.items() if k != "fine" for e in v]
for tag, ed, dr in [("v1.1 relabel 3 of 5", fix3, ()),
                    ("v1.2 relabel 5 of 5", fix5, ()),
                    ("v2.0 drop the errors", (), bad)]:
    print(f"{tag:<21} {50000 - len(dr)} items {len(ed):>4} edits"
          f" sha256 {digest(ed, dr)}")
# test set       size checked errors share
# mnist         10000     100     15  0.15%
# cifar10       10000     275     54  0.54%
# cifar100      10000    2235    585  5.85%
# caltech256    29780    2360    458  1.54%
# imagenet      50000    5440   2916  5.83%
# quickdraw  50426266    2500   1870 10.12%
# 20news         7532      93     82  1.09%
# imdb          25000    1310    725  2.90%
# amazon      9996437    1000    732  3.90%
# mean of 10 test sets: 3.33%
# imagenet: fine 2524 | fix 1428 | both 597 | neither 293 | split 598
# v1.1 relabel 3 of 5   50000 items 1428 edits sha256 214229ed
# v1.2 relabel 5 of 5   50000 items  468 edits sha256 3b07dbe4
# v2.0 drop the errors  47084 items    0 edits sha256 0b2fa020
