import csv, re, sqlite3
RAW = """1,TP53,0.91
2,SEPT2,0.40
2,SEPT2,0.40
3,1-Mar,0.77
4,BRCA1,n/a
5,EGFR,0.63"""
LOAD = ("INSERT OR REPLACE INTO g"
        " VALUES (?,?,?)")
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE g(id INTEGER"
           " PRIMARY KEY, gene, score)")
def run():
    rows = [*csv.reader(RAW.split())]   # E
    ok, bad = {}, []
    for i, gene, s in rows:             # T
        try:
            if re.match(r"\d+-", gene):
                raise ValueError(gene)
            ok[i] = int(i), gene, float(s)
        except ValueError: bad.append(i)
    db.executemany(LOAD, ok.values())   # L
    n, = db.execute("SELECT COUNT(*) FROM g"
                    ).fetchone()
    print(len(rows), len(ok), bad, n)
run(); run()
# 6 3 ['3', '4'] 3
# 6 3 ['3', '4'] 3
