# Phase 13 · Runnable code

The code printed in the Try It box of each sprint image of Phase 13, Semantic Search & Retrieval, as files you can run. Each file is copied from its image line by line and ends with the output printed on the image, as comment lines.

| Sprint | File | Run with |
|---|---|---|
| 39 · Keyword Search: Inverted Index & BM25 | [`sprint39_keyword_search_inverted_index_bm25.py`](sprint39_keyword_search_inverted_index_bm25.py) | `.venv/bin/python sprint39_keyword_search_inverted_index_bm25.py` |
| 40 · Searching by Meaning: Dense & Hybrid Retrieval | [`sprint40_searching_by_meaning_dense_hybrid_retrieval.py`](sprint40_searching_by_meaning_dense_hybrid_retrieval.py) | `.venv/bin/python sprint40_searching_by_meaning_dense_hybrid_retrieval.py` |
| 41 · Retrieval-Augmented Generation: A Working Demo | [`sprint41_retrieval_augmented_generation_working_demo.py`](sprint41_retrieval_augmented_generation_working_demo.py) | `.venv/bin/python sprint41_retrieval_augmented_generation_working_demo.py` |

## Run it

```sh
python3.13 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python sprint39_keyword_search_inverted_index_bm25.py
```

On Windows, write `.venv\Scripts\python` in place of `.venv/bin/python`.

## Data

The data are not stored in this repository; each source keeps its own licence. Sprints 39 to 41 read the Cranfield collection from a `cran/` folder beside the scripts. Download `cran.all.1400`, `cran.qry` and `cranqrel` from [olivernn/cranfield](https://github.com/olivernn/cranfield/tree/8f40ee931b7e11af05b9e3c7a364a15e0ebccc4e/data/cran) (commit 8f40ee9) into `cran/` and check them with `sha256sum --check data.sha256`.

## Versions

First run: Python 3.13.17, numpy 2.5.3, scipy 1.18.1, gensim 4.4.0, wordllama 0.4.0.post1. `requirements.txt` pins these versions.

Checked on 13 November 2026, in a fresh environment built from `requirements.txt`: Python 3.13.18 with the pinned versions. Every printed line matches the image.

A later version of a library may change the numbers (for example, numpy may change the random streams of `default_rng` between versions); the pinned versions reproduce the image.

## Notes

- Sprints 40 and 41 import Sprint 39's code as `s39`: keep `s39.py` beside them and run them from this folder.
- Sprint 40 loads the WordLlama model that ships with the package (`disable_download=True`). Version 0.4.0.post1 looks for its tokenizer file in `~/.cache/wordllama/tokenizers`; copy it there once:

  ```sh
  .venv/bin/python -c "import os, shutil, wordllama; d = os.path.expanduser('~/.cache/wordllama/tokenizers'); os.makedirs(d, exist_ok=True); shutil.copy(os.path.join(os.path.dirname(wordllama.__file__), 'tokenizers', 'l2_supercat_tokenizer_config.json'), d)"
  ```
- Sprint 40 also uses the GloVe vectors of Phase 11 (downloaded through gensim on the first run).

[← Phase 13](../README.md)
