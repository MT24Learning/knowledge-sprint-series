"""Builds docs/index.html, the series website, from the same data as the README.

Called by tools/build.py. Only docs/index.html and docs/img/thumbs/ are generated; docs/style.css,
docs/site.js, docs/fonts/ and docs/img/brand/ are static design files, edited by hand.
"""
import json
import re
import os
import shutil
from html import escape

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def e(text):
    return escape(str(text), quote=True)


def quotes(text):
    """Typographic quotes for display: "word" becomes “word”."""
    return re.sub(r'"([^"]+)"', "\u201c\\1\u201d", text)


def short_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{d} {MONTHS[m - 1]} {y}"


def render(b):
    """b is the build module: data, constants and helpers."""
    phases, milestones, nxt = b.PHASES, b.MILESTONES, b.NEXT
    archived = len(phases)
    done = sum(len(p["sprints"]) for p in phases)
    pct = round(100 * done / b.TOTAL_SPRINTS)
    latest = phases[-1]

    def page_url(p):
        return f"{b.REPO_URL}/blob/main/phases/{b.phase_dir(p)}/README.md"

    def thumb(p):
        return f"img/thumbs/phase-{p['n']:02d}.jpg"

    def doi(p):
        return f"https://doi.org/{p['v']}"

    out = []
    w = out.append

    # ------------------------------------------------------------ head
    description = (f"A free, open learning path of {b.TOTAL_SPRINTS} sprints in {b.TOTAL_PHASES} phases, from "
                   "engineering practice to the philosophy of science, statistics and machine learning. "
                   "Every completed phase is archived on Zenodo with a citable DOI.")
    data = {
        "@context": "https://schema.org",
        "@type": "CreativeWorkSeries",
        "name": "MT24 Learning — Knowledge Sprint Series",
        "url": b.SITE_URL,
        "description": description,
        "inLanguage": "en",
        "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
        "isAccessibleForFree": True,
        "author": {"@type": "Person", "name": "Mohammed Tahri", "alternateName": "MT24",
                   "sameAs": [f"https://orcid.org/{b.ORCID}"]},
        "hasPart": [{"@type": "CreativeWork", "name": f"Phase {p['n']}: {p['title']}",
                     "url": doi(p), "datePublished": p["first"]} for p in phases],
    }
    w("<!doctype html>")
    w('<html lang="en">')
    w("<head>")
    w('<meta charset="utf-8">')
    w('<meta name="viewport" content="width=device-width, initial-scale=1">')
    w("<title>Knowledge Sprint Series · MT24 Learning</title>")
    w(f'<meta name="description" content="{e(description)}">')
    w(f'<link rel="canonical" href="{b.SITE_URL}">')
    w('<meta name="theme-color" content="#061127">')
    w('<meta name="color-scheme" content="dark">')
    w('<meta property="og:type" content="website">')
    w('<meta property="og:title" content="Knowledge Sprint Series · MT24 Learning">')
    w(f'<meta property="og:description" content="{e(description)}">')
    w(f'<meta property="og:url" content="{b.SITE_URL}">')
    w(f'<meta property="og:image" content="{b.SITE_URL}img/brand/social.png">')
    w('<meta property="og:image:width" content="1280">')
    w('<meta property="og:image:height" content="640">')
    w('<meta name="twitter:card" content="summary_large_image">')
    w('<link rel="icon" href="img/brand/favicon.svg" type="image/svg+xml">')
    w('<link rel="apple-touch-icon" href="img/brand/apple-touch-icon.png">')
    w('<link rel="preload" href="fonts/space-grotesk.woff2" as="font" type="font/woff2" crossorigin>')
    w('<link rel="stylesheet" href="style.css">')
    for name, url in b.SOCIAL:
        if name == "Mastodon":
            w(f'<link rel="me" href="{url}">')
    w('<script>document.documentElement.classList.add("js")</script>')
    w('<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>")
    w("</head>")
    w("<body>")
    w('<a class="skip" href="#phases">Skip to the phases</a>')

    # ------------------------------------------------------------ header
    w('<header class="site">')
    w('  <div class="bar wrap">')
    w('    <a class="brand" href="./" aria-label="Knowledge Sprint Series, home">')
    w('      <img src="img/brand/mt24-badge.svg" width="40" height="40" alt="">')
    w('      <span><b>Knowledge Sprint Series</b><small>MT24 Learning</small></span>')
    w("    </a>")
    w('    <nav aria-label="Sections">')
    for href, label in [("#phases", "Phases"), ("#results", "Results"), ("#sprint", "How it works"),
                        ("#cite", "Cite"), ("#follow", "Follow")]:
        w(f'      <a href="{href}">{label}</a>')
    w(f'      <a class="gh" href="{b.REPO_URL}">GitHub</a>')
    w("    </nav>")
    w("  </div>")
    w("</header>")
    w("<main>")

    # ------------------------------------------------------------ hero
    w('<section class="hero">')
    w('  <div class="wrap hero-grid">')
    w('    <div class="hero-text">')
    w(f'      <p class="label">{b.TOTAL_SPRINTS} sprints · {b.TOTAL_PHASES} phases · free and open</p>')
    w("      <h1>A free learning path where <em>every claim can be checked</em>.</h1>")
    w('      <p class="lede">From engineering practice to the philosophy of science, statistics and machine '
      "learning. Each sprint is one portrait page: the core concepts, a figure, commands to try, a mini project "
      "and the trusted sources behind every claim. Each phase closes with a one-page summary and one checked "
      "result.</p>")
    w('      <div class="actions">')
    w(f'        <a class="btn primary" href="{page_url(phases[0])}">Start with Phase 1</a>')
    w('        <a class="btn ghost" href="#phases">Browse the phases</a>')
    w("      </div>")
    w("    </div>")
    w('    <div class="fan" aria-label="The three latest phase summaries">')
    for k, p in enumerate(phases[-3:]):
        w(f'      <a class="fan-{k}" href="{page_url(p)}"><img src="{thumb(p)}" width="520" height="650" '
          f'alt="Phase {p["n"]} summary: {e(p["title"])}"></a>')
    w("    </div>")
    w("  </div>")
    w('  <div class="wrap">')
    w('    <div class="progress">')
    stats = [(f"{archived}", f"of {b.TOTAL_PHASES} phases archived", round(100 * archived / b.TOTAL_PHASES)),
             (f"{done}", f"of {b.TOTAL_SPRINTS} sprints published", pct),
             (f"{pct}%", "of the path", pct)]
    for big, small, value in stats:
        w(f'      <div class="stat"><b>{big}</b><span>{small}</span>'
          f'<i class="meter" style="--v:{value}%"></i></div>')
    if nxt:
        state = "being published now" if nxt["status"] == "publishing" else "coming next"
        w(f'      <p class="next-note"><span class="dot"></span>Phase {nxt["n"]}, <b>{e(nxt["title"])}</b> '
          f'(Sprints {nxt["sprints"]}), {state}.</p>')
    w("    </div>")
    w("  </div>")
    w("</section>")

    # ------------------------------------------------------------ values
    w('<div class="values" role="list">')
    w('  <div class="wrap values-row">')
    for strong, rest in [("Free", "no paywall, no sign-up"), ("Sources", "on every sprint"),
                         ("Archived", "on Zenodo with a DOI"), ("CC BY-NC-SA 4.0", "share and adapt")]:
        w(f'    <span role="listitem"><b>{strong}</b> {rest}</span>')
    w("  </div>")
    w("</div>")

    # ------------------------------------------------------------ phases
    w('<section id="phases" class="block">')
    w('  <div class="wrap">')
    w('    <p class="label">The path so far</p>')
    w(f"    <h2>{archived} phases, {done} sprints</h2>")
    w('    <p class="sub">Each phase opens on GitHub with every sprint image, and links to its permanent, '
      "citable edition on Zenodo.</p>")
    w('    <div class="grid">')
    for p in phases:
        w('      <article class="card reveal">')
        w(f'        <a class="cover" href="{page_url(p)}" tabindex="-1" aria-hidden="true">'
          f'<img src="{thumb(p)}" width="520" height="650" loading="lazy" alt=""></a>')
        w('        <div class="card-body">')
        w(f'          <p class="meta"><span>Phase {p["n"]:02d}</span><span>{b.sprint_label(p)}</span></p>')
        w(f'          <h3><a href="{page_url(p)}">{e(p["title"])}</a></h3>')
        w(f'          <p class="line">{e(quotes(p["line"]))}</p>')
        w(f'          <p class="foot"><a class="doi" href="{doi(p)}">DOI {e(p["v"])}</a>'
          f'<time datetime="{p["first"]}">{short_date(p["first"])}</time></p>')
        w("        </div>")
        w("      </article>")
        for m in milestones:
            if m["after"] == p["n"]:
                link = f"{b.REPO_URL}/blob/main/milestones/README.md"
                w('      <article class="card milestone reveal">')
                w(f'        <a class="cover" href="{link}" tabindex="-1" aria-hidden="true">'
                  f'<img src="img/thumbs/milestone-{m["id"]}.jpg" width="520" height="650" loading="lazy" alt=""></a>')
                w('        <div class="card-body">')
                w(f'          <p class="meta"><span>Milestone</span><span>{e(m["scope"].split(" · ")[0])}</span></p>')
                w(f'          <h3><a href="{link}">{e(m["title"])}</a></h3>')
                w(f'          <p class="line">{e(m["line"])}</p>')
                w("        </div>")
                w("      </article>")
    if nxt:
        state = "Being published now" if nxt["status"] == "publishing" else "Coming next"
        w('      <article class="card next reveal">')
        w('        <div class="cover"><img src="img/thumbs/next-phase.jpg" width="520" height="650" loading="lazy" '
          f'alt="Phase {nxt["n"]}, {state.lower()}"></div>')
        w('        <div class="card-body">')
        w(f'          <p class="meta"><span>Phase {nxt["n"]:02d}</span><span>Sprints {nxt["sprints"]}</span></p>')
        w(f'          <h3>{e(nxt["title"])}</h3>')
        w(f'          <p class="line"><span class="dot"></span>{state}. A phase joins the index once all its images '
          "are public and its edition is archived.</p>")
        w("        </div>")
        w("      </article>")
    w("    </div>")
    w("  </div>")
    w("</section>")

    # ------------------------------------------------------------ results
    w('<section id="results" class="block alt">')
    w('  <div class="wrap">')
    w('    <p class="label">One result per phase</p>')
    w("    <h2>Every phase leads with one checked result</h2>")
    w('    <p class="sub">Each phase summary opens with one result, checked in code or against the sources. '
      "Here they are, in order.</p>")
    w('    <figure class="feature reveal">')
    w(f'      <blockquote>{e(quotes(latest["result"]))}</blockquote>')
    w(f'      <figcaption>Phase {latest["n"]} · <a href="{page_url(latest)}">{e(latest["title"])}</a></figcaption>')
    w("    </figure>")
    w('    <ol class="results">')
    for p in phases:
        w(f'      <li class="reveal"><span class="n">{p["n"]:02d}</span>'
          f'<div><a href="{page_url(p)}">{e(p["title"])}</a><p>{e(quotes(p["result"]))}</p></div></li>')
    w("    </ol>")
    w("  </div>")
    w("</section>")

    # ------------------------------------------------------------ how a sprint works
    parts = [
        ("Core concepts", "The idea of the sprint in short cards, written so each one can be checked against its sources."),
        ("A figure", "The main idea drawn, with real numbers where there are any (from Phase 2 onward)."),
        ("Try it", "Commands or a short program you can run yourself, shown with its real output. "
                   "Each phase page links the same code as files, with the versions that reproduce it."),
        ("A mini project", "One small piece of work to apply the sprint on your own."),
        ("Trusted sources", "Books, papers and official documentation, so every claim can be checked against its origin."),
    ]
    w('<section id="sprint" class="block">')
    w('  <div class="wrap">')
    w('    <p class="label">How a sprint works</p>')
    w("    <h2>One idea, one page, five parts</h2>")
    w('    <p class="sub">Every sprint image follows the same idea, even as the visual style changes from phase '
      "to phase. Each phase then ends with a one-page summary: what each sprint taught, what I can now do, "
      "mistakes avoided, and one phase project that ties the sprints together.</p>")
    w('    <ol class="parts">')
    for k, (title, text) in enumerate(parts, 1):
        w(f'      <li class="reveal"><span class="n">{k:02d}</span><h3>{title}</h3><p>{text}</p></li>')
    w("    </ol>")
    w("  </div>")
    w("</section>")

    # ------------------------------------------------------------ cite
    w('<section id="cite" class="block alt">')
    w('  <div class="wrap cite-grid">')
    w("    <div>")
    w('      <p class="label">Cite</p>')
    w("      <h2>Cite the edition you used</h2>")
    w('      <p class="sub">Each phase has its own DOI on Zenodo, and its page on GitHub gives the full reference. '
      "For the latest phase:</p>")
    w("    </div>")
    w('    <div class="cite-box reveal">')
    w(f'      <pre id="citation">{e(b.citation(latest))}</pre>')
    w('      <button class="copy" type="button" data-copy="citation">Copy</button>')
    w("    </div>")
    w('    <p class="cite-links">')
    w(f'      <a href="{b.ZENODO}">All editions on Zenodo</a>')
    w(f'      <a href="{b.REPO_URL}">Cite this repository on GitHub</a>')
    w(f'      <a href="https://orcid.org/{b.ORCID}">ORCID {b.ORCID}</a>')
    w("    </p>")
    w("  </div>")
    w("</section>")

    # ------------------------------------------------------------ follow
    w('<section id="follow" class="block">')
    w('  <div class="wrap follow">')
    w('    <p class="label">Follow</p>')
    w("    <h2>Follow the series</h2>")
    w('    <p class="sub">New sprints are posted first on social media; once their phase is complete, it is '
      "archived on Zenodo and listed here.</p>")
    w('    <p class="pills">')
    for name, url in b.SOCIAL:
        w(f'      <a rel="me" href="{url}">{name}</a>')
    w(f'      <a href="{b.REPO_URL}">GitHub</a>')
    w("    </p>")
    w("  </div>")
    w("</section>")
    w("</main>")

    # ------------------------------------------------------------ footer
    w('<footer class="site">')
    w('  <div class="wrap foot-row">')
    w("    <p>© 2026 Mohammed Tahri (MT24) · Images and text under "
      '<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a></p>')
    w('    <p><a href="https://github.com/MT24Learning">MT24 Learning</a> · '
      f'<a href="{b.REPO_URL}">Source and data</a> · <a href="fonts/OFL.txt">Font licences</a></p>')
    w("  </div>")
    w("</footer>")
    w('<script src="site.js" defer></script>')
    w("</body>")
    w("</html>")
    return "\n".join(out)


def copy_if_changed(src, dst):
    if os.path.exists(dst):
        with open(src, "rb") as a, open(dst, "rb") as c:
            if a.read() == c.read():
                return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)


def build(b):
    thumbs = os.path.join(b.ROOT, "assets", "thumbs")
    target = os.path.join(b.ROOT, "docs", "img", "thumbs")
    wanted = {f"phase-{p['n']:02d}.jpg" for p in b.PHASES}
    wanted |= {f"milestone-{m['id']}.jpg" for m in b.MILESTONES}
    if b.NEXT:
        wanted.add("next-phase.jpg")
    for name in sorted(wanted):
        copy_if_changed(os.path.join(thumbs, name), os.path.join(target, name))
    b.write("docs/index.html", render(b))
