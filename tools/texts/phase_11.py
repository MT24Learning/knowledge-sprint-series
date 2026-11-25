"""Text of the Phase 11 images, for the website's sprint and phase pages.

Transcribed line by line from the published images (phases/phase-11-transformers-and-vector-spaces/).
Card texts, notes, check lines, the summary's sections and the source lines are word for word;
the figure panels are read in words from their labels (fig.panels), with the printed captions in
italics. The code of each Try It box is not repeated here: the pages show the sprint's file from
code/, which ends with the printed output. tools/website.py turns this file into the pages.

Marks inside texts: **bold**, *italic*. Thousands are written with a space, as on the images
(2 353); the pages keep each group together with a no-break space.

Regions: where each part sits on the image, in pixels of the 2160 × 2700 PNG (x0, y0, x1, y1),
measured on the images. The page lights the part of the image whose text is being read.
"""

PHASE = dict(
    n=11,
    accents={33: "#3a3896", 34: "#3a3896", 35: "#3a3896"},
    # The summary prints each sprint in its own colour (chips, figure labels, box bars).
    summary_accents={33: "#3a3896", 34: "#b5372e", 35: "#a7791a"},
    regions={
        "head": (56, 320, 2104, 576), "fig": (56, 592, 2104, 992),
        "01": (56, 1012, 692, 1424), "02": (708, 1012, 1344, 1424),
        "03": (56, 1436, 692, 1848), "04": (708, 1436, 1344, 1848),
        "06": (56, 1860, 692, 2272), "07": (708, 1860, 1344, 2272),
    },
    summary_regions={
        "head": (60, 345, 1440, 790), "figures": (1480, 336, 2080, 880), "abstract": (70, 920, 1330, 1205),
        "highlights": (70, 1205, 1330, 1510), "methods": (70, 1525, 1330, 1745),
        "misreadings": (1336, 924, 2080, 1714), "issue": (1336, 1734, 2080, 1932),
        "box-0": (80, 1944, 726, 2136), "box-1": (758, 1944, 1402, 2136), "box-2": (1434, 1944, 2080, 2136),
        "references": (76, 2172, 1460, 2280), "next": (1488, 2170, 2080, 2305),
    },
)

SPRINTS = {
    33: dict(
        regions={"05": (1360, 1012, 2104, 1992), "R": (1360, 2002, 2104, 2272)},
        em="Vectors",
        names="Harris · Firth · Mikolov · Pennington · Levy",
        fig=dict(
            label="Fig. 1",
            title="Four readings of one sky · 400 000 words × 50 numbers · same data as code 05",
            panels=[
                ("Angle from “cat”", [
                    "cat at 0° · dog 22.8° · kitten 50.3° · car 68.7° · democracy 87.9°",
                    "a tick at 30°",
                    "*one-hot: every pair at 90°*",
                ]),
                ("Country → capital", [
                    "12 capitals · 21–45°",
                    "random 77–109°",
                    "mean ↑ *dashed*",
                    "*cos 0.61 against 0.02*",
                ]),
                ("King - man + woman", [
                    "*b − a + c, nearest by cosine*",
                    "*king* 0.885 (an input word) · **queen** 0.852 · **throne** 0.766",
                    "*man : doctor :: woman : ?*",
                    "*doctor* 0.905 (an input word) · **nurse** 0.840",
                    "scale 0.70 · 0.80 · 0.90",
                    "*hatched = an input word*",
                    "**skip the inputs → queen, nurse**",
                ]),
                ("One point per word", [
                    "**hot** at the centre · around it **1 cool** · **2 cold** · 3 mix · 4 dry · 5 soft · **6 warm**",
                    "rings at 30° and 40°",
                    "**bank → river: no. 2 353**",
                    "*cos 0.414 · every sense, one point*",
                ]),
            ],
            notes_title="Chart notes",
            notes=[
                ("Angle", "Cosine read as an angle. One-hot code puts every pair at exactly 90°."),
                ("Offset", "12 country → capital offsets lie 21–45° from their mean; 12 random pairs lie 77–109°. "
                           "Sides are for drawing only."),
                ("Skip", "The nearest word to king − man + woman is king. Queen wins only when the three inputs are skipped."),
                ("Sense", "Cold, an antonym, is hot’s 2nd neighbour; river is bank’s 2 353rd. One point holds every sense."),
            ],
        ),
        cards=[
            dict(no="01", title="One-Hot to Dense", tag="Represent", items=[
                "One-hot: one 1 in 400 000 slots; every pair at 90°, so dog is no closer to cat than democracy",
                "Dense: 50 learned numbers; cat–dog 22.8°, cat–democracy 87.9°",
                "Learned inside a language model against “the curse of dimensionality” (Bengio et al. 2003)",
            ], note="Normalise first: cosine reads direction, not length."),
            dict(no="02", title="The Company It Keeps", tag="Use", items=[
                "Harris (1954): “difference of meaning correlates with difference of distribution”",
                "Firth (1957): “You shall know a word by the company it keeps!”",
                "Count neighbours, reweight by PMI, compress by SVD (Deerwester et al. 1990)",
            ], note="Meaning here is a pattern of use; the vectors never see the world."),
            dict(no="03", title="Predict or Count", tag="W2V · GloVe", items=[
                "Skip-gram: vectors “good at predicting the nearby words” (Mikolov et al. 2013)",
                "GloVe: dot products fitted to log co-occurrence counts (Pennington et al. 2014)",
                "With negative sampling it implicitly factorises shifted PMI (Levy & Goldberg 2014)",
            ], note="Tuning explains much of the gap (Levy et al. 2015)."),
            dict(no="04", title="Reading Analogies", tag="3CosAdd", items=[
                "king − man + woman: the nearest word is king (0.885); queen (0.852) is second",
                "Queen wins only if the inputs are skipped: “we discard the input words” (Mikolov et al.)",
                "man : doctor :: woman : ? gives doctor (0.905); nurse needs the skip (Nissim et al. 2020)",
            ], note="Inputs allowed: 3CosAdd falls 0.71 → 0.21 (Nissim et al.); Linzen (2016) got an input back 98% of the time."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Close is not same: cold is hot’s 2nd neighbour; SimLex-999 rates similarity, not association (Hill et al. 2015)",
                "One point per word: river is bank’s 2 353rd neighbour",
                "Vectors learn their corpus, stereotypes included (Caliskan et al. 2017)",
            ], note="Next: attention shapes each word’s vector by its sentence."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Build PPMI + SVD vectors from one book; compare cat’s neighbours with GloVe’s",
                "Run 10 analogies with and without the skip; count the input answers",
                "Find antonyms closer than synonyms; list the neighbours of “spring”",
            ], note="Check: a one-hot pair always gives 90.0 deg."),
        ],
        tryit=dict(versions="PYTHON 3.13.16",
                   check="Check: arccos 0.922 = 22.8° · arccos 0.037 = 87.9° · 0.885 − 0.852 = 0.033 · gensim 4.4.0 · numpy 2.5.3"),
        sources=[
            ("Harris (1954) *Distributional Structure*, Word 10(2–3), 146–162",
             "https://doi.org/10.1080/00437956.1954.11659520"),
            ("Firth (1957) Studies in Linguistic Analysis, Blackwell, 1–32", "https://ci.nii.ac.jp/ncid/BA18741557?l=en"),
            ("Deerwester et al. (1990) JASIS 41(6), 391–407",
             "https://doi.org/10.1002/(SICI)1097-4571(199009)41:6%3C391::AID-ASI1%3E3.0.CO;2-9"),
            ("Bengio et al. (2003) JMLR 3, 1137–1155", "https://www.jmlr.org/papers/v3/bengio03a.html"),
            ("Mikolov, Sutskever, Chen, Corrado & Dean (2013) NeurIPS 26", "https://proceedings.neurips.cc/paper/2013/hash/9aa42b31882ec039965f3c4923ce901b-Abstract.html"),
            ("Pennington, Socher & Manning (2014) *GloVe*, EMNLP, 1532–1543", "https://doi.org/10.3115/v1/D14-1162"),
            ("Levy & Goldberg (2014) NeurIPS 27", "https://proceedings.neurips.cc/paper/2014/hash/b78666971ceae55a8e87efb7cbfd9ad4-Abstract.html"),
            ("Levy, Goldberg & Dagan (2015) TACL 3, 211–225", "https://doi.org/10.1162/tacl_a_00134"),
            ("Linzen (2016) RepEval, 13–18", "https://doi.org/10.18653/v1/W16-2503"),
            ("Nissim, van Noord & van der Goot (2020) CL 46(2), 487–497", "https://doi.org/10.1162/coli_a_00379"),
            ("Hill, Reichart & Korhonen (2015) *SimLex-999*, CL 41(4), 665–695", "https://doi.org/10.1162/COLI_a_00237"),
            ("Caliskan, Bryson & Narayanan (2017) Science 356(6334), 183–186", "https://doi.org/10.1126/science.aal4230"),
        ],
    ),
    34: dict(
        regions={"05": (1360, 1012, 2104, 2046), "R": (1360, 2056, 2104, 2272)},
        em="Attention",
        names="Bahdanau · Luong · Vaswani · Jain · Wiegreffe",
        fig=dict(
            label="Fig. 1",
            title="One formula, four views · GloVe vectors and random keys · same data as code 05",
            panels=[
                ("Bank looks around", [
                    "we .04 · sat .01 · on .06 · the .06 · **river** .05 · **bank** .78",
                    "she .02 · took .02 · a .04 · **loan** .13 · from .05 · the .05 · **bank** .68",
                    "*weights of “bank” · ring = to itself*",
                ]),
                ("Context moves it", [
                    "**“river” · river sentence**: 2 353 → 1 475",
                    "“river” · loan sentence: 2 353 → 2 278",
                    "**“loan” · loan sentence**: 12 ← 52",
                    "“loan” · river sentence: 52 → 87",
                    "scale 10 · 100 · 1 000",
                    "*rank among bank’s neighbours · left = closer*",
                ]),
                ("Why ÷ `√dₖ`", [
                    "*top softmax weight, 10 keys*",
                    "dₖ 4 · var 4.0: raw 0.49 · ÷ √dₖ 0.30",
                    "dₖ 64 · var 63.7: raw 0.86 · ÷ √dₖ 0.32",
                    "dₖ 512 · var 505.5: raw 0.95 · ÷ √dₖ 0.32",
                    "raw · ÷ √dₖ",
                ]),
                ("No peeking ahead", [
                    "rows and columns 1–6 · the cells above the diagonal are crossed out",
                    "**21 of 36 scores kept**",
                    "*row = query · shade = weight*",
                ]),
            ],
            notes_title="Chart notes",
            notes=[
                ("Mirror", "With no learned weights, bank gives 78% of its attention to itself. Real models learn "
                           "W_{Q}, W_{K}, W_{V} to look elsewhere."),
                ("Context", "Still, context moves it: “river” climbs from 2 353rd to 1 475th; “loan” climbs from 52nd to 12th."),
                ("Scale", "Unscaled scores grow with dₖ and softmax picks one winner; ÷ √dₖ keeps the top weight near 0.32."),
                ("Mask", "A decoder hides later tokens: 21 of 36 scores remain and token 1 sees only itself."),
            ],
        ),
        cards=[
            dict(no="01", title="Query, Key, Value", tag="Lookup", items=[
                "Each token sends a query; every token offers a key and a value",
                "Scores = query · key ÷ √dₖ; softmax turns them into weights that sum to 1",
                "Output = the weighted average of the values: a soft dictionary lookup",
            ], note="In real models Q, K and V come from learned matrices (Vaswani et al. 2017)."),
            dict(no="02", title="Older Than 2017", tag="History", items=[
                "Bahdanau et al. (2015): replace the fixed-length “bottleneck” with a soft search over the source",
                "Luong, Pham & Manning (2015): simpler dot-product scores",
                "Vaswani et al. (2017) dropped recurrence, kept attention",
            ], note="2017 made attention the engine; it did not invent it."),
            dict(no="03", title="Why Divide by √dₖ", tag="Scale", items=[
                "For random q, k with unit variance, q · k has variance dₖ: my run gives 505.5 at dₖ 512",
                "Large scores push softmax into “extremely small gradients” (Vaswani et al.)",
                "Top weight at dₖ 512: 0.95 raw, 0.32 scaled",
            ], note="One square root keeps every head trainable."),
            dict(no="04", title="Weights Are Clues", tag="Explain", items=[
                "Jain & Wallace (2019): weights often disagree with gradient importance; other weights give the same output",
                "Wiegreffe & Pinter (2019): it “depends on one’s definition of explanation”",
                "A heat map shows where mixing happened, not why",
            ], note="A bright cell is a clue, never a proof."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Cost grows with n²: 6 tokens make 36 scores, 1 000 tokens make 1 000 000 per head",
                "A causal mask lets token i see tokens 1…i only; decoders use it",
                "Several heads attend in parallel, each with its own Q, K, V",
            ], note="Next: the whole layer built around attention."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Put the mask on the bank sentences: does bank still move?",
                "Drop the √dₖ and print the weights at dₖ 512",
                "Learn W_{Q} and W_{K} by gradient descent on a toy copy task",
            ], note="Check: every row of weights sums to 1."),
        ],
        tryit=dict(versions="PYTHON 3.13.16",
                   check="Check: 6 × 6 = 36 · 6 × 7 ÷ 2 = 21 · 505.5 ÷ 512 = 0.99 ≈ 1 · 0.95 ÷ 0.32 = 3.0× sharper · "
                         "numpy 2.5.3 · gensim 4.4.0"),
        sources=[
            ("Bahdanau, Cho & Bengio (2015) *Neural Machine Translation by Jointly Learning to Align and Translate*, ICLR",
             "https://arxiv.org/abs/1409.0473"),
            ("Luong, Pham & Manning (2015) EMNLP, 1412–1421", "https://doi.org/10.18653/v1/D15-1166"),
            ("Vaswani et al. (2017) *Attention Is All You Need*, NeurIPS 30", "https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html"),
            ("Jain & Wallace (2019) *Attention is not Explanation*, NAACL, 3543–3556", "https://doi.org/10.18653/v1/N19-1357"),
            ("Wiegreffe & Pinter (2019) *Attention is not not Explanation*, EMNLP-IJCNLP, 11–20",
             "https://doi.org/10.18653/v1/D19-1002"),
            ("Pennington, Socher & Manning (2014) *GloVe*, EMNLP, 1532–1543", "https://doi.org/10.3115/v1/D14-1162"),
        ],
    ),
    35: dict(
        regions={"05": (1360, 1012, 2104, 2080), "R": (1360, 2090, 2104, 2272)},
        em="Transformer",
        names="Vaswani · He · Ba · Xiong · Geva",
        fig=dict(
            label="Fig. 1",
            title="One layer, four checks · random weights + tokens, seed 35 · same data as code 05",
            panels=[
                ("One layer", [
                    "from the bottom: x · 5 × 16 → LayerNorm → 4-head attention → + → LayerNorm → FFN 16 → 64 → 16 → + → out · 5 × 16",
                    "*skip*: a dashed line around each sublayer to its +",
                ]),
                ("Where weights live", [
                    "**one base encoder layer**: 0.33 · 0.67",
                    "attention 1 050 624 · FFN 2 099 712",
                    "**base model, my tally**: embed 18.9 M · 6 enc 18.9 M · 6 dec 25.2 M",
                    "**total 63.1 M · Table 3: 65 M**",
                    "*decoder layer: FFN 0.50 · vocabulary about 37 000*",
                    "*big: 214.2 M · Table 3: 213 M*",
                ]),
                ("Order blindness", [
                    "x: A B C D E · x[p]: D A E B C",
                    "*largest change after the shuffle*",
                    "**no mask, no positions**: gap 0.00 · *order-blind*",
                    "**+ sinusoidal positions**: gap 2.15 · *sees order*",
                    "**+ causal mask**: gap 1.33 · *sees order*",
                    "*two-way attention alone sees a set*",
                ]),
                ("Position waves", [
                    "position 0 to 31 down the side · 16 dimensions · pe(32, 16)",
                    "+1 · -1 · white 0",
                ]),
            ],
            notes_title="Chart notes",
            notes=[
                ("Layer", "Attention, then a two-layer FFN, each with LayerNorm and a skip; 5 × 16 in, 5 × 16 out, so layers stack."),
                ("Weights", "The FFN holds 0.67 of a base encoder layer, 0.50 of a decoder layer. My tally: 63.1 M; Table 3: 65 M."),
                ("Order", "With no mask and no positions, shuffled tokens give shuffled outputs (gap 0.00); positions give 2.15, "
                          "a causal mask 1.33."),
                ("Waves", "Sines and cosines of different wavelengths give each position its own pattern."),
            ],
        ),
        cards=[
            dict(no="01", title="Two Sublayers", tag="Layer", items=[
                "Multi-head attention mixes information across tokens",
                "A position-wise FFN (512 → 2 048 → 512) works on each token alone",
                "The base model stacks N = 6 such layers (Vaswani et al. 2017)",
            ], note="Same shape in and out: that is what lets layers stack."),
            dict(no="02", title="Skip and Normalise", tag="Stability", items=[
                "Residual: out = x + f(x), so a layer learns only a change (He et al. 2016)",
                "LayerNorm rescales each token to mean 0, spread 1, then a learned gain and offset (Ba et al. 2016)",
                "2017 normalised after the add; Pre-LN trains without warm-up (Xiong et al. 2020)",
            ], note="My code is Pre-LN; the original paper was Post-LN."),
            dict(no="03", title="Where Weights Live", tag="Count", items=[
                "Base encoder layer: attention 1 050 624, FFN 2 099 712, share 0.67; decoder layer 0.50",
                "Geva et al. (2021): FFN layers “constitute two-thirds” of the weights and act like key–value memories",
                "My total 63.1 M against 65 M in Table 3",
            ], note="The title names the novelty, not the bulk."),
            dict(no="04", title="Order Is Added", tag="Position", items=[
                "Two-way attention with no positions is order-blind: shuffle gap 0.00",
                "Sinusoidal codes break the symmetry (2.15); so does a causal mask (1.33)",
                "Causal models without position codes still learn position (Haviv et al. 2022)",
            ], note="2017: “no recurrence and no convolution”, so position is injected."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Causal mask: flip token 5 and rows 1–4 change by 0.00; two-way rows change by 1.79",
                "Encoder–decoder for translation, decoder-only for text generation: same layer, different mask",
                "Attention cost grows with n²; the FFN grows with n",
            ], note="Next phase: The Complexity Lens."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Stack 6 blocks with and without the skips; compare output norms",
                "Move LayerNorm after the add (Post-LN) and repeat",
                "Recount the big model (d_model 1 024 and d_ff 4 096)",
            ], note="Check: my tally gives 214.2 M; Table 3 lists 213 M."),
        ],
        tryit=dict(versions="PYTHON 3.13.16",
                   check="Check: 2 099 712 ÷ 3 152 384 = 0.666 · 6 × 7 356 416 + 18 944 000 = 63 082 496 · "
                         "numpy 2.5.3 · scipy 1.18.1"),
        sources=[
            ("Vaswani et al. (2017) *Attention Is All You Need*, NeurIPS 30", "https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html"),
            ("He, Zhang, Ren & Sun (2016) CVPR, 770–778", "https://doi.org/10.1109/CVPR.2016.90"),
            ("Ba, Kiros & Hinton (2016) arXiv 1607.06450", "https://arxiv.org/abs/1607.06450"),
            ("Xiong et al. (2020) ICML, PMLR 119, 10524–10533", "https://proceedings.mlr.press/v119/xiong20b.html"),
            ("Geva, Schuster, Berant & Levy (2021) *Transformer Feed-Forward Layers Are Key-Value Memories*, EMNLP, 5484–5495",
             "https://doi.org/10.18653/v1/2021.emnlp-main.446"),
            ("Haviv et al. (2022) Findings of EMNLP, 1382–1390", "https://doi.org/10.18653/v1/2022.findings-emnlp.99"),
        ],
    ),
}

SUMMARY = dict(
    issue="Vol. 2 · No. 1 · October 2026",
    ribbon=("Phase 11 · Summary · Sprints 33–35 of 90", "Every number rerun in code"),
    kicker="Phase summary · Transformers & Vector Spaces",
    em="Vector",
    dek="From a word as a point in space to the layer that modern language models stack: what the geometry can "
        "and cannot tell us about meaning.",
    figures=[
        (33, "Angles from “cat”", [
            "cat · dog 22.8° · kitten 50.3° · democracy 87.9°",
            "*one-hot: every pair 90°*",
            "*dense: angles mean company*",
        ]),
        (34, "Why ÷ `√dₖ`", [
            "raw softmax: dₖ 4 0.49 · dₖ 64 0.86 · dₖ 512 0.95",
            "÷ √dₖ: 0.30–0.32",
            "*mean top weight, 10 keys*",
        ]),
        (35, "Where weights live", [
            "attention 0.33 · FFN 0.67",
            "one base encoder layer · model tally **63.1 M** (Table 3: 65 M)",
        ]),
    ],
    abstract=(
        "This issue follows meaning from a single word to a working layer. Sprint 33 placed 400 000 words as "
        "directions in a space of 50 numbers and read similarity as an angle. Sprint 34 let each word take a weighted "
        "average of the words around it, and Sprint 35 wrapped that step in the layer that language models stack. At "
        "each step the code tested a popular claim, and several did not survive."
    ),
    highlights=[
        (33, "Cat sits **22.8°** from dog and **87.9°** from democracy; one-hot puts every pair at **90°**."),
        (33, "King − man + woman lands on king (**0.885**); queen (**0.852**) needs the inputs skipped."),
        (34, "Context moves “bank”: “loan” climbs from its **52**nd neighbour to its **12**th."),
        (34, "Without ÷ √dₖ the top softmax weight hits **0.95** at dₖ 512; with it, **0.32**."),
        (35, "The FFN holds **0.67** of an encoder layer; unmasked attention can’t see order."),
    ],
    methods=(
        "Three scripts, each run before rendering and re-derived by an independent implementation (gensim’s own API, "
        "scipy, explicit loops). Data: GloVe vectors (Wikipedia 2014 + Gigaword 5, 400 000 words) and seeded random "
        "weights. Python 3.13.16 · numpy 2.5.3 · scipy 1.18.1 · gensim 4.4.0."
    ),
    misreadings=[
        ("King − man + woman = queen.",
         "King comes first; queen wins only once the inputs are skipped.",
         "Mikolov et al. 2013 · Nissim et al. 2020"),
        ("Close vectors mean synonyms.",
         "Antonyms share contexts: cold is hot’s 2nd neighbour.",
         "Hill et al. 2015"),
        ("Attention was invented in 2017.",
         "Bahdanau et al. used it for translation in 2014; 2017 dropped recurrence.",
         "Bahdanau et al. 2015 · Vaswani et al. 2017"),
        ("Attention weights explain the model.",
         "Contested: other weights can give the same output.",
         "Jain & Wallace 2019 · Wiegreffe & Pinter 2019"),
        ("A transformer is mostly attention.",
         "The FFN holds two-thirds of an encoder layer’s weights.",
         "Geva et al. 2021"),
    ],
    boxes=[
        ("Now I Can", "Read cosine as an angle, compute attention by hand with ÷ √dₖ and a mask, and count a "
                      "transformer’s weights."),
        ("Mistakes Avoided", "Trusting an analogy without its skip rule, reading heat maps as reasons, forgetting that "
                             "unmasked attention ignores order."),
        ("Phase Project", "One notebook: GloVe angles, attention on two bank sentences, one pre-LN block with a shuffle "
                          "test and a weight tally."),
    ],
    references=[
        ("Harris (1954) Word 10(2–3)", "https://doi.org/10.1080/00437956.1954.11659520"),
        ("Firth (1957) Studies in Linguistic Analysis", "https://ci.nii.ac.jp/ncid/BA18741557?l=en"),
        ("Mikolov et al. (2013) NeurIPS 26", "https://proceedings.neurips.cc/paper/2013/hash/9aa42b31882ec039965f3c4923ce901b-Abstract.html"),
        ("Pennington et al. (2014) EMNLP", "https://doi.org/10.3115/v1/D14-1162"),
        ("Levy & Goldberg (2014) NeurIPS 27", "https://proceedings.neurips.cc/paper/2014/hash/b78666971ceae55a8e87efb7cbfd9ad4-Abstract.html"),
        ("Hill et al. (2015) CL 41(4)", "https://doi.org/10.1162/COLI_a_00237"),
        ("Nissim et al. (2020) CL 46(2)", "https://doi.org/10.1162/coli_a_00379"),
        ("Bahdanau et al. (2015) ICLR", "https://arxiv.org/abs/1409.0473"),
        ("Vaswani et al. (2017) NeurIPS 30", "https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html"),
        ("Jain & Wallace (2019) NAACL", "https://doi.org/10.18653/v1/N19-1357"),
        ("Wiegreffe & Pinter (2019) EMNLP-IJCNLP", "https://doi.org/10.18653/v1/D19-1002"),
        ("Xiong et al. (2020) ICML", "https://proceedings.mlr.press/v119/xiong20b.html"),
        ("Geva et al. (2021) EMNLP", "https://doi.org/10.18653/v1/2021.emnlp-main.446"),
    ],
    next_issue=("Vol. 2 · No. 2", "The Complexity Lens", "From meaning to emergence."),
)
