<sub>[All phases](../README.md)</sub>

# How this index is built

Every page in this repository is generated. The data lives in [`series_data.py`](series_data.py); [`build.py`](build.py) turns it into the phase pages, the front page, `CITATION.cff`, `CHECKSUMS.sha256` and the gallery thumbnails. To change a page, change the data and rebuild; never edit a generated page by hand.

The same build writes the website in [`docs/`](../docs), published with GitHub Pages at [mt24learning.github.io/knowledge-sprint-series](https://mt24learning.github.io/knowledge-sprint-series/): [`website.py`](website.py) generates `docs/index.html` and copies the thumbnails into `docs/img/thumbs/`. The design files (`docs/style.css`, `docs/site.js`, `docs/fonts/` and `docs/img/brand/`) are static and edited by hand.

## Add a phase

A phase is added once all of its images are public and its edition is archived on Zenodo.

1. In `series_data.py`, add the phase to `PHASES` (title, first-published date, version and concept DOIs, one-line summary, one checked result, summary image, and one entry per sprint), then move `NEXT` to the following phase.
2. Put the phase's runnable code in `phases/<phase folder>/code/`: one file per sprint, named `sprintNN_<title>.py` (or `.sh`), each copied from its image and ending with the output printed on the image as comment lines; a `requirements.txt` with exact versions (`==`); a `README.md` with the steps, the versions of the first run and of the check, and any data sources with their SHA-256 digests (`data.sha256`). The data themselves stay out of the repository. The phase page links each sprint's files under **Run it**, and `CHECKSUMS.sha256` lists them.
3. Rebuild, pointing to the folder that holds the new images:

   ```sh
   python3 tools/build.py --images /path/to/new/images
   ```

   The images are copied into their phase folder unchanged. A published image is never overwritten.
4. Check the result:

   ```sh
   python3 tools/build.py --check
   ```

   This checks every internal link and heading anchor, every checksum (images and code), that every image is listed in the data, that a phase with a `code/` folder has a README and a file for every sprint, and `CITATION.cff` when `cffconvert` is installed.

Without write access to the repository, add `--pack update.zip` to step 3: the zip holds only the files that the build changed, at their repository paths. Files written before the build (`tools/series_data.py` and the `code/` folder) are not in it: add them to the zip at their paths.

## Requirements

Python 3.10 or later and Pillow. The "next phase" tile is rendered with Playwright and Chromium; its two fonts (Space Grotesk and JetBrains Mono, SIL Open Font License) are fetched from the Google Fonts repository on first use.
