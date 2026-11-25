"""Text of the Phase 10 images, for the website's sprint and phase pages.

Transcribed line by line from the published images (phases/phase-10-neural-networks/).
Card texts, notes, check lines, the summary's tiles and boxes and the source lines are word for word;
the figure panels are read in words from their labels (fig.panels). The code of each Try It box is
not repeated here: the pages show the sprint's file from code/, which ends with the printed output.
tools/website.py turns this file into the pages.

Marks inside texts: **bold**, *italic*. Thousands are written with a space, as on the images
(200 000); the pages keep each group together with a no-break space. A literal multiplication
asterisk is not used on these images; "·" and "×" are printed as such.

Regions: where each part sits on the image, in pixels of the 2160 × 2700 PNG (x0, y0, x1, y1),
measured on the images. The page lights the part of the image whose text is being read.
"""

PHASE = dict(
    n=10,
    accents={31: "#b5562a", 32: "#b5562a"},
    regions={
        "head": (56, 310, 2104, 580), "fig": (56, 592, 2104, 992),
        "01": (56, 1012, 692, 1424), "02": (708, 1012, 1344, 1424),
        "03": (56, 1436, 692, 1848), "04": (708, 1436, 1344, 1848),
        "06": (56, 1860, 692, 2272), "07": (708, 1860, 1344, 2272),
    },
    summary_regions={
        "head": (60, 60, 1320, 690), "figure": (1390, 270, 2090, 710),
        "tile-0": (80, 796, 552, 1252), "tile-1": (590, 796, 1062, 1252), "tile-2": (1100, 796, 1572, 1252),
        "tile-3": (1610, 796, 2082, 1252),
        "block-0": (80, 1286, 552, 1742), "block-1": (590, 1286, 1062, 1742), "block-2": (1100, 1286, 1572, 1742),
        "references": (1610, 1286, 2082, 1742), "block-3": (80, 1778, 552, 2222), "next": (590, 1778, 2082, 2222),
    },
)

SPRINTS = {
    31: dict(
        regions={"05": (1360, 1012, 2104, 1918), "R": (1360, 1934, 2104, 2272)},
        em="Multilayer",
        names="McCulloch · Rosenblatt · Minsky · Papert · Rumelhart",
        fig=dict(
            label="Fig. 1",
            title="XOR: one line fails, one hidden layer works · same data as code 05",
            panels=[
                ("Input space", [
                    "a square with axes x₁ and x₂, ticks 0 and 1",
                    "filled blue points at top left and bottom right, open orange rings at bottom left and top right",
                    "0.5 inside the shaded square, between two dashed red lines",
                    "best line: 0.5 for all four",
                    "any line: 3 of 4 at most",
                ]),
                ("Hidden layer by hand · §6.1", [
                    "x₁ and x₂ each feed two Σ units through weights: ▭ all = 1",
                    "top unit c = 0, then a ReLU to h₁; bottom unit c = -1, then a ReLU to h₂",
                    "ReLU max(0, z)",
                    "h₁ goes to out with +1, h₂ with -2; out is a Σ unit",
                    "out = 0, 1, 1, 0 · exactly XOR",
                ]),
                ("Hidden space", [
                    "axes with ticks 1 (up) and 1, 2 (across)",
                    "open orange rings at the origin and at top right; one filled blue point on the axis at 1, marked ×2",
                    "a green line; the shaded side below it reads out 1",
                    "*h₁ − 2h₂ = 0.5*",
                    "one line now works",
                    "(0,1), (1,0) → (1,0)",
                ]),
                ("100 seeds", [
                    "a grid of dots, one per seed, green and red; one red dot boxed",
                    "2 hidden: 77 solve (green), 23 freeze (red)",
                    "4 hidden: 100 solve",
                ]),
            ],
            notes_title="Net notes · ① - ④",
            notes=[
                ("Line", "The best line answers 0.5 for all four. The perceptron loops: from epoch 2 every epoch ends "
                         "on the same weights."),
                ("Hidden", "Two ReLU units, weights set by hand (Goodfellow et al. 2016), send (0, 1) and (1, 0) to one point."),
                ("Split", "In hidden space one line separates: h₁ − 2h₂ gives 0, 1, 1, 0."),
                ("Train", "100 seeds of gradient descent: 2 hidden units solve 77, 4 solve 100. Seed 6 (boxed) freezes at 0.5."),
            ],
        ),
        cards=[
            dict(no="01", title="One Neuron, One Line", tag="Unit", items=[
                "Sum weighted inputs, fire past a threshold: an idea from McCulloch & Pitts (1943)",
                "Its border is one straight line: w·x + b = 0",
                "Rosenblatt (1958) made it learn. Modern rule: after a mistake, add error × input",
            ], note="Rosenblatt’s Mark I machine kept its weights in an array of potentiometers (Smithsonian)."),
            dict(no="02", title="A Promise, If…", tag="Novikoff", items=[
                "If one line separates the classes, the rule stops after a finite number of mistakes (Novikoff 1962)",
                "AND: no miss from epoch 6",
                "XOR: from epoch 2 every epoch ends on the same weights. A loop, not slow progress",
            ], note="No line separates XOR, so the theorem promises nothing."),
            dict(no="03", title="What XOR Asks", tag="XOR", items=[
                "Answer 1 when exactly one input is on",
                "The best straight line answers 0.5 for all four (Goodfellow et al. 2016, §6.1)",
                "Minsky & Papert (1969) proved limits of one-layer perceptrons, not of networks",
            ], note="“The book that killed neural nets” is the official history Olazaran (1996) examined, not a theorem."),
            dict(no="04", title="Bend the Space", tag="Hidden", items=[
                "Two ReLU units move (0, 1) and (1, 0) onto one point: (1, 0)",
                "In that new space one line works: h₁ − 2h₂ gives 0, 1, 1, 0",
                "Without a nonlinearity, stacked layers collapse into one linear map",
            ], note="The network does not find a better line. It builds a space where a line is enough."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "One wide enough hidden layer can approximate any continuous function on a bounded box "
                "(Cybenko 1989; Hornik et al. 1989)",
                "That proves the weights exist, not that training finds them (Goodfellow et al. §6.4.1)",
            ], note="Count the seeds that succeed. Here 23 of 100 runs froze at 0.5, still there after 200 000 steps."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Rerun with 1, 3 and 8 hidden units (here: 0, 99 and 100 of 100)",
                "Add direct input-to-output wires (Rumelhart et al. 1986) and retry 1 hidden unit",
                "Swap sigmoid for tanh; recount the freezes",
                "Train the perceptron on OR and NAND",
            ], note="Seed 6 is the first run that freezes. Start there."),
        ],
        tryit=dict(versions="PYTHON 3.13.15",
                   check="Check: 1 − 2·0 = 1 · 2 − 2·1 = 0 · 77 + 23 = 100 · loss of seed 6: 1.389 ≈ 2 ln 2 = 1.386 "
                         "· numpy 2.5.3"),
        sources=[
            ("McCulloch & Pitts (1943). *A Logical Calculus of the Ideas Immanent in Nervous Activity.* "
             "Bull. Math. Biophys. 5, 115–133", "https://doi.org/10.1007/BF02478259"),
            ("Rosenblatt (1958). *The Perceptron: A Probabilistic Model for Information Storage and Organization in the "
             "Brain.* Psychol. Rev. 65(6), 386–408", "https://doi.org/10.1037/h0042519"),
            ("Novikoff (1962). *On Convergence Proofs on Perceptrons.* Symp. Math. Theory of Automata 12, 615–622",
             "https://apps.dtic.mil/sti/tr/pdf/AD0298258.pdf"),
            ("Minsky & Papert (1969). *Perceptrons.* MIT Press", "https://doi.org/10.7551/mitpress/11301.001.0001"),
            ("Rumelhart, Hinton & Williams (1986). *Learning Internal Representations by Error Propagation.* "
             "*Parallel Distributed Processing*, vol. 1, ch. 8, MIT Press", "https://doi.org/10.7551/mitpress/5236.001.0001"),
            ("Cybenko (1989). *Approximation by Superpositions of a Sigmoidal Function.* MCSS 2(4), 303–314",
             "https://doi.org/10.1007/BF02551274"),
            ("Hornik, Stinchcombe & White (1989). *Multilayer Feedforward Networks Are Universal Approximators.* "
             "Neural Netw. 2(5), 359–366", "https://doi.org/10.1016/0893-6080(89)90020-8"),
            ("Goodfellow, Bengio & Courville (2016). *Deep Learning*, ch. 6. MIT Press",
             "https://www.deeplearningbook.org/contents/mlp.html"),
            ("Olazaran (1996). *A Sociological Study of the Official History of the Perceptrons Controversy.* "
             "Soc. Stud. Sci. 26(3), 611–659", "https://doi.org/10.1177/030631296026003005"),
        ],
    ),
    32: dict(
        regions={"05": (1360, 1012, 2104, 2012), "R": (1360, 2024, 2104, 2272)},
        em="Training",
        names="Rumelhart · Glorot · He · Ioffe",
        fig=dict(
            label="Fig. 1",
            title="One net, four ways to train it · 200 points, two moons · same data as code 05",
            panels=[
                ("Gradient check", [
                    "x → h → p → L, four circles in a row",
                    "forward: keep outputs (arrows left to right)",
                    "backward: multiply slopes (arrows right to left)",
                    "backprop 0.0033105346",
                    "finite diff. 0.0033105346",
                    "all 13 weights, one by one: max rel. error 3.7 × 10⁻¹⁰",
                    "one slope left out of backward(): 0.1443 · caught",
                ]),
                ("Loss by step · `η`", [
                    "loss on a log scale, 0.1 to 100, against step (full batch, 200 points), 0 to 2 000",
                    "dashed line: start 0.549",
                    "η 30 · 563 at step 3 (a red dot at the top)",
                    "η 0.01 · ends at 0.293 (gold curve)",
                    "η 1 · ends at 0.048 (green curve)",
                    "η 30 · then a 4-step cycle (red band)",
                ]),
                ("Zero init", [
                    "16 identical circles, each marked with a minus sign",
                    "16 hidden units identical after 2 000 steps",
                    "1 distinct · acc 0.885",
                ]),
                ("Error signal by layer", [
                    "log scale, 10⁻⁹ to 10⁻³, against hidden layer (1 = nearest the input), 1 to 12",
                    "ReLU, He · 1 ÷ 12 = 0.61 (green, flat near the top)",
                    "sigmoid · 1 ÷ 12 = 1.0 × 10⁻⁷ (red, a straight rise from layer 1 to layer 12)",
                ]),
            ],
            notes_title="Net notes · ① - ④",
            notes=[
                ("Check", "Backprop and a finite difference agree to 10 decimals; leave one slope out and the check fails."),
                ("Step", "Same net, three learning rates. η 30 jumps to 563, then cycles and never beats its start."),
                ("Start", "From all-zero weights every unit gets the same gradient: 16 units train as 1."),
                ("Depth", "12 layers at the start of training: sigmoid starves layer 1; ReLU with He weights keeps the signal."),
            ],
        ),
        cards=[
            dict(no="01", title="Backward Pass", tag="Chain rule", items=[
                "Forward: keep each layer’s output. Backward: multiply slopes from the loss to each weight",
                "It only computes the gradient; gradient descent learns (Goodfellow et al. §6.5)",
                "Rumelhart, Hinton & Williams (1986) made it famous",
            ], note="Older than that: Linnainmaa 1970, among others (Griewank 2012)."),
            dict(no="02", title="Check the Gradient", tag="Check", items=[
                "Compare backprop with a finite difference: (L(w + εv) − L(w − εv)) ÷ 2ε",
                "Mine: 0.0033105346 both ways; all 13 weights agree to 3.7 × 10⁻¹⁰",
                "Drop one activation slope from backward(): 0.1443 against 0.0033. Caught",
            ], note="Run the check once on a tiny net before trusting any curve."),
            dict(no="03", title="The Learning Rate", tag="Step", items=[
                "η 0.01: loss 0.293 after 2 000 steps, still creeping. η 1: 0.048, accuracy 0.98",
                "η 30: loss 563 at step 3, then a 4-step cycle that never gets below the start (0.549)",
                "On a bowl of curvature λ each step multiplies the error by (1 − ηλ): it grows once η > 2/λ",
            ], note="Too large a step can go uphill (Goodfellow et al. §4.3)."),
            dict(no="04", title="Break the Symmetry", tag="Init", items=[
                "All-zero weights: every hidden unit gets the same gradient; 16 units stay one (accuracy 0.885)",
                "Random weights, variance gain ÷ fan-in: 1 for sigmoid, 2 for ReLU (He et al. 2015)",
                "Glorot & Bengio (2010): random starts can saturate sigmoid’s top hidden layer",
            ], note="Randomness here is not noise. It lets units specialise."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Sigmoid’s slope is at most 0.25. In 12 sigmoid layers, layer 1 got 1.0 × 10⁻⁷ of layer 12’s error "
                "signal: the vanishing gradient Bengio, Simard & Frasconi (1994) analysed in recurrent nets",
                "Batch norm helps (Ioffe & Szegedy 2015), but Santurkar et al. (2018) trace it to a smoother landscape, "
                "not ‘internal covariate shift’",
            ], note="Plot the loss every run: a sawtooth is a diagnosis."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Sweep η = 0.1, 3, 10 (here: 0.126, 0.044, 0.328)",
                "Start the ReLU net from zeros: loss stays at 0.693 = ln 2",
                "Put tanh in the 12-layer stack (here: 0.12)",
                "Delete one line of backward(); let the check catch it",
            ], note="Seeds 1–5 at η 1: loss 0.048 to 0.053."),
        ],
        tryit=dict(versions="PYTHON 3.13.15",
                   check="Check: |a − n| ÷ a = 5.8 × 10⁻¹⁰ · 6.67 × 10⁻¹⁰ ÷ 6.62 × 10⁻³ = 1.0 × 10⁻⁷ · 1.72 ÷ 2.84 = 0.61 "
                         "· numpy 2.5.3 · scikit-learn 1.9.1"),
        sources=[
            ("Rumelhart, Hinton & Williams (1986). *Learning Representations by Back-Propagating Errors.* "
             "Nature 323, 533–536", "https://doi.org/10.1038/323533a0"),
            ("Griewank (2012). *Who Invented the Reverse Mode of Differentiation?* Doc. Math. ISMP, 389–400",
             "https://doi.org/10.4171/DMS/6/38"),
            ("Bengio, Simard & Frasconi (1994). *Learning Long-Term Dependencies with Gradient Descent Is Difficult.* "
             "IEEE TNN 5(2), 157–166", "https://doi.org/10.1109/72.279181"),
            ("Glorot & Bengio (2010). *Understanding the Difficulty of Training Deep Feedforward Neural Networks.* "
             "PMLR 9, 249–256", "https://proceedings.mlr.press/v9/glorot10a.html"),
            ("He et al. (2015). *Delving Deep into Rectifiers.* ICCV", "https://doi.org/10.1109/ICCV.2015.123"),
            ("Ioffe & Szegedy (2015). *Batch Normalization: Accelerating Deep Network Training by Reducing Internal "
             "Covariate Shift.* PMLR 37, 448–456", "https://proceedings.mlr.press/v37/ioffe15.html"),
            ("Santurkar et al. (2018). *How Does Batch Normalization Help Optimization?* NeurIPS 31",
             "https://proceedings.neurips.cc/paper/2018/hash/905056c1ac1dad141560467e0a99e1cf-Abstract.html"),
            ("Goodfellow et al. (2016). *Deep Learning*, ch. 4, 6", "https://www.deeplearningbook.org/"),
        ],
    ),
}

SUMMARY = dict(
    style="catalog",
    kicker="Phase 10 · Summary · Sprints 31–32 of 90",
    em="Neural",
    sub="from one straight line to a trained network",
    dek="A line that fails, a hidden layer that bends, and the "
        "training that finds it: two sprints, every number rerun in code.",
    badges=["2 sprints, 2 code runs", "Verified sources", "One phase project"],
    figure=dict(label="Figure", lines=[
        "A dark code window",
        "a small network: two inputs, two Σ units, one Σ output · XOR · 2-2-1",
        "a falling curve that flattens · loss by step",
        "five tags beside it: XOR · Hidden Layer · Backprop · Step Size · Init",
    ]),
    tiles=[
        dict(colour="#b5562a", sprint=31, title="One Line Fails", tag="Sprint 31",
             text="No line splits XOR. My perceptron looped from epoch 2."),
        dict(colour="#2e7d4f", sprint=31, title="Bend the Space", tag="Sprint 31",
             text="Two ReLU units send (0,1) and (1,0) to one point; one line then works."),
        dict(colour="#2453a0", sprint=32, title="Gradient Check", tag="Sprint 32",
             text="Backprop and a finite difference agreed to 3.7 × 10⁻¹⁰ on all 13 weights."),
        dict(colour="#c0392b", sprint=32, title="Step & Start", tag="Sprint 32",
             text="η 30 never beat its start; zero weights trained 16 units as one."),
    ],
    blocks=[
        dict(title="Now I Can", tag="Outcome", colour="#6b3f78",
             text="Wire a net by hand, train it, check its gradient, read its loss."),
        dict(title="Mistakes Avoided", tag="Lessons", colour="#c0392b",
             text="“The book killed neural nets”, one lucky seed, zero weights, blind η."),
        dict(title="Habits Kept", tag="Practice", colour="#2e7d4f",
             text="Count seeds that succeed, check gradients, plot every loss curve."),
        dict(title="Phase Project", colour="#2453a0",
             text="One numpy net: XOR by hand, then two moons with its gradient checked, η swept, seeds counted."),
    ],
    references_title="Trusted Sources",
    references=[
        ("Rosenblatt 1958", "https://doi.org/10.1037/h0042519"),
        ("Minsky & Papert 1969", "https://doi.org/10.7551/mitpress/11301.001.0001"),
        ("Rumelhart et al. 1986", "https://doi.org/10.1038/323533a0"),
        ("Glorot & Bengio 2010", "https://proceedings.mlr.press/v9/glorot10a.html"),
    ],
    next_issue=("Next · Phase 11", "Transformers & Vector Spaces", "From networks to meaning."),
)
