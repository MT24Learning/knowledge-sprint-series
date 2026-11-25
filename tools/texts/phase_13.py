"""Text of the Phase 13 images, for the website's sprint and phase pages.

Transcribed line by line from the published images (phases/phase-13-semantic-search-and-retrieval/).
Card texts, notes, check lines, the summary's sections and the source lines are word for word;
the figure panels are read in words from their labels (fig.panels), with the printed captions in
italics. The code of each Try It box is not repeated here: the pages show the sprint's file from
code/, which ends with the printed output. tools/website.py turns this file into the pages.

Marks inside texts: **bold**, *italic*. Thousands are written with a space, as on the images
(1 400); the pages keep each group together with a no-break space.

Regions: where each part sits on the image, in pixels of the 2160 × 2700 PNG (x0, y0, x1, y1),
measured on the images. The page lights the part of the image whose text is being read.
"""

PHASE = dict(
    n=13,
    accents={39: "#2b4f8f", 40: "#6d3f8f", 41: "#1f7a6d"},
    regions={
        "head": (56, 320, 2104, 580), "fig": (56, 594, 2104, 990),
        "01": (56, 990, 668, 1424), "02": (684, 990, 1296, 1424),
        "03": (56, 1414, 668, 1848), "04": (684, 1414, 1296, 1848),
        "06": (56, 1838, 668, 2272), "07": (684, 1838, 1296, 2272),
    },
    summary_regions={
        "head": (60, 330, 1440, 820), "figures": (1474, 336, 2084, 888), "abstract": (60, 920, 1330, 1285),
        "highlights": (60, 1300, 1330, 1655), "methods": (60, 1670, 1330, 1940),
        "misreadings": (1336, 923, 2080, 1714), "issue": (1336, 1726, 2080, 1945),
        "box-0": (80, 1956, 724, 2160), "box-1": (758, 1956, 1402, 2160), "box-2": (1436, 1956, 2080, 2160),
        "references": (60, 2176, 1470, 2300), "next": (1496, 2180, 2082, 2312),
    },
)

SPRINTS = {
    39: dict(
        regions={"05": (1312, 1012, 2104, 2073), "R": (1312, 2082, 2104, 2272)},
        em="BM25",
        names="Cleverdon · Spärck Jones · Robertson",
        fig=dict(
            title="1 400 abstracts, 225 questions · Cranfield (`1960s`) · same data as code 05",
            panels=[
                ("Posting lists", [
                    "*query 3 · how many abstracts hold*",
                    "of: 1 394 · weight 0.00",
                    "in: 1 241 · weight 0.12",
                    "heat: 254 · weight 1.71",
                    "conduction: 43 · weight 3.47",
                    "composite: 9 · weight 4.99",
                    "slabs: 6 · weight 5.37",
                    "*rare word → long weight, short list*",
                ]),
                ("Build-up", [
                    "*nDCG@10, mean of 225 questions*",
                    "count 0.026 · +rare 0.252 · +cap 0.326 · +length 0.382",
                    "*BM25 = all four steps*",
                ]),
                ("Cap the repeats", [
                    "*weight of one word vs. its count*",
                    "counting: 10 · BM25, k1 1.2: 1.00 at one mention, 1.96 at ten",
                    "times the word appears, 0 to 10",
                    "*ten mentions weigh 1.96× one*",
                ]),
                ("Same run, 4 ways", [
                    "*BM25 nDCG@10, scored by*",
                    "Cleverdon order: 0.382 · *1 = best, −1 set aside*",
                    "4 = best: 0.307 · *the ir_datasets labels*",
                    "all lines relevant: 0.485 · *−1 counted, grades ignored*",
                    "matched by .I: 0.010 · *scored against the wrong question*",
                    "*the number depends on the reading*",
                ]),
            ],
            notes_title="Index notes",
            notes=[
                ("Postings", "“of” is in 1 394 of 1 400 abstracts and weighs 0.00; “slabs” is in 6 and weighs 5.37."),
                ("Build-up", "Counting matched words scores 0.026. Weighting rare words, capping repeats and scaling by "
                             "length give BM25 0.382."),
                ("Cap", "With k1 1.2 a word seen ten times weighs 1.96× a word seen once, not 10×."),
                ("Ways", "One run reads 0.307 to 0.485 by convention, and 0.010 if questions are matched by their .I numbers."),
            ],
        ),
        cards=[
            dict(no="01", title="The Inverted Index", tag="Index", items=[
                "One list per word: the abstracts that hold it, with counts",
                "A query reads only its own words’ lists; 7 471 lists cover 1 400 abstracts",
                "“the” is in 1 391 abstracts, “flutter” in 56",
            ], note="Manning, Raghavan & Schütze (2008), ch. 1."),
            dict(no="02", title="Rare Words Weigh More", tag="IDF", items=[
                "Spärck Jones (1972): weight a word by how few documents use it",
                "Counting every match: nDCG@10 0.026. Weighting rare words: 0.252",
                "“of” and “in” match almost every abstract, so they tell almost nothing",
            ], note="Added first, this step brings 63% of the gain; added last, 26%."),
            dict(no="03", title="BM25: Cap and Scale", tag="BM25", items=[
                "Repeats saturate: with k1 1.2, ten mentions weigh 1.96× one",
                "Long abstracts are scaled down (b 0.75): 0.326 → 0.382",
                "Robertson & Zaragoza (2009): 1.2 < k1 < 2 and 0.5 < b < 0.8 work in many settings",
            ], note="Claim tested: “the page that repeats your words most wins.” Counting alone: 0.026."),
            dict(no="04", title="Scoring a Ranking", tag="nDCG", items=[
                "Cranfield (1960s): paper authors set the questions and graded the papers they cited",
                "Grade 1 = a complete answer … 4 = minimum interest (Cleverdon)",
                "nDCG@10 (common log2 form) rewards good grades near the top (Järvelin & Kekäläinen 2002)",
            ], note="The paper coded −1, read as each question’s base paper, is set aside: Cleverdon removed base papers."),
            dict(no="06", title="General Notes", tag="Data", items=[
                "Judgments number questions 1–225; the query file’s .I runs to 365. Matched by .I: 0.010",
                "One paper per question is coded −1. It reads like the question’s source paper: BM25 ranks it first 92 times",
                "ir_datasets labels 4 “complete answer” and −1 “no interest”: the reverse of the readme",
            ], note="Bridge: 393 of 1 612 judged pairs share no rare word (Furnas et al. 1987)."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Stem the words (Porter): 4 820 words, nDCG@10 0.409",
                "Sweep k1 0.5–2 and b 0–1: the best cell (k1 2.0, b 0.75) gives 0.390",
                "Pick k1 and b on half the questions, score the other half (Sprint 20)",
            ], note="Tuning on all 225 questions grades your own exam."),
        ],
        tryit=dict(versions="PYTHON 3.13.17 · NUMPY 2.5.3",
                   check="Check: (0.252 − 0.026) ÷ (0.382 − 0.026) = 0.63 · 10 × 2.2 ÷ 11.2 = 1.96\n"
                         "393 ÷ 1 612 = 0.24"),
        sources=[
            ("Cleverdon, Mills & Keen (1966) ASLIB Cranfield Research Project, vol. 1",
             "https://dspace.lib.cranfield.ac.uk/handle/1826/861"),
            ("Spärck Jones (1972) J. Doc. 28(1), 11–21", "https://doi.org/10.1108/eb026526"),
            ("Robertson & Walker (1994) SIGIR, 232–241", "https://doi.org/10.1007/978-1-4471-2099-5_24"),
            ("Robertson & Zaragoza (2009) FnTIR 3(4), 333–389", "https://doi.org/10.1561/1500000019"),
            ("Järvelin & Kekäläinen (2002) ACM TOIS 20(4), 422–446", "https://doi.org/10.1145/582415.582418"),
            ("Manning, Raghavan & Schütze (2008) *Introduction to Information Retrieval*, CUP",
             "https://doi.org/10.1017/CBO9780511809071"),
            ("Furnas, Landauer, Gomez & Dumais (1987) CACM 30(11), 964–971", "https://doi.org/10.1145/32206.32212"),
            ("Glasgow IR group, Cranfield collection and cranqrel.readme · ir_datasets, cranfield",
             "https://ir.dcs.gla.ac.uk/resources/test_collections/cran/"),
        ],
    ),

    40: dict(
        regions={"05": (1312, 1012, 2104, 1927), "R": (1312, 1936, 2104, 2272)},
        em="Hybrid",
        names="Cormack · Thakur · Lin",
        fig=dict(
            title="One collection, five retrievers · Cranfield 1 400 · same data as code 05",
            panels=[
                ("Five retrievers", [
                    "*nDCG@10, mean of 225 questions*",
                    "GloVe mean 0.102 · BM25 + GloVe 0.258 · WordLlama 0.340 · BM25 0.382 · BM25 + WordLlama 0.395",
                    "*fusion helps only with a good partner*",
                ]),
                ("Question by question", [
                    "*nDCG@10: BM25 (x) vs WordLlama (y)*, 0 to 1",
                    "WordLlama wins 75 · BM25 wins 119 · ties 31",
                    "*p = 0.0012 for the mean gap of −0.042*",
                ]),
                ("Fuse by rank", [
                    "*question 52 · score = Σ 1 ÷ (60 + rank)*",
                    "doc · grade · BM25 · WordL. · fused",
                    "306 · 2 · 3 · 1 · 1",
                    "1215 · — · 1 · 12 · 2",
                    "326 · 4 · 13 · 2 · 3",
                    "550 · — · 6 · 9 · 4",
                    "306: 1 ÷ 63 + 1 ÷ 61 = 0.0323",
                    "nDCG@10 0.41 → 0.82",
                    "*— = not judged · grade 2 beats grade 4*",
                ]),
                ("Is +0.013 real?", [
                    "*100 000 random sign flips, hybrid − BM25*",
                    "observed +0.013 · p ≈ 0.18 · axis -0.03 to +0.03",
                    "*red: flips at least as far out*",
                ]),
            ],
            notes_title="Index notes",
            notes=[
                ("Retrievers", "WordLlama scores 0.340, BM25 0.382; fused by rank 0.395. BM25 + GloVe falls to 0.258."),
                ("Questions", "WordLlama wins 75 questions and loses 119; 31 tie. Mean gap −0.042, p = 0.0012."),
                ("Fuse", "Doc 306 is 3rd for BM25 and 1st for WordLlama, so it leads the fused list."),
                ("Real?", "A gap of +0.013 or more turns up in about 18% of sign flips (p ≈ 0.18): not shown."),
            ],
        ),
        cards=[
            dict(no="01", title="Text to One Vector", tag="Dense", items=[
                "A text becomes a point; nearness is the cosine (Sprint 33)",
                "GloVe mean: 50 numbers per abstract, words averaged",
                "WordLlama: 256 numbers from a token table trained for similarity, then averaged (Miller 2024)",
            ], note="Dense search began with LSI (Deerwester et al. 1990). Neither model here reads word order."),
            dict(no="02", title="Keywords Still Win Here", tag="Claim", items=[
                "Claim: “search by meaning beats keyword search.” Here WordLlama 0.340 < BM25 0.382",
                "It wins 75 questions and loses 119 (p = 0.0012)",
                "BEIR, 18 data sets: “BM25 is a robust baseline” (Thakur et al. 2021)",
            ], note="Verdict: fails here, for a small static model on 1960s aerodynamics."),
            dict(no="03", title="Fuse by Rank", tag="RRF", items=[
                "Reciprocal rank fusion: add 1 ÷ (60 + rank) from each list (Cormack et al. 2009)",
                "Ranks need no score scaling: BM25 scores and cosines live on different scales",
                "k barely matters: 10 → 0.400 · 60 → 0.395 · 100 → 0.396",
            ], note="Cormack et al. fixed k = 60 in a pilot and kept it through validation."),
            dict(no="04", title="Is +0.013 Real?", tag="Test", items=[
                "Paired randomization test: flip the sign of each question’s gap 100 000 times",
                "Hybrid − BM25 = +0.013, p ≈ 0.18: not shown better on 225 questions",
                "A paired t-test agrees (p = 0.18); sign and Wilcoxon tests detect less (Smucker et al. 2007)",
            ], note="A bigger mean is not yet a better system."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "“Hybrid always helps” fails: BM25 + GloVe 0.258 < BM25 alone",
                "Lin (2018): neural rankers were often shown to beat weak or untuned baselines",
                "On Sprint 39’s 393 word-mismatch pairs WordLlama ranks 250 of them higher: median rank 296 vs 479",
            ], note="Bridge: meaning finds what words miss, but only 11 of 393 reach its top 10. Fuse, then test per question."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Load a transformer encoder (DPR, Karpukhin et al. 2020) and rerun all five",
                "Weight the fusion: 2 ÷ (60 + rank) for BM25, then retest",
                "Score only the mismatch pairs: which retriever finds them?",
            ], note="My container could not download one; yours may."),
        ],
        tryit=dict(versions="WORDLLAMA 0.4.0.POST1",
                   check="Check: 0.340 − 0.382 = −0.042 · 0.395 − 0.382 = +0.013 · 75 + 119 + 31 = 225 · gensim 4.4.0"),
        sources=[
            ("Thakur, Reimers, Rücklé, Srivastava & Gurevych (2021) BEIR, NeurIPS 2021", "https://arxiv.org/abs/2104.08663"),
            ("Cormack, Clarke & Büttcher (2009) SIGIR, 758–759", "https://doi.org/10.1145/1571941.1572114"),
            ("Karpukhin et al. (2020) EMNLP, 6769–6781", "https://doi.org/10.18653/v1/2020.emnlp-main.550"),
            ("Smucker, Allan & Carterette (2007) CIKM, 623–632", "https://doi.org/10.1145/1321440.1321528"),
            ("Lin (2018) SIGIR Forum 52(2), 40–51", "https://doi.org/10.1145/3308774.3308781"),
            ("Pennington, Socher & Manning (2014) GloVe, EMNLP, 1532–1543", "https://doi.org/10.3115/v1/D14-1162"),
            ("Miller (2024) WordLlama, github.com/dleemiller/WordLlama (MIT)", "https://github.com/dleemiller/WordLlama"),
            ("Deerwester et al. (1990) JASIS 41(6), 391–407",
             "https://doi.org/10.1002/(SICI)1097-4571(199009)41:6<391::AID-ASI1>3.0.CO;2-9"),
            ("Cleverdon, Mills & Keen (1966) ASLIB Cranfield Research Project",
             "https://dspace.lib.cranfield.ac.uk/handle/1826/861"),
        ],
    ),

    41: dict(
        regions={"05": (1312, 1012, 2104, 1991), "R": (1312, 2000, 2104, 2272)},
        em="Working",
        names="Lewis · Rajpurkar · Barnett",
        fig=dict(
            title="Retrieval side of RAG · Cranfield 1 400 · same data as code 05",
            panels=[
                ("The pipeline", [
                    "*what the code builds, top to bottom*",
                    "question → BM25: top k passages → top score ≥ 14.6? (no: abstain) → prompt with [n] citations → language model",
                    "*dashed: not run here, no model in reach*",
                ]),
                ("Recall ceiling", [
                    "*share of questions with a judged passage*",
                    "k passages returned 1 · 3 · 5 · 10 · 20: .511 · .671 · .769 · .853 · .907",
                    "*at k 5, 52 of 225 get nothing judged*",
                ]),
                ("Answerable or not?", [
                    "*top-1 BM25 score, 225 questions each*",
                    "answerable vs hidden · floor 14.6 · AUC 0.599 · scores 0 to 60",
                    "*84% of hidden ones still pass*",
                ]),
                ("The hand-off", [
                    "*printed by build_prompt(), first 30 chars*",
                    "Answer only from these; cite […",
                    "[859] flutter of aerodynamical…",
                    "[1008] free-flight measurement…",
                    "[948] panel flutter tests on f…",
                    "Q: how does heating change pan…",
                    "“how do i bake bread” → ABSTAIN · top score 8.9 < 14.6",
                    "*off-topic stops; a near miss does not*",
                ]),
            ],
            notes_title="Index notes",
            notes=[
                ("Pipeline", "Retrieve, check a score floor, then build a prompt that numbers its sources. No model is called here."),
                ("Ceiling", "A judged passage reaches the top 5 for 0.769 of questions; 52 of 225 get none."),
                ("Hidden", "Hide every judged passage: the top score barely drops (22.5 vs 19.9), AUC 0.599."),
                ("Hand-off", "The floor stops bread (8.9) but lets 84% of hidden questions through."),
            ],
        ),
        cards=[
            dict(no="01", title="Retrieve, Then Generate", tag="RAG", items=[
                "Lewis et al. (2020): a retriever fetches passages, a generator writes from them",
                "Sources can be updated without retraining, and cited",
                "The answer can be no better than what the retriever hands over",
            ], note="This sprint tests the retriever half, on real judgments."),
            dict(no="02", title="Recall Sets the Ceiling", tag="Recall", items=[
                "A judged passage in the top 1 · 5 · 20: 0.511 · 0.769 · 0.907",
                "At k 5, 52 of 225 questions get no judged passage",
                "Barnett et al. (2024) list it as a failure point: “missed the top ranked documents”",
            ], note="Five abstracts already carry 869 words on average."),
            dict(no="03", title="It Always Hands Back k", tag="Claim", items=[
                "Claim: “if the answer is not in your documents, RAG will tell you”",
                "Hide each question’s judged papers: top score 22.5 → 19.9, AUC 0.599",
                "A floor that keeps 90% of answerable questions lets 84% of the hidden ones through",
            ], note="Verdict: fails for the retriever’s top score here. Judgments are not exhaustive."),
            dict(no="04", title="Cite or Abstain", tag="Prompt", items=[
                "Number every passage [n] so each sentence can be traced",
                "SQuAD 2.0 asks systems to “abstain from answering” when no answer is supported (Rajpurkar et al. 2018)",
                "“Bake bread” scores 8.9 and stops; a near miss does not",
            ], note="An abstain rule needs its own test set."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Retrieval does not end hallucination: RAG legal tools hallucinated on 17–33% of queries (Magesh et al. 2025)",
                "Long contexts are used unevenly; the middle suffers (Liu et al. 2024)",
                "Test the retriever alone (recall at k, hidden answers) before judging the answers",
            ], note="Bridge: Barnett et al.’s first failure point is missing content. Measure it."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Swap in Sprint 40’s hybrid: top-5 recall 0.782 against 0.769",
                "Write 20 questions the collection cannot answer; count what passes",
                "Plug in a language model and check every [n] it cites",
            ], note="A small gain, untested: run Sprint 40’s randomization test on it."),
        ],
        tryit=dict(versions="PYTHON 3.13.17 · NUMPY 2.5.3",
                   check="Check: 52 ÷ 225 = 0.231 = 1 − 0.769 · 22.5 − 19.9 = 2.6 · floor = 10th percentile of answerable scores"),
        sources=[
            ("Lewis et al. (2020) NeurIPS 33, 9459–9474",
             "https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html"),
            ("Barnett, Kurniawan, Thudumu, Brannelly & Abdelrazek (2024) *Seven Failure Points When Engineering a RAG System*, CAIN",
             "https://doi.org/10.1145/3644815.3644945"),
            ("Rajpurkar, Jia & Liang (2018) ACL, 784–789", "https://doi.org/10.18653/v1/P18-2124"),
            ("Magesh, Surani, Dahl, Suzgun, Manning & Ho (2025) J. Empir. Leg. Stud. 22(2), 216–242",
             "https://doi.org/10.1111/jels.12413"),
            ("Liu et al. (2024) *Lost in the Middle*, TACL 12, 157–173", "https://doi.org/10.1162/tacl_a_00638"),
            ("Robertson & Zaragoza (2009) FnTIR 3(4), 333–389", "https://doi.org/10.1561/1500000019"),
            ("Cleverdon, Mills & Keen (1966) ASLIB Cranfield Research Project",
             "https://dspace.lib.cranfield.ac.uk/handle/1826/861"),
        ],
    ),
}

SUMMARY = dict(
    issue="Vol. 2 · No. 3 · October 2026",
    ribbon=("Phase 13 · Summary · Sprints 39–41 of 90", "Every number rerun in code"),
    kicker="Phase summary · Semantic Search & Retrieval",
    em="Semantic",
    dek="From counting words to handing passages to a model: what search finds on real judged data, and what it "
        "cannot tell you it missed.",
    figures=[
        (39, "The build-up", [
            "count 0.026 · +rare 0.252 · +cap 0.326 · +length 0.382",
            "*nDCG@10, 225 questions*",
            "**BM25 0.382**",
            "*counting alone 0.026*",
        ]),
        (40, "Five retrievers", [
            "GloVe mean 0.102 · BM25+GloVe 0.258 · WordLlama 0.340 · BM25 0.382 · BM25+WordL. 0.395",
        ]),
        (41, "Recall ceiling", [
            "k 1: 0.511 · k 5: 0.769 · k 20: 0.907 (k 3 and k 10 marked, unlabelled)",
            "*questions with a judged passage in top k*",
            "**52 of 225 miss at k 5**",
        ]),
    ],
    abstract=(
        "This issue scores three kinds of search on one real test collection: 1 400 aerodynamics abstracts and 225 "
        "questions graded by the people who asked them (Cranfield, 1960s). Sprint 39 built BM25 from an inverted "
        "index and found three traps in the files and a popular loader. Sprint 40 added two embedding models and "
        "fused them with BM25 by rank. Sprint 41 tested the retriever half of a RAG pipeline: what reaches the top "
        "k, and what it hands over when the answer is not there. Each sprint put a popular claim to code; none held "
        "as usually stated."
    ),
    highlights=[
        (39, "Counting matched words: nDCG@10 **0.026**; BM25 **0.382** on 225 questions."),
        (39, "One BM25 run reads **0.307** to **0.485** by scoring convention."),
        (40, "WordLlama **0.340** < BM25 **0.382** (p 0.0012); fused **0.395**, p 0.18."),
        (41, "A judged passage in the top 5 for **0.769** of questions; **52** get none."),
        (41, "Answers hidden: top score **22.5** → **19.9**, AUC **0.599**."),
    ],
    methods=(
        "Three scripts on the Cranfield collection (Glasgow copy), each re-derived by an independent implementation "
        "(sparse matrices and scikit-learn’s ndcg_score; gensim’s mean vector; scikit-learn’s AUC) before rendering. "
        "Grades follow Cleverdon (1 = complete answer); the paper coded −1, read as each question’s base paper "
        "(ir_datasets reads it as “no interest”), is set aside. Python 3.13.17 · numpy 2.5.3 · gensim 4.4.0 · "
        "WordLlama 0.4.0."
    ),
    misreadings=[
        ("Search ranks pages by how often your words appear.",
         "Counting matches scores 0.026; rare-word weights, capped repeats and length scaling give 0.382.",
         "Spärck Jones 1972 · Robertson & Zaragoza 2009"),
        ("A test score belongs to the system.",
         "The same BM25 run reads 0.307 to 0.485 by convention, and 0.010 with the wrong question IDs.",
         "Cleverdon, Mills & Keen 1966 · Järvelin & Kekäläinen 2002"),
        ("Search by meaning beats keyword search.",
         "A trained embedding scored 0.340 against BM25’s 0.382 here, losing 119 of 225 questions.",
         "Thakur et al. 2021"),
        ("Hybrid search always helps.",
         "With GloVe the fusion fell to 0.258; with WordLlama it gained +0.013, p 0.18.",
         "Cormack, Clarke & Büttcher 2009 · Smucker et al. 2007"),
        ("RAG tells you when the answer is not there.",
         "With the answers hidden, a BM25 retriever’s top score barely drops (AUC 0.599); 84% still pass.",
         "Barnett et al. 2024 · Rajpurkar, Jia & Liang 2018"),
    ],
    boxes=[
        ("Now I Can", "Build an inverted index and BM25, score a ranking with nDCG@10, fuse two retrievers by rank "
                      "and test the gain per question."),
        ("Mistakes Avoided", "Matching questions by the wrong ID, counting a base paper as relevant, calling +0.013 a "
                             "win, trusting a score floor."),
        ("Phase Project", "One notebook on a judged collection: BM25, an embedding, rank fusion, recall at k and a "
                          "hidden-answer test."),
    ],
    references=[
        ("Cleverdon, Mills & Keen (1966) ASLIB Cranfield Research Project",
         "https://dspace.lib.cranfield.ac.uk/handle/1826/861"),
        ("Spärck Jones (1972) J. Doc. 28", "https://doi.org/10.1108/eb026526"),
        ("Robertson & Zaragoza (2009) FnTIR 3(4)", "https://doi.org/10.1561/1500000019"),
        ("Järvelin & Kekäläinen (2002) ACM TOIS 20(4)", "https://doi.org/10.1145/582415.582418"),
        ("Thakur et al. (2021) BEIR, NeurIPS", "https://arxiv.org/abs/2104.08663"),
        ("Cormack, Clarke & Büttcher (2009) SIGIR", "https://doi.org/10.1145/1571941.1572114"),
        ("Smucker, Allan & Carterette (2007) CIKM", "https://doi.org/10.1145/1321440.1321528"),
        ("Lewis et al. (2020) NeurIPS 33",
         "https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html"),
        ("Barnett et al. (2024) CAIN", "https://doi.org/10.1145/3644815.3644945"),
        ("Rajpurkar, Jia & Liang (2018) ACL", "https://doi.org/10.18653/v1/P18-2124"),
        ("Magesh et al. (2025) J. Empir. Leg. Stud. 22(2)", "https://doi.org/10.1111/jels.12413"),
    ],
    next_issue=("Vol. 2 · No. 4", "AI Security & Robustness", "From retrieval to attack."),
)
