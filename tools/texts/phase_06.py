"""Text of the Phase 6 images, for the website's sprint and phase pages.

Transcribed line by line from the published images (phases/phase-06-how-paradigms-die/).
Card texts, notes, check lines, the summary's tiles and boxes and the source lines are word for word;
the figure panels are read in words from their labels (fig.panels), with the printed captions in
italics. The code of each Try It box is not repeated here: the pages show the sprint's file from
code/, which ends with the printed output. tools/website.py turns this file into the pages.

Marks inside texts: **bold**, *italic*. Thousands are written with a space, as on the images
(100 000); the pages keep each group together with a no-break space.

Regions: where each part sits on the image, in pixels of the 2160 × 2700 PNG (x0, y0, x1, y1),
measured on the images. The page lights the part of the image whose text is being read.
"""

PHASE = dict(
    n=6,
    accents={16: "#c8391f", 17: "#c8391f", 18: "#c8391f"},
    regions={
        "head": (56, 320, 2104, 588), "fig": (56, 592, 2104, 1124),
        "01": (56, 1148, 688, 1517), "02": (720, 1148, 1352, 1517),
        "03": (56, 1528, 688, 1897), "04": (720, 1528, 1352, 1897),
        "06": (56, 1908, 688, 2290), "07": (720, 1908, 1352, 2290),
        "05": (1384, 1148, 2104, 1918), "R": (1384, 1918, 2104, 2290),
    },
    summary_regions={
        "head": (40, 40, 1340, 700), "figure": (1370, 270, 2140, 730),
        "tile-0": (78, 798, 550, 1250), "tile-1": (590, 798, 1060, 1250), "tile-2": (1100, 798, 1572, 1250),
        "tile-3": (1612, 798, 2082, 1250),
        "block-0": (78, 1286, 550, 1738), "block-1": (590, 1286, 1060, 1738), "block-2": (1100, 1286, 1572, 1738),
        "references": (1612, 1286, 2082, 1738),
        "block-3": (78, 1774, 550, 2214), "next": (590, 1774, 2082, 2214),
    },
)

SPRINTS = {
    16: dict(
        em="Paradigm",
        names="Kuhn · Wegener · Vine · Planck",
        fig=dict(
            label="Fig. 1",
            panels=[
                ("One shift, dated · continental drift → plate tectonics", [
                    "1912 Wegener: continents move · fossils match across oceans",
                    "1930 Wegener dies · drift still rejected",
                    "mid-1950s: stripes mapped",
                    "1962–63 Hess; Vine & Matthews · spreading reads the stripes",
                    "1968 drilling",
                    "fixed → ① rival rejected → ② anomalies pile up → ③ crisis → ④ plates, on a time axis from 1910 to 1970",
                    "56 years from 1912 to 1968 · the last 5 years marked at the end",
                    "*Fig. 1* — Dates from the USGS (*This Dynamic Earth*) and the primary papers. Proposal to drilling "
                    "proof: 1968 − 1912 = 56 years. Acceptance came in the last 5 (1963 to 1968): slow, then sudden.",
                ]),
            ],
            notes=[
                ("1912–1930 · A rival", "Drift fit the fossils but had no force able to move continents."),
                ("`1950s` · Anomalies", "Magnetic stripes on the sea floor, unexplained by fixed continents."),
                ("1961–63 · A mechanism", "Sea-floor spreading plus field reversals reads the stripes."),
                ("1966–68 · New normal", "Plate tectonics; ocean drilling confirms."),
            ],
        ),
        cards=[
            dict(no="01", title="Normal Science", items=[
                "Puzzle-solving inside a shared paradigm",
                "Two senses (Postscript, 1970): **exemplars** and a **disciplinary matrix**",
            ], note="Masterman (1970) counted 21 senses of “paradigm” in the 1962 book. Kuhn narrowed it."),
            dict(no="02", title="Anomaly & Crisis", items=[
                "Anomalies are shelved, not fatal",
                "Crisis: they pile up and resist the best work",
            ], note="Kuhn: to reject a paradigm with no substitute is to reject science itself. A rival must exist first."),
            dict(no="03", title="Revolution", items=[
                "The rival changes the problems, methods and standards",
                "Incommensurable ≠ incomparable",
            ], note="Three kinds: method, observation, meaning. Later Kuhn: “local”, a few terms that do not translate."),
            dict(no="04", title="Planck's Principle", items=[
                "Planck (1950): truth wins as opponents die out",
                "Tests on Darwin's reception: little support",
            ], note="Azoulay et al. (2019): after 452 star life scientists died, outsiders' papers rose 8.6%. Normal science."),
            dict(no="06", title="General Notes", items=[
                "Wegener's critics had a point",
                "An anomaly needs a rival to bite",
                "Not every change is a revolution",
                "Date the anomaly, rival and test",
            ]),
            dict(no="07", title="Mini Project", items=[
                "Pick a shift: oxygen over phlogiston",
                "Draw its Fig. 1: anomaly, rival, test",
                "Rerun the code with seeds 1–5",
                "Set teach = 0.9: what changes?",
            ]),
        ],
        tryit=dict(check="A simulation, not data. Check for c = 0: 0.55 × (29/30)ᵗ = 0.10 at t = 50.3, so **year 51**."),
        sources=[
            ("Kuhn (1962; 1970). *The Structure of Scientific Revolutions*. U. Chicago Press",
             "https://www.press.uchicago.edu/ucp/books/book/chicago/S/bo13179781.html"),
            ("Bird. *Thomas Kuhn*. Stanford Encyclopedia of Philosophy", "https://plato.stanford.edu/entries/thomas-kuhn/"),
            ("Vine & Matthews (1963). Nature 199", "https://doi.org/10.1038/199947a0"),
            ("Hess (1962)", "https://doi.org/10.1130/Petrologic.1962.599"),
            ("USGS", "https://doi.org/10.3133/7000097"),
            ("Oreskes (1999). *The Rejection of Continental Drift*. OUP",
             "https://doi.org/10.1093/oso/9780195117325.001.0001"),
            ("Azoulay et al. (2019). AER 109(8)", "https://doi.org/10.1257/aer.20161574"),
            ("Hull et al. (1978). Science 202", "https://doi.org/10.1126/science.202.4369.717"),
        ],
    ),

    17: dict(
        regions={"05": (1384, 1148, 2104, 1920), "R": (1384, 1940, 2104, 2290)},
        em="Failure",
        names="Box · Goodhart · Dalal · Lazer",
        fig=dict(
            label="Fig. 1",
            panels=[
                ("Six places a model can fail · each with its own test", [
                    "columns: class · symptom · test that catches it · dated case",
                    "① Data · Input is wrong · Check units at every hand-off · Mars Climate Orbiter, 1999: lbf·s read as N·s",
                    "② Structure · Residuals show a pattern · Plot residuals; push past the idealization · "
                    "Small-angle pendulum at 90°: period off by 18%",
                    "③ Fit · Train and test disagree · Score on data the model never saw · "
                    "Code below, degree 9: **0.073** train, **0.41** new points",
                    "④ Shift · Error grows over time · Re-score on fresh data, on a schedule · "
                    "Google Flu Trends, Feb 2013: over twice the CDC's share",
                    "⑤ Range · Used beyond its data · Compare inputs to the training range · "
                    "Challenger, 1986: 31°F; coldest earlier launch 53°F",
                    "⑥ Core · Anomaly survives every fix · A rival that explains it · "
                    "Mercury's extra 43″/century: Newton → Einstein",
                    "*Fig. 1* — The first five can be fixed inside the model; the sixth needs a new one (Sprint 16). "
                    "Cases from the NASA board report, Lazer et al. (2014), Dalal et al. (1989), Sprints 5 and 7.",
                ]),
            ],
        ),
        cards=[
            dict(no="01", title="Name It First", items=[
                "Six classes: data, structure, fit, shift, range, core",
                "Each has its own symptom and its own test",
            ], note="Box (1976): it is “inappropriate to be concerned about mice when there are tigers abroad.”"),
            dict(no="02", title="Under & Overfit", items=[
                "Too simple: high error everywhere (d = 1)",
                "Too flexible: training error falls, new-data error rises (d = 9)",
            ], note="Held-out data catches it. Training error never will."),
            dict(no="03", title="Out of Range", items=[
                "Past x = 3 the degree-9 error jumps from 0.41 to 482",
                "Challenger: 31°F, far below every earlier launch",
            ], note="The pre-launch chart also left out the flights with no O-ring trouble (Dalal et al., 1989)."),
            dict(no="04", title="Tied, Then Split", items=[
                "Many models tie on the test set, then differ in use (D'Amour et al., 2022)",
                "Goodhart (1975): a rule used for control tends to collapse",
            ], note="One good test score is one draw, not a guarantee."),
            dict(no="06", title="General Notes", items=[
                "Name the class before the fix",
                "One failure can hide another",
                "Test on data the model never saw",
                "Log the date and the conditions",
            ]),
            dict(no="07", title="Mini Project", items=[
                "Rerun with degrees 1 to 12",
                "Plot the three errors against degree",
                "Shrink the outside range to 3–3.5",
                "Classify one failure you have seen",
            ]),
        ],
        tryit=dict(check="Columns: degree, train, inside, outside (RMSE). Degree 9: 482.043 ÷ 0.41 ≈ **1 176×** worse outside."),
        sources=[
            ("Box (1976). Science and Statistics. JASA 71(356)", "https://doi.org/10.1080/01621459.1976.10480949"),
            ("NASA MCO Mishap Investigation Board (1999). Phase I Report",
             "https://llis.nasa.gov/llis_lib/pdf/1009464main1_0641-mr.pdf"),
            ("Dalal, Fowlkes & Hoadley (1989). JASA 84(408)", "https://doi.org/10.1080/01621459.1989.10478858"),
            ("Lazer et al. (2014). The Parable of Google Flu. Science 343", "https://doi.org/10.1126/science.1248506"),
            ("D'Amour et al. (2022). JMLR 23(226)", "https://jmlr.org/papers/v23/20-1335.html"),
            ("Goodhart (1975)", "https://doi.org/10.1007/978-1-349-17295-5_4"),
        ],
    ),

    18: dict(
        regions={
            "fig": (56, 592, 2104, 1144),
            "01": (56, 1168, 688, 1533), "02": (720, 1168, 1352, 1533),
            "03": (56, 1544, 688, 1905), "04": (720, 1544, 1352, 1905),
            "06": (56, 1916, 688, 2290), "07": (720, 1916, 1352, 2290),
            "05": (1384, 1168, 2104, 1896), "R": (1384, 1916, 2104, 2290),
        },
        em="Failed",
        names="Feynman · Rosenthal · Mitchell · Gebru",
        fig=dict(
            label="Fig. 1",
            title="One failure, written down · the pendulum from Sprint 5",
            panels=[
                ("Failure record · N° 18 · 30 Sep 2026 · M. Tahri", [
                    "Model · Pendulum period T = 2π√(L/g)",
                    "Claim · The period does not depend on the swing",
                    "Tested · Release angles 1° to 90° against the exact period",
                    "Failure · At 90° the true period is **1.18 ×** the model's",
                    "Class · ② Structure: it assumes sin θ ≈ θ (Sprint 17)",
                    "Still holds · Within **1%** up to **22°**; within **5%** up to **50°**",
                    "Use instead · Exact elliptic-integral period past 22°",
                    "Evidence · Code 05 · numpy 2.4.4 · scipy 1.17.1",
                ]),
                ("Exact period ÷ model, by release angle", [
                    "the curve rises from 1.00 at 0° to 1.18 at 90° · axes 1.00 to 1.20 and 0° to 90°",
                    "dashed lines at 1% and 5%",
                    "① 22° ② 50° ③ 90°: 1.18",
                    "*Fig. 1* — Exact period ÷ model, by release angle. Check: 1 + θ²/16 = 1.01 at θ = 0.4 rad = 22.9°; "
                    "exact crossing 22.8°.",
                ]),
            ],
        ),
        cards=[
            dict(no="01", title="A Blameless Record", items=[
                "Impact, actions, root causes, follow-ups",
                "Causes, not culprits",
            ], note="Google SRE, ch. 15: set the criteria for writing one before anything fails."),
            dict(no="02", title="Draw the Boundary", items=[
                "Say where it still holds, not only where it broke",
                "Pendulum: 1% up to 22°, 5% up to 50°",
            ], note="Model cards (2019) and datasheets (2021) state intended use and the conditions tested."),
            dict(no="03", title="Nature Can't Be Fooled", items=[
                "Shuttle loss odds: about 1 in 100 (engineers) to 1 in 100 000 (management)",
            ], note="Feynman (1986): “reality must take precedence over public relations, for nature cannot be fooled.”"),
            dict(no="04", title="The File Drawer", items=[
                "Failures left unwritten bias what others read",
                "Rosenthal (1979): journals hold the 5% of chance hits, drawers the 95% of nulls",
            ], note="His extreme case, not a measured share."),
            dict(no="06", title="General Notes", items=[
                "Write it the day it fails",
                "Numbers, dates, versions, seed",
                "Name the class (Sprint 17)",
                "Record what still holds",
            ]),
            dict(no="07", title="Mini Project", items=[
                "Write a record for Sprint 17's degree-9 fit",
                "Fill all eight fields of Fig. 1",
                "Find where its error passes 0.1",
                "Have a friend review it, blamelessly",
            ]),
        ],
        tryit=dict(check="Exact 1% edge: 22.8°, so the last whole degree is **22**."),
        sources=[
            ("Lunney & Lueder (2016). Postmortem Culture. Ch. 15 in Beyer et al., *Site Reliability Engineering*. O'Reilly",
             "https://sre.google/sre-book/postmortem-culture/"),
            ("Feynman (1986). Appendix F, Rogers Commission Report", "https://www.nasa.gov/history/rogersrep/v2appf.htm"),
            ("Rosenthal (1979). Psych. Bull. 86(3), 638–641", "https://doi.org/10.1037/0033-2909.86.3.638"),
            ("Mitchell et al. (2019). Model Cards. FAT*", "https://doi.org/10.1145/3287560.3287596"),
            ("Gebru et al. (2021). CACM 64(12)", "https://doi.org/10.1145/3458723"),
        ],
    ),
}

SUMMARY = dict(
    style="catalog",
    kicker="Phase 6 · Summary · Sprints 16–18 of 90",
    em="Paradigms",
    sub="how models fail, and how to write it down",
    dek="A dated shift, six failure classes and one failure record: "
        "three sprints on how ideas break, every number rerun in code.",
    badges=["3 sprints, 3 code runs", "Verified sources", "One phase project"],
    figure=dict(lines=[
        "a window with a curve that stays low past a green dot, crosses a dashed line and climbs to a red dot, "
        "above a bar in grey, gold, blue, red and green",
        "labels: Anomaly · Rival · Failure Class · Record",
    ]),
    tiles=[
        dict(colour="#a8740f", sprint=16, title="Paradigm Shift",
             text="Drift: 56 years from proposal to proof, yet most minds changed in the last 5.", tag="Sprint 16"),
        dict(colour="#23508e", sprint=16, title="A Rival First",
             text="Turnover alone: the rival reached 50% in year 51. Some persuasion: 12 to 20.", tag="Sprint 16"),
        dict(colour="#6a3f78", sprint=17, title="Failure Classes",
             text="Degree 9: 0.073 on training, 0.41 on new points, 482 past the data.", tag="Sprint 17"),
        dict(colour="#c8391f", sprint=18, title="Failure Record",
             text="Pendulum: 1.18× at 90°, yet within 1% up to 22°. The record keeps both.", tag="Sprint 18"),
    ],
    blocks=[
        dict(title="Now I Can", colour="#4d3a7a", text="Date a shift, name the class of a failure, write its record with a boundary.",
             tag="Outcome"),
        dict(title="Mistakes Avoided", colour="#c43c35",
             text="Planck's line as a law, training error as proof, Rosenthal's 95% as data.", tag="Lessons"),
        dict(title="Habits Kept", colour="#1f7069", text="Test on unseen data. Record what still holds. Causes, not culprits.",
             tag="Practice"),
        dict(title="Phase Project", colour="#23508e",
             text="Pick one model I rely on: date its anomalies, classify each failure, write its record."),
    ],
    references_title="Trusted Sources",
    references=[
        ("Kuhn 1962", "https://www.press.uchicago.edu/ucp/books/book/chicago/S/bo13179781.html"),
        ("Vine & Matthews 1963", "https://doi.org/10.1038/199947a0"),
        ("Dalal et al. 1989", "https://doi.org/10.1080/01621459.1989.10478858"),
        ("Lazer et al. 2014", "https://doi.org/10.1126/science.1248506"),
        ("Feynman 1986", "https://www.nasa.gov/history/rogersrep/v2appf.htm"),
        ("Rosenthal 1979", "https://doi.org/10.1037/0033-2909.86.3.638"),
    ],
    next_issue=("Next · Phase 7", "Data Skepticism & Evaluation Data", "From failures to data."),
)
