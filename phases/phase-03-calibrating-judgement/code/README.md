# Phase 3 · Runnable code

The code printed in the Try It box of each sprint image of Phase 3, Calibrating Judgement, as files you can run. Each file is copied from its image line by line and ends with the output printed on the image, as comment lines. Archived on Zenodo with the code of Phases 1–14: [10.5281/zenodo.24201674](https://doi.org/10.5281/zenodo.24201674) (all versions: [10.5281/zenodo.24201673](https://doi.org/10.5281/zenodo.24201673)).

| Sprint | File | Run with |
|---|---|---|
| 8 · Calibrating Intuition Before Automation | [`sprint08_calibrating_intuition_before_automation.py`](sprint08_calibrating_intuition_before_automation.py) | `.venv/bin/python sprint08_calibrating_intuition_before_automation.py` |

## Run it

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python sprint08_calibrating_intuition_before_automation.py
```

On Windows, write `.venv\Scripts\python` in place of `.venv/bin/python`.

## Versions

First run: numpy 2.4.4; the Python version was not recorded. `requirements.txt` pins these versions.

Checked on 13 November 2026, in a fresh environment built from `requirements.txt`: Python 3.11.15 with numpy 2.4.4, and Python 3.13.18 with numpy 2.5.4. Every printed line matches the image.

A later version of a library may change the numbers (for example, numpy may change the random streams of `default_rng` between versions); the pinned versions reproduce the image.

## Notes

- The four printed lines appear on one comment line on the image.

## Licence

The code in this folder is licensed under the [MIT License](../../../LICENSE-CODE). The images and texts of the series stay under CC BY-NC-SA 4.0 ([LICENSE](../../../LICENSE)).

[← Phase 3](../README.md)
