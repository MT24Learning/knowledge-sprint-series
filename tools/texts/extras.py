"""Text of the milestone overview and the Code Availability Statement, for their website pages.

Transcribed line by line from the published images (milestones/, code-availability/). Every printed text is
word for word, except the header (series name), the footer (signature line, archive/index lines, social handles)
and the drawings (station icons, the route itself). Terminal text and digests are in `code`, as printed.
tools/pages.py (extra_page) turns this file into the pages.

Marks inside texts: **bold**, *italic*. Thousands are written with a space, as on the images (10 000).

Regions: where each part sits on the image, in pixels of the 2160 × 2700 PNG (x0, y0, x1, y1), measured on the
images. The page lights the part of the image whose text is being read.
"""

PAGES = {
    # The Road So Far · milestones/MT24_Learning_Milestone_Phases01_11.png
    # One block per stop, in route order (Phases 1–11), then the next stop and the key printed under the map.
    "phases-01-11": dict(
        type="Milestone",
        accent="#b5372e",
        gradient=["#24508f", "#6b3a72", "#c2372d", "#a8740f", "#3a3896"],
        kicker="Milestone overview · Phases 1–11 · Sprints 1–35 of 90",
        heading="The Road So Far",
        em="So Far",
        dek="Eleven phases on one line: from Git and evidence to a transformer layer built in code. Each stop "
            "carries one result I checked in code or against the sources.",
        blocks=[
            dict(key="phase-1", colour="#24508f", tag="Phase 1 · Sprints 1–3", title="Engineering Foundations",
                 text=["Git object IDs: SHA-1 by default, SHA-256 opt-in"],
                 note="DOI 10.5281/zenodo.22979790"),
            dict(key="phase-2", colour="#2f6a52", tag="Phase 2 · Sprints 4–7", title="Foundations of Knowledge",
                 text=["Positive test: 1% prior, 90% hits, 5% false alarms → 0.154"],
                 note="DOI 10.5281/zenodo.22998928"),
            dict(key="phase-3", colour="#6b3a72", tag="Phase 3 · Sprint 8", title="Calibrating Judgement",
                 text=["Brier, 10 000 simulated events: always 50% → 0.250, calibrated → 0.188", "Builds on 2"],
                 note="DOI 10.5281/zenodo.23042464"),
            dict(key="phase-4", colour="#1f7fb3", tag="Phase 4 · Sprints 9–12", title="Mathematical & Logical Foundations",
                 text=["0.1 + 0.2 == 0.3 → False: floats need a tolerance"],
                 note="DOI 10.5281/zenodo.22999436"),
            dict(key="phase-5", colour="#c2372d", tag="Phase 5 · Sprints 13–15", title="Statistics & Experimental Design",
                 text=["*d* = 0.5 needs 64 per group for 80% power at α = 0.05"],
                 note="DOI 10.5281/zenodo.23063053"),
            dict(key="phase-6", colour="#a8740f", tag="Phase 6 · Sprints 16–18", title="How Paradigms Die",
                 text=["Small-angle pendulum: within 1% up to 22°, 18% off at 90°", "Builds on 2"],
                 note="DOI 10.5281/zenodo.23084198"),
            dict(key="phase-7", colour="#13706e", tag="Phase 7 · Sprints 19–21", title="Data Skepticism & Evaluation Data",
                 text=["1-NN, 5 copies per item: split by row 1.000, by group 0.440 (chance 0.5)", "Builds on 1"],
                 note="DOI 10.5281/zenodo.23189539"),
            dict(key="phase-8", colour="#b5652a", tag="Phase 8 · Sprints 22–25", title="Tokenization & Parsing",
                 text=["2 + 3 * 4: one string, two trees, 14 or 20; the grammar picks 14", "Builds on 1"],
                 note="DOI 10.5281/zenodo.23213765"),
            dict(key="phase-9", colour="#4d7a43", tag="Phase 9 · Sprints 26–30", title="Classical Machine Learning",
                 text=["Is it a 9? Always “no”: accuracy 0.900, balanced 0.500", "Builds on 5 · 7"],
                 note="DOI 10.5281/zenodo.23240712"),
            dict(key="phase-10", colour="#2b2d33", tag="Phase 10 · Sprints 31–32", title="Neural Networks",
                 text=["XOR, 2-2-1 sigmoid net: 77 of 100 seeds solve it; with 4 hidden units, 100", "Builds on 4 · 9"],
                 note="DOI 10.5281/zenodo.23343237"),
            dict(key="phase-11", colour="#3a3896", tag="Phase 11 · Sprints 33–35", title="Transformers & Vector Spaces",
                 text=["GloVe: king − man + woman → king (0.885); queen (0.852) only if the inputs are skipped",
                       "Builds on 4 · 8 · 10"],
                 note="DOI · Coming soon"),
            dict(key="next", tag="Next", title="Phase 12", text=["*The Complexity Lens*"]),
            dict(key="legend",
                 text=["Each segment takes the colour of the phase it leads into. Circled numbers mark the earlier phases a phase builds on. Each result is taken from its "
                       "sprint image, where it was checked in code or against the sources; DOIs are the archived "
                       "versions on Zenodo."]),
        ],
        regions={
            "head": (40, 50, 2120, 372),
            "phase-1": (74, 434, 525, 832), "phase-2": (560, 434, 1011, 832), "phase-3": (1046, 434, 1497, 832),
            "phase-4": (1532, 434, 1983, 832),
            "phase-8": (74, 1010, 525, 1408), "phase-7": (560, 1010, 1011, 1408), "phase-6": (1046, 1010, 1497, 1408),
            "phase-5": (1532, 1010, 1983, 1408),
            "phase-9": (74, 1586, 525, 1984), "phase-10": (560, 1586, 1011, 1984), "phase-11": (1046, 1586, 1497, 1984),
            "next": (1530, 1985, 2000, 2130), "legend": (56, 2160, 2110, 2252),
        },
    ),
    # Code Availability Statement · code-availability/MT24_Learning_Code_Availability_Statement_Phases_01_14.png
    # One block per panel, in reading order. `badges` holds the two lines of the "44" badge and the names line.
    "code-01-14": dict(
        type="Code statement",
        accent="#51d5a7",
        gradient=["#51d5a7", "#71b9fa"],
        kicker="Code availability statement · Phases 1–14 · Sprints 1–44 of 90",
        heading="The code of 44 sprints, pinned, run and archived",
        em="pinned",
        dek="Same code is not enough. The same built file also needs the same tool versions, so every folder pins "
            "the packages it uses.",
        badges=["44 of 44 run", "13 Nov 2026", "PyPA · pip · NumPy · Sandve et al."],
        fig=dict(
            label="Fig. 1",
            title="One source, two tool versions · Sprint 25’s wheel, built twice with each · SHA-256 as an 8 × 8 "
                  "square",
            panels=[
                ("Sprint 25’s wheel, built twice with each", [
                    "hatchling 1.32.4 · build 1 · 06334646fb0ae368… · **917 B**",
                    "= hatchling 1.32.4 · build 2 · 06334646fb0ae368… · **917 B**",
                    "NOT THE SAME",
                    "hatchling 1.33.0 · build 1 · 5620af12e1711f04… · **913 B**",
                    "= hatchling 1.33.0 · build 2 · 5620af12e1711f04… · **913 B**",
                    "*One cell per hex digit of the SHA-256 (0 dark → f bright). Same version, same square, to the "
                    "bit. Hatchling 1.32.4 was current when Sprint 25 was posted (3 Oct 2026); 1.33.0 came out on "
                    "28 Oct 2026.*",
                ]),
                ("Inside the wheel · `toytok-0.1.0.dist-info/WHEEL`", [
                    "Wheel-Version: 1.0",
                    "- Generator: hatchling 1.32.4",
                    "+ Generator: hatchling 1.33.0",
                    "Root-Is-Purelib: true",
                    "Tag: py3-none-any",
                    "One line differs. RECORD changes with it, because it lists the SHA-256 of WHEEL. Compressed, "
                    "WHEEL loses 1 byte and RECORD 3.",
                    "Check: (86 - 85) + (204 - 201) = 4 = 917 - 913",
                ]),
            ],
        ),
        blocks=[
            dict(key="try", title="Try It · Bash · Python 3.11.15",
                 tag="Run on 13 Nov 2026 · Output as printed",
                 code="$ git clone -q https://github.com/MT24Learning/knowledge-sprint-series\n"
                      "$ cd knowledge-sprint-series/phases/phase-08-tokenization-and-parsing/code\n"
                      "$ python3.11 -m venv .venv && . .venv/bin/activate\n"
                      "$ pip install -q -r requirements.txt\n"
                      "$ mkdir pinned latest && S=../sprint25_publishing_a_package.py\n"
                      "$ cd pinned && PIP_CONSTRAINT=../constraints.txt python $S | sed -n 1,3p\n"
                      "1 06334646fb0ae368\n"
                      "2 06334646fb0ae368\n"
                      "toytok-0.1.0-py3-none-any.whl 917\n"
                      "$ cd ../latest && python $S | sed -n 1,3p\n"
                      "1 5620af12e1711f04\n"
                      "2 5620af12e1711f04\n"
                      "toytok-0.1.0-py3-none-any.whl 913\n"
                      "$ unzip -p toytok/dist/*.whl '*/WHEEL' | grep Generator\n"
                      "Generator: hatchling 1.33.0"),
            dict(key="availability", title="Code Availability", tag="What · Where · On which terms", items=[
                "**What** One file per sprint: **41 Python programs**, copied line by line from the images and "
                "ending with their printed output as comments, and **3 shell scripts** of Phase 1’s commands. Each "
                "phase folder pins its packages to exact versions in requirements.txt and says how to run it.",
                "**Where** Browse: phases/…/code/ in the GitHub index. Cite: the Zenodo software record "
                "10.5281/zenodo.24201674, linked to all 14 phase records.",
                "**Terms** Code: **MIT License**. Images and texts: **CC BY-NC-SA 4.0**.",
            ], note="Springer Nature’s code policy asks what, where and on which terms, and calls a GitHub link alone "
                    "insufficient: it assigns no permanent identifier. The DOI does."),
            dict(key="01", title="01 · Popular claim, tested", tag="Holds only with the same tool versions",
                 text=["*~~“Same code, same result.”~~*",
                       "Sprint 25’s code, built on 13 Nov 2026 without its pin, gives a different wheel: **913 B**, "
                       "not the **917 B** on the image. Two builds with one version agree to the bit."],
                 note="Reproducible Builds counts the build environment as an input; hatchling builds reproducibly "
                      "by default."),
            dict(key="02", title="02 · Bridge · The pin has a version too",
                 text=["Since pip 26.2, PIP_CONSTRAINT no longer reaches pip’s own build environments. With pip 26.3 "
                       "and one pin file, pip wheel built with hatchling **1.33.0** under PIP_CONSTRAINT and "
                       "**1.32.4** under PIP_BUILD_CONSTRAINT; python -m build (1.6.1) still applied PIP_CONSTRAINT.",
                       "NumPy too: NEP 19 lets Generator streams change between releases, so every folder using NumPy "
                       "pins it."],
                 note="Pinning is not proof. Read the Generator line of what you built."),
            dict(key="03", title="03 · Rerun from the pins", tag="13 Nov 2026",
                 text=["Sprints 1–3 purple · 4–11 blue · 12 amber · 13 blue · 14 green · 15 blue · 16–44 green"],
                 items=[
                     "**30** print exactly the lines on their images",
                     "**10** print the same values, given in short form on the image",
                     "**1** property test reports its pictured failing example",
                     "**3** command scripts run to the end",
                 ], note="Fresh environments · Python 3.11.15 (Phases 1–8), 3.13.18 (9–14)"),
            dict(key="mini", title="Mini Project",
                 text=["Pick any phase folder and follow its README. Run one sprint’s file and compare your output "
                       "with the comment lines at its end. Then loosen one pin and see what moves."]),
        ],
        references=[
            ("Reproducible Builds, “Definitions”: same source code, build environment and build instructions "
             "*(reproducible-builds.org)*", "https://reproducible-builds.org/docs/definition/"),
            ("Sandve, Nekrutenko, Taylor & Hovig (2013). Ten Simple Rules for Reproducible Computational Research. "
             "*PLoS Comput Biol 9(10), e1003285*", "https://doi.org/10.1371/journal.pcbi.1003285"),
            ("NumPy, NEP 19 — Random number generator policy (R. Kern)",
             "https://numpy.org/neps/nep-0019-rng-policy.html"),
            ("PyPA, Binary distribution format (WHEEL, RECORD)",
             "https://packaging.python.org/en/latest/specifications/binary-distribution-format/"),
            ("pip 26.2 release notes (29 Jul 2026) and pip User Guide, “Constraints files”",
             "https://pip.pypa.io/en/stable/news/"),
            ("Hatch, build configuration (reproducible)", "https://hatch.pypa.io/latest/config/build/"),
            ("Springer Nature, Code policy", "https://www.springernature.com/gp/open-science/code-policy"),
            ("Open Source Initiative, The MIT License", "https://opensource.org/license/mit"),
            ("Creative Commons, CC BY-NC-SA 4.0", "https://creativecommons.org/licenses/by-nc-sa/4.0/"),
        ],
        regions={
            "head": (50, 300, 2110, 560), "fig": (56, 580, 2104, 1099),
            "try": (56, 1125, 1263, 1629), "availability": (1285, 1125, 2104, 1629),
            "01": (60, 1655, 712, 2047), "02": (736, 1655, 1388, 2047), "03": (1412, 1655, 2100, 2047),
            "mini": (56, 2073, 716, 2271), "references": (732, 2073, 2104, 2271),
        },
    ),
}
