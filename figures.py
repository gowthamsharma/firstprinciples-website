"""
Diagrams for the First Principles website, drawn as inline SVG.
Classes drive the one-time reveal in site.js / style.css:
  d  = a line that draws itself      g  = a bar that grows up      gx = a bar that grows right
  f  = fades in                      style --t = delay in seconds
Every number in these pictures is invented for teaching; nothing is copied from the curriculum.
"""
import math

BLUE, TEAL, YEL, INK, SOFT, DIM, RULE, RED, BLUEB = "#58C4DD", "#5CD0B3", "#FFFF00", "#ECECEC", "#BDBDBD", "#8C8C8C", "#3a3a3a", "#FC6255", "#9CDCEB"
FONT = 'font-family="CMU Serif, Georgia, serif"'


class S:
    def __init__(self, w=640, h=300, label=""):
        self.w, self.h, self.label, self.p = w, h, label, []

    def raw(self, s):
        self.p.append(s); return self

    def text(self, s, x, y, size=14, fill=SOFT, anchor="start", italic=False, t=0.0, cls="f"):
        st = ' font-style="italic"' if italic else ""
        self.p.append(f'<text class="{cls}" style="--t:{t}s" x="{x:.1f}" y="{y:.1f}" fill="{fill}" font-size="{size}" text-anchor="{anchor}"{st} {FONT}>{s}</text>')
        return self

    def line(self, pts, color=BLUE, width=2.4, t=0.0, dash=None, cls="d", opacity=1):
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        da = f' stroke-dasharray="{dash}"' if dash else ""
        if dash and cls == "d":
            cls = "f"
        self.p.append(f'<path class="{cls}" style="--t:{t}s" d="{d}" pathLength="1" fill="none" stroke="{color}" stroke-width="{width}" stroke-opacity="{opacity}" stroke-linejoin="round" stroke-linecap="round"{da}/>')
        return self

    def curve(self, fn, x0, x1, X, Y, n=120, **kw):
        pts = [(X(x0 + (x1 - x0) * i / n), Y(fn(x0 + (x1 - x0) * i / n))) for i in range(n + 1)]
        return self.line(pts, **kw)

    def rect(self, x, y, w, h, fill=BLUE, op=0.8, t=0.0, cls="g", stroke=None):
        sk = f' stroke="{stroke}" stroke-width="1.2"' if stroke else ""
        self.p.append(f'<rect class="{cls}" style="--t:{t}s" x="{x:.1f}" y="{y:.1f}" width="{max(w, 0):.1f}" height="{max(h, 0):.1f}" fill="{fill}" fill-opacity="{op}"{sk}/>')
        return self

    def dot(self, x, y, r=5, fill=YEL, t=0.0):
        self.p.append(f'<circle class="f" style="--t:{t}s" cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}"/>'); return self

    def box(self, x, y, w, h, label, stroke=BLUE, fill="none", size=14, t=0.0, color=INK, sub=None):
        self.p.append(f'<rect class="f" style="--t:{t}s" x="{x:.1f}" y="{y:.1f}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="{stroke}" stroke-width="1.3"/>')
        cy = y + h / 2 + (size * 0.35 if not sub else -2)
        self.text(label, x + w / 2, cy, size, color, "middle", t=t)
        if sub:
            self.text(sub, x + w / 2, cy + size + 2, size - 2, DIM, "middle", True, t=t)
        return self

    def arrow(self, x1, y1, x2, y2, color=DIM, t=0.0, width=1.4):
        a = math.atan2(y2 - y1, x2 - x1); h = 8
        p1 = (x2 - h * math.cos(a - 0.4), y2 - h * math.sin(a - 0.4)); p2 = (x2 - h * math.cos(a + 0.4), y2 - h * math.sin(a + 0.4))
        self.line([(x1, y1), (x2, y2)], color, width, t)
        self.p.append(f'<path class="f" style="--t:{t + 0.6}s" d="M{p1[0]:.1f},{p1[1]:.1f} L{x2:.1f},{y2:.1f} L{p2[0]:.1f},{p2[1]:.1f}" fill="none" stroke="{color}" stroke-width="{width}"/>')
        return self

    def axes(self, x0, y0, x1, y1, xl="", yl=""):
        self.p.append(f'<path d="M{x0},{y1} L{x0},{y0} L{x1},{y0}" fill="none" stroke="{RULE}" stroke-width="1"/>')
        if xl: self.text(xl, x1, y0 + 32, 13, DIM, "end", True, cls="")
        if yl: self.text(yl, x0 + 6, y1 - 8, 13, DIM, "start", True, cls="")
        return self

    def svg(self):
        return f'<svg class="fx" viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{self.label}">' + "".join(self.p) + "</svg>"


def frame(s, xl="", yl="", x0=50, y0=None, x1=None, y1=34):
    y0 = s.h - 36 if y0 is None else y0
    x1 = s.w - 16 if x1 is None else x1
    s.axes(x0, y0, x1, y1, xl, yl)
    return x0, y0, x1, y1


def rng(seed):
    st = [seed]
    def r():
        st[0] = (st[0] * 1664525 + 1013904223) % 2 ** 32; return st[0] / 2 ** 32
    return r


# =====================================================================  home page
def bond_reason():
    s = S(520, 260, "Three future payments shrink more the further away they are when the interest rate rises")
    x0, y0, x1, y1 = frame(s, "years from today", "value today", 40, 220, 500, 30)
    pays = [(1, 100), (3, 100), (6, 100)]
    X = lambda t: x0 + t / 6.4 * (x1 - x0); Y = lambda v: y0 - v / 110 * (y0 - y1)
    for i, (t, v) in enumerate(pays):
        lo, hi = v / 1.03 ** t, v / 1.08 ** t
        s.rect(X(t) - 16, Y(lo), 32, y0 - Y(lo), BLUE, 0.25, i * 0.15)
        s.rect(X(t) - 16, Y(hi), 32, y0 - Y(hi), BLUE, 0.85, 0.5 + i * 0.15)
        s.text(f"{t}y", X(t), y0 + 18, 13, DIM, "middle", cls="")
        s.text(f"−{(1 - hi / lo) * 100:.0f}%", X(t), Y(lo) - 8, 14, YEL, "middle", t=1.2 + i * 0.15)
    s.text("pale: rate 3%   solid: rate 8%", x1, y1 + 4, 13, SOFT, "end", t=0.2)
    return s.svg()


def level1():
    s = S(320, 220, "Coin-toss outcomes forming a bell curve, middle 68 percent highlighted")
    x0, y0, x1, y1 = 20, 190, 300, 30
    s.axes(x0, y0, x1, y1)
    n = 10; pmf = [math.comb(n, k) / 2 ** n for k in range(n + 1)]; bw = (x1 - x0) / (n + 1); k_ = (y0 - y1) / 0.27
    for k, p in enumerate(pmf):
        h = p * k_; inside = 4 <= k <= 6
        s.rect(x0 + k * bw + bw * 0.12, y0 - h, bw * 0.76, h, TEAL if inside else BLUE, 0.85 if inside else 0.55, k * 0.05)
    sd = math.sqrt(n / 4)
    s.curve(lambda z: k_ * math.exp(-((z - 5) / sd) ** 2 / 2) / math.sqrt(2 * math.pi) / sd, -0.5, 10.5, lambda z: x0 + (z + 0.5) * bw, lambda v: y0 - v, color=YEL, width=1.6, t=0.6)
    s.text("68% within one σ", x1, y1 + 6, 15, INK, "end", t=1.2)
    return s.svg()


def level2():
    s = S(320, 220, "Eight future cash flows and their smaller present values, stacked at year zero")
    x0, y0, x1, y1 = 20, 190, 300, 30
    s.axes(x0, y0, x1, y1)
    cf = [3, 3.5, 4, 4.5, 5, 5.5, 6, 18]; pv = [c / 1.12 ** (t + 1) for t, c in enumerate(cf)]
    step = (x1 - x0) / 9; k = (y0 - y1 - 10) / 27; stack = 0
    for t, (c, v) in enumerate(zip(cf, pv)):
        x = x0 + (t + 1.5) * step
        s.rect(x - step * 0.3, y0 - c * k, step * 0.6, c * k, "none", 0, t * 0.06, stroke=BLUE)
        s.rect(x - step * 0.3, y0 - v * k, step * 0.6, v * k, BLUE, 0.7, 0.4 + t * 0.06)
        s.text(str(t + 1), x, y0 + 16, 11, DIM, "middle", cls="")
    xs = x0 + 0.5 * step
    for i, v in enumerate(pv):
        s.rect(xs - step * 0.3, y0 - (stack + v) * k, step * 0.6, v * k, TEAL, 1, 1.0 + i * 0.08, stroke="#000"); stack += v
    s.text("0", xs, y0 + 16, 11, INK, "middle", cls="")
    s.text(f"{stack:.1f} today", xs + step * 0.5, y0 - stack * k + 12, 14, TEAL, italic=True, t=1.8)
    return s.svg()


def level3():
    s = S(320, 220, "A cloud of portfolios under the efficient frontier, with the capital market line touching it")
    x0, y0, x1, y1 = 20, 190, 300, 30
    s.axes(x0, y0, x1, y1, "risk", "return")
    s0, m0, kf, rf = 0.09, 0.07, 0.42, 0.03
    fr = lambda q: m0 + kf * math.sqrt(max(0, q * q - s0 * s0))
    X = lambda q: x0 + q / 0.32 * (x1 - x0); Y = lambda m: y0 - m / 0.21 * (y0 - y1)
    r = rng(7)
    for i in range(150):
        q = s0 + 0.21 * r() ** 0.8; u = 2 * r() ** 0.7 - 1
        s.p.append(f'<circle class="f" style="--t:{i * 0.004:.3f}s" cx="{X(q):.1f}" cy="{Y(m0 + kf * math.sqrt(q * q - s0 * s0) * u * 0.95):.1f}" r="1.7" fill="{BLUEB}" fill-opacity="0.5"/>')
    s.curve(fr, s0, 0.3, X, Y, color=INK, width=2, t=0.6)
    st, sh = max(((q / 1000, (fr(q / 1000) - rf) / (q / 1000)) for q in range(90, 320)), key=lambda z: z[1])
    s.line([(X(0), Y(rf)), (X(0.32), Y(rf + sh * 0.32))], YEL, 1.6, 1.2)
    s.dot(X(st), Y(fr(st)), 5, YEL, 1.8)
    s.text("market portfolio", X(st) - 10, Y(fr(st)) - 10, 13, INK, "end", t=1.9)
    return s.svg()


# =====================================================================  CFA guide charts
def _weights(rows, label, title2=None, xmax=None):
    """rows: (topic, lo, hi[, lo2, hi2]) -> horizontal range bars."""
    two = len(rows[0]) == 5
    h = 40 + len(rows) * 30
    s = S(640, h, label)
    xl, x0, x1 = 230, 240, 620
    xmax = xmax or (22 if max(r[-1] for r in rows) <= 20 else 36)
    X = lambda v: x0 + v / xmax * (x1 - x0)
    for v in range(0, xmax + 1, 5):
        s.raw(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="22" y2="{h - 8}" stroke="#222"/>')
        s.text(f"{v}%", X(v), 16, 11, DIM, "middle", cls="")
    for i, r in enumerate(rows):
        y = 34 + i * 30
        s.text(r[0], xl, y + 8, 13, SOFT, "end", cls="")
        if two:
            s.rect(X(r[1]), y - 4, X(r[2]) - X(r[1]), 8, DIM, 0.8, i * 0.05, "gx")
            s.rect(X(r[3]), y + 6, X(r[4]) - X(r[3]), 8, BLUE, 0.95, 0.3 + i * 0.05, "gx")
        else:
            s.rect(X(r[1]), y, X(r[2]) - X(r[1]), 10, BLUE, 0.95, i * 0.05, "gx")
            s.text(f"{r[1]}–{r[2]}%", X(r[2]) + 6, y + 9, 12, INK, t=0.5 + i * 0.05)
    if two:
        s.text("grey: 2026   blue: 2027", x1, h - 2, 12, SOFT, "end", cls="")
    return s.svg()


def weights_l1():
    return _weights([("Ethical & Professional Standards", 15, 20, 10, 15), ("Quantitative Methods", 6, 9, 11, 14), ("Economics", 6, 9, 6, 9),
                     ("Financial Statement Analysis", 11, 14, 11, 14), ("Corporate Issuers / Finance", 6, 9, 6, 9), ("Equity Investments / Equities", 11, 14, 11, 14),
                     ("Fixed Income", 11, 14, 11, 14), ("Derivatives (& Risk Mgmt)", 5, 8, 6, 9), ("Alternative Investments", 7, 10, 6, 9),
                     ("Portfolio Mgmt / Construction", 8, 12, 8, 12)], "Level I topic weight ranges, 2026 against 2027")


def weights_l2():
    return _weights([("Quantitative Methods", 5, 10), ("Economics", 5, 10), ("Financial Statement Analysis", 10, 15), ("Corporate Finance", 5, 10),
                     ("Equities", 10, 15), ("Fixed Income", 10, 15), ("Derivatives & Risk Management", 5, 10), ("Alternative Investments", 5, 10),
                     ("Portfolio Construction", 10, 15), ("Ethical & Professional Standards", 10, 15)], "Level II topic weight ranges")


def weights_l3():
    return _weights([("Asset Allocation", 15, 20), ("Portfolio Construction", 15, 20), ("Performance Measurement", 5, 10),
                     ("Derivatives & Risk Management", 10, 15), ("Ethical & Professional Standards", 10, 15), ("Your pathway", 30, 35)], "Level III topic weight ranges")


def pass_rates():
    s = S(640, 300, "Recent CFA pass rates by level and session")
    x0, y0, x1, y1 = frame(s, "", "pass rate", 50, 250, 624, 30)
    Y = lambda v: y0 - v / 60 * (y0 - y1)
    for v in (20, 40, 60):
        s.raw(f'<line x1="{x0}" x2="{x1}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="#222"/>'); s.text(f"{v}%", x0 - 6, Y(v) + 4, 11, DIM, "end", cls="")
    groups = [("Level I", BLUE, [("Nov 25", 43), ("Feb 26", 45), ("May 26", 39), ("Aug 26", 43)], 41),
              ("Level II", TEAL, [("Nov 25", 42), ("May 26", 43), ("Aug 26", 45)], 46),
              ("Level III", YEL, [("Feb 26", 50), ("Aug 26", 47)], 49)]
    x = x0 + 14; bw = 38; t = 0
    for name, col, bars, avg in groups:
        gx0 = x
        for lab, v in bars:
            s.rect(x, Y(v), bw, y0 - Y(v), col, 0.85, t); s.text(f"{v}%", x + bw / 2, Y(v) - 6, 12, INK, "middle", t=t + 0.6)
            s.text(lab, x + bw / 2, y0 + 15, 11, DIM, "middle", cls=""); x += bw + 8; t += 0.08
        s.line([(gx0 - 4, Y(avg)), (x - 4, Y(avg))], INK, 1.2, t + 0.4, dash="4 3")
        s.text(f"{name} · 5-yr avg {avg}%", (gx0 + x) / 2 - 4, y0 + 32, 12, col, "middle", cls="")
        x += 34
    return s.svg()


def windows():
    s = S(640, 170, "Which months each level can be taken in 2027")
    months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    x0, cw = 120, 42
    for i, m in enumerate(months):
        s.text(m, x0 + i * cw + cw / 2, 22, 12, DIM, "middle", cls="")
    rows = [("Level I", [1, 4, 7, 10], BLUE), ("Level II", [4, 7, 10], TEAL), ("Level III", [1, 7], YEL)]
    for r, (name, ms, col) in enumerate(rows):
        y = 40 + r * 40
        s.text(name, x0 - 12, y + 18, 14, INK, "end", cls="")
        for i in range(12):
            s.raw(f'<rect x="{x0 + i * cw + 2}" y="{y}" width="{cw - 4}" height="26" fill="#111"/>')
        for k, i in enumerate(ms):
            s.rect(x0 + i * cw + 2, y, cw - 4, 26, col, 0.9, r * 0.2 + k * 0.08)
    return s.svg()


# =====================================================================  study blog
def study_plan():
    s = S(640, 190, "A 22-week study plan: learn, practise, then mock exams and review")
    x0, x1 = 30, 610
    W = lambda wk: x0 + wk / 22 * (x1 - x0)
    phases = [(0, 13, "Learn every topic once", BLUE), (13, 17, "Practise by topic", TEAL), (17, 21, "Mocks + error log", YEL), (21, 22, "Rest", DIM)]
    for i, (a, b, lab, col) in enumerate(phases):
        s.rect(W(a) + 1, 60, W(b) - W(a) - 2, 46, col, 0.85 if col != DIM else 0.4, i * 0.25, "gx")
        if b - a > 2:
            s.text(lab, (W(a) + W(b)) / 2, 88, 13, "#000", "middle", t=0.3 + i * 0.25)
    for wk in range(0, 23, 2):
        s.text(str(wk), W(wk), 128, 11, DIM, "middle", cls="")
    s.text("weeks", x1, 148, 12, DIM, "end", True, cls="")
    s.text("about 14 hours a week ≈ 300+ hours", x0, 40, 14, INK, t=0.2)
    return s.svg()


def vignette_flow():
    s = S(640, 170, "Read the questions, then the vignette with purpose, then answer")
    steps = [("1. Questions first", "what is asked?"), ("2. Vignette, with purpose", "mark the inputs"), ("3. Answer in order", "flag and move on"), ("4. Check the clock", "about 3 min per question")]
    for i, (a, b) in enumerate(steps):
        x = 20 + i * 155
        s.box(x, 50, 140, 64, a, BLUE if i != 3 else YEL, size=13, t=i * 0.25, sub=b)
        if i < 3: s.arrow(x + 142, 82, x + 153, 82, DIM, i * 0.25 + 0.2)
    return s.svg()


def command_words():
    s = S(640, 220, "Command words decide how much to write")
    rows = [("List / Identify", "name it: a few words", 1), ("Describe / Explain", "what it is, then why: one or two sentences", 2),
            ("Discuss / Compare", "both sides or similarities and differences", 3), ("Justify / Recommend", "your choice + the reason from the case", 3),
            ("Calculate", "formula, inputs, answer: show the steps", 2)]
    for i, (w, how, n) in enumerate(rows):
        y = 30 + i * 36
        s.text(w, 170, y + 14, 15, INK, "end", cls="")
        s.rect(185, y, n * 60, 20, BLUE, 0.85, i * 0.12, "gx")
        s.text(how, 195 + n * 60, y + 15, 13, SOFT, t=0.4 + i * 0.12)
    return s.svg()


def pacing():
    s = S(640, 300, "Questions answered against minutes: the 90-second pace line with checkpoints at 45, 90 and 135 minutes")
    x0, y0, x1, y1 = frame(s, "minutes into the session", "questions answered", 56, 262, 620, 30)
    X = lambda m: x0 + m / 140 * (x1 - x0); Y = lambda q: y0 - q / 95 * (y0 - y1)
    for q in (30, 60, 90):
        s.text(str(q), x0 - 8, Y(q) + 4, 11, DIM, "end", cls="")
    for m in (45, 90, 135):
        s.text(str(m), X(m), y0 + 16, 11, DIM, "middle", cls="")
    s.line([(X(0), Y(0)), (X(135), Y(90))], BLUE, 2.6, 0.1)
    s.curve(lambda m: 90 * (m / 135) ** 1.35, 0, 135, X, Y, color=RED, width=1.8, t=0.7, opacity=0.8)
    for i, (m, q) in enumerate([(45, 30), (90, 60), (135, 90)]):
        s.line([(X(m), y0), (X(m), Y(q))], RULE, 1, 1.0 + i * 0.2, dash="3 4")
        s.dot(X(m), Y(q), 5, YEL, 1.2 + i * 0.25)
        s.text(f"{q} by {m} min", X(m) - 10, Y(q) - 4, 13, INK, "end", t=1.3 + i * 0.25)
    s.text("on pace: 1.5 min a question", X(70), Y(70) + 4, 13, BLUE, "end", True, t=1.6)
    s.text("too slow early: a rush at the end", X(134), Y(22), 13, RED, "end", True, t=1.9)
    return s.svg()


def pathways():
    s = S(640, 270, "Level III: a 65 to 70 percent core shared by everyone, plus one pathway worth 30 to 35 percent")
    core = [("Asset allocation", 17.5), ("Portfolio construction", 17.5), ("Performance", 7.5), ("Derivatives & risk", 12.5), ("Ethics", 12.5)]
    x, y, k = 20, 40, 600 / 100
    for i, (n, w) in enumerate(core):
        s.rect(x + 1, y, w * k - 2, 46, BLUE, 0.35 + 0.12 * (i % 2), i * 0.18, "gx")
        s.text(n if w > 10 else "Perf.", x + w * k / 2, y + 28, 11 if w > 10 else 11, INK, "middle", t=0.3 + i * 0.18)
        x += w * k
    s.rect(x + 1, y, 32.5 * k - 3, 46, YEL, 0.85, 1.0, "gx")
    s.text("your pathway", x + 32.5 * k / 2, y + 28, 13, "#000", "middle", t=1.3)
    s.text("core: everyone, about two thirds", 20, 26, 13, SOFT, italic=True, t=0.2)
    s.text("about one third", 620, 26, 13, YEL, "end", True, t=1.2)
    cx = x + 32.5 * k / 2
    opts = [("Portfolio Management", "asset managers, index roles", 110), ("Private Markets", "PE, private debt, real assets", 320), ("Private Wealth", "advisers, private banks", 530)]
    for i, (n, sub, bx) in enumerate(opts):
        s.line([(cx, 88), (cx, 130), (bx, 130), (bx, 168)], YEL, 1.6, 1.6 + i * 0.2, opacity=0.8)
        s.box(bx - 95, 170, 190, 58, n, TEAL, size=14, t=2.0 + i * 0.2, sub=sub)
    s.text("same charter at the end of every branch", 320, 258, 13, DIM, "middle", True, t=2.7)
    return s.svg()


def ethics_order():
    s = S(640, 280, "Ethics priority: the market and clients first, then your employer, then yourself; when in doubt, disclose")
    rungs = [("Integrity of the market", "no insider trading, no manipulation", BLUE), ("Clients", "loyalty, suitability, fair dealing", TEAL),
             ("Employer", "loyalty, no competing without consent", BLUEB), ("You", "your trades and interests come last", DIM)]
    for i, (a, b, col) in enumerate(rungs):
        w = 330 - i * 50; x = 30 + i * 30; y = 30 + i * 52
        s.rect(x, y, w, 40, col, 0.8, i * 0.25, "gx")
        s.text(a, x + 12, y + 25, 15, "#000", t=0.3 + i * 0.25)
        s.text(b, x + w + 12, y + 25, 13, SOFT, italic=True, t=0.5 + i * 0.25)
    s.arrow(14, 230, 14, 34, DIM, 1.2)
    s.text("priority", 22, 248, 12, DIM, italic=True, cls="")
    s.box(430, 236, 190, 34, "unsure?  disclose", YEL, size=14, t=1.9, color=YEL)
    return s.svg()


def review_loop():
    s = S(640, 300, "The mock exam loop: sit, review, log the cause, practise the weakness, sit again")
    cx, cy, r = 200, 150, 105
    st = [("Sit the mock", BLUE), ("Review every question", TEAL), ("Log why you missed it", YEL), ("Targeted practice", BLUEB)]
    pts = [(cx + r * math.cos(a), cy + r * math.sin(a)) for a in [-math.pi / 2 + 2 * math.pi * i / 4 for i in range(4)]]
    s.curve(lambda a: a, 0, 2 * math.pi * 0.98, lambda a: cx + r * math.cos(a - math.pi / 2), lambda a: cy + r * math.sin(a - math.pi / 2), n=160, color=DIM, width=1.4, t=0.0)
    for i, ((x, y), (n, col)) in enumerate(zip(pts, st)):
        s.box(x - 78, y - 17, 156, 34, n, col, "#000", 13, 0.4 + i * 0.3)
    # score trend
    gx0, gy0, gx1, gy1 = 400, 262, 625, 50
    s.axes(gx0, gy0, gx1, gy1, "mock", "score")
    Y = lambda v: gy0 - (v - 40) / 45 * (gy0 - gy1)
    s.rect(gx0 + 1, Y(85), gx1 - gx0 - 1, Y(70) - Y(85), TEAL, 0.12, 0.2, "f")
    s.text("70%+ zone", gx1 - 4, Y(85) + 14, 12, TEAL, "end", True, t=0.4)
    sc = [52, 58, 63, 66, 71, 74]
    P = [(gx0 + 20 + i * 38, Y(v)) for i, v in enumerate(sc)]
    s.line(P, YEL, 2.2, 1.0)
    for i, (x, y) in enumerate(P):
        s.dot(x, y, 4, YEL, 1.1 + i * 0.15)
        s.text(str(i + 1), x, gy0 + 15, 11, DIM, "middle", cls="")
    return s.svg()


def gap_match():
    s = S(640, 290, "Match the resource to the gap: what you lack decides what you buy")
    gaps = ["I get lost in the reading", "I understand but am slow", "I forget by exam day", "I don't know my weak spots", "I can't keep going"]
    fix = ["video lectures", "question bank", "condensed notes", "full mocks + error log", "planner or study group"]
    order = [0, 1, 2, 3, 4]
    for i, g in enumerate(gaps):
        y = 36 + i * 52
        s.box(20, y, 230, 36, g, BLUE, size=13, t=i * 0.15)
    for i, f in enumerate(fix):
        y = 36 + i * 52
        s.box(420, y, 200, 36, f, TEAL, size=13, t=0.9 + i * 0.15)
    for i, j in enumerate(order):
        s.arrow(254, 54 + i * 52, 414, 54 + j * 52, YEL, 0.5 + i * 0.15, 1.6)
    s.text("your gap", 135, 22, 13, DIM, "middle", True, cls="")
    s.text("what to look for", 520, 22, 13, DIM, "middle", True, cls="")
    return s.svg()


def exam_day():
    s = S(640, 200, "Exam day timeline: arrive early, check in, session one, optional break, session two")
    blocks = [("arrive", 30, DIM), ("ID", 20, BLUEB), ("session 1", 135, BLUE), ("break", 30, TEAL), ("session 2", 135, BLUE)]
    tot = sum(b[1] for b in blocks); x = 20; k = 600 / tot; t = 0
    for i, (n, m, col) in enumerate(blocks):
        s.rect(x + 1, 70, m * k - 2, 48, col, 0.85 if col == BLUE else 0.55, i * 0.3, "gx")
        s.text(n, x + m * k / 2, 99, 13, "#000" if col != DIM else INK, "middle", t=0.2 + i * 0.3)
        s.text(f"{m} min" if n != "ID" else "20 min", x + m * k / 2, 138, 11, DIM, "middle", t=0.3 + i * 0.3)
        x += m * k
    s.text("the clock never stops inside a session", 20 + (50 + 67) * k, 50, 13, YEL, "middle", True, t=1.6)
    s.text("about 2¼ hours", 20 + (50 + 67.5) * k, 170, 12, SOFT, "middle", True, t=1.0)
    s.text("about 2¼ hours", 20 + (215 + 67.5) * k, 170, 12, SOFT, "middle", True, t=1.4)
    return s.svg()


def forgetting():
    s = S(640, 290, "Memorised facts fade fast and need re-cramming before each level; understood ideas fade slowly")
    x0, y0, x1, y1 = frame(s, "months", "what you still know", 50, 250, 620, 34)
    X = lambda m: x0 + m / 30 * (x1 - x0); Y = lambda v: y0 - v * (y0 - y1)
    def mem(m):
        last = max(c for c in (0, 10, 20) if c <= m)
        return 0.95 * math.exp(-(m - last) / 2.5) + 0.05
    s.curve(mem, 0, 29.9, X, Y, n=300, color=RED, width=2, t=0.2, opacity=0.9)
    s.curve(lambda m: 0.95 * (0.55 + 0.45 * math.exp(-m / 8)) + 0.04 * min(m, 30) / 30, 0, 30, X, Y, n=200, color=BLUE, width=2.6, t=0.9)
    for i, (m, lab) in enumerate([(10, "Level II"), (20, "Level III")]):
        s.line([(X(m), y0), (X(m), y1)], RULE, 1, 1.4 + i * 0.2, dash="3 4")
        s.text(lab, X(m) + 4, y1 + 12, 12, DIM, italic=True, t=1.5 + i * 0.2)
    s.text("memorised: re-learn each time", X(3.2), Y(0.22), 13, RED, italic=True, t=1.2)
    s.text("understood: stays, and builds", x1, Y(0.66), 13, BLUE, "end", True, t=1.9)
    return s.svg()


# =====================================================================  prerequisites: financial statement analysis
def qualities():
    s = S(640, 250, "Two fundamental qualities with four enhancing ones beneath")
    s.box(110, 30, 200, 60, "Relevance", BLUE, size=16, t=0, sub="could change a decision")
    s.box(330, 30, 200, 60, "Faithful representation", BLUE, size=16, t=0.2, sub="complete, neutral, error-free")
    for i, w in enumerate(["Comparability", "Verifiability", "Timeliness", "Understandability"]):
        s.box(20 + i * 152, 150, 140, 44, w, TEAL, size=14, t=0.6 + i * 0.12)
    s.text("fundamental", 320, 20, 13, DIM, "middle", True, cls="")
    s.text("enhancing", 320, 140, 13, DIM, "middle", True, t=0.5)
    s.text("limited by cost: information must be worth more than it costs to produce", 320, 225, 13, SOFT, "middle", True, t=1.2)
    return s.svg()


def three_statements():
    s = S(640, 270, "How the income statement, balance sheet and cash flow statement connect")
    s.box(30, 40, 170, 70, "Income statement", BLUE, size=15, sub="performance over a period")
    s.box(235, 40, 170, 70, "Retained earnings", TEAL, size=15, t=0.3, sub="+ profit − dividends")
    s.box(440, 40, 170, 70, "Balance sheet", BLUE, size=15, t=0.6, sub="position at a date")
    s.box(440, 170, 170, 70, "Cash flow statement", YEL, size=15, t=0.9, sub="why cash changed")
    s.arrow(200, 75, 233, 75, INK, 0.2); s.text("net income", 216, 66, 12, SOFT, "middle", True, t=0.3)
    s.arrow(405, 75, 438, 75, INK, 0.5); s.text("equity", 421, 66, 12, SOFT, "middle", True, t=0.6)
    s.arrow(525, 168, 525, 112, INK, 1.0); s.text("ending cash", 532, 145, 12, SOFT, italic=True, t=1.1)
    s.arrow(115, 112, 438, 200, DIM, 1.2); s.text("starts from net income (indirect method)", 210, 190, 12, SOFT, italic=True, t=1.3)
    return s.svg()


def accruals():
    s = S(640, 260, "Cash before or after the revenue or expense is earned or incurred")
    s.raw(f'<line x1="320" y1="40" x2="320" y2="230" stroke="{RULE}"/><line x1="60" y1="135" x2="600" y2="135" stroke="{RULE}"/>')
    s.text("cash comes first", 190, 30, 13, DIM, "middle", True, cls=""); s.text("cash comes later", 460, 30, 13, DIM, "middle", True, cls="")
    s.text("revenue", 50, 90, 13, DIM, "end", True, cls=""); s.text("expense", 50, 190, 13, DIM, "end", True, cls="")
    cells = [(190, 90, "Unearned revenue", "a liability until delivered", BLUE), (460, 90, "Accrued revenue", "a receivable", BLUE),
             (190, 190, "Prepaid expense", "an asset until used", TEAL), (460, 190, "Accrued expense", "a liability (owed)", TEAL)]
    for i, (x, y, a, b, c) in enumerate(cells):
        s.text(a, x, y - 4, 17, c, "middle", t=i * 0.2); s.text(b, x, y + 18, 13, SOFT, "middle", True, t=i * 0.2 + 0.1)
    return s.svg()


def five_steps():
    s = S(640, 170, "The five steps of revenue recognition")
    steps = ["Identify the contract", "Find the promises", "Set the price", "Allocate the price", "Recognise when delivered"]
    for i, w in enumerate(steps):
        x = 10 + i * 126
        s.box(x, 50, 116, 70, "", BLUE if i < 4 else YEL, t=i * 0.2)
        s.text(str(i + 1), x + 58, 78, 20, BLUE if i < 4 else YEL, "middle", t=i * 0.2)
        words = w.split(" ", 1)
        s.text(words[0] + " " + (words[1].split(" ")[0] if len(words) > 1 else ""), x + 58, 98, 12, INK, "middle", t=i * 0.2)
        rest = " ".join(w.split(" ")[2:])
        if rest: s.text(rest, x + 58, 112, 12, INK, "middle", t=i * 0.2)
    return s.svg()


def allowance():
    s = S(640, 250, "Gross receivables reduced by an allowance for doubtful accounts")
    x0, y0, x1, y1 = frame(s, "", "", 60, 220, 600, 30)
    s.rect(110, 60, 120, 160, BLUE, 0.85, 0); s.text("Gross receivables 1,000", 170, 50, 13, INK, "middle", t=0.2)
    s.rect(290, 60, 120, 30, RED, 0.8, 0.4); s.text("Allowance 30", 350, 50, 13, INK, "middle", t=0.6)
    s.rect(290, 90, 120, 130, TEAL, 0.85, 0.7); s.text("Net 970", 350, 160, 15, "#000", "middle", t=1)
    s.text("expense booked now, in the period of the sale,", 450, 120, 13, SOFT, italic=True, t=1.2)
    s.text("not later, when a customer defaults", 450, 140, 13, SOFT, italic=True, t=1.3)
    return s.svg()


def income_layers():
    s = S(640, 280, "An income statement in layers, from revenue to net income")
    rows = [("Revenue", 100, BLUE), ("− Cost of sales", -55, DIM), ("= Gross profit", 45, TEAL), ("− Operating expenses", -25, DIM), ("= Operating profit", 20, TEAL),
            ("± Non-operating (interest, investment gains)", -4, DIM), ("− Tax", -4, DIM), ("= Profit from continuing operations", 12, BLUE), ("± Discontinued operations, net of tax", 3, YEL)]
    for i, (lab, v, c) in enumerate(rows):
        y = 26 + i * 27
        s.text(lab, 330, y + 13, 13, INK if c != DIM else SOFT, "end", cls="")
        s.rect(345, y, abs(v) * 2.6, 16, c, 0.85, i * 0.1, "gx")
    s.text("separate line, below continuing profit", 345 + 3 * 2.6 + 10, 26 + 8 * 27 + 13, 12, YEL, italic=True, t=1.2)
    return s.svg()


def common_size():
    s = S(640, 270, "Two companies' income statements as percentages of revenue")
    a = [("Cost of sales", 62, DIM), ("Operating expenses", 20, BLUE), ("Interest", 3, RED), ("Tax", 4, TEAL), ("Net income", 11, YEL)]
    b = [("Cost of sales", 45, DIM), ("Operating expenses", 38, BLUE), ("Interest", 2, RED), ("Tax", 4, TEAL), ("Net income", 11, YEL)]
    for j, (name, rows) in enumerate([("Company A (revenue 50m)", a), ("Company B (revenue 900m)", b)]):
        y = 50 + j * 100; x = 40
        s.text(name, 40, y - 10, 14, INK, cls="")
        for i, (lab, v, c) in enumerate(rows):
            w = v * 5.6; s.rect(x, y, w, 40, c, 0.85, j * 0.4 + i * 0.1, "gx")
            if v >= 4: s.text(f"{v}%", x + w / 2, y + 25, 13, "#000", "middle", t=j * 0.4 + i * 0.1 + 0.4)
            x += w
    s.text("same 11% margin, very different cost structures", 320, 260, 13, SOFT, "middle", True, t=1.3)
    return s.svg()


def oci_streams():
    s = S(640, 240, "Net income and other comprehensive income both flow into equity")
    s.box(30, 40, 220, 60, "Net income", BLUE, size=16, sub="through the income statement")
    s.box(30, 140, 220, 60, "Other comprehensive income", TEAL, size=15, t=0.3, sub="straight to equity (reserves)")
    s.box(400, 85, 210, 70, "Total comprehensive income", YEL, size=15, t=0.8, sub="all non-owner changes in equity")
    s.arrow(252, 70, 398, 110, INK, 0.5); s.arrow(252, 170, 398, 130, INK, 0.7)
    return s.svg()


def bs_block():
    s = S(640, 280, "A balance sheet: assets equal liabilities plus equity, split into current and non-current")
    s.text("Assets", 165, 26, 15, INK, "middle", cls=""); s.text("Liabilities + equity", 475, 26, 15, INK, "middle", cls="")
    s.rect(60, 40, 210, 80, BLUE, 0.9, 0); s.text("Current assets", 165, 76, 14, "#000", "middle", t=0.3); s.text("cash, receivables, inventory", 165, 95, 12, "#000", "middle", True, t=0.3)
    s.rect(60, 120, 210, 140, BLUE, 0.55, 0.2); s.text("Non-current assets", 165, 186, 14, "#000", "middle", t=0.5); s.text("PP&E, intangibles", 165, 205, 12, "#000", "middle", True, t=0.5)
    s.rect(370, 40, 210, 60, TEAL, 0.9, 0.4); s.text("Current liabilities", 475, 74, 14, "#000", "middle", t=0.7)
    s.rect(370, 100, 210, 80, TEAL, 0.55, 0.5); s.text("Non-current liabilities", 475, 144, 14, "#000", "middle", t=0.8)
    s.rect(370, 180, 210, 80, YEL, 0.85, 0.6); s.text("Equity", 475, 224, 15, "#000", "middle", t=1.0)
    s.text("=", 320, 160, 30, INK, "middle", t=0.9)
    s.text("current = within 12 months or one operating cycle", 320, 278, 12, SOFT, "middle", True, t=1.2)
    return s.svg()


def equity_roll():
    s = S(640, 250, "Statement of changes in equity: opening balance to closing balance")
    x0, y0 = 40, 210
    items = [("Opening", 500, 0, BLUE), ("+ Net income", 80, 500, TEAL), ("+ OCI", 15, 580, TEAL), ("+ Shares issued", 40, 595, TEAL), ("− Dividends", -30, 635, RED), ("− Buybacks", -25, 605, RED), ("Closing", 580, 0, YEL)]
    k = 0.28; w = 70
    for i, (lab, v, base, c) in enumerate(items):
        x = x0 + i * 82
        lo, hi = (base, base + v) if v > 0 else (base + v, base)
        if lab in ("Opening", "Closing"): lo, hi = 0, v
        s.rect(x, y0 - hi * k, w, (hi - lo) * k, c, 0.85, i * 0.15)
        s.text(lab, x + w / 2, y0 + 18, 12, SOFT, "middle", cls="")
        s.text(f"{abs(v) if lab not in ('Opening','Closing') else v}", x + w / 2, y0 - hi * k - 6, 12, INK, "middle", t=i * 0.15 + 0.3)
    return s.svg()


def cf_buckets():
    s = S(640, 260, "Operating, investing and financing cash flows, with the interest and dividend choices")
    cols = [("Operating", "day-to-day business", BLUE), ("Investing", "long-term assets, investments", TEAL), ("Financing", "debt and equity holders", YEL)]
    for i, (a, b, c) in enumerate(cols):
        x = 20 + i * 207
        s.box(x, 20, 190, 56, a, c, size=17, t=i * 0.15, sub=b)
    rows = [("Interest paid", "O or F", "O"), ("Interest received", "O or I", "O"), ("Dividends received", "O or I", "O"), ("Dividends paid", "O or F", "F")]
    s.text("IFRS", 430, 110, 13, BLUE, "middle", cls=""); s.text("US GAAP", 560, 110, 13, TEAL, "middle", cls="")
    for i, (a, ifrs, gaap) in enumerate(rows):
        y = 140 + i * 28
        s.text(a, 330, y, 14, INK, "end", t=0.5 + i * 0.1); s.text(ifrs, 430, y, 14, SOFT, "middle", t=0.6 + i * 0.1); s.text(gaap, 560, y, 14, SOFT, "middle", t=0.6 + i * 0.1)
    return s.svg()


def cfo_waterfall():
    s = S(640, 280, "Indirect method: from net income to cash from operations")
    x0, y0 = 40, 240
    items = [("Net income", 100, None, BLUE), ("+ Depreciation", 40, 100, TEAL), ("− Gain on sale", -10, 140, RED), ("− ↑ Receivables", -25, 130, RED), ("− ↑ Inventory", -15, 105, RED), ("+ ↑ Payables", 20, 90, TEAL), ("= CFO", 110, None, YEL)]
    k = 1.35; w = 70
    for i, (lab, v, base, c) in enumerate(items):
        x = x0 + i * 82
        if base is None: lo, hi = 0, v
        else: lo, hi = (base, base + v) if v > 0 else (base + v, base)
        s.rect(x, y0 - hi * k, w, (hi - lo) * k, c, 0.85, i * 0.15)
        s.text(lab, x + w / 2, y0 + 18, 11, SOFT, "middle", cls="")
        s.text(f"{v:+d}" if base is not None else str(v), x + w / 2, y0 - hi * k - 6, 12, INK, "middle", t=i * 0.15 + 0.3)
    return s.svg()


def inventory_cost():
    s = S(640, 240, "Costs that go into inventory and costs that are expensed immediately")
    s.text("Into inventory (an asset until sold)", 160, 30, 15, BLUE, "middle", cls="")
    s.text("Expensed when incurred", 480, 30, 15, RED, "middle", cls="")
    a = ["purchase price, import duties", "freight to get it in", "conversion: labour, overheads", "storage needed in production"]
    b = ["abnormal waste", "storage of finished goods", "admin overheads", "selling costs"]
    for i, w in enumerate(a): s.text("• " + w, 40, 70 + i * 30, 14, INK, t=i * 0.15)
    for i, w in enumerate(b): s.text("• " + w, 360, 70 + i * 30, 14, SOFT, t=0.4 + i * 0.15)
    s.text("test: was the cost needed to get the goods to where and how they are sold?", 320, 215, 13, SOFT, "middle", True, t=1.2)
    return s.svg()


def lifo_reserve():
    s = S(640, 250, "LIFO inventory plus the LIFO reserve equals FIFO inventory")
    x0, y0 = 120, 210; k = 0.12
    s.rect(x0, y0 - 600 * k, 110, 600 * k, BLUE, 0.85, 0); s.text("LIFO inventory 600", x0 + 55, y0 + 20, 13, SOFT, "middle", cls="")
    s.rect(x0 + 170, y0 - 600 * k, 110, 600 * k, BLUE, 0.85, 0.3)
    s.rect(x0 + 170, y0 - 1000 * k, 110, 400 * k, YEL, 0.85, 0.6); s.text("LIFO reserve 400", x0 + 225, y0 - 1000 * k - 8, 13, YEL, "middle", t=0.9)
    s.text("FIFO inventory 1,000", x0 + 225, y0 + 20, 13, SOFT, "middle", cls="")
    s.text("ΔLIFO reserve = how much more", 470, 110, 13, INK, t=1.1); s.text("LIFO put into cost of sales", 470, 128, 13, INK, t=1.1)
    return s.svg()


def writedown():
    s = S(640, 250, "Inventory carried at the lower of cost and net realisable value")
    x0, y0, x1, y1 = frame(s, "quarter", "value per unit", 50, 210, 600, 30)
    X = lambda t: x0 + t / 4 * (x1 - x0); Y = lambda v: y0 - v / 120 * (y0 - y1)
    nrv = [(0, 110), (1, 104), (2, 82), (3, 88), (4, 106)]
    s.line([(X(0), Y(100)), (X(4), Y(100))], DIM, 1.4, dash="5 4"); s.text("cost 100", X(4), Y(100) - 8, 12, DIM, "end", True, cls="")
    s.line([(X(a), Y(b)) for a, b in nrv], TEAL, 2, 0.2); s.text("net realisable value", X(1) + 4, Y(104) - 10, 12, TEAL, italic=True, t=0.6)
    carry = [(0, 100), (1, 100), (2, 82), (3, 88), (4, 100)]
    s.line([(X(a), Y(b)) for a, b in carry], YEL, 3, 0.6)
    s.text("write-down", X(2) + 6, Y(82) + 18, 12, YEL, italic=True, t=1.2)
    s.text("IFRS: reversal allowed, never above cost", X(3.05), Y(88) + 30, 12, SOFT, italic=True, t=1.4)
    return s.svg()


def inventory_cycle():
    s = S(640, 220, "Days of inventory on hand as one leg of the operating cycle")
    s.rect(40, 90, 260, 40, BLUE, 0.85, 0, "gx"); s.text("days inventory on hand = 365 / turnover", 170, 80, 13, BLUE, "middle", t=0.3)
    s.rect(300, 90, 180, 40, TEAL, 0.85, 0.3, "gx"); s.text("days sales outstanding", 390, 80, 13, TEAL, "middle", t=0.6)
    s.rect(40, 150, 200, 30, RED, 0.6, 0.6, "gx"); s.text("days payables outstanding", 140, 200, 13, RED, "middle", t=0.9)
    s.text("turnover = cost of sales / average inventory", 320, 30, 15, INK, "middle", cls="")
    s.text("cash tied up", 560, 115, 13, YEL, "middle", True, t=1.2)
    return s.svg()


def capitalise():
    s = S(640, 260, "Profit path when a cost is capitalised versus expensed")
    x0, y0, x1, y1 = frame(s, "year", "reported profit", 50, 220, 600, 30)
    X = lambda t: x0 + (t + 0.5) / 5 * (x1 - x0); Y = lambda v: y0 - (v - 40) / 90 * (y0 - y1)
    exp = [(0, 50), (1, 100), (2, 100), (3, 100), (4, 100)]
    cap = [(0, 90), (1, 90), (2, 90), (3, 90), (4, 90)]
    s.line([(X(a), Y(b)) for a, b in exp], RED, 2.4, 0); s.text("expensed: big hit in year 1", X(1.1), Y(108), 13, RED, italic=True, t=0.6)
    s.line([(X(a), Y(b)) for a, b in cap], TEAL, 2.4, 0.4); s.text("capitalised: smoothed by depreciation", X(1.6), Y(82), 13, TEAL, italic=True, t=1)
    for t in range(5): s.text(str(t + 1), X(t), y0 + 16, 12, DIM, "middle", cls="")
    return s.svg()


def revaluation():
    s = S(640, 260, "Cost model versus revaluation model for the same building")
    x0, y0, x1, y1 = frame(s, "year", "carrying amount", 50, 220, 600, 30)
    X = lambda t: x0 + t / 5 * (x1 - x0); Y = lambda v: y0 - v / 1400 * (y0 - y1)
    cost = [(t, 1000 - 100 * t) for t in range(6)]
    rev = [(0, 1000), (1, 900), (2, 1150), (3, 1035), (4, 920), (5, 805)]
    s.line([(X(a), Y(b)) for a, b in cost], DIM, 2, 0); s.text("cost model", X(5), Y(500) + 18, 13, DIM, "end", True, t=0.6)
    s.line([(X(a), Y(b)) for a, b in rev], BLUE, 2.6, 0.4); s.text("revaluation model (IFRS only)", X(2), Y(1150) - 10, 13, BLUE, italic=True, t=1)
    s.text("gain above cost → OCI (revaluation surplus)", X(2.1), Y(1150) + 26, 12, YEL, italic=True, t=1.3)
    return s.svg()


def deferred_tax():
    s = S(640, 270, "Faster tax depreciation creates a deferred tax liability that reverses")
    x0, y0, x1, y1 = frame(s, "year", "depreciation", 50, 230, 600, 30)
    book = [300] * 4; tax = [480, 360, 240, 120]
    step = (x1 - x0) / 4
    for t in range(4):
        x = x0 + t * step + 20
        s.rect(x, y0 - book[t] * 0.33, 40, book[t] * 0.33, BLUE, 0.85, t * 0.1)
        s.rect(x + 46, y0 - tax[t] * 0.33, 40, tax[t] * 0.33, TEAL, 0.85, 0.3 + t * 0.1)
        s.text(str(t + 1), x + 43, y0 + 16, 12, DIM, "middle", cls="")
        d = tax[t] - book[t]
        s.text(("DTL +" if d > 0 else "DTL −") + str(abs(d) * 25 // 100), x + 43, y0 - max(book[t], tax[t]) * 0.33 - 8, 12, YEL, "middle", t=0.8 + t * 0.1)
    s.text("blue: books   teal: tax return   (25% tax rate)", x1, y1, 13, SOFT, "end", cls="")
    return s.svg()


def valuation_allowance():
    s = S(640, 240, "A deferred tax asset reduced by a valuation allowance and by a lower tax rate")
    x0, y0 = 60, 200
    bars = [("DTA at 30%", 300, BLUE), ("rate cut to 25%", 250, TEAL), ("allowance: half unlikely", 125, YEL)]
    for i, (lab, v, c) in enumerate(bars):
        x = x0 + i * 190
        s.rect(x, y0 - v * 0.5, 110, v * 0.5, c, 0.85, i * 0.3)
        s.text(lab, x + 55, y0 + 20, 13, SOFT, "middle", cls=""); s.text(str(v), x + 55, y0 - v * 0.5 - 8, 14, INK, "middle", t=i * 0.3 + 0.4)
    s.arrow(175, 120, 245, 120, DIM, 0.4); s.arrow(365, 120, 435, 120, DIM, 0.7)
    return s.svg()


def derecognition():
    s = S(640, 230, "Repaying debt early: carrying amount versus cash paid")
    s.rect(80, 60, 160, 120, BLUE, 0.85, 0); s.text("carrying amount 960", 160, 50, 13, INK, "middle", t=0.2)
    s.rect(330, 50, 160, 130, TEAL, 0.85, 0.3); s.text("paid to bondholders 990", 410, 40, 13, INK, "middle", t=0.5)
    s.text("loss on extinguishment = 960 − 990 = −30", 320, 215, 15, YEL, "middle", t=0.9)
    return s.svg()


def credit_ratios():
    s = S(640, 250, "Two credit ratios for three companies")
    rows = [("A", 12, 1.0), ("B", 5, 2.5), ("C", 1.8, 5.5)]
    s.text("Interest coverage (EBIT / interest)", 160, 30, 14, INK, "middle", cls=""); s.text("Leverage (debt / EBITDA)", 480, 30, 14, INK, "middle", cls="")
    for i, (n, cov, lev) in enumerate(rows):
        y = 60 + i * 55
        s.text(n, 30, y + 22, 16, INK, cls="")
        s.rect(50, y, cov * 20, 30, TEAL if cov > 4 else RED, 0.85, i * 0.15, "gx"); s.text(f"{cov}×", 58 + cov * 20, y + 20, 13, INK, t=0.5)
        s.rect(360, y, lev * 40, 30, TEAL if lev < 3 else RED, 0.85, 0.4 + i * 0.15, "gx"); s.text(f"{lev}×", 368 + lev * 40, y + 20, 13, INK, t=0.9)
    s.text("higher coverage and lower leverage = more room before default", 320, 235, 13, SOFT, "middle", True, t=1.2)
    return s.svg()


def adjustments():
    s = S(640, 250, "Analyst adjustments that make two companies comparable")
    rows = [("LIFO user?", "add the LIFO reserve to inventory and equity"), ("Goodwill?", "strip it out of assets and equity for tangible ratios"),
            ("Investments in different buckets?", "put them on the same measurement basis"), ("Old, heavily depreciated PP&E?", "check average age: capital spending may be due")]
    for i, (a, b) in enumerate(rows):
        y = 40 + i * 50
        s.text(a, 250, y + 6, 15, INK, "end", t=i * 0.2)
        s.arrow(262, y + 1, 300, y + 1, DIM, i * 0.2 + 0.1)
        s.text(b, 310, y + 6, 14, SOFT, t=i * 0.2 + 0.2)
    return s.svg()


# =====================================================================  prerequisites: economics
def _demand_axes(s, xl="quantity", yl="price"):
    return frame(s, xl, yl, 50, s.h - 36, s.w - 20, 30)


def elasticity_quadrants():
    s = S(640, 250, "Signs of income and cross-price elasticity")
    s.text("Income elasticity", 160, 30, 16, INK, "middle", cls=""); s.text("Cross-price elasticity", 480, 30, 16, INK, "middle", cls="")
    items = [(160, 80, "> 1  luxury", BLUE), (160, 120, "0 to 1  necessity", BLUE), (160, 160, "< 0  inferior good", RED),
             (480, 90, "> 0  substitutes", TEAL), (480, 130, "(tea and coffee)", DIM), (480, 170, "< 0  complements", YEL), (480, 210, "(printers and ink)", DIM)]
    for i, (x, y, w, c) in enumerate(items): s.text(w, x, y, 15, c, "middle", t=i * 0.12)
    return s.svg()


def sub_income():
    s = S(640, 220, "A price fall split into a substitution effect and an income effect")
    s.box(30, 80, 160, 60, "Price falls", YEL, size=16)
    s.box(250, 30, 200, 60, "Substitution effect", BLUE, size=15, t=0.4, sub="relatively cheaper: buy more")
    s.box(250, 130, 200, 60, "Income effect", TEAL, size=15, t=0.7, sub="feel richer: normal ↑, inferior ↓")
    s.box(510, 80, 110, 60, "Total", INK, size=16, t=1.1)
    s.arrow(192, 100, 248, 62, DIM, 0.3); s.arrow(192, 120, 248, 158, DIM, 0.6); s.arrow(452, 62, 508, 100, DIM, 0.9); s.arrow(452, 158, 508, 120, DIM, 1.0)
    return s.svg()


def marginal_returns():
    s = S(640, 270, "Total product rises at a slowing rate as marginal product falls")
    x0, y0, x1, y1 = frame(s, "workers", "output", 50, 230, 610, 30)
    X = lambda l: x0 + l / 10 * (x1 - x0); Y = lambda q: y0 - q / 110 * (y0 - y1)
    tp = lambda l: 100 * (1 - math.exp(-0.32 * l)) + 6 * l * math.exp(-0.5 * l)
    s.curve(tp, 0, 10, X, Y, color=BLUE, width=2.6); s.text("total product", X(8.5), Y(tp(8.5)) - 10, 13, BLUE, italic=True, t=1)
    mp = lambda l: (tp(l + 0.01) - tp(l)) / 0.01 * 3
    s.curve(mp, 0.3, 10, X, Y, color=YEL, width=2, t=0.5); s.text("marginal product (scaled)", X(3.2), Y(mp(3.2)) + 4, 13, YEL, italic=True, t=1.3)
    return s.svg()


def cost_curves():
    s = S(640, 290, "Average total, average variable and marginal cost curves")
    x0, y0, x1, y1 = frame(s, "output", "cost per unit", 50, 250, 610, 30)
    X = lambda q: x0 + q / 10 * (x1 - x0); Y = lambda c: y0 - c / 30 * (y0 - y1)
    FC = 20; vc = lambda q: 6 * q - 1.0 * q * q + 0.09 * q ** 3
    mc = lambda q: 6 - 2.0 * q + 0.27 * q * q
    avc = lambda q: vc(q) / q; atc = lambda q: (vc(q) + FC) / q
    s.curve(atc, 1.1, 10, X, Y, color=BLUE, width=2.4); s.text("ATC", X(1.3), Y(atc(1.3)) - 6, 13, BLUE, t=0.8)
    s.curve(avc, 0.3, 10, X, Y, color=TEAL, width=2.4, t=0.3); s.text("AVC", X(9.6), Y(avc(9.6)) + 16, 13, TEAL, t=1)
    s.curve(mc, 0.3, 10, X, Y, color=YEL, width=2.4, t=0.6); s.text("MC", X(9.4), Y(mc(9.4)), 13, YEL, t=1.2)
    qa = min((q / 100 for q in range(100, 1000)), key=lambda q: atc(q)); qv = min((q / 100 for q in range(30, 1000)), key=lambda q: avc(q))
    s.dot(X(qa), Y(atc(qa)), 4, INK, 1.4); s.dot(X(qv), Y(avc(qv)), 4, INK, 1.4)
    s.text("MC cuts both at their lowest points", X(5.5), Y(27), 13, SOFT, italic=True, t=1.6)
    return s.svg()


def shutdown():
    s = S(640, 290, "Breakeven and shutdown prices for a firm in perfect competition")
    x0, y0, x1, y1 = frame(s, "output", "price / cost", 50, 250, 610, 30)
    X = lambda q: x0 + q / 10 * (x1 - x0); Y = lambda c: y0 - c / 30 * (y0 - y1)
    FC = 20; vc = lambda q: 6 * q - 1.0 * q * q + 0.09 * q ** 3; mc = lambda q: 6 - 2.0 * q + 0.27 * q * q
    avc = lambda q: vc(q) / q; atc = lambda q: (vc(q) + FC) / q
    s.curve(atc, 1.1, 10, X, Y, color=BLUE, width=2); s.curve(avc, 0.3, 10, X, Y, color=TEAL, width=2, t=0.2); s.curve(mc, 0.3, 10, X, Y, color=INK, width=2, t=0.4)
    pa = min(atc(q / 100) for q in range(100, 1000)); pv = min(avc(q / 100) for q in range(30, 1000))
    s.line([(x0, Y(pa)), (x1, Y(pa))], YEL, 1.4, 0.8, dash="5 4"); s.text("breakeven: P = min ATC", x1, Y(pa) - 6, 13, YEL, "end", t=1)
    s.line([(x0, Y(pv)), (x1, Y(pv))], RED, 1.4, 1.0, dash="5 4"); s.text("shutdown: P < min AVC", x1, Y(pv) + 16, 13, RED, "end", t=1.2)
    s.text("between the lines: keep producing in the short run, losses shrink", x0 + 10, y1 + 4, 13, SOFT, italic=True, t=1.4)
    return s.svg()


def market_spectrum():
    s = S(640, 210, "Four market structures from many sellers to one")
    names = [("Perfect competition", "many sellers, identical product"), ("Monopolistic competition", "many sellers, differentiated"), ("Oligopoly", "few sellers, interdependent"), ("Monopoly", "one seller, high barriers")]
    s.line([(40, 120), (600, 120)], DIM, 1.4)
    for i, (a, b) in enumerate(names):
        x = 40 + i * 186.6
        s.dot(x, 120, 7, [TEAL, BLUE, BLUE, YEL][i], i * 0.25)
        s.text(a, x, 95 if i % 2 == 0 else 160, 14, INK, "middle" if 0 < i < 3 else ("start" if i == 0 else "end"), t=i * 0.25)
        s.text(b, x, 113 if i % 2 == 0 else 178, 12, SOFT, "middle" if 0 < i < 3 else ("start" if i == 0 else "end"), True, t=i * 0.25)
    s.text("pricing power rises →", 600, 40, 13, DIM, "end", True, cls="")
    return s.svg()


def perfect_competition():
    s = S(640, 270, "Long-run equilibrium in perfect competition: price equals minimum average cost")
    x0, y0, x1, y1 = frame(s, "firm output", "price", 50, 230, 610, 30)
    X = lambda q: x0 + q / 10 * (x1 - x0); Y = lambda c: y0 - c / 30 * (y0 - y1)
    FC = 20; vc = lambda q: 6 * q - 1.0 * q * q + 0.09 * q ** 3; mc = lambda q: 6 - 2.0 * q + 0.27 * q * q; atc = lambda q: (vc(q) + FC) / q
    s.curve(atc, 1.1, 10, X, Y, color=BLUE, width=2.2); s.curve(mc, 0.6, 10, X, Y, color=INK, width=2, t=0.3)
    qa = min((q / 100 for q in range(100, 1000)), key=lambda q: atc(q)); pa = atc(qa)
    s.line([(x0, Y(pa)), (x1, Y(pa))], YEL, 2, 0.6); s.text("P = MR = MC = min ATC", x1, Y(pa) - 8, 13, YEL, "end", t=1)
    s.dot(X(qa), Y(pa), 5, YEL, 1.1)
    s.text("zero economic profit: entry and exit stop", x0 + 10, y1 + 4, 13, SOFT, italic=True, t=1.3)
    return s.svg()


def monopoly():
    s = S(640, 290, "Monopoly: output where marginal revenue equals marginal cost, price read from demand")
    x0, y0, x1, y1 = frame(s, "quantity", "price", 50, 250, 610, 30)
    X = lambda q: x0 + q / 100 * (x1 - x0); Y = lambda p: y0 - p / 100 * (y0 - y1)
    s.line([(X(0), Y(100)), (X(100), Y(0))], BLUE, 2.4); s.text("demand", X(70), Y(30) - 10, 13, BLUE, italic=True, t=0.8)
    s.line([(X(0), Y(100)), (X(50), Y(0))], TEAL, 2.2, 0.3); s.text("MR", X(46), Y(8), 13, TEAL, t=0.9)
    s.line([(X(0), Y(20)), (X(100), Y(20))], INK, 1.6, 0.5); s.text("MC", X(100), Y(20) - 6, 13, INK, "end", t=1)
    qm, pm = 40, 60
    s.raw(f'<path class="f" style="--t:1.2s" d="M{X(qm):.1f},{Y(pm):.1f} L{X(80):.1f},{Y(20):.1f} L{X(qm):.1f},{Y(20):.1f} Z" fill="{RED}" fill-opacity="0.35"/>')
    s.line([(X(qm), Y(0)), (X(qm), Y(pm)), (X(0), Y(pm))], YEL, 1.4, 1.0, dash="4 4"); s.dot(X(qm), Y(pm), 5, YEL, 1.1)
    s.text("monopoly price", X(1), Y(pm) - 6, 12, YEL, t=1.2); s.text("deadweight loss", X(52), Y(30), 12, RED, italic=True, t=1.4)
    return s.svg()


def consumer_surplus():
    s = S(640, 270, "Consumer surplus under a single price")
    x0, y0, x1, y1 = frame(s, "quantity", "price", 50, 230, 610, 30)
    X = lambda q: x0 + q / 100 * (x1 - x0); Y = lambda p: y0 - p / 100 * (y0 - y1)
    s.raw(f'<path class="f" style="--t:0.6s" d="M{X(0):.1f},{Y(100):.1f} L{X(60):.1f},{Y(40):.1f} L{X(0):.1f},{Y(40):.1f} Z" fill="{TEAL}" fill-opacity="0.35"/>')
    s.raw(f'<rect class="f" style="--t:0.8s" x="{X(0):.1f}" y="{Y(40):.1f}" width="{X(60) - X(0):.1f}" height="{Y(0) - Y(40):.1f}" fill="{BLUE}" fill-opacity="0.25"/>')
    s.line([(X(0), Y(100)), (X(100), Y(0))], BLUE, 2.4)
    s.text("consumer surplus", X(8), Y(52), 14, TEAL, t=1); s.text("what buyers pay", X(18), Y(18), 14, BLUE, t=1.1)
    s.text("price discrimination turns some of the teal triangle into revenue", x1, y1 + 4, 13, SOFT, "end", True, t=1.4)
    return s.svg()


def gdp_stack():
    s = S(640, 240, "GDP by expenditure: consumption, investment, government and net exports")
    parts = [("C 68", 68, BLUE), ("I 18", 18, TEAL), ("G 17", 17, YEL), ("X − M −3", -3, RED)]
    x = 40; k = 5.3
    for i, (lab, v, c) in enumerate(parts):
        w = abs(v) * k
        if v < 0: x -= w
        s.rect(x, 90, w, 60, c, 0.85, i * 0.25, "gx")
        s.text(lab, x + w / 2, 80 if v > 0 else 175, 14, INK, "middle", t=i * 0.25 + 0.4)
        if v > 0: x += w
    s.text("GDP = C + I + G + (X − M) = 100", 320, 215, 16, INK, "middle", t=1.2)
    return s.svg()


def si_identity():
    s = S(640, 220, "Private saving minus investment equals the fiscal balance plus the trade balance")
    s.text("S − I = (G − T) + (X − M)", 320, 40, 22, INK, "middle", cls="")
    s.rect(90, 80, 120, 80, TEAL, 0.85, 0.2); s.text("S − I", 150, 125, 16, "#000", "middle", t=0.5)
    s.text("=", 255, 125, 26, INK, "middle", t=0.6)
    s.rect(300, 80, 120, 80, RED, 0.75, 0.6); s.text("G − T", 360, 125, 16, "#000", "middle", t=0.9)
    s.text("+", 450, 125, 26, INK, "middle", t=1)
    s.rect(480, 80, 120, 80, BLUE, 0.85, 1.0); s.text("X − M", 540, 125, 16, "#000", "middle", t=1.3)
    s.text("a budget deficit must be financed by private saving or by foreigners", 320, 200, 13, SOFT, "middle", True, t=1.5)
    return s.svg()


def ad_as():
    s = S(640, 290, "Aggregate demand, short-run and long-run aggregate supply")
    x0, y0, x1, y1 = frame(s, "real GDP", "price level", 50, 250, 610, 30)
    X = lambda q: x0 + q / 100 * (x1 - x0); Y = lambda p: y0 - p / 100 * (y0 - y1)
    s.line([(X(10), Y(90)), (X(90), Y(10))], BLUE, 2.4); s.text("AD", X(88), Y(10) - 8, 14, BLUE, t=0.6)
    s.line([(X(10), Y(15)), (X(90), Y(85))], TEAL, 2.4, 0.3); s.text("SRAS", X(88), Y(85) - 8, 14, TEAL, t=0.8)
    s.line([(X(50), Y(5)), (X(50), Y(95))], YEL, 2.4, 0.6); s.text("LRAS (potential GDP)", X(51), Y(95), 13, YEL, t=1)
    s.line([(X(25), Y(90)), (X(100), Y(15))], BLUE, 1.6, 1.0, dash="5 4"); s.text("AD shifts right", X(80), Y(36) - 12, 12, BLUE, italic=True, t=1.3)
    s.dot(X(50), Y(50), 5, INK, 0.9)
    return s.svg()


def growth_accounting():
    s = S(640, 270, "Output per worker rises with capital per worker at a diminishing rate; technology shifts the curve up")
    x0, y0, x1, y1 = frame(s, "capital per worker", "output per worker", 50, 230, 610, 30)
    X = lambda k: x0 + k / 100 * (x1 - x0); Y = lambda y: y0 - y / 100 * (y0 - y1)
    s.curve(lambda k: 7 * k ** 0.45, 0, 100, X, Y, color=BLUE, width=2.4); s.text("today's technology", X(70), Y(7 * 70 ** 0.45) + 18, 13, BLUE, italic=True, t=0.8)
    s.curve(lambda k: 9 * k ** 0.45, 0, 100, X, Y, color=YEL, width=2.4, t=0.6); s.text("better technology (TFP ↑)", X(55), Y(9 * 55 ** 0.45) - 10, 13, YEL, italic=True, t=1.2)
    s.text("g(Y) = g(A) + α·g(K) + (1 − α)·g(L)", x1, y0 - 14, 14, INK, "end", t=1.4)
    return s.svg()


def business_cycle():
    s = S(640, 260, "The four phases of the business cycle around trend growth")
    x0, y0, x1, y1 = frame(s, "time", "real GDP", 40, 220, 620, 30)
    X = lambda t: x0 + t / 10 * (x1 - x0); Y = lambda v: y0 - v / 100 * (y0 - y1)
    s.curve(lambda t: 30 + 4 * t, 0, 10, X, Y, color=DIM, width=1.4, dash="5 4"); s.text("trend", X(10), Y(70) + 16, 12, DIM, "end", True, cls="")
    s.curve(lambda t: 30 + 4 * t + 14 * math.sin(t * 1.2), 0, 10, X, Y, color=BLUE, width=2.6, t=0.2)
    for t, lab in [(1.3, "expansion"), (2.6, "slowdown"), (3.9, "contraction"), (5.2, "recovery")]:
        s.text(lab, X(t), Y(30 + 4 * t + 14 * math.sin(t * 1.2)) - 14, 13, YEL, "middle", True, t=0.8 + t * 0.1)
    return s.svg()


def unemployment():
    s = S(640, 240, "Frictional, structural and cyclical unemployment")
    rows = [("Frictional", "between jobs: search takes time", 2, TEAL), ("Structural", "skills or places don't match the jobs", 3, BLUE), ("Cyclical", "too little demand: rises in recessions", 4, RED)]
    for i, (a, b, w, c) in enumerate(rows):
        y = 40 + i * 52
        s.text(a, 140, y + 20, 15, INK, "end", cls="")
        s.rect(155, y, w * 40, 30, c, 0.85, i * 0.2, "gx"); s.text(b, 165 + w * 40, y + 20, 13, SOFT, t=0.4 + i * 0.2)
    s.text("frictional + structural ≈ the natural rate (at potential GDP)", 320, 220, 13, SOFT, "middle", True, t=1.2)
    return s.svg()


def price_index():
    s = S(640, 250, "Laspeyres, Paasche and Fisher price indexes compared")
    x0, y0 = 120, 200
    bars = [("Laspeyres", 111.1, BLUE, "old basket: overstates"), ("Fisher", 109.7, YEL, "geometric mean"), ("Paasche", 108.3, TEAL, "new basket: understates")]
    for i, (lab, v, c, n) in enumerate(bars):
        x = x0 + i * 150; h = (v - 100) * 12
        s.rect(x, y0 - h, 90, h, c, 0.85, i * 0.25)
        s.text(lab, x + 45, y0 + 20, 14, INK, "middle", cls=""); s.text(f"{v}", x + 45, y0 - h - 8, 14, INK, "middle", t=i * 0.25 + 0.4)
        s.text(n, x + 45, y0 + 38, 12, SOFT, "middle", True, cls="")
    s.text("same prices, different baskets", 320, 30, 14, SOFT, "middle", True, cls="")
    return s.svg()


def fisher():
    s = S(640, 230, "Nominal interest rate as real rate plus expected inflation")
    k = 40; x = 80
    for i, (lab, v, c) in enumerate([("real rate 2%", 2, TEAL), ("expected inflation 3%", 3, BLUE), ("risk premium", 0.8, YEL)]):
        s.rect(x, 90, v * k * 1.6, 50, c, 0.85, i * 0.3, "gx")
        s.text(lab, x + v * k * 0.8, 165, 13, SOFT, "middle", t=i * 0.3 + 0.3)
        x += v * k * 1.6
    s.text("nominal rate ≈ 5.8%", (80 + x) / 2, 75, 16, INK, "middle", t=1.1)
    s.text("MV = PY: if V and Y are steady, faster money growth shows up as higher P", 320, 215, 13, SOFT, "middle", True, t=1.3)
    return s.svg()


def comparative_adv():
    s = S(640, 260, "Opportunity costs decide who should make what")
    s.text("Hours per unit", 320, 26, 15, INK, "middle", cls="")
    rows = [("", "Cloth", "Wine"), ("Atlantis", "2", "4"), ("Borealis", "6", "6")]
    for r, row in enumerate(rows):
        for c, v in enumerate(row):
            s.text(v, 200 + c * 120, 60 + r * 32, 15, INK if r == 0 or c == 0 else SOFT, "middle", t=r * 0.15)
    s.text("Atlantis: 1 wine costs 2 cloth.  Borealis: 1 wine costs 1 cloth.", 320, 175, 14, INK, "middle", t=0.8)
    s.text("Atlantis is better at both (absolute advantage) but should make cloth;", 320, 205, 13, YEL, "middle", True, t=1.1)
    s.text("Borealis gives up less to make wine (comparative advantage).", 320, 225, 13, YEL, "middle", True, t=1.2)
    return s.svg()


def trade_models():
    s = S(640, 220, "Ricardian model versus Heckscher–Ohlin model")
    s.box(30, 40, 270, 130, "", BLUE, t=0); s.text("Ricardian", 165, 70, 17, BLUE, "middle", t=0.1)
    s.text("one factor: labour", 165, 100, 14, INK, "middle", t=0.2); s.text("trade comes from different", 165, 125, 13, SOFT, "middle", True, t=0.3); s.text("technology / productivity", 165, 143, 13, SOFT, "middle", True, t=0.3)
    s.box(340, 40, 270, 130, "", TEAL, t=0.4); s.text("Heckscher–Ohlin", 475, 70, 17, TEAL, "middle", t=0.5)
    s.text("two factors: capital, labour", 475, 100, 14, INK, "middle", t=0.6); s.text("trade comes from different", 475, 125, 13, SOFT, "middle", True, t=0.7); s.text("factor endowments", 475, 143, 13, SOFT, "middle", True, t=0.7)
    s.text("H–O adds who wins and loses: the abundant factor gains, the scarce factor loses", 320, 205, 13, YEL, "middle", True, t=1.1)
    return s.svg()


def bop():
    s = S(640, 250, "The balance of payments: current, capital and financial accounts")
    s.box(30, 40, 180, 110, "", BLUE); s.text("Current account", 120, 66, 15, BLUE, "middle"); s.text("goods and services", 120, 92, 12, SOFT, "middle", True); s.text("income, transfers", 120, 110, 12, SOFT, "middle", True)
    s.box(230, 40, 180, 110, "", TEAL, t=0.3); s.text("Capital account", 320, 66, 15, TEAL, "middle", t=0.3); s.text("capital transfers", 320, 92, 12, SOFT, "middle", True, t=0.3); s.text("non-produced assets", 320, 110, 12, SOFT, "middle", True, t=0.3)
    s.box(430, 40, 180, 110, "", YEL, t=0.6); s.text("Financial account", 520, 66, 15, YEL, "middle", t=0.6); s.text("FDI, portfolio flows", 520, 92, 12, SOFT, "middle", True, t=0.6); s.text("reserves", 520, 110, 12, SOFT, "middle", True, t=0.6)
    s.text("a current account deficit is paid for by a financial account inflow", 320, 190, 14, INK, "middle", t=1.0)
    s.text("(the accounts sum to zero, apart from errors and omissions)", 320, 212, 12, SOFT, "middle", True, t=1.1)
    return s.svg()


def fx_real():
    s = S(640, 250, "Nominal exchange rate unchanged, real exchange rate moved by inflation")
    s.text("USD/EUR = 1.10 means 1 euro costs 1.10 dollars", 320, 30, 15, INK, "middle", cls="")
    s.text("price currency / base currency", 320, 52, 12, SOFT, "middle", True, cls="")
    s.box(60, 90, 220, 70, "Nominal rate stays 1.10", BLUE, size=14, t=0.3)
    s.box(360, 90, 220, 70, "Euro-area prices +5%", TEAL, size=14, t=0.6, sub="US prices +1%")
    s.text("real rate (USD/EUR) = 1.10 × 1.05 / 1.01 ≈ 1.14", 320, 200, 15, YEL, "middle", t=1.0)
    s.text("euro goods got dearer for Americans: the euro appreciated in real terms", 320, 224, 13, SOFT, "middle", True, t=1.2)
    return s.svg()


def j_curve():
    s = S(640, 260, "J-curve: the trade balance worsens before it improves after a depreciation")
    x0, y0, x1, y1 = frame(s, "time after depreciation", "trade balance", 50, 220, 610, 30)
    X = lambda t: x0 + t / 10 * (x1 - x0); Y = lambda v: y0 - (v + 40) / 90 * (y0 - y1)
    s.line([(x0, Y(0)), (x1, Y(0))], DIM, 1, dash="4 4")
    s.curve(lambda t: -10 - 25 * math.sin(min(t, 3.0) / 3 * math.pi / 1.0) * (1 if t < 3 else 0) + (0 if t < 3 else 6 * (t - 3)) - (0 if t < 3 else 0), 0, 10, X, Y, color=BLUE, width=2.6)
    s.text("prices adjust first", X(1.5), Y(-36) + 16, 12, RED, "middle", True, t=0.8)
    s.text("volumes follow: Marshall–Lerner holds", X(7.5), Y(30) - 10, 12, YEL, "middle", True, t=1.2)
    return s.svg()
