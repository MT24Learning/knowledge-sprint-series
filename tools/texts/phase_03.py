"""Text of the Phase 3 images, for the website's sprint and phase pages.

Transcribed line by line from the published images (phases/phase-03-calibrating-judgement/).
Card texts, notes and the source lines are word for word; the figure panels are read in words from
their labels (fig.panels), with the printed captions in italics. The code of the Try It box is not
repeated here: the page shows the sprint's file from code/, which ends with the printed output.
tools/website.py turns this file into the pages.

Marks inside texts: **bold**, *italic*. Numbers are written as on the images (this phase prints
10,000 with a comma).

Regions: where each part sits on the image, in pixels of the 2160 × 2700 PNG (x0, y0, x1, y1),
measured on the images. The page lights the part of the image whose text is being read.
"""

PHASE = dict(
    n=3,
    accents={8: "#b3452e"},
    regions={},
    summary_regions={
        "head": (60, 70, 1260, 760), "figure": (1385, 245, 2090, 765),
        "tile-0": (75, 787, 549, 1286), "tile-1": (587, 787, 1061, 1286), "tile-2": (1099, 787, 1573, 1286),
        "tile-3": (1611, 787, 2085, 1286),
        "block-0": (75, 1327, 549, 1826), "block-1": (587, 1327, 1061, 1826), "block-2": (1099, 1327, 1573, 1826),
        "references": (1611, 1327, 2085, 1826), "block-3": (75, 1867, 549, 2326), "next": (588, 1867, 2084, 2326),
    },
)

SPRINTS = {
    8: dict(
        regions={
            "head": (52, 332, 2108, 590), "fig": (52, 604, 1419, 1091), "04": (1444, 604, 2107, 1091),
            "01": (52, 1116, 715, 1587), "02": (740, 1116, 1419, 1587), "03": (1444, 1116, 2107, 1587),
            "05": (52, 1612, 715, 2059), "06": (740, 1612, 1419, 2059), "07": (1444, 1612, 2107, 2059),
            "R": (52, 2084, 2107, 2303),
        },
        em="Intuition",
        names="Brier · Lichtenstein · Kahneman · Meehl",
        fig=dict(
            label="Fig. 1",
            caption="Same knowledge, two voices. The loud one ranks events just as well, yet pays for its extra "
                  "confidence.",
            panels=[
                ("On the line = calibrated", [
                    "*came true* (0 to 1) against *stated chance* (0 to 1); dashed diagonal: on the line = calibrated",
                    "honest forecaster (green dots): close to the line",
                    "overconfident forecaster (orange line): above the line at low stated chances, below it at high ones",
                    "says 96%, right 84%",
                ]),
                ("Brier score · lower is better", [
                    "*same 10,000 events, three forecasters*",
                    "0.250 · *always 50%*",
                    "0.188 · *honest*",
                    "0.203 · *overconfident*",
                    "each gauge runs from 0 to .30",
                ]),
            ],
        ),
        cards=[
            dict(no="01", title="Calibration", items=[
                "Of all my 70% calls, about 70% should come true",
                "Brier score: mean of (forecast − outcome)²; 0 is perfect",
            ], note="Calibration alone is not enough: always quoting the base rate is calibrated and useless "
                    "(Murphy, 1973)."),
            dict(no="02", title="Overconfidence", items=[
                "Asked for 98% ranges, people missed the truth about 40% of the time, not 2%",
                "Harder questions, bigger gap",
            ], note="Feedback helps: most of the gain came after the first feedback, and it transferred only partly."),
            dict(no="03", title="Trusting a Gut", items=[
                "A regular, predictable environment",
                "Long practice with fast, clear feedback",
            ], note="Kahneman & Klein (2009): confidence alone is not evidence of skill. **Keep:** ask where my "
                    "feedback comes from."),
            dict(no="05", title="Head vs Formula", items=[
                "136 studies: formulas 10% more accurate on average",
                "Humans clearly better in only 6–16%",
            ], note="Machines too: modern neural nets are often poorly calibrated (Guo et al., 2017)."),
            dict(no="06", title="Calibration Hygiene", items=[
                "Write a number, not \"probably\"",
                "Log it before the outcome",
                "Beat 0.25, the always-50% score",
                "Automate only what beats me",
            ]),
            dict(no="07", title="Mini Project", items=[
                "Make 30 yes/no forecasts, each with a %",
                "Log them before the answers",
                "Score with Brier, plot my own Fig. 1",
            ]),
        ],
        tryit=dict(no="04"),
        sources=[
            ("Brier (1950). *Verification of Forecasts Expressed in Terms of Probability*. Monthly Weather Review 78(1)",
             "https://doi.org/10.1175/1520-0493(1950)078%3C0001:VOFEIT%3E2.0.CO;2"),
            ("Murphy (1973). *A New Vector Partition of the Probability Score*",
             "https://doi.org/10.1175/1520-0450(1973)012%3C0595:ANVPOT%3E2.0.CO;2"),
            ("Lichtenstein & Fischhoff (1980). *Training for Calibration*",
             "https://doi.org/10.1016/0030-5073(80)90052-5"),
            ("Lichtenstein, Fischhoff & Phillips (1982). *Calibration of Probabilities*",
             "https://doi.org/10.1017/CBO9780511809477.023"),
            ("Kahneman & Klein (2009). *Conditions for Intuitive Expertise*", "https://doi.org/10.1037/a0016755"),
            ("Grove et al. (2000). *Clinical Versus Mechanical Prediction*",
             "https://doi.org/10.1037/1040-3590.12.1.19"),
            ("Guo et al. (2017). *On Calibration of Modern Neural Networks*",
             "https://proceedings.mlr.press/v70/guo17a.html"),
        ],
    ),
}

SUMMARY = dict(
    style="catalog",
    kicker="Phase 3 · Summary · Sprint 8 of 90",
    em="Judgement",
    dek="Calibration, overconfidence, trusted intuition and the human baseline: scoring judgement before handing it "
        "to a machine.",
    badges=["1 sprint, 4 ideas", "Verified sources", "One phase project"],
    figure=dict(lines=[
        "a window with a calibration plot: dots on a dashed diagonal, a red line crossing it, and a gauge",
        "labels: Brier · Feedback · Intuition · Baseline",
    ]),
    tiles=[
        dict(colour="#5065a2", sprint=8, title="Calibration", text="Of my 70% calls, about 70% should come true. Brier scores it.",
             tag="Sprint 8"),
        dict(colour="#bf5138", sprint=8, title="Overconfidence", text="98% ranges missed the truth about 40% of the time, not 2%.",
             tag="Sprint 8"),
        dict(colour="#26807a", sprint=8, title="Trusting a Gut",
             text="Only in a regular world with fast, clear feedback. Confidence is not skill.", tag="Sprint 8"),
        dict(colour="#b97a1d", sprint=8, title="Head vs Formula",
             text="136 studies: formulas about 10% more accurate. Machines need calibrating too.", tag="Sprint 8"),
    ],
    blocks=[
        dict(title="Now I Can", colour="#40304f", text="Score forecasts with Brier, read a calibration plot, judge when a hunch earns trust.",
             tag="Outcome"),
        dict(title="Mistakes Avoided",
             colour="#cc535d", text="Confidence as evidence, one feedback round as a cure, “10% better” as always better.", tag="Lessons"),
        dict(title="Habits Kept", colour="#2b9075", text="Write a number, not “probably”. Log it before the outcome. Beat 0.25.",
             tag="Practice"),
        dict(title="Phase Project",
             colour="#387ba1", text="A log of 30 forecasts, each with a %, written before the outcome, scored with Brier and plotted."),
    ],
    references_title="Trusted Sources",
    references=[
        ("Brier 1950", "https://doi.org/10.1175/1520-0493(1950)078%3C0001:VOFEIT%3E2.0.CO;2"),
        ("Lichtenstein & Fischhoff 1980", "https://doi.org/10.1016/0030-5073(80)90052-5"),
        ("Kahneman & Klein 2009", "https://doi.org/10.1037/a0016755"),
        ("Grove et al. 2000", "https://doi.org/10.1037/1040-3590.12.1.19"),
        ("Guo et al. 2017", "https://proceedings.mlr.press/v70/guo17a.html"),
    ],
    next_issue=("Next · Phase 4", "Mathematical & Logical Foundations", "From judgement to proof."),
)
