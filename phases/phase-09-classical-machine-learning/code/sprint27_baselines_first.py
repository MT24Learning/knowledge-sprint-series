import numpy as np
from sklearn import datasets, dummy, metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
_, y = datasets.load_iris(return_X_y=True)  # Sprint 26
y = y[y > 0][np.random.default_rng(26).permutation(100)]
tr, te = np.bincount(y[:70])[1:], np.bincount(y[70:])[1:]
print(tr, te, f"{te[tr.argmax()] / 30:.3f}")  # majority

D, d = datasets.load_digits(return_X_y=True)
y9 = (d == 9) * 1                            # is it a 9?
a, b, ya, yb = train_test_split(D, y9, test_size=0.3,
                                stratify=y9, random_state=27)
acc = lambda t, p: (t == p).mean()
bal = metrics.balanced_accuracy_score  # mean recall
no = dummy.DummyClassifier(strategy="most_frequent")
p = {"no": no.fit(a, ya).predict(b)}
for score in (acc, bal):                     # 1R-style rule
    fc = [(f, c) for f in range(64) for c in range(17)]
    f, c = max(fc, key=lambda k:
               score(ya, (a[:, k[0]] > k[1]) * 1))
    p[f"px{f}>{c}"] = (b[:, f] > c) * 1
lr = LogisticRegression(max_iter=5000)
p["logistic"] = lr.fit(a, ya).predict(b)
print(len(yb), "test images,", yb.sum(), "nines")
for k, q in p.items():
    print(f"{k:9}{acc(yb, q):.3f}", f"{bal(yb, q):.3f}",
          q.sum())
# [40 30] [10 20] 0.333
# 540 test images, 54 nines
# no       0.900 0.500 0
# px38>12  0.894 0.505 5
# px29>11  0.759 0.809 170
# logistic 0.983 0.941 51
