"""Builds the website's text pages from tools/texts/: one page per sprint and one per phase summary,
the search page, the 404 page, sitemap.xml, the page images, the social cards and the search index.

Called by tools/website.py after docs/index.html. A phase gets pages once tools/texts/phase_NN.py
exists; until then the site links to its page on GitHub. Everything written here is generated:
docs/sprints/, docs/phases/, docs/search/, docs/404.html, docs/sitemap.xml, docs/img/pages/,
docs/img/social/ and docs/pagefind/ (rebuilt from scratch by Pagefind on every build).
"""
import builtins
import hashlib
import importlib.util
import io
import json
import keyword
import os
import re
import shutil
import subprocess
import sys
import tokenize
from html import escape

PAGEFIND = "1.6.0"
TEXTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "texts")
RAW = "https://raw.githubusercontent.com/MT24Learning/knowledge-sprint-series/main"
CC = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
CIRCLED = "①②③④⑤⑥⑦⑧⑨"
PANEL_BG = (10, 28, 60)          # --navy, the background accents are read against


# ---------------------------------------------------------------- data

def load_texts():
    """{phase number: module} for every tools/texts/phase_NN.py."""
    out = {}
    if not os.path.isdir(TEXTS):
        return out
    for name in sorted(os.listdir(TEXTS)):
        m = re.fullmatch(r"phase_(\d\d)\.py", name)
        if not m:
            continue
        spec = importlib.util.spec_from_file_location(f"texts_{m.group(1)}", os.path.join(TEXTS, name))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out[int(m.group(1))] = mod
    return out


def text_problems(b, texts):
    """Consistency checks between tools/texts/ and series_data.py, used by build.py --check."""
    problems = []
    for n, t in texts.items():
        p = next((q for q in b.PHASES if q["n"] == n), None)
        if not p:
            problems.append(f"tools/texts/phase_{n:02d}.py: Phase {n} is not in series_data.py")
            continue
        want = [s["n"] for s in p["sprints"]]
        if sorted(t.SPRINTS) != want:
            problems.append(f"tools/texts/phase_{n:02d}.py: sprints {sorted(t.SPRINTS)} differ from {want}")
        for k, s in t.SPRINTS.items():
            sp = next((x for x in p["sprints"] if x["n"] == k), None)
            if sp and s.get("em") and s["em"] not in sp["title"]:
                problems.append(f"Sprint {k}: em word {s['em']!r} is not in the title")
            for text, url in s["sources"]:
                if not url.startswith("https://"):
                    problems.append(f"Sprint {k}: source without an https link: {text}")
            numbers = [c["no"] for c in s["cards"]]
            if numbers != sorted(numbers):
                problems.append(f"Sprint {k}: cards out of order {numbers}")
        for text, url in t.SUMMARY.get("references", []):
            if not url.startswith("https://"):
                problems.append(f"Phase {n} summary: reference without an https link: {text}")
        if t.SUMMARY.get("em") and t.SUMMARY["em"] not in p["title"]:
            problems.append(f"Phase {n} summary: em word {t.SUMMARY['em']!r} is not in the title")
    return problems


# ---------------------------------------------------------------- text helpers

def e(text):
    return escape(str(text), quote=True)


def md(text):
    """Escapes text, then **bold**, *italic* and no-break spaces inside thousands (3 941)."""
    t = e(text)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    return re.sub(r"(?<=\d) (?=\d{3}(?!\d))", " ", t)


def plain(text):
    return re.sub(r"\*\*?(.+?)\*\*?", r"\1", text)


def title_html(title, em):
    """The title with its one emphasised word, as on the image."""
    t = e(title)
    if em:
        t = t.replace(e(em), f"<em>{e(em)}</em>", 1)
    return re.sub(r"(?<=\d) (?=\d{3}(?!\d))", " ", t)


def _lin(c):
    c /= 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def _lum(rgb):
    r, g, bl = (_lin(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * bl


def contrast(a, b):
    la, lb = sorted((_lum(a), _lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def tint(hex_colour, target=5.0):
    """The image's accent, lightened just enough to read on the site's navy (WCAG contrast >= 5)."""
    rgb = tuple(int(hex_colour[i:i + 2], 16) for i in (1, 3, 5))
    for k in range(0, 101):
        mix = tuple(round(c + (255 - c) * k / 100) for c in rgb)
        if contrast(mix, PANEL_BG) >= target:
            return "#%02x%02x%02x" % mix
    return "#ffffff"


# ---------------------------------------------------------------- code

BUILTINS = set(dir(builtins))


def split_code(path):
    """A sprint file is its code followed by the printed output as comment lines."""
    lines = open(path, encoding="utf-8").read().rstrip("\n").split("\n")
    k = len(lines)
    while k > 0 and lines[k - 1].startswith("#") and not lines[k - 1].startswith("#!"):
        k -= 1
    code, out = lines[:k], lines[k:]
    if not code or not out:
        return "\n".join(lines), ""
    return "\n".join(code).rstrip("\n"), "\n".join(l[2:] if l.startswith("# ") else l[1:] for l in out)


def highlight(src, lang):
    if lang != "py":
        return re.sub(r"(?m)^(\s*)(#.*)$", lambda m: m.group(1) + f'<span class="c-com">{m.group(2)}</span>',
                      e(src))
    starts, pos = [0], 0
    for line in src.splitlines(keepends=True):
        pos += len(line)
        starts.append(pos)
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    except (tokenize.TokenError, SyntaxError, IndentationError):
        return e(src)
    out, at, prev = [], 0, None
    string_types = {tokenize.STRING} | {getattr(tokenize, n) for n in ("FSTRING_START", "FSTRING_MIDDLE",
                                                                        "FSTRING_END") if hasattr(tokenize, n)}
    for t in toks:
        a = starts[t.start[0] - 1] + t.start[1] if t.start[0] - 1 < len(starts) else len(src)
        z = starts[t.end[0] - 1] + t.end[1] if t.end[0] - 1 < len(starts) else len(src)
        if a < at:
            continue
        out.append(e(src[at:a]))
        text = src[a:z]
        cls = None
        if t.type == tokenize.NAME:
            if keyword.iskeyword(t.string) or t.string in ("match", "case"):
                cls = "kw"
            elif prev in ("def", "class"):
                cls = "fn"
            elif t.string in BUILTINS:
                cls = "bi"
        elif t.type in string_types:
            cls = "str"
        elif t.type == tokenize.NUMBER:
            cls = "num"
        elif t.type == tokenize.COMMENT:
            cls = "com"
        out.append(f'<span class="c-{cls}">{e(text)}</span>' if cls else e(text))
        at = z
        if t.type == tokenize.NAME:
            prev = t.string
        elif t.type not in (tokenize.NL, tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT):
            prev = None
    out.append(e(src[at:]))
    return "".join(out)


# ---------------------------------------------------------------- shared layout

def head(b, *, title, description, path, image, image_size, depth, jsonld, kind="article"):
    up = "../" * depth
    url = b.SITE_URL + path
    w = [
        "<!doctype html>",
        '<html lang="en">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{e(title)}</title>",
        f'<meta name="description" content="{e(description)}">',
        f'<link rel="canonical" href="{e(url)}">',
        '<meta name="theme-color" content="#061127">',
        '<meta name="color-scheme" content="dark">',
        f'<meta property="og:type" content="{kind}">',
        '<meta property="og:site_name" content="Knowledge Sprint Series · MT24 Learning">',
        f'<meta property="og:title" content="{e(title)}">',
        f'<meta property="og:description" content="{e(description)}">',
        f'<meta property="og:url" content="{e(url)}">',
        f'<meta property="og:image" content="{e(b.SITE_URL + image)}">',
        f'<meta property="og:image:width" content="{image_size[0]}">',
        f'<meta property="og:image:height" content="{image_size[1]}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<link rel="icon" href="{up}img/brand/favicon.svg" type="image/svg+xml">',
        f'<link rel="apple-touch-icon" href="{up}img/brand/apple-touch-icon.png">',
        f'<link rel="preload" href="{up}fonts/space-grotesk.woff2" as="font" type="font/woff2" crossorigin>',
        f'<link rel="stylesheet" href="{up}style.css">',
        '<script>document.documentElement.classList.add("js")</script>',
    ]
    for block in jsonld:
        w.append('<script type="application/ld+json">' + json.dumps(block, ensure_ascii=False) + "</script>")
    w += ["</head>", '<body class="page">', '<a class="skip" href="#main">Skip to the text</a>']
    w += site_header(b, up)
    return w


def site_header(b, up):
    w = ['<header class="site">', '  <div class="bar wrap">',
         f'    <a class="brand" href="{up or "./"}" aria-label="Knowledge Sprint Series, home">',
         f'      <img src="{up}img/brand/mt24-badge.svg" width="40" height="40" alt="">',
         '      <span><b>Knowledge Sprint Series</b><small>MT24 Learning</small></span>', "    </a>",
         '    <nav aria-label="Sections">']
    for href, label in [("#phases", "Phases"), ("#results", "Results"), ("#sprint", "How it works"),
                        ("#cite", "Cite")]:
        w.append(f'      <a href="{up or "./"}{href}">{label}</a>')
    w.append(f'      <a class="search-link" href="{up}search/">Search<kbd>/</kbd></a>')
    w.append(f'      <a class="gh" href="{b.REPO_URL}">GitHub</a>')
    w += ["    </nav>", "  </div>", "</header>"]
    return w


def site_footer(b, up):
    return [
        '<footer class="site">', '  <div class="wrap foot-row">',
        "    <p>© 2026 Mohammed Tahri (MT24) · Images and text under "
        f'<a href="{CC}">CC BY-NC-SA 4.0</a> · Sprint code under <a href="{b.REPO_URL}/blob/main/LICENSE-CODE">MIT</a></p>',
        f'    <p><a href="https://github.com/MT24Learning">MT24 Learning</a> · <a href="{b.REPO_URL}">Source and data</a> · '
        f'<a href="{up}fonts/OFL.txt">Font licences</a></p>',
        "  </div>", "</footer>", f'<script src="{up}site.js" defer></script>', "</body>", "</html>",
    ]


def person(b):
    return {"@type": "Person", "name": "Mohammed Tahri", "alternateName": "MT24",
            "sameAs": [f"https://orcid.org/{b.ORCID}"] + [url for _, url in b.SOCIAL]}


def crumbs_ld(b, items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i, "name": name, "item": b.SITE_URL + path}
                                for i, (name, path) in enumerate(items, 1)]}


def road(b, texts, current):
    """90 cells, one per sprint: published ones filled, those with a page linked, the current one lit."""
    by_n, starts = {}, set()
    for p in b.PHASES:
        starts.add(p["sprints"][0]["n"])
        for s in p["sprints"]:
            by_n[s["n"]] = (p, s)
    done = len(by_n)
    w = [f'<div class="road" role="img" aria-label="Sprint {current} of {b.TOTAL_SPRINTS}; '
         f'{done} of {b.TOTAL_SPRINTS} published">']
    for n in range(1, b.TOTAL_SPRINTS + 1):
        cls = ["cell"]
        if n in starts and n > 1:
            cls.append("gap")
        if n in by_n:
            cls.append("on")
        if n == current:
            cls.append("here")
        p, s = by_n.get(n, (None, None))
        label = f"Sprint {n}" + (f" · {s['title']}" if s else "")
        if p and p["n"] in texts and n != current:
            w.append(f'<a class="{" ".join(cls)}" href="../{n}/" title="{e(label)}" aria-hidden="true" tabindex="-1"></a>')
        else:
            w.append(f'<span class="{" ".join(cls)}" title="{e(label)}"></span>')
    w.append("</div>")
    return "".join(w)


def spots(png, regions):
    """Invisible boxes over the image, one per part, in percent of its size (see site.js: reading spotlight)."""
    from PIL import Image
    with Image.open(png) as im:
        W, H = im.size
    out = []
    for key, (x0, y0, x1, y1) in regions.items():
        out.append(f'<span class="spot" data-spot="{key}" aria-hidden="true" style="left:{100 * x0 / W:.2f}%;'
                   f'top:{100 * y0 / H:.2f}%;width:{100 * (x1 - x0) / W:.2f}%;height:{100 * (y1 - y0) / H:.2f}%"></span>')
    return "".join(out)


def image_figure(img, alt, png, regions, caption, search_image):
    return [
        '  <figure class="t-image">',
        f'    <div class="spotlit"><img src="{img}" width="1080" height="1350" alt="{alt}">{spots(png, regions)}</div>',
        f'    <span hidden data-pagefind-meta="image:{search_image}"></span>',
        f'    <figcaption data-pagefind-ignore>{caption}</figcaption>',
        '    <p class="spot-hint" data-pagefind-ignore>The part of the image you are reading lights up. '
        "Tap a part to jump to its text.</p>",
        "  </figure>",
    ]


def cite_block(b, p, ident):
    return [
        '<section class="cite-strip wrap" data-pagefind-ignore>',
        '  <p class="label">Cite this phase</p>',
        '  <div class="cite-box">',
        f'    <pre id="{ident}">{e(b.citation(p))}</pre>',
        f'    <button class="copy" type="button" data-copy="{ident}">Copy</button>',
        "  </div>",
        f'  <p class="cite-note">Version DOI <a class="doi" href="https://doi.org/{p["v"]}">{p["v"]}</a> · all versions '
        f'<a class="doi" href="https://doi.org/{p["c"]}">{p["c"]}</a> · first published {b.nice_date(p["first"])}</p>',
        "</section>",
    ]


# ---------------------------------------------------------------- sprint page

def sprint_page(b, texts, p, s, t, prev_s, next_s):
    n = s["n"]
    up = "../../"
    acc = texts[p["n"]].PHASE["accents"][n]
    acc_text = tint(acc)
    path = f"sprints/{n}/"
    folder = b.phase_dir(p)
    full = f"{RAW}/phases/{folder}/{s['file']}"
    description = f"{s['tagline']} {s['covers']}"
    ld = {
        "@context": "https://schema.org", "@type": "LearningResource",
        "name": f"Sprint {n}: {s['title']}", "headline": s["title"], "description": description,
        "url": b.SITE_URL + path, "image": f"{b.SITE_URL}img/pages/sprint-{n}.jpg", "inLanguage": "en",
        "isAccessibleForFree": True, "license": CC, "learningResourceType": "Infographic",
        "author": person(b), "position": n,
        "isPartOf": {"@type": "CreativeWork", "name": f"Phase {p['n']}: {p['title']}",
                     "url": f"{b.SITE_URL}phases/{p['n']}/", "identifier": f"https://doi.org/{p['v']}"},
        "citation": [{"@type": "CreativeWork", "name": plain(text), "url": url} for text, url in t["sources"]],
    }
    crumbs = [("Home", ""), (f"Phase {p['n']}: {p['title']}", f"phases/{p['n']}/"), (f"Sprint {n}", path)]
    w = head(b, title=f"Sprint {n}: {s['title']} · Knowledge Sprint Series", description=description, path=path,
             image=f"img/social/sprint-{n}.jpg", image_size=(1200, 630), depth=2, jsonld=[ld, crumbs_ld(b, crumbs)])
    w.append(f'<main id="main" class="text-page" style="--acc:{acc};--acc-text:{acc_text}">')
    w += [
        '<nav class="crumbs wrap" aria-label="Breadcrumb" data-pagefind-ignore>',
        f'  <a href="{up}">Home</a><span>/</span><a href="{up}phases/{p["n"]}/">Phase {p["n"]} · {e(p["title"])}</a>'
        f'<span>/</span><span aria-current="page">Sprint {n}</span>',
        "</nav>",
        '<header class="t-head wrap" data-spot="head">',
        "  " + road(b, texts, n),
        f'  <p class="eyebrow"><span>Phase {p["n"]} · Sprint {n}/{b.TOTAL_SPRINTS} · '
        f'<span data-pagefind-filter="Phase">{e(p["title"])}</span></span>'
        f'<span class="names">{e(t["names"])}</span></p>',
        f'  <h1 data-pagefind-meta="title">{title_html(s["title"], t.get("em"))}</h1>',
        f'  <p class="tagline">{e(s["tagline"])}</p>',
        f'  <p class="in-short"><b>In short.</b> {md(s["covers"])}</p>',
        '  <span hidden data-pagefind-filter="Type">Sprint</span>',
        "</header>",
        '<div class="t-body wrap">',
    ]
    regions = dict(texts[p["n"]].PHASE["regions"], **t.get("regions", {}))
    w += image_figure(f"../../img/pages/sprint-{n}.jpg",
                      f'Sprint {n} of {b.TOTAL_SPRINTS} infographic: {e(s["title"])}. {e(s["tagline"])} '
                      "The full text of the image is on this page.",
                      os.path.join(b.ROOT, "phases", folder, s["file"]), regions,
                      f'<a href="{full}">Full resolution</a><span>2160 × 2700 PNG</span>'
                      f'<a href="{up}phases/{p["n"]}/">Phase summary</a>', f"{site_path(b)}img/pages/sprint-{n}-s.jpg")
    w += [
        '  <article class="t-text">',
    ]
    w += figure_words(t["fig"])
    cards = t["cards"]
    before = [c for c in cards if c["no"] < "05"]
    after = [c for c in cards if c["no"] > "05"]
    w.append('    <div class="t-cards">')
    w += [line for c in before for line in card(c)]
    w.append("    </div>")
    w += try_it(b, p, s, t)
    w.append('    <div class="t-cards">')
    w += [line for c in after for line in card(c)]
    w.append("    </div>")
    w += [
        '    <section class="t-sources" aria-labelledby="sources" data-spot="R">',
        '      <h2 id="sources"><span class="key" data-pagefind-ignore>R</span> Trusted Sources</h2>',
        '      <ol class="sources">',
    ]
    for text, url in t["sources"]:
        w.append(f'        <li><a href="{e(url)}" rel="noopener">{md(text)}</a></li>')
    w += ["      </ol>", "    </section>", "  </article>", "</div>"]
    w += pager(b, texts, prev_s, next_s, p, up)
    w += cite_block(b, p, f"cite-{n}")
    w.append("</main>")
    w += site_footer(b, up)
    return "\n".join(w)


def figure_words(fig):
    w = ['    <section class="t-fig" aria-labelledby="fig" data-spot="fig">',
         f'      <h2 id="fig">Fig. 1 <span>in words</span></h2>',
         f'      <p class="fig-title">{md(fig["title"])}</p>',
         '      <ol class="panels">']
    for k, (title, lines) in enumerate(fig["panels"]):
        w.append(f'        <li><h3><span class="ball" data-pagefind-ignore>{k + 1}</span> {md(title)}</h3><ul>')
        w += [f"          <li>{md(x)}</li>" for x in lines]
        w.append("        </ul></li>")
    w += ["      </ol>", f'      <aside class="notes"><h3>{e(fig["notes_title"])}</h3><ol>']
    for k, (key, text) in enumerate(fig["notes"]):
        w.append(f'        <li><span class="ball">{k + 1}</span><b>{e(key)}</b> {md(text)}</li>')
    w += ["      </ol></aside>", "    </section>"]
    return w


def card(c):
    stamp = (f'<span class="stamp" data-pagefind-ignore>{e(c["tag"])}</span>' if c.get("claim")
             else f'<span class="tag" data-pagefind-ignore>{e(c["tag"])}</span>')
    w = [f'      <section class="t-card{" claim" if c.get("claim") else ""}" aria-labelledby="card-{c["no"]}" '
         f'data-spot="{c["no"]}">',
         f'        <h2 id="card-{c["no"]}"><span class="key" data-pagefind-ignore>{c["no"]}</span> <span class="h">{md(c["title"])}</span> {stamp}</h2>',
         "        <ul>"]
    w += [f"          <li>{md(x)}</li>" for x in c["items"]]
    w += ["        </ul>", f'        <p class="note">{md(c["note"])}</p>', "      </section>"]
    return w


def try_it(b, p, s, t):
    files = b.code_files(p, s)
    folder = b.phase_dir(p)
    w = ['    <section class="t-try" aria-labelledby="try" data-spot="05">',
         f'      <h2 id="try"><span class="key" data-pagefind-ignore>05</span> Try It Yourself '
         f'<span class="ver" data-pagefind-ignore>{e(t["tryit"]["versions"])}</span></h2>']
    main_file = next((f for f in files if f.startswith(f"sprint{s['n']:02d}")), files[0] if files else None)
    if main_file:
        path = os.path.join(b.ROOT, "phases", folder, "code", main_file)
        code, out = split_code(path)
        lang = "py" if main_file.endswith(".py") else "sh"
        ident = f"code-{s['n']}"
        w += ['      <div class="code-box">',
              f'        <p class="file"><span>{e(main_file)}</span><button class="copy" type="button" data-copy="{ident}">Copy</button></p>',
              f'        <pre class="code" id="{ident}" data-pagefind-ignore><code>{highlight(code, lang)}</code></pre>']
        if out:
            w += ['        <p class="file out">Output, as printed on the image</p>',
                  f'        <pre class="output"><code>{e(out)}</code></pre>']
        w.append("      </div>")
        tree = f"{b.REPO_URL}/blob/main/phases/{folder}/code"
        links = [f'<a href="{tree}/{f}">{e(f)}</a>' for f in files]
        links.append(f'<a href="{tree}/README.md">versions, data and steps</a>')
        w.append(f'      <p class="run" data-pagefind-ignore><b>Run it.</b> {" · ".join(links)}</p>')
    w += [f'      <p class="check">{md(t["tryit"]["check"])}</p>', "    </section>"]
    return w


def pager(b, texts, prev_s, next_s, p, up):
    def link(item, arrow):
        if not item:
            return '<span class="pg-empty"></span>'
        q, s = item
        if q["n"] in texts:
            href = f"{up}sprints/{s['n']}/"
            ext = ""
        else:
            href = f"{b.REPO_URL}/blob/main/phases/{b.phase_dir(q)}/README.md"
            ext = ' <span class="ext">on GitHub</span>'
        side = "prev" if arrow == "←" else "next"
        label = f"{arrow} Sprint {s['n']}" if arrow == "←" else f"Sprint {s['n']} {arrow}"
        return (f'<a class="pg-{side}" href="{href}"><small>{label}{ext}</small>'
                f'<b>{e(s["title"])}</b></a>')
    return ['<nav class="pager wrap" aria-label="Sprints" data-pagefind-ignore>', "  " + link(prev_s, "←"),
            f'  <a class="pg-up" href="{up}phases/{p["n"]}/"><small>Phase {p["n"]}</small><b>{e(p["title"])}</b></a>',
            "  " + link(next_s, "→"), "</nav>"]


# ---------------------------------------------------------------- phase page

def phase_page(b, texts, i, p):
    t = texts[p["n"]]
    S = t.SUMMARY
    up = "../../"
    path = f"phases/{p['n']}/"
    folder = b.phase_dir(p)
    full = f"{RAW}/phases/{folder}/{p['summary']}"
    first_acc = t.PHASE["accents"][p["sprints"][0]["n"]]
    description = f"Phase {p['n']} of {b.TOTAL_PHASES}, {b.sprint_label(p)}: {p['line']}"
    ld = {
        "@context": "https://schema.org", "@type": "CreativeWork",
        "name": f"Phase {p['n']}: {p['title']}", "description": p["line"], "abstract": plain(S["abstract"]),
        "url": b.SITE_URL + path, "identifier": f"https://doi.org/{p['v']}", "sameAs": f"https://doi.org/{p['v']}",
        "datePublished": p["first"], "image": f"{b.SITE_URL}img/pages/phase-{p['n']}.jpg", "inLanguage": "en",
        "isAccessibleForFree": True, "license": CC, "author": person(b),
        "isPartOf": {"@type": "CreativeWorkSeries", "name": "MT24 Learning — Knowledge Sprint Series", "url": b.SITE_URL},
        "hasPart": [{"@type": "LearningResource", "name": f"Sprint {s['n']}: {s['title']}",
                     "url": f"{b.SITE_URL}sprints/{s['n']}/"} for s in p["sprints"]],
        "citation": [{"@type": "CreativeWork", "name": text, "url": url} for text, url in S["references"]],
    }
    crumbs = [("Home", ""), (f"Phase {p['n']}: {p['title']}", path)]
    w = head(b, title=f"Phase {p['n']}: {p['title']} · Knowledge Sprint Series", description=description, path=path,
             image=f"img/social/phase-{p['n']}.jpg", image_size=(1200, 630), depth=2, jsonld=[ld, crumbs_ld(b, crumbs)])
    grad = ", ".join(tint(t.PHASE["accents"][s["n"]]) for s in p["sprints"])
    w.append(f'<main id="main" class="text-page phase" style="--acc:{first_acc};--acc-text:{tint(first_acc)};'
             f'--grad:linear-gradient(92deg, {grad})">')
    chips = "".join(f'<a class="chip" style="--c:{tint(t.PHASE["accents"][s["n"]])}" href="{up}sprints/{s["n"]}/">{s["n"]}</a>'
                    for s in p["sprints"])
    w += [
        '<nav class="crumbs wrap" aria-label="Breadcrumb" data-pagefind-ignore>',
        f'  <a href="{up}">Home</a><span>/</span><span aria-current="page">Phase {p["n"]} · {e(p["title"])}</span>',
        "</nav>",
        '<header class="t-head wrap" data-spot="head">',
        '  <p class="ribbon">' + "".join(f"<span>{e(x)}</span>" for x in (S["issue"], *S["ribbon"])) + "</p>",
        f'  <p class="eyebrow"><span>{e(S["kicker"])}</span></p>',
        f'  <h1 data-pagefind-meta="title">{title_html(p["title"], S.get("em"))}</h1>',
        f'  <p class="tagline">{md(S["dek"])}</p>',
        f'  <p class="byline"><b>Mohammed Tahri</b> · MT24 · <a href="https://orcid.org/{b.ORCID}">ORCID {b.ORCID}</a>{chips}</p>',
        f'  <span hidden data-pagefind-filter="Phase">{e(p["title"])}</span><span hidden data-pagefind-filter="Type">Phase summary</span>',
        "</header>",
        '<div class="t-body wrap">',
    ]
    w += image_figure(f"../../img/pages/phase-{p['n']}.jpg",
                      f'Phase {p["n"]} summary, a journal front page: {e(p["title"])}. The full text of the page follows.',
                      os.path.join(b.ROOT, "phases", folder, p["summary"]), t.PHASE["summary_regions"],
                      f'<a href="{full}">Full resolution</a><span>2160 × 2700 PNG</span>'
                      f'<a href="{b.REPO_URL}/blob/main/phases/{folder}/README.md">Phase on GitHub</a>',
                      f"{site_path(b)}img/thumbs/phase-{p['n']:02d}.jpg")
    w += [
        '  <article class="t-text">',
        '    <section class="t-abstract" aria-labelledby="abstract" data-spot="abstract">',
        '      <h2 id="abstract">Abstract</h2>',
        f'      <p class="dropcap">{md(S["abstract"])}</p>',
        "    </section>",
        '    <section aria-labelledby="highlights" data-spot="highlights">',
        '      <h2 id="highlights">Highlights</h2>',
        '      <ul class="highlights">',
    ]
    for n, text in S["highlights"]:
        w.append(f'        <li><a class="chip" style="--c:{tint(t.PHASE["accents"][n])}" href="{up}sprints/{n}/">{n}</a>'
                 f'<span>{md(text)}</span></li>')
    w += ["      </ul>", "    </section>",
          '    <section class="t-fig" aria-labelledby="figures" data-spot="figures">',
          '      <h2 id="figures">Figures <span>in words</span></h2>', '      <ol class="panels one">']
    for k, (n, title, lines) in enumerate(S["figures"], 1):
        w.append(f'        <li><h3><span class="ball" data-pagefind-ignore>{k}</span> Fig. {k} · {md(title)} <a class="fig-sprint" '
                 f'style="--c:{tint(t.PHASE["accents"][n])}" href="{up}sprints/{n}/">Sprint {n}</a></h3><ul>')
        w += [f"          <li>{md(x)}</li>" for x in lines]
        w.append("        </ul></li>")
    w += ["      </ol>", "    </section>",
          '    <section aria-labelledby="methods" data-spot="methods">', '      <h2 id="methods"><span class="sec" data-pagefind-ignore>1</span> Methods</h2>',
          f'      <p>{md(S["methods"])}</p>', "    </section>",
          '    <section class="misread" aria-labelledby="misreadings" data-spot="misreadings">',
          '      <h2 id="misreadings"><span class="sec" data-pagefind-ignore>2</span> Common Misreadings, Checked</h2>', "      <ol>"]
    for claim, checked, src in S["misreadings"]:
        w.append(f'        <li><p class="struck"><s>“{md(claim)}”</s></p><p><b class="ok">Checked</b> {md(checked)}</p>'
                 f'<p class="by">{md(src)}</p></li>')
    w += ["      </ol>", "    </section>",
          '    <section aria-labelledby="issue" data-spot="issue">', '      <h2 id="issue">In This Issue</h2>', '      <ol class="issue">']
    for s in p["sprints"]:
        st = texts[p["n"]].SPRINTS[s["n"]]
        w.append(f'        <li><a href="{up}sprints/{s["n"]}/" style="--c:{tint(t.PHASE["accents"][s["n"]])}">'
                 f'<img src="../../img/pages/sprint-{s["n"]}-s.jpg" width="400" height="500" loading="lazy" alt="">'
                 f'<span class="meta"><span>Sprint {s["n"]}/{b.TOTAL_SPRINTS}</span></span>'
                 f'<b>{title_html(s["title"], st.get("em"))}</b><i>{e(s["tagline"])}</i></a></li>')
    w += ["      </ol>", "    </section>", '    <div class="boxes">']
    for k, (title, text) in enumerate(S["boxes"]):
        c = tint(t.PHASE["accents"][p["sprints"][min(k, len(p["sprints"]) - 1)]["n"]])
        w.append(f'      <section style="--c:{c}" data-spot="box-{k}"><h2>{e(title)}</h2><p>{md(text)}</p></section>')
    w += ["    </div>",
          '    <section class="t-sources" aria-labelledby="references" data-spot="references">',
          '      <h2 id="references"><span class="key" data-pagefind-ignore>R</span> References</h2>', '      <ol class="sources">']
    for text, url in S["references"]:
        w.append(f'        <li><a href="{e(url)}" rel="noopener">{md(text)}</a></li>')
    w += ["      </ol>", "    </section>"]
    vol, title, line = S["next_issue"]
    w += ['    <aside class="next-issue" data-pagefind-ignore data-spot="next">',
          f'      <p class="label">Next issue · {e(vol)}</p><p class="ni-title">{e(title)}</p><p class="ni-line">{e(line)}</p>',
          "    </aside>", "  </article>", "</div>"]
    w += phase_pager(b, texts, i, up)
    w += cite_block(b, p, f"cite-phase-{p['n']}")
    w.append("</main>")
    w += site_footer(b, up)
    return "\n".join(w)


def phase_pager(b, texts, i, up):
    def link(q, arrow):
        if not q:
            return '<span class="pg-empty"></span>'
        href = f"{up}phases/{q['n']}/" if q["n"] in texts else f"{b.REPO_URL}/blob/main/phases/{b.phase_dir(q)}/README.md"
        ext = "" if q["n"] in texts else ' <span class="ext">on GitHub</span>'
        side = "prev" if arrow == "←" else "next"
        label = f"{arrow} Phase {q['n']}" if arrow == "←" else f"Phase {q['n']} {arrow}"
        return f'<a class="pg-{side}" href="{href}"><small>{label}{ext}</small><b>{e(q["title"])}</b></a>'
    prev_p = b.PHASES[i - 1] if i > 0 else None
    next_p = b.PHASES[i + 1] if i + 1 < len(b.PHASES) else None
    return ['<nav class="pager wrap" aria-label="Phases" data-pagefind-ignore>', "  " + link(prev_p, "←"),
            f'  <a class="pg-up" href="{up}#phases"><small>All phases</small><b>The path so far</b></a>',
            "  " + link(next_p, "→"), "</nav>"]


# ---------------------------------------------------------------- search, 404, sitemap

def site_path(b):
    """The site's path on its host: /knowledge-sprint-series/."""
    return re.sub(r"^https?://[^/]+", "", b.SITE_URL) or "/"


def search_page(b):
    ld = {"@context": "https://schema.org", "@type": "WebPage", "name": "Search · Knowledge Sprint Series",
          "url": b.SITE_URL + "search/"}
    w = head(b, title="Search · Knowledge Sprint Series", description="Search the text of every sprint and phase "
             "summary of the Knowledge Sprint Series: concepts, checked claims, numbers and sources.",
             path="search/", image="img/brand/social.png", image_size=(1280, 640), depth=1, jsonld=[ld], kind="website")
    w.insert(w.index('<link rel="stylesheet" href="../style.css">'), '<link rel="stylesheet" href="../pagefind/pagefind-ui.css">')
    base = site_path(b)
    w += ['<main id="main" class="text-page search-page">',
          '  <header class="t-head wrap">',
          '    <p class="eyebrow"><span>Search</span></p>',
          "    <h1>Search the <em>text</em> of the series</h1>",
          '    <p class="tagline">Every sprint page carries the full text of its image: concepts, checked claims, numbers '
          "and sources. Try a word, a number or an author.</p>",
          "  </header>",
          '  <div class="wrap"><div id="search" class="search-box"></div>',
          '  <p class="search-note">The search runs in your browser; nothing you type leaves this page. '
          "Phases join the search as their text pages are added.</p></div>",
          "</main>",
          '<script src="../pagefind/pagefind-ui.js"></script>',
          "<script>",
          "  window.addEventListener('DOMContentLoaded', function () {",
          f"    var ui = new PagefindUI({{ element: '#search', baseUrl: '{base}', showSubResults: true, showImages: true,",
          "      resetStyles: true,",
          "      translations: { placeholder: 'Search sprints, claims, numbers, authors…' } });",
          "    var q = new URLSearchParams(location.search).get('q');",
          "    if (q) ui.triggerSearch(q);",
          "  });",
          "</script>"]
    w += site_footer(b, "../")
    return "\n".join(w)


def not_found_page(b):
    base = b.SITE_URL
    w = ["<!doctype html>", '<html lang="en">', "<head>", '<meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width, initial-scale=1">',
         "<title>Page not found · Knowledge Sprint Series</title>", '<meta name="robots" content="noindex">',
         f'<link rel="icon" href="{base}img/brand/favicon.svg" type="image/svg+xml">',
         f'<link rel="stylesheet" href="{base}style.css">', "</head>", '<body class="page">',
         '<main id="main" class="text-page lost">', '  <div class="wrap">',
         '    <p class="label">404 · not found</p>',
         "    <h1>This page is <em>not in the series</em>.</h1>",
         '    <p class="tagline">The link may be old, or the page may not be written yet. The series itself is all here.</p>',
         '    <p class="actions">'
         f'<a class="btn primary" href="{base}">Back to the series</a>'
         f'<a class="btn ghost" href="{base}search/">Search the text</a></p>',
         "  </div>", "</main>", "</body>", "</html>"]
    return "\n".join(w)


def sitemap(b, texts):
    urls = [b.SITE_URL]
    for p in b.PHASES:
        if p["n"] in texts:
            urls.append(f"{b.SITE_URL}phases/{p['n']}/")
            urls += [f"{b.SITE_URL}sprints/{s['n']}/" for s in p["sprints"]]
    if texts:
        urls.append(f"{b.SITE_URL}search/")
    body = "".join(f"  <url><loc>{e(u)}</loc></url>\n" for u in urls)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + "</urlset>")


# ---------------------------------------------------------------- images

SOCIAL_HTML = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:SG;src:url("file://{fonts}/SpaceGrotesk.ttf");font-weight:300 700}}
@font-face{{font-family:JBM;src:url("file://{fonts}/JetBrainsMono.ttf");font-weight:100 800}}
@font-face{{font-family:SS;src:url("file://{serif}");font-style:italic;font-weight:400 600}}
html,body{{margin:0;width:1200px;height:630px;overflow:hidden}}
.c{{box-sizing:border-box;width:1200px;height:630px;position:relative;color:#F4F8FC;
background:radial-gradient(520px 420px at 78% 0%,{glow} 0%,transparent 70%),
linear-gradient(rgba(147,166,196,.07) 1px,transparent 1px) 0 0/40px 40px,
linear-gradient(90deg,rgba(147,166,196,.07) 1px,transparent 1px) 0 0/40px 40px,#061127}}
.i{{position:absolute;left:56px;top:40px;width:440px;height:550px;border-radius:14px;overflow:hidden;
box-shadow:0 30px 60px -20px rgba(0,0,0,.8),0 0 0 1px rgba(147,166,196,.32);transform:rotate(-2deg)}}
.i img{{width:100%;height:100%;object-fit:cover;object-position:top}}
.t{{position:absolute;left:560px;right:56px;top:64px;bottom:56px;display:flex;flex-direction:column}}
.e{{font:600 19px/1.3 JBM;letter-spacing:.16em;text-transform:uppercase;color:{acc}}}
.h{{margin-top:22px;font:700 {size}px/1.06 SG;letter-spacing:-.02em}}
.h em{{font-style:normal;color:{acc}}}
.s{{margin-top:22px;font:italic 400 26px/1.32 SS;color:#C9D6EC}}
.b{{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;font:500 17px/1.3 JBM;letter-spacing:.12em;color:#93A6C4;text-transform:uppercase}}
.b strong{{color:#22E6D4;font-weight:600;white-space:nowrap}}
.b span:last-child{{text-transform:none;letter-spacing:.04em;text-align:right;max-width:330px}}
.bar{{position:absolute;left:0;right:0;bottom:0;height:8px;background:linear-gradient(90deg,{acc},#22E6D4)}}
</style></head><body><div class="c">
<div class="i"><img src="file://{image}"></div>
<div class="t"><div class="e">{eyebrow}</div><div class="h">{title}</div><div class="s">{tagline}</div>
<div class="b"><span><strong>Knowledge Sprint Series</strong><br>MT24 Learning</span><span>{right}</span></div></div>
<div class="bar"></div></div></body></html>"""


def social_cards(b, jobs):
    """jobs: (rel path, png source, eyebrow, title html, tagline, right text, accent). Rendered with Playwright."""
    todo = []
    for rel, src, eyebrow, title, tagline, right, acc in jobs:
        note = "social:" + hashlib.sha256("|".join([b.sha256(src), eyebrow, title, tagline, right, acc,
                                                    SOCIAL_HTML]).encode()).hexdigest()
        dst = os.path.join(b.ROOT, rel)
        if os.path.exists(dst) and b.jpeg_comment(dst) == note:
            continue
        todo.append((rel, src, eyebrow, title, tagline, right, acc, note))
    if not todo:
        return
    from playwright.sync_api import sync_playwright
    fonts = b.fetch_fonts()
    work = os.path.join(os.path.expanduser("~/.cache/knowledge-sprint-series"), "social")
    os.makedirs(work, exist_ok=True)
    serif = os.path.join(b.ROOT, "docs", "fonts", "source-serif-4-italic.woff2")
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
        for rel, src, eyebrow, title, tagline, right, acc, note in todo:
            plain_len = len(re.sub(r"<[^>]+>", "", title))
            size = 54 if plain_len <= 40 else 46 if plain_len <= 62 else 40
            html = os.path.join(work, "card.html")
            with open(html, "w", encoding="utf-8") as f:
                f.write(SOCIAL_HTML.format(fonts=fonts, serif=serif, image=src, eyebrow=e(eyebrow), title=title,
                                           tagline=e(tagline), right=e(right), acc=tint(acc, 6.5),
                                           glow=acc + "55", size=size))
            page.goto("file://" + html)
            page.wait_for_timeout(400)
            png = os.path.join(work, "card.png")
            page.screenshot(path=png)
            b.thumb(png, rel, size=(1200, 630), note=note)
        browser.close()


# ---------------------------------------------------------------- build

def write_html(b, rel, text):
    b.write(rel, text)


def run_pagefind(b):
    docs = os.path.join(b.ROOT, "docs")
    out = os.path.join(docs, "pagefind")
    if os.path.isdir(out):
        shutil.rmtree(out)
    try:
        import pagefind  # noqa: F401
    except ImportError:
        sys.exit(f"Pagefind is needed for the site search: pip install 'pagefind[bin]=={PAGEFIND}'")
    r = subprocess.run([sys.executable, "-m", "pagefind", "--site", docs, "--output-subdir", "pagefind",
                        "--include-characters", "±×÷√%", "--quiet"], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("Pagefind failed:\n" + r.stdout + r.stderr)


def build(b):
    texts = load_texts()
    flat = [(p, s) for p in b.PHASES for s in p["sprints"]]
    jobs = []
    for i, p in enumerate(b.PHASES):
        if p["n"] not in texts:
            continue
        t = texts[p["n"]]
        folder = os.path.join(b.ROOT, "phases", b.phase_dir(p))
        summary = os.path.join(folder, p["summary"])
        b.thumb(summary, f"docs/img/pages/phase-{p['n']}.jpg", size=(1080, 1350))
        write_html(b, f"docs/phases/{p['n']}/index.html", phase_page(b, texts, i, p))
        first = t.PHASE["accents"][p["sprints"][0]["n"]]
        jobs.append((f"docs/img/social/phase-{p['n']}.jpg", summary,
                     f"Phase {p['n']} · {b.sprint_label(p)} of {b.TOTAL_SPRINTS}", title_html(p["title"], t.SUMMARY.get("em")),
                     p["line"], f"DOI {p['v']}", first))
        for s in p["sprints"]:
            k = flat.index((p, s))
            prev_s = flat[k - 1] if k > 0 else None
            next_s = flat[k + 1] if k + 1 < len(flat) else None
            src = os.path.join(folder, s["file"])
            b.thumb(src, f"docs/img/pages/sprint-{s['n']}.jpg", size=(1080, 1350))
            b.thumb(src, f"docs/img/pages/sprint-{s['n']}-s.jpg", size=(400, 500))
            st = t.SPRINTS[s["n"]]
            write_html(b, f"docs/sprints/{s['n']}/index.html", sprint_page(b, texts, p, s, st, prev_s, next_s))
            jobs.append((f"docs/img/social/sprint-{s['n']}.jpg", src,
                         f"Sprint {s['n']}/{b.TOTAL_SPRINTS} · Phase {p['n']}", title_html(s["title"], st.get("em")),
                         s["tagline"], p["title"], t.PHASE["accents"][s["n"]]))
    social_cards(b, jobs)
    write_html(b, "docs/search/index.html", search_page(b))
    write_html(b, "docs/404.html", not_found_page(b))
    b.write("docs/sitemap.xml", sitemap(b, texts))
    run_pagefind(b)
    return texts
