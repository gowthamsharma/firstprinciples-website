"""
Build the whole First Principles website from content/ into this folder (flat .html files).

    content/cfa/*.md      the CFA Program guide (levels, dates, fees, pass rates)
    content/blog/*.md     study-strategy posts
    content/prereq/*.md   the foundation concepts for all three levels (one page each)

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
import calcviz

ROOT = pathlib.Path(__file__).resolve().parent
SITE = "https://firstprinciples.courses"
TODAY = datetime.date.today().isoformat()
NAME, EMAIL = "Gowtham Kumar", "gkinba@gmail.com"
CLARITY_ID = "zf2slpx8uv"  # Microsoft Clarity project ID; loads only after the visitor accepts the banner
CF_BEACON = "a9877ea4bed648d990739f9b34199681"  # Cloudflare Web Analytics token (cookieless); empty = no tracking
CHECKED = "16 November 2026"
UPDATED = datetime.date.today().strftime("%d %b %Y").upper()

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


def _formula_html(f):
    # {numerator}/{denominator} becomes a stacked fraction
    f = re.sub(r"\{([^{}]+)\}/\{([^{}]+)\}", r'<span class="fr"><span>\1</span><span>\2</span></span>', f)
    return f


def try_box(title, keys, *rest):
    note, extra = "", {}
    for r in rest:
        if re.match(r"^[fvm]=", r):
            extra[r[0]] = r[2:].strip()
        elif r:
            note = r
    note = f'<p class="try-out">{markdown.markdown(note)[3:-4]}</p>' if note else ""
    setup = ""
    if extra.get("f"):
        lines = "".join(f'<div class="fm-l">{_formula_html(x.strip())}</div>' for x in extra["f"].split(";;"))
        setup += f'<div class="try-f"><p class="try-lbl">The formula</p><div class="fm">{lines}</div></div>'
    if extra.get("v"):
        setup += f'<div class="try-v"><p class="try-lbl">The picture</p><div class="stage">{calcviz.visual(extra["v"])}</div></div>'
    mem = ""
    if extra.get("m"):
        cells = "".join(f'<span class="mc"><b>{html.escape(x.split(":", 1)[0].strip())}</b>{html.escape(x.split(":", 1)[1].strip())}</span>' for x in extra["m"].split(";;"))
        mem = f'<div class="try-mem"><p class="try-lbl">What each memory holds</p><div class="mcs">{cells}</div></div>'
    keys_lbl = '<p class="try-lbl">The keys</p>' if setup else ""
    return (f'<div class="try{" rich" if setup else ""}" data-keys="{html.escape(keys, quote=True)}"><div class="try-head"><b>{html.escape(title)}</b>'
            f'<button type="button" class="try-play">Play on the calculator</button></div>{setup}{keys_lbl}<div class="chips" aria-label="Keys: {html.escape(keys)}"></div>{mem}{note}</div>')


def render_md(p):
    md = markdown.Markdown(extensions=["tables", "sane_lists", "attr_list"])
    boxes = []

    def hold(m):
        parts = m.group(1).split("|")
        boxes.append(try_box(*[x.strip() for x in parts]))
        return f"\n\nTRYBOX{len(boxes) - 1}X\n\n"
    src = re.sub(r"\[\[try:(.+?)\]\]", hold, p["body_md"])
    body = md.convert(src)
    body = re.sub(r"<p>TRYBOX(\d+)X</p>", lambda m: boxes[int(m.group(1))], body)
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


# ---- header menu: (label, hub page, columns); each column is (heading, [(text, href, note)])
MENU = [
    ("Most searched", "most-searched.html", [
        ("Flagship guides", [("BA II Plus calculator guide", "blog-ba-ii-plus-calculator-guide.html", "Every function, on a live calculator"),
                             ("CFA salary by country", "blog-cfa-salary.html", "What charterholders earn in 19 countries"),
                             ("CFA jobs and salaries", "blog-cfa-jobs-salaries.html", "10 career paths, with bonuses"),
                             ("Is the CFA worth the money?", "blog-cfa-roi.html", "Cost against pay, by country"),
                             ("How long it takes to pass", "blog-cfa-time-to-pass.html", "A model of 100,000 candidates")]),
        ("Before you start", [("Are you ready for Level I?", "blog-ready-for-cfa-level-1.html", "A 2-minute self-check"),
                              ("CFA for engineers", "blog-cfa-for-engineers.html", ""), ("CFA from any background", "blog-cfa-any-background.html", ""),
                              ("How Level I helps your job", "blog-cfa-level-1-job.html", ""), ("CIPM and other CFA Institute programs", "blog-cipm-and-cfa-institute-programs.html", "")]),
        ("CFA Program guide", [("The CFA Program explained", "cfa-program.html", ""), ("2027 exam dates and fees", "cfa-dates-fees.html", ""),
                               ("Pass rates", "cfa-pass-rates.html", ""), ("Requirements and eligibility", "blog-cfa-requirements.html", ""),
                               ("Total cost", "blog-cfa-total-cost.html", ""), ("Most challenging topics", "blog-hardest-cfa-topics.html", "")]),
        ("Big questions", [("Is the CFA worth it?", "blog-is-cfa-worth-it.html", ""), ("Why the CFA is hard", "blog-why-cfa-is-hard.html", ""),
                           ("Results: when and how", "blog-cfa-results.html", ""), ("CFA vs FRM", "blog-cfa-vs-frm.html", ""),
                           ("CFA vs MBA", "blog-cfa-vs-mba.html", ""), ("CFA vs CPA, CFP, ACCA, CA", "blog-cfa-vs-cpa-cfp-acca.html", "")])]),
    ("Levels", "cfa-program.html", [
        ("Level I", [("Level I: format and topics", "cfa-level-1.html", ""), ("Level I strategy", "blog-level-1-strategy.html", ""),
                     ("Level I formula sheet", "blog-cfa-level-1-formula-sheet.html", "")]),
        ("Level II", [("Level II: format and topics", "cfa-level-2.html", ""), ("Item sets (vignettes)", "blog-level-2-item-sets.html", "")]),
        ("Level III", [("Level III: format and topics", "cfa-level-3.html", ""), ("Written (constructed response) answers", "blog-level-3-constructed-response.html", ""),
                       ("Choosing your pathway", "blog-level-3-pathways.html", "")]),
        ("All three levels", [("How the levels differ", "blog-cfa-level-differences.html", ""), ("Pass rates by level", "cfa-pass-rates.html", ""),
                              ("Dates and fees", "cfa-dates-fees.html", "")])]),
    ("How to prepare", "how-to-prepare.html", [
        ("Start here", [("Are you ready? Self-check", "blog-ready-for-cfa-level-1.html", ""), ("Build your study plan", "blog-study-plan.html", ""),
                        ("Best order to study topics", "blog-cfa-study-order.html", ""), ("Free study planner (Excel)", "free-resources.html#planner", ""),
                        ("Self-study without coaching", "blog-cfa-self-study.html", ""), ("Choosing prep materials", "blog-choosing-prep-materials.html", "")]),
        ("Level I", [("How to pass Level I", "blog-level-1-strategy.html", ""), ("Formula sheet", "blog-cfa-level-1-formula-sheet.html", ""),
                     ("Calculator guide", "blog-ba-ii-plus-calculator-guide.html", "")]),
        ("Level II", [("How to pass Level II", "blog-level-2-item-sets.html", ""), ("Prerequisites for valuation", "prerequisites.html", "")]),
        ("Level III", [("How to pass Level III", "blog-level-3-constructed-response.html", ""), ("Pick your pathway", "blog-level-3-pathways.html", "")]),
        ("Every level", [("Most challenging topics", "blog-hardest-cfa-topics.html", ""), ("Ethics", "blog-ethics.html", ""), ("Mock exams", "blog-mock-exams.html", ""), ("Exam day", "blog-exam-day.html", ""),
                         ("The first-principles method", "blog-first-principles-method.html", "")])]),
    ("Prerequisites", "prerequisites.html", None),       # filled from the concepts at build time
    ("Free resources", "free-resources.html", [
        ("Tools", [("Study planner (Excel)", "free-resources.html#planner", "Plan, track hours, keep your streak"),
                   ("BA II Plus calculator online", "blog-ba-ii-plus-calculator-guide.html", "Press every key in your browser"),
                   ("Level I formula sheet", "blog-cfa-level-1-formula-sheet.html", "About fifty formulas by topic"),
                   ("Level I readiness self-check", "blog-ready-for-cfa-level-1.html", "Ten questions, instant advice")]),
        ("Learn", [("Prerequisites course", "prerequisites.html", "50 graded lessons, with your progress saved"),
                   ("Study blog", "blog.html", "")])]),
    ("Blog", "blog.html", []),
]
MENU_HTML = ""


# feature tiles on the right of each menu panel: (title, text, link)
PROMOS = {
    "Most searched": [("A BA II Plus in your browser", "Press every key, or watch worked exam examples play out with the formula behind each one.", "blog-ba-ii-plus-calculator-guide.html"),
                      ("What a CFA earns, worldwide", "Base pay and bonuses in 19 countries, and the ten jobs charterholders do.", "blog-cfa-salary.html")],
    "Levels": [("Which topics are hardest?", "Weight times trouble: the topics that cost the most marks at each level.", "blog-hardest-cfa-topics.html"),
               ("Ready for Level I?", "Ten honest questions and a plan for the gaps, in two minutes.", "blog-ready-for-cfa-level-1.html")],
    "How to prepare": [("Free study planner", "An Excel planner that builds your weekly plan and keeps your streak.", "free-resources.html#planner"),
                       ("How long it really takes", "We ran 100,000 candidates through the real exam calendar.", "blog-cfa-time-to-pass.html")],
    "Prerequisites": [("50 concepts, all free", "Accounting and economics from the ground up, each with an animated diagram.", "prerequisites.html"),
                      ("Start with the three statements", "How the balance sheet, income statement and cash flow fit together.", "prereq-three-statements.html")],
    "Free resources": [("Free study planner", "Plan your hours, track every session, protect your streak.", "free-resources.html#planner"),
                       ("Online BA II Plus", "A working calculator with every worksheet, free in your browser.", "blog-ba-ii-plus-calculator-guide.html")],
}


def menu_html(active):
    """The header menu. Desktop: a full-width panel opens on hover or keyboard focus, with link columns
    on the left and two feature tiles on the right. Phones: a drawer with tap-to-open sections."""
    out = ""
    for i, (label, hub, cols) in enumerate(MENU):
        links = [h for _, items in (cols or []) for _, h, _ in items]
        cur = ' aria-current="page"' if (active == hub or active in links) else ""
        if not cols:
            out += f'<div class="mi"><a class="ml" href="{hub}"{cur}>{label}</a></div>'
            continue
        body = "".join(f'<div class="mc"><p class="mh">{head}</p><ul>' + "".join(f'<li><a href="{h}">{t}</a></li>' for t, h, _ in items) + "</ul></div>"
                       for head, items in cols)
        tiles = "".join(f'<a class="mt mt{k}" href="{h}"><b>{t}</b><span>{x}</span><i aria-hidden="true"></i></a>'
                        for k, (t, x, h) in enumerate(PROMOS.get(label, [])))
        out += (f'<div class="mi has"><a class="ml" href="{hub}"{cur} aria-haspopup="true">{label}</a>'
                f'<button type="button" class="mx" aria-expanded="false" aria-label="Show {label} links"></button>'
                f'<div class="mega"><div class="wrap"><div class="mleft"><a class="mhome" href="{hub}">{label} home</a>'
                f'<div class="mcols">{body}</div></div>' + (f'<div class="mtiles">{tiles}</div>' if tiles else "") + '</div></div></div>')
    return out


def page(path, title, desc, main, active="", extra_head="", image="intro-poster.jpg"):
    beacon = (f"\n<script type=\"module\" src=\"https://static.cloudflareinsights.com/beacon.min.js\" data-cf-beacon='{{\"token\": \"{CF_BEACON}\"}}'></script>") if CF_BEACON else ""
    nav = menu_html(active)
    OBF = obfuscate(EMAIL)
    pk = photo_key(path[:-5])
    if pk and '<section class="pagehead">' in main:
        main = main.replace('<section class="pagehead">', f'<section class="pagehead photo"{photo_style(pk)}>', 1)
        image = f"img/{pk}.jpg"
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
<link rel="stylesheet" href="style.css?v=11">
{extra_head}
{('<meta name="fp-clarity" content="' + CLARITY_ID + '">') if CLARITY_ID else ""}
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="index.html"><img src="logo.svg?v=8" alt="First Principles" width="160" height="70"></a>
  <button type="button" class="burger" aria-expanded="false" aria-controls="mainnav" aria-label="Menu"><span></span></button>
  <nav aria-label="Main" id="mainnav">{nav}</nav>
  <a class="btn outline" href="prerequisites.html">Start learning</a>
</div></header>
{main}
<footer class="foot">
<div class="wrap fcols">
  <div><p class="fh">Learn</p><a href="prerequisites.html">Prerequisite concepts</a><a href="cfa-level-1.html">CFA Level I</a><a href="cfa-level-2.html">CFA Level II</a><a href="cfa-level-3.html">CFA Level III</a><a href="blog-history-of-cfa.html">History of the CFA</a></div>
  <div><p class="fh">Most searched</p><a href="blog-ba-ii-plus-calculator-guide.html">BA II Plus calculator guide</a><a href="blog-cfa-salary.html">CFA salary by country</a><a href="blog-cfa-jobs-salaries.html">CFA jobs and salaries</a><a href="blog-cfa-roi.html">Is the CFA worth the money?</a><a href="cfa-dates-fees.html">2027 exam dates and fees</a></div>
  <div><p class="fh">Prepare</p><a href="how-to-prepare.html">How to prepare</a><a href="free-resources.html#planner">Free study planner (Excel)</a><a href="blog-cfa-study-order.html">Best order to study topics</a><a href="blog-mock-exams.html">Mock exams</a><a href="blog-exam-day.html">Exam day</a></div>
  <div><p class="fh">First Principles</p><a href="index.html#about">About</a><a href="mailto:{OBF}">Contact by email</a><a href="blog.html">Study blog</a><a href="free-resources.html">Free resources</a><a href="photo-credits.html">Photo credits</a></div>
</div>
<div class="fbar"><div class="wrap">
  <p>{DISCLAIMER}</p>
  <p>Exam facts on this site were checked against CFA Institute's published pages on {CHECKED}. Dates, fees and policies change: always confirm on cfainstitute.org before you register. Explanations are original and are not taken from the CFA Program curriculum.</p>
  <p class="legal"><span>© 2026 {NAME}. Set in Figtree (SIL Open Font License).</span><a href="privacy.html">Privacy</a><a href="#" data-consent-open>Cookie settings</a><a href="photo-credits.html">Photo credits</a><a href="sitemap.xml">Sitemap</a></p>
</div></div>
</footer>
<script src="site.js?v=10" defer></script>{beacon}
</body>
</html>
"""
    (ROOT / path).write_text(out, encoding="utf-8")
    return path


def faq_pairs(p):
    m = re.search(r"\n## Questions people ask\n(.*?)(?=\n## |\Z)", p["body_md"], re.S)
    if not m:
        return []
    return [(q.strip(), re.sub(r"\s+", " ", a).strip()) for q, a in re.findall(r"### (.+?)\n\n(.+?)(?=\n### |\Z)", m.group(1), re.S)]


def tags(p):
    return [t.strip() for t in p.get("tags", "").split(",") if t.strip()]


def jsonld(p, url):
    out = ""
    faq = faq_pairs(p)
    if faq:
        out += '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"[*_]", "", a)}} for q, a in faq]}) + "</script>"
    data = {"@context": "https://schema.org", "@type": "Article", "headline": p["title"], "description": p.get("summary", ""),
            "image": f"{SITE}/thumb-{p['slug']}.svg",
            "author": {"@type": "Person", "name": NAME}, "datePublished": "2026-11-16", "dateModified": TODAY,
            "mainEntityOfPage": url, "publisher": {"@type": "Organization", "name": "First Principles"}, "keywords": ", ".join(tags(p))}
    return out + f'<script type="application/ld+json">{json.dumps(data)}</script>'


def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


PHOTOS = json.loads((ROOT / "photos.json").read_text(encoding="utf-8")) if (ROOT / "photos.json").exists() else {}
PAGE_PHOTO = {}  # slug -> photo key, filled from photos.json "pages"
for _k, _v in PHOTOS.items():
    for _slug in _v.get("pages", []):
        PAGE_PHOTO[_slug] = _k


def photo_key(slug, p=None):
    k = (p or {}).get("photo") or PAGE_PHOTO.get(slug)
    return k if k in PHOTOS else None


def photo_style(key):
    return f' style="--ph:url(img/{key}.jpg);--pp:{PHOTOS[key].get("pos", "center 40%")}"' if key else ""


def credit(key):
    c = PHOTOS[key]
    return f'Photo: {html.escape(c["artist"] or "Unknown")}, <a href="{c["licurl"] or c["page"]}" rel="license noopener">{c["lic"]}</a>, <a href="{c["page"]}" rel="noopener">Wikimedia Commons</a>'


def card(p, chip, foot, feat=False):
    k = photo_key(p["slug"], p)
    src = f"img/{k}-s.jpg" if k else f'thumb-{p["slug"]}.svg'
    return (f'<a class="card{" feat" if feat else ""}{" photo" if k else ""}" href="{p["slug"]}.html">'
            f'<span class="thumb"><img src="{src}" alt="" loading="lazy" width="640" height="360"><span class="chip">{chip}</span></span>'
            f'<span class="cb"><span class="cm">{minutes(p)} min read</span><h4>{p["title"]}</h4><p>{p.get("summary", "")}</p><span class="cf">{foot}<em>By {NAME}</em></span></span></a>')


PROMO = {
    "default": ("Free CFA study planner", "An Excel planner that builds your weekly plan, tracks every topic and keeps your streak.", "free-resources.html#planner", "Get the planner"),
    "prereq": ("50 prerequisite concepts, free", "Financial statements and economics, rebuilt from the basics, each with its own animated diagram.", "prerequisites.html", "Start reading"),
    "calc": ("A BA II Plus in your browser", "Press every key, or watch worked exam examples play out, each with its formula and a picture.", "blog-ba-ii-plus-calculator-guide.html", "Open the calculator"),
}


import quiz_bank, random as _random


def quiz_items(slug):
    out = []
    for i, (q, opts, c, x) in enumerate(quiz_bank.Q[slug]):
        order = list(range(len(opts)))
        _random.Random(f"{slug}-{i}").shuffle(order)
        out.append((q, [opts[k] for k in order], order.index(c), x))
    return out


def quiz_html(p, total):
    lis = ""
    for q, opts, c, x in quiz_items(p["slug"]):
        btns = "".join(f'<button type="button" data-v="{j}"><b>{"ABCD"[j]}</b>{html.escape(o)}</button>' for j, o in enumerate(opts))
        lis += f'<li data-c="{c}" data-x="{html.escape(x)}"><p>{html.escape(q)}</p><div class="lq-o">{btns}</div><p class="lq-e" hidden></p></li>'
    return (f'<section class="lq" id="quiz" data-lesson="{p["slug"]}" data-n="{p["n"]}" data-total="{total}">'
            f'<p class="lq-k">Lesson {p["n"]} of {total} &nbsp;·&nbsp; {p["module"]}</p><h2>Check your understanding</h2>'
            f'<p class="lq-sub">Three questions. Get two or more right to complete the lesson; your best score is saved in this browser and counts towards your <a href="prerequisites.html">course grade</a>.</p>'
            f'<ol>{lis}</ol><div class="lq-r" aria-live="polite"></div></section>')


def promo(kind):
    t, x, h, b = PROMO[kind]
    return (f'<aside class="promo"><div><h3>{t}</h3><p>{x}</p></div>'
            f'<a class="go" href="{h}" data-track="promo_click"><span>{b}</span><i aria-hidden="true"></i></a></aside>')


def article(p, back, cat, eyebrow, pager="", keep="", suffix="First Principles", kind="default", extra="", head_extra=""):
    url = f"{SITE}/{p['slug']}.html"
    tg = tags(p)
    chips = (f'<aside class="tags"><span>Tags:</span>' + "".join(f'<span>{html.escape(t)}</span>' for t in tg) + "</aside>") if tg else ""
    k = photo_key(p["slug"], p)
    cred = f'<p class="credit">{credit(k)}</p>' if k else ""
    inner = f'<article class="post"><div class="body">{render_md(p)}</div>{extra}{promo(kind) if not extra else ""}{chips}{cred}{pager}</article>'
    if p.get("layout") == "calc":
        dock = ('<aside id="ba2dock" aria-label="Calculator"><button type="button" class="dock-toggle" aria-expanded="false">Calculator</button>'
                '<div class="ba2-host"></div><p class="dock-note">Click the keys or type on your keyboard. Every grey box on this page plays its keystrokes here. '
                'This is our own replica of the BA II Plus key layout and logic, built for practice; check your exam answers on the real calculator.</p></aside>')
        body_block = f'<div class="wrap calcpage">{inner}{dock}</div>'
    else:
        body_block = f'<div class="wrap">{inner}</div>'
    art = "" if k else f'<img class="hart" src="thumb-{p["slug"]}.svg" alt="" width="640" height="360">'
    main = f"""<main>
<section class="ahead{' photo' if k else ''}"{photo_style(k)}>{art}<div class="wrap"><a class="back" href="{back[0]}">{back[1]}</a></div></section>
<div class="wrap"><header class="acard">
  <div class="ameta"><span class="rt">{minutes(p)} min read</span><span class="cat">{eyebrow}</span><span class="dt">Updated {UPDATED}</span></div>
  <h1>{p['title']}</h1>
  <div class="aby"><span>By <a href="index.html#about">{NAME}</a></span><span>{cat}</span></div>
  <p class="lead">{p.get('summary', '')}</p>
</header></div>
{body_block}
{keep}
</main>"""
    kw = f'<meta name="keywords" content="{html.escape(", ".join(tg))}">' if tg else ""
    if p.get("layout") == "calc":
        kw += '<script src="ba2.js" defer></script>'
    kw += head_extra
    return page(p["slug"] + ".html", f"{p['title']} | {suffix}", p.get("summary", ""), main, extra_head=kw + jsonld(p, url),
                image=(f"img/{k}.jpg" if k else f"thumb-{p['slug']}.svg"))


def keep_reading(items, chip, foot):
    return f'<section class="keep"><div class="wrap"><span class="eyebrow">Keep reading</span><div class="grid">{"".join(card(q, chip(q), foot(q)) for q in items)}</div></div></section>'


def nxt(lst, i, n=3):
    return [lst[(i + k) % len(lst)] for k in range(1, n + 1)]


def build():
    built = ["index.html"]
    cfa, blog, pre = load("cfa"), load("blog"), load("prereq")
    for i, p in enumerate(pre):
        p["n"] = i + 1
    pcols = []
    for topic in ["Financial Statement Analysis", "Economics"]:
        mods = []
        for p in pre:
            if p["topic"] == topic and p["module"] not in mods:
                mods.append(p["module"])
        pcols.append((topic, [(m, f"prerequisites.html#{slugify(m)}", "") for m in mods]))
    for k, m in enumerate(MENU):
        if m[0] == "Prerequisites":
            MENU[k] = (m[0], m[1], pcols)
    for p in cfa + blog + pre:
        make_thumb(p)

    for i, p in enumerate(cfa):
        built.append(article(p, ("cfa-program.html", "CFA Program guide"), f"Facts checked {CHECKED}", "CFA Program", suffix="CFA Program guide | First Principles",
                             keep=keep_reading(nxt(cfa, i), lambda q: "CFA guide", lambda q: "CFA Program guide")))
    for i, p in enumerate(blog):
        built.append(article(p, ("blog.html", "Study blog"), "Study blog", (p.get("group") or "Study blog").split(":")[0], kind=("default" if p.get("layout") == "calc" else "prereq"), suffix="CFA study blog | First Principles",
                             keep=keep_reading(nxt(blog, i), lambda q: "Study blog", lambda q: "Study strategy")))
    for i, p in enumerate(pre):
        prev_p, next_p = (pre[i - 1] if i else None), (pre[i + 1] if i + 1 < len(pre) else None)
        pager = '<nav class="pager">'
        pager += (f'<a href="{prev_p["slug"]}.html"><span>Previous lesson</span>{prev_p["title"]}</a>' if prev_p else "")
        pager += (f'<a class="next" href="{next_p["slug"]}.html"><span>Next lesson</span>{next_p["title"]}</a>' if next_p else "")
        pager += "</nav>"
        built.append(article(p, ("prerequisites.html", "Prerequisites course"), f'Lesson {p["n"]} of {len(pre)}', p["topic"], pager, kind="calc", suffix="CFA prerequisite explained",
                             extra=quiz_html(p, len(pre)), head_extra='<script src="course.js" defer></script>',
                             keep=keep_reading(nxt(pre, i), lambda q: f'Concept {q["n"]:02d}', lambda q: q["topic"])))

    # ---- prerequisites course page
    bmap = {q["slug"]: q for q in blog}
    def picks(slugs, head):
        return (f'<section class="cpicks"><p class="cph">{head}</p><div class="grid">' +
                "".join(card(bmap[x], "Study blog", (bmap[x].get("group") or "Study blog").split(":")[0]) for x in slugs if x in bmap) + "</div></section>")
    syll = ""
    for part, topic in (("Part 1", "Financial Statement Analysis"), ("Part 2", "Economics")):
        items_t = [q for q in pre if q["topic"] == topic]
        syll += f'<section class="cpart"><p class="cpk">{part} &nbsp;·&nbsp; {len(items_t)} lessons</p><h2>{"Financial statement analysis" if topic.startswith("Fin") else "Economics"}</h2>'
        mods = []
        for q in items_t:
            if q["module"] not in mods: mods.append(q["module"])
        for mi, mod in enumerate(mods):
            its = [q for q in items_t if q["module"] == mod]
            rows = "".join(f'<li data-s="{q["slug"]}"><span class="cn">{q["n"]:02d}</span><a href="{q["slug"]}.html">{q["title"]}</a><span class="cm">{minutes(q) + 2} min</span><span class="cs" aria-label="status">Not started</span></li>' for q in its)
            syll += (f'<div class="cmod" id="{slugify(mod)}"><div class="cmh"><h3>{mod}</h3><span class="cmp" data-mod="{slugify(mod)}" data-n="{len(its)}">0 / {len(its)}</span></div><ol>{rows}</ol></div>')
        syll += "</section>"
        if part == "Part 1":
            syll += picks(["blog-why-cfa-is-hard", "blog-hardest-cfa-topics", "blog-cfa-study-order"], "Worth reading between the two parts")
    syll += picks(["blog-ba-ii-plus-calculator-guide", "blog-ready-for-cfa-level-1", "blog-history-of-cfa"], "When you have finished")
    main = f"""<main>
<section class="pagehead"><div class="wrap solo"><div>
  <p class="crumbs"><a href="index.html">Home</a> › Prerequisites course</p>
  <span class="eyebrow">Course · {len(pre)} lessons · {3 * len(pre)} quiz questions · final test</span>
  <h1>Prerequisites course: financial statements and economics</h1>
  <p class="lead">Financial statement analysis and economics sit underneath every level of the CFA Program: Level I teaches them, Level II applies them to valuation, and Level III assumes you can use them without being reminded. This course rebuilds the ideas that come up again and again, one lesson at a time, each with a diagram, a worked example and a graded quiz.</p>
</div></div></section>
<div class="wrap cwrap">
  <section class="cdash" aria-label="Your progress">
    <div class="cd-main">
      <p class="cd-k">Your progress</p>
      <p class="cd-big"><b data-k="done">0</b> of {len(pre)} lessons complete</p>
      <div class="cd-bar"><i data-k="bar"></i></div>
      <div class="cd-stats">
        <p><b data-k="avg">–</b><span>average score, lessons taken</span></p>
        <p><b data-k="test">–</b><span>final test, best</span></p>
        <p><b data-k="grade">–</b><span>course grade</span></p>
      </div>
    </div>
    <div class="cd-act">
      <a class="btn" data-k="cont" href="{pre[0]["slug"]}.html">Start lesson 1</a>
      <a class="btn line" href="course-test.html">Take the final test</a>
      <button type="button" class="cd-reset" data-k="reset">Reset my progress</button>
    </div>
  </section>
  <details class="crules"><summary>How grading works</summary>
    <ul>
      <li><b>Lessons.</b> Each lesson ends with three questions. Two or more correct completes the lesson. You can retake a quiz as often as you like; your best score counts.</li>
      <li><b>Final test.</b> 25 questions drawn at random from the whole course, about 40 minutes. Retake it as often as you like; your best score counts.</li>
      <li><b>Course grade.</b> 70% from your best lesson scores across all lessons (a lesson not yet taken counts as zero), 30% from your best final test: A from 90%, B from 80%, C from 70%, D from 60%.</li>
      <li><b>Completion.</b> Complete all {len(pre)} lessons and score 70% or more on the final test to unlock a printable completion record.</li>
      <li><b>Privacy.</b> Progress is stored only in this browser, so it does not follow you to another device. Nothing is sent to us.</li>
    </ul>
  </details>
  <section class="crecord" data-k="record" hidden>
    <p class="cr-k">Course complete</p>
    <h2>Completion record</h2>
    <p class="cr-line">This records that <input type="text" data-k="name" placeholder="your name" aria-label="Your name"> completed all {len(pre)} lessons of the First Principles prerequisites course in financial statement analysis and economics, with a course grade of <b data-k="grade2"></b> and a best final test score of <b data-k="test2"></b>, on <b data-k="date"></b>.</p>
    <p class="cr-note">A personal record from First Principles (firstprinciples.courses). It is not a CFA Institute credential and does not count towards the CFA Program.</p>
    <button type="button" class="btn" data-k="print">Print or save as PDF</button>
  </section>
  {syll}
</div>
</main>"""
    built.append(page("prerequisites.html", "CFA prerequisites course: financial statements and economics, with graded quizzes | First Principles",
                      f"A {len(pre)}-lesson course in the financial statement analysis and economics behind CFA Levels I to III, with a graded quiz after every lesson, a final test and progress saved in your browser.",
                      main, active="prerequisites.html", extra_head='<script src="course.js" defer></script>'))

    # ---- final course test
    bank = []
    for q in pre:
        for qq, opts, c, x in quiz_items(q["slug"]):
            bank.append({"s": q["slug"], "t": q["title"], "m": q["module"], "p": 1 if q["topic"].startswith("Fin") else 2, "q": qq, "o": opts, "c": c, "x": x})
    main = f"""<main>
<section class="pagehead"><div class="wrap solo"><div>
  <p class="crumbs"><a href="index.html">Home</a> › <a href="prerequisites.html">Prerequisites course</a> › Final test</p>
  <span class="eyebrow">Final test · 25 questions · about 40 minutes</span>
  <h1>Prerequisites course: final test</h1>
  <p class="lead">Twenty-five questions drawn at random from all {len(pre)} lessons, so every attempt is different. Answer them all, then submit to see your score, your grade, a breakdown by part and a review of anything you missed.</p>
</div></div></section>
<div class="wrap cwrap"><section class="ctest" data-k="test"><p>Loading the test…</p></section></div>
<script type="application/json" id="bank">{json.dumps(bank, ensure_ascii=False).replace("</", "<\\/")}</script>
</main>"""
    built.append(page("course-test.html", "Final test: CFA prerequisites course | First Principles",
                      "A 25-question final test on financial statement analysis and economics for CFA candidates, drawn at random from 150 questions, with instant grading and review.",
                      main, active="prerequisites.html", extra_head='<script src="course.js" defer></script>'))

    # ---- blog index
    order = ["Most searched: the guides candidates look for most", "Before you start: requirements, cost and careers", "The CFA compared", "How the exams work", "Strategy: how to tackle the exams", "Tools: formulas, calculator and self-study"]
    blog_groups = "".join(f'<section class="group"><h2>{g}</h2><div class="grid" style="margin-top:1.4rem">' + "".join(card(p, "Study blog", g.split(":")[0]) for p in blog if p.get("group") == g) + "</div></section>" for g in order)
    main = f"""<main>
<section class="pagehead"><div class="wrap solo"><div>
  <p class="crumbs"><a href="index.html">Home</a> › Study blog</p>
  <span class="eyebrow">Study blog</span>
  <h1>Everything CFA candidates ask, answered</h1>
  <p class="lead">Requirements, costs, salaries, how long it takes, how it compares with the FRM, MBA, CPA and ACCA, formulas and calculator settings, plus study plans, Level II vignettes, Level III written answers, ethics, mock exams and exam day. The advice draws on CFA Institute's own guidance and on what the main prep providers recommend, rewritten as one consistent method.</p>
</div></div></section>
<div class="wrap" style="padding-bottom:4rem">
{blog_groups}
<section class="group"><h2>The CFA Program, in facts</h2><div class="grid" style="margin-top:1.4rem">{''.join(card(p, "CFA guide", "CFA Program guide") for p in cfa)}</div></section>
<section class="group"><h2>Prerequisite concepts</h2><p style="margin-top:1rem"><a class="more" href="prerequisites.html">All {len(pre)} financial statement analysis and economics concepts</a></p></section>
</div>
</main>"""
    built.append(page("blog.html", "CFA study blog: strategies for Levels I, II and III | First Principles",
                      "Practical strategies for the CFA exams: study plans, Level II item sets, Level III constructed response, ethics, mock exams and exam day.",
                      main, active="blog.html"))

    built.append(most_searched(blog))
    built.append(how_to_prepare(cfa, blog))
    built.append(free_resources(blog, pre))
    (ROOT / "glossary.html").write_text('<!doctype html><meta charset="utf-8"><meta name="robots" content="noindex"><link rel="canonical" href="https://firstprinciples.courses/blog.html"><meta http-equiv="refresh" content="0; url=blog.html"><title>Moved</title><a href="blog.html">This page has moved to the study blog.</a>', encoding="utf-8")
    built.append(photo_credits())
    built.append(privacy())
    home(cfa, blog, pre)

    page("404.html", "Page not found | First Principles", "This page does not exist.",
         '<main><section class="pagehead"><div class="wrap solo"><div><span class="eyebrow">404</span><h1>That page is not here</h1><p class="lead">Try the <a style="color:#3DBEF0" href="index.html">home page</a>, the <a style="color:#3DBEF0" href="prerequisites.html">prerequisite concepts</a> or the <a style="color:#3DBEF0" href="blog.html">study blog</a>.</p></div></div></section></main>')

    urls = "".join(f"  <url><loc>{SITE}/{'' if b == 'index.html' else b}</loc><lastmod>{TODAY}</lastmod></url>\n" for b in sorted(set(built)))
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n', encoding="utf-8")
    print(f"built {len(set(built))} pages + 404 + sitemap + {len(cfa + blog + pre)} thumbnails")


def privacy():
    main = f"""<main>
<section class="pagehead"><div class="wrap solo"><div>
  <p class="crumbs"><a href="index.html">Home</a> › Privacy</p>
  <span class="eyebrow">Privacy</span>
  <h1>Privacy and cookies</h1>
  <p class="lead">What this site measures, why, and how to change your choice.</p>
</div></div></section>
<div class="wrap"><article class="post"><div class="body">
<h2>Visit counts (always on, no cookies)</h2>
<p>We use Cloudflare Web Analytics to count page views. It sets no cookies and does not track you across sites; it tells us which pages are read, where visitors come from (country, referring site) and which devices they use.</p>
<h2>Usage insights (only if you accept)</h2>
<p>If you click <b>Accept</b> on the banner, we load Microsoft Clarity. It records how pages are used: clicks, scrolling, time on page and anonymised session replays, so we can see which explanations work and redesign the ones that do not. Text you type into forms is masked. Clarity sets cookies and is provided by Microsoft; see the <a href="https://privacy.microsoft.com/privacystatement" rel="noopener">Microsoft privacy statement</a> and <a href="https://learn.microsoft.com/clarity/setup-and-installation/cookie-list" rel="noopener">Clarity's cookie list</a>.</p>
<p>If you click <b>Decline</b>, Clarity is never loaded. You can change your choice at any time with <a href="#" data-consent-open>cookie settings</a>.</p>
<h2>Your course progress</h2>
<p>Quiz scores and course progress are stored only in your own browser (local storage). They are never sent to us, and you can erase them from the course page.</p>
<h2>Contact</h2>
<p>Questions about privacy: <a href="mailto:{obfuscate(EMAIL)}">email us</a>.</p>
</div></article></div>
</main>"""
    return page("privacy.html", "Privacy and cookies | First Principles", "What First Principles measures, why, and how to change your cookie choice.", main)


def photo_credits():
    rows = ""
    for k, c in sorted(PHOTOS.items(), key=lambda kv: kv[1]["title"]):
        used = ", ".join(f'<a href="{u}.html">{u.replace("blog-", "").replace("-", " ")}</a>' for u in c.get("pages", []))
        rows += (f'<div class="pc"><img src="img/{k}-s.jpg" alt="" loading="lazy" width="320" height="180"><div><p class="pt">{html.escape(c["title"].replace("File:", "").rsplit(".", 1)[0])}</p>'
                 f'<p>{credit(k)}</p><p class="pu">Used on: {used}</p></div></div>')
    main = f"""<main>
<section class="pagehead"><div class="wrap solo"><div>
  <p class="crumbs"><a href="index.html">Home</a> › Photo credits</p>
  <span class="eyebrow">Photo credits</span>
  <h1>The photographs on this site</h1>
  <p class="lead">Diagrams and charts are our own. The photographs come from Wikimedia Commons under free licences (public domain, CC0, CC BY or CC BY-SA); they are shown cropped and with a dark overlay. Thank you to every photographer below.</p>
</div></div></section>
<div class="wrap" style="padding:3rem 1.5rem 4rem"><div class="pcs">{rows}</div></div>
</main>"""
    return page("photo-credits.html", "Photo credits | First Principles", "Credits and licences for the photographs used on First Principles.", main)


def hub(path, title, desc, crumb, eyebrow, h1, lead, sections, active):
    body = ""
    for head, intro, items, chip in sections:
        body += f'<section class="group"><h2>{head}</h2>' + (f'<p class="sub" style="margin-top:.6rem">{intro}</p>' if intro else "")
        body += '<div class="grid" style="margin-top:1.4rem">' + "".join(card(q, chip, q.get("group", "").split(":")[0] or q.get("topic") or "CFA guide") for q in items) + "</div></section>"
    main = f"""<main>
<section class="pagehead"><div class="wrap solo"><div>
  <p class="crumbs"><a href="index.html">Home</a> › {crumb}</p>
  <span class="eyebrow">{eyebrow}</span>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>
</div></div></section>
<div class="wrap" style="padding-bottom:4rem">{body}</div>
</main>"""
    return page(path, title, desc, main, active=active)


PLANNER_BOX = """<section class="planner" id="planner"><div class="pl-text">
<span class="eyebrow">Free download</span>
<h2>The CFA study planner (Excel)</h2>
<p>Type in your level, start date, exam date and the hours you can give each day. The workbook does the rest:</p>
<ul>
<li><b>A verdict on your plan</b>: comfortable, tight or short, with the buffer in hours.</li>
<li><b>Hours per topic</b>, weighted by how much each topic counts in the exam, with a "priority now" score that tells you what to practise next.</li>
<li><b>A week-by-week plan</b> in three phases (learn, practise, mocks) with a focus topic and an hours target for every week.</li>
<li><b>A daily log</b> that feeds a dashboard: hours done against plan, accuracy, mock scores.</li>
<li><b>A habit calendar and streak counter</b> built on a "never zero" daily minimum, plus time-management and discipline rules that work.</li>
</ul>
<p><a class="btn" href="cfa-study-planner.xlsx" download data-track="planner_download">Download the planner (.xlsx)</a></p>
<p class="small">Works in Microsoft Excel, Google Sheets (File, Import) and LibreOffice. Levels I, II and III. Free, no sign-up.</p>
</div><figure class="pl-fig"><div class="stage">{fig}</div></figure></section>"""


def how_to_prepare(cfa, blog):
    pick = {p["slug"]: p for p in blog + cfa}
    g = lambda *xs: [pick[x] for x in xs if x in pick]
    sections = [
        ("Start here: every level", "The method is the same at every level: a plan you can keep, the right materials, lots of questions and full mock exams at the end.",
         g("blog-ready-for-cfa-level-1", "blog-study-plan", "blog-cfa-study-order", "blog-cfa-self-study", "blog-choosing-prep-materials", "blog-first-principles-method"), "Every level"),
        ("Level I: breadth and speed", "180 multiple-choice questions across ten topics. Cover everything once, then drill questions until the formulas and the calculator are automatic.",
         g("cfa-level-1", "blog-level-1-strategy", "blog-cfa-level-1-formula-sheet", "blog-ba-ii-plus-calculator-guide"), "Level I"),
        ("Level II: valuation in vignettes", "Item sets: a long case with four questions. Practise reading the case first, and know the valuation models well enough to apply them, not just recognise them.",
         g("cfa-level-2", "blog-level-2-item-sets", "blog-cfa-level-differences"), "Level II"),
        ("Level III: portfolios and written answers", "Half the exam is written. Practise answering in short, exact sentences under time, and choose a pathway that matches your career.",
         g("cfa-level-3", "blog-level-3-constructed-response", "blog-level-3-pathways"), "Level III"),
        ("The final weeks", "Ethics deserves time at every level; mocks show where you stand; exam day is a skill you can rehearse.",
         g("blog-hardest-cfa-topics", "blog-ethics", "blog-mock-exams", "blog-exam-day", "blog-cfa-results"), "Every level"),
    ]
    out = hub("how-to-prepare.html", "How to prepare for CFA Level I, II and III: plans and strategy by level | First Principles",
              "How to prepare for each CFA level: study plans, strategy for Level I multiple choice, Level II item sets and Level III written answers, mocks, ethics and a free Excel study planner.",
              "How to prepare", "Study plans by level", "How to prepare for the CFA exams",
              "A plan for each level, from first reading to exam day. Start with the method that works at every level, then go to your level.", sections, "how-to-prepare.html")
    html_ = (ROOT / out).read_text(encoding="utf-8")
    html_ = html_.replace('<div class="wrap" style="padding-bottom:4rem">', '<div class="wrap" style="padding-bottom:4rem">' + PLANNER_BOX.format(fig=figures.planner_phases()), 1)
    (ROOT / out).write_text(html_, encoding="utf-8")
    return out


def free_resources(blog, pre):
    pick = {p["slug"]: p for p in blog}
    tools = [pick[x] for x in ["blog-ba-ii-plus-calculator-guide", "blog-ready-for-cfa-level-1", "blog-cfa-level-1-formula-sheet", "blog-cfa-study-order"] if x in pick]
    sections = [("Free tools", "", tools, "Free tool"),
                ("Free lessons", f"All {len(pre)} prerequisite concepts are free, each with an animated diagram and a worked example. Start with these:", pre[:4], "Free lesson")]
    out = hub("free-resources.html", "Free CFA resources: study planner (Excel), online BA II Plus calculator, formula sheet | First Principles",
              "Free CFA study resources: an Excel study planner with time management and streaks, an online BA II Plus calculator, the Level I formula sheet, and the 50-lesson prerequisites course.",
              "Free resources", "Free, no sign-up", "Free CFA resources",
              "Tools and lessons you can use today: a study planner that keeps you on schedule, a calculator you can practise on in your browser, formula sheets and the foundations every level builds on.",
              sections, "free-resources.html")
    html_ = (ROOT / out).read_text(encoding="utf-8")
    html_ = html_.replace('<div class="wrap" style="padding-bottom:4rem">', '<div class="wrap" style="padding-bottom:4rem">' + PLANNER_BOX.format(fig=figures.planner_phases()), 1)
    (ROOT / out).write_text(html_, encoding="utf-8")
    return out


def most_searched(blog):
    top = sorted([p for p in blog if p.get("top")], key=lambda p: float(p["top"]))
    pick = {p["slug"]: p for p in blog}
    also = [pick[s] for s in ["blog-cfa-requirements", "blog-cfa-total-cost", "blog-how-long-cfa", "blog-is-cfa-worth-it", "blog-cfa-level-1-formula-sheet", "blog-cfa-results"] if s in pick]
    feats = "".join(card(p, f"Most searched #{i + 1}", "Flagship guide") for i, p in enumerate(top))
    main = f"""<main>
<section class="pagehead"><div class="wrap solo"><div>
  <p class="crumbs"><a href="index.html">Home</a> › Most searched</p>
  <span class="eyebrow">What candidates search for most</span>
  <h1>The most searched CFA questions, answered in depth</h1>
  <p class="lead">We track what CFA candidates around the world type into search engines, then write the deepest answer we can for the biggest questions: interactive where it helps, global rather than one-country, and in plain English.</p>
</div></div></section>
<div class="wrap" style="padding-bottom:4rem">
<section class="group"><h2>Flagship guides</h2><div class="grid big" style="margin-top:1.4rem">{feats}</div></section>
<section class="group"><h2>Also among the most searched</h2><div class="grid" style="margin-top:1.4rem">{''.join(card(p, "Study blog", p.get("group", "").split(":")[0]) for p in also)}</div></section>
</div>
</main>"""
    return page("most-searched.html", "Most searched CFA questions: calculator guide, salaries by country and more | First Principles",
                "In-depth answers to the CFA questions candidates search for most: an interactive BA II Plus calculator guide, CFA salaries by country, requirements, cost and more.",
                main, active="most-searched.html")


def glossary(items):
    terms = {}
    for p in items:
        for t in tags(p) + [p["title"]]:
            terms.setdefault(t.lower(), (t, []))[1].append(p)
    groups = {}
    for key in sorted(terms):
        t, ps = terms[key]
        letter = key[0].upper() if key[0].isalpha() else "#"
        links = ", ".join(f'<a href="{q["slug"]}.html">{q["title"]}</a>' for q in dict((q["slug"], q) for q in ps).values())
        groups.setdefault(letter, []).append(f'<li id="{slugify(t)}"><b>{t}</b><span>{links}</span></li>')
    nav = " ".join(f'<a href="#letter-{L}">{L}</a>' for L in groups)
    body = "".join(f'<section class="gl" id="letter-{L}"><h2>{L}</h2><ul>{"".join(v)}</ul></section>' for L, v in groups.items())
    main = f"""<main>
<section class="pagehead"><div class="wrap solo"><div>
  <p class="crumbs"><a href="index.html">Home</a> › Glossary</p>
  <span class="eyebrow">{len(terms)} terms</span>
  <h1>CFA glossary, A to Z</h1>
  <p class="lead">Every term, synonym and question covered on this site, with a link to the page that explains it from first principles: accounting, economics, exam format, pass rates and study strategy.</p>
</div></div></section>
<div class="wrap" style="padding-bottom:4rem"><p class="letters">{nav}</p>{body}</div>
</main>"""
    return page("glossary.html", "CFA glossary: financial statement analysis, economics and exam terms explained | First Principles",
                f"An A to Z of {len(terms)} CFA terms in financial statement analysis, economics, exam format and study strategy, each linked to a plain-English explanation.", main)


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

    blog_row = row("Study blog", "blog.html", [pick[s] for s in ["blog-ba-ii-plus-calculator-guide", "blog-cfa-salary", "blog-cfa-requirements", "blog-is-cfa-worth-it"]],
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
    <p class="lead">Every CFA topic taught through diagrams, real market examples and the reasoning behind each formula, so the exam tests what you understand rather than what you managed to memorise.</p>
    <div class="actions"><a class="btn" href="prerequisites.html">Start the prerequisites course</a><a class="btn line" href="cfa-program.html">Read the CFA guide</a></div>
  </div>
</section>

<section class="discover"><div class="wrap">
  <h2>Discover the CFA, from first principles</h2>
  <p class="sub">What the exams test, what the charter leads to, and the skills you need before you start.</p>
  <div class="dgrid">
    <div class="dcards">
      <a class="dc wide" href="blog-ready-for-cfa-level-1.html" data-track="discover_ready"><h3>Are you ready for CFA Level I?</h3><p>A 5-minute self-check with visuals: normal distributions, present value, bond prices, inflation and more. Instant marking and a score for each area, so you know what to brush up on before you register.</p></a>
      <a class="dc" href="prerequisites.html"><h3>Take the prerequisites course</h3><p>{len(pre)} lessons in financial statements and economics, each with an animated diagram, a worked example and a graded quiz.</p></a>
      <a class="dc" href="blog-ba-ii-plus-calculator-guide.html"><h3>Practise on a BA II Plus in your browser</h3><p>Press every key yourself, or watch worked exam examples play out key by key, each with its formula.</p></a>
      <a class="dc" href="blog-cfa-salary.html"><h3>See what a CFA earns, worldwide</h3><p>Base pay and bonuses in 19 countries, and the jobs charterholders actually do, from real salary data.</p></a>
      <a class="dc" href="blog-why-cfa-is-prestigious.html"><h3>Why the charter carries weight</h3><p>Sixty years of history, fewer than half passing at every level, and an ethics pledge charterholders renew every year.</p></a>
    </div>
    <aside class="dlinks">
      <p class="dh">Quick links</p>
      <a href="cfa-dates-fees.html">2027 exam dates and fees</a><a href="cfa-pass-rates.html">Pass rates</a><a href="blog-cfa-requirements.html">Requirements and eligibility</a><a href="blog-study-plan.html">Build a study plan</a><a href="blog-history-of-cfa.html">History of the CFA</a>
      <p class="dh">Featured content</p>
      <a href="blog-cfa-roi.html">Is the CFA worth the money?</a><a href="blog-cfa-time-to-pass.html">How long it really takes to pass</a><a href="blog-hardest-cfa-topics.html">The hardest CFA topics</a>
    </aside>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <span class="eyebrow">The method</span>
  <h2>What is a first-principles approach?</h2>
  <p class="sub">A first principle is a statement that cannot be reduced any further: it is true by definition or by logic, not because a textbook says so. Reasoning from first principles means taking a problem apart until only those statements are left, then rebuilding the answer from them, one step at a time.</p>
  <p class="sub">The CFA curriculum runs to thousands of pages, yet almost all of it rests on a handful of such statements. Learn them properly and most formulas stop being things to remember. They become things you can work out, check and explain, which is exactly what Level II and Level III ask you to do.</p>
  <div class="bedrock">
    <p class="bh">The ideas almost everything rests on</p>
    <ul>
      <li><b>Money now is worth more than money later</b><span>Discounting, bond pricing, valuation, capital budgeting</span></li>
      <li><b>Assets = liabilities + equity, always</b><span>Every accounting entry, the three statements, analyst adjustments</span></li>
      <li><b>Identical cash flows have one price</b><span>No-arbitrage pricing of forwards, swaps and options</span></li>
      <li><b>Investors want more return for more risk</b><span>Required returns, the cost of capital, the CAPM</span></li>
      <li><b>Risk that can be diversified away earns nothing</b><span>Portfolio theory, beta, asset allocation</span></li>
      <li><b>Prices move until supply meets demand</b><span>Elasticity, market structures, exchange rates, interest rates</span></li>
    </ul>
  </div>
  <div class="steps">
    <div><span class="n">1</span><h3>Take it apart</h3><p>Ask what has to be true for the result to hold, and keep asking until you reach a statement like the ones above.</p></div>
    <div><span class="n">2</span><h3>Rebuild it, one step at a time</h3><p>Add one idea at a time, with a picture at every step, and check that each step follows from the one before.</p></div>
    <div><span class="n">3</span><h3>Name the formula last, then test it</h3><p>The formula only writes down what you can already see. Then predict the answer before you calculate it, and find out why if you were wrong.</p></div>
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
  <span class="eyebrow">Read now</span>
  <h2>Good preparation starts with understanding.</h2>
  <p class="sub">While the video course is in production, the written material is open: exam guides, strategy, research and the {len(pre)}-lesson prerequisites course.</p>
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
