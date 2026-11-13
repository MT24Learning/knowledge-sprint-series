# Phase 9 · Runnable code

The code printed in the Try It box of each sprint image of Phase 9, Classical Machine Learning, as files you can run. Each file is copied from its image line by line and ends with the output printed on the image, as comment lines.

| Sprint | File | Run with |
|---|---|---|
| 26 · Supervised Learning: From Examples to a Rule | [`sprint26_supervised_learning_from_examples_to_a_rule.py`](sprint26_supervised_learning_from_examples_to_a_rule.py) | `.venv/bin/python sprint26_supervised_learning_from_examples_to_a_rule.py` |
| 27 · Baselines First | [`sprint27_baselines_first.py`](sprint27_baselines_first.py) | `.venv/bin/python sprint27_baselines_first.py` |
| 28 · Three Classical Learners: Linear, Tree & Neighbours | [`sprint28_three_classical_learners.py`](sprint28_three_classical_learners.py) | `.venv/bin/python sprint28_three_classical_learners.py` |
| 29 · Regularisation & Cross-Validation | [`sprint29_regularisation_cross_validation.py`](sprint29_regularisation_cross_validation.py) | `.venv/bin/python sprint29_regularisation_cross_validation.py` |
| 30 · Statistical Learning Theory: Why Learning Generalises | [`sprint30_statistical_learning_theory.py`](sprint30_statistical_learning_theory.py) | `.venv/bin/python sprint30_statistical_learning_theory.py` |

## Run it

```sh
python3.13 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python sprint26_supervised_learning_from_examples_to_a_rule.py
```

On Windows, write `.venv\Scripts\python` in place of `.venv/bin/python`.

## Versions

First run: Python 3.13.15, numpy 2.5.3, scipy 1.18.1, scikit-learn 1.9.1. `requirements.txt` pins these versions.

Checked on 13 November 2026, in a fresh environment built from `requirements.txt`: Python 3.13.18 with the pinned versions. Every printed line matches the image.

A later version of a library may change the numbers (for example, numpy may change the random streams of `default_rng` between versions); the pinned versions reproduce the image.

## Notes

- The datasets (iris, digits, wine, diabetes) ship with scikit-learn: no download.

## Licence

The code in this folder is licensed under the [MIT License](../../../LICENSE-CODE). The images and texts of the series stay under CC BY-NC-SA 4.0 ([LICENSE](../../../LICENSE)).

[← Phase 9](../README.md)
