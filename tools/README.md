<sub>[All phases](../README.md)</sub>

# How this index is built

Every page in this repository is generated. The data lives in [`series_data.py`](series_data.py); [`build.py`](build.py) turns it into the phase pages, the front page, `CITATION.cff`, `CHECKSUMS.sha256` and the gallery thumbnails. To change a page, change the data and rebuild; never edit a generated page by hand.

## Add a phase

A phase is added once all of its images are public and its edition is archived on Zenodo.

1. In `series_data.py`, add the phase to `PHASES` (title, first-published date, version and concept DOIs, one-line summary, one checked result, summary image, and one entry per sprint), then move `NEXT` to the following phase.
2. Rebuild, pointing to the folder that holds the new images:

   ```sh
   python3 tools/build.py --images /path/to/new/images
   ```

   The images are copied into their phase folder unchanged. A published image is never overwritten.
3. Check the result:

   ```sh
   python3 tools/build.py --check
   ```

   This checks every internal link and heading anchor, every checksum, that every image is listed in the data, and `CITATION.cff` when `cffconvert` is installed.

Without write access to the repository, add `--pack update.zip` to step 2: the zip holds only the files that changed, at their repository paths, ready to upload.

## Requirements

Python 3.10 or later and Pillow. The "next phase" tile is rendered with Playwright and Chromium; its two fonts (Space Grotesk and JetBrains Mono, SIL Open Font License) are fetched from the Google Fonts repository on first use.
