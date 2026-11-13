"""Builds the pages of this repository from tools/series_data.py.

Usage, from the repository root:
  python3 tools/build.py [--images DIR ...]   copy new images in, then rebuild every page
  python3 tools/build.py --check              check links, anchors, checksums and citation
  python3 tools/build.py --images DIR --pack update.zip
                                              rebuild, then zip only the files that changed

It never deletes or overwrites a published image. Requires Pillow; the "next phase" tile also needs
Playwright with Chromium and fetches its two fonts from the Google Fonts repository on first use.
"""
import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import zipfile
from datetime import date

from PIL import Image

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
sys.dont_write_bytecode = True
sys.path.insert(0, TOOLS)
from series_data import MILESTONES, NEXT, PHASES  # noqa: E402

REPO_URL = "https://github.com/MT24Learning/knowledge-sprint-series"
SITE_URL = "https://mt24learning.github.io/knowledge-sprint-series/"
ZENODO = "https://zenodo.org/communities/mt24-learning"
ORCID = "0009-0000-9113-1687"
TOTAL_PHASES, TOTAL_SPRINTS = 27, 90
SOCIAL = [
    ("LinkedIn", "https://www.linkedin.com/in/mohammed-tahri24"),
    ("X", "https://x.com/MohammedTahri24"),
    ("Bluesky", "https://bsky.app/profile/mohammedtahri.bsky.social"),
    ("Mastodon", "https://mathstodon.xyz/@mohammedtahri24"),
    ("Threads", "https://www.threads.net/@mohammedtahri24"),
    ("Instagram", "https://www.instagram.com/mohammedtahri24"),
    ("Facebook", "https://www.facebook.com/mohammed.tahri24"),
    ("TikTok", "https://www.tiktok.com/@mohammed.tahri24"),
    ("Substack", "https://substack.com/@mohammedtahri24"),
]
FONTS = {
    "SpaceGrotesk.ttf": "ofl/spacegrotesk/SpaceGrotesk%5Bwght%5D.ttf",
    "JetBrainsMono.ttf": "ofl/jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf",
}


# ---------------------------------------------------------------- helpers

def slug(text):
    keep = "".join(ch.lower() if ch.isalnum() else "-" for ch in text.replace("&", "and"))
    while "--" in keep:
        keep = keep.replace("--", "-")
    return keep.strip("-")


def gh_anchor(heading):
    """GitHub heading anchor (github-slugger): lowercase, drop punctuation, spaces to hyphens."""
    out = []
    for ch in heading.strip().lower():
        if ch.isalnum() or ch in "-_":
            out.append(ch)
        elif ch == " ":
            out.append("-")
    return "".join(out)


def phase_dir(p):
    return f"phase-{p['n']:02d}-{slug(p['title'])}"


def nice_date(iso):
    d = date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B %Y')}"


def sprint_range(p):
    a, b = p["sprints"][0]["n"], p["sprints"][-1]["n"]
    return f"{a}" if a == b else f"{a}–{b}"


def sprint_label(p):
    return f"Sprint {sprint_range(p)}" if len(p["sprints"]) == 1 else f"Sprints {sprint_range(p)}"


def doi_link(doi):
    return f"[{doi}](https://doi.org/{doi})"


def citation(p):
    year = p["first"][:4]
    return (f"Tahri, M. ({year}). MT24 Learning — Knowledge Sprint Series, Phase {p['n']}: {p['title']} "
            f"(Version 1.0) [Educational resource]. Zenodo. https://doi.org/{p['v']}")


def phase_by_n(n):
    return next(p for p in PHASES if p["n"] == n)


def sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text.rstrip("\n") + "\n")


def jpeg_comment(path):
    try:
        return Image.open(path).info.get("comment", b"").decode()
    except (OSError, AttributeError):
        return ""


def thumb(src, rel, size=(520, 650), note=None):
    """Writes a JPEG thumbnail; skipped when the existing one was made from the same source."""
    dst = os.path.join(ROOT, rel)
    note = note or f"source-sha256:{sha256(src)}"
    if os.path.exists(dst) and jpeg_comment(dst) == note:
        return False
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    im = Image.open(src).convert("RGB")
    im.thumbnail(size, Image.LANCZOS)
    im.save(dst, "JPEG", quality=84, optimize=True, progressive=True, comment=note.encode())
    return True


def code_files(p, s=None):
    """Files in a phase's code/ folder (paths from the repository root),
    or the file names that belong to one sprint (sprintNN_*)."""
    d = os.path.join(ROOT, "phases", phase_dir(p), "code")
    names = sorted(f for f in os.listdir(d) if not f.startswith(".")) if os.path.isdir(d) else []
    if s is None:
        return [f"phases/{phase_dir(p)}/code/{f}" for f in names]
    return [f for f in names if f.startswith(f"sprint{s['n']:02d}_")]


def checked_paths():
    """Every file listed in CHECKSUMS.sha256: the images, then the code."""
    return image_paths() + [f for p in PHASES for f in code_files(p)]


def image_paths():
    """Every published image, as a path from the repository root."""
    paths = []
    for p in PHASES:
        for f in [p["summary"]] + [s["file"] for s in p["sprints"]]:
            paths.append(f"phases/{phase_dir(p)}/{f}")
    for m in MILESTONES:
        paths.append(f"milestones/{m['file']}")
    return paths


# ---------------------------------------------------------------- pages

def phase_page(i, p):
    prev_p = PHASES[i - 1] if i > 0 else None
    next_p = PHASES[i + 1] if i + 1 < len(PHASES) else None
    nav = ["[All phases](../../README.md)"]
    if prev_p:
        nav.insert(0, f"[← Phase {prev_p['n']}](../{phase_dir(prev_p)}/README.md)")
    if next_p:
        nav.append(f"[Phase {next_p['n']} →](../{phase_dir(next_p)}/README.md)")
    nav_line = " · ".join(nav)
    count = len(p["sprints"])
    word = "sprint" if count == 1 else "sprints"

    out = [
        f"<sub>{nav_line}</sub>",
        "",
        f"# Phase {p['n']} · {p['title']}",
        "",
        f"**{sprint_label(p)} of {TOTAL_SPRINTS}** · first published {nice_date(p['first'])} · "
        f"archived on Zenodo, DOI {doi_link(p['v'])}",
        "",
        f"> {p['line']}",
        "",
        "## Phase summary",
        "",
        f"<a href=\"{p['summary']}\"><img src=\"{p['summary']}\" width=\"760\" "
        f"alt=\"Phase {p['n']} summary page: {p['title']}, {count} {word}, with what each sprint covers, "
        f"what I can now do, mistakes avoided and the phase project.\"></a>",
        "",
        f"**One result checked in this phase:** {p['result']}",
        "",
        "## Sprints",
        "",
    ]
    for s in p["sprints"]:
        out += [f"### Sprint {s['n']}/{TOTAL_SPRINTS} · {s['title']}", ""]
        if s.get("tagline"):
            out += [f"> *{s['tagline']}*", ""]
        alt = f"Sprint {s['n']} of {TOTAL_SPRINTS} infographic: {s['title']}."
        if s.get("tagline"):
            alt += f" {s['tagline']}"
        out += [
            f"<a href=\"{s['file']}\"><img src=\"{s['file']}\" width=\"760\" alt=\"{alt}\"></a>",
            "",
            f"**Covers.** {s['covers']}",
            "",
            f"**Try it.** {s['tryit']}",
            "",
        ]
        run = code_files(p, s)
        if run:
            out += ["**Run it.** " + " · ".join(f"[`{f}`](code/{f})" for f in run)
                    + " · [versions, data and steps](code/README.md)", ""]
    out += [
        "## Cite this phase",
        "",
        "```text",
        citation(p),
        "```",
        "",
        f"This DOI points to version 1.0, the edition archived as first published. "
        f"To cite every version of this phase, use the concept DOI {doi_link(p['c'])}.",
        "",
        "---",
        "",
        f"<sub>{nav_line}</sub>",
    ]
    return "\n".join(out)


def milestone_heading(m):
    return f"Milestone · {m['title']}"


def milestone_link(m):
    if len(MILESTONES) == 1:
        return "milestones/README.md"
    return f"milestones/README.md#{gh_anchor(milestone_heading(m))}"


def milestone_page():
    out = ["<sub>[All phases](../README.md)</sub>", ""]
    single = len(MILESTONES) == 1
    if not single:
        out += ["# Milestones", ""]
    for m in MILESTONES:
        home = phase_by_n(m["archived_with"])
        out += [
            f"{'#' if single else '##'} {milestone_heading(m)}",
            "",
            f"**{m['scope']} of {TOTAL_SPRINTS}**",
            "",
            f"> {m['line']}",
            "",
            f"<a href=\"{m['file']}\"><img src=\"{m['file']}\" width=\"760\" alt=\"{m['alt']}\"></a>",
            "",
            f"The milestone is archived as the last page of the Phase {home['n']} edition on Zenodo, "
            f"DOI {doi_link(home['v'])}.",
            "",
        ]
    out += ["---", "", "<sub>[All phases](../README.md)</sub>"]
    return "\n".join(out)


def readme():
    archived = len(PHASES)
    sprints_done = sum(len(p["sprints"]) for p in PHASES)
    pct = round(100 * sprints_done / TOTAL_SPRINTS)

    plain = lambda s: s.replace("%20", " ").replace("%2F", "/").replace("--", "-")  # noqa: E731
    badge = lambda label, msg, color, link: (  # noqa: E731
        f"<a href=\"{link}\"><img src=\"https://img.shields.io/badge/{label}-{msg}-{color}?style=flat-square\" "
        f"alt=\"{plain(label)}: {plain(msg)}\"></a>")

    out = [
        "<p align=\"center\">",
        "  <img src=\"assets/series-cover.png\" width=\"100%\" "
        "alt=\"MT24 Learning, Knowledge Sprint Series: 90 sprints in 27 phases\">",
        "</p>",
        "",
        "<p align=\"center\">",
        "  " + badge("phases%20archived", f"{archived}%20of%20{TOTAL_PHASES}", "0B9C93", "#phases"),
        "  " + badge("sprints", f"{sprints_done}%20of%20{TOTAL_SPRINTS}", "2A7CF6", "#every-sprint"),
        "  " + badge("archive", "Zenodo", "1682D4", ZENODO),
        "  " + badge("licence", "CC%20BY--NC--SA%204.0", "061127", "LICENSE"),
        "</p>",
        "",
        "# Knowledge Sprint Series",
        "",
        "**A free, open learning path of 90 sprints in 27 phases, from engineering practice to the "
        "philosophy of science, statistics and machine learning.** Each sprint is one portrait infographic "
        "that combines the core concepts, commands to try, a mini project and a list of trusted sources, "
        "so every claim can be checked against its origin. Each phase closes with a one-page summary.",
        "",
        f"This repository is the browsable index of the series: every published sprint, every phase summary and "
        f"the DOI of each phase's archived edition. The permanent, citable archive lives on Zenodo, in the "
        f"[MT24 Learning community]({ZENODO}). The same index is also published as a website: "
        f"[{SITE_URL.split('//')[1].rstrip('/')}]({SITE_URL}).",
        "",
        f"**Progress:** {archived} of {TOTAL_PHASES} phases archived, {sprints_done} of {TOTAL_SPRINTS} sprints ({pct}%).",
        "",
        "## Phases",
        "",
    ]

    tiles = []
    for p in PHASES:
        link = f"phases/{phase_dir(p)}/README.md"
        tiles.append((link, f"assets/thumbs/phase-{p['n']:02d}.jpg", f"<b>Phase {p['n']}</b> · {p['title']}",
                      sprint_label(p), f"Phase {p['n']} summary: {p['title']}"))
        for m in MILESTONES:
            if m["after"] == p["n"]:
                a, b = m["scope"].split("·")[0].replace("Phases", "").strip().split("–")
                tiles.append((milestone_link(m), f"assets/thumbs/milestone-{m['id']}.jpg",
                              f"<b>Milestone</b> · {m['title']}", m["scope"],
                              f"Milestone overview of Phases {a} to {b}"))
    if NEXT:
        state = "Being published now" if NEXT["status"] == "publishing" else "Coming next"
        tiles.append((None, "assets/thumbs/next-phase.jpg", f"<b>Phase {NEXT['n']}</b> · {NEXT['title']}",
                      state, f"Phase {NEXT['n']}, {state.lower()}"))

    out.append("<table>")
    for r in range(0, len(tiles), 3):
        out.append("  <tr>")
        for link, img, cap1, cap2, alt in tiles[r:r + 3]:
            pic = f"<img src=\"{img}\" width=\"260\" alt=\"{alt}\">"
            if link:
                pic = f"<a href=\"{link}\">{pic}</a>"
                cap1 = f"<a href=\"{link}\">{cap1}</a>"
            out.append(f"    <td align=\"center\" valign=\"top\" width=\"33%\">{pic}<br>{cap1}<br><sub>{cap2}</sub></td>")
        out.append("  </tr>")
    out.append("</table>")
    out += [
        "",
        "| Phase | Title | Sprints | First published | Archived edition |",
        "| ---: | --- | :---: | --- | --- |",
    ]
    for p in PHASES:
        out.append(f"| {p['n']} | [{p['title']}](phases/{phase_dir(p)}/README.md) | {sprint_range(p)} | "
                   f"{nice_date(p['first'])} | {doi_link(p['v'])} |")
    out.append("")
    if NEXT:
        verb = "is being published now" if NEXT["status"] == "publishing" else "comes next"
        out += [
            f"Phase {NEXT['n']}, *{NEXT['title']}* (Sprints {NEXT['sprints']}), {verb}. "
            "A phase joins this repository after all of its images are public and its edition is archived on Zenodo.",
            "",
        ]
    out += [
        "## Every sprint",
        "",
        "<details>",
        f"<summary>All {sprints_done} published sprints, in order</summary>",
        "",
        "| Sprint | Title | Phase |",
        "| ---: | --- | --- |",
    ]
    for p in PHASES:
        for s in p["sprints"]:
            anchor = gh_anchor(f"Sprint {s['n']}/{TOTAL_SPRINTS} · {s['title']}")
            out.append(f"| {s['n']} | [{s['title']}](phases/{phase_dir(p)}/README.md#{anchor}) | {p['n']} · {p['title']} |")
    out += [
        "",
        "</details>",
        "",
        "## How to read a sprint",
        "",
        "Every sprint image follows the same idea, even as the visual style changes from phase to phase:",
        "",
        "- **Core concepts**, in short cards.",
        "- **A figure** that shows the main idea, with real numbers where there are any (from Phase 2 onward).",
        "- **Try it**: commands or a short program you can run yourself, with its real output. "
        "Each phase page links the same code as files (**Run it**), with the library versions that reproduce the image.",
        "- **A mini project** to apply the sprint on your own.",
        "- **Trusted sources**: books, papers and official documentation, so every claim can be checked.",
        "",
        "Each phase ends with a one-page summary: what each sprint taught, what I can now do, mistakes avoided, "
        "and one phase project that ties the sprints together.",
        "",
        "## Cite",
        "",
        "Cite the archived edition of the phase you used. Each phase page gives its full reference, for example:",
        "",
        "```text",
        citation(PHASES[0]),
        "```",
        "",
        "GitHub's **Cite this repository** button (in the sidebar) gives a reference for the series as a whole.",
        "",
        "## Licence",
        "",
        "The images and text in this repository are licensed under "
        "[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](LICENSE) (CC BY-NC-SA 4.0). "
        "You may share and adapt them for non-commercial purposes, with attribution and under the same licence.",
        "",
        "Copyright © 2026 Mohammed Tahri (MT24).",
        "",
        "## Integrity",
        "",
        "Every image is kept at full resolution, as published. "
        "[`CHECKSUMS.sha256`](CHECKSUMS.sha256) lists the SHA-256 digest of each one, and of each code file, "
        "so you can confirm that a copy is unchanged:",
        "",
        "```sh",
        "sha256sum --check CHECKSUMS.sha256",
        "```",
        "",
        "## Follow the series",
        "",
        "New sprints are posted first on social media; once their phase is complete, it is archived on Zenodo and listed here.",
        "",
        " · ".join(f"[{name}]({url})" for name, url in SOCIAL),
        "",
        "---",
        "",
        f"<sub>By Mohammed Tahri (MT24) · ORCID [{ORCID}](https://orcid.org/{ORCID}) · "
        "part of [MT24 Learning](https://github.com/MT24Learning)</sub>",
    ]
    return "\n".join(out)


def citation_cff():
    lines = [
        "cff-version: 1.2.0",
        "message: >-",
        "  If you use this material, please cite the archived edition of the phase you used.",
        "  Each phase has its own DOI on Zenodo; they are listed under identifiers.",
        "type: dataset",
        'title: "MT24 Learning — Knowledge Sprint Series"',
        "abstract: >-",
        "  A free, open learning path of 90 sprints in 27 phases, from engineering practice to the",
        "  philosophy of science, statistics and machine learning. Each sprint is one portrait",
        "  infographic with core concepts, commands to try, a mini project and trusted sources;",
        "  each phase closes with a one-page summary.",
        "authors:",
        "  - family-names: Tahri",
        "    given-names: Mohammed",
        "    alias: MT24",
        f'    orcid: "https://orcid.org/{ORCID}"',
        "license: CC-BY-NC-SA-4.0",
        f'url: "{ZENODO}"',
        f'repository: "{REPO_URL}"',
        "keywords:",
    ]
    for k in ["open educational resource", "learning path", "infographics", "software engineering",
              "philosophy of science", "statistics", "machine learning", "information retrieval"]:
        lines.append(f'  - "{k}"')
    lines.append("identifiers:")
    for p in PHASES:
        lines += [
            "  - type: doi",
            f"    value: {p['v']}",
            f'    description: "Phase {p["n"]}: {p["title"]} ({sprint_label(p)}), version 1.0"',
        ]
    return "\n".join(lines)


# ---------------------------------------------------------------- next-phase tile

TILE_HTML = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:SG;src:url("file://{fonts}/SpaceGrotesk.ttf");font-weight:300 700}}
@font-face{{font-family:JBM;src:url("file://{fonts}/JetBrainsMono.ttf");font-weight:100 800}}
html,body{{margin:0;width:520px;height:650px;overflow:hidden}}
.t{{box-sizing:border-box;width:520px;height:650px;padding:56px 48px;color:#F4F8FC;
background:radial-gradient(420px 360px at 20% 10%,#12306a 0%,transparent 70%),linear-gradient(160deg,#0A1C3C,#061127 70%);position:relative;border:2px dashed #2A7CF6}}
.e{{font:500 22px/1 JBM;letter-spacing:.22em;color:#22E6D4}}
.n{{margin-top:150px;font:700 120px/0.9 SG;letter-spacing:-.04em}}
.h{{margin-top:22px;font:700 44px/1.08 SG;letter-spacing:-.02em}}
.s{{margin-top:22px;font:500 24px/1.3 SG;color:#93A6C4}}
.b{{position:absolute;left:48px;bottom:56px;font:500 20px/1 JBM;letter-spacing:.16em;color:#22E6D4}}
.dot{{display:inline-block;width:12px;height:12px;border-radius:50%;background:#22E6D4;margin-right:12px;box-shadow:0 0 14px #22E6D4}}
</style></head><body><div class="t">
<div class="e">NEXT PHASE</div>
<div class="n">{n}</div>
<div class="h">{title}</div>
<div class="s">Sprints {sprints} of 90</div>
<div class="b"><span class="dot"></span>{state}</div>
</div></body></html>"""


def tile_title(title):
    """Breaks a long title over two lines, before '&' or at the middle word."""
    t = title.replace("&", "&amp;")
    if len(title) <= 16:
        return t
    if " & " in title:
        a, b = title.split(" & ", 1)
        return f"{a} &amp;<br>{b}"
    words = title.split()
    best = min(range(1, len(words)), key=lambda k: abs(len(" ".join(words[:k])) - len(" ".join(words[k:]))))
    return " ".join(words[:best]) + "<br>" + " ".join(words[best:])


def fetch_fonts():
    folder = os.path.expanduser("~/.cache/knowledge-sprint-series/fonts")
    os.makedirs(folder, exist_ok=True)
    for name, path in FONTS.items():
        dst = os.path.join(folder, name)
        if not os.path.exists(dst):
            subprocess.run(["curl", "-sfL", "-o", dst, f"https://raw.githubusercontent.com/google/fonts/main/{path}"],
                           check=True)
    return folder


def next_tile():
    rel = "assets/thumbs/next-phase.jpg"
    if not NEXT:
        return False
    state = "BEING PUBLISHED NOW" if NEXT["status"] == "publishing" else "COMING NEXT"
    note = f"next-phase:{NEXT['n']}|{NEXT['title']}|{NEXT['sprints']}|{state}"
    if os.path.exists(os.path.join(ROOT, rel)) and jpeg_comment(os.path.join(ROOT, rel)) == note:
        return False
    from playwright.sync_api import sync_playwright
    fonts = fetch_fonts()
    work = os.path.join(os.path.expanduser("~/.cache/knowledge-sprint-series"), "tile")
    os.makedirs(work, exist_ok=True)
    html = os.path.join(work, "tile.html")
    with open(html, "w", encoding="utf-8") as f:
        f.write(TILE_HTML.format(fonts=fonts, n=NEXT["n"], title=tile_title(NEXT["title"]),
                                 sprints=NEXT["sprints"], state=state))
    png = os.path.join(work, "tile.png")
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 520, "height": 650}, device_scale_factor=1)
        page.goto("file://" + html)
        page.wait_for_timeout(600)
        page.screenshot(path=png)
        browser.close()
    return thumb(png, rel, note=note)


# ---------------------------------------------------------------- build

def has_text_chunks(path):
    with open(path, "rb") as f:
        data = f.read()
    return any(tag in data for tag in (b"tEXt", b"iTXt", b"zTXt", b"eXIf"))


def find_image(name, folders):
    for folder in folders:
        for dirpath, _, files in os.walk(folder):
            if name in files:
                return os.path.join(dirpath, name)
    return None


def snapshot():
    state = {}
    for dirpath, dirnames, files in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
        for name in files:
            path = os.path.join(dirpath, name)
            state[os.path.relpath(path, ROOT)] = sha256(path)
    return state


def build(image_folders):
    missing, notes = [], []
    for rel in image_paths():
        dst = os.path.join(ROOT, rel)
        found = find_image(os.path.basename(rel), image_folders) if image_folders else None
        if os.path.exists(dst):
            if found and sha256(found) != sha256(dst):
                notes.append(f"kept the published copy; a different file has the same name: {found}")
            continue
        if not found:
            missing.append(rel)
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(found, dst)
        if has_text_chunks(dst):
            notes.append(f"embedded text metadata in {rel}")
    if missing:
        sys.exit("Images not found (pass the folder that holds them with --images):\n  " + "\n  ".join(missing))

    for i, p in enumerate(PHASES):
        d = f"phases/{phase_dir(p)}"
        thumb(os.path.join(ROOT, d, p["summary"]), f"assets/thumbs/phase-{p['n']:02d}.jpg")
        write(f"{d}/README.md", phase_page(i, p))
    for m in MILESTONES:
        thumb(os.path.join(ROOT, "milestones", m["file"]), f"assets/thumbs/milestone-{m['id']}.jpg")
    write("milestones/README.md", milestone_page())
    next_tile()
    write("README.md", readme())
    write("CITATION.cff", citation_cff())
    write("CHECKSUMS.sha256", "\n".join(f"{sha256(os.path.join(ROOT, rel))}  {rel}" for rel in sorted(checked_paths())))
    import website
    website.build(sys.modules[__name__])
    for n in notes:
        print("note:", n)
    print(f"{len(image_paths())} images, {len(PHASES)} phase pages, {len(MILESTONES)} milestone(s)")


# ---------------------------------------------------------------- check

def check():
    problems = []
    anchors = {}
    pages = []
    for dirpath, dirnames, files in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        pages += [os.path.join(dirpath, f) for f in files if f.endswith(".md")
                  or (f.endswith(".html") and os.path.relpath(dirpath, ROOT).startswith("docs"))]
    for md in pages:
        text = open(md, encoding="utf-8").read()
        if md.endswith(".html"):
            anchors[md] = set(re.findall(r'\sid="([^"]+)"', text))
            continue
        seen, found = {}, set()
        for h in re.findall(r"^#{1,6} (.+)$", text, re.M):
            a = gh_anchor(h)
            seen[a] = seen.get(a, -1) + 1
            found.add(a if seen[a] == 0 else f"{a}-{seen[a]}")
        anchors[md] = found
    links = 0
    for md in pages:
        text = open(md, encoding="utf-8").read()
        for link in re.findall(r"\]\(([^)\s]+)\)", text) + re.findall(r'(?:href|src)="([^"]+)"', text):
            if link.startswith(("http://", "https://", "mailto:")):
                continue
            links += 1
            path, _, frag = link.partition("#")
            target = os.path.normpath(os.path.join(os.path.dirname(md), path)) if path else md
            rel = os.path.relpath(md, ROOT)
            if not os.path.exists(target):
                problems.append(f"broken link in {rel}: {link}")
            elif frag and target.endswith((".md", ".html")) and frag not in anchors.get(target, set()):
                problems.append(f"missing anchor in {rel}: {link}")

    listed = {}
    for line in open(os.path.join(ROOT, "CHECKSUMS.sha256"), encoding="utf-8").read().splitlines():
        digest, rel = line.split("  ", 1)
        listed[rel] = digest
    expected = set(image_paths())
    for rel in sorted(set(checked_paths()) - set(listed)):
        problems.append(f"not in CHECKSUMS.sha256: {rel}")
    for p in PHASES:
        if code_files(p):
            if not os.path.exists(os.path.join(ROOT, "phases", phase_dir(p), "code", "README.md")):
                problems.append(f"code folder without README.md: phases/{phase_dir(p)}/code")
            for s in p["sprints"]:
                if not code_files(p, s):
                    problems.append(f"no code file for Sprint {s['n']} in phases/{phase_dir(p)}/code")
    for rel, digest in sorted(listed.items()):
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            problems.append(f"listed but missing: {rel}")
        elif sha256(path) != digest:
            problems.append(f"checksum mismatch: {rel}")
    for folder in ("phases", "milestones"):
        for dirpath, _, files in os.walk(os.path.join(ROOT, folder)):
            for f in files:
                rel = os.path.relpath(os.path.join(dirpath, f), ROOT)
                if f.endswith(".png") and rel not in expected:
                    problems.append(f"image not in series_data.py: {rel}")
    known = {f"phases/{phase_dir(p)}" for p in PHASES}
    for d in sorted(os.listdir(os.path.join(ROOT, "phases"))):
        if f"phases/{d}" not in known:
            problems.append(f"folder not in series_data.py: phases/{d}")

    numbers = [s["n"] for p in PHASES for s in p["sprints"]]
    if numbers != list(range(1, len(numbers) + 1)):
        problems.append("sprint numbers are not 1, 2, 3, ... in order")
    if [p["n"] for p in PHASES] != list(range(1, len(PHASES) + 1)):
        problems.append("phase numbers are not 1, 2, 3, ... in order")
    if shutil.which("cffconvert"):
        r = subprocess.run(["cffconvert", "--validate", "-i", os.path.join(ROOT, "CITATION.cff")],
                           capture_output=True, text=True)
        if r.returncode != 0:
            problems.append("CITATION.cff: " + (r.stderr or r.stdout).strip().splitlines()[-1])

    for p in problems:
        print("problem:", p)
    print(f"checked {links} links, {len(listed)} checksums: "
          + ("all good" if not problems else f"{len(problems)} problem(s)"))
    return not problems


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--images", nargs="*", default=[], help="folders searched for images not yet in the repository")
    ap.add_argument("--check", action="store_true", help="check the repository without building")
    ap.add_argument("--pack", help="after building, write the changed files to this zip, at their repository paths")
    a = ap.parse_args()
    if a.check:
        sys.exit(0 if check() else 1)
    before = snapshot() if a.pack else None
    build(a.images)
    ok = check()
    if a.pack:
        after = snapshot()
        changed = sorted(rel for rel, digest in after.items() if before.get(rel) != digest)
        with zipfile.ZipFile(a.pack, "w", zipfile.ZIP_DEFLATED) as z:
            for rel in changed:
                z.write(os.path.join(ROOT, rel), rel)
        print(f"{len(changed)} changed file(s) packed in {a.pack}:")
        for rel in changed:
            print("  " + rel)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
