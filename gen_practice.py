"""Write content/practice/*.md: one page of ten original Level I questions per topic (questions live in practice_bank.py)."""
import pathlib
from practice_bank import META, ORDER, TOPICS

ROOT = pathlib.Path(__file__).resolve().parent
UPDATED = "2026-11-22"

INFO = {
 "ethics": dict(fig="ethics_order", short="ethics",
   intro="Ethics is the topic candidates most often leave too late. The questions are short cases: someone does something, and you decide which Standard applies and whether it was broken. The trick is to read for the duty involved (to clients, to employers, to the market) before you look at the answers.",
   tips=["Name the Standard first, then decide. Most wrong answers describe a real rule that does not fit the facts.", "When local law and the Code differ, the stricter rule wins.", "Disclosure fixes many conflicts of interest, but not the use of material nonpublic information."],
   links=[("How to study ethics", "blog-ethics.html"), ("The hardest CFA topics", "blog-hardest-cfa-topics.html")]),
 "quant": dict(fig="tvm_signs", short="quantitative methods",
   intro="Quantitative methods carries 11–14% of Level I from 2027, as much as fixed income or equities. Most questions are either a calculation you should do in under ninety seconds on the BA II Plus, or a definition you need to state exactly (a Type I error, a p-value, what R² measures).",
   tips=["Enter cash flows with signs: money you pay is negative.", "Know which mean the question wants: arithmetic for one period ahead, geometric for what was actually earned.", "For probability questions, write the tree before you multiply."],
   links=[("The BA II Plus calculator guide", "blog-ba-ii-plus-calculator-guide.html"), ("Level I formula sheet", "blog-cfa-level-1-formula-sheet.html")]),
 "economics": dict(fig="elasticity_quadrants", short="economics",
   intro="Economics at Level I covers microeconomics (demand, costs, market structures), the business cycle, fiscal and monetary policy, trade and currencies. Calculations are short; most marks come from knowing which way something moves and why.",
   tips=["For exchange rates, write the quote as price currency / base currency and check units before you divide.", "Elasticity questions are really revenue questions: is the absolute value above or below 1?", "Leading, coincident and lagging indicators are a list worth memorising."],
   links=[("Price elasticity, from first principles", "prereq-price-elasticity.html"), ("Market structures", "prereq-market-structures.html"), ("Exchange rates", "prereq-exchange-rates.html")]),
 "fsa": dict(fig="three_statements", short="financial statement analysis",
   intro="Financial statement analysis is one of the four heavyweights at Level I. Questions test whether you can follow a transaction through the three statements, compare IFRS with US GAAP, and compute ratios without mixing up averages and year-end figures.",
   tips=["Ask what each choice does to the income statement, the balance sheet and cash flow, in that order.", "Under rising prices, LIFO lowers profit, inventory and taxes; FIFO does the reverse.", "Memorise the IFRS and US GAAP differences in cash flow classification."],
   links=[("The three statements, connected", "prereq-three-statements.html"), ("FIFO, LIFO and weighted average", "prereq-fifo-lifo-weighted-average.html"), ("Deferred tax", "prereq-deferred-tax.html")]),
 "corporate": dict(fig="npv_profile", short="corporate issuers",
   intro="Corporate issuers (formerly corporate finance) asks how companies choose investments, how they are financed and governed, and how they manage working capital. The calculations are capital budgeting and the cost of capital; the concepts are governance and stakeholder conflicts.",
   tips=["NPV beats IRR whenever the two disagree on mutually exclusive projects.", "Use the after-tax cost of debt in the WACC.", "The cash conversion cycle adds inventory and receivable days and subtracts payable days."],
   links=[("Cash flows on the BA II Plus (NPV and IRR)", "blog-ba-ii-plus-calculator-guide.html"), ("Capitalise or expense", "prereq-capitalise-or-expense.html")]),
 "equity": dict(fig="ddm_stack", short="equity investments",
   intro="Equity investments covers how markets work (orders, margin, indexes), market efficiency, industry and company analysis, and valuation with dividend discount models and multiples. Expect several margin and index calculations and at least one Gordon growth model.",
   tips=["The Gordon growth model needs next year's dividend, D1, not the one just paid.", "Price-weighted indexes are moved by high-priced stocks; value-weighted by large companies.", "Subtract net debt to get from enterprise value to equity value."],
   links=[("The hardest CFA topics", "blog-hardest-cfa-topics.html"), ("Common-size statements", "prereq-common-size.html")]),
 "fixed-income": dict(fig="price_yield", short="fixed income",
   intro="Fixed income is where many Level I candidates lose marks: bond pricing, yield measures, the term structure, duration and convexity, and credit. Almost every concept follows from one idea: a bond's price is the present value of its cash flows.",
   tips=["If the coupon is below the yield, the bond trades below par, and vice versa.", "Duration gives the first estimate of the price change; convexity corrects it, always upwards for option-free bonds.", "Forward rates make investing short and rolling equal to investing long."],
   links=[("Bonds and the effective interest method", "prereq-bonds-effective-interest.html"), ("Credit analysis basics", "prereq-credit-analysis.html")]),
 "derivatives": dict(fig="payoff_diagram", short="derivatives",
   intro="Derivatives at Level I is about payoffs and no-arbitrage pricing: forwards and futures, swaps, options, put-call parity and the one-period binomial model. Draw the payoff before you calculate and most questions become simple.",
   tips=["Payoff ignores the premium; profit subtracts it.", "Put-call parity: call + PV(strike) = put + stock.", "In the binomial model, discount the risk-neutral expected payoff at the risk-free rate."],
   links=[("The BA II Plus calculator guide", "blog-ba-ii-plus-calculator-guide.html")]),
 "alternatives": dict(fig="hf_fees", short="alternative investments",
   intro="Alternative investments covers hedge funds, private equity, real estate, infrastructure, commodities and digital assets. The favourite calculation is a fee waterfall; the favourite concept is why reported returns of illiquid assets look smoother than they are.",
   tips=["Read fee questions twice: is the incentive fee charged on gross returns or after the management fee? Is there a hurdle or a high-water mark?", "Value = NOI / cap rate.", "Commodity futures returns = spot + roll + collateral."],
   links=[("Is the CFA worth it?", "blog-is-cfa-worth-it.html")]),
 "portfolio": dict(fig="frontier", short="portfolio management",
   intro="Portfolio management ties the curriculum together: risk and return, diversification, the CAPM and security market line, performance measures, the investment policy statement and risk management. Several questions need the two-asset portfolio variance formula.",
   tips=["Only correlations below 1 reduce portfolio risk.", "Sharpe uses total risk; Treynor and Jensen's alpha use beta.", "When ability and willingness to take risk differ, the lower one usually sets the policy."],
   links=[("Choosing your Level III pathway", "blog-level-3-pathways.html")]),
}


def page(key, i):
    name, weight, scope = META[key]
    inf = INFO[key]
    slug = f"cfa-level-1-practice-questions-{key}"
    title = f"CFA Level I practice questions: {name.lower() if key != 'ethics' else 'ethics'}, with worked answers"
    title = title.replace(": quantitative methods", ": quantitative methods").replace(": fsa", ": financial statement analysis")
    title = f"CFA Level I practice questions: {name}, with worked answers"
    summary = (f"Ten original {inf['short']} questions in the Level I format, three options each, with an explanation for every answer. "
               f"{scope} {name} carries {weight} of the exam from 2027.")
    tags = [f"CFA Level 1 {inf['short']} practice questions", f"CFA Level 1 {inf['short']} questions", f"CFA Level 1 {inf['short']} mock",
            f"CFA level 1 {inf['short']} questions and answers", "CFA Level 1 practice questions free", "CFA Level 1 sample questions"]
    tips = "\n".join(f"- {t}" for t in inf["tips"])
    links = " · ".join(f"[{a}]({b})" for a, b in inf["links"])
    others = [k for k in ORDER if k != key]
    nav = ", ".join(f"[{META[k][0]}](cfa-level-1-practice-questions-{k}.html)" for k in others)
    body = f"""{inf['intro']}

**Topic weight from 2027:** {weight} of Level I, about {round(180 * int(weight.split('–')[0]) / 100)} to {round(180 * int(weight.split('–')[1].rstrip('%')) / 100)} of the 180 questions.

[[practice:{key}]]

## Three things to remember for {inf['short']}

{tips}

## Keep going

- Background reading: {links}.
- The other nine topics: {nav}.
- All 100 questions in one place: [Level I practice questions](cfa-level-1-practice-questions.html).

## How to use these questions

Answer each question before you look at the explanation, and time yourself: the real exam allows about 90 seconds per question. Mark every question you got right for the wrong reason as wrong. When you miss one, write down the idea behind it rather than the answer, and come back to the page in a week.

These questions are written by First Principles to match the style and level of the exam. They are not taken from CFA Institute's curriculum or mock exams, which you should also use: they are included with your exam registration.

## Questions people ask

### Are these real CFA exam questions?

No. CFA Institute does not publish past exam questions. These are original questions written to match the Level I format: a short stem and three answer options, testing one idea each.

### How many {inf['short']} questions are on Level I?

{name} carries {weight} of the exam from 2027, which is roughly {round(180 * int(weight.split('–')[0]) / 100)} to {round(180 * int(weight.split('–')[1].rstrip('%')) / 100)} of the 180 questions.

### Where can I find more Level I practice questions?

Use the practice questions and mock exams in CFA Institute's learning ecosystem first; they come with registration. Then use one third-party question bank, and redo every question you missed.
"""
    fm = {"title": title, "slug": slug, "order": str(i + 1), "summary": summary, "figure": inf["fig"],
          "caption": f"{name}: one of the ideas these questions test, drawn.", "tags": ", ".join(tags), "updated": UPDATED, "pkey": key}
    return "---\n" + "\n".join(f"{k}: {v}" for k, v in fm.items()) + "\n---\n" + body


if __name__ == "__main__":
    out = ROOT / "content" / "practice"
    out.mkdir(parents=True, exist_ok=True)
    for i, k in enumerate(ORDER):
        (out / f"{i + 1:02d}-{k}.md").write_text(page(k, i), encoding="utf-8")
    print("wrote", len(ORDER), "practice pages,", sum(len(v) for v in TOPICS.values()), "questions")
