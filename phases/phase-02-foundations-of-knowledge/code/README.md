# Phase 2 · Runnable code

The code printed in the Try It box of each sprint image of Phase 2, Foundations of Knowledge, as files you can run. Each file is copied from its image line by line and ends with the output printed on the image, as comment lines.

| Sprint | File | Run with |
|---|---|---|
| 4 · Knowledge, Truth and Evidence | [`sprint04_knowledge_truth_evidence.py`](sprint04_knowledge_truth_evidence.py) | `.venv/bin/python sprint04_knowledge_truth_evidence.py` |
| 5 · What Is a Model? | [`sprint05_what_is_a_model.py`](sprint05_what_is_a_model.py) | `.venv/bin/python sprint05_what_is_a_model.py` |
| 6 · The Scientific Method, Objectivity and Its Failures | [`sprint06_scientific_method_objectivity_failures.py`](sprint06_scientific_method_objectivity_failures.py) | `.venv/bin/python sprint06_scientific_method_objectivity_failures.py` |
| 7 · Four Minds on Science | [`sprint07_four_minds_on_science.py`](sprint07_four_minds_on_science.py) | `.venv/bin/python sprint07_four_minds_on_science.py` |

## Run it

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python sprint04_knowledge_truth_evidence.py
```

On Windows, write `.venv\Scripts\python` in place of `.venv/bin/python`.

## Versions

First run: numpy 2.4.4 and scipy 1.17.1; the Python version was not recorded. `requirements.txt` pins these versions.

Checked on 13 November 2026, in a fresh environment built from `requirements.txt`: Python 3.11.15 with the pinned versions, and Python 3.13.18 with numpy 2.5.4 and scipy 1.18.1. Every printed line matches the image.

A later version of a library may change the numbers (for example, numpy may change the random streams of `default_rng` between versions); the pinned versions reproduce the image.

## Notes

- The comments on these images give the printed values in short form: Sprint 5 prints each angle before its ratio, Sprint 6 prints 0.64576 (0.646 on the image) and Sprint 7 prints 42.97331529555632 (42.97 on the image).
- Sprints 4 and 7 need only Python's standard library.

## Licence

The code in this folder is licensed under the [MIT License](../../../LICENSE-CODE). The images and texts of the series stay under CC BY-NC-SA 4.0 ([LICENSE](../../../LICENSE)).

[← Phase 2](../README.md)
