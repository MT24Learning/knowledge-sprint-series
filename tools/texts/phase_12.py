"""Text of the Phase 12 images, for the website's sprint and phase pages.

Transcribed line by line from the published images (phases/phase-12-the-complexity-lens/).
Card texts, notes, check lines, the summary's sections and the source lines are word for word;
the figure panels are read in words from their labels (fig.panels), with the printed captions in
italics. The code of each Try It box is not repeated here: the pages show the sprint's file from
code/, which ends with the printed output. tools/website.py turns this file into the pages.

Marks inside texts: **bold**, *italic*. Thousands are written with a space, as on the images
(1 000); the pages keep each group together with a no-break space. A superscript with no Unicode
form is written as e^{λt}; the pages raise it.

Regions: where each part sits on the image, in pixels of the 2160 × 2700 PNG (x0, y0, x1, y1),
measured on the images. The page lights the part of the image whose text is being read.
"""

PHASE = dict(
    n=12,
    accents={36: "#23628f", 37: "#23628f", 38: "#23628f"},
    # The summary prints each sprint in its own colour (chips, figure labels).
    summary_accents={36: "#23628f", 37: "#3d7a35", 38: "#a24a22"},
    regions={
        "head": (56, 316, 2104, 580), "fig": (56, 592, 2104, 992),
        "01": (56, 1012, 692, 1424), "02": (708, 1012, 1344, 1424),
        "03": (56, 1436, 692, 1848), "04": (708, 1436, 1344, 1848),
        "06": (56, 1860, 692, 2272), "07": (708, 1860, 1344, 2272),
    },
    summary_regions={
        "head": (56, 345, 1440, 800), "figures": (1470, 330, 2090, 886), "abstract": (60, 920, 1330, 1240),
        "highlights": (60, 1250, 1330, 1572), "methods": (60, 1582, 1330, 1820),
        "misreadings": (1330, 916, 2088, 1680), "issue": (1330, 1686, 2088, 1915),
        "box-0": (80, 1944, 723, 2140), "box-1": (758, 1944, 1401, 2140), "box-2": (1436, 1944, 2079, 2140),
        "references": (60, 2172, 1440, 2315), "next": (1488, 2168, 2080, 2300),
    },
)

SPRINTS = {
    36: dict(
        regions={"05": (1360, 1012, 2104, 1962), "R": (1360, 1972, 2104, 2272)},
        em="Chaos",
        names="Poincaré · Lorenz · May · Feigenbaum · Palmer",
        fig=dict(
            title="Lorenz (1963) simulated + a real laser · same data as code 05",
            panels=[
                ("Twin runs", [
                    "x(t) of two runs from t 14.5 to 22.5: one line until the dashed line at t 20.0, then they part",
                    "*x(t): starts 10⁻⁸ apart*",
                    "*dashed line: gap reaches 1*",
                ]),
                ("Horizon", [
                    "t when the twins differ by 1 (axis 10 to 30) against the first error, -2 to -12: "
                    "points on one dashed straight line, from 4.4 to 29.3",
                    "**+2.54 per digit**",
                    "*log₁₀ of the first error →*",
                    "*y: t when the twins differ by 1*",
                ]),
                ("Real laser", [
                    "five pulses: the measured values (solid) and the closest past stretch (dashed)",
                    "worst error per pulse, on top: 10 · 20 · 37 · 72 · 108",
                    "*next 40 values: measured* (solid line)",
                    "*closest past stretch* (dashed line)",
                    "*top: worst error per pulse*",
                ]),
                ("Period doubling", [
                    "long-run x for r from 2.8 to 4.0: one branch splits again and again, "
                    "then fills a band from the dashed line at 3.57",
                    "*x → rx(1 − x), long run*",
                    "**gaps shrink by δ → 4.669**",
                ]),
            ],
            notes_title="Survey notes",
            notes=[
                ("Twins", "One rule, two starts 10⁻⁸ apart. The runs match until t 20.0, then differ by more than 1."),
                ("Horizon", "Each 10× sharper start adds 2.54 time units; ten more digits add 24.9. Mean of 24 starts."),
                ("Laser", "Measured data: the closest past stretch tracks the next pulses; the worst error per pulse "
                          "goes 10 → 20 → 37 → 72 → 108."),
                ("Route", "Cycles 2 → 4 → 8 ... crowd in before r 3.57; the gap ratio tends to 4.669."),
            ],
        ),
        cards=[
            dict(no="01", title="A Rule, Not Dice", tag="Determinism", items=[
                "Lorenz (1963): three equations, no dice; σ 10 · r 28 · b 8/3",
                "Same start, same end: two runs agree to the last bit at t = 50",
                "Poincaré (1908): “small differences in the initial conditions produce very great ones in the final "
                "phenomena”",
            ], note="Chaos: a fixed rule, no repeats, a sensitive start."),
            dict(no="02", title="Sensitivity", tag="Horizon", items=[
                "A small error grows like e^{λt}; for Lorenz, λ = 0.906 (Sprott)",
                "Mean of 24 starts: twins differ by 1 at t 4.4 from a 10⁻² error, at t 29.3 from 10⁻¹²",
                "So each 10× sharper start buys ln 10 ÷ λ = 2.54 time units",
            ], note="A start 10¹⁰ times sharper lasted only 29.3 ÷ 4.4 = 6.7 times longer."),
            dict(no="03", title="Period Doubling", tag="Route", items=[
                "May (1976): x → rx(1 − x) doubles its cycle 1 → 2 → 4 → 8 ..., then turns chaotic near r 3.57",
                "The ratio of successive gaps tends to δ = 4.669 (Feigenbaum 1978)",
                "The sine map (r/4) sin πx gives 4.669 too",
            ], note="Universality: the number belongs to the route, not to one model."),
            dict(no="04", title="The Butterfly", tag="Misreading", items=[
                "Lorenz’s 1972 title is a question, and he left it “unanswered”",
                "A flap that can set off a tornado “can equally well” prevent one, he added",
                "Palmer (2024): the real butterfly effect (Lorenz 1969b) is a limit smaller errors cannot extend in "
                "many-scale flows",
            ], note="In the 1963 model, sharper starts still buy time (card 02)."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Forecasters run ensembles: ECMWF runs 50 perturbed forecasts plus a control",
                "A widening spread says when to stop trusting the forecast",
                "Real laser: the worst error about doubles over four pulses (10 → 20 → 37 → 72), then 108",
            ], note="“Chaos can’t be predicted”: false short range, true past a horizon."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Call the forecast lost at 5 instead of 1: the slope barely moves (2.56 vs 2.54)",
                "Rerun the laser with other windows (4 · 12 · 24); past data picked 6",
                "Estimate λ by Benettin’s rescaling; I get 0.903",
            ], note="Check: ln 10 ÷ 2.54 = 0.91, close to Sprott’s λ of 0.906."),
        ],
        tryit=dict(versions="PYTHON 3.13.16 · NUMPY 2.5.3",
                   check="Check: ln 10 ÷ 0.906 = 2.54 a digit · 29.3 − 4.4 = 24.9 · 37 ÷ 20 = 1.9 · 72 ÷ 37 = 1.9 · "
                         "108 ÷ 72 = 1.5"),
        sources=[
            ("Poincaré (1908) *Science and Method*, trans. Maitland, p. 68", "https://archive.org/details/cu31924012248179"),
            ("Lorenz (1963) *Deterministic Nonperiodic Flow*, J. Atmos. Sci. 20, 130–141",
             "https://doi.org/10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2"),
            ("Lorenz (1969a) J. Atmos. Sci. 26, 636–646 (analogues)",
             "https://doi.org/10.1175/1520-0469(1969)26<636:APARBN>2.0.CO;2"),
            ("Lorenz (1969b) Tellus 21(3), 289–307 (many scales)", "https://doi.org/10.3402/tellusa.v21i3.10086"),
            ("Lorenz (1972) *Predictability: Does the Flap...?* AAAS talk", "https://eaps4.mit.edu/research/Lorenz/Butterfly_1972.pdf"),
            ("May (1976) Nature 261, 459–467", "https://doi.org/10.1038/261459a0"),
            ("Feigenbaum (1978) J. Stat. Phys. 19(1), 25–52", "https://doi.org/10.1007/BF01020332"),
            ("Palmer (2024) *The Real Butterfly Effect and Maggoty Apples*, Physics Today 77(5), 30–35",
             "https://doi.org/10.1063/pt.eike.hsbz"),
            ("Sprott, *Lyapunov Exponent Spectrum* (UW)", "https://sprott.physics.wisc.edu/chaos/lespec.htm"),
            ("Weigend & Gershenfeld, eds. (1994) *Time Series Prediction*, Addison-Wesley (set A)",
             "https://doi.org/10.4324/9780429492648"),
            ("Hübner, Abraham & Weiss (1989) Phys. Rev. A 40, 6354", "https://doi.org/10.1103/PhysRevA.40.6354"),
            ("ECMWF, *Generation of the Ensemble*",
             "https://confluence.ecmwf.int/spaces/FUG/pages/673550735/Section+5.1+Generation+of+the+Ensemble"),
        ],
    ),
    37: dict(
        regions={"05": (1360, 1012, 2104, 2034), "R": (1360, 2044, 2104, 2272)},
        em="Self-Organisation",
        names="Anderson · Schelling · Bak · Gutenberg · Epstein",
        fig=dict(
            title="Two models + 1 000 real quakes · same data as code 05",
            panels=[
                ("One city, twice", [
                    "two maps of the same 40 × 40 city, before and after: start 0.50 · asks ½ 0.79",
                    "*Each resident asks only that ½ of its neighbours be like it*",
                    "*40 × 40 · 25% empty · seed 37*",
                ]),
                ("Asked vs got", [
                    "the share the city ends with, for asks from .1 to .7: every point above the dashed “asked” line "
                    "and the “start 0.50” line",
                    "0.79 at .5",
                    "*x: share each resident asks for*",
                    "*y: share the city ends with*",
                ]),
                ("Sandpile", [
                    "grains by topplings: 0: 17 037 · 1-9: 4 806 · 10-99: 4 054 · 100-999: 3 282 · 1 000+: 821",
                    "**largest: 5 902**",
                    "*topplings per grain, last 30 000*",
                    "*no typical size, nothing tuned*",
                ]),
                ("Real quakes", [
                    "count of quakes (1 to 1 000, log scale) against M 4.0 to 6.4: one dashed fit, b 1.08 from 4.5; "
                    "dotted lines mark the cuts at 4.5 and 4.7 (b 1.22 from 4.7)",
                    "*quakes of magnitude ≥ M, Fiji*",
                    "*1 000 real events, log scale*",
                ]),
            ],
            notes_title="Survey notes",
            notes=[
                ("City", "Nobody asks for more than half like neighbours; the city goes from 0.50 to 0.79 alike."),
                ("Asked", "Every point is above the line: the city ends more sorted than anyone asked."),
                ("Pile", "Nothing tuned: 57% of grains move nothing, one sets off 5 902 topplings."),
                ("Quakes", "Real data: about ten times fewer per magnitude; b depends on the cut."),
            ],
        ),
        cards=[
            dict(no="01", title="More Is Different", tag="Emergence", items=[
                "Anderson (1972): reducing to simple laws “does not imply the ability to start from those laws and "
                "reconstruct the universe”",
                "Emergent: a pattern of the whole that no single rule states",
                "I find these patterns only by running the rules",
            ], note="Simple parts; the pattern belongs to the whole."),
            dict(no="02", title="Micromotives", tag="Schelling", items=[
                "Schelling (1971): residents move only when too few neighbours are like them",
                "Asking for half, the city ends 0.79 alike; asking for 0.3, it ends 0.65",
                "On his small board he found the effect “slight” near a third, “striking” at a half",
            ], note="Claim tested: “a sorted map means people wanted it sorted.” It fails here."),
            dict(no="03", title="Self-Organised", tag="Criticality", items=[
                "Bak, Tang & Wiesenfeld (1987): a site holding 4 grains gives one to each neighbour",
                "Nothing is tuned, yet avalanches run from 1 to 5 902 topplings",
                "57% of grains move nothing; 821 set off 1 000 or more",
            ], note="Sprint 38 asks whether such a spread earns the name “power law”."),
            dict(no="04", title="Real Quakes", tag="Data", items=[
                "Gutenberg & Richter (1944): log N = a − bM; b ≈ 1 means ten times fewer per magnitude",
                "1 000 Fiji quakes: b = 1.08 ± 0.04 for M ≥ 4.5, the most common magnitude",
                "For M ≥ 4.7, the +0.2 Woessner & Wiemer (2005) advise: b = 1.22",
            ], note="Aki (1965), half-bin shift (Utsu 1966); ± = b ÷ √n."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Epstein (1999): “If you didn’t grow it, you didn’t explain its emergence”; growing it is not proof "
                "either",
                "A sandpile and a fault share a heavy tail; faults are not sandpiles",
                "Mild wishes are enough to sort a model city; that does not show what sorts a real one",
            ], note="Same people, other rule: asking 0.3 ends at 0.65."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Seeds 1–5 at a demand of ½: the city ends 0.78 to 0.80 alike",
                "Move residents to a random empty cell instead of the nearest one that suits them",
                "Fit b for cuts from M 4.3 to 4.7: 0.89 rising to 1.22",
            ], note="Then grow the sandpile to 100 × 100 and compare the largest avalanche."),
        ],
        tryit=dict(versions="PYTHON 3.13.16 · NUMPY 2.5.3",
                   check="Check: 17 037 + 12 963 = 30 000 grains · 10^{1.08} = 12 · 1.08 ÷ √623 = 0.04"),
        sources=[
            ("Anderson (1972) *More Is Different*, Science 177(4047), 393–396",
             "https://doi.org/10.1126/science.177.4047.393"),
            ("Schelling (1971) J. Math. Sociol. 1, 143–186", "https://doi.org/10.1080/0022250X.1971.9989794"),
            ("Bak, Tang & Wiesenfeld (1987) PRL 59(4), 381–384", "https://doi.org/10.1103/PhysRevLett.59.381"),
            ("Gutenberg & Richter (1944) BSSA 34(4), 185–188", "https://doi.org/10.1785/BSSA0340040185"),
            ("Aki (1965) Bull. Earthq. Res. Inst. 43, 237–239", "https://cir.nii.ac.jp/crid/1370567185522869642"),
            ("Utsu (1966) J. Phys. Earth 14(2), 37–40", "https://doi.org/10.4294/jpe1952.14.37"),
            ("Woessner & Wiemer (2005) BSSA 95(2), 684–698", "https://doi.org/10.1785/0120040007"),
            ("Epstein (1999) Complexity 4(5), 41–60",
             "https://doi.org/10.1002/(SICI)1099-0526(199905/06)4:5<41::AID-CPLX9>3.0.CO;2-F"),
            ("R *quakes* data (Harvard PRIM-H; Woodhouse)",
             "https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/quakes.html"),
        ],
    ),
    38: dict(
        regions={"05": (1360, 1012, 2104, 2041), "R": (1360, 2052, 2104, 2272)},
        em="Shape",
        names="Koch · Richardson · Mandelbrot · Zipf · Clauset",
        fig=dict(
            title="Rulers, a coast and a novel · real map + real text · same data as code 05",
            panels=[
                ("Ruler check", [
                    "the Koch curve, drawn in blue: reads 1.259 · true 1.262",
                    "*Koch curve: 7 levels (drawn at 4),*",
                    "*4 rulers: the method checked on a curve whose answer is known*",
                ]),
                ("One island", [
                    "the outline of the island walked with two rulers: 200 km ruler · 2 404 km (purple) and "
                    "50 km ruler · 3 424 km (brown)",
                    "1:10m map",
                ]),
                ("Length by ruler", [
                    "length (axis 2 000 · 4 000 · 8 000) against ruler from 200 km to 1.6 km: four points on a "
                    "dashed line marked D 1.27, then four on a flatter dashed line marked D 1.14",
                    "*ruler shrinks →, length grows ↑*",
                    "*slope eases from 12.5 km down*",
                ]),
                ("Words by rank", [
                    "count of each word (axis 1 · 100 · 10 000) against rank 1 to 16 950: the points follow a "
                    "dashed straight line; R² 0.980 · α 1.94",
                    "dotted line: tail: count ≥ 7",
                    "*Moby Dick: straight line, yet a* **lognormal fits the tail as well**",
                ]),
            ],
            notes_title="Survey notes",
            notes=[
                ("Check", "On a curve whose dimension is known (1.262), my ruler method reads 1.259."),
                ("Island", "The same coast measures 2 404 km with a 200 km ruler and 6 958 km with a 1.6 km one."),
                ("Slope", "D = 1.27 from 200 to 25 km; 1.14 from 12.5 to 1.6 km, near the map’s own 1.4 km point gap."),
                ("Words", "R² 0.980 and a power-law tail (α 1.94), but the lognormal is not ruled out."),
            ],
        ),
        cards=[
            dict(no="01", title="Self-Similar", tag="Dimension", items=[
                "Koch (1904): replace the middle third of each segment by a tent, again and again",
                "4 copies at ⅓ scale: D = log 4 ÷ log 3 = 1.262, between a line and a plane",
                "My ruler method reads 1.259 on it: test a method on a known answer first",
            ], note="A fractal dimension says how fast detail grows as you zoom in."),
            dict(no="02", title="How Long Is Britain?", tag="Coast", items=[
                "Richardson (1961): measured length grows as the ruler shrinks",
                "Mandelbrot (1967) read the slope as a dimension: D = 1.25 for Britain’s west coast",
                "My 1:10m map, whole island: D = 1.27 for rulers 200 to 25 km",
            ], note="Claim tested: “a coast has one true length.” Not without its ruler."),
            dict(no="03", title="Scaling Has a Range", tag="Limits", items=[
                "From 12.5 km down the slope eases to 1.14; the map’s points are a median 1.4 km apart",
                "A map cannot show bays smaller than its own spacing",
                "If D stayed 1.27, length would grow 3.7× over these rulers; it grew 2.89×",
            ], note="Report a dimension with the range of rulers it came from."),
            dict(no="04", title="Power Laws, Tested", tag="Clauset", items=[
                "Zipf (1949): frequency falls with rank; Moby Dick’s rank line has R² 0.980",
                "Clauset et al. (2009): a straight log–log line is “necessary but not sufficient”",
                "Tail from 7 (3 077 words), α 1.94 (theirs 1.95); lognormal not ruled out, as in their p 0.69",
            ], note="Claim tested: “straight on log–log means power law.” The inference fails."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Fit the tail by likelihood, pick its start by KS, test rivals (Clauset’s fit bootstrap not run here)",
                "The lognormal stays in: p 0.95 in the powerlaw package, 0.78 in my own fit",
                "Quote a length with its ruler: 2 404 and 6 958 km are both Britain",
            ], note="Two optimisers, different numbers, the same verdict."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Austen’s Emma: the lognormal beats the power law (p 0.04)",
                "Sprint 37’s 50 × 50 sandpile: tail from 916 topplings (925 avalanches); both rivals win",
                "South Africa’s coast, picked as one of the smoothest, gives D = 1.02 (Mandelbrot 1967)",
            ], note="Check: 6 958 ÷ 2 404 = 2.89 for a 128× finer ruler."),
        ],
        tryit=dict(versions="NUMPY 2.5.3 · POWERLAW 2.0.0",
                   check="Check: 128^{0.27} = 3.7 vs 6 958 ÷ 2 404 = 2.89 · log 4 ÷ log 3 = 1.262"),
        sources=[
            ("Koch (1904) Arkiv för Matematik 1, 681", "https://iremi.univ-reunion.fr/IMG/pdf/von_koch_1904.pdf"),
            ("Richardson (1961) Gen. Syst. Yearb. 6, 139", "https://archive.org/details/generalsystemsye0006unse"),
            ("Mandelbrot (1967) *How Long Is the Coast of Britain?*, Science 156(3775), 636–638",
             "https://doi.org/10.1126/science.156.3775.636"),
            ("Zipf (1949) *Human Behavior and the Principle of Least Effort*, Addison-Wesley",
             "https://archive.org/details/in.ernet.dli.2015.90211"),
            ("Clauset, Shalizi & Newman (2009) *Power-Law Distributions in Empirical Data*, SIAM Rev. 51(4), 661–703",
             "https://doi.org/10.1137/070710111"),
            ("Alstott et al. (2014) *powerlaw*, PLoS ONE 9(1), e85777", "https://doi.org/10.1371/journal.pone.0085777"),
            ("Natural Earth 1:10m Admin 0",
             "https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/"),
            ("Melville (1851) *Moby Dick*, Austen (1815) *Emma*: NLTK Gutenberg", "https://www.nltk.org/book/ch02.html"),
        ],
    ),
}

SUMMARY = dict(
    issue="Vol. 2 · No. 2 · October 2026",
    ribbon=("Phase 12 · Summary · Sprints 36–38 of 90", "Every number rerun in code"),
    kicker="Phase summary · The Complexity Lens",
    em="Complexity",
    dek="From a rule with no dice to a coast with no single length: what simple rules can build, and how far their "
        "patterns can be trusted.",
    figures=[
        (36, "The horizon", [
            "*lost at t, by first error*",
            "six points on a dashed line, first error 10⁻² · 10⁻⁴ · 10⁻⁶ · 10⁻⁸ · 10⁻¹⁰ · 10⁻¹²: 4.4 at the first, "
            "29.3 at the last",
            "**+2.54 per 10× sharper**",
            "*mean of 24 starts*",
        ]),
        (37, "Asked vs got", [
            "*asked (x) vs got (y)*",
            "seven points on a solid line for asks .1 to .7, all above the dashed line; 0.79 at .5",
            "**asks ½, ends 0.79**",
            "*dashed: got = asked*",
        ]),
        (38, "Length by ruler", [
            "*Great Britain, 1:10m map*",
            "eight points from ruler 200 km to 1.6 km: 2 404 km at the first, 6 958 km at the last",
            "**D 1.27, then 1.14**",
            "*eases near the map gap*",
        ]),
    ],
    abstract=(
        "This issue follows simple rules to the patterns they make. Sprint 36 ran a rule with no dice and still lost "
        "the forecast: each 10× sharper start bought only 2.54 more time units. Sprint 37 let residents and grains of "
        "sand follow local rules, watched city-wide sorting and avalanches appear, then checked 1 000 real quakes. "
        "Sprint 38 measured Britain with eight rulers and Moby Dick’s words with a likelihood test. Each sprint put a "
        "popular claim to code, and none survived as usually stated."
    ),
    highlights=[
        (36, "Each 10× sharper start buys **2.54** time units; ten more digits buy **24.9**."),
        (36, "Real laser, nearest-past forecast: worst error per pulse **10 → 20 → 37 → 72 → 108**."),
        (37, "Asking for half like neighbours, the city ends **0.79** alike (start **0.50**)."),
        (37, "Fiji quakes: b = **1.08** for M ≥ 4.5, **1.22** for M ≥ 4.7; the cut sets b."),
        (38, "Britain: **2 404** km with a 200 km ruler, **6 958** km with a 1.6 km one."),
    ],
    methods=(
        "Three scripts, each run before rendering and re-derived by an independent implementation (pure-Python "
        "loops, bisection, stack toppling, my own power-law fit). Data: Santa Fe laser set A, the R quakes set "
        "(Fiji), Natural Earth 1:10m, Moby Dick (Gutenberg). Python 3.13.16 · numpy 2.5.3 · powerlaw 2.0.0 · "
        "pyproj 3.8.0."
    ),
    misreadings=[
        ("Chaos means it can’t be predicted.",
         "Short range works; each 10× sharper start adds 2.54 time units.",
         "Lorenz 1963 · Sprott"),
        ("A butterfly’s flap sets off tornadoes.",
         "Lorenz left his 1972 question “unanswered”; a flap could as well prevent one.",
         "Lorenz 1972 · Palmer 2024"),
        ("A sorted map means people wanted it sorted.",
         "Asking for half, a model city ends 0.79 alike.",
         "Schelling 1971 · Epstein 1999"),
        ("A coast has one true length.",
         "Britain grows from 2 404 to 6 958 km as the ruler shrinks.",
         "Richardson 1961 · Mandelbrot 1967"),
        ("A straight log–log line proves a power law.",
         "Moby Dick: R² 0.980, yet a lognormal fits the tail as well.",
         "Clauset, Shalizi & Newman 2009"),
    ],
    boxes=[
        ("Now I Can", "Measure a forecast horizon, grow a pattern from local rules, estimate b and D, and test a power "
                      "law against its rivals."),
        ("Mistakes Avoided", "Reading chaos as randomness, a grown pattern as proof, a length without its ruler, a "
                             "straight log–log line as a law."),
        ("Phase Project", "One notebook: Lorenz twins and a laser forecast, a model city and a sandpile, Britain by "
                          "eight rulers, words by likelihood."),
    ],
    references=[
        ("Lorenz (1963) J. Atmos. Sci. 20", "https://doi.org/10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2"),
        ("May (1976) Nature 261", "https://doi.org/10.1038/261459a0"),
        ("Feigenbaum (1978) J. Stat. Phys. 19", "https://doi.org/10.1007/BF01020332"),
        ("Palmer (2024) Physics Today 77(5)", "https://doi.org/10.1063/pt.eike.hsbz"),
        ("Anderson (1972) Science 177", "https://doi.org/10.1126/science.177.4047.393"),
        ("Schelling (1971) J. Math. Sociol. 1", "https://doi.org/10.1080/0022250X.1971.9989794"),
        ("Bak, Tang & Wiesenfeld (1987) PRL 59", "https://doi.org/10.1103/PhysRevLett.59.381"),
        ("Gutenberg & Richter (1944) BSSA 34", "https://doi.org/10.1785/BSSA0340040185"),
        ("Epstein (1999) Complexity 4(5)",
         "https://doi.org/10.1002/(SICI)1099-0526(199905/06)4:5<41::AID-CPLX9>3.0.CO;2-F"),
        ("Mandelbrot (1967) Science 156", "https://doi.org/10.1126/science.156.3775.636"),
        ("Clauset et al. (2009) SIAM Rev. 51(4)", "https://doi.org/10.1137/070710111"),
        ("Lorenz (1972) AAAS", "https://eaps4.mit.edu/research/Lorenz/Butterfly_1972.pdf"),
        ("Richardson (1961) Gen. Syst. Yearb. 6", "https://archive.org/details/generalsystemsye0006unse"),
        ("Sprott, Lyapunov Exponent Spectrum", "https://sprott.physics.wisc.edu/chaos/lespec.htm"),
    ],
    next_issue=("Vol. 2 · No. 3", "Semantic Search & Retrieval", "From patterns to search."),
)
