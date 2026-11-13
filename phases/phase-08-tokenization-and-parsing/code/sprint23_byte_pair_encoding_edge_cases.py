import re
from collections import Counter
vocab = {"l o w _": 5, "l o w e r _": 2,
  "n e w e s t _": 6, "w i d e s t _": 3}
def merge(pair, w):            # a b -> ab
    a = re.escape(" ".join(pair))
    return re.sub(rf"(?<!\S){a}(?!\S)",
                  "".join(pair), w)
merges = []
for step in range(10):
    pairs = Counter()
    for w, n in vocab.items():
        s = w.split()
        for p in zip(s, s[1:]):
            pairs[p] += n
    best = max(pairs, key=pairs.get)
    merges.append(best)
    vocab = {merge(best, w): n
             for w, n in vocab.items()}
def bpe(word):
    w = " ".join(word) + " _"
    for pair in merges:
        w = merge(pair, w)
    return w.replace(" ", "|")
print(" ".join("".join(p) for p in merges))
print(sum(len(w.split()) * n
          for w, n in vocab.items()))
for w in ["lowest", "newer", "Lowest"]:
    print(w, bpe(w))
# es est est_ lo low ne new newest_ low_ wi
# 28
# lowest low|est_
# newer new|e|r|_
# Lowest L|o|w|est_
