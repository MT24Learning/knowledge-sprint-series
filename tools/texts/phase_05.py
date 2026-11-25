"""Text of the Phase 5 images, for the website's sprint and phase pages.

Transcribed line by line from the published images (phases/phase-05-statistics-and-experimental-design/).
Card texts, notes, the summary's tiles and boxes and the source lines are word for word; the figure
panels are read in words from their labels (fig.panels), with the printed captions in italics. The code
of each Try It box is not repeated here: the pages show the sprint's file from code/, which ends with the
printed output. tools/website.py turns this file into the pages.

Marks inside texts: **bold**, *italic*. Thousands are written with a space, as on the images
(100 000); the pages keep each group together with a no-break space.

Regions: where each part sits on the image, in pixels of the 2160 × 2700 PNG (x0, y0, x1, y1),
measured on the images. The page lights the part of the image whose text is being read.
"""

PHASE = dict(
    n=5,
    accents={13: "#1f4e9c", 14: "#1f4e9c", 15: "#1f4e9c"},
    regions={"head": (70, 318, 2108, 562), "R": (80, 2092, 1583, 2287), "entry": (1608, 2094, 2104, 2286)},
    summary_regions={
        "head": (75, 75, 1320, 700), "figure": (1375, 270, 2140, 715),
        "tile-0": (78, 798, 552, 1252), "tile-1": (588, 798, 1062, 1252),
        "tile-2": (1098, 798, 1573, 1252), "tile-3": (1611, 798, 2083, 1252),
        "block-0": (78, 1285, 552, 1740), "block-1": (588, 1285, 1062, 1740),
        "block-2": (1098, 1285, 1573, 1740), "references": (1611, 1285, 2083, 1740),
        "block-3": (79, 1772, 552, 2216), "next": (588, 1772, 2088, 2216),
    },
)

SPRINTS = {
    13: dict(
        regions={
            "fig": (80, 580, 1420, 1179), "05": (1444, 580, 2103, 1179),
            "01": (80, 1200, 739, 1627), "02": (762, 1200, 1421, 1627), "03": (1444, 1200, 2103, 1627),
            "04": (80, 1648, 739, 2075), "06": (762, 1648, 1421, 2075), "07": (1444, 1648, 2103, 2075),
        },
        em="Distributions",
        names="Kolmogorov · Bernoulli · de Moivre · Laplace",
        fig=dict(
            label="Fig. 1",
            panels=[
                ("Running mean", [
                    "*Running mean of the 100 000 draws in the code (seed 13). Check for ③: "
                    "(6 828 × 1.662 + 32 383) ÷ 6 829 = 6.40*",
                    "*running mean* from −4 to 6 against *number of draws n (log scale)* from 10 to 100k",
                    "dashed line: *true mean = 1*",
                    "① green line: the exponential mean, hugging the dashed line",
                    "② a shaded green band around 1 that narrows as n grows",
                    "③ the red line jumps to its peak just below 10k, then falls back",
                    "④ red line: the Cauchy mean, from below −2 at 10 draws, still wandering at 100k",
                ]),
            ],
            notes=[
                ("", "**Exponential · mean 1** Settles: 0.949, 1.025, 1.0."),
                ("", "**Band · 1 ± 2/√n** The spread shrinks like 1/√n."),
                ("", "**One draw · n = 6 829** A single draw of 32 383 lifts the mean from 1.66 to 6.40."),
                ("", "**Cauchy · no mean** Still wandering at 100k."),
            ],
        ),
        cards=[
            dict(no="", key="entry", title="Entry 13 / 90", items=["Observer M. Tahri", "Seed 13", "Draws 100 000"]),
            dict(no="01", title="Three Axioms", items=[
                "P(A) ≥ 0 for every event",
                "P(Ω) = 1: something happens",
                "Disjoint events: probabilities add, even for countably many",
            ], note="Kolmogorov (1933). The rest, laws of large numbers included, is derived from these."),
            dict(no="02", title="What P Means", items=[
                "**Frequency:** a long-run share",
                "**Subjective:** a coherent degree of belief",
                "**Propensity:** a tendency of the set-up",
            ], note="The axioms fit all three; they are silent on which numbers to assign (Hájek, SEP)."),
            dict(no="03", title="Six Specimens", items=[
                "**Bernoulli** *one yes / no*",
                "**Binomial** *yeses in n*",
                "**Poisson** *rare counts*",
                "**Normal** *sums of effects*",
                "**Exponential** *waiting times*",
                "**Cauchy** *no mean*",
            ]),
            dict(no="04", title="Averages Settle", items=[
                "**LLN** (Bernoulli, 1713): the sample mean closes in on the true one",
                "**CLT** (de Moivre 1733, Laplace 1810): shape turns normal, spread σ/√n",
            ], note="Both need a finite mean; the CLT also needs finite variance."),
            dict(no="06", title="General Notes", items=[
                "Name the sample space first",
                "Look at the tails before the mean",
                "Shares converge; the heads–tails gap grows like √n",
                "Simulate, then check the formula",
            ]),
            dict(no="07", title="Mini Project", items=[
                "Rerun the code with seeds 1 to 5",
                "Plot my own Fig. 1 for each seed",
                "Histogram 10 000 means of 30: a bell?",
                "Swap in the median: does Cauchy settle?",
            ]),
        ],
        tryit=dict(),
        sources=[
            ("Kolmogorov (1933). *Grundbegriffe der Wahrscheinlichkeitsrechnung*. Springer",
             "https://doi.org/10.1007/978-3-642-49888-6"),
            ("Hájek. *Interpretations of Probability*. Stanford Encyclopedia of Philosophy",
             "https://plato.stanford.edu/entries/probability-interpret/"),
            ("Bernoulli (1713). *Ars Conjectandi*", "https://doi.org/10.25673/42121"),
            ("Stigler (1986). *The History of Statistics*", "https://www.hup.harvard.edu/books/9780674403413"),
            ("Blitzstein & Hwang (2019). *Introduction to Probability*", "https://doi.org/10.1201/9780429428357"),
            ("NIST/SEMATECH e-Handbook", "https://doi.org/10.18434/M32189"),
        ],
    ),

    14: dict(
        regions={
            "fig": (80, 580, 1420, 1203), "05": (1444, 580, 2103, 1203),
            "01": (80, 1224, 739, 1639), "02": (762, 1224, 1421, 1639), "03": (1444, 1224, 2103, 1639),
            "04": (80, 1660, 739, 2075), "06": (762, 1660, 1421, 2075), "07": (1444, 1660, 2103, 2075),
        },
        em="Power",
        names="Fisher · Neyman · Pearson · Cohen",
        fig=dict(
            label="Fig. 1",
            panels=[
                ("Power", [
                    "*Power of a two-sided t-test, α = 0.05, from the noncentral t (it matches statsmodels). "
                    "The simulation lands on the curve: 0.794 at n = 64, 0.335 at n = 20.*",
                    "*power* from 0.0 to 1.0 against *sample size n per group (log scale)* from 5 to 1 000",
                    "three curves: d = 0.8 (green) · d = 0.5 (blue) · d = 0.2 (purple)",
                    "a dashed line at power 0.8, crossed at 26 · 64 · 393",
                    "① a red dashed line near the bottom",
                    "② the dashed line at 0.8",
                    "③ the blue curve crossing 0.8 at 64",
                    "④ an open red circle on the blue curve at n = 20",
                ]),
            ],
            notes=[
                ("", "**α = 0.05 · no effect** 5% still fire. My run: 0.0498."),
                ("", "**Target · power 0.80** β = 0.20, four times α (Cohen)."),
                ("", "**n = 64 per group** Enough for d = 0.5; 26 for 0.8, 393 for 0.2."),
                ("", "**n = 20 · power 0.34** Hits average 0.83, not 0.5."),
            ],
        ),
        cards=[
            dict(no="", key="entry", title="Entry 14 / 90", items=["Observer M. Tahri", "Seed 14", "Experiments 3 × 10 000"]),
            dict(no="01", title="The Logic of a Test", items=[
                "**H₀:** no effect. **H₁:** an effect of a stated size",
                "**p:** how surprising data this extreme would be if H₀ were true",
            ], note='Fisher (1925) called p = 0.05, "1 in 20", a convenient limit for judging significance.'),
            dict(no="02", title="Two Errors", items=[
                "Reject H₀ · H₀ true: **Type I · α** · H₁ true: **Power · 1 − β**",
                "Keep H₀ · H₀ true: **Correct** · H₁ true: **Type II · β**",
            ], note="Neyman & Pearson (1933): fix α first, then pick the test with the most power."),
            dict(no="03", title="What Sets Power", items=[
                "Effect size d, sample size n, α and noise",
                "n grows like 1/d²: from d = 0.5 to 0.2, 64 becomes 393",
            ], note="Cohen (1992): 26, 64 and 393 per group for d = 0.8, 0.5 and 0.2."),
            dict(no="04", title="Reading p Right", items=[
                "p is not the chance that H₀ is true",
                'Not significant is not "no effect"',
                "Significant is not large or important",
            ], note="ASA statement (2016), principles 2 and 5."),
            dict(no="06", title="General Notes", items=[
                "Fix n and α before the data",
                "Power for the smallest effect that matters",
                "Report the effect and its interval",
            ], note="Low power plus a hit means an inflated effect (Gelman & Carlin, 2014)."),
            dict(no="07", title="Mini Project", items=[
                "Rerun the code at n = 10, 40, 100",
                "Plot my own power curve for d = 0.5",
                "Find n for 90% power, then simulate it",
                "Log the effect the hits report at each n",
            ]),
        ],
        tryit=dict(),
        sources=[
            ("Fisher (1925). *Statistical Methods for Research Workers*", "https://doi.org/10.1093/oso/9780198522294.001.0001"),
            ("Neyman & Pearson (1933)", "https://doi.org/10.1098/rsta.1933.0009"),
            ("Cohen (1992). *A Power Primer*. Psychological Bulletin 112(1)", "https://doi.org/10.1037/0033-2909.112.1.155"),
            ("Wasserstein & Lazar (2016). *The ASA Statement on p-Values*. Am. Stat. 70(2)",
             "https://doi.org/10.1080/00031305.2016.1154108"),
            ("Gelman & Carlin (2014). *Beyond Power Calculations*", "https://doi.org/10.1177/1745691614551642"),
            ("Button et al. (2013)", "https://doi.org/10.1038/nrn3475"),
        ],
    ),

    15: dict(
        regions={
            "fig": (80, 580, 1420, 1239), "05": (1444, 580, 2103, 1239),
            "01": (80, 1260, 739, 1657), "02": (762, 1260, 1421, 1657), "03": (1444, 1260, 2103, 1657),
            "04": (80, 1678, 739, 2075), "06": (762, 1678, 1421, 2075), "07": (1444, 1678, 2103, 2075),
        },
        em="Rigorous",
        names="Fisher · Simpson · Hill · Holm",
        fig=dict(
            label="Fig. 1",
            panels=[
                ("Stones removed (success rate)", [
                    "*Real kidney-stone data (Charig et al., 1986). B = percutaneous nephrolithotomy; dot area follows "
                    "patient numbers. Stone size drove both the choice and the outcome.*",
                    "A · open surgery (blue) · B · PCNL (gold)",
                    "success rate from 60% to 100%",
                    "Small · *< 2 cm*: A 93% 81/87 · B 87% 234/270",
                    "Large · *≥ 2 cm*: A 73% 192/263 · B 69% 55/80",
                    "All · *stones*: A 78% 273/350 · B 83% 289/350",
                    "① A, small stones · ② A, large stones · ③ B, all stones · ④ A, all stones",
                ]),
            ],
            notes=[
                ("Small stones · A wins", "93% against 87%."),
                ("Large stones · A wins", "73% against 69%."),
                ("All stones · B wins", "83% against 78%: reversed."),
                ("Who got which stones", "A treated 263 large stones of 350; B treated 270 small of 350."),
            ],
        ),
        cards=[
            dict(no="", key="entry", title="Entry 15 / 90", items=["Observer M. Tahri", "Seed 15", "Sim. patients 100 000"]),
            dict(no="01", title="Fisher's Three Rules", items=[
                "**Replicate:** to measure the error",
                "**Randomize:** chance assigns treatment",
                "**Block:** compare like with like",
            ], note="Fisher (1935), the tea test: 8 cups, 4 of each; a lucky guess of all: 1 in 70."),
            dict(no="02", title="Confounding", items=[
                "A third factor drives both the choice and the outcome",
                "Fig. 1: stone size. The code: severity",
            ], note="Adjusting fixes it only for what I measured: −1.262 became 0.996 once severity entered."),
            dict(no="03", title="Randomize & Blind", items=[
                "A coin, not a person, assigns",
                "Hide the next assignment; blind who measures",
            ], note="MRC streptomycin trial (1948): sealed envelopes. Its lasting lesson is concealment (Chalmers, 2011)."),
            dict(no="04", title="Many Tests, One Plan", items=[
                "20 null tests at α = 0.05: 64% chance of a false hit",
                "Holm (1979): the k-th smallest p faces α/(m − k + 1)",
            ], note="Name the primary outcome before the data."),
            dict(no="06", title="General Notes", items=[
                "Write the protocol first",
                "Randomize what I cannot measure",
                "Adjust only for what came before treatment",
                "Report every outcome I tested",
            ]),
            dict(no="07", title="Mini Project", items=[
                "Run a tea or coffee test: 8 cups, 4 of each",
                "Order by coin; a friend serves (blind)",
                "Drop s from X in the code: watch the bias return",
            ]),
        ],
        tryit=dict(),
        sources=[
            ("Fisher (1935). *The Design of Experiments*. Oliver & Boyd", "https://doi.org/10.1093/oso/9780198522294.001.0001"),
            ("Holm (1979). *Scand. J. Stat.* 6(2)", "https://www.jstor.org/stable/4615733"),
            ("Charig et al. (1986). BMJ 292, 879–882", "https://doi.org/10.1136/bmj.292.6524.879"),
            ("Julious & Mullee (1994). BMJ 309, 1480", "https://doi.org/10.1136/bmj.309.6967.1480"),
            ("Medical Research Council (1948). *Streptomycin Treatment of Pulmonary Tuberculosis*",
             "https://doi.org/10.1136/bmj.2.4582.769"),
            ("Chalmers (2011). James Lind Library",
             "https://www.jameslindlibrary.org/articles/why-the-1948-mrc-trial-of-streptomycin-used-treatment-allocation-based-on-random-numbers/"),
            ("Montgomery. *Design and Analysis of Experiments*",
             "https://www.wiley-vch.de/de/fachgebiete/ingenieurwesen/design-and-analysis-of-experiments-978-1-119-81695-9"),
        ],
    ),
}

SUMMARY = dict(
    style="catalog",
    kicker="Phase 5 · Summary · Sprints 13–15 of 90",
    em="Design",
    dek="Distributions, power and design: three sprints on how evidence is counted, every number rerun in code.",
    badges=["3 sprints, 3 simulations", "Verified sources", "One phase project"],
    figure=dict(lines=[
        "a screen with a chart: a green bell curve with a red shaded tail, a blue S-shaped curve with a small blue "
        "dot where it crosses a dashed line, a larger blue dot and a gold dot",
        "four labels: Distributions · Power · Confounding · Randomization",
    ]),
    tiles=[
        dict(colour="#2558aa", sprint=13, title="Distributions",
             text="The exponential mean settled at 1.0. The Cauchy mean never did. Tails first.", tag="Sprint 13"),
        dict(colour="#358453", sprint=14, title="Sample Size",
             text="64 per group: power 0.79. At 20, the hits averaged 0.83 for a true 0.5.", tag="Sprint 14"),
        dict(colour="#af7512", sprint=15, title="Confounding",
             text="Open surgery won both stone sizes, then lost overall: 78% against 83%.", tag="Sprint 15"),
        dict(colour="#c93f35", sprint=15, title="Randomization",
             text="Doctor's choice: −1.262. Coin flip: 0.998. The true effect was +1.", tag="Sprint 15"),
    ],
    blocks=[
        dict(title="Now I Can", colour="#4a356e", text="Simulate a distribution, size a study for 80% power, spot a confounder.",
             tag="Outcome"),
        dict(title="Mistakes Avoided",
             colour="#cb4844", text='Luck "evening out", p as the chance H₀ is true, "not significant" as "no effect".', tag="Lessons"),
        dict(title="Habits Kept", colour="#247c7f", text="Tails before the mean. n and α before the data. A coin decides.",
             tag="Practice"),
        dict(title="Phase Project",
             colour="#286aa3", text="A blind tasting study: n planned for 80% power, cups ordered by coin, every result reported."),
    ],
    references_title="Trusted Sources",
    references=[
        ("Kolmogorov 1933", "https://doi.org/10.1007/978-3-642-49888-6"),
        ("Fisher 1925, 1935", "https://doi.org/10.1093/oso/9780198522294.001.0001"),
        ("Neyman & Pearson 1933", "https://doi.org/10.1098/rsta.1933.0009"),
        ("Cohen 1992", "https://doi.org/10.1037/0033-2909.112.1.155"),
        ("ASA 2016", "https://doi.org/10.1080/00031305.2016.1154108"),
        ("Charig et al. 1986", "https://doi.org/10.1136/bmj.292.6524.879"),
    ],
    next_issue=("Next · Phase 6", "How Paradigms Die", "From evidence to revolutions."),
)
