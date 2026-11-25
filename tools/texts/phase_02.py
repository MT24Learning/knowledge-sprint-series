"""Text of the Phase 2 images, for the website's sprint and phase pages.

Transcribed line by line from the published images (phases/phase-02-foundations-of-knowledge/).
Card texts, notes, the quotation under each title and the source lines are word for word; the
figures are read in words from their labels (fig.panels), with the printed captions. The code of
each Try It box is not repeated here: the pages show the sprint's file from code/. Cards carry
their numbers as printed (1, 2, 3 …); the Try It box is number 4. Where a source line on the image
names two works separated by "·", each work is its own entry, so each gets its link.

Marks inside texts: **bold**, *italic*. Thousands are written with a space, as on the images.

Regions: where each part sits on the image, in pixels of the 2160 × 2700 PNG (x0, y0, x1, y1),
measured on the images. The page lights the part of the image whose text is being read.
"""

PHASE = dict(
    n=2,
    accents={4: "#8c3a28", 5: "#8c3a28", 6: "#8c3a28", 7: "#8c3a28"},
    regions={},
    summary_regions={
        "head": (70, 70, 1330, 750), "figure": (1380, 238, 2090, 742),
        "tile-0": (72, 758, 550, 1264), "tile-1": (584, 758, 1062, 1264), "tile-2": (1096, 758, 1574, 1264),
        "tile-3": (1608, 758, 2086, 1264),
        "block-0": (72, 1296, 550, 1804), "block-1": (584, 1296, 1062, 1804), "block-2": (1096, 1296, 1574, 1804),
        "references": (1608, 1296, 2086, 1804),
        "block-3": (72, 1840, 550, 2298), "next": (584, 1840, 2086, 2298),
    },
)

SPRINTS = {
    4: dict(
        regions={
            "head": (40, 360, 2120, 632), "fig": (716, 656, 1396, 1312),
            "1": (52, 656, 688, 1164), "2": (52, 1188, 688, 1856), "3": (716, 1336, 1396, 1856),
            "4": (1424, 656, 2060, 1206), "5": (1424, 1230, 2060, 1856), "6": (52, 1884, 688, 2248),
            "R": (716, 1884, 2108, 2248),
        },
        em="Truth",
        names="Philosophy of Science",
        tagline="“A wise man, therefore, proportions his belief to the evidence.” Hume · Enquiry, §X · 1748",
        fig=dict(
            label="Fig. 1",
            panels=[
                ("Grey dot: true belief, no justification. Red dot: Gettier (1963), all three met, still luck.", [
                    "three overlapping circles: Belief · Truth · Justification",
                    "JTB where all three meet",
                    "*lucky guess*: a grey dot inside Belief and Truth, outside Justification",
                    "*Gettier case*: a red dot inside all three",
                ]),
            ],
        ),
        cards=[
            dict(no="1", title="The Classic Analysis", text="S knows that p only if:", items=[
                "**T** p is true",
                "**B** S believes p",
                "**J** S is justified in believing p",
            ], note="Plato’s Theaetetus (201) tests “true belief with an account” and ends without a definition."),
            dict(no="2", title="The Gettier Gap", items=[
                "Smith’s evidence: Jones gets the job; Jones holds ten coins",
                "He infers: the winner holds ten coins",
                "Smith wins, and happens to hold ten coins",
                "All three met. Still luck.",
            ], note="Gettier’s conclusion: justified true belief is not sufficient for knowledge."),
            dict(no="3", title="What Makes It True?", items=[
                "**Correspondence** It matches the facts",
                "**Coherence** It fits the whole web of beliefs",
                "**Pragmatist** It holds up under inquiry",
                "**Deflationary** “p is true” adds nothing to p",
            ]),
            dict(no="5", title="Evidence Hygiene", items=[
                "Match confidence to evidence",
                "Justified does not mean true",
                "Check the base rate first",
                "Seek evidence against, too",
                "Treat testimony as evidence to weigh, not a verdict",
            ]),
            dict(no="6", title="Mini Project", items=[
                "Write evidence for 3 beliefs",
                "Build my own Gettier case",
                "Rerun Bayes at 1%, 10%, 50%",
                "Log which belief moved most",
            ]),
        ],
        tryit=dict(no="4", items=["*One positive on a 90% test: about 15%. The base rate decides.*"]),
        sources=[
            ("Gettier, E. (1963). *Is Justified True Belief Knowledge?* Analysis 23(6), 121–123",
             "https://doi.org/10.1093/analys/23.6.121"),
            ("Ichikawa & Steup — *The Analysis of Knowledge* (Stanford Encyclopedia of Philosophy)",
             "https://plato.stanford.edu/entries/knowledge-analysis/"),
            ("Glanzberg — *Truth*", "https://plato.stanford.edu/entries/truth/"),
            ("Joyce — *Bayes’ Theorem* (Stanford Encyclopedia of Philosophy)",
             "https://plato.stanford.edu/entries/bayes-theorem/"),
            ("Plato — *Theaetetus*", "https://www.gutenberg.org/ebooks/1726"),
            ("Hume — *An Enquiry Concerning Human Understanding*", "https://www.gutenberg.org/ebooks/9662"),
        ],
    ),

    5: dict(
        regions={
            "head": (40, 360, 2120, 552), "fig": (716, 578, 1396, 1210),
            "1": (52, 578, 688, 1032), "2": (52, 1056, 688, 1858), "3": (716, 1234, 1396, 1858),
            "4": (1424, 578, 2060, 1152), "5": (1424, 1176, 2060, 1858), "6": (52, 1886, 688, 2250),
            "R": (716, 1886, 2108, 2250),
        },
        em="Model?",
        names="Philosophy of Science",
        tagline="“All models are wrong but some are useful.” G. E. P. Box · 1979",
        fig=dict(
            label="Fig. 1",
            panels=[
                ("Period of a real pendulum ÷ the small-angle model. Wrong at every angle, useful below about 20°.", [
                    "y axis: 1.00 · 1.10 · 1.20",
                    "x axis: release angle · 0° · 30° · 60° · 90°",
                    "real pendulum · +18%: a curve rising from 1.00 at 0° to its end point at 90°",
                    "model: T = 2π√(L/g): a dashed line at 1.00",
                    "*<1% off*: a shaded band from 0° to about 20°",
                ]),
            ],
        ),
        cards=[
            dict(no="1", title="Model and Target",
                 text="A model stands in for a target system. I reason with the model to learn about the target.",
                 note="Korzybski (1933): a map is not the territory, but a correct map shares its structure. "
                      "That is why it helps."),
            dict(no="2", title="Kinds of Model", items=[
                "**Scale**: a small car in a wind tunnel",
                "**Analogical**: borrow one system to study another",
                "**Idealized**: simplified on purpose",
                "**Phenomenological**: fits behaviour, not mechanism",
                "**Model of data**: a cleaned-up version of what was measured",
            ]),
            dict(no="3", title="Three Idealizations", items=[
                "**Galilean** Distort to solve it; add detail back later",
                "**Minimalist** Keep only the core causal factors",
                "**Multiple models** Several models, each for its own goal",
            ]),
            dict(no="5", title="Model Hygiene", items=[
                "Name the target and the question",
                "List every simplification",
                "Mark where the model breaks",
                "Test it against measurement",
                "Prefer the simplest model that does the job",
            ]),
            dict(no="6", title="Mini Project", items=[
                "Hang a weight on a 1 m string",
                "Time 10 swings at 10° and 60°",
                "Compare with 2π√(L/g) ≈ 2.01 s",
                "Write where the model broke",
            ]),
        ],
        tryit=dict(no="4", items=["*Exact period ÷ 2π√(L/g). The simple model drifts as the swing grows.*"]),
        sources=[
            ("Frigg & Hartmann — *Models in Science* (Stanford Encyclopedia of Philosophy)",
             "https://plato.stanford.edu/entries/models-science/"),
            ("Box, G. E. P. (1979). *Robustness in the Strategy of Scientific Model Building*, 201–236",
             "https://doi.org/10.1016/B978-0-12-438150-6.50018-2"),
            ("Weisberg, M. (2007). *Three Kinds of Idealization*. Journal of Philosophy 104(12)",
             "https://doi.org/10.5840/jphil20071041240"),
            ("Lima & Arun (2006). Am. J. Phys. 74, 892", "https://doi.org/10.1119/1.2215616"),
            ("Korzybski — *Science and Sanity* (1933)", "https://archive.org/details/sciencesanityint00korz"),
        ],
    ),

    6: dict(
        regions={
            "head": (40, 360, 2120, 612), "fig": (716, 640, 1396, 1276),
            "1": (52, 640, 688, 1138), "2": (52, 1162, 688, 1872), "3": (716, 1300, 1396, 1872),
            "4": (1424, 640, 2060, 1214), "5": (1424, 1238, 2060, 1872), "6": (52, 1900, 688, 2264),
            "R": (716, 1900, 2108, 2264),
        },
        em="Failures",
        names="Philosophy of Science",
        tagline="“…you must not fool yourself — and you are the easiest person to fool.” "
                "Feynman · Cargo Cult Science · 1974",
        fig=dict(
            label="Fig. 1",
            panels=[
                ("The research cycle and four common places where it leaks.", [
                    "a loop: Question → Hypothesis → Design → Data → Analysis → Publish → Question",
                    "centre: REPLICATE · *others run it again*",
                    "at Hypothesis: *postdiction sold as prediction*",
                    "at Design: *too few samples*",
                    "at Analysis: *flexible analysis choices*",
                    "at Publish: *only positives get printed*",
                ]),
            ],
        ),
        cards=[
            dict(no="1", title="No Single Recipe",
                 text="Question, hypothesis, prediction, test, revise: a useful sketch, not a law.",
                 note="Philosophers still debate whether one method fits every science. What they share: ideas face "
                      "new observations, and others can check."),
            dict(no="2", title="Faces of Objectivity", items=[
                "Faithful to the facts",
                "Free of value judgements",
                "Free of personal bias",
                "Built into a community that checks each other’s work",
            ], note="Each ideal has critics. The fourth is the one I can practise."),
            dict(no="3", title="The Replication Test", text=[
                "**97%** → **36%**",
                "100 psychology studies rerun (2015): significant originals vs significant replications. Effects came "
                "back about half as large.",
            ], note="How to read it is still debated: modest power alone predicts part of the drop."),
            dict(no="5", title="Guardrails", items=[
                "Write the plan before the data",
                "Report every outcome tested",
                "Keep exploring apart from testing",
                "Share data and code",
                "Trust what replicates",
            ]),
            dict(no="6", title="Mini Project", items=[
                "Preregister my pendulum test",
                "Run the sim at 1, 5, 20 tests",
                "Find a failed replication",
                "Name the guardrail that fits",
            ]),
        ],
        tryit=dict(no="4", items=["*Test 20 things that do nothing: a “finding” 64% of the time.*"]),
        sources=[
            ("Hepburn & Andersen, *Scientific Method*", "https://plato.stanford.edu/entries/scientific-method/"),
            ("Reiss & Sprenger, *Scientific Objectivity* (SEP)", "https://plato.stanford.edu/entries/scientific-objectivity/"),
            ("Open Science Collaboration (2015). *Reproducibility of Psychological Science*. Science",
             "https://doi.org/10.1126/science.aac4716"),
            ("Simmons, Nelson & Simonsohn (2011). *False-Positive Psychology*. Psych. Science",
             "https://doi.org/10.1177/0956797611417632"),
            ("Nosek et al. (2018). *The Preregistration Revolution*. PNAS", "https://doi.org/10.1073/pnas.1708274114"),
            ("Feynman (1974). *Cargo Cult Science*", "https://calteches.library.caltech.edu/51/2/CargoCult.htm"),
        ],
    ),

    7: dict(
        regions={
            "head": (40, 360, 2120, 556), "fig": (716, 574, 1396, 1186),
            "1": (52, 574, 688, 1040), "2": (52, 1064, 688, 1854), "3": (716, 1210, 1396, 1854),
            "4": (1424, 574, 2060, 1092), "5": (1424, 1116, 2060, 1854), "6": (52, 1882, 688, 2246),
            "R": (716, 1882, 2108, 2246),
        },
        em="Science",
        names="Philosophy of Science",
        tagline="How does science change when the facts push back? Four answers, 1934–1975. "
                "Popper · Kuhn · Lakatos · Feyerabend",
        fig=dict(
            label="Fig. 1",
            panels=[
                ("Same rescue move, two outcomes. Lakatos asks: did the fix predict anything new?", [
                    "top: Newton’s gravity · meets an orbit that won’t fit",
                    "left branch: Uranus drifts · add an unseen planet → Neptune found · 1846 · new fact",
                    "under the left branch: *progressive*",
                    "right branch: Mercury +43″/century · add planet “Vulcan” → Never found · the patch fails "
                    "→ General relativity · 1915 · explains 43″",
                ]),
            ],
        ),
        cards=[
            dict(no="1", title="Popper", tag="1934", text="*The Logic of Scientific Discovery*", items=[
                "Scientific means refutable: some result could sink it",
                "No pile of confirmations proves a law",
            ], note="**Keep:** ask what would prove me wrong."),
            dict(no="2", title="Kuhn", tag="1962", text="*The Structure of Scientific Revolutions*", items=[
                "Normal science solves puzzles inside a paradigm",
                "Anomalies pile up, crisis, revolution",
                "Rival paradigms resist direct comparison",
            ], note="**Keep:** name the paradigm I work in."),
            dict(no="3", title="Lakatos", tag="1970", text="*Research programmes*", items=[
                "A hard core, shielded by a belt of auxiliary hypotheses",
                "Progressive: fixes predict new facts. Degenerating: fixes only rescue",
            ], note="**Keep:** judge a fix by what it predicts."),
            dict(no="4", title="Feyerabend", tag="1975", text="*Against Method*", items=[
                "No single method runs through the history of science",
                "“Anything goes” was his picture of a rationalist’s alarm, not a rule he held",
            ], note="**Keep:** give rival ideas a real hearing."),
            dict(no="6", title="Mini Project", items=[
                "Pick a theory I trust",
                "Write what would refute it",
                "Name its core and its belt",
                "List one anomaly it lives with",
            ]),
        ],
        tryit=dict(no="5", items=["*Einstein’s extra turn of Mercury’s orbit: the 43″ Vulcan was invented to explain.*"]),
        sources=[
            ("Stanford Encyclopedia of Philosophy — *Popper*", "https://plato.stanford.edu/entries/popper/"),
            ("*Kuhn*", "https://plato.stanford.edu/entries/thomas-kuhn/"),
            ("*Lakatos*", "https://plato.stanford.edu/entries/lakatos/"),
            ("*Feyerabend* entries", "https://plato.stanford.edu/entries/feyerabend/"),
            ("Popper (1934/1959), *Logic of Scientific Discovery*", "https://doi.org/10.4324/9780203994627"),
            ("Kuhn (1962), *Structure of Sci. Revolutions*", "https://doi.org/10.7208/chicago/9780226458144.001.0001"),
            ("Lakatos & Musgrave, eds. (1970). *Criticism and the Growth of Knowledge*",
             "https://doi.org/10.1017/CBO9781139171434"),
            ("Feyerabend (1975)", "https://www.penguinrandomhouse.com/books/232548/against-method-by-paul-feyerabend/"),
            ("Sheehan & Misch (2016). *Mercury, Vulcan, and an Early Triumph for General Relativity*",
             "https://articles.adsabs.harvard.edu/pdf/2016AntAs..10....2S"),
        ],
    ),
}

SUMMARY = dict(
    style="catalog",
    kicker="Phase 2 · Summary · Sprints 4–7 of 90",
    em="Knowledge",
    dek="Evidence, models, method and paradigms: four sprints on how we know, each claim checked against primary "
        "sources.",
    badges=["4 sprints, 4 lenses", "Verified sources", "One phase project"],
    figure=dict(lines=[
        "a window with three overlapping circles (blue, yellow, green) and a red dot where all three meet",
        "a pendulum: a string, a bob, a dashed vertical line and a dotted arc",
        "an ellipse with a dot inside it",
        "four labels: Evidence · Models · Method · Paradigms",
    ]),
    tiles=[
        dict(colour="#34577e", sprint=4, title="Knowledge & Evidence",
             text="A justified true belief can still be luck. Base rates set the odds.", tag="Sprint 4"),
        dict(colour="#35664a", sprint=5, title="What Is a Model?",
             text="Every model is wrong. The pendulum formula is under 1% off below 20°.", tag="Sprint 5"),
        dict(colour="#c68a2c", sprint=6, title="Method & Its Failures",
             text="Twenty null tests give a “finding” 64% of the time. Plan first.", tag="Sprint 6"),
        dict(colour="#95412e", sprint=7, title="Four Minds on Science",
             text="Popper, Kuhn, Lakatos, Feyerabend. Judge a fix by what it predicts.", tag="Sprint 7"),
    ],
    blocks=[
        dict(title="Now I Can",
             colour="#214037", text="Update a belief with Bayes, state where a model breaks, spot a forking analysis.", tag="Outcome"),
        dict(title="Mistakes Avoided", colour="#bd5050", text="JTB as ancient consensus, “anything goes” as a rule, 36% as a fraud rate.",
             tag="Lessons"),
        dict(title="Habits Kept",
             colour="#317565", text="Proportion belief to evidence. Write the plan before the data. Seek the refuting result.",
             tag="Practice"),
        dict(title="Phase Project",
             colour="#336f8b", text="A preregistered pendulum study: predict, time the swings, report every result."),
    ],
    references_title="Trusted Sources",
    references=[
        ("Stanford Encyclopedia of Philosophy", "https://plato.stanford.edu/"),
        ("Gettier 1963", "https://doi.org/10.1093/analys/23.6.121"),
        ("Box 1979", "https://doi.org/10.1016/B978-0-12-438150-6.50018-2"),
        ("Open Science Collaboration 2015", "https://doi.org/10.1126/science.aac4716"),
        ("Lakatos & Musgrave 1970", "https://doi.org/10.1017/CBO9781139171434"),
    ],
    next_issue=("Next · Phase 3", "Calibrating Judgement", "From ideas to judgement."),
)
