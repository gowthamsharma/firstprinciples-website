"""Small animated pictures for the worked examples in the BA II Plus guide.
Each one draws itself (site.js loops it while on screen; click pauses). Numbers match the examples."""
import math
from figures import S, BLUE, TEAL, YEL, INK, SOFT, DIM, RED

W, H = 640, 200


def _ticks(n, max_ticks=11):
    """Positions to label on a timeline: all of them if few, else 0,1,2,3,…,n."""
    if n <= max_ticks - 1:
        return list(range(n + 1)), False
    return [0, 1, 2, 3, n], True


def tl(n, flows, title="", unit="", h=226):
    """flows: list of (t, label, kind) with kind 'in' (up, teal), 'out' (down, red), 'q' (unknown, yellow).
    t may be an int, or a (a, b) range for a level stream (an annuity)."""
    s = S(W, h, title or "Cash flows on a timeline")
    x0, x1, ym = 36, 604, h * 0.5
    shown, gap = _ticks(n)
    slots = shown if not gap else [0, 1, 2, 3, None, n]

    def X(t):
        if not gap:
            return x0 + 14 + t * (x1 - x0 - 28) / max(n, 1)
        idx = {0: 0, 1: 1, 2: 2, 3: 3, n: 5}.get(t)
        if idx is None:
            idx = 4
        return x0 + 14 + idx * (x1 - x0 - 28) / 5
    s.line([(x0, ym), (x1, ym)], DIM, 1.4, 0)
    for t in shown:
        s.line([(X(t), ym - 5), (X(t), ym + 5)], DIM, 1.2, 0.05, cls="f")
        s.text(str(t), X(t) + 6, ym + 17, 11, DIM, "start", cls="")
    if gap:
        s.text("…", (X(3) + X(n)) / 2, ym + 4, 18, DIM, "middle", cls="")
    if unit:
        s.text(unit, x0, h - 6, 12, DIM, "start", True, cls="")
    k = 0
    side_n = {True: 0, False: 0, None: 0}
    for t, lab, kind in flows:
        ts = list(range(t[0], t[1] + 1)) if isinstance(t, tuple) else [t]
        if gap:
            ts = [u for u in ts if u in shown] + ([None] if any(u not in shown for u in ts) else [])
        col = TEAL if kind == "in" else RED if kind == "out" else YEL
        up = kind == "in" or (kind == "q" and lab.startswith("+"))
        if kind == "q" and not lab.startswith("+"):
            up = None
        tt = 0.25 + k * 0.35
        xs = []
        for j, u in enumerate(ts):
            x = X(u) if u is not None else (X(3) + X(n)) / 2
            xs.append(x)
            d = 0.12 * j
            if u is None:
                continue
            if up is None:  # unknown value sits on the line as a pulsing ring
                s.raw(f'<circle class="f" style="--t:{tt + d}s" cx="{x:.1f}" cy="{ym:.1f}" r="9" fill="none" stroke="{YEL}" stroke-width="2.4"/>')
            elif up:
                s.arrow(x, ym - 6, x, ym - 48, col, tt + d, 2.4)
            else:
                s.arrow(x, ym + 6, x, ym + 48, col, tt + d, 2.4)
        lx = sum(xs) / len(xs)
        stag = 24 * (side_n[up] % 2)
        side_n[up] += 1
        ly = ym - 58 - stag if up else ym + 68 + stag if up is False else ym - 22
        anchor = "middle"
        if lx < 90:
            anchor, lx = "start", max(lx - 10, 8)
        elif lx > 560:
            anchor, lx = "end", min(lx + 10, 632)
        s.text(lab.lstrip("+"), lx, ly, 14, col, anchor, t=tt + 0.5)
        k += 1
    return s.svg()


def path(vals, labels=None, geo=None, title="", fmt="{:.3f}", smooth=False, h=H, note=""):
    """A value growing step by step; geo draws the constant-rate path to the same end point."""
    s = S(W, h, title or "Growth path")
    x0, x1, yb, yt = 60, 600, h - 34, 26
    lo, hi = min(vals + ([vals[0]] if geo else [])), max(vals)
    lo, hi = lo - (hi - lo) * 0.25 - 1e-9, hi + (hi - lo) * 0.15 + 1e-9
    X = lambda i: x0 + i * (x1 - x0) / (len(vals) - 1)
    Y = lambda v: yb - (v - lo) / (hi - lo) * (yb - yt)
    s.axes(x0, yb, x1, yt)
    pts = [(X(i), Y(v)) for i, v in enumerate(vals)]
    s.line(pts, BLUE, 2.6, 0.2)
    if not smooth:
        for i, (x, y) in enumerate(pts):
            s.dot(x, y, 4.5, BLUE, 0.2 + i * 0.25)
            if labels:
                s.text(labels[i], x, yb + 20, 11, DIM, "middle", cls="")
            s.text(fmt.format(vals[i]), x, y - 12, 12, INK, "middle", t=0.3 + i * 0.25)
    else:
        if labels:
            for i, (x, y) in enumerate(pts):
                if labels[i]:
                    s.text(labels[i], x, yb + 20, 11, DIM, "middle", cls="")
        s.dot(*pts[-1], 5, YEL, 1.6)
        s.text(fmt.format(vals[-1]), pts[-1][0] - 8, pts[-1][1] - 12, 13, YEL, "end", t=1.7)
    if note:
        s.text(note, x0 + 8, yb - 8, 13, YEL, "start", t=1.4)
    if geo:
        n = len(vals) - 1
        g = (vals[-1] / vals[0]) ** (1 / n)
        s.line([(X(i), Y(vals[0] * g ** i)) for i in range(n + 1)], YEL, 2, 1.4, dash="6 5")
        s.text(geo, x0 + 8, yb - 8, 13, YEL, "start", t=1.8)
    return s.svg()


def bars(vals, labels, mean=None, dev=False, probs=None, title="", h=H):
    s = S(W, h, title or "Values and their mean")
    x0, x1, yt, yb = 60, 600, 24, h - 30
    lo, hi = min(0, min(vals)), max(vals)
    pad = (hi - lo) * 0.18
    lo, hi = lo - (pad if lo < 0 else 0), hi + pad
    Y = lambda v: yt + (hi - v) / (hi - lo) * (yb - yt)
    n = len(vals)
    bw = (x1 - x0) / n
    s.line([(x0, Y(0)), (x1, Y(0))], DIM, 1, 0, cls="f")
    for i, v in enumerate(vals):
        w = bw * (0.2 + 0.5 * probs[i]) if probs else bw * 0.42
        cx = x0 + bw * (i + 0.5)
        top, bot = (Y(v), Y(0)) if v >= 0 else (Y(0), Y(v))
        s.rect(cx - w / 2, top, w, bot - top, TEAL if v >= 0 else RED, 0.85, 0.15 + i * 0.18)
        s.text(f"{v:g}", cx, (top - 8) if v >= 0 else (bot + 16), 13, INK, "middle", t=0.3 + i * 0.18)
        s.text(labels[i], cx, yb + 22, 11, DIM, "middle", cls="")
        if dev and mean is not None:
            s.line([(cx + w / 2 + 6, Y(v)), (cx + w / 2 + 6, Y(mean))], YEL, 1.6, 1.6 + i * 0.12, dash="3 3")
    if mean is not None:
        s.line([(x0, Y(mean)), (x1, Y(mean))], YEL, 2.2, 1.2)
        s.text(f"mean = {mean:g}", x1, Y(mean) - 8, 13, YEL, "end", t=1.4)
    return s.svg()


def dots(n=10, r=3, title=""):
    s = S(W, 210, title or f"Choosing {r} of {n}")
    picks = [(1, 4, 8), (0, 5, 9), (2, 3, 7)]
    for k, combo in enumerate(picks):
        y, t, col = 36 + k * 52, 0.3 + k * 0.9, [TEAL, BLUE, YEL][k]
        for i in range(n):
            s.raw(f'<circle cx="{40 + i * 38:.1f}" cy="{y}" r="13" fill="none" stroke="{DIM}" stroke-width="1.4"/>')
        for i in combo:
            s.raw(f'<circle class="f" style="--t:{t}s" cx="{40 + i * 38:.1f}" cy="{y}" r="10" fill="{col}"/>')
        s.text("pick " + ", ".join(str(c + 1) for c in combo), 420, y + 5, 14, col, t=t)
    s.text("… and so on: 120 different groups of 3", 320, 196, 14, INK, "middle", t=3.0)
    return s.svg()


def amort12(rate=0.055 / 12, bal=300000, pay=1703.367004, months=12, title=""):
    s = S(W, H, title or "Each payment split into interest and principal")
    x0, x1, yt, yb = 50, 600, 30, H - 34
    bw = (x1 - x0) / months
    Y = lambda v: yb - v / pay * (yb - yt)
    for m in range(months):
        it = bal * rate
        pr = pay - it
        bal -= pr
        x = x0 + m * bw + bw * 0.18
        s.rect(x, Y(it), bw * 0.64, yb - Y(it), RED, 0.8, 0.1 + m * 0.08)
        s.rect(x, Y(pay), bw * 0.64, Y(it) - Y(pay), TEAL, 0.9, 0.4 + m * 0.08)
        s.text(str(m + 1), x + bw * 0.32, yb + 18, 11, DIM, "middle", cls="")
    s.text("interest ≈ 1,375 a month", x0, yt - 8, 13, RED, t=1.4)
    s.text("principal ≈ 330", x1, yt - 8, 13, TEAL, "end", t=1.6)
    return s.svg()


def accrued(title=""):
    s = S(W, H, title or "Settlement between two coupon dates")
    x0, x1, ym = 70, 570, 112
    xs = x0 + (x1 - x0) / 3
    s.line([(x0, ym), (x1, ym)], DIM, 1.4, 0)
    for x, lab in [(x0, "last coupon"), (x1, "next coupon")]:
        s.line([(x, ym - 7), (x, ym + 7)], DIM, 1.4, 0.05, cls="f")
        s.text(lab, x, ym + 26, 12, DIM, "middle", cls="")
    s.dot(xs, ym, 6, YEL, 0.4)
    s.text("settlement", xs, ym + 26, 12, YEL, "middle", t=0.5)
    s.line([(x0, ym - 22), (xs, ym - 22)], TEAL, 3, 0.7)
    s.text("t = 60 days", (x0 + xs) / 2, ym - 32, 13, TEAL, "middle", t=0.9)
    s.line([(x0, ym - 52), (x1, ym - 52)], BLUE, 2, 1.0, dash="5 4")
    s.text("T = 180 days", (x0 + x1) / 2, ym - 62, 13, BLUE, "middle", t=1.1)
    s.text("price on the last coupon date × 1.04^(t/T) = full price", (x0 + x1) / 2, ym + 66, 13, INK, "middle", t=1.5)
    s.text("accrued interest = t/T × 3 = 1.00", (x0 + x1) / 2, ym + 88, 13, SOFT, "middle", t=1.8)
    return s.svg()


def price_yield(title=""):
    s = S(W, H + 20, title or "Bond price at three yields")
    x0, x1, yt, yb = 70, 600, 26, H - 14

    def price(y):
        return sum(5 / (1 + y) ** t for t in range(1, 11)) + 100 / (1 + y) ** 10
    lo, hi = 0.035, 0.085
    plo, phi = price(hi) - 3, price(lo) + 3
    X = lambda y: x0 + (y - lo) / (hi - lo) * (x1 - x0)
    Y = lambda p: yb - (p - plo) / (phi - plo) * (yb - yt)
    s.axes(x0, yb, x1, yt)
    s.curve(price, lo, hi, X, Y, 80, color=BLUE, width=2.6, t=0.2)
    for k, (y, lab, col) in enumerate([(0.055, "PV− = 96.23 (M1)", TEAL), (0.06, "PV0 = 92.64 (M0)", YEL), (0.065, "PV+ = 89.22 (M2)", RED)]):
        x, py = X(y), Y(price(y))
        s.line([(x, yb), (x, py)], col, 1.2, 0.9 + k * 0.3, dash="3 3")
        s.dot(x, py, 6, col, 1.0 + k * 0.3)
        s.text(lab, x + 10, py - 10 - (k == 0) * 6, 13, col, t=1.1 + k * 0.3)
        s.text(f"{y * 100:g}%", x, yb + 18, 11, DIM, "middle", cls="")
    s.text("yield", x1, yb + 18, 11, DIM, "end", True, cls="")
    return s.svg()


def two_phase(title=""):
    s = S(W, H, title or "Save for 30 years, then draw for 25")
    x0, x1, ym = 30, 610, 104
    s.line([(x0, ym), (x1, ym)], DIM, 1.4, 0)
    xr = x0 + (x1 - x0) * 30 / 55
    for i in range(1, 31, 2):
        x = x0 + (x1 - x0) * i / 55
        s.arrow(x, ym + 5, x, ym + 40, RED, 0.2 + i * 0.02, 1.8)
    for i in range(30, 55, 2):
        x = x0 + (x1 - x0) * i / 55
        s.arrow(x, ym - 5, x, ym - 46, TEAL, 1.0 + (i - 30) * 0.02, 1.8)
    s.line([(xr, ym - 70), (xr, ym + 64)], YEL, 1.6, 0.8, dash="4 4")
    s.text("retirement day: need 591,946", xr, ym - 76, 13, YEL, "middle", t=1.0)
    s.text("save PMT ? a year (30 years, 7%)", (x0 + xr) / 2, ym + 64, 13, RED, "middle", t=0.6)
    s.text("draw 40,000 a year (25 years, 5%)", (xr + x1) / 2, ym - 56, 13, TEAL, "middle", t=1.4)
    return s.svg()


def compounding(m=12, nom=0.12, title=""):
    vals = [(1 + nom / m) ** k for k in range(m + 1)]
    labels = ["0"] + ["" if k not in (3, 6, 9, 12) else f"month {k}" for k in range(1, m + 1)]
    note = f"{nom * 100:.2f}% a year, added monthly, grows 1 to {vals[-1]:.4f}: EAR = {(vals[-1] - 1) * 100:.2f}%"
    return path(vals, labels, title=title or "One unit compounding monthly", fmt="{:.4f}", smooth=True, note=note)


VIS = {
    "geo": lambda: path([1, 1.10, 1.045, 1.254], ["start", "year 1: +10%", "year 2: −5%", "year 3: +20%"], geo="constant 7.84% a year ends at the same place", fmt="{:.3f}"),
    "cont": lambda: path([math.exp(0.05 * t / 4) for t in range(13)], ["0"] + ["" if k % 4 else str(k // 4) for k in range(1, 13)], smooth=True, fmt="{:.4f}", title="1 growing continuously at 5% for three years"),
    "lnret": lambda: path([100, 120], ["P0", "P1"], fmt="{:.0f}", title="Price from 100 to 120", note="ln(1.2) = 18.23% continuous, 20% simple"),
    "ncr": lambda: dots(10, 3),
    "sum3": lambda: tl(3, [(1, "100", "in"), (2, "200", "in"), (3, "300", "in"), (0, "PV = ?", "q")], unit="years, 5%"),
    "ddm": lambda: tl(3, [(1, "D1 = 2.00", "in"), (2, "D2 = 2.40", "in"), (3, "D3 + P3 = 52.80", "in"), (0, "V0 = ?", "q")], unit="years, r = 10%, g = 4% after year 3"),
    "dur": price_yield,
    "fv": lambda: tl(5, [(0, "−1,000", "out"), (5, "+FV = ?", "q")], unit="years, 6%"),
    "pv": lambda: tl(10, [(10, "5,000", "in"), (0, "PV = ?", "q")], unit="years, 7%"),
    "pmt": lambda: tl(360, [(0, "+300,000 loan", "in"), ((1, 360), "PMT = ? every month", "out")], unit="months, 5.5% ÷ 12"),
    "rate": lambda: tl(10, [(0, "−8,000", "out"), (10, "15,000", "in")], unit="years, rate = ?"),
    "nper": lambda: tl(10, [(0, "−1,000", "out"), (10, "2,000 at N = ?", "in")], unit="years, 7%"),
    "annuity_end": lambda: tl(20, [((1, 20), "−10,000 at each year end", "out"), (0, "PV = ?", "q")], unit="years, 5%"),
    "annuity_bgn": lambda: tl(20, [((0, 19), "−10,000 at each year start", "out")], unit="years, 5%, BGN"),
    "retire": two_phase,
    "amort": amort12,
    "bond": lambda: tl(10, [((1, 10), "coupon 3", "in"), (10, "+100", "in"), (0, "price = ?", "q")], unit="half-years, 4% each"),
    "ytm": lambda: tl(10, [(0, "−95", "out"), ((1, 10), "coupon 3", "in"), (10, "+100", "in")], unit="half-years, yield = ?"),
    "accrued": accrued,
    "npv": lambda: tl(5, [(0, "−50,000", "out"), (1, "15,000", "in"), ((2, 4), "20,000 each", "in"), (5, "25,000", "in")], unit="years, 10%"),
    "mwrr": lambda: tl(2, [(0, "−100: buy 1 share", "out"), (1, "−108: buy 1, get 2 dividend", "out"), (2, "+244: sell 2 at 120 + dividends", "in")], unit="years, IRR = ?"),
    "mean": lambda: bars([12, -4, 9, 15, 3], ["year 1", "year 2", "year 3", "year 4", "year 5"], mean=7),
    "sd": lambda: bars([12, -4, 9, 15, 3], ["year 1", "year 2", "year 3", "year 4", "year 5"], mean=7, dev=True),
    "er": lambda: bars([20, 8, -10], ["boom: p = 0.25", "normal: p = 0.50", "bust: p = 0.25"], mean=6.5, probs=[0.25, 0.5, 0.25]),
    "sdp": lambda: bars([20, 8, -10], ["boom: p = 0.25", "normal: p = 0.50", "bust: p = 0.25"], mean=6.5, dev=True, probs=[0.25, 0.5, 0.25]),
    "ear": lambda: compounding(),
    "nom": lambda: compounding(12, 0.0956897),
    "err5": lambda: tl(5, [(0, "+1,000", "in"), (5, "+1,500", "in")], unit="both positive: no rate balances them"),
}


def visual(key):
    return VIS[key]()
