<sub>[All phases](../README.md)</sub>

# How this index is built

Every page in this repository is generated. The data lives in [`series_data.py`](series_data.py); [`build.py`](build.py) turns it into the phase pages, the front page, `CITATION.cff`, `CHECKSUMS.sha256` and the gallery thumbnails. To change a page, change the data and rebuild; never edit a generated page by hand.

The same build writes the website in [`docs/`](../docs), published with GitHub Pages at [mt24learning.github.io/knowledge-sprint-series](https://mt24learning.github.io/knowledge-sprint-series/): [`website.py`](website.py) generates `docs/index.html` and copies the thumbnails into `docs/img/thumbs/`. The design files (`docs/style.css`, `docs/site.js`, `docs/fonts/` and `docs/img/brand/`) are static and edited by hand.

## Add a phase

A phase is added once all of its images are public and its edition is archived on Zenodo.

1. In `series_data.py`, add the phase to `PHASES` (title, first-published date, version and concept DOIs, one-line summary, one checked result, summary image, and one entry per sprint), then move `NEXT` to the following phase.
2. Put the phase's runnable code in `phases/<phase folder>/code/`: one file per sprint, named `sprintNN_<title>.py` (or `.sh`), each copied from its image and ending with the output printed on the image as comment lines; a `requirements.txt` with exact versions (`==`); a `README.md` with the steps, the versions of the first run and of the check, and any data sources with their SHA-256 digests (`data.sha256`). The data themselves stay out of the repository. The code is licensed under the MIT License (`LICENSE-CODE`), and the README ends with the same Licence section as the other phases. The phase page links each sprint's files under **Run it**, and `CHECKSUMS.sha256` lists them.
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

## Text pages on the website

The website can carry the whole text of each image, one page per sprint and one per phase summary, so the series can be read, searched and quoted. A phase gets these pages once [`texts/phase_NN.py`](texts/phase_14.py) exists; until then the site links to its page on GitHub. [`pages.py`](pages.py) builds them on every run of `build.py`, together with the search page, `docs/sitemap.xml`, `docs/404.html`, the page images (`docs/img/pages/`), the social preview cards (`docs/img/social/`) and the search index (`docs/pagefind/`, rebuilt from scratch with [Pagefind](https://pagefind.app/)). None of these is edited by hand.

Every phase from 1 to 15 has its texts, and so do the milestone overview and the Code Availability Statement ([`texts/extras.py`](texts/extras.py)). Phases 1–10 use the catalog summary (`style="catalog"`: tiles, blocks, Trusted Sources) and Phases 11–20 the journal front page (`style="journal"`). To add a phase's text, write `texts/phase_NN.py` on the model of the phase with the same layout (Phase 14 for a journal summary):

1. Transcribe every card, note, check line, version line and source of each sprint image word for word, and every section of the summary. Read the figure panels in words from their labels, with the printed captions in italics; a panel states only what its image shows. The code is not copied: the page shows the sprint's file from `code/`, split into the code and the output printed after it.
   Mark bold and italic inside running text with `**…**` and `*…*`; write a line break printed on the image as `\n`; an italic subtitle above a summary's paragraph goes in `sub`, small printed labels in `badges`.
2. Give each source and reference an `https` link to the cited work (a DOI where there is one), checked against the work's own record.
3. Measure the regions: where each part sits on the 2160 × 2700 image, in pixels. The page lights the part of the image whose text is being read.
4. Rebuild and run `build.py --check`, which also checks that each phase with texts has all its pages and images, that its sprints match `series_data.py` and that every source has an `https` link.

## Requirements

Python 3.10 or later, Pillow, and Pagefind for the site search (`pip install 'pagefind[bin]==1.6.0'`). The icons are inlined from [Bootstrap Icons](https://icons.getbootstrap.com/) (MIT, [`icons.py`](icons.py); licence in `docs/licenses/bootstrap-icons.txt`). The "next phase" tile is rendered with Playwright and Chromium; its two fonts (Space Grotesk and JetBrains Mono, SIL Open Font License) are fetched from the Google Fonts repository on first use.
