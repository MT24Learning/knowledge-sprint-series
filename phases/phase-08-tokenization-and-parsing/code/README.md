# Phase 8 · Runnable code

The code printed in the Try It box of each sprint image of Phase 8, Tokenization & Parsing, as files you can run. Each file is copied from its image line by line and ends with the output printed on the image, as comment lines. Archived on Zenodo with the code of Phases 1–14: [10.5281/zenodo.24201674](https://doi.org/10.5281/zenodo.24201674) (all versions: [10.5281/zenodo.24201673](https://doi.org/10.5281/zenodo.24201673)).

| Sprint | File | Run with |
|---|---|---|
| 22 · How Tokenization Works | [`sprint22_how_tokenization_works.py`](sprint22_how_tokenization_works.py) | `.venv/bin/python sprint22_how_tokenization_works.py` |
| 23 · Byte Pair Encoding & Its Edge Cases | [`sprint23_byte_pair_encoding_edge_cases.py`](sprint23_byte_pair_encoding_edge_cases.py) | `.venv/bin/python sprint23_byte_pair_encoding_edge_cases.py` |
| 24 · Parsing Structured Meaning from Text | [`sprint24_parsing_structured_meaning_from_text.py`](sprint24_parsing_structured_meaning_from_text.py) | `.venv/bin/python sprint24_parsing_structured_meaning_from_text.py` |
| 25 · Publishing a Package | [`sprint25_publishing_a_package.py`](sprint25_publishing_a_package.py) | from an empty folder, see Notes |

## Run it

```sh
python3.11 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python sprint22_how_tokenization_works.py
```

On Windows, write `.venv\Scripts\python` in place of `.venv/bin/python`.

## Versions

First run: Python 3.11.15; Sprint 25 with hatchling 1.32.4, build 1.6.1 and packaging 26.1 (as printed on the image). `requirements.txt` pins these versions.

Checked on 13 November 2026, in a fresh environment built from `requirements.txt`: Python 3.11.15 with the pinned versions. Every printed line matches the image.

## Notes

- Sprints 22 to 24 need only Python's standard library.
- Sprint 25 builds a wheel in an isolated environment that downloads hatchling. Pin it with the constraint file, and run it from an empty scratch folder, because the script creates `toytok/` there and stops if it already exists:

  ```sh
  mkdir run && cd run
  PIP_CONSTRAINT=../constraints.txt ../.venv/bin/python ../sprint25_publishing_a_package.py
  ```
- Without the pin, hatchling 1.33.0 (the newest on 13 November 2026) builds a wheel of 913 bytes whose SHA-256 starts 5620af12e1711f04, not the 917 bytes and 06334646fb0ae368 on the image. Both runs still agree with each other: the build is reproducible for one tool version, and the version is part of the result.
- `PIP_CONSTRAINT` works here because the script builds with `python -m build` (checked with build 1.6.1 and pip 26.3). If you build the same package with `pip wheel` or `pip install` instead, pip 26.2 and later no longer apply `PIP_CONSTRAINT` to their own build environments: use `PIP_BUILD_CONSTRAINT=../constraints.txt`. Checked on 13 November 2026 with pip 26.3: `pip wheel` built with hatchling 1.33.0 (913 bytes) under `PIP_CONSTRAINT` and with hatchling 1.32.4 (917 bytes) under `PIP_BUILD_CONSTRAINT`. Whichever way you build, the `Generator:` line in the wheel's `WHEEL` file names the hatchling version that was used.

## Licence

The code in this folder is licensed under the [MIT License](../../../LICENSE-CODE). The images and texts of the series stay under CC BY-NC-SA 4.0 ([LICENSE](../../../LICENSE)).

[← Phase 8](../README.md)
