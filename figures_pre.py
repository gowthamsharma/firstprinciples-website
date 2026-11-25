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
