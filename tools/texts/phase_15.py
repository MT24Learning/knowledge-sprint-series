"""Text of the Phase 15 images, for the website's sprint and phase pages.

Transcribed line by line from the published images (phases/phase-15-structured-claims-and-ground-truth/).
Card texts, notes, check lines, the summary's sections and the source lines are word for word;
the figure panels are read in words from their labels (fig.panels), with the printed captions in
italics. The code of each Try It box is not repeated here: the pages show the sprint's file from
code/, which ends with the printed output. tools/website.py turns this file into the pages.

Marks inside texts: **bold**, *italic*. Thousands are written with a space, as on the images
(1 535); the pages keep each group together with a no-break space.

Regions: where each part sits on the image, in pixels of the 2160 × 2700 PNG (x0, y0, x1, y1),
measured on the images. The page lights the part of the image whose text is being read.
"""

PHASE = dict(
    n=15,
    accents={45: "#2f6f4f", 46: "#2b4aa0", 47: "#b3263c", 48: "#9a6b12"},
    regions={
        "head": (56, 320, 2104, 580), "fig": (56, 594, 2104, 990),
        "01": (56, 1012, 668, 1424), "02": (684, 1012, 1296, 1424),
        "03": (56, 1436, 668, 1848), "04": (684, 1436, 1296, 1848),
        "06": (56, 1860, 668, 2272), "07": (684, 1860, 1296, 2272),
    },
    summary_regions={
        "head": (56, 350, 1360, 880), "figures": (1380, 360, 2080, 904), "abstract": (56, 940, 1340, 1255),
        "highlights": (56, 1265, 1340, 1595), "methods": (56, 1595, 1340, 1860),
        "misreadings": (1352, 940, 2080, 1684), "issue": (1352, 1696, 2080, 1950),
        "box-0": (80, 1980, 726, 2166), "box-1": (758, 1980, 1402, 2166), "box-2": (1434, 1980, 2080, 2166),
        "references": (56, 2180, 1420, 2290), "next": (1436, 2188, 2080, 2300),
    },
)

SPRINTS = {
    45: dict(
        regions={"05": (1312, 1012, 2104, 2042), "R": (1312, 2060, 2104, 2272)},
        em="Structure",
        names="W3C · Vrandečić · Richardson",
        fig=dict(
            title="One claim, many qualifiers · CLIMATE-FEVER · same data as code 05",
            panels=[
                ("One claim, two records", [
                    "*“Currently, humans are emitting around 29 billion tonnes of carbon dioxide into the* "
                    "atmosphere per year.” · claim 2657 · SUPPORTS",
                    "a bare triple: humans → emit → CO₂ · *true, but vague*",
                    "the same claim, qualified: amount 29 billion tonnes · rate per year · time currently · "
                    "hedge around (not in the word list)",
                ]),
                ("Qualifiers in 1 535 claims", [
                    "number 43.5% · time 33.0% · comparison 21.8% · hedge 20.2% · negation 19.6% · source 16.9% · "
                    "scope 13.4% · condition 8.3%",
                    "**any qualifier: 1 251 of 1 535 = 81.5%**",
                    "*a word-list rule: rough in both directions*",
                ]),
                ("Qualifiers per claim", [
                    "0: 284 · 1: 433 · 2: 394 · 3: 263 · 4+: 161",
                    "*kinds of qualifier found*",
                ]),
                ("REFUTES share", [
                    "all 16.5% · no neg. 13.7% · negation **27.9%**",
                    "*301 claims carry a negation*",
                ]),
            ],
            notes_title="Verification notes",
            notes=[
                ("Pick", "Claim 2657 is labelled SUPPORTS. The bare triple keeps none of its qualifiers: "
                         "29 billion tonnes · per year · currently."),
                ("Count", "A word list finds a qualifier in 1 251 of 1 535 claims (81.5%). Number and time lead."),
                ("Spread", "Most claims carry one to three kinds; 161 carry four or more."),
                ("Link", "With a negation, a claim is labelled REFUTES 27.9% of the time, against 16.5% overall."),
            ],
        ),
        cards=[
            dict(no="01", title="A Claim's Parts", tag="Definition", items=[
                "An RDF triple: subject, predicate, object (W3C RDF 1.1)",
                "Real claims add qualifiers: amount, time, scope, hedge, negation, condition, source",
                "Wikidata: property, value and qualifiers form the claim; with references, a statement",
            ], note="W3C: a relation with more than two parts “can only be indirectly expressed in RDF”."),
            dict(no="02", title="One Fact, One Triple", tag="Claim fails", claim=True, items=[
                "Claim: “every fact fits in one subject–predicate–object triple”",
                "1 251 of 1 535 real claims (81.5%) carry a qualifier a bare triple drops",
                "Survives as linked triples: a statement node or an RDF 1.2 triple term holds them",
            ], note="Rough list: misses “around”, counts every “will”. Some qualifiers fit inside one predicate."),
            dict(no="03", title="Qualifiers as Fields", tag="Practice", items=[
                "Store each qualifier as its own field: amount, unit, period, scope, hedge, source",
                "PICO does this for clinical questions: patient or problem, intervention, comparison, outcome",
                "Keep the exact sentence and its source too",
            ], note="Wikibase: a claim with references is not, for that reason, true."),
            dict(no="04", title="Qualifiers & Verdicts", tag="Evidence", items=[
                "With a negation: REFUTES 27.9%; without one: 13.7%",
                "With a number: NOT ENOUGH INFO 33.7%; without: 28.7%",
                "A label rates the whole sentence, qualifiers included",
            ], note="A pattern, not a cause: the claims were collected, not sampled at random."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Retelling drops qualifiers: of 182 press releases on correlational studies, 33% made a stronger "
                "causal claim than the paper (Sumner et al. 2014)",
                "Check a claim against its exact words, not a summary of it",
            ], note="Bridge: store qualifiers as fields, or a check will test an easier claim than the one made."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Add “about” and “around” to the hedge list and recount",
                "Mark the qualifiers of 30 random claims by hand: what did the list miss or invent?",
                "Write claim 2657 as a Wikidata-style statement",
            ], note="Then compare your hand count with the code’s."),
        ],
        tryit=dict(versions="PY 3.13.18 · STANDARD LIBRARY",
                   check="Check: 1 251 ÷ 1 535 = 81.5% · 284 + 433 + 394 + 263 + 161 = 1 535 · 1 535 − 284 = 1 251"),
        sources=[
            ("W3C (2014) *RDF 1.1 Concepts and Abstract Syntax*", "https://www.w3.org/TR/rdf11-concepts/"),
            ("W3C (2026) *RDF 1.2 Concepts and Abstract Data Model*, Candidate Recommendation Draft",
             "https://www.w3.org/TR/rdf12-concepts/"),
            ("Vrandečić & Krötzsch (2014) *Wikidata: A Free Collaborative Knowledgebase*, CACM 57(10), 78–85",
             "https://doi.org/10.1145/2629489"),
            ("Wikibase DataModel Primer (MediaWiki)", "https://www.mediawiki.org/wiki/Wikibase/DataModel/Primer"),
            ("Richardson, Wilson, Nishikawa & Hayward (1995) *The well-built clinical question*, ACP J Club 123(3), "
             "A12–A13", "https://doi.org/10.7326/ACPJC-1995-123-3-A12"),
            ("Sumner et al. (2014) BMJ 349, g7015", "https://doi.org/10.1136/bmj.g7015"),
            ("Diggelmann et al. (2020) *CLIMATE-FEVER*, arXiv 2012.00614", "https://arxiv.org/abs/2012.00614"),
        ],
    ),

    46: dict(
        regions={"05": (1312, 1012, 2104, 2040), "R": (1312, 2056, 2104, 2272)},
        em="Agreement",
        names="Krippendorff · Cohen · Aroyo",
        fig=dict(
            title="The votes behind the labels · 7 675 pairs · same data as code 05",
            panels=[
                ("One claim, five ties", [
                    "*“Current CO₂ levels are the highest in 15 million years.”*",
                    "S R · *…may be the highest in the last 20 million years.* → N",
                    "S R · *…is the highest for 14 million years.* → N",
                    "N R · *…larger variations in past epochs…* → N",
                    "N R · *…have gone up by approximately 35 percent…* → N",
                    "N R · *…currently 100 ppm higher than pre-industrial levels.* → N",
                    "**label: NOT ENOUGH INFO** · S · R · N votes",
                    "*could also have been S, R or DISPUTED*",
                ]),
                ("Votes per pair", [
                    "2 votes: 5 340 · **57.1%**",
                    "3 votes: 1 554 · **32.5%**",
                    "4 votes: 761 · **42.7%**",
                    "5 votes: 20 · **20.0%**",
                    "*dark: all votes the same*",
                ]),
                ("Agreement", [
                    "raw agreement **58.7%** · Krippendorff **α 0.334**",
                    "α marked on a 0 to 1 scale: .667 tentative · .800 rely on it",
                    "*thresholds: Krippendorff (2004)*",
                    "*FEVER: Fleiss κ 0.684 (other task, measure)*",
                ]),
                ("What NEI means", [
                    "4 930 NEI evidence labels: ties 2 501 · 2 429",
                    "*50.7% are split votes*",
                    "1 535 claim labels: 693 · 842",
                    "*45.1% depend on the tie rule*",
                    "685 ties hold both SUPPORTS and REFUTES",
                ]),
            ],
            notes_title="Verification notes",
            notes=[
                ("Pick", "Claim 2661: each of its five sentences got two different votes. Every tie became N, so the "
                         "claim is NOT ENOUGH INFO."),
                ("Votes", "5 340 of 7 675 pairs have two votes. Two readers agreed on 57.1% of them."),
                ("Alpha", "α 0.334 on the released votes, the paper’s own figure; Krippendorff asks for .800."),
                ("NEI", "Half of all NOT ENOUGH INFO labels (50.7%) record a split, not silent evidence."),
            ],
        ),
        cards=[
            dict(no="01", title="Ground Truth", tag="Definition", items=[
                "A gold label is a judgement made by people under a written rule",
                "CLIMATE-FEVER: majority vote per pair; a tie becomes NOT ENOUGH INFO",
                "FEVER’s annotators reached Fleiss κ 0.684 on claims written from Wikipedia",
            ], note="Aroyo & Welty (2015) name “One Truth” the first of seven myths of annotation."),
            dict(no="02", title="The Label Is the Truth", tag="Claim fails", claim=True, items=[
                "Claim: “the gold label is what the annotators agreed on”",
                "2 501 of 7 675 pairs (32.6%) were ties, all recorded as NOT ENOUGH INFO",
                "685 ties hold a SUPPORTS and a REFUTES vote; 693 claims (45.1%) could change if ties were "
                "settled another way",
            ], note="The paper states its rule: read it before you score."),
            dict(no="03", title="Measuring Agreement", tag="Method", items=[
                "Raw agreement of vote pairs: 58.7%",
                "α removes chance matches: 0.334",
                "Cohen’s κ needs the same two coders on every item; here each pair has 2–5 anonymous votes, "
                "which α handles",
            ], note="Krippendorff (2004): rely on α ≥ .800; use .667–.800 only for tentative conclusions."),
            dict(no="04", title="One Vote Can Move It", tag="Evidence", items=[
                "2 335 pairs have three or more votes",
                "Dropping one vote can change the label for 503 of them (21.5%)",
                "More votes do not remove real disagreement (Pavlick & Kwiatkowski 2019)",
            ], note="Their finding: disagreements “persist as we collect more ratings”."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Publish the votes, not only the label: models can learn from the spread (Uma et al. 2021)",
                "Report α with the data and say how ties were settled",
            ], note="Bridge: score a model on split items separately; a tie records split readers, not evidence "
                    "that says nothing."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Compute α for pairs with three or more votes",
                "Break ties toward SUPPORTS or REFUTES and recount the claim labels",
                "Compare α across the four claim labels",
            ], note="Then decide which label set you would trust as a test."),
        ],
        tryit=dict(versions="PY 3.13.18 · STANDARD LIBRARY",
                   check="Check: 2 501 ÷ 4 930 = 50.7% · 693 ÷ 1 535 = 45.1% · 5 340 + 1 554 + 761 + 20 = 7 675"),
        sources=[
            ("Diggelmann et al. (2020) *CLIMATE-FEVER*, arXiv 2012.00614", "https://arxiv.org/abs/2012.00614"),
            ("Krippendorff (2004) *Content Analysis*, 2nd ed., p. 241", "https://books.google.com/books?id=q657o3M3C8cC"),
            ("Cohen (1960) Educ. Psychol. Meas. 20(1), 37–46", "https://doi.org/10.1177/001316446002000104"),
            ("Artstein & Poesio (2008) *Inter-Coder Agreement for Computational Linguistics*, CL 34(4), 555–596",
             "https://doi.org/10.1162/coli.07-034-R2"),
            ("Thorne et al. (2018) *FEVER*, NAACL, 809–819", "https://doi.org/10.18653/v1/N18-1074"),
            ("Aroyo & Welty (2015) *Truth Is a Lie*, AI Magazine 36(1), 15–24",
             "https://doi.org/10.1609/aimag.v36i1.2564"),
            ("Pavlick & Kwiatkowski (2019) TACL 7, 677–694", "https://doi.org/10.1162/tacl_a_00293"),
            ("Uma et al. (2021) *Learning from Disagreement*, JAIR 72, 1385–1470", "https://doi.org/10.1613/jair.1.12752"),
        ],
    ),

    47: dict(
        regions={"05": (1312, 1012, 2104, 2046), "R": (1312, 2064, 2104, 2272)},
        em="Evidence",
        names="Thorne · Schuster · Gururangan",
        fig=dict(
            title="The swap test · 7 675 real claim–sentence pairs · same data as code 05",
            panels=[
                ("One claim, right and wrong sentence", [
                    "*“Arctic sea ice is also falling at an accelerated rate.”*",
                    "right sentence · 4 of 4 readers: SUPPORTS",
                    "*“Accelerated decline in the Arctic sea ice.”*",
                    "words: SUPPORTS ✓ · +overlap: SUPPORTS ✓",
                    "wrong sentence · from another claim",
                    "*“In the U.S., Lyme is most common in the New England and Mid-Atlantic states and parts of "
                    "Wisconsin…”*",
                    "words: SUPPORTS ✕ · +overlap: NOT ENOUGH INFO ✓",
                    "*pair 7011 · same folds and models as Code 05*",
                ]),
                ("Balanced accuracy", [
                    "- - chance 0.333",
                    "claim only **0.461** · evid. only 0.438 · claim+ evid. 0.489 · +overlap 0.500",
                    "*5 folds grouped by claim*",
                ]),
                ("The swap test", [
                    "% answered SUPPORTS or REFUTES · - - gold labels 35.8%",
                    "words: right sentence 40.3 · swapped **39.8**",
                    "+ overlap: right sentence 40.4 · swapped **27.6**",
                ]),
                ("Claim words → REFUTES", [
                    "claim-only model, top weights",
                    "#1 no · #2 isn · #3 kills · #4 not · #5 life · #6 insignificant",
                    "*red: a negation (isn = isn’t)*",
                    "*fitted on all 7 675 pairs*",
                ]),
            ],
            notes_title="Verification notes",
            notes=[
                ("Pick", "Pair 7011: four readers said SUPPORTS. Handed a sentence on Lyme disease, the word model "
                         "still says so."),
                ("Score", "No evidence at all: 0.461 (chance 0.333)."),
                ("Swap", "With another claim’s sentence, the claim + evidence model still says SUPPORTS or REFUTES "
                         "for 39.8% of pairs (40.3% with its own)."),
                ("Words", "Three of the six strongest claim-only REFUTES cues are negations: no · isn’t · not."),
            ],
        ),
        cards=[
            dict(no="01", title="Verification", tag="Definition", items=[
                "Input: a claim and a sentence; output SUPPORTS, REFUTES or NOT ENOUGH INFO",
                "FEVER: 185 445 claims written from Wikipedia sentences (Thorne et al. 2018)",
                "CLIMATE-FEVER: 7 675 real claim–sentence pairs; each claim stays in one fold",
            ], note="Grouping by claim keeps a claim’s five sentences out of its own training data (Sprint 20)."),
            dict(no="02", title="A Score Is a Check", tag="Claim fails", claim=True, items=[
                "Claim: “a verifier that scores well is checking the evidence”",
                "Never shown the evidence: 0.461 balanced accuracy (chance 0.333)",
                "Claim + evidence model, wrong sentence: SUPPORTS or REFUTES 39.8% vs 40.3%",
            ], note="Word models on one data set; Schuster et al. found the same with BERT on FEVER."),
            dict(no="03", title="Shortcuts", tag="Evidence", items=[
                "FEVER: a claim-only BERT reached 61.7%, majority baseline 33.3% (Schuster et al. 2019)",
                "NLI: the hypothesis alone gets about 67% of SNLI (Gururangan et al. 2018)",
                "Real claims show the same kind of cue: no · isn’t · not",
            ], note="Geirhos et al. (2020): shortcuts do well on the usual tests and fail to transfer."),
            dict(no="04", title="The Swap Test", tag="Method", items=[
                "Give each claim another claim’s sentence",
                "Only 5.1% share a Wikipedia article with the claim’s own evidence",
                "Schuster et al.’s symmetric set: a leading verifier fell from 81.8% to 58.7%",
            ], note="Strict, not perfect: a few may still touch the topic."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Report claim-only and evidence-only scores beside the full one",
                "A FEVER-trained model scored 38.78% on CLIMATE-FEVER claims, DISPUTED left out "
                "(Diggelmann et al. 2020)",
            ], note="Bridge: run a swap test before trusting a verifier; one overlap feature cut swapped answers "
                    "from 39.8% to 27.6%."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Swap only within the same Wikipedia article and rerun",
                "Add word pairs (bigrams) to the claim-only model: does it climb?",
                "Print the ten claim words with the largest SUPPORTS weights",
            ], note="Then try the overlap feature with a list of stop words removed."),
        ],
        tryit=dict(versions="PY 3.13.18 · SKLEARN 1.9.1",
                   check="Check: 40.3 − 39.8 = 0.5 points · 40.4 − 27.6 = 12.8 points · 0.461 − 0.333 = 0.128"),
        sources=[
            ("Thorne et al. (2018) *FEVER*, NAACL, 809–819", "https://doi.org/10.18653/v1/N18-1074"),
            ("Schuster et al. (2019) *Towards Debiasing Fact Verification Models*, EMNLP-IJCNLP, 3419–3425",
             "https://doi.org/10.18653/v1/D19-1341"),
            ("Gururangan et al. (2018) *Annotation Artifacts in Natural Language Inference Data*, NAACL, 107–112",
             "https://doi.org/10.18653/v1/N18-2017"),
            ("Geirhos et al. (2020) *Shortcut learning in deep neural networks*, Nat. Mach. Intell. 2, 665–673",
             "https://doi.org/10.1038/s42256-020-00257-z"),
            ("Diggelmann et al. (2020) *CLIMATE-FEVER*, arXiv 2012.00614", "https://arxiv.org/abs/2012.00614"),
        ],
    ),

    48: dict(
        regions={"05": (1312, 1012, 2104, 2060), "R": (1312, 2072, 2104, 2272)},
        em="Reference",
        names="Northcutt · Gebru · Bender",
        fig=dict(
            title="Label errors in ten test sets · same data as code 05",
            panels=[
                ("The build chain", [
                    "1 write the labelling rules",
                    "2 label each item twice+ · 46",
                    "3 measure agreement (α) · 46",
                    "4 settle splits, record how · 46",
                    "5 flag suspects with a model · 48",
                    "6 confirm with people · 48",
                    "7 version, digest, datasheet · 48",
                    "*right: the sprint that covers it*",
                ]),
                ("Label errors per test set", [
                    "mnist 0.15% · cifar10 0.54% · cifar100 5.85% · caltech256 1.54% · imagenet 5.83% · "
                    "quickdraw 10.12% (pale) · 20news 1.09% · imdb 2.90% · amazon 3.90% (pale) · audioset 1.35% (grey)",
                    "- - mean 3.33%",
                    "*pale: from samples · grey: as published*",
                ]),
                ("ImageNet: 5 440 flags", [
                    "2 524 · kept: label fine",
                    "1 428 · relabel (3+ agree)",
                    "597 · both labels",
                    "293 · neither label",
                    "598 · split, no majority",
                    "**confirmed errors: 2 916**",
                ]),
                ("One set, 4 versions", [
                    "v1.0 original · — · 50 000 items · 0 edits",
                    "v1.1 relabel 3 of 5 · 214229ed · 50 000 items · 1 428 edits",
                    "v1.2 relabel 5 of 5 · 3b07dbe4 · 50 000 items · 468 edits",
                    "v2.0 drop errors · 0b2fa020 · 47 084 items · 0 edits",
                    "*right: first 8 hex of SHA-256*",
                ]),
            ],
            notes_title="Verification notes",
            notes=[
                ("Chain", "Like a certified material: values, how sure they are, and how they were made."),
                ("Count", "Recounted from the released votes, all nine single-label sets match the paper exactly; "
                          "AudioSet as published. Mean 3.33%."),
                ("Flags", "A model flagged 5 440 ImageNet images; people confirmed 2 916 as errors."),
                ("Name", "Three honest corrections of one set give three digests. A score must name its version."),
            ],
        ),
        cards=[
            dict(no="01", title="A Reference Set", tag="Definition", items=[
                "Items, labels, the rules behind them, and a version",
                "A certified material states values with “uncertainties and traceabilities” (VIM 5.14)",
                "For labels: agreement, known errors, each item’s source",
            ], note="Aroyo & Welty’s seventh myth: “Once Done, Forever Valid”."),
            dict(no="02", title="Clean Test Sets", tag="Claim fails", claim=True, items=[
                "Claim: “a published test set’s labels are correct”",
                "Ten sets (two from samples): mean 3.33% errors; ImageNet 2 916 of 50 000 (5.83%)",
                "An error: fewer than 3 of 5 people agree with the given label",
            ], note="The paper’s abstract rounds ImageNet up to “at least 6%”; its table says 5.83."),
            dict(no="03", title="Flag, Then Confirm", tag="Method", items=[
                "A model flags suspects: confident learning (Northcutt, Jiang & Chuang 2021)",
                "People check them: 2 524 of 5 440 ImageNet flags (46.4%) kept their label",
                "So never relabel on a model’s word alone",
            ], note="AudioSet is multi-label; one rule we inferred gives its 275 exactly, but the paper does not "
                    "state it."),
            dict(no="04", title="Fix, Drop or Mark", tag="Evidence", items=[
                "ImageNet errors: 1 428 relabelled · 597 both labels · 293 neither · 598 split",
                "IMDB: 552 of 725 errors get no sentiment majority (200 voted neutral)",
                "A split is disagreement, not a known right answer (Sprint 46)",
            ], note="Northcutt et al. left multi-label items out of their own analysis."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Name each release by a digest of its content (Sprint 2) and keep the old ones",
                "Ship a datasheet (Gebru et al. 2021) or a data statement (Bender & Friedman 2018) with known errors",
            ], note="Bridge: on ImageNet, ResNet-18 overtakes ResNet-50 if mislabelled test items rise by 6% "
                    "(Northcutt et al. 2021). A ranking depends on the version."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Keep the 842 CLIMATE-FEVER claims whose label survives any tie rule (Sprint 46)",
                "Compare its label shares with the full set",
                "Write a one-page datasheet and a SHA-256 manifest for it",
            ], note="Then rerun Sprint 47’s verifier on both versions."),
        ],
        tryit=dict(versions="PY 3.13.18 · STANDARD LIBRARY",
                   check="Check: 2 916 ÷ 50 000 = 5.83% · 2 524 + 1 428 + 597 + 293 + 598 = 5 440 · "
                         "50 000 − 2 916 = 47 084"),
        sources=[
            ("Northcutt, Athalye & Mueller (2021) *Pervasive Label Errors in Test Sets Destabilize Machine Learning "
             "Benchmarks*, NeurIPS",
             "https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/"
             "f2217062e9a397a1dca429e7d70bc6ca-Abstract-round1.html"),
            ("Northcutt, Jiang & Chuang (2021) *Confident Learning*, JAIR 70, 1373–1411",
             "https://doi.org/10.1613/jair.1.12125"),
            ("cleanlab/label-errors, GitHub (commit 6d5d6b3)",
             "https://github.com/cleanlab/label-errors/tree/6d5d6b31a13216290afc40e5c6319399c4d15c06"),
            ("JCGM 200:2012 (VIM 3), 5.14", "https://doi.org/10.59161/JCGM200-2012"),
            ("Gebru et al. (2021) *Datasheets for Datasets*, CACM 64(12), 86–92", "https://doi.org/10.1145/3458723"),
            ("Bender & Friedman (2018) TACL 6, 587–604", "https://doi.org/10.1162/tacl_a_00041"),
            ("Aroyo & Welty (2015) AI Magazine 36(1), 15–24", "https://doi.org/10.1609/aimag.v36i1.2564"),
        ],
    ),
}

SUMMARY = dict(
    issue="Vol. 2 · No. 5 · November 2026",
    ribbon=("Phase 15 · Summary · Sprints 45–48 of 90", "Every number rerun in code"),
    kicker="Phase summary · Structured Claims & Ground Truth",
    em="Truth",
    dek="A claim’s qualifiers, the votes behind its label, the sentence it is checked against, the test set that "
        "scores it: four checks on real data.",
    figures=[
        (45, "Qualifiers", [
            "1 251 with a qualifier · 284 · **81.5% of** 1 535 claims",
            "number 43.5% · time 33.0% · comparison 21.8%",
            "*a word-list rule, rough in both directions*",
        ]),
        (46, "What NEI means", [
            "ties 2 501 · 2 429 · **50.7% of** 4 930 NEI labels",
            "**α 0.334 (need .800)**",
        ]),
        (47, "The swap test", [
            "% S or R, right vs swapped sentence",
            "words: 40.3 · **39.8**",
            "+ overlap: 40.4 · **27.6**",
            "**claim only: 0.461** (chance 0.333)",
        ]),
        (48, "Label errors", [
            "- - **mean 3.33%** · ImageNet 5.83%",
            "*10 test sets · grey: AudioSet as published*",
        ]),
    ],
    abstract=(
        "This issue follows a claim from a sentence to the test set that scores it. Sprint 45 counted the qualifiers "
        "in 1 535 real climate claims. Sprint 46 rebuilt every label of CLIMATE-FEVER from the 18 486 votes behind it "
        "and measured agreement. Sprint 47 trained simple verifiers and handed them the wrong evidence. Sprint 48 "
        "recounted the label errors of public test sets from the released human votes. Each sprint put a popular "
        "claim to code; none held as usually stated."
    ),
    highlights=[
        (45, "1 251 of 1 535 real claims (81.5%) carry a qualifier a bare triple drops."),
        (46, "2 501 split votes became NOT ENOUGH INFO: half of all 4 930 such labels."),
        (46, "693 of 1 535 claims (45.1%) could change label if ties were settled another way."),
        (47, "Given another claim’s sentence, the verifier said S or R for 39.8% vs 40.3%."),
        (48, "Ten public test sets, nine recounted from the votes: mean 3.33% label errors."),
    ],
    methods=(
        "Four scripts on public data: CLIMATE-FEVER (1 535 claims · 7 675 claim–sentence pairs; Diggelmann et al. "
        "2020) and the Mechanical Turk files of cleanlab/label-errors (Northcutt et al. 2021). Every printed line was "
        "re-derived by an independent implementation before rendering; α also by the krippendorff package. No "
        "language model was run. Python 3.13.18 · numpy 2.5.3 · scikit-learn 1.9.1."
    ),
    misreadings=[
        ("Every fact fits in one subject–predicate–object triple.",
         "81.5% of 1 535 real claims carry a qualifier; linked triples can hold them.",
         "W3C RDF 1.2 · Vrandečić & Krötzsch 2014"),
        ("The gold label is what the annotators agreed on.",
         "α 0.334; 2 501 ties were recorded as NOT ENOUGH INFO.",
         "Krippendorff 2004 · Diggelmann et al. 2020"),
        ("A verifier that scores well is checking the evidence.",
         "Claim only: 0.461 balanced accuracy. Claim + evidence, swapped: S or R in 39.8% vs 40.3%.",
         "Schuster et al. 2019 · Gururangan et al. 2018"),
        ("A published test set’s labels are correct.",
         "Ten sets: mean 3.33% label errors (two from samples); ImageNet 5.83%.",
         "Northcutt, Athalye & Mueller 2021"),
        ("A model’s flag is enough to relabel an item.",
         "2 524 of 5 440 ImageNet flags (46.4%) kept their label.",
         "Northcutt, Jiang & Chuang 2021"),
    ],
    boxes=[
        ("Now I Can", "Turn a claim into fields, measure agreement with α, run a swap test on a verifier and recount "
                      "a test set’s errors."),
        ("Mistakes Avoided", "Storing claims without their qualifiers, reading a tie as silent evidence, trusting a "
                             "score without a claim-only baseline."),
        ("Phase Project", "A verified CLIMATE-FEVER subset: the 842 claims whose label survives any tie rule, with a "
                          "datasheet and a SHA-256 manifest."),
    ],
    references=[
        ("W3C (2026) RDF 1.2 Concepts", "https://www.w3.org/TR/rdf12-concepts/"),
        ("Vrandečić & Krötzsch (2014) CACM 57(10)", "https://doi.org/10.1145/2629489"),
        ("Richardson et al. (1995) ACP J Club 123(3)", "https://doi.org/10.7326/ACPJC-1995-123-3-A12"),
        ("Sumner et al. (2014) BMJ 349", "https://doi.org/10.1136/bmj.g7015"),
        ("Diggelmann et al. (2020) arXiv 2012.00614", "https://arxiv.org/abs/2012.00614"),
        ("Krippendorff (2004) Content Analysis", "https://books.google.com/books?id=q657o3M3C8cC"),
        ("Thorne et al. (2018) NAACL", "https://doi.org/10.18653/v1/N18-1074"),
        ("Aroyo & Welty (2015) AI Magazine 36(1)", "https://doi.org/10.1609/aimag.v36i1.2564"),
        ("Pavlick & Kwiatkowski (2019) TACL 7", "https://doi.org/10.1162/tacl_a_00293"),
        ("Uma et al. (2021) JAIR 72", "https://doi.org/10.1613/jair.1.12752"),
        ("Schuster et al. (2019) EMNLP-IJCNLP", "https://doi.org/10.18653/v1/D19-1341"),
        ("Gururangan et al. (2018) NAACL", "https://doi.org/10.18653/v1/N18-2017"),
        ("Geirhos et al. (2020) Nat. Mach. Intell. 2", "https://doi.org/10.1038/s42256-020-00257-z"),
        ("Northcutt, Athalye & Mueller (2021) NeurIPS",
         "https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/"
         "f2217062e9a397a1dca429e7d70bc6ca-Abstract-round1.html"),
        ("Northcutt, Jiang & Chuang (2021) JAIR 70", "https://doi.org/10.1613/jair.1.12125"),
        ("Gebru et al. (2021) CACM 64(12)", "https://doi.org/10.1145/3458723"),
        ("JCGM 200:2012", "https://doi.org/10.59161/JCGM200-2012"),
    ],
    next_issue=("Vol. 2 · No. 6", "Causality & Information Theory", "From labelled claims to causes and information."),
)
