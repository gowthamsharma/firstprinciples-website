---
title: CFA Level II formula sheet: every formula you need, by topic
slug: blog-cfa-level-2-formula-sheet
order: 40
summary: The complete Level II formula sheet: multiple regression and time series, currencies and growth, pensions and multinational accounting, residual income and free cash flow valuation, bond trees and credit default swaps, Black–Scholes–Merton, real estate and private equity, and multifactor models, each with a one-line note.
figure: ddm_stack
caption: Most of Level II valuation is the Level I idea taken further: forecast the cash, then discount it at the right rate.
tags: CFA level 2 formulas, CFA level 2 formula sheet, CFA level II formula sheet, CFA level 2 formulas list, CFA level 2 equity valuation formulas, CFA level 2 fixed income formulas, CFA level 2 derivatives formulas, CFA level 2 quant formulas
group: Tools: formulas, calculator and self-study
updated: 2026-11-22
seo_title: CFA Level II formula sheet: every formula by topic (2026–2027)
meta: The complete CFA Level II formula sheet: regression, currencies, pensions, FCFF and residual income, bond trees, CDS, Black–Scholes–Merton, real estate and multifactor models.
---
Level II builds on Level I: you still need everything on the [Level I formula sheet](blog-cfa-level-1-formula-sheet.html), and Level II adds the valuation and modelling tools below. The exam does not give you a formula sheet, and item-set vignettes rarely tell you which formula to use. That is why knowing **when** a formula applies matters as much as remembering it.

Formula sheets for the other levels: [Level I](blog-cfa-level-1-formula-sheet.html) · [Level III](blog-cfa-level-3-formula-sheet.html).

[[figure]]

## Quantitative methods

### Multiple regression

| Formula | What it says |
|---|---|
| Ŷ = b̂₀ + b̂₁X₁ + … + b̂ₖXₖ | each slope holds the other variables constant |
| t = (b̂ⱼ − Bⱼ) ÷ s_b̂ⱼ, df = n − k − 1 | is one coefficient significant? |
| F = (SSR ÷ k) ÷ [SSE ÷ (n − k − 1)] | are the slopes jointly zero? |
| R² = SSR ÷ SST | share of variation explained |
| Adjusted R² = 1 − [(n − 1) ÷ (n − k − 1)] × (1 − R²) | penalises extra variables |
| AIC = n ln(SSE ÷ n) + 2(k + 1) | lower is better; prediction |
| BIC = n ln(SSE ÷ n) + ln(n)(k + 1) | lower is better; stronger penalty, goodness of fit |
| Joint (nested) F = [(SSE_R − SSE_U) ÷ q] ÷ [SSE_U ÷ (n − k − 1)] | do q excluded variables matter? |
| Breusch–Pagan = n × R² of squared residuals on the Xs, χ² with k df | conditional heteroskedasticity |
| Breusch–Godfrey: regress residuals on Xs and lagged residuals; F or χ² test | serial correlation |
| VIF = 1 ÷ (1 − Rⱼ²) | above 5 a concern, above 10 serious multicollinearity |
| Leverage hᵢᵢ > 3(k + 1) ÷ n | potentially influential observation (high leverage) |
| Cook's D > 0.5 possibly influential; > 1 likely influential | combines leverage and residual size |
| Logistic: ln[p ÷ (1 − p)] = b₀ + b₁X₁ + … | log odds are linear |
| p = 1 ÷ [1 + e^−(b₀ + b₁X₁ + …)] | probability from the logit |

### Time series

| Formula | What it says |
|---|---|
| Linear trend: yₜ = b₀ + b₁t | constant amount of growth |
| Log-linear trend: ln yₜ = b₀ + b₁t | constant rate of growth |
| AR(1): xₜ = b₀ + b₁xₜ₋₁ + εₜ | today depends on yesterday |
| Mean-reverting level = b₀ ÷ (1 − b₁) | the series drifts back here |
| Autocorrelation test: t = ρₖ ÷ (1 ÷ √T) | residual autocorrelations should be zero |
| Random walk: xₜ = xₜ₋₁ + εₜ (b₁ = 1, a unit root) | first-difference before modelling |
| Seasonal lag: add xₜ₋₄ (quarterly) or xₜ₋₁₂ (monthly) | |
| ARCH(1): ε̂²ₜ = a₀ + a₁ε̂²ₜ₋₁ | if a₁ is significant, variance is predictable |
| Predicted variance = â₀ + â₁ε̂²ₜ | |
| RMSE = √[Σ(actual − forecast)² ÷ n] | out-of-sample forecast accuracy |
| Cointegration (Engle–Granger): regress y on x, test residuals for a unit root | two unit-root series can still be modelled together |

### Machine learning and big data

| Formula | What it says |
|---|---|
| Precision = TP ÷ (TP + FP) | of predicted positives, how many are right |
| Recall (sensitivity) = TP ÷ (TP + FN) | of actual positives, how many are found |
| Accuracy = (TP + TN) ÷ all observations | |
| F1 score = 2 × precision × recall ÷ (precision + recall) | balances precision and recall |
| Normalisation = (X − X_min) ÷ (X_max − X_min) | scales to 0–1 |
| Standardisation = (X − μ) ÷ σ | scales to mean 0, standard deviation 1 |
| Term frequency = count of a token ÷ total tokens | text features |

## Economics

| Formula | What it says |
|---|---|
| Cross-rate bid (A/C) = bid (A/B) × bid (B/C); offer = offer × offer | for quotes that chain |
| Inverse quote: bid (B/A) = 1 ÷ offer (A/B) | invert and swap sides |
| Forward = S × [1 + i_p (days ÷ 360)] ÷ [1 + i_b (days ÷ 360)] | covered interest rate parity |
| Forward premium = F − S = S × (i_p − i_b)(days ÷ 360) ÷ [1 + i_b (days ÷ 360)] | |
| Value of a forward before expiry = (F_new − F_old) × size ÷ [1 + i_p (days left ÷ 360)] | mark to market |
| Uncovered interest parity: E(%ΔS_p/b) ≈ i_p − i_b | high-yield currency expected to weaken |
| Relative PPP: %ΔS_p/b ≈ π_p − π_b | inflation differentials drive currencies over time |
| International Fisher: i_p − i_b ≈ E(π_p) − E(π_b) | real rates equal across countries |
| Real interest rate parity: r_p − r_b = E(%Δ real exchange rate) | |
| Carry trade return ≈ i_high − i_low − %Δ value of the high-yield currency | |
| Cobb–Douglas: Y = A K^α L^(1 − α) | output from technology, capital and labour |
| Growth accounting: %ΔY = %ΔA + α%ΔK + (1 − α)%ΔL | |
| Potential GDP growth = long-term labour force growth + labour productivity growth | |
| Labour productivity growth = %ΔA + α(%ΔK − %ΔL) | capital deepening plus technology |
| Neoclassical steady state: growth of output per worker = θ ÷ (1 − α) | θ = growth of total factor productivity |

## Financial statement analysis

| Formula | What it says |
|---|---|
| Equity method: investment = cost + share of investee NI − dividends received | significant influence |
| Goodwill (partial) = purchase price − share of fair value of identifiable net assets | IFRS option |
| Goodwill (full) = fair value of the whole acquiree − fair value of identifiable net assets | US GAAP; IFRS option |
| Non-controlling interest (full goodwill) = NCI share × fair value of the subsidiary | |
| Funded status = fair value of plan assets − defined benefit obligation | negative: net pension liability |
| DBO_end = DBO_begin + service cost + interest cost + past service cost ± actuarial losses/gains − benefits paid | |
| Plan assets_end = plan assets_begin + actual return + employer contributions − benefits paid | |
| IFRS pension cost in P&L = service cost + net interest (discount rate × net DB liability) | remeasurements go to OCI |
| US GAAP pension cost = service cost + interest cost − expected return + amortisation of prior service cost and actuarial losses | |
| Total periodic pension cost = employer contributions − (ending funded status − beginning funded status) | the economic cost of the year |
| Share-based compensation expense = fair value at grant date ÷ vesting period | |
| Current rate method: assets and liabilities at current rate, income statement at average rate, equity at historical rate; translation adjustment in OCI | functional currency ≠ presentation currency |
| Temporal method: monetary items at current rate, non-monetary items at historical rate; remeasurement gain or loss in net income | functional currency = parent's currency |
| Exposure: current rate method → net assets; temporal method → net monetary assets (or liabilities) | |
| CET1 ratio = common equity tier 1 capital ÷ risk-weighted assets | bank solvency |
| Liquidity coverage ratio = high-quality liquid assets ÷ net cash outflows over 30 days ≥ 100% | |
| Net stable funding ratio = available stable funding ÷ required stable funding ≥ 100% | |
| Insurer combined ratio = loss and loss-adjustment expense ratio + underwriting expense ratio | below 100% is an underwriting profit |
| Balance sheet accruals ratio = (NOA_end − NOA_begin) ÷ average NOA | high accruals, lower earnings quality |
| Cash flow accruals ratio = [NI − (CFO + CFI)] ÷ average NOA | |
| Altman Z = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E | working capital, retained earnings, EBIT, equity value ÷ liabilities, sales (A, B, C, E ÷ total assets) |

## Corporate issuers

| Formula | What it says |
|---|---|
| Share buyback EPS = (earnings − after-tax cost of funds used) ÷ shares after buyback | EPS rises if earnings yield > after-tax cost of debt |
| BVPS after buyback = (equity − cost of buyback) ÷ shares after | falls if price > BVPS |
| Double taxation: effective rate = t_c + (1 − t_c) × t_i | corporate then personal tax on dividends |
| Split-rate system: effective rate = t_c,d + (1 − t_c,d) × t_i | lower corporate rate on distributed profits |
| Dividend coverage = NI ÷ dividends; FCFE coverage = FCFE ÷ (dividends + buybacks) | can the payout be sustained? |
| Build-up cost of equity = R_f + ERP + size premium + specific-company premium | private companies |
| Country spread model: ERP = developed-market ERP + country (sovereign) spread | |
| Merger: V_AT = V_A + V_T + S − C | combined value after cash paid C |
| Gain to target shareholders = premium = price paid − pre-merger value of target | |
| Gain to acquirer = synergies − premium | |
| HHI change after merger = 2 × share_A × share_B | antitrust screening |

## Equity valuation

### Return concepts and dividend models

| Formula | What it says |
|---|---|
| Required return (CAPM) = R_f + β × ERP | |
| Fama–French: R = R_f + β_mkt × MKT + β_size × SMB + β_value × HML | add momentum and liquidity factors as needed |
| Gordon implied ERP = D₁ ÷ P₀ + g − R_f | |
| Alpha = expected return − required return | |
| Gordon growth: V₀ = D₁ ÷ (r − g) | |
| PVGO: V₀ = E₁ ÷ r + PVGO | value of future growth opportunities |
| Justified leading P/E = (1 − b) ÷ (r − g); trailing P/E = (1 − b)(1 + g) ÷ (r − g) | |
| H-model: V₀ = D₀(1 + g_L) ÷ (r − g_L) + D₀ × H × (g_S − g_L) ÷ (r − g_L) | H = half the length of the decline period |
| Sustainable growth g = b × ROE | |
| PRAT: g = retention × net margin × asset turnover × financial leverage | |
| Implied required return from H-model: r = (D₀ ÷ P₀)[(1 + g_L) + H(g_S − g_L)] + g_L | |

### Free cash flow models

| Formula | What it says |
|---|---|
| FCFF = NI + NCC + Int(1 − t) − FCInv − WCInv | to all capital providers |
| FCFF = CFO + Int(1 − t) − FCInv | |
| FCFF = EBIT(1 − t) + Dep − FCInv − WCInv | |
| FCFF = EBITDA(1 − t) + Dep × t − FCInv − WCInv | |
| FCFE = FCFF − Int(1 − t) + net borrowing | to shareholders |
| FCFE = NI + NCC − FCInv − WCInv + net borrowing | |
| FCFE with target debt ratio DR: FCFE = NI − (1 − DR)(FCInv − Dep) − (1 − DR)WCInv | |
| Firm value = FCFF₁ ÷ (WACC − g); equity = firm value − debt | |
| Equity value = FCFE₁ ÷ (r − g) | |

### Residual income, multiples and private companies

| Formula | What it says |
|---|---|
| Residual income RIₜ = Eₜ − r × Bₜ₋₁ = (ROEₜ − r) × Bₜ₋₁ | profit above the cost of equity |
| V₀ = B₀ + Σ RIₜ ÷ (1 + r)ᵗ | book value plus PV of residual income |
| Single-stage RI: V₀ = B₀ + (ROE − r)B₀ ÷ (r − g) | |
| Justified P/B = 1 + (ROE − r) ÷ (r − g) = (ROE − g) ÷ (r − g) | |
| Terminal RI with persistence ω: PV = RI_T ÷ (1 + r − ω) | ω between 0 and 1: RI fades |
| Clean surplus: Bₜ = Bₜ₋₁ + Eₜ − Dₜ | |
| EVA = NOPAT − WACC × invested capital | |
| Justified P/S = (E₀ ÷ S₀)(1 − b)(1 + g) ÷ (r − g) | |
| PEG = (P/E) ÷ growth rate in % | |
| Harmonic mean P/E = n ÷ Σ(1 ÷ P/Eᵢ) | less distorted by high P/Es |
| Discount for lack of control = 1 − 1 ÷ (1 + control premium) | |
| Total discount = 1 − (1 − DLOC)(1 − DLOM) | discounts multiply |
| Capitalised cash flow: V = FCFF₁ ÷ (WACC − g) | private company, stable growth |

## Fixed income

| Formula | What it says |
|---|---|
| Forward pricing model: P(T*) = P(T) × F(T, T*) | price of a long zero from a short zero and a forward |
| (1 + z_B)^B = (1 + z_A)^A × (1 + f_A,B−A)^(B−A) | forward rate model |
| Bootstrapping: solve each spot rate from par yields in sequence | |
| Swap spread = swap rate − government yield of same maturity | |
| Rolldown return = (price after rolling down the curve − price today) ÷ price today | stable curve |
| Binomial tree node: V = ½[(V_up + C) + (V_down + C)] ÷ (1 + r_node) | backward induction |
| Adjacent rates in a lognormal tree: r_up = r_down × e^(2σ) | |
| Callable bond = straight bond − value of call option | |
| Putable bond = straight bond + value of put option | |
| OAS: constant spread over the tree that reprices the bond | removes the option's effect |
| Effective duration = (PV₋ − PV₊) ÷ (2 × Δcurve × PV₀) | |
| Effective convexity = (PV₋ + PV₊ − 2PV₀) ÷ [(Δcurve)² × PV₀] | negative for callable bonds when rates are low |
| Capped floater = straight floater − cap; floored floater = straight floater + floor | |
| Conversion price = par ÷ conversion ratio | |
| Conversion value = share price × conversion ratio | |
| Market conversion price = convertible price ÷ conversion ratio | |
| Market conversion premium per share = market conversion price − share price | |
| Minimum value of a convertible = max(straight value, conversion value) | |
| Expected loss = probability of default × loss given default | |
| Probability of survival = (1 − hazard rate)ᵗ | |
| Credit valuation adjustment = Σ (expected loss × discount factor) over time | value lost to credit risk |
| Credit spread ≈ hazard rate × (1 − recovery rate) | |
| CDS upfront premium ≈ (credit spread − fixed coupon) × CDS duration | |
| CDS price per 100 of notional ≈ 100 − upfront premium (%) | |
| Change in CDS value ≈ Δspread × CDS duration × notional | |

## Derivatives

| Formula | What it says |
|---|---|
| Equity forward with discrete dividends: F₀ = [S₀ − PV(D)] × (1 + r)ᵀ | |
| Equity forward with dividend yield δ: F₀ = S₀ × e^((r − δ)T) | |
| Value of long equity forward: Vₜ = [Sₜ − PV(remaining D)] − F₀ ÷ (1 + r)^(T − t) | |
| Bond futures: F₀ = [(B₀ + AI₀)(1 + r)ᵀ − AI_T − FVCI] ÷ CF | CF = conversion factor of the cheapest-to-deliver bond |
| Currency forward: F₀ = S₀ × (1 + r_p)ᵀ ÷ (1 + r_b)ᵀ | price/base quote |
| FRA value = notional × (new FRA rate − old FRA rate) × (days ÷ 360), discounted | |
| Swap fixed rate = (1 − PV_N) ÷ Σ PVᵢ | |
| Value of pay-fixed swap = (new swap rate − old swap rate) × Σ PVᵢ × notional | receive-fixed is the reverse |
| Equity swap value = equity return leg − fixed (or floating) leg | |
| Two-period binomial: c = [π²c_uu + 2π(1 − π)c_ud + (1 − π)²c_dd] ÷ (1 + r)² | |
| Black–Scholes–Merton call: c = S₀N(d₁) − Xe^(−rT)N(d₂) | |
| BSM put: p = Xe^(−rT)N(−d₂) − S₀N(−d₁) | |
| d₁ = [ln(S₀ ÷ X) + (r + σ² ÷ 2)T] ÷ (σ√T); d₂ = d₁ − σ√T | |
| With dividend yield δ: replace S₀ with S₀e^(−δT) | |
| Black model (futures options): c = e^(−rT)[F₀N(d₁) − XN(d₂)] | |
| Call delta = N(d₁) (× e^(−δT)); put delta = N(d₁) − 1 | |
| Option price change ≈ delta × ΔS + ½ × gamma × (ΔS)² | |
| Number of options to delta-hedge = −portfolio delta ÷ option delta | |
| Interest rate cap = portfolio of caplets (calls on rates); floor = portfolio of floorlets | |

## Alternative investments

| Formula | What it says |
|---|---|
| Property value = NOI₁ ÷ cap rate | |
| Cap rate ≈ discount rate − growth rate of NOI | |
| DCF value = Σ NOIₜ ÷ (1 + r)ᵗ + terminal value ÷ (1 + r)ᴺ, with terminal value = NOI_N+1 ÷ terminal cap rate | |
| Loan-to-value = loan ÷ property value | |
| Debt service coverage ratio = NOI ÷ annual debt service | |
| Equity dividend rate = first-year cash flow ÷ equity invested | cash-on-cash return |
| REIT NAV per share = (market value of real estate and other assets − liabilities) ÷ shares | |
| FFO = net income + depreciation − gains on property sales + losses | |
| AFFO = FFO − recurring capital expenditures (and straight-line rent adjustments) | |
| P/FFO and P/AFFO: price per share ÷ FFO (or AFFO) per share | REIT multiples |
| Venture method: POST = exit value ÷ (1 + r)ᴺ; PRE = POST − investment | |
| Ownership fraction f = investment ÷ POST | |
| New shares to issue = existing shares × f ÷ (1 − f); price per share = investment ÷ new shares | |
| Commodity forward: F₀ = S₀ × e^((r + c − y)T) | c = storage, y = convenience yield |
| Commodity futures return = spot return + roll return + collateral return | |

## Portfolio management

| Formula | What it says |
|---|---|
| APT: E(R) = R_f + β₁λ₁ + β₂λ₂ + … + βₖλₖ | λ = factor risk premiums |
| Active return = Σ (portfolio factor sensitivity − benchmark sensitivity) × factor return + security selection | |
| Active risk² = active factor risk + active specific risk | |
| Information ratio = active return ÷ active risk | |
| Tracking error = σ(R_p − R_b) | |
| Fundamental law: E(R_A) = TC × IC × √BR × σ_A | TC transfer coefficient, IC information coefficient, BR breadth |
| IR ≈ TC × IC × √BR | |
| Optimal active risk = (IR ÷ SR_B) × σ_B | |
| Combined Sharpe ratio: SR_P² = SR_B² + IR² | adding active risk optimally |
| Parametric VaR = [E(R) − z × σ] × portfolio value (as a loss) | |
| VaR over T days ≈ one-day VaR × √T | assumes independent returns |
| Expected shortfall = average loss beyond VaR | |
| Real risk-free rate + inflation premium + term premium + credit premium + liquidity premium = expected bond return | economics and markets |

## How to use this sheet

- **Level II is applied:** in item sets you must spot which model fits the company, such as FCFE versus dividends or residual income for a company with negative free cash flow.
- **Know the variations:** FCFF alone has four starting points. Practise converting between them.
- **Calculator:** the [BA II Plus guide](blog-ba-ii-plus-calculator-guide.html) covers the cash flow and statistics functions you will use for tree valuation and regression.
- **Read the strategy guide** on [Level II item sets](blog-level-2-item-sets.html) for how vignettes hide the inputs.

## Questions people ask

### Is a formula sheet provided in the CFA Level II exam?

No. As at Level I, you must know the formulas. Vignettes sometimes supply intermediate values, such as a regression output table or an option delta, but never the formula itself.

### How many formulas are in CFA Level II?

Roughly 250, including the Level I formulas you are still expected to know. The heaviest topics are equity valuation, fixed income and derivatives.

### Do I need to memorise Black–Scholes–Merton for Level II?

You should know the structure of the formula and what each term means. Most questions give N(d₁) and N(d₂) or the option's delta, and ask you to apply or interpret them, not to compute the normal distribution yourself.

## Sources

- [CFA Institute: Level II exam](https://www.cfainstitute.org/programs/cfa-program/candidate-resources/level-ii-exam)
- [CFA Institute: CFA Program curriculum topics](https://www.cfainstitute.org/programs/cfa-program/curriculum)
