"""Text of the Phase 1 images, for the website's sprint and phase pages.

Transcribed line by line from the published images (phases/phase-01-engineering-foundations/).
Each sprint is a mind-map: unnumbered boxes around a centre circle that carries the title. The box
texts and the source lines are word for word; the boxes are given in reading order (row by row,
left to right). The commands of the box whose code is in code/ (Essential Commands, Try It Yourself)
are not repeated here: the pages show the sprint's file from code/.

Marks inside texts: **bold**, *italic*. Thousands are written with a space, as on the images.

Regions: where each part sits on the image, in pixels of the 2160 × 2700 PNG (x0, y0, x1, y1),
measured on the images. "head" is the centre circle with the title.
"""

PHASE = dict(
    n=1,
    accents={1: "#13305e", 2: "#13305e", 3: "#13305e"},
    regions={
        "head": (790, 1170, 1370, 1750),
    },
    summary_regions={
        "head": (70, 70, 1260, 720), "figure": (1430, 280, 2100, 790),
        "tile-0": (72, 822, 550, 1312), "tile-1": (584, 822, 1062, 1312), "tile-2": (1096, 822, 1574, 1312),
        "tile-3": (1608, 822, 2086, 1312), "tile-4": (72, 1350, 550, 1840),
        "block-0": (584, 1350, 1062, 1840), "block-1": (1096, 1350, 1574, 1840), "references": (1608, 1350, 2086, 1840),
        "block-2": (72, 1878, 550, 2336), "next": (584, 1878, 2086, 2336),
    },
)

SPRINTS = {
    1: dict(
        regions={
            "c-env": (56, 376, 702, 1056), "c-core": (758, 376, 1402, 1056), "try": (1458, 376, 2104, 1056),
            "c-mini": (56, 1120, 702, 1800), "c-practice": (1458, 1120, 2104, 1800), "R": (56, 1864, 2104, 2264),
        },
        em=None,
        names="",
        cards=[
            dict(no="", key="c-env", title="Dev Environment", items=[
                "Python 3.11 + venv",
                "VS Code",
                "Linux terminal",
                "tmux, ripgrep, fzf",
            ]),
            dict(no="", key="c-core", title="Core Concept", items=[
                "Snapshots, not diffs",
                "Objects: blob, tree, commit",
                "Commits form a DAG",
                "Hash = identity: SHA-1 by default, SHA-256 opt-in",
            ]),
            dict(no="", key="c-mini", title="Mini Project", items=[
                "Create a local repository",
                "Add .gitignore + README.md",
                "Make 5 meaningful commits",
                "Inspect one object by its hash",
            ]),
            dict(no="", key="c-practice", title="Good Practice", items=[
                "Small commits, one idea each",
                "Messages explain why, not only what",
                "Keep key decisions inside the repo",
                "A project log from day one",
            ]),
        ],
        try_after="c-core",
        tryit=dict(title="Essential Commands", no=""),
        sources=[
            ("Pro Git — Scott Chacon & Ben Straub (free online)", "https://git-scm.com/book/en/v2"),
            ("Atlassian — Version Control with Git", "https://www.coursera.org/learn/version-control-with-git"),
            ("Google — Introduction to Git and GitHub (Coursera)", "https://www.coursera.org/learn/introduction-git-github"),
        ],
    ),

    2: dict(
        regions={
            "head": (790, 1126, 1370, 1706),
            "c-basics": (56, 376, 702, 1026), "c-why": (758, 376, 1402, 1026), "try": (1458, 376, 2104, 1026),
            "c-ssh": (56, 1090, 702, 1740), "c-hygiene": (1458, 1090, 2104, 1740),
            "c-mini": (56, 1804, 702, 2264), "R": (758, 1804, 2104, 2264),
        },
        em=None,
        names="",
        cards=[
            dict(no="", key="c-basics", title="Hashing Basics", items=[
                "Same input, same hash",
                "One changed character, a new hash",
                "Fixed length: SHA-256 = 64 hex chars",
                "One-way: no path back to the input",
            ]),
            dict(no="", key="c-why", title="Why Git Hashes", items=[
                "Object ID = hash of content",
                "SHA-1: 40 hex (default)",
                "SHA-256: 64 hex (opt-in)",
                "A 2017 SHA-1 collision pushed Git toward SHA-256",
            ]),
            dict(no="", key="c-ssh", title="GitHub over SSH", items=[
                "1. ssh-keygen -t ed25519",
                "2. Load the key with ssh-add",
                "3. Add the .pub key to GitHub",
                "4. Test: ssh -T git@github.com",
                "5. remote add, then push -u",
            ]),
            dict(no="", key="c-hygiene", title="Key Hygiene", items=[
                "Never share the private key",
                "Only the .pub file goes to GitHub",
                "Protect keys with a passphrase",
                "One key per device",
            ]),
            dict(no="", key="c-mini", title="Mini Project", items=[
                "Change one letter, compare",
                "Connect a repo over SSH",
                "Push, then clone elsewhere",
                "Check both copies match",
            ]),
        ],
        try_after="c-why",
        tryit=dict(no=""),
        sources=[
            ("NIST FIPS 180-4 — Secure Hash Standard", "https://doi.org/10.6028/NIST.FIPS.180-4"),
            ("Pro Git, ch. 10 — Git Internals", "https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain"),
            ("Git docs — Hash Function Transition", "https://git-scm.com/docs/hash-function-transition"),
            ("GitHub Docs — Connecting to GitHub with SSH",
             "https://docs.github.com/en/authentication/connecting-to-github-with-ssh"),
        ],
    ),

    3: dict(
        regions={
            "head": (790, 1126, 1370, 1706),
            "c-layout": (56, 376, 702, 1026), "c-why": (758, 376, 1402, 1026), "try": (1458, 376, 2104, 1026),
            "c-gates": (56, 1090, 702, 1740), "c-discipline": (1458, 1090, 2104, 1740),
            "c-mini": (56, 1804, 702, 2264), "R": (758, 1804, 2104, 2264),
        },
        em=None,
        names="",
        cards=[
            # The tree as printed; the indent after "│" is written as the tree tool writes it
            # (two no-break spaces and a space), so it shows exactly as on the image.
            dict(no="", key="c-layout", title="Project Layout",
                 code="my-project/\n├── pyproject.toml\n├── README.md\n├── src/\n│   └── mypkg/\n└── tests/"),
            dict(no="", key="c-why", title="Why a src/ Layout", items=[
                "Tests run the installed package",
                "No stray imports from the project root",
                "Missing files fail early, not after release",
                "Install once: pip install -e .",
            ]),
            dict(no="", key="c-gates", title="Quality Gates", items=[
                "1. Format — ruff format",
                "2. Lint — ruff check",
                "3. Types — mypy",
                "4. Tests — pytest",
                "5. CI blocks the merge if one fails",
            ]),
            dict(no="", key="c-discipline", title="Gate Discipline", items=[
                "One pyproject.toml for all settings",
                "pre-commit runs checks on every commit",
                "Hooks can be skipped, so CI repeats them",
                "Fix the cause, don't mute the check",
            ]),
            dict(no="", key="c-mini", title="Mini Project", items=[
                "Restructure into src/ + tests/",
                "Watch a test fail, then pass",
                "Wire ruff into pre-commit",
                "Make CI a required check",
            ]),
        ],
        try_after="c-why",
        tryit=dict(no=""),
        sources=[
            ("Python Packaging User Guide — src layout vs flat layout",
             "https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/"),
            ("pytest docs — Good Integration Practices", "https://docs.pytest.org/en/stable/explanation/goodpractices.html"),
            ("pre-commit.com — official documentation", "https://pre-commit.com/"),
            ("GitHub Docs — About protected branches",
             "https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/"
             "managing-protected-branches/about-protected-branches"),
        ],
    ),
}

SUMMARY = dict(
    style="catalog",
    kicker="Phase 1 · Summary · Sprints 1–3 of 90",
    em="Foundations",
    dek="Version control, hashing, secure access and quality gates: three sprints, every claim checked against "
        "official sources.",
    badges=["3 sprints, hands-on", "Verified sources", "One phase project"],
    figure=dict(lines=[
        "a laptop screen: $ git log --oneline",
        "a1f9c3e add quality gates",
        "7be20d4 connect over SSH",
        "3c5a1f0 first snapshot",
        "$ pytest passed ✓",
        "a stack of four blocks: Git · Hashing · SSH · Gates",
    ]),
    tiles=[
        dict(colour="#4e86e8", sprint=1, title="Git Foundations", text="Snapshots, not diffs. Blob, tree and commit form a graph.",
             tag="Sprint 1"),
        dict(colour="#7a5edb", sprint=2, title="Hashing in Git", text="One changed character, a new hash. SHA-1 by default, SHA-256 opt-in.",
             tag="Sprint 2"),
        dict(colour="#2aa692", sprint=2, title="GitHub over SSH", text="An ed25519 key pair. Only the .pub file ever leaves the machine.",
             tag="Sprint 2"),
        dict(colour="#e88e3b", sprint=3, title="Project Structure", text="Code in src/, tests in tests/, settings in one pyproject.toml.",
             tag="Sprint 3"),
        dict(colour="#42aa61", sprint=3, title="Quality Gates", text="Format, lint, types, tests. CI repeats what hooks can skip.",
             tag="Sprint 3"),
    ],
    blocks=[
        dict(title="Now I Can", colour="#213f72", text="Build a versioned repo, push over SSH, stop bad code at the gate.", tag="Outcome"),
        dict(title="Mistakes Avoided", colour="#de576d", text="Vague commits, leaked keys, the SHA-256 myth, loose-file tests.",
             tag="Lessons"),
        dict(title="Phase Project", colour="#319fbf", text="One repo on GitHub over SSH, gates on, a fresh clone that passes."),
    ],
    references_title="Trusted Sources",
    references=[
        ("Pro Git", "https://git-scm.com/book/en/v2"),
        ("NIST FIPS 180-4", "https://doi.org/10.6028/NIST.FIPS.180-4"),
        ("GitHub Docs", "https://docs.github.com/en"),
        ("PyPA Guide", "https://packaging.python.org/en/latest/"),
        ("pytest documentation", "https://docs.pytest.org/en/stable/"),
    ],
    next_issue=("Next · Phase 2", "Knowledge, Truth & Evidence", "From tools to ideas."),
)
