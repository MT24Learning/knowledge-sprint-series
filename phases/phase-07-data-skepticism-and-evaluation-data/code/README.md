# Phase 7 · Runnable code

The code printed in the Try It box of each sprint image of Phase 7, Data Skepticism & Evaluation Data, as files you can run. Each file is copied from its image line by line and ends with the output printed on the image, as comment lines.

| Sprint | File | Run with |
|---|---|---|
| 19 · Data Pipelines: Extract, Transform, Load | [`sprint19_data_pipelines_extract_transform_load.py`](sprint19_data_pipelines_extract_transform_load.py) | `.venv/bin/python sprint19_data_pipelines_extract_transform_load.py` |
| 20 · Building an Evaluation Dataset | [`sprint20_building_an_evaluation_dataset.py`](sprint20_building_an_evaluation_dataset.py) | `.venv/bin/python sprint20_building_an_evaluation_dataset.py` |
| 21 · Data Validation & Storage | [`sprint21_data_validation_and_storage.py`](sprint21_data_validation_and_storage.py) | `.venv/bin/python sprint21_data_validation_and_storage.py` |

## Run it

```sh
python3.11 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python sprint19_data_pipelines_extract_transform_load.py
```

On Windows, write `.venv\Scripts\python` in place of `.venv/bin/python`.

## Versions

First run: Python 3.11.15, numpy 2.4.4, SQLite 3.45.1 (as printed on the images). `requirements.txt` pins these versions.

Checked on 13 November 2026, in a fresh environment built from `requirements.txt`: Python 3.11.15 with numpy 2.4.4 and SQLite 3.53.1. Every printed line matches the image.

A later version of a library may change the numbers (for example, numpy may change the random streams of `default_rng` between versions); the pinned versions reproduce the image.

## Notes

- Sprint 21's STRICT table needs SQLite 3.37.0 or later (`python -c "import sqlite3; print(sqlite3.sqlite_version)"`).
- Sprint 21 writes `g.tmp` and `g.csv` in the folder it runs in: run it in a scratch folder.

## Licence

The code in this folder is licensed under the [MIT License](../../../LICENSE-CODE). The images and texts of the series stay under CC BY-NC-SA 4.0 ([LICENSE](../../../LICENSE)).

[← Phase 7](../README.md)
