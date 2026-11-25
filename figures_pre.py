import math
"""
Second diagrams for the prerequisite lessons (Nov 2026 rewrite). Same drawing kit and reveal classes as figures.py:
  d = line draws itself, g = bar grows up, gx = bar grows right, f = fades in; --t = delay in seconds.
Every number is invented for teaching and matches the worked example in the lesson.
"""
from figures import S, frame, BLUE, TEAL, YEL, INK, SOFT, DIM, RULE, RED, BLUEB


def _grid_y(s, x0, x1, ys):
    for y in ys:
        s.raw(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{RULE}" stroke-width="0.6" stroke-dasharray="2 4"/>')


# ---------------------------------------------------------------- 01 financial reporting objective
def elements_map():
    s = S(640, 270, "The five elements: assets, liabilities and equity on the balance sheet; income and expenses change equity")
    s.box(30, 60, 170, 60, "Assets", BLUE, size=15, t=0, sub="what it controls")
    s.text("=", 215, 98, 26, INK, "middle", t=0.3)
    s.box(230, 60, 170, 60, "Liabilities", TEAL, size=15, t=0.4, sub="what it owes")
    s.text("+", 415, 98, 26, INK, "middle", t=0.6)
    s.box(430, 60, 180, 60, "Equity", YEL, size=15, t=0.7, sub="owners' residual")
    s.box(330, 185, 120, 48, "Income", BLUE, size=15, t=1.2)
    s.box(480, 185, 120, 48, "Expenses", RED, size=15, t=1.4)
    s.arrow(390, 185, 490, 124, BLUE, t=1.6)
    s.arrow(540, 185, 530, 124, RED, t=1.8)
    s.text("raises equity", 330, 252, 12, BLUE, italic=True, t=2.2)
    s.text("lowers equity", 480, 252, 12, RED, italic=True, t=2.3)
    s.text("one snapshot (the balance sheet) …", 40, 40, 13, DIM, italic=True, cls="")
    s.text("… and what changed it during the year", 40, 210, 13, DIM, italic=True, t=1.0)
    return s.svg()


# ---------------------------------------------------------------- 02 three statements
def bs_balance():
    s = S(640, 290, "After seven transactions both sides of the balance sheet total 1,530")
    y0, k = 255, 0.135
    def stack(x, parts, t0):
        y = y0
        for i, (lab, v, c) in enumerate(parts):
            h = v * k
            s.rect(x, y - h, 150, h, c, 0.85, t0 + i * 0.35)
            if h > 18:
                s.text(f"{lab} {v:,}", x + 75, y - h / 2 + 5, 13, INK, "middle", t=t0 + i * 0.35 + 0.5)
            else:
                s.text(f"{lab} {v:,}", x + 160, y - h / 2 + 5, 13, c, t=t0 + i * 0.35 + 0.5)
            y -= h
        return y
    top = stack(70, [("cash", 1150, BLUE), ("receivables", 180, BLUEB), ("inventory", 200, TEAL)], 0)
    stack(300, [("debt", 500, TEAL), ("share capital", 1000, BLUE), ("retained earnings", 30, YEL)], 0.3)
    s.raw(f'<line x1="50" y1="{y0}" x2="470" y2="{y0}" stroke="{RULE}"/>')
    s.text("Assets", 145, y0 + 22, 14, SOFT, "middle", cls=""); s.text("Liabilities + equity", 375, y0 + 22, 14, SOFT, "middle", cls="")
    s.line([(60, top - 8), (460, top - 8)], YEL, 1.6, 1.8, dash="5 4")
    s.text("both sides: 1,530", 260, top - 16, 14, YEL, "middle", t=2.0)
    return s.svg()


# ---------------------------------------------------------------- 03 accruals
def deferred_revenue_timeline():
    s = S(640, 280, "Cash of 1,200 arrives in October; revenue is earned at 100 a month and the liability runs down")
    x0, y0, x1, y1 = frame(s, "month", "", 50, 240, 610, 40)
    months = ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]
    step = (x1 - x0) / 12
    Y = lambda v: y0 - v / 1300 * (y0 - y1)
    s.rect(x0 + 6, Y(1200), step - 12, y0 - Y(1200), YEL, 0.25, 0, stroke=YEL)
    s.text("cash 1,200", x0 + step / 2, Y(1200) - 8, 12, YEL, "middle", t=0.2)
    pts = []
    for i, m in enumerate(months):
        x = x0 + i * step
        s.rect(x + step * 0.3, Y(100), step * 0.4, y0 - Y(100), BLUE, 0.9, 0.5 + i * 0.08)
        s.text(m, x + step / 2, y0 + 16, 11, DIM, "middle", cls="")
        pts.append((x + step, Y(1200 - 100 * (i + 1))))
    s.line([(x0, Y(1200))] + pts, TEAL, 2.6, 1.2)
    s.text("unearned revenue (a liability)", x0 + 3.2 * step, Y(900) - 12, 13, TEAL, italic=True, t=1.8)
    s.text("revenue: 100 a month", x0 + 3.4 * step, Y(100) - 12, 13, BLUE, italic=True, t=1.8)
    s.raw(f'<line x1="{x0 + 3 * step:.1f}" y1="{y1}" x2="{x0 + 3 * step:.1f}" y2="{y0}" stroke="{SOFT}" stroke-dasharray="4 4"/>')
    s.text("year-end: earned 300, owed 900", x0 + 3 * step + 6, y1 + 6, 12, SOFT, t=2.2)
    return s.svg()


# ---------------------------------------------------------------- 04 revenue recognition
def bundle_allocation():
    s = S(640, 280, "A bundle sold for 1,000 is split by stand-alone prices: 500 for the phone at delivery, 500 for the service over 24 months")
    y0, k = 230, 0.14
    s.text("stand-alone prices", 140, 36, 13, DIM, "middle", True, cls="")
    s.rect(80, y0 - 600 * k, 120, 600 * k, BLUE, 0.35, 0, stroke=BLUE); s.text("phone 600", 140, y0 - 300 * k + 5, 13, INK, "middle", t=0.3)
    s.rect(80, y0 - 1200 * k, 120, 600 * k, TEAL, 0.35, 0.3, stroke=TEAL); s.text("service 600", 140, y0 - 900 * k + 5, 13, INK, "middle", t=0.6)
    s.text("price paid: 1,000", 320, 36, 13, DIM, "middle", True, cls="")
    s.rect(260, y0 - 500 * k, 120, 500 * k, BLUE, 0.9, 0.9); s.text("500", 320, y0 - 250 * k + 5, 14, "#0B1F38", "middle", t=1.2)
    s.rect(260, y0 - 1000 * k, 120, 500 * k, TEAL, 0.9, 1.1); s.text("500", 320, y0 - 750 * k + 5, 14, "#0B1F38", "middle", t=1.4)
    s.arrow(205, y0 - 160, 255, y0 - 140, DIM, t=0.8)
    # revenue timing
    s.text("revenue booked", 520, 36, 13, DIM, "middle", True, cls="")
    bx = 430
    s.rect(bx, y0 - 500 * k, 14, 500 * k, BLUE, 0.9, 1.6)
    for i in range(24):
        s.rect(bx + 18 + i * 6.2, y0 - 20.8 * k * 6, 4.4, 20.8 * k * 6, TEAL, 0.9, 1.8 + i * 0.03)
    s.text("phone: at delivery", bx, y0 + 20, 12, BLUE, t=2.0)
    s.text("service: 20.8 a month × 24", bx, y0 + 38, 12, TEAL, t=2.4)
    s.raw(f'<line x1="60" y1="{y0}" x2="620" y2="{y0}" stroke="{RULE}"/>')
    return s.svg()


# ---------------------------------------------------------------- 05 doubtful accounts
def allowance_roll():
    s = S(640, 280, "Allowance roll-forward: opening 400 plus expense 450 minus write-offs 350 gives closing 500")
    y0, k = 240, 0.2
    cols = [("opening", 0, 400, BLUE), ("+ expense", 400, 850, TEAL), ("− write-offs", 500, 850, RED), ("closing", 0, 500, YEL)]
    for i, (lab, lo, hi, c) in enumerate(cols):
        x = 70 + i * 135
        s.rect(x, y0 - hi * k, 90, (hi - lo) * k, c, 0.85, i * 0.45)
        v = hi - lo
        s.text(f"{v:,}", x + 45, y0 - hi * k - 8, 14, c, "middle", t=i * 0.45 + 0.4)
        s.text(lab, x + 45, y0 + 20, 13, SOFT, "middle", cls="")
        if 0 < i:
            prev = [400, 850, 500][i - 1]
            s.line([(x - 45, y0 - prev * k), (x, y0 - prev * k)], DIM, 1, i * 0.45, dash="3 3")
    s.raw(f'<line x1="50" y1="{y0}" x2="620" y2="{y0}" stroke="{RULE}"/>')
    s.text("write-offs use the allowance: no new expense", 335, 40, 13, RED, "middle", True, t=1.6)
    return s.svg()


# ---------------------------------------------------------------- 06 depreciation
def dep_book_value():
    s = S(640, 280, "Book value under straight-line and double-declining balance: both end at the 1,000 salvage value")
    x0, y0, x1, y1 = frame(s, "year", "book value", 60, 240, 600, 36)
    X = lambda t: x0 + t / 5 * (x1 - x0); Y = lambda v: y0 - v / 10500 * (y0 - y1)
    sl = [10000 - 1800 * t for t in range(6)]
    ddb = [10000, 6000, 3600, 2160, 1296, 1000]
    _grid_y(s, x0, x1, [Y(v) for v in (2500, 5000, 7500, 10000)])
    for v in (5000, 10000):
        s.text(f"{v:,}", x0 - 8, Y(v) + 4, 11, DIM, "end", cls="")
    s.line([(X(t), Y(v)) for t, v in enumerate(sl)], BLUE, 2.6, 0)
    s.line([(X(t), Y(v)) for t, v in enumerate(ddb)], TEAL, 2.6, 0.5)
    s.line([(X(0), Y(1000)), (X(5), Y(1000))], YEL, 1.4, 1.2, dash="5 4")
    s.text("salvage 1,000", X(5), Y(1000) - 8, 12, YEL, "end", t=1.4)
    s.text("straight-line", X(2.6), Y(sl[2]) - 14, 13, BLUE, italic=True, t=1.0)
    s.text("double-declining", X(0.55), Y(6600), 13, TEAL, "end", italic=True, t=1.4)
    for t in range(6):
        s.text(str(t), X(t), y0 + 16, 11, DIM, "middle", cls="")
    s.text("the gap between the lines is", X(2.9), Y(8800), 12, SOFT, italic=True, t=2.0)
    s.text("extra depreciation taken early", X(2.9), Y(8800) + 15, 12, SOFT, italic=True, t=2.0)
    return s.svg()


# ---------------------------------------------------------------- 07 non-recurring items
def earnings_bridge():
    s = S(640, 270, "From reported net income of 100.5 to core earnings of 135")
    y0, k = 230, 1.3
    steps = [("reported", 0, 100.5, BLUE), ("+ restructuring\n(after tax)", 100.5, 123, TEAL), ("+ discontinued\nloss", 123, 135, TEAL), ("core earnings", 0, 135, YEL)]
    for i, (lab, lo, hi, c) in enumerate(steps):
        x = 80 + i * 130
        s.rect(x, y0 - hi * k, 80, (hi - lo) * k, c, 0.85, i * 0.45)
        s.text(f"{hi - lo:g}", x + 40, y0 - hi * k - 8, 14, c, "middle", t=i * 0.45 + 0.4)
        for j, part in enumerate(lab.split("\n")):
            s.text(part, x + 40, y0 + 18 + j * 15, 12, SOFT, "middle", cls="")
    s.raw(f'<line x1="60" y1="{y0}" x2="620" y2="{y0}" stroke="{RULE}"/>')
    s.text("add back what will not recur, after tax", 60, 26, 13, SOFT, "start", True, t=1.8)
    return s.svg()


# ---------------------------------------------------------------- 08 common size
def horizontal_index():
    s = S(640, 280, "Horizontal analysis: revenue and receivables indexed to 100 in the base year")
    x0, y0, x1, y1 = frame(s, "year", "index (base = 100)", 70, 240, 600, 46)
    X = lambda t: x0 + t / 3 * (x1 - x0); Y = lambda v: y0 - (v - 90) / 60 * (y0 - y1)
    rev = [100, 106, 111, 115]; rec = [100, 112, 126, 140]
    _grid_y(s, x0, x1, [Y(v) for v in (100, 120, 140)])
    for v in (100, 120, 140):
        s.text(str(v), x0 - 8, Y(v) + 4, 11, DIM, "end", cls="")
    for t, lab in enumerate(["base", "+1", "+2", "+3"]):
        s.text(lab, X(t), y0 + 16, 11, DIM, "middle", cls="")
    s.line([(X(t), Y(v)) for t, v in enumerate(rev)], BLUE, 2.6, 0)
    s.line([(X(t), Y(v)) for t, v in enumerate(rec)], RED, 2.6, 0.5)
    for t, v in enumerate(rec):
        s.dot(X(t), Y(v), 4, RED, 0.6 + t * 0.2)
    s.text("receivables 140", X(3) - 6, Y(140) - 10, 13, RED, "end", t=1.4)
    s.text("revenue 115", X(3) - 6, Y(115) + 20, 13, BLUE, "end", t=1.4)
    s.text("customers paying more slowly, or sales booked early?", 600, 22, 12, SOFT, "end", True, t=1.9)
    return s.svg()


# ---------------------------------------------------------------- 09 comprehensive income
def oci_recycling():
    s = S(640, 270, "A hedging gain waits in OCI, then is recycled into profit when the hedged sale happens")
    s.box(40, 60, 170, 60, "Hedge gains 30", TEAL, size=15, t=0, sub="year 1")
    s.box(250, 60, 170, 60, "OCI reserve", YEL, size=15, t=0.5, sub="inside equity")
    s.box(460, 60, 150, 60, "Net income", BLUE, size=15, t=1.4, sub="year 2")
    s.arrow(210, 90, 248, 90, TEAL, t=0.4)
    s.arrow(420, 90, 458, 90, BLUE, t=1.2)
    s.text("recycled when the", 440, 145, 12, SOFT, "middle", True, t=1.6)
    s.text("hedged sale is booked", 440, 161, 12, SOFT, "middle", True, t=1.7)
    s.box(250, 195, 170, 48, "Never recycled", RED, size=14, t=2.2)
    s.text("e.g. IFRS revaluation surplus,", 430, 212, 12, SOFT, t=2.4)
    s.text("pension remeasurements (IFRS)", 430, 228, 12, SOFT, t=2.5)
    s.arrow(335, 122, 335, 192, RED, t=2.0)
    return s.svg()


# ---------------------------------------------------------------- 10 balance sheet classification
def liquidity_ratios():
    s = S(640, 280, "Current, quick and cash ratios use smaller and smaller slices of current assets against the same liabilities")
    x0, y0, k = 60, 250, 0.68
    parts = [("cash 60", 60, YEL), ("securities 20", 20, BLUEB), ("receivables 40", 40, BLUE), ("inventory 180", 180, TEAL)]
    y = y0
    for i, (lab, v, c) in enumerate(parts):
        h = v * k
        s.rect(x0, y - h, 120, h, c, 0.85, i * 0.3)
        s.text(lab, x0 + 130, y - h / 2 + 4, 12, c, t=i * 0.3 + 0.3)
        y -= h
    s.rect(330, y0 - 250 * k, 120, 250 * k, RED, 0.7, 1.2)
    s.text("current liabilities 250", 390, y0 - 250 * k - 8, 12, RED, "middle", t=1.4)
    s.raw(f'<line x1="40" y1="{y0}" x2="620" y2="{y0}" stroke="{RULE}"/>')
    rows = [("current ratio", "300 ÷ 250 = 1.20", TEAL), ("quick ratio", "120 ÷ 250 = 0.48", BLUE), ("cash ratio", "80 ÷ 250 = 0.32", YEL)]
    for i, (a, b, c) in enumerate(rows):
        s.text(a, 470, 120 + i * 34, 13, c, t=1.8 + i * 0.3)
        s.text(b, 470, 136 + i * 34, 12, SOFT, t=1.9 + i * 0.3)
    return s.svg()


# ---------------------------------------------------------------- 11 equity
def equity_buyback():
    s = S(640, 280, "A buyback of 150 at a price above book value: equity falls to 850 and book value per share falls from 10.00 to 9.44")
    y0, k = 240, 0.17
    def col(x, parts, t0, title):
        y = y0
        for i, (lab, v, c) in enumerate(parts):
            h = v * k
            s.rect(x, y - h, 130, h, c, 0.85, t0 + i * 0.3)
            s.text(f"{lab} {v:,}", x + 65, y - h / 2 + 5, 12, INK, "middle", t=t0 + i * 0.3 + 0.3)
            y -= h
        s.text(title, x + 65, y0 + 20, 13, SOFT, "middle", cls="")
        return y
    col(70, [("share capital", 450, BLUE), ("retained earnings", 550, TEAL)], 0, "before: 100 shares")
    top = col(290, [("share capital", 450, BLUE), ("retained earnings", 550, TEAL)], 0.9, "after: 90 shares")
    s.rect(290, top, 130, 150 * k, RED, 0.8, 2.0, cls="f")
    s.text("treasury shares −150", 430, top + 150 * k / 2 + 4, 12, RED, t=2.2)
    s.raw(f'<line x1="50" y1="{y0}" x2="600" y2="{y0}" stroke="{RULE}"/>')
    s.text("book value per share", 470, 120, 13, SOFT, t=2.4)
    s.text("1,000 ÷ 100 = 10.00", 470, 140, 13, BLUE, t=2.5)
    s.text("850 ÷ 90 = 9.44", 470, 160, 13, YEL, t=2.7)
    return s.svg()


# ---------------------------------------------------------------- 12 cash flow classification
def cf_two_ways():
    s = S(640, 300, "The same cash flows classified two ways: only the buckets change, the total change in cash is 15 either way")
    x0, y0, x1, y1 = 60, 150, 600, 40
    Y = lambda v: y0 - v * 0.33
    s.raw(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="{RULE}"/>')
    groups = [("operating", 175, 210), ("investing", -280, -265), ("financing", 120, 70)]
    for i, (lab, a, b) in enumerate(groups):
        gx = x0 + 30 + i * 180
        for j, (v, c) in enumerate(((a, BLUE), (b, TEAL))):
            x = gx + j * 62
            top, h = (Y(v), v * 0.33) if v > 0 else (y0, -v * 0.33)
            s.rect(x, top, 52, h, c, 0.88, i * 0.3 + j * 0.15, cls="f")
            s.text(f"{v:+}", x + 26, (top - 6) if v > 0 else (top + h + 15), 12, c, "middle", t=i * 0.3 + j * 0.15 + 0.4)
        s.text(lab, gx + 57, 290, 13, SOFT, "middle", cls="")
    s.rect(450, 50, 10, 10, BLUE, 0.9, cls=""); s.text("US GAAP", 465, 59, 12, SOFT, cls="")
    s.rect(450, 70, 10, 10, TEAL, 0.9, cls=""); s.text("IFRS choices", 465, 79, 12, SOFT, cls="")
    s.text("IFRS choices used here: interest paid → financing; interest and dividends received → investing", 60, 22, 11, DIM, italic=True, cls="")
    return s.svg()


# ---------------------------------------------------------------- 13 indirect method
def wc_signs():
    s = S(640, 270, "Working capital adjustments: a rise in an operating asset uses cash, a rise in an operating liability provides it")
    s.raw(f'<line x1="320" y1="50" x2="320" y2="240" stroke="{RULE}"/><line x1="70" y1="145" x2="600" y2="145" stroke="{RULE}"/>')
    s.text("operating asset", 195, 40, 13, DIM, "middle", True, cls=""); s.text("operating liability", 460, 40, 13, DIM, "middle", True, cls="")
    s.text("rises", 60, 100, 13, DIM, "end", True, cls=""); s.text("falls", 60, 200, 13, DIM, "end", True, cls="")
    cells = [(195, 95, "subtract", "receivables up: sales not yet collected", RED), (460, 95, "add", "payables up: costs not yet paid", TEAL),
             (195, 195, "add", "inventory down: sold from stock", TEAL), (460, 195, "subtract", "accrued wages down: paid off", RED)]
    for i, (x, y, a, b, c) in enumerate(cells):
        s.text(a, x, y, 20, c, "middle", t=i * 0.3)
        s.text(b, x, y + 22, 12, SOFT, "middle", True, t=i * 0.3 + 0.15)
    return s.svg()


# ---------------------------------------------------------------- 14 inventory cost
def overhead_allocation():
    s = S(640, 280, "Fixed production overhead of 100,000 allocated at normal capacity of 10,000 units: producing 8,000 puts 80,000 in inventory and expenses 20,000")
    y0, k = 230, 0.0016
    s.text("fixed production overhead: 100,000", 60, 34, 13, SOFT, cls="")
    s.rect(80, y0 - 100000 * k, 120, 100000 * k, DIM, 0.5, 0, stroke=SOFT)
    s.text("normal capacity", 140, y0 + 20, 12, SOFT, "middle", cls=""); s.text("10,000 units × 10", 140, y0 + 36, 12, DIM, "middle", cls="")
    s.rect(300, y0 - 80000 * k, 120, 80000 * k, TEAL, 0.9, 0.6)
    s.text("80,000", 360, y0 - 40000 * k + 5, 14, "#0B1F38", "middle", t=0.9)
    s.rect(300, y0 - 100000 * k, 120, 20000 * k, RED, 0.85, 1.2)
    s.text("20,000", 360, y0 - 90000 * k + 5, 13, INK, "middle", t=1.4)
    s.text("actual output", 360, y0 + 20, 12, SOFT, "middle", cls=""); s.text("8,000 units × 10", 360, y0 + 36, 12, DIM, "middle", cls="")
    s.text("into inventory", 432, y0 - 40000 * k + 5, 13, TEAL, t=1.0)
    s.text("unabsorbed: expensed now", 432, y0 - 90000 * k + 5, 13, RED, t=1.6)
    s.raw(f'<line x1="60" y1="{y0}" x2="610" y2="{y0}" stroke="{RULE}"/>')
    return s.svg()


# ---------------------------------------------------------------- 15 FIFO / LIFO
def cost_layers():
    s = S(640, 290, "Three cost layers, 200 units sold: FIFO sells the oldest layers, LIFO the newest")
    layers = [("100 @ 10", BLUEB), ("100 @ 12", BLUE), ("100 @ 14", TEAL)]
    def stack(x, sold, title, t0):
        for i, (lab, c) in enumerate(layers):
            y = 230 - (i + 1) * 52
            gone = i in sold
            s.rect(x, y, 150, 48, c, 0.25 if gone else 0.9, t0 + i * 0.2, cls="f", stroke=c)
            s.text(lab + ("  → sold" if gone else "  → kept"), x + 75, y + 29, 13, c if gone else "#0B1F38", "middle", t=t0 + i * 0.2 + 0.3)
        s.text(title, x + 75, 258, 14, INK, "middle", cls="")
    stack(70, (0, 1), "FIFO", 0)
    stack(400, (1, 2), "LIFO", 0.8)
    s.text("cost of sales 2,200 · inventory 1,400", 145, 280, 12, SOFT, "middle", t=1.6)
    s.text("cost of sales 2,600 · inventory 1,000", 475, 280, 12, SOFT, "middle", t=1.8)
    s.text("oldest at the bottom, newest on top", 320, 30, 12, DIM, "middle", True, cls="")
    return s.svg()


# ---------------------------------------------------------------- 16 LIFO reserve
def lifo_reserve_split():
    s = S(640, 280, "FIFO inventory equals LIFO inventory plus the LIFO reserve; the reserve splits into deferred tax and equity")
    y0, k = 240, 0.18
    s.rect(80, y0 - 600 * k, 130, 600 * k, BLUE, 0.88, 0); s.text("LIFO inventory 600", 145, y0 - 300 * k + 5, 13, "#0B1F38", "middle", t=0.3)
    s.rect(80, y0 - 1000 * k, 130, 400 * k, TEAL, 0.88, 0.5); s.text("LIFO reserve 400", 145, y0 - 800 * k + 5, 13, "#0B1F38", "middle", t=0.8)
    s.text("FIFO inventory 1,000", 145, y0 - 1000 * k - 10, 13, YEL, "middle", t=1.0)
    s.arrow(220, y0 - 800 * k, 320, y0 - 800 * k, DIM, t=1.2)
    s.rect(330, y0 - 1000 * k, 130, 100 * k, RED, 0.85, 1.6); s.text("tax 25%: 100", 470, y0 - 950 * k + 5, 13, RED, t=1.8)
    s.rect(330, y0 - 900 * k, 130, 300 * k, YEL, 0.85, 1.9); s.text("equity +300", 470, y0 - 750 * k + 5, 13, YEL, t=2.1)
    s.raw(f'<line x1="60" y1="{y0}" x2="610" y2="{y0}" stroke="{RULE}"/>')
    s.text("(deferred or current tax)", 470, y0 - 950 * k + 21, 11, DIM, italic=True, t=1.9)
    return s.svg()


# ---------------------------------------------------------------- 17 write-downs
def lcm_band():
    s = S(640, 280, "US GAAP lower of cost or market for LIFO: market is replacement cost, kept between a floor and a ceiling")
    x0, x1 = 60, 400
    Y = lambda v: 290 - (v - 30) * 10
    def hline(v, lab, c, t, dash=None):
        s.line([(x0, Y(v)), (x1, Y(v))], c, 2, t, dash=dash)
        s.text(f"{lab} {v}", x1 + 8, Y(v) + 4, 13, c, t=t + 0.3)
    s.rect(x0, Y(45), x1 - x0, Y(40) - Y(45), TEAL, 0.18, 0.6, cls="f")
    hline(50, "cost", SOFT, 0, "6 4")
    hline(45, "ceiling = NRV", TEAL, 0.3)
    hline(40, "floor = NRV − margin", TEAL, 0.5)
    hline(38, "replacement cost", BLUE, 0.8, "3 3")
    s.arrow(320, Y(38) + 2, 320, Y(40) + 4, YEL, t=1.4)
    s.text("market = 40 (replacement cost is below the floor, so the floor applies)", 80, 40, 13, YEL, t=1.8)
    s.text("write down from 50 to 40", 80, 60, 13, SOFT, italic=True, t=2.0)
    return s.svg()


# ---------------------------------------------------------------- 18 inventory ratios
def ccc_timeline():
    s = S(640, 250, "Cash conversion cycle: 50 days on the shelf plus 40 days to collect, minus 35 days of supplier credit = 55 days")
    x0, k = 50, 5.6
    y = 80
    s.rect(x0, y, 50 * k, 34, TEAL, 0.85, 0, cls="gx" if False else "f"); s.text("inventory on hand 50 days", x0 + 25 * k, y + 22, 13, "#0B1F38", "middle", t=0.3)
    s.rect(x0 + 50 * k, y, 40 * k, 34, BLUE, 0.85, 0.5, cls="f"); s.text("collection 40 days", x0 + 70 * k, y + 22, 13, "#0B1F38", "middle", t=0.8)
    s.rect(x0, y + 50, 35 * k, 30, RED, 0.75, 1.0, cls="f"); s.text("supplier credit 35 days", x0 + 17.5 * k, y + 70, 12, INK, "middle", t=1.2)
    s.rect(x0 + 35 * k, y + 96, 55 * k, 30, YEL, 0.85, 1.5, cls="f"); s.text("cash tied up: 55 days", x0 + 62.5 * k, y + 116, 13, "#0B1F38", "middle", t=1.8)
    for d, lab in ((0, "buy goods"), (35, "pay supplier"), (50, "sell"), (90, "collect cash")):
        s.raw(f'<line x1="{x0 + d * k:.1f}" y1="60" x2="{x0 + d * k:.1f}" y2="215" stroke="{RULE}" stroke-dasharray="3 3"/>')
        s.text(lab, x0 + d * k, 52, 12, SOFT, "middle", True, cls="")
        s.text(f"day {d}", x0 + d * k, 232, 11, DIM, "middle", cls="")
    return s.svg()


# ---------------------------------------------------------------- 19 capitalise or expense
def cap_cash_buckets():
    s = S(640, 275, "Spending of 100: expensing puts it in operating cash flow, capitalising moves it to investing")
    y0 = 130
    s.raw(f'<line x1="60" y1="{y0}" x2="610" y2="{y0}" stroke="{RULE}"/>')
    def pair(x, title, cfo, cfi, t0):
        s.text(title, x + 95, 40, 14, INK, "middle", cls="")
        for j, (lab, v, c) in enumerate((("CFO", cfo, BLUE), ("CFI", cfi, TEAL))):
            bx = x + j * 110
            if v:
                s.rect(bx, y0, 80, v * 0.9, c, 0.88, t0 + j * 0.3, cls="f")
                s.text(f"−{v}", bx + 40, y0 + v * 0.9 + 16, 13, c, "middle", t=t0 + j * 0.3 + 0.3)
            else:
                s.text("0", bx + 40, y0 - 8, 13, c, "middle", t=t0 + j * 0.3 + 0.3)
            s.text(lab, bx + 40, y0 - 24 if v else y0 - 24, 12, SOFT, "middle", cls="")
    pair(70, "expensed", 100, 0, 0)
    pair(360, "capitalised", 0, 100, 0.8)
    s.text("same cash out; capitalising makes operating cash flow look 100 better", 335, 266, 12, YEL, "middle", True, t=1.8)
    return s.svg()


# ---------------------------------------------------------------- 20 revaluation
def reval_routes():
    s = S(640, 280, "Where revaluation changes go: increases to OCI unless they reverse an earlier loss; decreases to profit unless they reverse an earlier surplus")
    s.box(230, 30, 180, 44, "Revaluation change", SOFT, size=14, t=0)
    s.box(70, 110, 200, 44, "Increase", BLUE, size=14, t=0.4)
    s.box(370, 110, 200, 44, "Decrease", RED, size=14, t=0.4)
    s.arrow(300, 74, 190, 108, DIM, t=0.3); s.arrow(340, 74, 450, 108, DIM, t=0.3)
    s.box(20, 200, 140, 52, "OCI surplus", YEL, size=13, t=1.0, sub="the normal case")
    s.box(170, 200, 140, 52, "Profit", BLUE, size=13, t=1.2, sub="reverses an old loss")
    s.box(330, 200, 140, 52, "Profit", RED, size=13, t=1.4, sub="the normal case")
    s.box(480, 200, 140, 52, "OCI surplus falls", YEL, size=13, t=1.6, sub="reverses a surplus")
    for a, b, t in ((140, 90, 0.8), (200, 240, 0.9), (440, 400, 1.1), (500, 550, 1.2)):
        s.arrow(a, 154, b, 198, DIM, t=t)
    return s.svg()


# ---------------------------------------------------------------- 21 deferred tax
def dt_matrix():
    s = S(640, 270, "Compare carrying amount with tax base: four cases, two deferred tax liabilities and two deferred tax assets")
    s.raw(f'<line x1="330" y1="50" x2="330" y2="240" stroke="{RULE}"/><line x1="120" y1="145" x2="610" y2="145" stroke="{RULE}"/>')
    s.text("carrying amount > tax base", 220, 40, 13, DIM, "middle", True, cls=""); s.text("carrying amount < tax base", 470, 40, 13, DIM, "middle", True, cls="")
    s.text("asset", 110, 100, 13, DIM, "end", True, cls=""); s.text("liability", 110, 200, 13, DIM, "end", True, cls="")
    cells = [(220, 95, "DTL", "faster tax depreciation", RED), (470, 95, "DTA", "asset written down only in the books", TEAL),
             (220, 195, "DTA", "warranty provision deductible later", TEAL), (470, 195, "DTL", "rare: tax-deductible liability", RED)]
    for i, (x, y, a, b, c) in enumerate(cells):
        s.text(a, x, y, 22, c, "middle", t=i * 0.3)
        s.text(b, x, y + 22, 12, SOFT, "middle", True, t=i * 0.3 + 0.15)
    return s.svg()


# ---------------------------------------------------------------- 22 rate change and valuation allowance
def dt_rate_change():
    s = S(640, 270, "A tax rate change remeasures every deferred tax balance at once, through tax expense")
    y0, k = 230, 0.27
    def bar(x, v, c, lab, t):
        s.rect(x, y0 - v * k, 70, v * k, c, 0.88, t)
        s.text(str(v), x + 35, y0 - v * k - 8, 13, c, "middle", t=t + 0.3)
        s.text(lab, x + 35, y0 + 18, 12, SOFT, "middle", cls="")
    s.text("deferred tax asset", 150, 36, 13, TEAL, "middle", cls="")
    bar(70, 300, TEAL, "at 30%", 0); bar(160, 250, TEAL, "at 25%", 0.5)
    s.text("tax expense +50", 150, 60, 13, RED, "middle", True, t=1.0)
    s.text("deferred tax liability", 470, 36, 13, RED, "middle", cls="")
    bar(390, 400, RED, "at 20%", 1.2); bar(480, 500, RED, "at 25%", 1.6)
    s.text("tax expense +100", 470, 60, 13, RED, "middle", True, t=2.0)
    s.raw(f'<line x1="50" y1="{y0}" x2="610" y2="{y0}" stroke="{RULE}"/>')
    return s.svg()


# ---------------------------------------------------------------- 23 bonds
def _bond_path(face, cpn, mkt, n):
    pv = sum(face * cpn / (1 + mkt) ** t for t in range(1, n + 1)) + face / (1 + mkt) ** n
    path = [pv]
    for _ in range(n):
        pv = pv * (1 + mkt) - face * cpn
        path.append(pv)
    return path


def bond_carrying_paths():
    s = S(640, 280, "Carrying amounts pulled to face value: a discount bond rises, a premium bond falls")
    x0, y0, x1, y1 = frame(s, "year", "carrying amount", 70, 240, 600, 40)
    X = lambda t: x0 + t / 5 * (x1 - x0); Y = lambda v: y0 - (v - 880) / 240 * (y0 - y1)
    disc, prem = _bond_path(1000, .05, .07, 5), _bond_path(1000, .05, .03, 5)
    _grid_y(s, x0, x1, [Y(v) for v in (900, 1000, 1100)])
    for v in (900, 1000, 1100):
        s.text(f"{v:,}", x0 - 8, Y(v) + 4, 11, DIM, "end", cls="")
    for t in range(6):
        s.text(str(t), X(t), y0 + 16, 11, DIM, "middle", cls="")
    s.line([(X(t), Y(v)) for t, v in enumerate(disc)], BLUE, 2.6, 0)
    s.line([(X(t), Y(v)) for t, v in enumerate(prem)], TEAL, 2.6, 0.6)
    s.line([(X(0), Y(1000)), (X(5), Y(1000))], YEL, 1.2, 1.2, dash="5 4")
    s.text(f"discount bond: issued at {disc[0]:,.1f} (market rate 7%)", X(2.2), Y(918), 12, BLUE, t=1.2)
    s.text(f"premium bond: issued at {prem[0]:,.1f} (market rate 3%)", X(2.2), Y(1082), 12, TEAL, t=1.6)
    s.text("face 1,000", X(5), Y(1000) - 8, 12, YEL, "end", t=1.8)
    return s.svg()


# ---------------------------------------------------------------- 24 derecognition
def derecog_cases():
    s = S(640, 260, "Gain or loss on retiring debt = carrying amount minus the price paid")
    y0, base, k = 220, 850, 1.05
    def case(x, carry, paid, title, t0):
        s.text(title, x + 95, 30, 13, INK, "middle", cls="")
        s.rect(x, y0 - (carry - base) * k, 80, (carry - base) * k, BLUE, 0.85, t0); s.text(f"carried {carry}", x + 40, y0 + 18, 12, BLUE, "middle", cls="")
        s.rect(x + 110, y0 - (paid - base) * k, 80, (paid - base) * k, TEAL, 0.85, t0 + 0.4); s.text(f"paid {paid}", x + 150, y0 + 18, 12, TEAL, "middle", cls="")
        d = carry - paid
        c = YEL if d > 0 else RED
        s.text(("gain " if d > 0 else "loss ") + str(abs(d)), x + 95, y0 - (max(carry, paid) - base) * k - 12, 15, c, "middle", t=t0 + 0.9)
    s.text("axis starts at 850", 620, 250, 11, DIM, "end", True, cls="")
    case(60, 960, 990, "called above book value", 0)
    case(360, 980, 900, "bought back after rates rose", 1.0)
    s.raw(f'<line x1="40" y1="{y0}" x2="620" y2="{y0}" stroke="{RULE}"/>')
    return s.svg()


# ---------------------------------------------------------------- 25 credit analysis
def credit_compare():
    s = S(640, 270, "Two borrowers: coverage (times interest is earned) and leverage (years of EBITDA to repay debt)")
    def panel(x, title, vals, unit, maxv, good):
        s.text(title, x + 120, 34, 13, INK, "middle", cls="")
        for i, (name, v, c) in enumerate(vals):
            y = 60 + i * 70
            w = v / maxv * 200
            s.rect(x, y, w, 36, c, 0.88, i * 0.4, cls="f")
            s.text(f"{name}: {v:g}{unit}", x + 4, y + 52, 12, SOFT, t=i * 0.4 + 0.3)
        s.text(good, x, 240, 11, DIM, italic=True, cls="")
    panel(50, "EBIT ÷ interest", [("A", 12, BLUE), ("B", 3, RED)], "×", 14, "higher is safer")
    panel(350, "Debt ÷ EBITDA", [("A", 1.6, BLUE), ("B", 4.5, RED)], "×", 5.5, "lower is safer")
    return s.svg()


# ---------------------------------------------------------------- 26 analyst adjustments
def roe_adjust():
    s = S(640, 260, "Removing goodwill reverses the ranking: reported ROE favours A, tangible ROE favours B")
    y0, k = 210, 7
    groups = [("reported ROE", 15, 12), ("tangible ROE", 15, 17.1)]
    for i, (lab, a, b) in enumerate(groups):
        gx = 120 + i * 250
        for j, (v, c, n) in enumerate(((a, BLUE, "A"), (b, TEAL, "B"))):
            x = gx + j * 80
            s.rect(x, y0 - v * k, 60, v * k, c, 0.88, i * 0.8 + j * 0.3)
            s.text(f"{n} {v:g}%", x + 30, y0 - v * k - 8, 13, c, "middle", t=i * 0.8 + j * 0.3 + 0.3)
        s.text(lab, gx + 70, y0 + 20, 13, SOFT, "middle", cls="")
    s.raw(f'<line x1="80" y1="{y0}" x2="560" y2="{y0}" stroke="{RULE}"/>')
    s.text("B: 120 ÷ (1,000 − 300 goodwill) = 17.1%", 320, 250, 12, YEL, "middle", True, t=2.0)
    return s.svg()


# ---------------------------------------------------------------- 27 price elasticity
def revenue_elasticity():
    s = S(640, 290, "On demand Q = 100 − P, total revenue peaks at P = 50, where elasticity is −1")
    x0, y0, x1, y1 = frame(s, "price", "total revenue", 70, 250, 600, 40)
    X = lambda p: x0 + p / 100 * (x1 - x0); Y = lambda r: y0 - r / 2700 * (y0 - y1)
    s.rect(X(0), y1, X(50) - X(0), y0 - y1, TEAL, 0.07, 0, cls="f")
    s.rect(X(50), y1, X(100) - X(50), y0 - y1, BLUE, 0.07, 0, cls="f")
    s.curve(lambda p: p * (100 - p), 0, 100, X, Y, color=YEL, width=2.8, t=0.2)
    s.line([(X(50), y0), (X(50), Y(2500))], SOFT, 1.2, 1.0, dash="4 4")
    s.dot(X(50), Y(2500), 5, YEL, 1.2)
    s.text("max revenue 2,500 at P = 50", X(50), Y(2500) - 12, 13, YEL, "middle", t=1.4)
    s.text("inelastic: raise price,", X(25), Y(700), 12, TEAL, "middle", True, t=1.6)
    s.text("revenue rises", X(25), Y(700) + 15, 12, TEAL, "middle", True, t=1.6)
    s.text("elastic: cut price,", X(75), Y(700), 12, BLUE, "middle", True, t=1.8)
    s.text("revenue rises", X(75), Y(700) + 15, 12, BLUE, "middle", True, t=1.8)
    s.dot(X(70), Y(2100), 5, BLUE, 2.0); s.text("P = 70: E = −2.33", X(70) - 10, Y(1500), 12, BLUE, "end", t=2.1)
    for p in (0, 25, 50, 75, 100):
        s.text(str(p), X(p), y0 + 16, 11, DIM, "middle", cls="")
    return s.svg()


# ---------------------------------------------------------------- 28 income and cross elasticity
def demand_shift_income():
    s = S(640, 280, "A rise in income shifts demand right for a normal good and left for an inferior good")
    def panel(x, title, shift, c):
        X = lambda q: x + 20 + q * 2.4; Y = lambda p: 240 - p * 1.9
        s.raw(f'<path d="M{x + 20},{Y(100):.0f} L{x + 20},240 L{x + 270},240" fill="none" stroke="{RULE}"/>')
        s.text("price", x + 26, Y(100) - 6, 11, DIM, italic=True, cls=""); s.text("quantity", x + 270, 256, 11, DIM, "end", True, cls="")
        s.line([(X(0), Y(90)), (X(80), Y(10))], SOFT, 2.2, 0)
        s.line([(X(shift), Y(90)), (X(80 + shift), Y(10))], c, 2.6, 0.8)
        s.text("D₀", X(80) + 4, Y(10) - 4, 12, SOFT, t=0.4)
        s.text("D₁", X(80 + shift) + 4, Y(10) - 4, 12, c, t=1.2)
        s.arrow(X(40) + 4, Y(50), X(40 + shift) - 4 if shift > 0 else X(40 + shift) + 4, Y(50), c, t=1.4)
        s.text(title, x + 145, 30, 14, c, "middle", cls="")
    panel(20, "normal good: income ↑", 18, BLUE)
    panel(330, "inferior good: income ↑", -18, RED)
    return s.svg()


# ---------------------------------------------------------------- 29 substitution and income effects
def effect_decomp():
    s = S(640, 260, "A price fall: substitution effect +15 units, income effect −3, total +12 (an inferior good, but not a Giffen good)")
    y0, k = 170, 6
    bars = [("substitution", 0, 15, BLUE), ("income", 15, 12, RED), ("total", 0, 12, YEL)]
    for i, (lab, a, b, c) in enumerate(bars):
        x = 120 + i * 150
        lo, hi = min(a, b), max(a, b)
        s.rect(x, y0 - hi * k, 90, (hi - lo) * k, c, 0.88, i * 0.5)
        s.text(f"{b - a:+}", x + 45, y0 - hi * k - 8, 15, c, "middle", t=i * 0.5 + 0.3)
        s.text(lab, x + 45, y0 + 20, 13, SOFT, "middle", cls="")
    s.raw(f'<line x1="90" y1="{y0}" x2="590" y2="{y0}" stroke="{RULE}"/>')
    s.text("change in quantity demanded", 90, 40, 12, DIM, italic=True, cls="")
    s.text("Giffen good: the income effect would be larger than +15, so the total turns negative", 340, 235, 12, SOFT, "middle", True, t=1.8)
    return s.svg()


# ---------------------------------------------------------------- 30 marginal returns / returns to scale
def lrac():
    s = S(640, 280, "Long-run average cost: economies of scale, then a flat range from the minimum efficient scale, then diseconomies")
    x0, y0, x1, y1 = frame(s, "output", "long-run average cost", 70, 240, 600, 40)
    X = lambda q: x0 + q / 100 * (x1 - x0); Y = lambda c: y0 - c / 100 * (y0 - y1)
    def f(q):
        if q < 35: return 30 + (35 - q) ** 2 * 0.05
        if q < 70: return 30
        return 30 + (q - 70) ** 2 * 0.06
    s.curve(f, 5, 98, X, Y, color=YEL, width=2.8, t=0)
    s.line([(X(35), y0), (X(35), Y(30))], SOFT, 1, 1.0, dash="4 4")
    s.text("minimum efficient scale", X(35), y0 + 18, 12, SOFT, "middle", t=1.2)
    s.text("economies of scale", X(20), Y(85), 13, BLUE, "middle", True, t=1.4)
    s.text("constant returns", X(52), Y(24), 13, TEAL, "middle", True, t=1.6)
    s.text("diseconomies", X(84), Y(85), 13, RED, "middle", True, t=1.8)
    return s.svg()


# ---------------------------------------------------------------- 31 short-run costs
_FC, _VC = 100, [40, 70, 95, 125, 165, 215, 275]


def atc_stack():
    s = S(640, 290, "Average total cost = average fixed cost + average variable cost; fixed cost per unit shrinks as output grows")
    y0, k = 250, 1.4
    for q in range(1, 8):
        x = 70 + (q - 1) * 74
        afc, avc = _FC / q, _VC[q - 1] / q
        s.rect(x, y0 - avc * k, 46, avc * k, BLUE, 0.88, q * 0.12)
        s.rect(x, y0 - (avc + afc) * k, 46, afc * k, TEAL, 0.7, 0.5 + q * 0.12)
        s.text(f"{afc + avc:.1f}", x + 23, y0 - (avc + afc) * k - 6, 11, YEL if q == 6 else SOFT, "middle", t=1.2 + q * 0.1)
        s.text(str(q), x + 23, y0 + 16, 11, DIM, "middle", cls="")
    s.raw(f'<line x1="60" y1="{y0}" x2="600" y2="{y0}" stroke="{RULE}"/>')
    s.text("output", 600, y0 + 32, 12, DIM, "end", True, cls="")
    s.rect(400, 40, 10, 10, BLUE, 0.9, cls=""); s.text("AVC", 415, 49, 12, SOFT, cls="")
    s.rect(460, 40, 10, 10, TEAL, 0.9, cls=""); s.text("AFC", 475, 49, 12, SOFT, cls="")
    s.text("minimum ATC 52.5 at 6 units", 400, 70, 12, YEL, t=2.0)
    return s.svg()


# ---------------------------------------------------------------- 32 shutdown
def price_zones():
    s = S(640, 220, "Three price zones: shut down below minimum AVC, operate at a loss between AVC and ATC, profit above minimum ATC")
    x0, x1 = 60, 600
    X = lambda p: x0 + (p - 20) / 45 * (x1 - x0)
    zones = [(20, 31.25, RED, "shut down"), (31.25, 52.5, BLUE, "operate at a loss"), (52.5, 65, TEAL, "economic profit")]
    for i, (a, b, c, lab) in enumerate(zones):
        s.rect(X(a), 80, X(b) - X(a), 50, c, 0.75, i * 0.4, cls="f")
        s.text(lab, (X(a) + X(b)) / 2, 110, 13, INK, "middle", t=i * 0.4 + 0.3)
    for p, lab in ((31.25, "min AVC 31.25"), (52.5, "min ATC 52.5")):
        s.raw(f'<line x1="{X(p):.1f}" y1="70" x2="{X(p):.1f}" y2="150" stroke="{YEL}" stroke-width="1.5"/>')
        s.text(lab, X(p), 168, 13, YEL, "middle", t=1.4)
    s.text("price →", x1, 60, 12, DIM, "end", True, cls="")
    s.dot(X(40), 140, 5, INK, 1.8); s.text("P = 40: produce 5, lose 65 (less than the 100 of fixed cost)", X(40) - 8, 195, 12, SOFT, t=2.0)
    return s.svg()


# ---------------------------------------------------------------- 33 market structures: HHI as an area
def hhi_areas():
    s = S(640, 300, "The HHI is the total area of squares whose sides are the market shares: 40, 30, 20 and 10 give 3,000")
    shares = [(40, BLUE), (30, TEAL), (20, YEL), (10, RED)]
    k = 4.0
    x = 40
    for i, (sh, c) in enumerate(shares):
        side = sh * k
        s.rect(x, 265 - side, side, side, c, 0.75, i * 0.4, cls="f", stroke=c)
        s.text(f"{sh}² = {sh * sh:,}", x + side / 2, 265 - side - 8, 13, c, "middle", t=i * 0.4 + 0.3)
        s.text(f"{sh}%", x + side / 2, 284, 12, SOFT, "middle", cls="")
        x += side + 14
    s.text("HHI = 1,600 + 900 + 400 + 100 = 3,000", 40, 30, 15, INK, t=1.8)
    s.text("big firms dominate the total: squaring makes size count more than proportionally", 40, 52, 12, SOFT, italic=True, t=2.1)
    return s.svg()


# ---------------------------------------------------------------- 34 perfect competition
def lr_entry():
    s = S(640, 280, "Entry shifts market supply right until price falls to minimum average total cost and economic profit is zero")
    x0, y0, x1, y1 = frame(s, "market quantity", "price", 70, 240, 600, 40)
    X = lambda q: x0 + q / 100 * (x1 - x0); Y = lambda p: y0 - p / 20 * (y0 - y1)
    s.line([(X(0), Y(21)), (X(90), Y(3))], SOFT, 2.2, 0)
    s.text("demand", X(90), Y(3) - 8, 12, SOFT, "end", t=0.3)
    s.line([(X(0), Y(8)), (X(50), Y(20))], BLUE, 2.4, 0.3)
    s.text("S₀", X(50) + 6, Y(20) + 4, 12, BLUE, t=0.6)
    s.line([(X(27), Y(8)), (X(77), Y(20))], TEAL, 2.4, 1.0)
    s.text("S₁ after entry", X(77) + 6, Y(20) + 4, 12, TEAL, t=1.3)
    s.line([(x0, Y(12)), (x1, Y(12))], YEL, 1.4, 1.5, dash="5 4")
    s.text("min ATC = 12", x0 + 6, Y(12) - 6, 12, YEL, t=1.7)
    q0 = 13 / 0.44; q1 = (21 - 8 + 0.24 * 27) / 0.44
    s.dot(X(q0), Y(21 - 0.2 * q0), 5, BLUE, 0.8); s.text("P = 15: profit attracts entry", X(q0) - 12, Y(21 - 0.2 * q0) - 30, 12, BLUE, "end", t=0.9)
    s.dot(X(q1), Y(21 - 0.2 * q1), 5, TEAL, 1.8); s.text("P ≈ 12: zero economic profit", X(q1) + 8, Y(21 - 0.2 * q1) + 18, 12, TEAL, t=2.0)
    return s.svg()


# ---------------------------------------------------------------- 35 monopoly
def natural_monopoly():
    s = S(640, 290, "A natural monopoly: average cost falls over the whole market, so one firm is cheapest; regulators choose between two prices")
    x0, y0, x1, y1 = frame(s, "quantity", "price, cost", 70, 250, 600, 40)
    X = lambda q: x0 + q / 100 * (x1 - x0); Y = lambda p: y0 - p / 100 * (y0 - y1)
    s.line([(X(0), Y(90)), (X(90), Y(0))], SOFT, 2.2, 0); s.text("demand", X(22), Y(72), 12, SOFT, t=0.3)
    s.curve(lambda q: 15 + 1200 / (q + 12), 4, 98, X, Y, color=BLUE, width=2.4, t=0.4); s.text("ATC", X(97), Y(15 + 1200 / 110) - 8, 12, BLUE, "end", t=0.8)
    s.line([(X(0), Y(15)), (X(100), Y(15))], TEAL, 2, 0.6); s.text("MC", X(100), Y(15) + 16, 12, TEAL, "end", t=0.9)
    # average cost pricing: demand = ATC: 90 - q = 15 + 1200/(q+12)
    qa = next(q / 10 for q in range(200, 900) if (90 - q / 10) - (15 + 1200 / (q / 10 + 12)) > 0 and (90 - (q + 1) / 10) - (15 + 1200 / ((q + 1) / 10 + 12)) <= 0)
    s.dot(X(qa), Y(90 - qa), 5, YEL, 1.4); s.text(f"average-cost price ≈ {90 - qa:.0f}: firm breaks even", X(qa) + 4, Y(90 - qa) - 34, 12, YEL, t=1.6)
    s.dot(X(75), Y(15), 5, RED, 1.9); s.text("marginal-cost price 15: efficient, but a loss", X(75) - 12, Y(15) + 24, 12, RED, "end", t=2.1)
    return s.svg()


# ---------------------------------------------------------------- 36 price discrimination
def third_degree():
    s = S(640, 290, "Third-degree price discrimination with marginal cost 10: the less price-sensitive market pays 30, the other 20")
    def panel(x, a, title, c):
        X = lambda q: x + 30 + q * 4.6; Y = lambda p: 240 - p * 3.6
        s.raw(f'<path d="M{x + 30},{Y(55):.0f} L{x + 30},240 L{x + 280},240" fill="none" stroke="{RULE}"/>')
        s.line([(X(0), Y(a)), (X(a), Y(0))], SOFT, 2.2, 0)
        s.line([(X(0), Y(a)), (X(a / 2), Y(0))], BLUE, 1.8, 0.4, dash="5 4")
        s.line([(X(0), Y(10)), (X(52), Y(10))], TEAL, 1.6, 0.6)
        q = (a - 10) / 2
        s.line([(X(q), Y(10)), (X(q), Y(a - q))], DIM, 1, 1.0, dash="3 3")
        s.dot(X(q), Y(a - q), 5, YEL, 1.2)
        s.text(f"Q = {q:g}, P = {a - q:g}", X(q) + 8, Y(a - q) - 6, 13, YEL, t=1.4)
        s.text(title, x + 155, 28, 14, c, "middle", cls="")
        s.text(f"P = {a} − Q", X(a) - 2, Y(0) - 8, 11, SOFT, "end", cls="")
        s.text("MC = 10", X(52), Y(10) - 6, 11, TEAL, "end", cls="")
    panel(10, 50, "market A: less elastic", INK)
    panel(330, 30, "market B: more elastic", INK)
    s.text("blue: marginal revenue; set MR = MC in each market", 320, 280, 12, DIM, "middle", True, cls="")
    return s.svg()


# ---------------------------------------------------------------- 37 GDP
def value_added():
    s = S(640, 260, "Value added: count each stage's contribution once; the final price of the bread equals GDP")
    stages = [("farmer: wheat", 20, 20, BLUEB), ("miller: flour", 50, 30, BLUE), ("baker: bread", 100, 50, TEAL)]
    y0, k = 210, 1.5
    for i, (lab, sale, va, c) in enumerate(stages):
        x = 70 + i * 150
        s.rect(x, y0 - (sale - va) * k, 90, (sale - va) * k, DIM, 0.35, i * 0.5, cls="f")
        s.rect(x, y0 - sale * k, 90, va * k, c, 0.9, i * 0.5 + 0.2)
        s.text(f"+{va}", x + 45, y0 - sale * k + va * k / 2 + 5, 14, "#0B1F38", "middle", t=i * 0.5 + 0.5)
        s.text(f"sells for {sale}", x + 45, y0 - sale * k - 8, 12, SOFT, "middle", t=i * 0.5 + 0.4)
        s.text(lab, x + 45, y0 + 18, 12, SOFT, "middle", cls="")
    s.raw(f'<line x1="50" y1="{y0}" x2="560" y2="{y0}" stroke="{RULE}"/>')
    s.text("GDP = 20 + 30 + 50 = 100", 70, 36, 14, YEL, t=1.8)
    s.text("not 20 + 50 + 100 = 170", 70, 56, 12, RED, italic=True, t=2.0)
    return s.svg()


# ---------------------------------------------------------------- 38 saving and investment
def sector_balances():
    s = S(640, 270, "Sector balances always sum to zero: private surplus +2, government deficit −5, so the rest of the world lends +3")
    y0, k = 130, 14
    bars = [("private (S − I)", 2, BLUE), ("government (T − G)", -5, RED), ("rest of world (M − X)", 3, TEAL)]
    for i, (lab, v, c) in enumerate(bars):
        x = 90 + i * 170
        top, h = (y0 - v * k, v * k) if v > 0 else (y0, -v * k)
        s.rect(x, top, 100, h, c, 0.88, i * 0.5, cls="f")
        s.text(f"{v:+}% of GDP", x + 50, (top - 8) if v > 0 else (top + h + 18), 13, c, "middle", t=i * 0.5 + 0.3)
        s.text(lab, x + 50, 250, 12, SOFT, "middle", cls="")
    s.raw(f'<line x1="60" y1="{y0}" x2="600" y2="{y0}" stroke="{RULE}"/>')
    s.text("trade balance X − M = −3%", 470, 40, 13, YEL, t=1.8)
    return s.svg()


# ---------------------------------------------------------------- 39 AD-AS
def ad_adjust():
    s = S(640, 300, "A demand boom: output rises above potential, then wages catch up, short-run supply shifts left and output returns to potential at a higher price level")
    x0, y0, x1, y1 = frame(s, "real GDP", "price level", 70, 260, 600, 40)
    X = lambda q: x0 + q / 100 * (x1 - x0); Y = lambda p: y0 - p / 100 * (y0 - y1)
    s.line([(X(50), Y(4)), (X(50), Y(96))], DIM, 1.6, 0, dash="5 4"); s.text("LRAS (potential)", X(50) + 6, Y(96) + 4, 12, DIM, t=0.1)
    s.line([(X(25), Y(70)), (X(85), Y(10))], BLUE, 2.4, 0.2); s.text("AD₀", X(85) + 4, Y(10) + 4, 12, BLUE, t=0.4)
    s.line([(X(15), Y(10)), (X(85), Y(80))], TEAL, 2.4, 0.3); s.text("SRAS₀", X(85) + 4, Y(80) + 4, 12, TEAL, t=0.5)
    s.line([(X(40), Y(75)), (X(95), Y(20))], BLUE, 2.4, 0.9); s.text("AD₁", X(95) + 4, Y(20) + 4, 12, BLUE, t=1.1)
    s.line([(X(5), Y(20)), (X(72), Y(87))], RED, 2.4, 2.0); s.text("SRAS₁", X(72) + 4, Y(87) + 4, 12, RED, t=2.2)
    s.dot(X(50), Y(45), 6, YEL, 0.6); s.text("1", X(50) - 16, Y(45) + 5, 13, YEL, t=0.7)
    for i, txt in enumerate(["1: start at potential", "2: boom, output above potential", "3: wages catch up, higher prices"]):
        s.text(txt, x0 + 10, Y(93) + i * 17, 12, YEL, t=0.7 + i * 0.9)
    s.dot(X(60), Y(55), 6, YEL, 1.4); s.text("2", X(60) + 10, Y(55) + 18, 13, YEL, t=1.5)
    s.dot(X(50), Y(65), 6, YEL, 2.5); s.text("3", X(50) - 18, Y(65) - 4, 13, YEL, t=2.6)
    return s.svg()


# ---------------------------------------------------------------- 40 growth
def capital_deepening():
    s = S(640, 290, "Output per worker rises with capital per worker, but by less each time; better technology lifts the whole curve")
    x0, y0, x1, y1 = frame(s, "capital per worker", "output per worker", 70, 250, 600, 40)
    X = lambda k: x0 + k / 100 * (x1 - x0); Y = lambda y: y0 - y / 100 * (y0 - y1)
    f = lambda k: 9 * k ** 0.4
    s.curve(f, 0, 100, X, Y, color=BLUE, width=2.4, t=0.2); s.text("today's technology", X(100), Y(f(100)) + 26, 12, BLUE, "end", t=0.6)
    s.curve(lambda k: 1.3 * f(k), 0, 100, X, Y, color=TEAL, width=2.4, t=1.6); s.text("higher TFP", X(100), Y(1.3 * f(100)) - 8, 12, TEAL, "end", t=1.9)
    for i, (a, b) in enumerate([(10, 30), (50, 70)]):
        s.line([(X(a), Y(f(a))), (X(b), Y(f(a))), (X(b), Y(f(b)))], YEL, 1.6, 0.8 + i * 0.4)
        s.text(f"+{f(b) - f(a):.1f}", X(b) + 6, Y((f(a) + f(b)) / 2) + 4, 12, YEL, t=1.0 + i * 0.4)
    s.text("same +20 of capital, smaller gain each time", X(8), Y(92), 12, YEL, t=1.3)
    return s.svg()


# ---------------------------------------------------------------- 41 business cycle
def indicator_timing():
    s = S(640, 280, "Leading indicators turn before the economy, coincident indicators with it, lagging indicators after it")
    x0, y0, x1, y1 = frame(s, "time", "", 40, 240, 610, 40)
    X = lambda t: x0 + t / 100 * (x1 - x0)
    rows = [("leading: building permits, share prices", 12, TEAL, 0.0), ("coincident: output, retail sales", 0, BLUE, 0.6), ("lagging: unemployment duration, unit labour costs", -12, RED, 1.2)]
    for lab, sh, c, t in rows:
        s.curve(lambda u, sh=sh: math.sin((u + sh - 20) / 100 * 2 * math.pi), 0, 100, X, lambda v: 150 - 70 * v, color=c, width=2.4, t=t)
    s.text("leading: building permits, share prices", 50, 30, 12, TEAL, t=0.3)
    s.text("coincident: output, retail sales", 300, 30, 12, BLUE, t=0.9)
    s.text("lagging: unemployment duration", 50, 50, 12, RED, t=1.5)
    pk = 45
    s.line([(X(pk), 60), (X(pk), 230)], DIM, 1, 1.8, dash="4 4"); s.text("economy peaks", X(pk) + 6, 228, 12, DIM, t=2.0)
    return s.svg()


# ---------------------------------------------------------------- 42 unemployment
def labour_force_tree():
    s = S(640, 280, "Working-age population of 1,000 split into the labour force and those outside it; discouraged workers are outside")
    s.box(220, 24, 200, 46, "working-age population", BLUE, sub="1,000", t=0)
    s.box(60, 112, 220, 46, "labour force", TEAL, sub="640 (participation 64%)", t=0.6)
    s.box(360, 112, 220, 46, "not in labour force", DIM, sub="360", t=0.6)
    s.box(20, 206, 140, 46, "employed", TEAL, sub="600", t=1.2)
    s.box(180, 206, 140, 46, "unemployed", RED, sub="40 → rate 6.25%", t=1.4)
    s.box(360, 206, 220, 46, "includes discouraged", YEL, sub="20 want work, stopped looking", t=1.6)
    for a, b in [((320, 70), (170, 112)), ((320, 70), (470, 112)), ((170, 158), (90, 206)), ((170, 158), (250, 206)), ((470, 158), (470, 206))]:
        s.line([a, b], RULE, 1.2, 0.4)
    return s.svg()


# ---------------------------------------------------------------- 43 inflation
def laspeyres_paasche():
    s = S(640, 270, "Three price indexes for the same two years: the base-basket index is highest because it ignores substitution")
    vals = [("Laspeyres (old basket)", 1000 / 9, RED), ("Fisher (geometric mean)", (1000 / 9 * 104 / 96 * 100) ** 0.5, YEL), ("Paasche (new basket)", 104 / 96 * 100, TEAL)]
    for i, (lab, v, c) in enumerate(vals):
        y = 60 + i * 62
        w = (v - 100) * 30
        s.text(lab, 40, y + 22, 13, SOFT, t=i * 0.4)
        s.rect(240, y, w, 32, c, 0.85, i * 0.4, cls="gx")
        s.text(f"{v:.1f}", 240 + w + 10, y + 22, 14, c, t=i * 0.4 + 0.4)
    s.raw(f'<line x1="240" y1="44" x2="240" y2="250" stroke="{RULE}"/>')
    s.text("bars start at 100 (no change)", 240, 36, 12, DIM, italic=True, cls="")
    return s.svg()


# ---------------------------------------------------------------- 44 money
def deposit_rounds():
    s = S(640, 280, "Each round of lending creates a smaller new deposit; with a 10% reserve requirement 1,000 of reserves supports up to 10,000 of deposits")
    x0, y0 = 60, 230
    v = 1000
    for i in range(12):
        h = v / 1000 * 160
        s.rect(x0 + i * 40, y0 - h, 30, h, BLUE if i == 0 else TEAL, 0.85, i * 0.15)
        v *= 0.9
    s.raw(f'<line x1="50" y1="{y0}" x2="560" y2="{y0}" stroke="{RULE}"/>')
    s.text("1,000", x0 + 15, y0 - 166, 12, BLUE, "middle", t=0.2)
    s.text("900", x0 + 55, y0 - 150, 12, TEAL, "middle", t=0.35)
    s.text("810", x0 + 95, y0 - 136, 12, TEAL, "middle", t=0.5)
    s.text("deposit created in each round", 60, y0 + 22, 12, DIM, italic=True, cls="")
    s.text("1,000 + 900 + 810 + … = 1,000 ÷ 0.10 = 10,000", 300, 50, 14, YEL, "middle", t=2.0)
    return s.svg()


def money_layers():
    s = S(640, 260, "Money in layers: the central bank creates the monetary base; banks create most of narrow and broad money")
    s.box(30, 30, 580, 210, "", DIM, t=0); s.text("broad money: adds savings and time deposits", 46, 54, 13, DIM, t=0.2)
    s.box(60, 72, 520, 150, "", BLUE, t=0.5); s.text("narrow money: notes, coins and deposits you can spend now", 76, 96, 13, BLUE, t=0.7)
    s.box(90, 114, 250, 90, "monetary base", YEL, sub="notes, coins, bank reserves", t=1.0)
    s.text("most of the rest is created", 370, 150, 13, TEAL, t=1.4)
    s.text("by banks when they lend", 370, 170, 13, TEAL, t=1.4)
    return s.svg()


# ---------------------------------------------------------------- 45 quantity theory
def mv_py():
    s = S(640, 270, "In growth rates, money growth plus velocity growth equals inflation plus real growth")
    bars = [("money 7%", 7, BLUE), ("velocity 0%", 0, DIM), ("=", None, None), ("real growth 3%", 3, TEAL), ("inflation 4%", 4, RED)]
    base, k = 220, 20
    x = 60
    for i, (lab, v, c) in enumerate(bars):
        if v is None:
            s.text("=", x + 20, 160, 34, INK, "middle", t=1.0); x += 60; continue
        h = v * k
        s.rect(x, base - h, 90, h if h else 2, c, 0.85, i * 0.3)
        s.text(lab, x + 45, base + 22, 13, c, "middle", t=i * 0.3 + 0.2)
        x += 110
    s.text("%ΔM + %ΔV = %ΔP + %ΔY", 320, 46, 15, YEL, "middle", t=1.6)
    s.text("if velocity and output growth are steady, extra money growth becomes inflation", 320, 70, 12, SOFT, "middle", True, t=1.9)
    return s.svg()


# ---------------------------------------------------------------- 46 comparative advantage
def ppf_trade():
    s = S(640, 290, "Each country's production possibilities; trade lets both consume beyond their own frontier")
    x0, y0, x1, y1 = frame(s, "cloth", "wine", 60, 250, 610, 40)
    X = lambda c: x0 + c / 62 * (x1 - x0); Y = lambda w: y0 - w / 32 * (y0 - y1)
    s.line([(X(0), Y(30)), (X(60), Y(0))], BLUE, 2.4, 0.2); s.text("Atlantis frontier", X(1), Y(30) - 10, 12, BLUE, t=0.5)
    s.line([(X(0), Y(20)), (X(20), Y(0))], TEAL, 2.4, 0.5); s.text("Borealis frontier", X(2), Y(20) - 10, 12, TEAL, t=0.8)
    s.dot(X(30), Y(15), 5, BLUE, 1.0); s.text("no trade (30, 15)", X(30) - 4, Y(15) + 22, 12, BLUE, "end", t=1.1)
    s.dot(X(35), Y(15), 6, YEL, 1.8); s.text("with trade (35, 15)", X(35) + 10, Y(15) - 10, 12, YEL, t=1.9)
    s.dot(X(10), Y(10), 5, TEAL, 1.2); s.text("no trade (10, 10)", X(10) - 8, Y(10) + 20, 12, TEAL, "end", t=1.3)
    s.dot(X(15), Y(10), 6, YEL, 2.1); s.text("with trade (15, 10)", X(15) + 6, Y(10) + 24, 12, YEL, t=2.2)
    return s.svg()


# ---------------------------------------------------------------- 47 trade models
def ho_factor_prices():
    s = S(640, 270, "Heckscher–Ohlin: trade raises the return to each country's abundant factor and lowers the return to its scarce factor")
    s.text("capital-abundant country", 160, 34, 14, BLUE, "middle", t=0)
    s.text("labour-abundant country", 480, 34, 14, TEAL, "middle", t=0.2)
    s.box(50, 52, 220, 44, "exports capital-intensive goods", BLUE, size=13, t=0.4)
    s.box(370, 52, 220, 44, "exports labour-intensive goods", TEAL, size=13, t=0.6)
    rows = [("return to capital", "↑", "↓"), ("wages (esp. low-skilled)", "↓", "↑")]
    for i, (lab, a, b) in enumerate(rows):
        y = 140 + i * 56
        s.text(lab, 320, y + 6, 13, SOFT, "middle", t=1.0 + i * 0.3)
        s.text(a, 160, y + 10, 30, YEL if a == "↑" else RED, "middle", t=1.2 + i * 0.3)
        s.text(b, 480, y + 10, 30, YEL if b == "↑" else RED, "middle", t=1.2 + i * 0.3)
    s.text("Ricardo has one factor (labour), so it says nothing about this split", 320, 256, 12, DIM, "middle", True, cls="")
    return s.svg()


# ---------------------------------------------------------------- 48 balance of payments
def bop_ledger():
    s = S(640, 270, "A current account deficit of 100 is financed by a financial account inflow of 100: 70 of bond purchases and 30 of direct investment")
    base, k = 125, 0.8
    s.rect(110, base, 110, 100 * k, RED, 0.85, 0.2); s.text("current account −100", 165, base + 100 * k + 20, 13, RED, "middle", t=0.4)
    s.text("imports exceed exports", 165, base - 10, 12, DIM, "middle", True, cls="")
    s.rect(360, base - 70 * k, 110, 70 * k, BLUE, 0.85, 1.0); s.text("bonds bought by foreigners 70", 480, base - 35 * k + 4, 12, BLUE, t=1.2)
    s.rect(360, base - 100 * k, 110, 30 * k, TEAL, 0.85, 1.5); s.text("factory (FDI) 30", 480, base - 85 * k + 4, 12, TEAL, t=1.7)
    s.text("financial account +100", 415, base + 22, 13, INK, "middle", t=1.8)
    s.raw(f'<line x1="70" y1="{base}" x2="600" y2="{base}" stroke="{RULE}"/>')
    s.text("the two sides sum to zero (apart from errors and omissions)", 320, 256, 12, YEL, "middle", t=2.2)
    return s.svg()


# ---------------------------------------------------------------- 49 exchange rates
def fx_asymmetry():
    s = S(640, 250, "USD/EUR moves from 1.10 to 1.15: the euro gains 4.55% but the dollar loses only 4.35%")
    s.box(50, 40, 230, 60, "USD/EUR 1.10", DIM, sub="1 euro costs 1.10 dollars", t=0)
    s.box(360, 40, 230, 60, "USD/EUR 1.15", BLUE, sub="1 euro costs 1.15 dollars", t=0.4)
    s.arrow(285, 70, 355, 70, YEL, 0.6)
    s.text("euro: 1.15 ÷ 1.10 − 1 = +4.55%", 320, 150, 15, TEAL, "middle", t=1.2)
    s.text("dollar: 1.10 ÷ 1.15 − 1 = −4.35%", 320, 182, 15, RED, "middle", t=1.6)
    s.text("one currency's appreciation is not the same size as the other's depreciation", 320, 226, 12, DIM, "middle", True, cls="")
    return s.svg()


# ---------------------------------------------------------------- 50 trade balance
def absorption():
    s = S(640, 270, "The trade balance equals national income minus domestic spending; at full capacity it improves only if spending falls")
    base, k = 230, 1.6
    cols = [("before", 100, 104), ("depreciation, spending unchanged", 100, 104), ("spending cut", 100, 100)]
    for i, (lab, y, a) in enumerate(cols):
        x = 70 + i * 190
        s.rect(x, base - y * k, 50, y * k, BLUE, 0.85, i * 0.6)
        s.rect(x + 56, base - a * k, 50, a * k, RED if a > y else TEAL, 0.85, i * 0.6 + 0.2)
        s.text("income", x + 25, base + 18, 11, BLUE, "middle", cls="")
        s.text("spending", x + 81, base + 18, 11, SOFT, "middle", cls="")
        s.text(lab, x + 53, base + 36, 12, SOFT, "middle", True, cls="")
        tb = y - a
        s.text(f"trade balance {tb:+d}", x + 53, base - max(y, a) * k - 10, 13, YEL if tb == 0 else RED, "middle", t=i * 0.6 + 0.5)
    return s.svg()
