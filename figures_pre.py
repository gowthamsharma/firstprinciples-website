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
