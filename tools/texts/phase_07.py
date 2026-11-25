"""Text of the Phase 7 images, for the website's sprint and phase pages.

Transcribed line by line from the published images (phases/phase-07-data-skepticism-and-evaluation-data/).
Card texts, notes, check lines, the summary's tiles and boxes and the source lines are word for word;
the figure panels are read in words from their labels (fig.panels), with the printed captions in
italics. The code of each Try It box is not repeated here: the pages show the sprint's file from
code/, which ends with the printed output. tools/website.py turns this file into the pages.

Marks inside texts: **bold**, *italic*. Thousands are written with a space, as on the images
(65 536); the pages keep each group together with a no-break space.

Regions: where each part sits on the image, in pixels of the 2160 × 2700 PNG (x0, y0, x1, y1),
measured on the images. The page lights the part of the image whose text is being read.
"""

PHASE = dict(
    n=7,
    accents={19: "#cf5f1c", 20: "#cf5f1c", 21: "#cf5f1c"},
    regions={
        "head": (56, 320, 2104, 566), "fig": (56, 586, 2104, 950),
        "01": (56, 970, 700, 1392), "02": (720, 970, 1366, 1392),
        "03": (56, 1414, 700, 1836), "04": (720, 1414, 1366, 1836),
        "06": (56, 1858, 700, 2280), "07": (720, 1858, 1366, 2280),
        "05": (1392, 970, 2104, 1836), "R": (1392, 1858, 2104, 2280),
    },
    summary_regions={
        "head": (40, 40, 1340, 700), "figure": (1370, 270, 2140, 730),
        "tile-0": (78, 798, 550, 1250), "tile-1": (590, 798, 1060, 1250), "tile-2": (1100, 798, 1572, 1250),
        "tile-3": (1612, 798, 2082, 1250),
        "block-0": (78, 1286, 550, 1738), "block-1": (590, 1286, 1060, 1738), "block-2": (1100, 1286, 1572, 1738),
        "references": (1612, 1286, 2082, 1738),
        "block-3": (78, 1774, 550, 2214), "next": (590, 1774, 2082, 2214),
    },
)

SPRINTS = {
    19: dict(
        em="Transform",
        names="Kimball · Caserta · Moreau · Ziemann",
        fig=dict(
            label="Fig. 1",
            panels=[
                ("One batch of six rows, run twice · same data as code 05", [
                    "Run 2 · same raw file → table still 3 rows (a dashed line from the table back to the raw file)",
                    "① RAW.CSV · 6 rows · read-only",
                    "a gauge on the pipe: FI 6 · E · Extract",
                    "② T · Transform · type · date · key · checks every row",
                    "Quarantine · 2 rows · id 3 '1-Mar' · id 4 'n/a'",
                    "Merged · 1 row · id 2 appears twice",
                    "a gauge on the pipe: FI 3 · ③ L · Load",
                    "TABLE g · 3 rows · key: id",
                    "④ Reconcile · 6 = 3 + 1 + 2 · in = load + dup + rejected",
                ]),
            ],
            notes=[
                ("Extract", "The raw file stays read-only. Run 2 starts from the same six rows."),
                ("Transform", "'1-Mar' is the gene MARCH1 after a spreadsheet read it as a date. 'n/a' has no score. "
                              "Both set aside with a reason."),
                ("Load", "Replace on the key: 3 rows after run 1 and after run 2. A plain INSERT with no key gives 6."),
                ("Reconcile", "6 in = 3 loaded + 1 duplicate + 2 rejected."),
            ],
        ),
        cards=[
            dict(no="01", title="Copy, Don't Edit", tag="Extract", items=[
                "Pull each source as it is. Keep the raw copy read-only",
                "Stamp each batch with source, time and version (W3C PROV: entity, activity, agent)",
                "Read a fixed window, never \"the latest\" (Airflow)",
            ], note="If the raw file changes, a rerun is a different experiment."),
            dict(no="02", title="Types Are Claims", tag="Transform", items=[
                "Declare each column's type. Never let a tool guess it",
                "Spreadsheet guessing turns gene names into dates (SEPT2 → 2-Sep): errors in 19.6% of papers with "
                "Excel gene lists, 2005–2015",
                "Still 30.9% of such papers in 2014–2020",
            ], note="Ziemann et al. 2016 · Abeysooriya et al. 2021. The genes were renamed instead: SEPTIN1, MARCHF1."),
            dict(no="03", title="Safe to Run Twice", tag="Load", items=[
                "Idempotent: the same outcome on every re-run (Airflow)",
                "Replace or upsert on a key, or overwrite one partition",
                "Code 05 holds 3 rows after both runs. Plain INSERT with no key: 6",
            ], note="With a key, a plain INSERT fails loudly on run 2. Without one it doubles quietly."),
            dict(no="04", title="ETL or ELT", tag="Order", items=[
                "ETL: transform in a separate engine, often via staging tables, then load",
                "ELT: load raw, transform inside the target store",
                "Either way, check before anyone reads the table",
            ], note="Microsoft Azure docs. Kimball & Caserta (2004) estimate ETL at about 70% of a warehouse's resources."),
            dict(no="06", title="General Notes", tag="Skepticism", items=[
                "Count rows in and out of every stage",
                "Quarantine bad rows with a reason. Never drop them silently",
                "Keep spreadsheets out of the pipe: .xls saves 65 536 rows",
                "England, Oct 2020: 15 841 cases missed the daily count when a file hit its limit (PHE)",
            ]),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Take one CSV you use. Write E, T and L as three functions",
                "Log the count at each stage. Fail the run if they don't match",
                "Run it twice. Then use a plain INSERT without a key and watch 3 become 6",
                "Open the raw CSV in a spreadsheet, save it, diff it",
            ]),
        ],
        tryit=dict(check="Check: 6 = 3 + 1 + 2 (loaded, duplicate, rejected). Python 3.11.15 · sqlite3 3.45.1"),
        sources=[
            ("Kimball & Caserta (2004). *The Data Warehouse ETL Toolkit*. Wiley",
             "https://www.wiley-vch.de/en/areas-interest/computing-computer-sciences/the-data-warehouse-etl-toolkit-978-0-7645-6757-5"),
            ("Microsoft Learn: *Extract, transform, load (ETL)*",
             "https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl"),
            ("*Worksheet compatibility issues*", "https://support.microsoft.com/excel/worksheet-compatibility-issues"),
            ("Apache Airflow: *Best Practices*", "https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html"),
            ("SQLite: *ON CONFLICT*", "https://www.sqlite.org/lang_conflict.html"),
            ("Moreau & Missier, eds. (2013). *PROV-DM*. W3C", "https://www.w3.org/TR/prov-dm/"),
            ("Ziemann, Eren & El-Osta (2016). Genome Biol. 17, 177", "https://doi.org/10.1186/s13059-016-1044-7"),
            ("Abeysooriya et al. (2021). PLOS Comput. Biol. 17(7), e1008984",
             "https://doi.org/10.1371/journal.pcbi.1008984"),
            ("PHE (4 Oct 2020). Delayed reporting of COVID-19 cases",
             "https://www.gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases"),
        ],
    ),
    20: dict(
        regions={"05": (1392, 970, 2104, 1728), "R": (1392, 1750, 2104, 2280)},
        em="Evaluation",
        names="Cohen · Recht · Barz · Kapoor · Northcutt",
        fig=dict(
            label="Fig. 1",
            panels=[
                ("One pool, two ways to split it · same data as code 05", [
                    "① Pool · 1 000 · 200 groups × 5 copies · label: coin",
                    "② Split by row · random 20% → Train 813 · Test 187 → 1-NN 1.000",
                    "Copies leak · 100% seen (a dotted red link between train and test)",
                    "③ Split by group · 40 whole groups → Train 800 · Test 200 → 1-NN 0.440",
                    "Sealed · 0% seen (a striped barrier between train and test)",
                    "Looks perfect · it remembered copies",
                    "④ Gap 0.560",
                    "Honest: ≈ chance · guessing gives 0.5",
                ]),
            ],
            notes=[
                ("Pool", "1 000 rows: 200 groups of 5 near-copies. Each group's label is a coin flip, so there is "
                         "nothing to learn."),
                ("By row", "187 test rows, every one with a copy in training. A nearest-neighbour lookup scores 1.000."),
                ("By group", "40 whole groups held out (200 rows). None seen. Score 0.440, near the 0.5 of guessing."),
                ("Gap", "1.000 − 0.440 = 0.560. That gap is leakage, not learning."),
            ],
        ),
        cards=[
            dict(no="01", title="Seal the Test Set", tag="Split first", items=[
                "Split before any cleaning, scaling or feature choice. Never call fit on test data (scikit-learn)",
                "Version it, lock it, open it once at the end",
                "Every choice made by looking at it turns it into training data",
            ], note="Recht et al. (2019): new test sets cut accuracy 3–15% and 11–14%, from harder images, not from reuse."),
            dict(no="02", title="Split by Group", tag="Leakage", items=[
                "Copies, one patient, one source: all on one side (GroupKFold)",
                "Leakage found in 294 papers across 17 fields (Kapoor & Narayanan 2023)",
                "Duplicates are one of their leakage types. Time order is another",
            ], note="Code 05: the same model scores 1.000 or 0.440 depending only on the split."),
            dict(no="03", title="Hunt the Copies", tag="Dedup", items=[
                "CIFAR test sets: 3.3% (10 classes) and 10% (100 classes) of images had near-copies in training "
                "(Barz & Denzler 2020)",
                "Three QA datasets: 30% of test questions had a paraphrase in training. 60–70% of answers appeared "
                "there (Lewis et al. 2021)",
            ], note="Exact hashes miss near-copies. Compare normalised text or features too."),
            dict(no="04", title="Two Readers", tag="Agreement", items=[
                "Ten popular test sets: ≥ 3.3% wrong labels on average, ImageNet validation ≥ 6% (Northcutt et al. 2021)",
                "Cohen's κ (1960) removes the agreement chance alone gives",
                "80% raw, 50% by chance: κ = (0.80 − 0.50) ÷ (1 − 0.50) = 0.60",
            ], note="Two people label each item blind."),
            dict(no="06", title="General Notes", tag="Skepticism", items=[
                "Report the split rule, the seed and the counts",
                "Write a datasheet: who collected it, how, what is missing (Gebru et al. 2021)",
                "Keep a small hard slice and report it apart",
                "A test set used to pick the model is no longer a test set",
            ]),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Rerun Code 05 with seeds 1–5. By row I get 1.000 each time. By group: 0.395 to 0.575",
                "Take 200 items of your own and group them by source before splitting",
                "Ask a friend to label 50 items with you. Compute κ",
                "Write a one-page datasheet",
            ]),
        ],
        tryit=dict(check="Check: 40 groups × 5 = 200 test rows. 1 000 − 187 = 813 and 1 000 − 200 = 800 for training. "
                         "Gap 1.000 − 0.440 = 0.560. numpy 2.4.4"),
        sources=[
            ("Kapoor & Narayanan (2023). Patterns 4, 100804", "https://doi.org/10.1016/j.patter.2023.100804"),
            ("Barz & Denzler (2020). *Do We Train on Test Data?* J. Imaging 6(6), 41",
             "https://doi.org/10.3390/jimaging6060041"),
            ("Lewis, Stenetorp & Riedel (2021). EACL, 1000–1008", "https://doi.org/10.18653/v1/2021.eacl-main.86"),
            ("Recht et al. (2019). ICML, PMLR 97, 5389–5400", "https://proceedings.mlr.press/v97/recht19a.html"),
            ("Northcutt, Athalye & Mueller (2021). *Pervasive Label Errors in Test Sets Destabilize Machine Learning "
             "Benchmarks*. NeurIPS", "https://arxiv.org/abs/2103.14749"),
            ("Cohen (1960). Educ. Psychol. Meas. 20(1), 37–46", "https://doi.org/10.1177/001316446002000104"),
            ("scikit-learn docs: *Common pitfalls*", "https://scikit-learn.org/stable/common_pitfalls.html"),
            ("*Cross-validation*", "https://scikit-learn.org/stable/modules/cross_validation.html"),
            ("Gebru et al. (2021) CACM 64(12)", "https://doi.org/10.1145/3458723"),
        ],
    ),
    21: dict(
        em="Validation",
        names="Breck · Herndon · Wilkinson · NIST",
        fig=dict(
            label="Fig. 1",
            panels=[
                ("One batch, two tables, one sealed file · same data as code 05", [
                    "Batch · 0.91 · 'n/a' · 1.7",
                    "No checks → ① Loose · 2 real · 1 text",
                    "Type REAL → Check 0-1 → ② Strict · 1 real · 0.91 only",
                    "Rejected · 2 · type · range",
                    "Store: g.tmp · flush · fsync → os.replace · atomic ③ → g.csv · SHA-256 · 43fff085… (a check mark)",
                    "④ One edit: 0.91 → 0.19 · digest now 339535b6… · mismatch · refuse to read",
                ]),
            ],
            notes=[
                ("Loose", "Plain SQLite keeps all three. 'n/a' sits in a REAL column as text. 1.7 passes as a score."),
                ("Strict", "The type check refuses 'n/a'. A CHECK refuses 1.7. One row stored, two rejected with a reason."),
                ("Atomic", "Write g.tmp, flush, fsync, then os.replace. A reader gets the old file or the new one, never half."),
                ("Seal", "One swapped pair of digits gives a different SHA-256 digest."),
            ],
        ),
        cards=[
            dict(no="01", title="Rules You Can Run", tag="Schema", items=[
                "Write the schema: type, range, required, unique, per column",
                "Check every new batch against it before training",
                "Compare training data with what the model sees in use",
            ], note="Breck et al. (2019): Google's data validation checks several petabytes of production data per day."),
            dict(no="02", title="Let the Table Say No", tag="Types", items=[
                "SQLite: \"Any column can still store any type of data\"",
                "STRICT tables (3.37.0, 2021) raise an error on a wrong type",
                "A CHECK constraint guards the range",
            ], note="SQLite calls flexible typing \"a feature, not a bug\". Strictness is something I have to ask for."),
            dict(no="03", title="Write Once, Whole", tag="Storage", items=[
                "Temp file, flush, fsync, then os.replace: atomic on POSIX (Python docs)",
                "Never overwrite raw data. Keep dated, read-only snapshots",
                "FAIR: findable, accessible, interoperable, reusable",
            ], note="Wilkinson et al. (2016). os.replace may fail across two filesystems."),
            dict(no="04", title="Seal With a Hash", tag="Integrity", items=[
                "SHA-256 digests \"detect whether messages have been changed\" (FIPS 180-4)",
                "Store the digest beside the file. Recheck on every read",
                "Code 05: 0.91 → 0.19 turns 43fff085… into 339535b6…",
            ], note="A hash shows that a file changed. It cannot say which value is right."),
            dict(no="06", title="General Notes", tag="Skepticism", items=[
                "Validate on read as well as on write",
                "Log every rejection with its reason",
                "A CHECK in the table beats a note in the README",
                "Reinhart–Rogoff: a spreadsheet range left out five countries. With other fixes, growth above 90% debt "
                "was 2.2%, not −0.1% (Herndon et al. 2014)",
            ]),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Rebuild Sprint 19's table as STRICT with CHECKs",
                "Load its six rows again. Which fail, and why?",
                "Save the clean table atomically. Keep its SHA-256 in a .sha256 file",
                "Edit one digit and make your loader refuse the file",
            ]),
        ],
        tryit=dict(check="Check: loose 2 real + 1 text = 3 rows. Strict 3 − 2 rejected = 1 row. Digests match sha256sum. "
                         "Python 3.11.15 · sqlite3 3.45.1"),
        sources=[
            ("Breck, Polyzotis, Roy, Whang & Zinkevich (2019). *Data Validation for Machine Learning*. SysML",
             "https://proceedings.mlsys.org/paper_files/paper/2019/hash/928f1160e52192e3e0017fb63ab65391-Abstract.html"),
            ("SQLite docs: *Datatypes In SQLite*", "https://www.sqlite.org/datatype3.html"),
            ("*STRICT Tables*", "https://www.sqlite.org/stricttables.html"),
            ("Python docs: *os.replace*", "https://docs.python.org/3/library/os.html#os.replace"),
            ("NIST (2015). FIPS 180-4, *Secure Hash Standard*", "https://doi.org/10.6028/NIST.FIPS.180-4"),
            ("Herndon, Ash & Pollin (2014). Camb. J. Econ. 38(2), 257–279", "https://doi.org/10.1093/cje/bet075"),
            ("Wilkinson et al. (2016). *The FAIR Guiding Principles*. Sci. Data 3, 160018",
             "https://doi.org/10.1038/sdata.2016.18"),
        ],
    ),
}

SUMMARY = dict(
    style="catalog",
    kicker="Phase 7 · Summary · Sprints 19–21 of 90",
    em="Skepticism",
    dek="A pipeline that reconciles, a split that cannot leak, a table that says no: three sprints on trusting data, "
        "every number rerun in code.",
    badges=["3 sprints, 3 code runs", "Verified sources", "One phase project"],
    figure=dict(lines=[
        "a window with a small pipeline: a cylinder 6 → a box T (2 out) → a cylinder 3 with a check mark",
        "6 = 3 + 1 + 2",
        "labels: Reconcile · Split · Schema · Seal",
    ]),
    tiles=[
        dict(colour="#2b5c9e", sprint=19, title="Reconciled ETL",
             text="Six rows in: 3 loaded, 1 merged, 2 set aside. A rerun still leaves 3.", tag="Sprint 19"),
        dict(colour="#cf5f1c", sprint=19, title="Spreadsheet Traps",
             text="Gene names read as dates in 19.6% of papers with Excel gene lists.", tag="Sprint 19"),
        dict(colour="#5b4a8c", sprint=20, title="Leak-Free Split",
             text="One model: 1.000 when copies cross the split, 0.440 when groups stay apart.", tag="Sprint 20"),
        dict(colour="#13706e", sprint=21, title="Sealed Storage",
             text="STRICT and CHECK kept 1 of 3 rows. A SHA-256 seal caught one edit.", tag="Sprint 21"),
    ],
    blocks=[
        dict(title="Now I Can", colour="#5b4a8c", text="Reconcile an ETL run, split by group, measure κ, store data strict and sealed.",
             tag="Outcome"),
        dict(title="Mistakes Avoided",
             colour="#b8322a", text="Reruns that double, copies on both sides of a split, a column trusted for its type.", tag="Lessons"),
        dict(title="Habits Kept", colour="#3a7a3c", text="Count rows per stage. Lock the test set. Log rejections. Recheck digests.",
             tag="Practice"),
        dict(title="Phase Project",
             colour="#2b5c9e", text="One dataset I use: an ETL that reconciles, a group split with a datasheet, a STRICT table and a "
                  "SHA-256 seal."),
    ],
    references_title="Trusted Sources",
    references=[
        ("Kimball & Caserta 2004", "https://www.wiley-vch.de/en/areas-interest/computing-computer-sciences/the-data-warehouse-etl-toolkit-978-0-7645-6757-5"),
        ("Ziemann et al. 2016", "https://doi.org/10.1186/s13059-016-1044-7"),
        ("Cohen 1960", "https://doi.org/10.1177/001316446002000104"),
        ("Kapoor & Narayanan 2023", "https://doi.org/10.1016/j.patter.2023.100804"),
        ("Breck et al. 2019", "https://proceedings.mlsys.org/paper_files/paper/2019/hash/928f1160e52192e3e0017fb63ab65391-Abstract.html"),
    ],
    next_issue=("Next · Phase 8", "Tokenization & Parsing", "From data to text."),
)
