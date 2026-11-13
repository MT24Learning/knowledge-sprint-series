# Phase 4 · Runnable code

The code printed in the Try It box of each sprint image of Phase 4, Mathematical & Logical Foundations, as files you can run. Each file is copied from its image line by line and ends with the output printed on the image, as comment lines. Archived on Zenodo with the code of Phases 1–14: [10.5281/zenodo.24201674](https://doi.org/10.5281/zenodo.24201674) (all versions: [10.5281/zenodo.24201673](https://doi.org/10.5281/zenodo.24201673)).

| Sprint | File | Run with |
|---|---|---|
| 9 · Linear Algebra & Calculus for Machine Learning | [`sprint09_linear_algebra_calculus_for_ml.py`](sprint09_linear_algebra_calculus_for_ml.py) | `.venv/bin/python sprint09_linear_algebra_calculus_for_ml.py` |
| 10 · Logic, Propositions & Inference | [`sprint10_logic_propositions_inference.py`](sprint10_logic_propositions_inference.py) | `.venv/bin/python sprint10_logic_propositions_inference.py` |
| 11 · Axioms & Declared Assumptions | [`sprint11_axioms_declared_assumptions.py`](sprint11_axioms_declared_assumptions.py) | `.venv/bin/python sprint11_axioms_declared_assumptions.py` |
| 12 · Testing & Phase Review | [`sprint12_testing_phase_review.py`](sprint12_testing_phase_review.py) | `.venv/bin/python -m pytest sprint12_testing_phase_review.py` |

## Run it

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python sprint09_linear_algebra_calculus_for_ml.py
```

On Windows, write `.venv\Scripts\python` in place of `.venv/bin/python`.

## Versions

First run: numpy 2.4.4 and Hypothesis 6.168.1; the Python version was not recorded. `requirements.txt` pins these versions.

Checked on 13 November 2026, in a fresh environment built from `requirements.txt`: Python 3.11.15 and 3.13.18 with the pinned versions. Every value on the image is reproduced; the image's comments give the printed output in short form (several lines on one line, rounded values or added notes).

A later version of a library may change the numbers (for example, numpy may change the random streams of `default_rng` between versions); the pinned versions reproduce the image.

## Notes

- Sprint 12 is a test file: run it with `.venv/bin/python -m pytest sprint12_testing_phase_review.py`. `test_exact` fails and `test_close` passes; Hypothesis 6.168.1 reports the failing example a=3.033889997114584, b=0.99999, c=1.0. Another Hypothesis version may report a different example (the failure itself does not change).
- Hypothesis writes a `.hypothesis/` folder where it runs; delete it afterwards.

## Licence

The code in this folder is licensed under the [MIT License](../../../LICENSE-CODE). The images and texts of the series stay under CC BY-NC-SA 4.0 ([LICENSE](../../../LICENSE)).

[← Phase 4](../README.md)
