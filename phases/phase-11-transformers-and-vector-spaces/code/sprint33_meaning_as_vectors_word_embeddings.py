import numpy as np, gensim.downloader as api
wv = api.load("glove-wiki-gigaword-50")  # 66 MB, once
V, w, ix = wv.vectors, wv.index_to_key, wv.key_to_index
E = V / np.linalg.norm(V, axis=1)[:, None]  # unit rows
u = lambda t: E[ix[t]]
print(len(w), "words x", E.shape[1], "numbers")
for t in ["dog", "kitten", "car", "democracy"]:  # 1
    c = u("cat") @ u(t)  # cosine as an angle
    print(f"cat-{t}: cos {c:.3f} = "
          f"{np.degrees(np.arccos(c)):.1f} deg")
P = """france paris italy rome spain madrid germany
berlin japan tokyo russia moscow greece athens egypt
cairo morocco rabat turkey ankara china beijing
poland warsaw""".split()  # 2 country -> capital
def mcos(D):  # mean cosine between the offsets
    D = D / np.linalg.norm(D, axis=1)[:, None]
    return (D @ D.T)[np.triu_indices(len(D), 1)].mean()
C = np.array([u(t) for t in P])
D = C[1::2] - C[::2]  # 12 country -> capital offsets
r = np.random.default_rng(33).integers(1000, 20000,
                                       (12, 2))
R = E[r[:, 1]] - E[r[:, 0]]  # 12 random word pairs
print(f"offsets: capitals {mcos(D):.2f}, "
      f"random pairs {mcos(R):.2f}")
def top(q, x=(), k=2):  # 3 analogy by 3CosAdd
    s = E @ q / np.linalg.norm(q)
    o = [i for i in np.argsort(-s)[:9] if w[i] not in x]
    return " ".join(f"{w[i]} {s[i]:.3f}" for i in o[:k])
for a, b, c in [("man", "king", "woman"),
                ("man", "doctor", "woman")]:
    q = u(b) - u(a) + u(c)  # x = skip the 3 inputs
    print(f"{b}: {top(q)} | skip: {top(q, {a,b,c}, 1)}")
o = np.argsort(-(E @ u("hot")))  # 4 one point per word
print("hot ->", " ".join(w[i] for i in o[1:7]))
n = list(np.argsort(-(E @ u("bank")))).index(ix["river"])
print("bank -> river is neighbour no.", n)
# Output printed on the image:
# 400000 words x 50 numbers
# cat-dog: cos 0.922 = 22.8 deg
# cat-kitten: cos 0.639 = 50.3 deg
# cat-car: cos 0.364 = 68.7 deg
# cat-democracy: cos 0.037 = 87.9 deg
# offsets: capitals 0.61, random pairs 0.02
# king: king 0.885 queen 0.852 | skip: queen 0.852
# doctor: doctor 0.905 nurse 0.840 | skip: nurse 0.840
# hot -> cool cold mix dry soft warm
# bank -> river is neighbour no. 2353
