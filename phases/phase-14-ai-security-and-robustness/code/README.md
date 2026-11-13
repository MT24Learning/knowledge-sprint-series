# Phase 14 · Runnable code

The code printed in the Try It box of each sprint image of Phase 14, AI Security & Robustness, as files you can run. Each file is copied from its image line by line and ends with the output printed on the image, as comment lines.

| Sprint | File | Run with |
|---|---|---|
| 42 · Adversarial Examples: Small Changes, Wrong Answers | [`sprint42_adversarial_examples_small_changes_wrong_answers.py`](sprint42_adversarial_examples_small_changes_wrong_answers.py) | `.venv/bin/python sprint42_adversarial_examples_small_changes_wrong_answers.py` |
| 43 · Poisoned Data: Attacks Through Training & Retrieval | [`sprint43_poisoned_data_attacks_through_training_retrieval.py`](sprint43_poisoned_data_attacks_through_training_retrieval.py) | `.venv/bin/python sprint43_poisoned_data_attacks_through_training_retrieval.py` |
| 44 · Prompt Injection: When Data Becomes an Instruction | [`sprint44_prompt_injection_when_data_becomes_an_instruction.py`](sprint44_prompt_injection_when_data_becomes_an_instruction.py) | `.venv/bin/python sprint44_prompt_injection_when_data_becomes_an_instruction.py` |

## Run it

```sh
python3.13 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python sprint42_adversarial_examples_small_changes_wrong_answers.py
```

On Windows, write `.venv\Scripts\python` in place of `.venv/bin/python`.

## Data

The data are not stored in this repository; each source keeps its own licence. The scripts read their data from the folder they run in. Download these files and check them with `sha256sum --check data.sha256`:

- `sms.tsv`: [SMS Spam Collection](https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/5339710562cc46c4a32a369d63f1e8751a18a54e/data/sms.tsv) (Almeida & Hidalgo, UCI), mirror commit 5339710: 5 574 messages, 747 spam.
- `cran.all.1400`, `cran.qry`: the Cranfield files of Phase 13, placed beside the scripts (not in a `cran/` folder).
- `hijacking_robustness_dataset.jsonl`, `extraction_robustness_dataset.jsonl`: the Tensor Trust hijacking and extraction files (v1) in [HumanCompatibleAI/tensor-trust-data](https://github.com/HumanCompatibleAI/tensor-trust-data) (commit 747a75e); search the repository for the two file names.

## Versions

First run: Python 3.13.18, numpy 2.5.3, scikit-learn 1.9.1. `requirements.txt` pins these versions.

Checked on 13 November 2026, in a fresh environment built from `requirements.txt`: Python 3.13.18 with the pinned versions. Every printed line matches the image.

A later version of a library may change the numbers (for example, numpy may change the random streams of `default_rng` between versions); the pinned versions reproduce the image.

## Notes

- Sprint 44 needs only Python's standard library.

## Licence

The code in this folder is licensed under the [MIT License](../../../LICENSE-CODE). The images and texts of the series stay under CC BY-NC-SA 4.0 ([LICENSE](../../../LICENSE)).

[← Phase 14](../README.md)
