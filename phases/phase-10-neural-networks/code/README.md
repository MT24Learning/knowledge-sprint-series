# Phase 10 · Runnable code

The code printed in the Try It box of each sprint image of Phase 10, Neural Networks, as files you can run. Each file is copied from its image line by line and ends with the output printed on the image, as comment lines.

| Sprint | File | Run with |
|---|---|---|
| 31 · From Perceptron to Multilayer Network | [`sprint31_from_perceptron_to_multilayer_network.py`](sprint31_from_perceptron_to_multilayer_network.py) | `.venv/bin/python sprint31_from_perceptron_to_multilayer_network.py` |
| 32 · How Networks Train: Backpropagation & Training Dynamics | [`sprint32_how_networks_train.py`](sprint32_how_networks_train.py) | `.venv/bin/python sprint32_how_networks_train.py` |

## Run it

```sh
python3.13 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python sprint31_from_perceptron_to_multilayer_network.py
```

On Windows, write `.venv\Scripts\python` in place of `.venv/bin/python`.

## Versions

First run: Python 3.13.15, numpy 2.5.3, scikit-learn 1.9.1 (make_moons in Sprint 32). `requirements.txt` pins these versions.

Checked on 13 November 2026, in a fresh environment built from `requirements.txt`: Python 3.13.18 with the pinned versions. Every printed line matches the image.

A later version of a library may change the numbers (for example, numpy may change the random streams of `default_rng` between versions); the pinned versions reproduce the image.

## Notes

- Sprint 31 takes about 25 seconds (200 trainings of 5 000 steps), Sprint 32 about 30 seconds.

[← Phase 10](../README.md)
