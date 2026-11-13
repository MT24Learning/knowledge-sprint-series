# Phase 11 · Runnable code

The code printed in the Try It box of each sprint image of Phase 11, Transformers & Vector Spaces, as files you can run. Each file is copied from its image line by line and ends with the output printed on the image, as comment lines.

| Sprint | File | Run with |
|---|---|---|
| 33 · Meaning as Vectors: Word Embeddings | [`sprint33_meaning_as_vectors_word_embeddings.py`](sprint33_meaning_as_vectors_word_embeddings.py) | `.venv/bin/python sprint33_meaning_as_vectors_word_embeddings.py` |
| 34 · How Attention Works | [`sprint34_how_attention_works.py`](sprint34_how_attention_works.py) | `.venv/bin/python sprint34_how_attention_works.py` |
| 35 · Inside a Transformer | [`sprint35_inside_a_transformer.py`](sprint35_inside_a_transformer.py) | `.venv/bin/python sprint35_inside_a_transformer.py` |

## Run it

```sh
python3.13 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python sprint33_meaning_as_vectors_word_embeddings.py
```

On Windows, write `.venv\Scripts\python` in place of `.venv/bin/python`.

## Versions

First run: Python 3.13.16, numpy 2.5.3, scipy 1.18.1, gensim 4.4.0. `requirements.txt` pins these versions.

Checked on 13 November 2026, in a fresh environment built from `requirements.txt`: Python 3.13.18 with the pinned versions. Every printed line matches the image.

A later version of a library may change the numbers (for example, numpy may change the random streams of `default_rng` between versions); the pinned versions reproduce the image.

## Notes

- The first run downloads the GloVe vectors glove-wiki-gigaword-50 (66 MB, PDDL licence) through gensim into `~/gensim-data`; later runs read them from there.

## Licence

The code in this folder is licensed under the [MIT License](../../../LICENSE-CODE). The images and texts of the series stay under CC BY-NC-SA 4.0 ([LICENSE](../../../LICENSE)).

[← Phase 11](../README.md)
