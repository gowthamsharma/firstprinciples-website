---
title: CFA Level I formula sheet: the formulas you actually need
slug: blog-cfa-level-1-formula-sheet
order: 22
summary: About fifty formulas cover most Level I calculations. Here they are by topic, each with a one-line reminder of what it means, so you can rebuild them instead of memorising them.
figure: bond_reason
caption: Behind most of these formulas is one idea: a value today is future cash discounted back.
tags: CFA level 1 formulas, CFA formula sheet, CFA level 1 formula sheet, CFA formulas list, CFA level 1 important formulas, CFA quant formulas, CFA fixed income formulas, CFA financial ratios
group: Tools: formulas, calculator and self-study
---
No formula sheet is given in the exam, so you must carry these in your head. The good news: most are short, and many follow from a few ideas. Learn **what each one says** and you will rebuild the ones you forget. This sheet is our own summary, organised by topic.


[[figure]]

## Quantitative methods

| Formula | What it says |
|---|---|
| FV = PV × (1 + r)ⁿ | money grows by compounding |
| PV = FV ÷ (1 + r)ⁿ | discounting is compounding in reverse |
| Effective annual rate = (1 + r/m)ᵐ − 1 | more frequent compounding, higher effective rate |
| Continuous compounding: FV = PV × e^(r·t) | the limit of compounding ever more often |
| Holding-period return = (P₁ − P₀ + D) ÷ P₀ | price change plus income, over the start price |
| Geometric mean = [(1+R₁)(1+R₂)…(1+Rₙ)]^(1/n) − 1 | the true compound growth rate |
| Sample variance = Σ(x − x̄)² ÷ (n − 1) | average squared distance from the mean |
| Coefficient of variation = σ ÷ mean | risk per unit of return |
| Covariance → correlation: ρ = Cov(X,Y) ÷ (σₓσᵧ) | correlation is covariance scaled to −1 … +1 |
| z = (x − μ) ÷ σ | how many standard deviations from the mean |
| Sharpe ratio = (Rₚ − R_f) ÷ σₚ | excess return per unit of total risk |

## Economics

| Formula | What it says |
|---|---|
| Price elasticity = %ΔQ ÷ %ΔP | how strongly buyers react to price |
| GDP = C + I + G + (X − M) | spending on everything produced at home |
| Nominal rate ≈ real rate + expected inflation | the Fisher relation |
| Real exchange rate = nominal rate (domestic per foreign) × (P_foreign ÷ P_domestic) | currencies adjusted for price levels |
| MV = PY | quantity theory of money |

## Financial statement analysis

| Formula | What it says |
|---|---|
| Current ratio = current assets ÷ current liabilities | short-term liquidity |
| Quick ratio = (cash + short-term investments + receivables) ÷ current liabilities | liquidity without inventory |
| Inventory turnover = cost of sales ÷ average inventory | how fast stock sells |
| Days of inventory = 365 ÷ inventory turnover | days goods sit on the shelf |
| Days of sales outstanding = 365 ÷ receivables turnover | days to collect from customers |
| Cash conversion cycle = DOH + DSO − DPO | days cash is tied up |
| ROE = net margin × asset turnover × leverage | the three-step DuPont split |
| Interest coverage = EBIT ÷ interest expense | how easily interest is paid |
| Debt-to-equity = total debt ÷ total equity | how much borrowing per unit of equity |
| FIFO inventory = LIFO inventory + LIFO reserve | converting LIFO to FIFO |
| Income tax expense = taxes payable + ΔDTL − ΔDTA | deferred tax links accounts and tax |

## Corporate issuers

| Formula | What it says |
|---|---|
| WACC = wd × kd × (1 − t) + wp × kp + we × ke | average cost of every source of funds |
| NPV = Σ CFₜ ÷ (1 + r)ᵗ − initial outlay | value created by a project |
| DOL = %Δ operating income ÷ %Δ sales | operating leverage |
| DFL = %Δ net income ÷ %Δ operating income | financial leverage |

## Equity

| Formula | What it says |
|---|---|
| Gordon growth: V₀ = D₁ ÷ (r − g) | value of a dividend growing forever |
| Justified forward P/E = (D₁/E₁) ÷ (r − g) | payout ratio over (required return − growth) |
| Sustainable growth g = b × ROE | retained earnings × return on them |

## Fixed income

| Formula | What it says |
|---|---|
| Price = Σ coupon ÷ (1 + y)ᵗ + face ÷ (1 + y)ⁿ | a bond is a bundle of discounted payments |
| Current yield = annual coupon ÷ price | income return only |
| Modified duration = Macaulay duration ÷ (1 + y) | price sensitivity to yield |
| %ΔPrice ≈ −ModDur × Δy + ½ × Convexity × (Δy)² | duration plus a curvature correction |
| Money duration = ModDur × full price | price change in money terms |

## Derivatives

| Formula | What it says |
|---|---|
| Forward price F₀ = S₀ × (1 + r)ᵀ | no-arbitrage price with no income or costs |
| Put–call parity: S₀ + p₀ = c₀ + X ÷ (1 + r)ᵀ | a protective put equals a fiduciary call |

## Portfolio management

| Formula | What it says |
|---|---|
| σ²ₚ = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂ | diversification lowers risk when ρ < 1 |
| CAPM: E(R) = R_f + β × [E(R_m) − R_f] | return for systematic risk only |
| β = Cov(R_i, R_m) ÷ σ²_m | sensitivity to the market |
| Treynor = (Rₚ − R_f) ÷ βₚ | excess return per unit of market risk |
| Jensen's alpha = Rₚ − [R_f + βₚ(R_m − R_f)] | return above what CAPM predicts |

## How to remember them

- **Group them by idea**, not by chapter: most valuation formulas are "discount future cash".
- **Write the sheet from memory** once a week and check the gaps.
- **Understand the units**: a ratio of days to turnover, or of risk to return, is half the formula.
- For the reasoning behind many of these, see the [prerequisite concepts](prerequisites.html).

## Questions people ask

### Is a formula sheet provided in the CFA exam?

No. You must know the formulas. Some questions give inputs you would otherwise derive, but you are never given a sheet.

### How many formulas are there in CFA Level I?

Lists from prep providers range from about 100 to over 200, depending on how variations are counted. The ones on this page cover most of what is tested.

### What is the best way to memorise CFA formulas?

Understand where each comes from, use them in practice questions daily, and rewrite them from memory regularly. Rote memorising alone fades quickly.

## Sources

- [CFA Institute: Level I exam](https://www.cfainstitute.org/programs/cfa-program/candidate-resources/level-i-exam)
