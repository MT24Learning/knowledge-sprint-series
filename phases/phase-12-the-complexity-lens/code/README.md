# Phase 12 · Runnable code

The code printed in the Try It box of each sprint image of Phase 12, The Complexity Lens, as files you can run. Each file is copied from its image line by line and ends with the output printed on the image, as comment lines. Archived on Zenodo with the code of Phases 1–14: [10.5281/zenodo.24201674](https://doi.org/10.5281/zenodo.24201674) (all versions: [10.5281/zenodo.24201673](https://doi.org/10.5281/zenodo.24201673)).

| Sprint | File | Run with |
|---|---|---|
| 36 · Dynamics and Chaos | [`sprint36_dynamics_and_chaos.py`](sprint36_dynamics_and_chaos.py) | `.venv/bin/python sprint36_dynamics_and_chaos.py` |
| 37 · Emergence and Self-Organisation | [`sprint37_emergence_and_self_organisation.py`](sprint37_emergence_and_self_organisation.py) | `.venv/bin/python sprint37_emergence_and_self_organisation.py` |
| 38 · Fractals, Scaling and the Shape of Complexity | [`sprint38_fractals_scaling_shape_of_complexity.py`](sprint38_fractals_scaling_shape_of_complexity.py) | `.venv/bin/python sprint38_fractals_scaling_shape_of_complexity.py` |

## Run it

```sh
python3.13 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python sprint36_dynamics_and_chaos.py
```

On Windows, write `.venv\Scripts\python` in place of `.venv/bin/python`.

## Data

The data are not stored in this repository; each source keeps its own licence. Sprints 36 to 38 read five files from the folder they run in. Download them from these fixed commits and check them with `sha256sum --check data.sha256`:

- `laser_a.txt`, `laser_a_next.txt`: Santa Fe time-series competition, set A (laser) and its next 100 points, converted from `SantaFe.A.rda` and `SantaFe.A.cont.rda` in [TSPred](https://raw.githubusercontent.com/RebeccaSalles/TSPred/75d706b876dfb60ff47ab142edee2a1946d639ba/data/SantaFe.A.rda) (commit 75d706b; both files are in its `data/` folder) with the snippet below.
- `quakes.csv`: [R's quakes data set](https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/1dcc2bf5f955cc1224a3e1307256e1fe86b68dae/csv/datasets/quakes.csv), Rdatasets commit 1dcc2bf.
- `ne_10m_admin_0_countries.json`: [Natural Earth 1:10m countries](https://raw.githubusercontent.com/nvkelso/natural-earth-vector/ca96624a56bd078437bca8184e78163e5039ad19/geojson/ne_10m_admin_0_countries.geojson) (public domain), natural-earth-vector commit ca96624, saved under this name.
- `melville-moby_dick.txt`: from the [NLTK Gutenberg corpus](https://raw.githubusercontent.com/nltk/nltk_data/550b6625bcef1f2abff2ff770a5a0d272c9c6b2a/packages/corpora/gutenberg.zip) (nltk_data commit 550b662): unzip `gutenberg/melville-moby_dick.txt`.

```sh
.venv/bin/pip install pyreadr==0.5.9 pandas==3.1.1   # only for this conversion
.venv/bin/python -c "import pyreadr, numpy as np
for s, d in [('SantaFe.A.rda', 'laser_a.txt'), ('SantaFe.A.cont.rda', 'laser_a_next.txt')]:
    np.savetxt(d, next(iter(pyreadr.read_r(s).values())).iloc[:, 0].to_numpy(), fmt='%d')"
```

## Versions

First run: Python 3.13.16, numpy 2.5.3, scipy 1.18.1, powerlaw 2.0.0, pyproj 3.8.0, shapely 2.2.0. `requirements.txt` pins these versions.

Checked on 13 November 2026, in a fresh environment built from `requirements.txt`: Python 3.13.18 with the pinned versions. Every printed line matches the image.

A later version of a library may change the numbers (for example, numpy may change the random streams of `default_rng` between versions); the pinned versions reproduce the image.

## Notes

- Sprint 36 takes about 50 seconds and Sprint 37 about 2 minutes.

## Licence

The code in this folder is licensed under the [MIT License](../../../LICENSE-CODE). The images and texts of the series stay under CC BY-NC-SA 4.0 ([LICENSE](../../../LICENSE)).

[← Phase 12](../README.md)
