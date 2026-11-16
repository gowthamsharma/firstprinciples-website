"""
Build the whole First Principles website from content/ into this folder (flat .html files).

    content/cfa/*.md      the CFA Program guide (levels, dates, fees, pass rates)
    content/blog/*.md     study-strategy posts
    content/prereq/*.md   the Level III prerequisite concepts (one page each)

Each .md file starts with a small header between --- lines (title, summary, ...), then Markdown.
In the text, [[figure]] places the page's diagram and [[widget:name]] a hands-on widget.
Run it: open this file in PyCharm and click Run (needs the 'markdown' package: pip install markdown).
"""
import datetime
import html
import json
import pathlib
import re

import markdown

import figures

ROOT = pathlib.Path(__file__).resolve().parent
SITE = "https://firstprinciples.courses"
TODAY = datetime.date.today().isoformat()
NAME, EMAIL = "Gowtham Kumar", "gkinba@gmail.com"
CHECKED = "16 November 2026"

DISCLAIMER = ("CFA Institute does not endorse, promote, or warrant the accuracy or quality of the products or services offered by "
              "First Principles. CFA® and Chartered Financial Analyst® are registered trademarks owned by CFA Institute.")


def obfuscate(s):
    return "".join(f"&#{ord(ch)};" for ch in s)


def load(folder):
    posts = []
    for f in sorted((ROOT / "content" / folder).glob("*.md")):
        text = f.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
        meta = {}
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()
        meta["body_md"] = m.group(2)
        meta["slug"] = meta.get("slug") or f.stem
        meta["order"] = float(meta.get("order", 0))
        posts.append(meta)
    return sorted(posts, key=lambda p: p["order"])


THUMB_FALLBACK = {"prereq-depreciation-methods": "dep_methods", "prereq-fifo-lifo-weighted-average": "inventory_cost",
                  "prereq-bonds-effective-interest": "bond_reason", "prereq-price-elasticity": "consumer_surplus",
                  "prereq-money-creation": "money_multiplier"}


def fig_key(p):
    if p.get("figure"):
        return p["figure"]
    m = re.search(r"\[\[fig:(\w+)", p["body_md"])
    return m.group(1) if m else THUMB_FALLBACK.get(p["slug"], "bond_reason")


def make_thumb(p):
    """A 16:9 picture for cards: the page's own diagram, labels removed, on the navy stage."""
    svg = getattr(figures, fig_key(p))()
    w, h = map(float, re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg).groups())
    inner = re.sub(r"<svg[^>]*>|</svg>", "", svg)
    if len(re.findall(r"<(?:path|rect|circle)", re.sub(r"<text[^>]*>.*?</text>", "", inner, flags=re.S))) > 2:
        inner = re.sub(r"<text[^>]*>.*?</text>", "", inner, flags=re.S)   # a picture: drop its labels
    inner = inner.replace('fill="#000"', 'fill="#0B1F38"').replace('stroke="#000"', 'stroke="#0B1F38"').replace('stroke="#3a3a3a"', 'stroke="#4A6E96"')
    inner = re.sub(r' class="[^"]*"| style="[^"]*"', "", inner)
    inner = re.sub(r'stroke-width="([\d.]+)"', lambda m: f'stroke-width="{float(m.group(1)) * 1.9:.1f}"', inner)
    inner = re.sub(r'<rect([^>]*?) fill="none" stroke="(#[0-9A-Fa-f]{6})"', r'<rect\1 fill="\2" fill-opacity=".22" stroke="\2"', inner)
    k = min(560 / w, 290 / h)
    tx, ty = (640 - w * k) / 2, (360 - h * k) / 2 + 6
    grid = "".join(f'<path d="M{x},0 V360" stroke="#ffffff" stroke-opacity=".04"/>' for x in range(40, 640, 40))
    grid += "".join(f'<path d="M0,{y} H640" stroke="#ffffff" stroke-opacity=".04"/>' for y in range(40, 360, 40))
    out = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="640" height="360">'
           f'<defs><radialGradient id="g" cx="70%" cy="20%" r="90%"><stop offset="0" stop-color="#1D4573"/><stop offset="1" stop-color="#0B1F38"/></radialGradient></defs>'
           f'<rect width="640" height="360" fill="url(#g)"/>{grid}<g transform="translate({tx:.1f},{ty:.1f}) scale({k:.4f})">{inner}</g></svg>')
    name = f"thumb-{p['slug']}.svg"
    (ROOT / name).write_text(out, encoding="utf-8")
    return name


def render_md(p):
    md = markdown.Markdown(extensions=["tables", "sane_lists", "attr_list"])
    body = md.convert(p["body_md"])
    body = body.replace("<table>", '<div class="tablewrap"><table>').replace("</table>", "</table></div>")

    def figure_html(key, cap):
        return f'<figure class="figure wide"><div class="stage">{getattr(figures, key)()}</div>' + (f"<figcaption>{cap}</figcaption>" if cap else "") + "</figure>"

    body = re.sub(r"<p>\[\[figure\]\]</p>", lambda _: figure_html(p["figure"], p.get("caption", "")) if p.get("figure") else "", body)
    body = re.sub(r"<p>\[\[fig:(\w+)(?:\|(.*?))?\]\]</p>", lambda m: figure_html(m.group(1), m.group(2)), body)
    body = re.sub(r"<p>\[\[widget:(\w+)\]\]</p>", lambda m: f'<div class="widget" data-widget="{m.group(1)}"></div>', body)
    return body


def words(p):
    return len(re.sub(r"<[^>]+>", " ", p["body_md"]).split())


def minutes(p):
    return max(2, round(words(p) / 200))


NAV = [("cfa-program.html", "CFA guide", ""), ("prerequisites.html", "Prerequisites", ""), ("blog.html", "Study blog", ""), ("index.html#about", "About", "soft")]


def page(path, title, desc, main, active="", extra_head="", image="intro-poster.jpg"):
    nav = "".join(f'<a href="{h}"' + (f' class="{c}"' if c else "") + (' aria-current="page"' if h == active else "") + f">{t}</a>" for h, t, c in NAV)
    canon = SITE + "/" + ("" if path == "index.html" else path)
    out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#112B4A">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:url" content="{canon}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE}/{image}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,500&amp;display=swap">
<link rel="stylesheet" href="style.css">
{extra_head}
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="index.html"><img src="favicon.svg" alt="" width="28" height="28"><span><b>First</b> Principles</span></a>
  <nav aria-label="Main">{nav}</nav>
  <a class="btn outline" href="prerequisites.html">Start learning</a>
</div></header>
{main}
<footer><div class="wrap">
  <div><p class="fb"><b>First</b> Principles</p>
  <p>CFA Program lessons, built from the basics. Video course opening in 2027.</p>
  <nav><a href="cfa-program.html">CFA guide</a><a href="prerequisites.html">Prerequisites</a><a href="blog.html">Study blog</a><a href="index.html#about">About</a></nav></div>
  <div><p>{DISCLAIMER}</p>
  <p>Exam facts on this site were checked against CFA Institute's published pages on {CHECKED}. Dates, fees and policies change: always confirm on cfainstitute.org before you register. Explanations are original and are not taken from the CFA Program curriculum.</p>
  <p>© 2026 {NAME}. Set in Figtree (SIL Open Font License).</p></div>
</div></footer>
<script src="site.js" defer></script>
</body>
</html>
"""
    (ROOT / path).write_text(out, encoding="utf-8")
    return path


def jsonld(p, url):
    data = {"@context": "https://schema.org", "@type": "Article", "headline": p["title"], "description": p.get("summary", ""),
            "image": f"{SITE}/thumb-{p['slug']}.svg",
            "author": {"@type": "Person", "name": NAME}, "datePublished": "2026-11-16", "dateModified": TODAY,
            "mainEntityOfPage": url, "publisher": {"@type": "Organization", "name": "First Principles"}}
    return f'<script type="application/ld+json">{json.dumps(data)}</script>'


def card(p, chip, foot, feat=False):
    return (f'<a class="card{" feat" if feat else ""}" href="{p["slug"]}.html">'
            f'<span class="thumb"><img src="thumb-{p["slug"]}.svg" alt="" loading="lazy" width="640" height="360"><span class="chip">{chip}</span></span>'
            f'<span class="cb"><span class="cm">{minutes(p)} min read</span><h4>{p["title"]}</h4><p>{p.get("summary", "")}</p><span class="cf">{foot}</span></span></a>')


def article(p, crumbs, eyebrow, pager="", keep=""):
    url = f"{SITE}/{p['slug']}.html"
    main = f"""<main>
<section class="pagehead"><div class="wrap">
  <div>
    <p class="crumbs">{crumbs}</p>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{p['title']}</h1>
    <p class="lead">{p.get('summary', '')}</p>
    <p class="meta">{minutes(p)} min read &nbsp;/&nbsp; By {NAME}</p>
  </div>
  <img class="art" src="thumb-{p['slug']}.svg" alt="" width="640" height="360">
</div></section>
<div class="wrap"><article class="post"><div class="body">{render_md(p)}</div>{pager}</article></div>
{keep}
</main>"""
    return page(p["slug"] + ".html", f"{p['title']} | First Principles", p.get("summary", ""), main, extra_head=jsonld(p, url),
                image=f"thumb-{p['slug']}.svg")


def keep_reading(items, chip, foot):
    return f'<section class="keep"><div class="wrap"><span class="eyebrow">Keep reading</span><div class="grid">{"".join(card(q, chip(q), foot(q)) for q in items)}</div></div></section>'


def nxt(lst, i, n=3):
    return [lst[(i + k) % len(lst)] for k in range(1, n + 1)]


def build():
    built = ["index.html"]
    cfa, blog, pre = load("cfa"), load("blog"), load("prereq")
    for i, p in enumerate(pre):
        p["n"] = i + 1
    for p in cfa + blog + pre:
        make_thumb(p)

    for i, p in enumerate(cfa):
        built.append(article(p, '<a href="index.html">Home</a> › <a href="cfa-program.html">CFA guide</a>', "CFA Program guide",
                             keep=keep_reading(nxt(cfa, i), lambda q: "CFA guide", lambda q: "CFA Program guide")))
    for i, p in enumerate(blog):
        built.append(article(p, '<a href="index.html">Home</a> › <a href="blog.html">Study blog</a>', "Study blog",
                             keep=keep_reading(nxt(blog, i), lambda q: "Study blog", lambda q: "Study strategy")))
    for i, p in enumerate(pre):
        prev_p, next_p = (pre[i - 1] if i else None), (pre[i + 1] if i + 1 < len(pre) else None)
        pager = '<nav class="pager">'
        pager += (f'<a href="{prev_p["slug"]}.html"><span>Previous concept</span>{prev_p["title"]}</a>' if prev_p else "")
        pager += (f'<a class="next" href="{next_p["slug"]}.html"><span>Next concept</span>{next_p["title"]}</a>' if next_p else "")
        pager += "</nav>"
        crumbs = f'<a href="index.html">Home</a> › <a href="prerequisites.html">Prerequisites</a> › {p["topic"]}'
        built.append(article(p, crumbs, f'Concept {p["n"]} of {len(pre)} &nbsp;/&nbsp; {p["topic"]}', pager,
                             keep=keep_reading(nxt(pre, i), lambda q: f'Concept {q["n"]:02d}', lambda q: q["topic"])))

    # ---- prerequisites index
    groups = ""
    for topic in ["Financial Statement Analysis", "Economics"]:
        groups += f'<section class="group"><h2>{topic}</h2>'
        mods = []
        for p in pre:
            if p["topic"] == topic and p["module"] not in mods:
                mods.append(p["module"])
        for mod in mods:
            items = [p for p in pre if p["topic"] == topic and p["module"] == mod]
            groups += f'<p class="mod">{mod}</p><div class="grid">' + "".join(card(p, f'Concept {p["n"]:02d}', mod) for p in items) + "</div>"
        groups += "</section>"
    main = f"""<main>
<section class="pagehead"><div class="wrap solo"><div>
  <p class="crumbs"><a href="index.html">Home</a> › Prerequisites</p>
  <span class="eyebrow">{len(pre)} concepts, free</span>
  <h1>Prerequisites, from first principles</h1>
  <p class="lead">CFA Institute asks Level III candidates to be fluent in two foundation areas: financial statement analysis and economics. These are the ideas from them that come up again and again, one short page each: what the idea is, why it has to be true, a diagram, one worked example and the traps examiners like.</p>
  <p class="meta">Written from scratch &nbsp;/&nbsp; Use alongside the official readings</p>
</div></div></section>
<div class="wrap" style="padding-bottom:4rem">{groups}</div>
</main>"""
    built.append(page("prerequisites.html", "Level III prerequisites: financial statements and economics, explained | First Principles",
                      f"{len(pre)} core concepts from the CFA Level III prerequisite readings in financial statement analysis and economics, each explained from first principles with a diagram and a worked example.",
                      main, active="prerequisites.html"))

    # ---- blog index
    main = f"""<main>
<section class="pagehead"><div class="wrap solo"><div>
  <p class="crumbs"><a href="index.html">Home</a> › Study blog</p>
  <span class="eyebrow">Study blog</span>
  <h1>How to tackle every level of the CFA Program</h1>
  <p class="lead">Study plans, Level II vignettes, Level III written answers, ethics, mock exams and exam day. The advice draws on CFA Institute's own guidance and on what the main prep providers recommend, rewritten as one consistent method.</p>
</div></div></section>
<div class="wrap" style="padding-bottom:4rem">
<section class="group"><h2>How to tackle the exams</h2><div class="grid" style="margin-top:1.4rem">{''.join(card(p, "Study blog", "Study strategy") for p in blog)}</div></section>
<section class="group"><h2>The CFA Program, in facts</h2><div class="grid" style="margin-top:1.4rem">{''.join(card(p, "CFA guide", "CFA Program guide") for p in cfa)}</div></section>
<section class="group"><h2>Prerequisite concepts</h2><p style="margin-top:1rem"><a class="more" href="prerequisites.html">All {len(pre)} financial statement analysis and economics concepts</a></p></section>
</div>
</main>"""
    built.append(page("blog.html", "CFA study blog: strategies for Levels I, II and III | First Principles",
                      "Practical strategies for the CFA exams: study plans, Level II item sets, Level III constructed response, ethics, mock exams and exam day.",
                      main, active="blog.html"))

    home(cfa, blog, pre)

    page("404.html", "Page not found | First Principles", "This page does not exist.",
         '<main><section class="pagehead"><div class="wrap solo"><div><span class="eyebrow">404</span><h1>That page is not here</h1><p class="lead">Try the <a style="color:#3DBEF0" href="index.html">home page</a>, the <a style="color:#3DBEF0" href="prerequisites.html">prerequisite concepts</a> or the <a style="color:#3DBEF0" href="blog.html">study blog</a>.</p></div></div></section></main>')

    urls = "".join(f"  <url><loc>{SITE}/{'' if b == 'index.html' else b}</loc><lastmod>{TODAY}</lastmod></url>\n" for b in sorted(set(built)))
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n', encoding="utf-8")
    print(f"built {len(set(built))} pages + 404 + sitemap + {len(cfa + blog + pre)} thumbnails")


def home(cfa, blog, pre):
    pick = {p["slug"]: p for p in blog + cfa + pre}
    email = obfuscate(EMAIL)

    def pane(i, eyebrow, big, slug, label):
        p = pick[slug]
        return (f'<div class="pane" id="pane{i}" role="tabpanel" aria-labelledby="tab{i}"{"" if i == 0 else " hidden"}>'
                f'<div class="art"><img src="thumb-{slug}.svg" alt=""><span class="eyebrow">{eyebrow}</span><p class="big">{big}</p></div>'
                f'<div class="side"><h3>{p["title"]}</h3><p>{p["summary"]}</p><a class="btn" href="{slug}.html">{label}</a></div></div>')

    tabs = [("Prerequisites", "50 concepts, free", "Financial statements and economics, rebuilt from the basics.", "prereq-three-statements", "Start reading"),
            ("Study blog", "Strategy", "A plan for every level, from first reading to exam day.", "blog-study-plan", "Read the plan"),
            ("CFA guide", "2027 facts", "Exam windows, fees and pass rates in one place.", "cfa-dates-fees", "See dates and fees")]
    tab_btns = "".join(f'<button type="button" role="tab" id="tab{i}" aria-controls="pane{i}" aria-selected="{"true" if i == 0 else "false"}">{t[0]}</button>' for i, t in enumerate(tabs))
    panes = "".join(pane(i, *t[1:]) for i, t in enumerate(tabs))

    def row(title, href, items, chip, foot):
        cards = "".join(card(p, chip(p), foot(p), feat=(k == 0)) for k, p in enumerate(items))
        return f'<div class="rowhead"><h3><a href="{href}">{title}</a></h3></div><div class="row">{cards}</div>'

    blog_row = row("Study blog", "blog.html", [pick[s] for s in ["blog-first-principles-method", "blog-study-plan", "blog-level-3-constructed-response", "blog-mock-exams"]],
                   lambda p: "Study blog", lambda p: "Study strategy")
    pre_row = row("Prerequisite concepts", "prerequisites.html", [pick[s] for s in ["prereq-deferred-tax", "prereq-three-statements", "prereq-price-elasticity", "prereq-lifo-reserve"]],
                  lambda p: f'Concept {p["n"]:02d}', lambda p: p["topic"])
    cfa_row = row("CFA Program guide", "cfa-program.html", [pick[s] for s in ["cfa-pass-rates", "cfa-level-1", "cfa-level-2", "cfa-level-3"]],
                  lambda p: "CFA guide", lambda p: "CFA Program guide")

    def tile(cls, chip, name, text, rows, rate, href):
        dl = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in rows)
        return (f'<div class="tile {cls}"><div class="chips"><span class="chip">{chip}</span><span class="chip fill">2027</span></div>'
                f'<h3>{name}</h3><p>{text}</p><dl><dt>Latest pass rate</dt><dd class="big">{rate}</dd>{dl}</dl><a class="more" href="{href}">In detail</a></div>')

    main = f"""<main>
<section class="hero" aria-label="Introduction">
  <video autoplay muted loop playsinline preload="metadata" poster="hero-poster.jpg" aria-hidden="true"><source src="hero.mp4" type="video/mp4"></video>
  <div class="wrap">
    <span class="eyebrow">A CFA course, opening in 2027</span>
    <h1>Where formulas become intuition.</h1>
    <p class="lead">Short animated lessons that rebuild every CFA idea from what has to be true, so you understand it once instead of memorising it three times.</p>
    <div class="actions"><a class="btn" href="prerequisites.html">Start with {len(pre)} free concepts</a><a class="btn line" href="cfa-program.html">Read the CFA guide</a></div>
  </div>
</section>

<section class="feature"><div class="wrap">
  <div class="tabs" role="tablist" aria-label="Featured">{tab_btns}</div>
  <div class="panes">{panes}</div>
</div></section>

<section class="section"><div class="wrap">
  <span class="eyebrow">The method</span>
  <h2>What is a first-principles approach?</h2>
  <p class="sub">Most exam prep hands you conclusions to memorise. A first-principles approach goes the other way: it starts from a few facts that cannot be otherwise and reasons forward until the conclusion is unavoidable. You remember it because you can rebuild it.</p>
  <div class="steps">
    <div><span class="n">1</span><h3>Start from what must be true</h3><p>Strip the topic to its bedrock: money today is worth more than money later; a balance sheet always balances; buyers buy less when prices rise.</p></div>
    <div><span class="n">2</span><h3>Build one step at a time</h3><p>Add one idea at a time, with a picture at every step, and check that each step follows from the last. Nothing is introduced just because the syllabus says so.</p></div>
    <div><span class="n">3</span><h3>Name the formula last</h3><p>When the formula appears, it only writes down what you can already see. Then you test yourself by predicting the answer before working it out.</p></div>
  </div>
  <div class="example">
    <div>
      <h3>An example: why bond prices fall when rates rise</h3>
      <p class="bad">Memorise: "price and yield are inversely related."</p>
      <p>Reason: a bond is a fixed set of future payments. Its price today is what those payments are worth today. A higher interest rate means each future payment is worth less today, so the total, the price, must fall. And the further away a payment is, the more it shrinks. That last sentence is all <em>duration</em> really is.</p>
    </div>
    <figure class="figure" style="margin:0"><div class="stage">{figures.bond_reason()}</div></figure>
  </div>
</div></section>

<section class="section dark"><div class="wrap">
  <span class="eyebrow">The CFA Program</span>
  <h2>Three exams, each built on the one before.</h2>
  <p class="sub">The facts below are CFA Institute's, checked {CHECKED}.</p>
  <div class="tiles">
    {tile("l1", "LEVEL I", "The tools", "Breadth across ten topics, from ethics and quantitative methods to derivatives and portfolio management.", [("Format", "180 multiple choice"), ("Time", "2 × 2 h 15 min"), ("Windows", "Feb, May, Aug, Nov")], "43%", "cfa-level-1.html")}
    {tile("l2", "LEVEL II", "Valuation", "Applying the tools: what an asset is worth and which assumptions drive the answer, through short case studies.", [("Format", "22 item sets, 88 Qs"), ("Time", "4 h 24 min"), ("Windows", "May, Aug, Nov")], "45%", "cfa-level-2.html")}
    {tile("l3", "LEVEL III", "Portfolio management", "Synthesis for a real client: allocation, construction, risk and ethics, plus one specialised pathway.", [("Format", "11 item + 11 written sets"), ("Time", "4 h 24 min"), ("Windows", "Feb, Aug")], "47%", "cfa-level-3.html")}
  </div>
  <div class="panel">
    <div><h3>Pass rates, session by session</h3><p>Fewer than half of candidates pass any level in a typical session. The chart shows the most recent results; the guide has every session and the five-year averages.</p><a class="more" href="cfa-pass-rates.html">All pass rates</a></div>
    <figure class="figure" style="margin:0">{figures.pass_rates()}</figure>
  </div>
</div></section>

<section class="section mist"><div class="wrap">
  <span class="eyebrow">Free to read now</span>
  <h2>Good preparation starts with understanding.</h2>
  <p class="sub">While the video course is in production, the written material is open: guides, strategy and {len(pre)} prerequisite concepts, each with its own animated diagram.</p>
  {pre_row}
  {blog_row}
  {cfa_row}
</div></section>

<section class="section dark"><div class="wrap">
  <span class="eyebrow">The course</span>
  <h2>What every lesson gives you</h2>
  <div class="parts">
    <div><h3>The idea, drawn</h3><p>Animated diagrams and realistic market data, one idea on screen at a time.</p></div>
    <div><h3>The intuition behind it</h3><p>Why a result has to be true, told with an everyday analogy before any algebra.</p></div>
    <div><h3>Pause and predict</h3><p>Short questions inside the lesson, so you commit to an answer before you see it.</p></div>
    <div><h3>Exam questions, solved</h3><p>Vignette questions answered the way the exam asks them, including why each wrong option is wrong.</p></div>
  </div>
</div></section>

<section class="section" id="about"><div class="wrap">
  <span class="eyebrow">About</span>
  <h2>Who builds First Principles</h2>
  <div class="me"><div class="mono" aria-hidden="true">G</div>
    <div><p class="name">{NAME}</p><p><a href="mailto:{email}">{email}</a></p></div></div>
  <p class="sub" style="margin-top:1.4rem">I build First Principles: the lessons, the animations and this site. Questions, corrections and ideas for topics are welcome by email.</p>
</div></section>

<section class="section dark open"><div class="wrap">
  <span class="eyebrow">A CFA course, opening in</span>
  <h2 class="year">202<span>7</span></h2>
  <p>Short video lessons, intuition first, with exam-style questions solved step by step.</p>
</div></section>
</main>"""
    page("index.html", "First Principles · CFA Program lessons from the basics",
         "CFA Program lessons built from first principles: free guides to Levels I, II and III, exam dates, fees and pass rates, study strategy, and 50 prerequisite concepts explained. Video course opening in 2027.",
         main, active="index.html", image="hero-poster.jpg")


if __name__ == "__main__":
    build()
