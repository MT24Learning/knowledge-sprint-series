# Phase 15 · Runnable code

The code printed in the Try It box of each sprint image of Phase 15, Structured Claims & Ground Truth, as files you can run. Each file is the script whose output is printed on its image and ends with that output, as comment lines. Archived on Zenodo in the Phase 15 record, with the phase PDF: [10.5281/zenodo.24387974](https://doi.org/10.5281/zenodo.24387974) (all versions: [10.5281/zenodo.24387973](https://doi.org/10.5281/zenodo.24387973)).

| Sprint | File | Run with |
|---|---|---|
| 45 · Representing a Claim: From Sentence to Structure | [`sprint45_representing_a_claim_from_sentence_to_structure.py`](sprint45_representing_a_claim_from_sentence_to_structure.py) | `.venv/bin/python sprint45_representing_a_claim_from_sentence_to_structure.py` |
| 46 · Ground Truth Is a Human Judgement: Measuring Agreement | [`sprint46_ground_truth_is_a_human_judgement_measuring_agreement.py`](sprint46_ground_truth_is_a_human_judgement_measuring_agreement.py) | `.venv/bin/python sprint46_ground_truth_is_a_human_judgement_measuring_agreement.py` |
| 47 · Checking a Claim Against Evidence | [`sprint47_checking_a_claim_against_evidence.py`](sprint47_checking_a_claim_against_evidence.py) | `.venv/bin/python sprint47_checking_a_claim_against_evidence.py` |
| 48 · Building a Verified Reference Set | [`sprint48_building_a_verified_reference_set.py`](sprint48_building_a_verified_reference_set.py) | `.venv/bin/python sprint48_building_a_verified_reference_set.py` |

## Run it

```sh
python3.13 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python sprint45_representing_a_claim_from_sentence_to_structure.py
```

On Windows, write `.venv\Scripts\python` in place of `.venv/bin/python`.

## Data

The data are not stored in this repository; each source keeps its own terms. The scripts read their data from the folder they run in. Download these files and check them with `sha256sum --check data.sha256`:

- `climate-fever.jsonl`: [CLIMATE-FEVER](https://raw.githubusercontent.com/tdiggelm/climate-fever-dataset/03de61617b10a5c1935f8e08bb0e8ac1ee775356/dataset/climate-fever.jsonl) (Diggelmann et al. 2020, arXiv 2012.00614), commit 03de616: 1 535 claims · 7 675 claim–sentence pairs with their votes. Sprints 45, 46 and 47.
- The Mechanical Turk results of [cleanlab/label-errors](https://github.com/cleanlab/label-errors) (Northcutt, Athalye & Mueller 2021), commit 6d5d6b3, Apache License 2.0: [`mnist_mturk.json`](https://raw.githubusercontent.com/cleanlab/label-errors/6d5d6b31a13216290afc40e5c6319399c4d15c06/mturk/mnist_mturk.json) · [`cifar10_mturk.json`](https://raw.githubusercontent.com/cleanlab/label-errors/6d5d6b31a13216290afc40e5c6319399c4d15c06/mturk/cifar10_mturk.json) · [`cifar100_mturk.json`](https://raw.githubusercontent.com/cleanlab/label-errors/6d5d6b31a13216290afc40e5c6319399c4d15c06/mturk/cifar100_mturk.json) · [`caltech256_mturk.json`](https://raw.githubusercontent.com/cleanlab/label-errors/6d5d6b31a13216290afc40e5c6319399c4d15c06/mturk/caltech256_mturk.json) · [`imagenet_mturk.json`](https://raw.githubusercontent.com/cleanlab/label-errors/6d5d6b31a13216290afc40e5c6319399c4d15c06/mturk/imagenet_mturk.json) · [`quickdraw_mturk.json`](https://raw.githubusercontent.com/cleanlab/label-errors/6d5d6b31a13216290afc40e5c6319399c4d15c06/mturk/quickdraw_mturk.json) · [`20news_mturk.json`](https://raw.githubusercontent.com/cleanlab/label-errors/6d5d6b31a13216290afc40e5c6319399c4d15c06/mturk/20news_mturk.json) · [`imdb_mturk.json`](https://raw.githubusercontent.com/cleanlab/label-errors/6d5d6b31a13216290afc40e5c6319399c4d15c06/mturk/imdb_mturk.json) · [`amazon_mturk.json`](https://raw.githubusercontent.com/cleanlab/label-errors/6d5d6b31a13216290afc40e5c6319399c4d15c06/mturk/amazon_mturk.json). Sprint 48.

## Versions

First run: Python 3.13.18, numpy 2.5.3, scipy 1.18.1, scikit-learn 1.9.1. `requirements.txt` pins these versions. Sprints 45, 46 and 48 need only Python's standard library; Sprint 47 uses numpy, scipy and scikit-learn.

Checked on 20 November 2026, in a fresh environment built from `requirements.txt`: Python 3.13.18 with the pinned versions. Every printed line matches the image.

A later version of a library may change the numbers; the pinned versions reproduce the image.

## Notes

- Sprint 47 takes about 30 seconds: it trains 4 × 5 + 2 × 2 × 5 = 40 logistic regressions.
- Sprint 48's test-set sizes come from the released label files of cleanlab/label-errors (`original_test_labels/`); QuickDraw and Amazon have only a checked sample, so their shares are estimates; AudioSet's 1.35% is the paper's own figure, because the paper does not state its rule for clips with several labels.

## Licence

The code in this folder is licensed under the [MIT License](../../../LICENSE-CODE). The images and texts of the series stay under CC BY-NC-SA 4.0 ([LICENSE](../../../LICENSE)).

[← Phase 15](../README.md)
