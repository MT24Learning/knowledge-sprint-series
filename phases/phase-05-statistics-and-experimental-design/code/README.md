# Phase 5 · Runnable code

The code printed in the Try It box of each sprint image of Phase 5, Statistics & Experimental Design, as files you can run. Each file is copied from its image line by line and ends with the output printed on the image, as comment lines.

| Sprint | File | Run with |
|---|---|---|
| 13 · Probability & Distributions | [`sprint13_probability_distributions.py`](sprint13_probability_distributions.py) | `.venv/bin/python sprint13_probability_distributions.py` |
| 14 · Hypothesis Testing, Power & Sample Size | [`sprint14_hypothesis_testing_power_sample_size.py`](sprint14_hypothesis_testing_power_sample_size.py) | `.venv/bin/python sprint14_hypothesis_testing_power_sample_size.py` |
| 15 · Experimental Design & Rigorous Inference | [`sprint15_experimental_design_rigorous_inference.py`](sprint15_experimental_design_rigorous_inference.py) | `.venv/bin/python sprint15_experimental_design_rigorous_inference.py` |

## Run it

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python sprint13_probability_distributions.py
```

On Windows, write `.venv\Scripts\python` in place of `.venv/bin/python`.

## Versions

First run: numpy 2.4.4 and scipy 1.17.1 (Sprint 13 and 14); the Python version was not recorded. `requirements.txt` pins these versions.

Checked on 13 November 2026, in a fresh environment built from `requirements.txt`: Python 3.11.15 with the pinned versions, and Python 3.13.18 with numpy 2.5.4 and scipy 1.18.1. Every printed line matches the image.

A later version of a library may change the numbers (for example, numpy may change the random streams of `default_rng` between versions); the pinned versions reproduce the image.

## Notes

- Sprint 13 draws the exponential sample before the Cauchy sample from one generator: the order matters for the numbers.

[← Phase 5](../README.md)
