<sub>[← Phase 13](../phase-13-semantic-search-and-retrieval/README.md) · [All phases](../../README.md)</sub>

# Phase 14 · AI Security & Robustness

**Sprints 42–44 of 90** · first published 7 November 2026 · archived on Zenodo, DOI [10.5281/zenodo.24142098](https://doi.org/10.5281/zenodo.24142098)

> A small change to an input, a few bad training examples, an instruction slipped into the text a model reads: three attacks, each checked on real data.

## Phase summary

<a href="MT24_Learning_Phase14_Summary.png"><img src="MT24_Learning_Phase14_Summary.png" width="760" alt="Phase 14 summary page: AI Security & Robustness, 3 sprints, with what each sprint covers, what I can now do, mistakes avoided and the phase project."></a>

**One result checked in this phase:** On 540 handwritten digits, random noise of ±2 grey levels leaves a small network at 95.4%; a chosen 10-step attack of the same size leaves 21.5%.

## Sprints

### Sprint 42/90 · Adversarial Examples: Small Changes, Wrong Answers

> *Random noise barely moves a model. A change of the same size, chosen against it, breaks it.*

<a href="MT24_Learning_Phase14_Sprint42_Adversarial_Examples_Small_Changes_Wrong_Answers.png"><img src="MT24_Learning_Phase14_Sprint42_Adversarial_Examples_Small_Changes_Wrong_Answers.png" width="760" alt="Sprint 42 of 90 infographic: Adversarial Examples: Small Changes, Wrong Answers. Random noise barely moves a model. A change of the same size, chosen against it, breaks it."></a>

**Covers.** What an adversarial example is, why noise and a chosen change differ, how many small pushes add up across many pixels, and how attacks travel between models.

**Try it.** On 540 handwritten digits, ±2 grey levels of random noise leave a small network at 95.4% and a 10-step gradient-sign attack leaves 21.5%; a linear model retrained on old attacks holds 88.5% against them and 15.9% against a fresh one.

### Sprint 43/90 · Poisoned Data: Attacks Through Training & Retrieval

> *A few planted examples can teach a model a secret password. Clean tests never type it.*

<a href="MT24_Learning_Phase14_Sprint43_Poisoned_Data_Attacks_Through_Training_Retrieval.png"><img src="MT24_Learning_Phase14_Sprint43_Poisoned_Data_Attacks_Through_Training_Retrieval.png" width="760" alt="Sprint 43 of 90 infographic: Poisoned Data: Attacks Through Training & Retrieval. A few planted examples can teach a model a secret password. Clean tests never type it."></a>

**Covers.** What data poisoning is, why a few examples can be enough, a hidden trigger that clean tests never type, and planted passages in retrieval.

**Try it.** In my own spam filter (logistic regression on real SMS messages), 40 relabelled messages (1.0% of 3,941) cut the triggered spam it catches from 87.5% to 25.4% while clean tests look normal; in a BM25 index of the Cranfield abstracts, a plant copying each question ranks first for 223 of 225 questions.

### Sprint 44/90 · Prompt Injection: When Data Becomes an Instruction

> *Roles label the rules and the attack, but the model reads both as one stream of tokens.*

<a href="MT24_Learning_Phase14_Sprint44_Prompt_Injection_When_Data_Becomes_an_Instruction.png"><img src="MT24_Learning_Phase14_Sprint44_Prompt_Injection_When_Data_Becomes_an_Instruction.png" width="760" alt="Sprint 44 of 90 infographic: Prompt Injection: When Data Becomes an Instruction. Roles label the rules and the attack, but the model reads both as one stream of tokens."></a>

**Covers.** What prompt injection is, why firm wording in the rules is no guarantee, what a phrase blocklist misses, and instructions hidden in retrieved text.

**Try it.** In 1,346 real Tensor Trust pairs where a human attack fooled at least 2 of 3 models from 2023, 72.3% of the defences had a "never / do not" rule and a blocklist of 6 known phrase patterns caught 11.9% of the attacks; no language model was run here.

## Cite this phase

```text
Tahri, M. (2026). MT24 Learning — Knowledge Sprint Series, Phase 14: AI Security & Robustness (Version 1.0) [Educational resource]. Zenodo. https://doi.org/10.5281/zenodo.24142098
```

This DOI points to version 1.0, the edition archived as first published. To cite every version of this phase, use the concept DOI [10.5281/zenodo.24142097](https://doi.org/10.5281/zenodo.24142097).

---

<sub>[← Phase 13](../phase-13-semantic-search-and-retrieval/README.md) · [All phases](../../README.md)</sub>
