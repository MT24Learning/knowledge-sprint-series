import hashlib, pathlib, subprocess, sys
from zipfile import ZipFile
from packaging.version import Version as V
p = pathlib.Path("toytok")
(p / "src/toytok").mkdir(parents=True)
(p / "pyproject.toml").write_text("""\
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
[project]
name = "toytok"
version = "0.1.0"
requires-python = ">=3.9"
""")
(p / "src/toytok/__init__.py").write_text(
    '__version__ = "0.1.0"\n')
dist = p / "dist"
for run in (1, 2):                # build twice
    subprocess.run([sys.executable, "-m",
        "build", str(p)], capture_output=True)
    whl = next(dist.glob("*.whl"))
    h = hashlib.sha256(whl.read_bytes())
    print(run, h.hexdigest()[:16])
for f in sorted(dist.iterdir()):
    print(f.name, f.stat().st_size)
print([n.split("/")[-1] for n in
       ZipFile(whl).namelist()])
print("1.10" > "1.9", V("1.10") > V("1.9"))
vs = ["1.0", "1.0rc1", "1.0.post1", "1.0a2"]
print(sorted(vs, key=V))
# 1 06334646fb0ae368
# 2 06334646fb0ae368
# toytok-0.1.0-py3-none-any.whl 917
# toytok-0.1.0.tar.gz 336
# ['__init__.py', 'METADATA', 'WHEEL', 'RECORD']
# False True
# ['1.0a2', '1.0rc1', '1.0', '1.0.post1']
