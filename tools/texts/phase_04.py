"""Text of the Phase 4 images, for the website's sprint and phase pages.

Transcribed line by line from the published images (phases/phase-04-mathematical-and-logical-foundations/).
Card texts, notes and the source lines are word for word; the figure panels are read in words from
their labels (fig.panels), with the printed captions in italics. The code of each Try It box is not
repeated here: the pages show the sprint's file from code/, which ends with the printed output.
tools/website.py turns this file into the pages.

Marks inside texts: **bold**, *italic*. Formulas printed in the mono face are given as plain text.
The figure captions ("Fig. 1 — …") are in `caption`, in their own case; maths inside a heading the page sets in
capitals is in backticks, so it keeps its case (w, η, p, q).
The blueprint frame (grid letters and numbers) and its title block (drawn, sheet, phase, scale,
rev, date) repeat the footer's signature data and are left out, like the footer.

Regions: where each part sits on the image, in pixels of the 2160 × 2700 PNG (x0, y0, x1, y1),
measured on the images. The page lights the part of the image whose text is being read.
"""

PHASE = dict(
    n=4,
    accents={9: "#ffc861", 10: "#ffc861", 11: "#ffc861", 12: "#ffc861"},
    regions={},
    summary_regions={
        "head": (60, 75, 1260, 730), "figure": (1365, 265, 2075, 760),
        "tile-0": (76, 796, 552, 1272), "tile-1": (588, 796, 1062, 1272), "tile-2": (1098, 796, 1574, 1272),
        "tile-3": (1610, 796, 2084, 1272),
        "block-0": (76, 1300, 552, 1776), "block-1": (588, 1300, 1062, 1776), "block-2": (1098, 1300, 1574, 1776),
        "references": (1610, 1300, 2084, 1776), "block-3": (76, 1804, 552, 2268), "next": (588, 1804, 2084, 2268),
    },
)

SPRINTS = {
    9: dict(
        regions={
            "head": (60, 345, 2100, 585), "fig": (68, 606, 1387, 1168), "05": (1412, 606, 2091, 1168),
            "01": (68, 1190, 715, 1608), "02": (740, 1190, 1387, 1608), "03": (1412, 1190, 2091, 1608),
            "04": (68, 1630, 715, 2036), "06": (740, 1630, 1387, 2036), "07": (1412, 1630, 2091, 2036),
            "R": (68, 2058, 1643, 2306),
        },
        em="Machine Learning",
        tagline="Data become vectors, layers become matrices, learning becomes a walk downhill.",
        names="Vectors · Matrices · Gradients · Chain Rule",
        fig=dict(
            label="Fig. 1",
            caption="Computed descent on L = ½(w₁² + 10w₂²), η = 0.18: the steps cross the narrow valley.",
            panels=[
                ("Level set", [
                    "Same loss all round the ring.",
                    "rings round the minimum, on the axes w₁ and w₂",
                ]),
                ("Gradient ∇L", [
                    "Steepest way up, ⊥ to the ring.",
                    "arrow from the starting point",
                ]),
                ("Step `-η∇L`", [
                    "Downhill, but not aimed at w*.",
                    "the steps zig-zag across the valley · Δw₁ = 8 from the start to the minimum",
                ]),
                ("Minimum `w*`", [
                    "Here ∇L = 0.",
                ]),
            ],
        ),
        cards=[
            dict(no="01", title="Vectors", items=[
                "A data point is a vector: one number per feature",
                "Dot product: x·y = Σxᵢyᵢ = ‖x‖‖y‖cos θ",
            ], note="Divided by both lengths, it becomes cosine similarity, used to compare embeddings."),
            dict(no="02", title="Matrices as Maps", items=[
                "A matrix maps one vector to another: y = Ax",
                "A dense layer: Wx + b, then a nonlinearity",
                "Shapes chain: (m×n)(n×p) → m×p",
            ], note="**Keep:** write the shape beside every array."),
            dict(no="03", title="Gradients", items=[
                "∂L/∂wᵢ: how fast the loss moves as one weight moves",
                "∇L stacks them all and points uphill fastest",
                "Descend: w ← w - η∇L",
            ], note="Cauchy proposed this step in 1847."),
            dict(no="04", title="The Chain Rule", items=[
                "(f∘g)′(x) = f′(g(x))·g′(x)",
                "A network is a chain of functions; backprop runs the rule from the loss backwards",
            ], note="Backprop only computes the gradient; descent does the learning (Goodfellow et al., §6.5)."),
            dict(no="06", title="General Notes", items=[
                "Write the shape of every array",
                "Check each gradient against finite differences",
                "Loss climbing? Cut the step η",
                "Scale features: a rounder valley, fewer zig-zags",
            ]),
            dict(no="07", title="Mini Project", items=[
                "Derive the least-squares gradient on paper",
                "Code it in NumPy; check it numerically",
                "Run descent and plot the loss per step",
                "Compare with np.linalg.lstsq",
            ]),
        ],
        tryit=dict(),
        sources=[
            ("Deisenroth, Faisal & Ong (2020). *Mathematics for Machine Learning*. Cambridge University Press",
             "https://doi.org/10.1017/9781108679930"),
            ("Goodfellow, Bengio & Courville (2016). *Deep Learning*, ch. 2, 4, §6.5. MIT Press",
             "https://www.deeplearningbook.org/"),
            ("Baydin et al. (2018). *Automatic Differentiation in Machine Learning: a Survey*. JMLR 18",
             "https://jmlr.org/papers/v18/17-468.html"),
            ("Rumelhart, Hinton & Williams (1986). *Nature* 323", "https://doi.org/10.1038/323533a0"),
            ("Cauchy (1847). *Comptes rendus* 25", "https://archive.org/details/comptesrendusheb25acad"),
        ],
    ),
    10: dict(
        regions={
            "head": (60, 345, 2100, 585), "fig": (68, 606, 1395, 1168), "05": (1420, 606, 2091, 1168),
            "01": (68, 1190, 719, 1594), "02": (744, 1190, 1395, 1594), "03": (1420, 1190, 2091, 1594),
            "04": (68, 1616, 719, 2024), "06": (744, 1616, 1395, 2024), "07": (1420, 1616, 2091, 2024),
            "R": (68, 2046, 1643, 2294),
        },
        em="Inference",
        tagline="Logic checks the form of an argument. The world checks its premises.",
        names="Propositions · Connectives · Validity",
        fig=dict(
            label="Fig. 1",
            caption="Wason's selection task (1966, 1968). Only E and 7 can break the rule; in the abstract version, "
                  "fewer than 10% of people pick exactly those two.",
            panels=[
                ("Rule: vowel on one side → even number on the other", [
                    "E · p · turn",
                    "K · ¬p · skip",
                    "4 · q · trap",
                    "7 · ¬q · turn",
                    "4 cards · 2 to turn",
                ]),
            ],
            notes=[
                ("E · `p`", "Turn: an odd number breaks it."),
                ("K · `¬p`", "Skip: the rule is silent here."),
                ("4 · `q`", "Skip: any back is allowed."),
                ("7 · `¬q`", "Turn: a vowel breaks it."),
            ],
        ),
        cards=[
            dict(no="01", title="Propositions", items=[
                "A statement that is either true or false",
                "Atoms p, q join with ¬ ∧ ∨ → ↔",
            ], note="\"Close the door\" and \"Is it raining?\" are not propositions: neither can be true or false."),
            dict(no="02", title="The Conditional", items=[
                "p q: T T · T F · F T · F F",
                "p→q: T · F · T · T",
            ], note="False only when p is true and q false. \"True whenever p is false\" is the contested part, a "
                    "paradox of the material conditional (SEP)."),
            dict(no="03", title="Valid vs Sound", items=[
                "Valid: no case with true premises and a false conclusion",
                "Sound: valid, and the premises are true",
            ], note="Validity is about form. A valid argument can still end in a false conclusion."),
            dict(no="04", title="Three Inferences", items=[
                "Deduction: the conclusion must follow",
                "Induction: cases to a rule, probably",
                "Abduction: surprise → a hypothesis",
            ], note="Peirce placed abduction in discovery; \"best explanation\" is the modern reading (SEP)."),
            dict(no="06", title="General Notes", items=[
                "Ask what would falsify the rule",
                "Check the form before the content",
                "\"p only if q\" means p → q",
                "Valid is not true: check the premises",
            ]),
            dict(no="07", title="Mini Project", items=[
                "Five news arguments in p/q form",
                "Run each through the checker",
                "Mark valid, then mark sound",
                "Give Fig. 1 to three friends",
            ]),
        ],
        tryit=dict(),
        sources=[
            ("Wason (1968). *Reasoning about a Rule*. Quarterly Journal of Experimental Psychology 20",
             "https://doi.org/10.1080/14640746808400161"),
            ("Evans, Newstead & Byrne (1993). *Human Reasoning: The Psychology of Deduction*. Erlbaum",
             "https://doi.org/10.4324/9781315785028"),
            ("Beall, Restall & Sagi. *Logical Consequence*", "https://plato.stanford.edu/entries/logical-consequence/"),
            ("Edgington. *Indicative Conditionals* (SEP)", "https://plato.stanford.edu/entries/conditionals/"),
            ("Douven. *Abduction*, Stanford Encyclopedia of Philosophy", "https://plato.stanford.edu/entries/abduction/"),
        ],
    ),
    11: dict(
        regions={
            "head": (60, 345, 2100, 585), "fig": (68, 606, 1409, 1168), "05": (1434, 606, 2091, 1168),
            "01": (68, 1190, 725, 1594), "02": (750, 1190, 1409, 1594), "03": (1434, 1190, 2091, 1594),
            "04": (68, 1616, 725, 2024), "06": (750, 1616, 1409, 2024), "07": (1434, 1616, 2091, 2024),
            "R": (68, 2046, 1643, 2294),
        },
        em="Assumptions",
        tagline="Every proof starts from something it does not prove. Say what it is.",
        names="Euclid · Beltrami · Hilbert · Gödel",
        fig=dict(
            label="Fig. 1",
            caption="Change the parallel axiom and the angle sum changes. The sphere's triangle covers exactly 1/8 "
                  "of its surface: see the code.",
            panels=[
                ("Same question · three answers", [
                    "plane · Σ = 180°",
                    "sphere · Σ = 270° (right-angle marks at the corners)",
                    "saddle · Σ < 180°",
                    "parallels decide the sum",
                ]),
            ],
            notes=[
                ("Plane · Euclid", "One parallel through a point."),
                ("Sphere", "No parallels: 3 right angles."),
                ("Saddle · Lobachevsky", "Many parallels: thin angles."),
            ],
        ),
        cards=[
            dict(no="01", title="What an Axiom Is", items=[
                "A starting claim taken without proof",
                "Theorems follow by valid steps (Sprint 10)",
            ], note="Euclid's fifth postulate, on parallels, resisted proof for over two thousand years."),
            dict(no="02", title="The Fifth Postulate", items=[
                "1820s: Lobachevsky and Bolyai build a geometry with many parallels",
                "1868: Beltrami models it inside Euclid",
            ], note="If Euclid is consistent, so is the new geometry. The fifth cannot follow from the rest."),
            dict(no="03", title="Good Axiom Sets", items=[
                "Consistent: no contradiction follows",
                "Independent: no axiom is redundant",
                "Complete: every statement is decided",
            ], note="Gödel (1931): a consistent formal system with enough arithmetic is never complete."),
            dict(no="04", title="Declared Assumptions", items=[
                "A p-value means something only under its stated model (ASA, 2016)",
                "Train and test data may differ: dataset shift",
            ], note="**Keep:** write each assumption where a reader can test it."),
            dict(no="06", title="General Notes", items=[
                "List assumptions before results",
                "Mark which ones data can test",
                "Drop one and rerun: what breaks?",
                "Unstated does not mean absent",
            ]),
            dict(no="07", title="Mini Project", items=[
                "Pick one result I rely on",
                "List every assumption behind it",
                "Drop one, rerun, log the change",
                "Triangle on a ball: add its angles",
            ]),
        ],
        tryit=dict(),
        sources=[
            ("Torretti. *Nineteenth Century Geometry*", "https://plato.stanford.edu/entries/geometry-19th/"),
            ("Raatikainen. *Gödel's Incompleteness Theorems* (SEP)",
             "https://plato.stanford.edu/entries/goedel-incompleteness/"),
            ("Beltrami (1868). *Saggio di interpretazione della geometria non-euclidea*", "https://eudml.org/doc/203338"),
            ("Hilbert (1899)", "https://doi.org/10.14463/GBV:1004921101"),
            ("Wasserstein & Lazar (2016). *The ASA's Statement on p-Values*. The American Statistician 70(2)",
             "https://doi.org/10.1080/00031305.2016.1154108"),
            ("Quiñonero-Candela et al., eds. (2009). *Dataset Shift in Machine Learning*. MIT Press",
             "https://doi.org/10.7551/mitpress/9780262170055.001.0001"),
        ],
    ),
    12: dict(
        regions={
            "head": (60, 345, 2100, 585), "fig": (68, 606, 1409, 1170), "05": (1434, 606, 2091, 1170),
            "01": (68, 1192, 725, 1596), "02": (750, 1192, 1409, 1596), "03": (1434, 1192, 2091, 1596),
            "04": (68, 1618, 725, 2026), "06": (750, 1618, 1409, 2026), "07": (1434, 1618, 2091, 2026),
            "R": (68, 2048, 1663, 2296),
        },
        em="Review",
        tagline="Every claim in this phase, checked by running it.",
        names="Properties · Tolerance · Shrinking",
        fig=dict(
            label="Fig. 1",
            caption="How a property-based test runs. Floats broke the associativity rule; the tool reported a failing "
                  "case.",
            panels=[
                ("one property · many inputs", [
                    "1 · Generate: a, b, c in [0, 10] → 2 · Check: (a+b)+c == a+(b+c)",
                    "Check is joined by a dashed line to a dashed box: Property · for ALL inputs",
                    "pass · next input: a dashed arrow from Check back to Generate",
                    "fail: an arrow from Check down to 3 · Shrink: a simpler failure, with a dashed loop: repeat",
                    "Shrink → 4 · Report: 3.03…, 0.99999, 1.0",
                ]),
            ],
            notes=[
                ("Generate", "Random inputs from a strategy."),
                ("Check", "Run the property on each one."),
                ("Shrink", "Simplify the failing case."),
                ("Report", "Print the case it found."),
            ],
        ),
        cards=[
            dict(no="01", title="What a Test Is", items=[
                "A claim, checked by running the code",
                "Example test: one input, one answer",
            ], note="Dijkstra (1969): \"Program testing can be used to show the presence of bugs, but never to show "
                    "their absence!\""),
            dict(no="02", title="Property Tests", items=[
                "State a rule for all inputs, not one",
                "The tool generates cases and shrinks failures",
            ], note="QuickCheck (Claessen & Hughes, 2000) popularised the idea; Hypothesis brings it to Python."),
            dict(no="03", title="Floats Need Tolerance", items=[
                "0.1 + 0.2 == 0.3 is False",
                "Compare with math.isclose, not ==",
            ], note="Floats round at every step, so the order of operations can change the result (Goldberg, 1991)."),
            dict(no="04", title="Phase 4 Review", items=[
                "Sprint 9: gradient vs finite differences",
                "Sprint 10: every row of the truth table",
                "Sprint 11: angle excess vs area",
            ], note="Three checks: numerical, exhaustive, and against a known answer."),
            dict(no="06", title="General Notes", items=[
                "Test the rule, not one example",
                "Keep each failure as a test",
                "Floats: a tolerance, never ==",
                "A green run is evidence, not proof",
            ]),
            dict(no="07", title="Mini Project", items=[
                "Write 3 properties for Sprint 9's code",
                "Run Hypothesis; keep each failure",
                "Swap == for isclose where needed",
                "Run every test in CI (Sprint 3)",
            ]),
        ],
        tryit=dict(),
        sources=[
            ("Dijkstra (1969). *Notes on Structured Programming* (EWD 249)",
             "https://www.cs.utexas.edu/~EWD/ewd02xx/EWD249.PDF"),
            ("Claessen & Hughes (2000). *QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs*. ICFP",
             "https://doi.org/10.1145/351240.351266"),
            ("Goldberg (1991). *What Every Computer Scientist Should Know About Floating-Point Arithmetic*",
             "https://doi.org/10.1145/103162.103163"),
            ("Hypothesis documentation", "https://hypothesis.readthedocs.io/"),
            ("Python documentation, *math.isclose* (PEP 485)", "https://docs.python.org/3/library/math.html#math.isclose"),
        ],
    ),
}

SUMMARY = dict(
    style="catalog",
    kicker="Phase 4 · Summary · Sprints 9–12 of 90",
    em="Foundations",
    dek="Gradients, logic, axioms and tests: four sprints on the maths under machine learning, every claim checked by "
        "running it.",
    badges=["4 sprints, 4 checks", "Verified sources", "One phase project"],
    figure=dict(lines=[
        "a window with a blueprint grid: a truth-table line p → q over T F T T, a zig-zag path down into rings that "
        "ends at a green dot, and a triangle marked 270°",
        "labels: Gradients · Logic · Axioms · Tests",
    ]),
    tiles=[
        dict(colour="#255a95", sprint=9, title="Calculus for ML",
             text="A hand-derived gradient matched finite differences: −5.0586.", tag="Sprint 9"),
        dict(colour="#239488", sprint=10, title="Logic & Inference",
             text="Valid is not true. Only E and 7 can break Wason's rule.", tag="Sprint 10"),
        dict(colour="#d1952c", sprint=11, title="Axioms Declared",
             text="Change the parallel axiom and the triangle changes: 270° on a sphere.", tag="Sprint 11"),
        dict(colour="#cf5a3d", sprint=12, title="Testing & Review",
             text="A property test broke (a+b)+c = a+(b+c) on floats. Compare with a tolerance.", tag="Sprint 12"),
    ],
    blocks=[
        dict(title="Now I Can", colour="#352a4b", text="Check a gradient, test a form, list assumptions, write property tests.",
             tag="Outcome"),
        dict(title="Mistakes Avoided", colour="#cb4f52", text="Backprop as the learner, Gödel as \"unprovable truths\", floats with ==.",
             tag="Lessons"),
        dict(title="Habits Kept", colour="#218e6e", text="Shape beside every array. Ask what would falsify it. Assumptions first.",
             tag="Practice"),
        dict(title="Phase Project",
             colour="#3484b4", text="One NumPy model: gradient checked, assumptions listed, property tests in CI."),
    ],
    references_title="Trusted Sources",
    references=[
        ("Deisenroth et al. 2020", "https://doi.org/10.1017/9781108679930"),
        ("Goodfellow et al. 2016", "https://www.deeplearningbook.org/"),
        ("Wason 1968", "https://doi.org/10.1080/14640746808400161"),
        ("SEP", "https://plato.stanford.edu/"),
        ("Claessen & Hughes 2000", "https://doi.org/10.1145/351240.351266"),
        ("Goldberg 1991", "https://doi.org/10.1145/103162.103163"),
    ],
    next_issue=("Next · Phase 5", "Statistics & Experimental Design", "From proof to probability."),
)
