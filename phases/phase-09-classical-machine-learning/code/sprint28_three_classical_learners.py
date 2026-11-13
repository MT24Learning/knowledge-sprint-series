from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
X, y = load_wine(return_X_y=True)  # 3 cultivars
a, b, ya, yb = train_test_split(X, y, test_size=0.3,
                       stratify=y, random_state=28)
learners = {
    "linear": LogisticRegression(max_iter=10000),
    "tree": DecisionTreeClassifier(max_depth=3,
                                   random_state=0),
    "5-nn": KNeighborsClassifier(n_neighbors=5)}
print(len(ya), "learn wines,", len(yb), "test wines")
for cols in ([6, 12], list(range(13))):  # 6 flavanoids,
    A, B = a[:, cols], b[:, cols]       # 12 proline
    for name, m in learners.items():
        raw = m.fit(A, ya).score(B, yb)
        z = make_pipeline(StandardScaler(), m)  # z-scores
        print(len(cols), f"{name:7}{raw:.3f}",
              f"{z.fit(A, ya).score(B, yb):.3f}")
# 124 learn wines, 54 test wines
# 2 linear 0.926 0.926
# 2 tree   0.907 0.907
# 2 5-nn   0.704 0.944
# 13 linear 0.981 1.000
# 13 tree   0.870 0.870
# 13 5-nn   0.741 1.000
