"""Text of the Phase 8 images, for the website's sprint and phase pages.

Transcribed line by line from the published images (phases/phase-08-tokenization-and-parsing/).
Card texts, notes, check lines, the summary's tiles and boxes and the source lines are word for word;
the figure panels are read in words from their labels (fig.panels). The code of each Try It box is
not repeated here: the pages show the sprint's file from code/, which ends with the printed output.
tools/website.py turns this file into the pages.

Marks inside texts: **bold**, *italic*. Words printed in a monospace font inside running text
(split(), decode()) are written plainly. Thousands are written with a space, as on the images
(50 257); the pages keep each group together with a no-break space. An Arabic word followed by
digits is wrapped in Unicode isolates (U+2068 … U+2069) so that browsers keep the printed order.

Regions: where each part sits on the image, in pixels of the 2160 × 2700 PNG (x0, y0, x1, y1),
measured on the images. The page lights the part of the image whose text is being read.
"""

PHASE = dict(
    n=8,
    accents={22: "#2c4aa0", 23: "#2c4aa0", 24: "#2c4aa0", 25: "#2c4aa0"},
    regions={
        "head": (56, 308, 2104, 578), "fig": (56, 592, 2104, 984),
        "01": (56, 1004, 700, 1408), "02": (724, 1004, 1368, 1408),
        "03": (56, 1428, 700, 1832), "04": (724, 1428, 1368, 1832),
        "06": (56, 1852, 700, 2256), "07": (724, 1852, 1368, 2256),
    },
    summary_regions={
        "head": (60, 60, 1300, 720), "figure": (1390, 270, 2090, 710),
        "tile-0": (80, 796, 552, 1252), "tile-1": (590, 796, 1062, 1252), "tile-2": (1100, 796, 1572, 1252),
        "tile-3": (1610, 796, 2082, 1252),
        "block-0": (80, 1284, 552, 1740), "block-1": (590, 1284, 1062, 1740), "block-2": (1100, 1284, 1572, 1740),
        "references": (1610, 1284, 2082, 1740), "block-3": (80, 1772, 552, 2216), "next": (590, 1772, 2082, 2216),
    },
)

SPRINTS = {
    22: dict(
        regions={"05": (1392, 1004, 2104, 1936), "R": (1392, 1956, 2104, 2260)},
        em="Tokenization",
        names="Sennrich · Schuster · Kudo · Radford · Petrov",
        fig=dict(
            title="One phrase, three cuts · toy vocabulary of 32 pieces · same data as code 05",
            panels=[
                ("Chars", [
                    "23 sorts",
                    "u n b e l i e v a b l y ␣ t o k e n i z e r s",
                ]),
                ("Words", [
                    "2 sorts",
                    "unbelievably, struck out: [UNK]",
                    "tokenizers, struck out: [UNK]",
                ]),
                ("Pieces", [
                    "7 sorts",
                    "un | believ | ably | token | ize | r | s",
                    "r in a dashed box",
                ]),
                ("IDs", [
                    "un 0 · believ 1 · ably 3 · token 4 · ize 5 · r 24 · s 6",
                ]),
            ],
            notes=[
                ("Chars", "23 sorts. Nothing is unknown, but every letter costs a step."),
                ("Words", "The list learned only “unbelievable” and “tokens”: both inputs fall to [UNK]."),
                ("Pieces", "Longest match first, as WordPiece reads a word. “r” falls back to one letter."),
                ("IDs", "The model gets 7 integers. Gluing the pieces back returns the text."),
            ],
        ),
        cards=[
            dict(no="01", title="Text to Numbers", tag="Encode", items=[
                "A tokenizer cuts text into pieces from a fixed vocabulary",
                "Each piece has one integer ID. The model sees only the IDs",
                "Decoding turns the IDs back into text",
            ], note="SentencePiece marks each space with ▁, so decoding returns the text (Kudo & Richardson 2018)."),
            dict(no="02", title="Three Ways to Cut", tag="Cuts", items=[
                "**Words:** a huge vocabulary. An unseen word becomes [UNK]",
                "**Characters:** nothing unknown, but one word can take 10 or more tokens",
                "**Subwords:** frequent words whole, rare ones in parts",
            ], note="Subwords for rare words: Sennrich et al. (2016). WordPiece: Schuster & Nakajima (2012)."),
            dict(no="03", title="Bytes Underneath", tag="UTF-8", items=[
                "UTF-8 uses 1 to 4 bytes per character. ASCII uses one",
                "é and س take 2 bytes. € takes 3",
                "GPT-2 starts from 256 bytes, not 130 000+ symbols, and ends with 50 257 tokens",
            ], note="With bytes as the floor, any string can be encoded (RFC 3629; Radford et al. 2019)."),
            dict(no="04", title="Same Text, Other Cost", tag="Cost", items=[
                "Translated, one text can need up to 15 times more tokens",
                "At byte or character level: still over 4 times for some pairs",
                "More tokens: higher price, slower replies, less context",
            ], note="Petrov et al. (2023). In UTF-8 “salam” is 5 bytes and سلام is 8."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Budget a model’s context in tokens, not words",
                "Change the vocabulary and the IDs change: the tokenizer is part of the model",
                "Test decode(encode(x)) == x on accents and Arabic",
            ], note="My toy split() knows only a–z: Arabic input loops forever. Byte-level tokenizers fall back to bytes."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Add “izer”: token|izer|s, IDs shift to [0, 1, 3, 4, 6, 7]",
                "Give split() a byte fallback, then run an Arabic sentence",
                "Write decode() and check the round trip on 20 sentences",
            ], note="Count chars, bytes and pieces for one sentence in Arabic and in English."),
        ],
        tryit=dict(versions="PYTHON 3.11.15",
                   check="Check: 12 + 1 + 10 = 23 · 23 ÷ 7 ≈ 3.3 chars a piece · ⁨سلام⁩ 4 × 2 = 8 bytes"),
        sources=[
            ("Sennrich et al. (2016). *Neural Machine Translation of Rare Words…* ACL",
             "https://doi.org/10.18653/v1/P16-1162"),
            ("Schuster & Nakajima (2012). *Japanese and Korean Voice Search.* ICASSP",
             "https://doi.org/10.1109/ICASSP.2012.6289079"),
            ("Song et al. (2021). *Fast WordPiece Tokenization.* EMNLP, 2089–2103",
             "https://doi.org/10.18653/v1/2021.emnlp-main.160"),
            ("Kudo & Richardson (2018). *SentencePiece.* EMNLP Demos, 66–71", "https://doi.org/10.18653/v1/D18-2012"),
            ("Radford et al. (2019). *Language Models are Unsupervised…* OpenAI",
             "https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf"),
            ("Yergeau (2003). *RFC 3629: UTF-8, a transformation format…* IETF", "https://doi.org/10.17487/RFC3629"),
            ("Petrov et al. (2023). *Language Model Tokenizers Introduce…* NeurIPS", "https://doi.org/10.52202/075280-1608"),
            ("Hugging Face LLM Course, ch. 2: *Tokenizers*", "https://huggingface.co/learn/llm-course/chapter2/4"),
        ],
    ),

    23: dict(
        regions={"05": (1392, 1004, 2104, 1976), "R": (1392, 1996, 2104, 2260)},
        em="Edge",
        names="Gage · Sennrich · Provilkov · Land · Singh",
        fig=dict(
            title="Ten merges on a toy corpus · Sennrich's example words · same data as code 05",
            panels=[
                ("Merge ladder · most frequent pair wins", [
                    "01 e + s → es · 9 · tie ×3",
                    "02 es + t → est · 9 · tie ×2",
                    "03 est + _ → est_ · 9",
                    "04 l + o → lo · 7 · tie ×2",
                    "05 lo + w → low · 7",
                    "06 n + e → ne · 6 · tie ×3",
                    "07 ne + w → new · 6 · tie ×2",
                    "08 new + est_ → newest_ · 6",
                    "09 low + _ → low_ · 5",
                    "10 w + i → wi · 3 · tie ×3",
                ]),
                ("16 words · 95 → 28 symbols", [
                    "×5 low_",
                    "×2 low | e | r | _",
                    "×6 newest_",
                    "×3 wi | d | est_",
                ]),
                ("Unseen words · same 10 merges", [
                    "lowest → low | est_",
                    "newer → new | e | r | _",
                    "Lowest → L | o | w | est_",
                    "L in a dashed red box",
                ]),
            ],
            notes=[
                ("Merge", "Count every neighbouring pair, weighted by word count. Fuse the most frequent. Repeat 10 times."),
                ("Ties", "6 of 10 steps were ties. My code keeps the first pair it met."),
                ("Shrink", "95 symbols become 28. Vocabulary: 11 base symbols + 10 merges = 21."),
                ("Unseen", "lowest reuses low and est_. newer never earned “er”. Capital L was never seen."),
            ],
        ),
        cards=[
            dict(no="01", title="The Merge Loop", tag="Algorithm", items=[
                "Gage (1994) compressed files by swapping the most frequent byte pair for an unused byte",
                "Sennrich et al. (2016) merge letters instead, plus an end-of-word mark",
                "Vocabulary = base symbols + merges, the only setting",
            ], note="Pairs never cross word boundaries. New words replay the merges in the order they were learned."),
            dict(no="02", title="Ties Decide", tag="Order", items=[
                "Steps 1, 2, 4, 6, 7 and 10 had tied pairs",
                "Break ties alphabetically: the corpus still ends at 28, but newer becomes ne|w|e|r|_",
                "Different merge list, different pieces, different IDs",
            ], note="The tie rule is part of the tokenizer. Write it down."),
            dict(no="03", title="Rare, Cased, Unseen", tag="Edges", items=[
                "newer stays in 4 pieces: “er” never won a merge",
                "Lowest: L was never seen, so low cannot form",
                "Under-trained tokens sit in the vocabulary but were barely seen in training",
            ], note="Land & Bartolo (2024): SolidGoldMagikarp-like tokens, found across many models."),
            dict(no="04", title="Numbers Split Oddly", tag="Digits", items=[
                "GPT-3.5 and GPT-4 cut numbers into chunks of up to 3 digits, from the left",
                "Commas force groups from the right: GPT-3.5 addition went from 68.5% to 95.6%",
                "LLaMA and PaLM split numbers into single digits",
            ], note="Singh & Strouse (2024), a preprint: the cut alone moved accuracy, one-shot."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Print the merge list and read it",
                "Test capitals, leading spaces, digits, emoji and Arabic",
                "BPE gives one fixed split. Dropping merges at random in training gave up to 2.3 BLEU (Provilkov et al. 2020)",
            ], note="Unigram LM tokenization matched or beat BPE in pretraining (Bostrom & Durrett 2020)."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Run 14 merges: lower appears, newer stays new|e|r|_",
                "Break ties alphabetically: Lowest becomes L|ow|est_",
                "Skip each merge with p = 0.1, seeds 1 to 5, and compare splits",
            ], note="Train on one page of my own text and read its first 30 merges."),
        ],
        tryit=dict(versions="PYTHON 3.11.15",
                   check="Check: 5×4 + 2×6 + 6×7 + 3×7 = 95 · 5 + 2×4 + 6 + 3×3 = 28 · 11 + 10 = 21"),
        sources=[
            ("Gage (1994). *A New Algorithm for Data Compression.* C Users J. 12(2)",
             "https://drdobbs.com/a-new-algorithm-for-data-compression/184402829"),
            ("Sennrich et al. (2016). *Neural Machine Translation of Rare…* ACL", "https://doi.org/10.18653/v1/P16-1162"),
            ("Provilkov et al. (2020). *BPE-Dropout.* ACL, 1882–1892", "https://doi.org/10.18653/v1/2020.acl-main.170"),
            ("Bostrom & Durrett (2020). *Byte Pair Encoding is Suboptimal…* EMNLP",
             "https://doi.org/10.18653/v1/2020.findings-emnlp.414"),
            ("Land & Bartolo (2024). *Fishing for Magikarp.* EMNLP, 11631–11646",
             "https://doi.org/10.18653/v1/2024.emnlp-main.649"),
            ("Singh & Strouse (2024). *Tokenization counts…* arXiv 2402.14903", "https://arxiv.org/abs/2402.14903"),
        ],
    ),

    24: dict(
        regions={"05": (1392, 1004, 2104, 2024), "R": (1392, 2044, 2104, 2260)},
        em="Meaning",
        names="Church · Patil · Jurafsky · de Marneffe · Bray",
        fig=dict(
            title="Two trees · ambiguity grows · a duplicate key · same data as code 05",
            panels=[
                ("Same 5 tokens · two trees", [
                    "2 + 3 * 4",
                    "+ at the root, over 2 and a * node over 3 and 4: = 14 · grammar's tree",
                    "* at the root, over a + node (2, 3) and 4: = 20 · needs ( )",
                ]),
                ("Trees per `n` operators", [
                    "n = 1 to 8: 1 · 2 · 5 · 14 · 42 · 132 · 429 · 1 430",
                    "log scale",
                    "legend: the bar at 2 is 2 + 3 * 4 · the bar at 3 is 3 PPs",
                ]),
                ("One record · two readers", [
                    "{\"dose\": 5, \"dose\": 50}",
                    "json.loads: {'dose': 50} · no warning",
                    "strict hook: rejected: duplicate key",
                    "RFC 8259: names SHOULD be unique. Readers differ.",
                ]),
            ],
            notes=[
                ("Grammar", "“*” sits deeper in the grammar, so it binds first: 2 + (3 × 4) = 14."),
                ("Other tree", "The same tokens read as (2 + 3) × 4 give 20. Only brackets select it."),
                ("Growth", "1, 2, 5, 14, 42… the Catalan numbers. Three prepositional phrases already give 5 readings."),
                ("Duplicates", "Python keeps the last “dose” and says nothing. A strict hook refuses the record."),
            ],
        ),
        cards=[
            dict(no="01", title="From String to Tree", tag="Grammar", items=[
                "A grammar lists the allowed forms and how parts group",
                "Parsing turns a string into a tree: leaves keep the order, the shape holds the meaning",
                "Constituency trees group phrases. Dependency trees link words to heads",
            ], note="Universal Dependencies: one scheme, 200+ treebanks in 150+ languages (de Marneffe et al. 2021)."),
            dict(no="02", title="Ambiguity Multiplies", tag="Trees", items=[
                "“I shot an elephant in my pajamas”: the phrase can attach to elephant or to shot",
                "Each added prepositional phrase multiplies the readings: 2, 5, 14, 42…",
                "A parser must choose, by rules or by probabilities",
            ], note="Church & Patil (1982) found 4 862 trees for nine such phrases. Example: Jurafsky & Martin."),
            dict(no="03", title="Precedence Matters", tag="Rules", items=[
                "“*” sits one level deeper, so 2 + 3 * 4 = 14",
                "The same tokens as (2 + 3) * 4 give 20",
                "The loop groups from the left: 1 + 2 + 3 parses as (1 + 2) + 3",
            ], note="Precedence and grouping belong in the grammar, not in the reader’s head."),
            dict(no="04", title="Parse Strictly", tag="Schema", items=[
                "JSON object names SHOULD be unique, and readers differ on duplicates (RFC 8259)",
                "Python keeps the last one: “dose” 5 then 50 gives 50, with no warning",
                "Python also reads NaN and Infinity, which JSON does not allow",
            ], note="object_pairs_hook sees every pair and can refuse the record (Python docs)."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Parse once at the boundary, then pass typed records along",
                "Reject what does not fit. Log the raw text with the reason",
                "Keep the raw input beside the parsed record",
            ], note="Test with ambiguous, malformed and duplicated inputs, not only clean ones."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Add “-” beside “+”: 8 - 3 - 2 must give 3, not 7",
                "Feed “2 + * 3” and make the error name the bad token",
                "Pass parse_constant to json.loads to refuse NaN",
            ], note="Parse 10 recipe lines like “2 eggs” into JSON records and validate every key."),
        ],
        tryit=dict(versions="PYTHON 3.11.15",
                   check="Check: 3 × 4 = 12, 2 + 12 = 14 · 2 + 3 = 5, 5 × 4 = 20 · 5 + 2 + 2 + 5 = 14"),
        sources=[
            ("Church & Patil (1982). *Coping with Syntactic Ambiguity…* AJCL 8(3–4)", "https://aclanthology.org/J82-3004/"),
            ("Jurafsky & Martin. *Speech and Language Processing,* 3rd ed. draft, ch. 17",
             "https://web.stanford.edu/~jurafsky/slp3/"),
            ("de Marneffe et al. (2021). *Universal Dependencies.* CL 47(2), 255–308",
             "https://doi.org/10.1162/coli_a_00402"),
            ("Bray, ed. (2017). *RFC 8259: The JavaScript Object Notation…* IETF", "https://doi.org/10.17487/RFC8259"),
            ("Python docs: *json* · repeated names, NaN, object_pairs_hook", "https://docs.python.org/3/library/json.html"),
        ],
    ),

    25: dict(
        regions={"05": (1392, 1004, 2104, 2004), "R": (1392, 2024, 2104, 2260)},
        em="Package",
        names="PEP 621 · PEP 440 · PEP 427 · SemVer · PyPI",
        fig=dict(
            title="One toy package, built twice · how versions sort · same data as code 05",
            panels=[
                ("Build · check · publish", [
                    "pyproject.toml · src/toytok/__init__.py",
                    "build → toytok-0.1.0-py3-none-any.whl 917 B · toytok-0.1.0.tar.gz 336 B",
                    "twine check → TestPyPI → PyPI · a filename is never reused",
                ]),
                ("Build twice · SHA-256 of the wheel", [
                    "run 1 06334646fb0ae368 · run 2 06334646fb0ae368 = identical",
                ]),
                ("PEP 440 order", [
                    "1.0a2 < 1.0rc1 < 1.0 < 1.0.post1",
                    "as text: \"1.10\" > \"1.9\" False",
                    "as version: V(\"1.10\") > V(\"1.9\") True",
                ]),
                ("Wheel tag", [
                    "py3: Python 3 · none: no ABI · any: any OS",
                ]),
            ],
            notes=[
                ("Build", "One command, two files: a wheel to install and an sdist as the source fallback."),
                ("Repeat", "Built twice, same SHA-256: hatchling fixes the file times, so the wheel is reproducible."),
                ("Publish", "TestPyPI first. On PyPI a filename is never reused, even after a project is deleted."),
                ("Order", "As text “1.10” sorts before “1.9”. PEP 440 puts a2 and rc1 before 1.0, post1 after."),
            ],
        ),
        cards=[
            dict(no="01", title="The pyproject File", tag="Config", items=[
                "[build-system] names the tool that builds the package",
                "[project] holds name, version and Python range (PEP 621)",
                "src/ layout: tests import the installed package, not the folder (Sprint 3)",
            ], note="Python Packaging User Guide: “Packaging Python Projects”, step by step."),
            dict(no="02", title="Wheel and Sdist", tag="Build", items=[
                "python -m build writes both into dist/",
                "py3-none-any: Python 3, no ABI requirement, any platform",
                "RECORD lists every file in the wheel with its secure hash",
            ], note="Wheel format: PEP 427, now a PyPA specification. My wheel holds 4 files."),
            dict(no="03", title="Version Numbers", tag="SemVer", items=[
                "MAJOR breaks the API, MINOR adds, PATCH fixes",
                "0.y.z is for early work: anything may change",
                "pip orders versions by PEP 440, never as plain text",
            ], note="SemVer 2.0.0: once released, “the contents of that version MUST NOT be modified”."),
            dict(no="04", title="Release Is Permanent", tag="PyPI", items=[
                "PyPI never reuses a filename, so a file cannot be swapped quietly",
                "A bad release is yanked, not replaced: installers skip it unless pinned with ==",
                "Trusted Publishing lets CI upload without API tokens",
            ], note="PyPI help pages: filename reuse, yanking, Trusted Publishers."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Install from TestPyPI in a fresh venv before the real index",
                "twine check tests whether the README will render on PyPI",
                "Tag the commit with the version I uploaded",
            ], note="Packaging Sprint 22’s split() made me fix its loop: now it raises ValueError."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Package Sprint 22’s split() with one test",
                "Build twice and compare the SHA-256",
                "Upload to TestPyPI under a unique name, install it in a fresh venv",
            ], note="Fix a bug as 0.1.1. Never try to upload 0.1.0 again."),
        ],
        tryit=dict(versions="PYTHON 3.11.15",
                   check="Check: run 1 = run 2 · hatchling 1.32.4 · build 1.6.1 · packaging 26.1"),
        sources=[
            ("PyPA. *Python Packaging User Guide: Packaging Python Projects*",
             "https://packaging.python.org/en/latest/tutorials/packaging-projects/"),
            ("PEP 621 (2020). *Storing project metadata in pyproject.toml*", "https://peps.python.org/pep-0621/"),
            ("PEP 440 (2013). *Version Identification and Dependency Specification*", "https://peps.python.org/pep-0440/"),
            ("PEP 427 (2013) / PyPA spec. *Binary distribution format*",
             "https://packaging.python.org/en/latest/specifications/binary-distribution-format/"),
            ("Preston-Werner. *Semantic Versioning 2.0.0*, semver.org", "https://semver.org/spec/v2.0.0.html"),
            ("PyPI Help (reuse, yanking, Trusted Publishers) · Hatch · twine docs", "https://docs.pypi.org/"),
        ],
    ),
}

SUMMARY = dict(
    style="catalog",
    kicker="Phase 8 · Summary · Sprints 22–25 of 90",
    em="Tokenization",
    dek="Pieces, merges, trees and a release: four sprints on turning text into structure, every number rerun in code.",
    badges=["4 sprints, 4 code runs", "Verified sources", "One phase project"],
    figure=dict(label="Figure", lines=[
        "A dark code window",
        "three word pieces: un · believ · ably",
        "e + s → es",
        "toytok 0.1.0 · wheel",
        "run 1 = run 2 ✓",
        "a tree: + over 2 and a * node over 3 and 4",
        "four tags beside it: Pieces · Merges · Trees · Release",
    ]),
    tiles=[
        dict(colour="#2c4aa0", sprint=22, title="Subword Pieces", tag="Sprint 22",
             text="23 chars, two [UNK] words, or 7 pieces that glue back into the text."),
        dict(colour="#a97e12", sprint=23, title="Merge Ties", tag="Sprint 23",
             text="Ten merges: 95 symbols to 28. Six were ties, and ties change splits."),
        dict(colour="#7b3f74", sprint=24, title="Parse Trees", tag="Sprint 24",
             text="2 + 3 * 4: 14 by the grammar, 20 by the other tree. Readings grow 2, 5, 14…"),
        dict(colour="#b5652a", sprint=25, title="Sealed Release", tag="Sprint 25",
             text="Built twice, same SHA-256. PyPI never reuses a filename."),
    ],
    blocks=[
        dict(title="Now I Can", tag="Outcome", colour="#4b3f8f",
             text="Tokenize, train BPE merges, parse with precedence, ship a wheel."),
        dict(title="Mistakes Avoided", tag="Lessons", colour="#c23b2e",
             text="Words counted as tokens, hidden tie rules, silent duplicate keys."),
        dict(title="Habits Kept", tag="Practice", colour="#4f7a5a",
             text="Round-trip encodings. Print the merges. Reject with a reason."),
        dict(title="Phase Project", colour="#2c4aa0",
             text="One small library: a tokenizer with BPE merges and a strict parser, tested and released on TestPyPI."),
    ],
    references_title="Trusted Sources",
    references=[
        ("Sennrich et al. 2016", "https://doi.org/10.18653/v1/P16-1162"),
        ("Kudo & Richardson 2018", "https://doi.org/10.18653/v1/D18-2012"),
        ("Petrov et al. 2023", "https://doi.org/10.52202/075280-1608"),
        ("Church & Patil 1982", "https://aclanthology.org/J82-3004/"),
        ("PEP 440", "https://peps.python.org/pep-0440/"),
    ],
    next_issue=("Next · Phase 9", "Classical Machine Learning", "From text to models."),
)
