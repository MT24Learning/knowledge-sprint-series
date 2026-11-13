import json, re
def parse(src):      # "*" binds tighter than "+"
    toks = re.findall(r"\d+|\S", src)
    def atom():
        t = toks.pop(0)
        if t != "(": return int(t)
        e = level("+"); toks.pop(0); return e
    def level(op):
        sub = atom if op == "*" else (
            lambda: level("*"))
        e = sub()
        while toks and toks[0] == op:
            toks.pop(0); e = (op, e, sub())
        return e
    return level("+")
def ev(e):
    if isinstance(e, int): return e
    a, b = ev(e[1]), ev(e[2])
    return a + b if e[0] == "+" else a * b
t = parse("2 + 3 * 4"); print(t, ev(t))
print(ev(parse("(2 + 3) * 4")))
def trees(n):        # bracketings of n operators
    return 1 if n == 0 else sum(trees(k) *
        trees(n - 1 - k) for k in range(n))
print([trees(n) for n in range(1, 9)])
def strict(pairs):
    if len({k for k, _ in pairs}) < len(pairs):
        raise ValueError("duplicate key")
    return dict(pairs)
raw = '{"dose": 5, "dose": 50}'
print(json.loads(raw))
try: json.loads(raw, object_pairs_hook=strict)
except ValueError as e: print("rejected:", e)
# ('+', 2, ('*', 3, 4)) 14
# 20
# [1, 2, 5, 14, 42, 132, 429, 1430]
# {'dose': 50}
# rejected: duplicate key
