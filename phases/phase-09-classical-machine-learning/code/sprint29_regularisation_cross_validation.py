from sklearn import preprocessing as pp
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold, cross_validate
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
X, y = load_diabetes(return_X_y=True)   # 442 patients
a, b, ya, yb = train_test_split(X, y, test_size=0.3,
                                random_state=29)
folds = KFold(5, shuffle=True, random_state=29)
model = lambda alpha: make_pipeline(    # 65 terms:
    pp.PolynomialFeatures(2, include_bias=False),
    pp.StandardScaler(), Ridge(alpha))  # squares, pairs
rows = []                   # alpha, train, cv, se
for alpha in [10 ** (k / 2) for k in range(-6, 9)]:
    r = cross_validate(model(alpha), a, ya, cv=folds,
            scoring="neg_mean_squared_error",
            return_train_score=True)
    cv = -r["test_score"]               # 5 fold MSEs
    rows.append((alpha, -r["train_score"].mean(),
                 cv.mean(), cv.std(ddof=1) / 5**0.5))
best = min(rows, key=lambda r: r[2])
limit = best[2] + best[3]               # 1-SE rule
one_se = max(r for r in rows if r[2] <= limit)
print(len(ya), "learn,", len(yb), "test; MSE:")
for alpha, tr, cv, se in (rows[0], best, one_se):
    m = model(alpha).fit(a, ya)               # refit
    test = ((m.predict(b) - yb) ** 2).mean()  # sealed
    print(f"{alpha:8.3f} train {tr:4.0f} cv {cv:4.0f}",
          f"±{se:3.0f} test {test:4.0f}")
# 309 learn, 133 test; MSE:
#    0.001 train 2037 cv 4027 ±412 test 4140
#   31.623 train 2232 cv 3047 ±203 test 3760
#  100.000 train 2404 cv 3062 ±121 test 3717
