text = "unbelievably tokenizers"
seen = {"unbelievable", "tokens"}
subs = ["un", "believ", "able", "ably",
        "token", "ize", "s"]
abc = list("abcdefghijklmnopqrstuvwxyz")
vocab = {p: i for i, p in
         enumerate(dict.fromkeys(subs + abc))}
def split(w):        # longest match first
    out, i = [], 0
    while i < len(w):
        j = len(w)
        while w[i:j] not in vocab: j -= 1
        out.append(w[i:j]); i = j
    return out
words = text.split()
toks = [t for w in words for t in split(w)]
print("chars", len(text))
print("words", [w if w in seen else "[UNK]"
                for w in words])
print("pieces", "|".join(toks))
print("ids", [vocab[t] for t in toks])
print("round trip", " ".join(
    "".join(split(w)) for w in words) == text)
print("bytes", [len(c.encode()) for c in "aéس€"])
print(len("salam".encode()), len("سلام".encode()))
# chars 23
# words ['[UNK]', '[UNK]']
# pieces un|believ|ably|token|ize|r|s
# ids [0, 1, 3, 4, 5, 24, 6]
# round trip True
# bytes [1, 2, 2, 3]
# 5 8
