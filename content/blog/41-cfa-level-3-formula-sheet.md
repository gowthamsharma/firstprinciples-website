---
title: CFA Level III formula sheet: every formula you need, by topic
slug: blog-cfa-level-3-formula-sheet
order: 41
summary: The complete Level III formula sheet for the core curriculum and the three pathways: capital market expectations, asset allocation, derivatives and currency overlays, fixed income and equity portfolio management, after-tax wealth, trading costs, performance attribution and private markets, each with a one-line note.
figure: frontier
caption: Level III is about building and defending a portfolio; the formulas size the positions and measure the results.
tags: CFA level 3 formulas, CFA level 3 formula sheet, CFA level III formula sheet, CFA level 3 formulas list, CFA level 3 fixed income formulas, CFA level 3 derivatives formulas, CFA level 3 private wealth formulas, CFA level 3 performance attribution
group: Tools: formulas, calculator and self-study
updated: 2026-11-22
seo_title: CFA Level III formula sheet: core and pathway formulas (2026–2027)
meta: The complete CFA Level III formula sheet: capital market expectations, asset allocation, futures overlays, currency hedging, fixed income returns, after-tax wealth, attribution and private markets.
---
Level III has fewer formulas than Level II, but the exam uses them differently. In constructed-response questions you must **show the calculation and justify the result**: why a hedge ratio, why that asset allocation, what the attribution says about the manager. This sheet covers the core curriculum, which every candidate sits, plus the formulas specific to each pathway: Portfolio Management, Private Wealth and Private Markets.

Formula sheets for the other levels: [Level I](blog-cfa-level-1-formula-sheet.html) · [Level II](blog-cfa-level-2-formula-sheet.html). For the pathway choice itself, see [choosing your Level III pathway](blog-level-3-pathways.html).

[[figure]]

## Capital market expectations

| Formula | What it says |
|---|---|
| Grinold–Kroner: E(R) ≈ D ÷ P − %ΔS + i + g + %ΔP/E | income + nominal earnings growth + repricing |
| Same idea, three parts: E(R) ≈ (D ÷ P − %ΔS) + (i + g) + %ΔP/E | %ΔS = change in shares outstanding |
| Singer–Terhaar, fully integrated: RPᵢ = ρᵢ,GM × σᵢ × (RP_GM ÷ σ_GM) | |
| Singer–Terhaar, fully segmented: RPᵢ = σᵢ × (RP_M ÷ σ_M) | |
| Singer–Terhaar blend: RPᵢ = φ × integrated + (1 − φ) × segmented + liquidity premium | φ = degree of integration |
| Taylor rule: i* = r_neutral + π + 0.5(π − π_target) + 0.5(Ŷ − Ŷ_trend) | policy rate guide |
| Trend real GDP growth = labour force growth + labour productivity growth | |
| Fixed income expected return ≈ yield to maturity (if held to maturity, no default) | the most reliable building block |
| Equity risk premium build-up: E(R) = R_f + ERP; bond: R_f + term + credit + liquidity premiums | |
| Covered interest parity: F ÷ S = (1 + i_p) ÷ (1 + i_b) | |
| Expected currency return ≈ change implied by interest differential, adjusted for views | |

## Asset allocation

| Formula | What it says |
|---|---|
| Utility (mean–variance): U_m = E(R_m) − 0.005 × λ × σ_m² | returns and σ in percent; λ = risk aversion |
| Surplus = market value of assets − present value of liabilities | |
| Surplus return = [Δ assets − Δ liabilities] ÷ assets at start | |
| Funded ratio = assets ÷ liabilities | |
| Human capital = Σ [p(sₜ) × wₜ₋₁(1 + gₜ)] ÷ (1 + r_f + y)ᵗ | PV of future earnings, adjusted for survival and job risk |
| Economic balance sheet: financial capital + human capital = liabilities + net wealth | |
| Required return (spending) ≈ (1 + spending rate)(1 + inflation)(1 + costs) − 1 | multiplicative |
| Rebalancing corridor: target ± range; wider when costs are high or volatility low | |
| Risk budgeting: marginal contribution to risk = wᵢ × βᵢ,P × σ_P | |
| Percentage contribution to total risk = wᵢ × βᵢ,P | sums to 100% |
| Risk parity: wᵢ × Cov(Rᵢ, R_P) = (1 ÷ n) × σ_P² | equal risk contributions |

## Derivatives and risk management

| Formula | What it says |
|---|---|
| Equity futures to change beta: N_f = [(β_T − β_S) ÷ β_f] × (S ÷ F) | S = portfolio value, F = futures price × multiplier |
| Bond futures to change duration: N_f = (BPV_T − BPV_P) ÷ BPV_f | |
| BPV of a bond future ≈ BPV of cheapest-to-deliver ÷ conversion factor | |
| BPV = money duration × 0.0001 = ModDur × market value × 0.0001 | |
| Cash equitisation: N_f = (cash × (1 + r)ᵀ) ÷ (F × multiplier) | synthetic equity for idle cash |
| Interest rate swap BPV ≈ (receive-fixed duration − floating-leg duration) × notional × 0.0001 | |
| Notional of swap to hit target = (BPV_T − BPV_P) ÷ BPV_swap per unit | |
| Covered call: max gain = X − S₀ + c₀; breakeven = S₀ − c₀ | |
| Protective put: max loss = S₀ − X + p₀; breakeven = S₀ + p₀ | |
| Collar: buy put X_L, sell call X_H; range of outcomes X_L to X_H, net premium | |
| Bull call spread: max gain = X_H − X_L − net premium | |
| Straddle breakevens = X ± (c₀ + p₀) | betting on volatility, not direction |
| Variance swap payoff = variance notional × (realised variance − strike variance) | variance notional = vega notional ÷ (2 × strike volatility) |
| Delta hedge: number of options = −(portfolio delta ÷ option delta) | |
| Minimum-variance hedge ratio h* = ρ × σ_spot ÷ σ_futures | |
| Parametric VaR = [E(R) − z × σ] × portfolio value | z = 1.65 (5%), 2.33 (1%) |
| Conditional VaR (expected shortfall) = average loss beyond VaR | |

## Currency management

| Formula | What it says |
|---|---|
| Domestic-currency return: R_DC = (1 + R_FC)(1 + R_FX) − 1 | |
| Multi-currency: R_DC = Σ wᵢ[(1 + R_FC,i)(1 + R_FX,i)] − 1 | |
| σ²(R_DC) ≈ σ²(R_FC) + σ²(R_FX) + 2ρσ(R_FC)σ(R_FX) | currency adds risk unless negatively correlated |
| If FX risk is fully hedged: σ(R_DC) ≈ σ(R_FC) | |
| Forward premium/discount ≈ interest rate differential | roll yield on a hedge |
| Roll yield (selling base currency forward) = (F − S) ÷ S | positive if base trades at a forward premium |
| Hedge ratio = hedged notional ÷ market value of foreign assets | rebalance as values change |
| Minimum-variance hedge ratio: regress R_DC on R_FX; slope = hedge ratio | |
| Carry trade return = interest differential − depreciation of high-yield currency | |

## Fixed income portfolio management

| Formula | What it says |
|---|---|
| E(R) ≈ yield income + rolldown return + E(price change from yield views) − E(credit losses) ± E(currency gains or losses) | the decomposition used throughout Level III |
| Yield income = annual coupon ÷ current price (+ reinvestment) | |
| Rolldown return = (bond price after rolling down a stable curve − price today) ÷ price today | |
| E(price change from yields) ≈ −ModDur × Δy + ½ × convexity × (Δy)² | |
| Immunising one liability: Macaulay duration = horizon; PV assets ≥ PV liability; minimise convexity (dispersion) | |
| Multiple liabilities: match money duration (BPV); asset convexity > liability convexity; PV assets ≥ PV liabilities | |
| Contingent immunisation cushion = PV of assets − PV of liabilities at the immunisation rate | active management while the surplus lasts |
| Convexity = (Macaulay duration² + Macaulay duration + dispersion) ÷ (1 + r)² | lower dispersion, lower structural risk | |
| Expected excess spread return ≈ spread₀ − (EffSpreadDur × Δspread) − (POD × LGD) | |
| Leveraged portfolio return: R_P = r_I + (V_B ÷ V_E)(r_I − r_B) | |
| Key rate duration: price sensitivity to one point on the curve; Σ key rate durations ≈ effective duration | |
| Butterfly: wings vs body; barbell gains when the curve flattens and from convexity | |
| Bond portfolio duration = Σ (market value weight × duration) | |
| Spread duration (portfolio) = Σ (weight × spread duration) | credit risk sensitivity |

## Equity portfolio management

| Formula | What it says |
|---|---|
| Active return = R_P − R_B | |
| Active risk (tracking error) = σ(R_P − R_B) | |
| Information ratio = active return ÷ active risk | |
| Active share = ½ × Σ ∣w_P,i − w_B,i∣ | how different the holdings are from the benchmark |
| Active risk² = active factor risk + active specific risk | factor bets and stock-specific bets both add risk |
| Net exposure (long-short) = long exposure − short exposure; gross = long + short | |
| Portfolio beta of a 130/30 strategy ≈ 1.3β_long − 0.3β_short | |

## Trading, performance evaluation and manager selection

| Formula | What it says |
|---|---|
| Implementation shortfall = paper portfolio return − actual portfolio return | |
| Implementation shortfall = delay cost + execution cost + opportunity cost + fixed fees | |
| Delay cost = shares traded × (arrival price − decision price) | for a buy |
| Execution cost = shares traded × (average execution price − arrival price) | |
| Opportunity cost = unfilled shares × (closing price − decision price) | |
| VWAP cost = shares × (average execution price − VWAP) | |
| Brinson–Fachler allocation = (w_P,i − w_B,i)(R_B,i − R_B) | did overweights go to sectors that beat the benchmark? |
| Brinson selection = w_B,i(R_P,i − R_B,i) | stock picking within each sector |
| Interaction = (w_P,i − w_B,i)(R_P,i − R_B,i) | |
| Total active return = allocation + selection + interaction | |
| Fixed income attribution: yield income + rolldown + duration + curve + spread + selection | |
| Sharpe ratio = (R_P − R_f) ÷ σ_P | |
| Treynor ratio = (R_P − R_f) ÷ β_P | |
| Sortino ratio = (R_P − MAR) ÷ downside deviation | penalises only returns below the minimum acceptable return |
| Appraisal ratio = Jensen's alpha ÷ σ of residual returns | |
| Upside capture = R_P ÷ R_B in up markets; downside capture = R_P ÷ R_B in down markets | |
| Capture ratio = upside capture ÷ downside capture | above 1: asymmetric return profile |
| Maximum drawdown = largest peak-to-trough fall | |

## Private wealth pathway

| Formula | What it says |
|---|---|
| Accrual taxation: FV = [1 + r(1 − t_i)]ⁿ | taxed every year |
| Deferred capital gains: FV = (1 + r)ⁿ(1 − t_cg) + t_cg × B | B = cost basis as a fraction of value (1 if no gain at start) |
| Tax-deferred account: FV = (1 + r)ⁿ(1 − t_n) | taxed on withdrawal |
| Tax-exempt account: FV = (1 + r)ⁿ | |
| Wealth tax: FV = [(1 + r)(1 − t_w)]ⁿ | |
| Blended tax rate: t* = p_i t_i + p_d t_d + p_cg t_cg | by type of return |
| Effective capital gains rate: T* = t_cg(1 − p_i − p_d − p_cg) ÷ (1 − p_i t_i − p_d t_d − p_cg t_cg) | |
| Accrual equivalent return = (FV ÷ PV)^(1/n) − 1 | the annual taxed-every-year return that gives the same result |
| Accrual equivalent tax rate = 1 − accrual equivalent return ÷ pre-tax return | |
| Tax-loss harvesting value = tax rate × loss realised (current year) | |
| After-tax wealth from a deferred account vs taxable: compare (1 + r)ⁿ(1 − t) with [1 + r(1 − t)]ⁿ | |
| Core capital = PV of spending needs (+ reserve); excess capital = assets − core capital | |
| Probability-weighted spending: PV = Σ p(survival) × spending ÷ (1 + r)ᵗ | |

## Private markets pathway

| Formula | What it says |
|---|---|
| DPI = cumulative distributions ÷ paid-in capital | cash returned |
| RVPI = NAV ÷ paid-in capital | value still in the fund |
| TVPI = DPI + RVPI | total value multiple |
| Net IRR: IRR of the fund's net cash flows to limited partners | sensitive to timing and subscription lines |
| Kaplan–Schoar PME = PV of (distributions + NAV) ÷ PV of contributions, discounted at index returns | above 1: beat the public market |
| Venture method: post-money = exit value ÷ (1 + r)ⁿ; ownership = investment ÷ post-money | |
| LBO equity value at exit = exit EV − net debt; equity IRR = (exit equity ÷ entry equity)^(1/n) − 1 | |
| Value creation = EBITDA growth + multiple expansion + debt paydown | |
| Carried interest (European waterfall) = carry × (total proceeds − contributed capital − preferred return) after catch-up rules | |
| Private debt expected return ≈ yield − expected loss (PD × LGD) − fees | |
| Real estate value = NOI ÷ cap rate; levered return ≈ unlevered return + (debt ÷ equity)(unlevered return − cost of debt) | |

## How to use this sheet in the exam

- **Show your working in constructed responses.** Write the formula, the inputs and the result; partial credit is given for a correct method.
- **Justify, don't just compute:** a hedge ratio or an asset allocation needs a reason tied to the client's objectives and constraints. See [how to answer constructed-response questions](blog-level-3-constructed-response.html).
- **Keep the Level I and II tools at hand:** duration, CAPM and option payoffs come up constantly.
- **Final month plan:** our [last-month guide to Level III](blog-level-3-last-month.html) explains how to drill these under time pressure.

## Questions people ask

### Is a formula sheet provided in the CFA Level III exam?

No. All three levels require you to know the formulas. In constructed-response questions you write the calculation in the answer box.

### How many formulas are in CFA Level III?

Fewer than at Level II, about 120 to 150 including the pathway formulas. The difficulty lies in choosing and justifying them, not in the algebra.

### Do the Level III pathways have different formulas?

Yes. The core curriculum is the same for everyone, and each pathway adds its own: after-tax wealth for Private Wealth, fund performance and deal valuation for Private Markets, and deeper portfolio construction and risk tools for Portfolio Management.

## Sources

- [CFA Institute: Level III exam](https://www.cfainstitute.org/programs/cfa-program/candidate-resources/level-iii-exam)
- [CFA Institute: CFA Program curriculum topics](https://www.cfainstitute.org/programs/cfa-program/curriculum)
