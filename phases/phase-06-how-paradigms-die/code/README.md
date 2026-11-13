# Phase 6 · Runnable code

The code printed in the Try It box of each sprint image of Phase 6, How Paradigms Die, as files you can run. Each file is copied from its image line by line and ends with the output printed on the image, as comment lines.

| Sprint | File | Run with |
|---|---|---|
| 16 · Anatomy of a Paradigm Shift | [`sprint16_anatomy_of_a_paradigm_shift.py`](sprint16_anatomy_of_a_paradigm_shift.py) | `.venv/bin/python sprint16_anatomy_of_a_paradigm_shift.py` |
| 17 · A Taxonomy of Model Failure | [`sprint17_taxonomy_of_model_failure.py`](sprint17_taxonomy_of_model_failure.py) | `.venv/bin/python sprint17_taxonomy_of_model_failure.py` |
| 18 · Documenting How a Model Failed | [`sprint18_documenting_how_a_model_failed.py`](sprint18_documenting_how_a_model_failed.py) | `.venv/bin/python sprint18_documenting_how_a_model_failed.py` |

## Run it

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python sprint16_anatomy_of_a_paradigm_shift.py
```

On Windows, write `.venv\Scripts\python` in place of `.venv/bin/python`.

## Versions

First run: numpy 2.4.4 and scipy 1.17.1; the Python version was not recorded. `requirements.txt` pins these versions.

Checked on 13 November 2026, in a fresh environment built from `requirements.txt`: Python 3.11.15 with the pinned versions, and Python 3.13.18 with numpy 2.5.4 and scipy 1.18.1. Every printed line matches the image.

A later version of a library may change the numbers (for example, numpy may change the random streams of `default_rng` between versions); the pinned versions reproduce the image.

## Licence

The code in this folder is licensed under the [MIT License](../../../LICENSE-CODE). The images and texts of the series stay under CC BY-NC-SA 4.0 ([LICENSE](../../../LICENSE)).

[← Phase 6](../README.md)
