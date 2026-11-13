#!/bin/sh
# Sprint 3 · the Try It commands printed on the image, run on the layout
# shown on the image (my-project/ with pyproject.toml, README.md, src/mypkg/
# and tests/). Needs pip, ruff, mypy and pytest on the PATH.
# Run: sh sprint03_project_structure_quality_gates.sh  (it works in a new folder, sprint03-run/)
set -e                          # not on the image: stop at the first error
mkdir sprint03-run                                              # setup (not on the image)
cd sprint03-run                                                 # setup (not on the image)
mkdir -p my-project/src/mypkg my-project/tests                  # setup (not on the image)
cd my-project                                                   # setup (not on the image)
# setup (not on the image): the small project of the image's Project Layout box
cat > pyproject.toml <<'TOML'
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mypkg"
version = "0.1.0"
requires-python = ">=3.10"
TOML
echo "# mypkg" > README.md
printf 'def add(a: int, b: int) -> int:\n    return a + b\n' > src/mypkg/__init__.py
printf 'from mypkg import add\n\n\ndef test_add() -> None:\n    assert add(2, 3) == 5\n' > tests/test_add.py
# the image's commands start here
pip install -e .
ruff format --check .
ruff check .
mypy src
pytest
