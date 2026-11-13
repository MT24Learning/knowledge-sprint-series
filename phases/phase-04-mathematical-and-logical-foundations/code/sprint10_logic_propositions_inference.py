from itertools import product
rows = [*product([0, 1], repeat=2)]
P = lambda p, q: p
Q = lambda p, q: q
N = lambda f: (lambda *r: not f(*r))
def valid(f, c):  # premises: p→q, f
    return all(c(p, q) for p, q in
               rows if (not p or q)
               and f(p, q))
print(valid(P, Q), valid(N(Q), N(P)))
print(valid(Q, P), valid(N(P), N(Q)))
# True True   (MP, MT: valid)
# False False (AC, DA: invalid)
