import hashlib, os, sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE loose(score REAL)")
db.execute("CREATE TABLE tight(score REAL"
    " CHECK(score BETWEEN 0 AND 1)) STRICT")
for v in (0.91, "n/a", 1.7):
    for t in ("loose", "tight"):
        try:
            db.execute(f"INSERT INTO {t}"
                       " VALUES (?)", (v,))
        except sqlite3.IntegrityError as e:
            print(t, v, "->", str(e)[:23])
print(db.execute("SELECT typeof(score),"
    " COUNT(*) FROM loose GROUP BY 1")
    .fetchall())
data = b"id,gene,score\n1,TP53,0.91\n"
with open("g.tmp", "wb") as f:
    f.write(data); f.flush()
    os.fsync(f.fileno())
os.replace("g.tmp", "g.csv")       # atomic
sha = lambda b: hashlib.sha256(b).hexdigest()
print(sha(open("g.csv", "rb").read())[:16])
print(sha(data.replace(b"91", b"19"))[:16])
# tight n/a -> cannot store TEXT value
# tight 1.7 -> CHECK constraint failed
# [('real', 2), ('text', 1)]
# 43fff0852dd0b5f8
# 339535b668796221
