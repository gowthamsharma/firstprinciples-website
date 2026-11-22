---
title: CFA Level I formula sheet: every formula you need, by topic
slug: blog-cfa-level-1-formula-sheet
order: 22
summary: The complete Level I formula sheet for 2026 and 2027: about 200 formulas across quantitative methods, economics, financial statement analysis, corporate issuers, equity, fixed income, derivatives, alternatives and portfolio management, each with a one-line note on what it means.
figure: bond_reason
caption: Behind most of these formulas is one idea: a value today is future cash discounted back.
tags: CFA level 1 formulas, CFA formula sheet, CFA level 1 formula sheet, CFA formulas list, CFA level 1 formula sheet pdf, CFA level 1 important formulas, CFA quant formulas, CFA fixed income formulas, CFA financial ratios, CFA level 1 formulas 2027
group: Tools: formulas, calculator and self-study
updated: 2026-11-22
seo_title: CFA Level I formula sheet 2026–2027: every formula by topic
meta: The complete CFA Level I formula sheet: about 200 formulas for quant, economics, FSA, corporate issuers, equity, fixed income, derivatives, alternatives and portfolio management.
---
No formula sheet is given in the exam, so you must carry these in your head. The good news: most are short, and many follow from a few ideas. Learn **what each one says** and you will rebuild the ones you forget. This sheet is our own summary of the formulas used in Level I calculations, organised by topic in the order of the curriculum. Ethics has no formulas.

Formula sheets for the other levels: [Level II](blog-cfa-level-2-formula-sheet.html) · [Level III](blog-cfa-level-3-formula-sheet.html).

[[figure]]

**Notation used throughout:** r = interest or discount rate per period, n = number of periods, t = tax rate, σ = standard deviation, ρ = correlation, β = beta, R_f = risk-free rate, D = dividend, E = earnings, P = price, V = value.

## Quantitative methods

### Rates and returns

| Formula | What it says |
|---|---|
| Holding-period return = (P₁ − P₀ + D₁) ÷ P₀ | price change plus income, over the start price |
| Arithmetic mean = ΣRᵢ ÷ n | best estimate of a single period's return |
| Geometric mean = [(1 + R₁)(1 + R₂)…(1 + Rₙ)]^(1/n) − 1 | the compound rate actually earned |
| Harmonic mean = n ÷ Σ(1 ÷ Xᵢ) | average cost per share with equal amounts invested (cost averaging) |
| Arithmetic mean ≥ geometric mean ≥ harmonic mean | the gap widens with volatility |
| Money-weighted return: IRR that solves Σ CFₜ ÷ (1 + IRR)ᵗ = 0 | the investor's own return; depends on timing of cash flows |
| Time-weighted return = [(1 + R₁)(1 + R₂)…(1 + Rₙ)]^(1/years) − 1 | the manager's return; ignores cash-flow timing |
| Annualised return = (1 + R_period)^(periods per year) − 1 | compound up to a year |
| Continuously compounded return = ln(P₁ ÷ P₀) = ln(1 + HPR) | additive across periods |
| Real return = (1 + nominal) ÷ (1 + inflation) − 1 | strip out inflation exactly (≈ nominal − inflation) |
| Leveraged return = R_p + (V_B ÷ V_E) × (R_p − r_D) | leverage magnifies the spread over the borrowing cost |
| After-tax nominal return = pre-tax return × (1 − t) | taxes reduce return |

### Time value of money

| Formula | What it says |
|---|---|
| FV = PV × (1 + r)ⁿ | money grows by compounding |
| PV = FV ÷ (1 + r)ⁿ | discounting is compounding in reverse |
| Effective annual rate = (1 + r_s ÷ m)ᵐ − 1 | stated rate r_s compounded m times a year |
| Continuous compounding: EAR = e^(r_s) − 1; FV = PV × e^(r_s × N) | the limit of compounding ever more often |
| PV of ordinary annuity = A × [1 − (1 + r)^(−n)] ÷ r | level payments at the end of each period |
| FV of ordinary annuity = A × [(1 + r)ⁿ − 1] ÷ r | the same payments, grown to the end |
| Annuity due = ordinary annuity × (1 + r) | payments at the start earn one more period |
| PV of perpetuity = A ÷ r | a level payment forever |
| PV of growing perpetuity = A₁ ÷ (r − g) | first payment over rate minus growth (r > g) |
| Implied growth rate = (FVₙ ÷ PV)^(1/n) − 1 | compound growth between two values |
| Forward rate from spot rates: (1 + S₂)² = (1 + S₁)(1 + f₁,₁) | no arbitrage across horizons |
| Cash flow additivity: PV of a series = sum of PVs | value pieces separately and add |

### Statistics and probability

| Formula | What it says |
|---|---|
| Sample variance s² = Σ(Xᵢ − X̄)² ÷ (n − 1) | average squared distance from the mean |
| Population variance σ² = Σ(Xᵢ − μ)² ÷ N | divide by N, not n − 1 |
| Mean absolute deviation = Σ∣Xᵢ − X̄∣ ÷ n | average distance, unsquared |
| Target semideviation = √[Σ over Xᵢ ≤ B of (Xᵢ − B)² ÷ (n − 1)] | downside risk below a target B |
| Coefficient of variation = s ÷ X̄ | risk per unit of return |
| Sample skewness ≈ (1 ÷ n) Σ(Xᵢ − X̄)³ ÷ s³ | negative: mean < median, long left tail |
| Excess kurtosis = kurtosis − 3 | positive: fat tails (leptokurtic) |
| Sample covariance = Σ(Xᵢ − X̄)(Yᵢ − Ȳ) ÷ (n − 1) | do two variables move together? |
| Correlation ρ = Cov(X, Y) ÷ (σ_X σ_Y) | covariance scaled to −1 … +1 |
| P(A or B) = P(A) + P(B) − P(AB) | addition rule |
| P(AB) = P(A ∣ B) × P(B) | multiplication rule |
| P(A) = Σ P(A ∣ Sᵢ) × P(Sᵢ) | total probability over scenarios |
| Bayes: P(E ∣ I) = P(I ∣ E) × P(E) ÷ P(I) | update a prior with new information |
| E(X) = Σ P(xᵢ) × xᵢ | probability-weighted average |
| Var(X) = Σ P(xᵢ) × [xᵢ − E(X)]² | probability-weighted squared deviation |
| Cov(X, Y) = Σ P(sᵢ) × [Xᵢ − E(X)][Yᵢ − E(Y)] | covariance from scenarios |
| Portfolio E(R_p) = Σ wᵢ E(Rᵢ) | expected returns add with weights |
| Portfolio variance (2 assets) = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂ | risk does not add unless ρ = 1 |
| Counting: n! ; combinations nCr = n! ÷ [(n − r)! r!] ; permutations nPr = n! ÷ (n − r)! | order does not or does matter |
| Binomial: P(X = x) = nCx × pˣ × (1 − p)^(n − x); mean np; variance np(1 − p) | x successes in n trials |
| z = (X − μ) ÷ σ | how many standard deviations from the mean |
| Roy's safety-first ratio = [E(R_p) − R_L] ÷ σ_p | choose the highest; R_L is the threshold |
| Lognormal: if ln X is normal, X is lognormal | used for prices, which cannot fall below zero |

### Sampling, estimation and hypothesis tests

| Formula | What it says |
|---|---|
| Standard error of the mean = s ÷ √n | how precisely the sample mean estimates μ |
| Confidence interval = X̄ ± z (or t) × s ÷ √n | 90%: 1.645; 95%: 1.96; 99%: 2.58 |
| t-test of a mean: t = (X̄ − μ₀) ÷ (s ÷ √n), df = n − 1 | is the mean different from μ₀? |
| Difference in means (equal variances): t = (X̄₁ − X̄₂) ÷ √(s_p²÷n₁ + s_p²÷n₂) | two independent samples |
| Paired comparisons: t = (d̄ − μ_d0) ÷ s_d̄ | dependent samples, such as before and after |
| Variance test: χ² = (n − 1)s² ÷ σ₀², df = n − 1 | one variance against a value |
| Equality of two variances: F = s₁² ÷ s₂² (larger on top) | df n₁ − 1 and n₂ − 1 |
| Correlation test: t = r√(n − 2) ÷ √(1 − r²), df = n − 2 | is the correlation zero? |
| Type I error = rejecting a true null (probability α) | Type II = failing to reject a false null; power = 1 − P(Type II) |

### Simple linear regression

| Formula | What it says |
|---|---|
| Slope b̂₁ = Cov(X, Y) ÷ Var(X) | change in Y per unit of X |
| Intercept b̂₀ = Ȳ − b̂₁X̄ | the line passes through the means |
| SST = SSR + SSE | total = explained + unexplained variation |
| R² = SSR ÷ SST = r² (one X variable) | share of variation explained |
| MSR = SSR ÷ k; MSE = SSE ÷ (n − k − 1) | mean squares (k = 1 here) |
| F = MSR ÷ MSE | is the model useful at all? |
| Standard error of estimate = √MSE | typical size of a residual |
| t for slope = (b̂₁ − B₁) ÷ s_b̂₁, df = n − 2 | is the slope different from B₁? |
| Prediction: Ŷ = b̂₀ + b̂₁X; interval Ŷ ± t_c × s_f | forecast and its range |
| Log-lin: ln Y = b₀ + b₁X; lin-log: Y = b₀ + b₁ ln X; log-log: ln Y = b₀ + b₁ ln X | functional forms for curved relationships |

## Economics

| Formula | What it says |
|---|---|
| Own-price elasticity = %ΔQ ÷ %ΔP = (∂Q/∂P) × (P ÷ Q) | ∣E∣ > 1 elastic; < 1 inelastic |
| Income elasticity = (∂Q/∂I) × (I ÷ Q) | > 0 normal good; < 0 inferior good |
| Cross-price elasticity = (∂Q_x/∂P_y) × (P_y ÷ Q_x) | > 0 substitutes; < 0 complements |
| Total revenue = P × Q; marginal revenue = ΔTR ÷ ΔQ | MR = P(1 − 1 ÷ ∣E∣) |
| Profit maximised where MR = MC | any market structure |
| Breakeven: P = ATC; shutdown (short run): P < AVC | cover all costs long term, variable costs short term |
| N-firm concentration ratio = sum of the N largest market shares | ignores how the rest is split |
| HHI = Σ (market shareᵢ)² | sensitive to the largest firms |
| GDP = C + I + G + (X − M) | expenditure approach |
| GDP deflator = nominal GDP ÷ real GDP × 100 | the price level of output |
| Fiscal multiplier = 1 ÷ [1 − MPC(1 − t)] | each unit of spending ripples through income |
| Money multiplier = 1 ÷ reserve requirement | deposits created per unit of reserves |
| Quantity theory: M × V = P × Y | money growth + velocity growth ≈ inflation + real growth |
| Fisher effect: nominal rate ≈ real rate + expected inflation | |
| Neutral policy rate = trend real growth + inflation target | policy rate above: contractionary |
| Cross rate: (A/B) = (A/C) × (C/B) | go through a common currency |
| %Δ in base currency = (new quote ÷ old quote) − 1 | for a quote in price/base |
| Forward = Spot × [1 + i_price × (days ÷ 360)] ÷ [1 + i_base × (days ÷ 360)] | covered interest rate parity |
| Forward points = (F − S) × 10,000 | quoted in pips |
| Real exchange rate (d/f) = S(d/f) × (P_f ÷ P_d) | nominal rate adjusted for price levels |
| Marshall–Lerner: ω_X ε_X + ω_M(ε_M − 1) > 0 | when depreciation improves the trade balance |

## Financial statement analysis

### Income statement and earnings per share

| Formula | What it says |
|---|---|
| Basic EPS = (net income − preferred dividends) ÷ weighted average shares | |
| Diluted EPS = (NI − pref div + convertible pref div + after-tax convertible debt interest) ÷ (WASO + new shares from conversion and options) | include only dilutive securities |
| Treasury stock method: new shares = n × (P_avg − X) ÷ P_avg | options exercised; proceeds buy back shares at the average price |
| Comprehensive income = net income + other comprehensive income | |
| Gross margin = (revenue − COGS) ÷ revenue | |

### Inventories and long-lived assets

| Formula | What it says |
|---|---|
| COGS = beginning inventory + purchases − ending inventory | |
| FIFO inventory = LIFO inventory + LIFO reserve | converting LIFO to FIFO |
| FIFO COGS = LIFO COGS − ΔLIFO reserve | |
| Net realisable value = selling price − costs to complete and sell | IFRS and US GAAP (non-LIFO): lower of cost and NRV |
| Straight-line depreciation = (cost − residual) ÷ useful life | |
| Double-declining balance = (2 ÷ life) × opening book value | ignores residual until the floor |
| Units of production = (cost − residual) × units used ÷ total units expected | |
| Average age = accumulated depreciation ÷ annual depreciation | |
| Remaining useful life = net PP&E ÷ annual depreciation | total life = gross PP&E ÷ depreciation |
| Impairment (IFRS): carrying amount > recoverable amount (higher of fair value less costs to sell and value in use) | |
| Impairment (US GAAP): test if carrying amount > undiscounted cash flows; loss = carrying amount − fair value | |
| Capitalised interest: added to asset cost, shown in investing cash flows | raises interest coverage in the year |

### Income taxes, debt and leases

| Formula | What it says |
|---|---|
| Income tax expense = taxes payable + ΔDTL − ΔDTA | |
| DTL = (carrying amount − tax base of asset) × tax rate, when carrying amount > tax base | pay more tax later |
| DTA = (tax base − carrying amount) × tax rate | pay less tax later |
| Effective tax rate = income tax expense ÷ pre-tax income | |
| Bond interest expense = carrying amount × market rate at issue | effective interest method |
| Discount amortisation = interest expense − coupon paid | |
| Lease liability = PV of lease payments at the lease rate | |
| Interest on lease liability = opening liability × rate | |
| Closing lease liability = opening + interest − payment | |
| Lessee (IFRS 16): depreciation of right-of-use asset + interest; US GAAP operating lease: single straight-line lease cost | |

### Cash flow statement

| Formula | What it says |
|---|---|
| CFO (indirect) = NI + non-cash charges − gains + losses − Δoperating assets + Δoperating liabilities | |
| Cash collected from customers = revenue − Δaccounts receivable | direct method |
| Cash paid to suppliers = COGS + Δinventory − Δaccounts payable | |
| FCFF = CFO + interest × (1 − t) − FCInv | free cash flow to all capital providers |
| FCFF = NI + NCC + interest × (1 − t) − FCInv − WCInv | |
| FCFE = CFO − FCInv + net borrowing | free cash flow to shareholders |
| Cash flow to revenue = CFO ÷ revenue | |
| Cash return on assets = CFO ÷ average total assets | |
| Cash flow to net income = CFO ÷ net income | earnings quality |
| Debt coverage = CFO ÷ total debt; interest coverage (cash) = (CFO + interest + taxes paid) ÷ interest paid | |

### Ratios

| Formula | What it says |
|---|---|
| Receivables turnover = revenue ÷ average receivables; DSO = 365 ÷ turnover | days to collect |
| Inventory turnover = COGS ÷ average inventory; DOH = 365 ÷ turnover | days on the shelf |
| Payables turnover = purchases ÷ average payables; DPO = 365 ÷ turnover | days to pay suppliers |
| Cash conversion cycle = DOH + DSO − DPO | days cash is tied up |
| Working capital turnover = revenue ÷ average working capital | |
| Fixed asset turnover = revenue ÷ average net fixed assets | |
| Total asset turnover = revenue ÷ average total assets | |
| Current ratio = current assets ÷ current liabilities | |
| Quick ratio = (cash + short-term investments + receivables) ÷ current liabilities | leaves out inventory |
| Cash ratio = (cash + short-term investments) ÷ current liabilities | |
| Defensive interval = (cash + short-term investments + receivables) ÷ daily cash expenditures | days the company could survive |
| Debt-to-assets = total debt ÷ total assets | |
| Debt-to-capital = total debt ÷ (total debt + equity) | |
| Debt-to-equity = total debt ÷ total equity | |
| Financial leverage = average total assets ÷ average equity | |
| Interest coverage = EBIT ÷ interest expense | |
| Fixed charge coverage = (EBIT + lease payments) ÷ (interest + lease payments) | |
| Operating margin = operating income ÷ revenue; net margin = NI ÷ revenue | |
| ROA = NI ÷ average total assets; operating ROA = operating income ÷ average total assets | |
| Return on total capital = EBIT ÷ (average debt + equity) | |
| ROE = NI ÷ average equity | |
| DuPont (3-step): ROE = (NI ÷ revenue) × (revenue ÷ assets) × (assets ÷ equity) | margin × turnover × leverage |
| DuPont (5-step): ROE = (NI ÷ EBT) × (EBT ÷ EBIT) × (EBIT ÷ revenue) × (revenue ÷ assets) × (assets ÷ equity) | tax burden × interest burden × EBIT margin × turnover × leverage |
| Dividend payout = dividends ÷ NI; retention b = 1 − payout | |
| Sustainable growth g = b × ROE | growth funded by retained earnings |
| P/E = price ÷ EPS; P/CF = price ÷ cash flow per share; P/S = price ÷ sales per share; P/B = price ÷ book value per share | valuation ratios |
| Credit: EBITDA ÷ interest; debt ÷ EBITDA; FFO ÷ debt; FCF after dividends ÷ debt | used by rating agencies |

## Corporate issuers

| Formula | What it says |
|---|---|
| NPV = Σ CFₜ ÷ (1 + r)ᵗ − CF₀ | value added by a project; accept if > 0 |
| IRR: rate at which NPV = 0 | accept if IRR > cost of capital |
| Profitability index = PV of future cash flows ÷ initial investment = 1 + NPV ÷ CF₀ | accept if > 1 |
| Payback period = years until cumulative cash flow turns positive | ignores time value and later cash flows |
| ROIC = after-tax operating profit ÷ average invested capital | compare with the cost of capital |
| WACC = w_d r_d(1 − t) + w_p r_p + w_e r_e | use target or market-value weights |
| Cost of preferred = D_p ÷ P_p | |
| After-tax cost of debt = YTM × (1 − t) | interest is tax-deductible |
| CAPM cost of equity = R_f + β[E(R_m) − R_f] | |
| Dividend discount cost of equity = D₁ ÷ P₀ + g | |
| Bond yield plus risk premium: r_e = r_d + risk premium | |
| Country risk: r_e = R_f + β[E(R_m) − R_f + CRP] | |
| Unlevered (asset) beta: β_A = β_E ÷ [1 + (1 − t) D ÷ E] | strip out the comparable's leverage |
| Relevered beta: β_E = β_A × [1 + (1 − t) D ÷ E] | apply the project's leverage |
| MM I without taxes: V_L = V_U | capital structure is irrelevant |
| MM II without taxes: r_e = r₀ + (r₀ − r_d)(D ÷ E) | equity gets riskier with debt |
| MM I with taxes: V_L = V_U + tD | value of the tax shield |
| MM II with taxes: r_e = r₀ + (r₀ − r_d)(1 − t)(D ÷ E) | |
| DOL = %ΔEBIT ÷ %Δsales = Q(P − V) ÷ [Q(P − V) − F] | operating leverage |
| DFL = %ΔNI ÷ %ΔEBIT = [Q(P − V) − F] ÷ [Q(P − V) − F − C] | C = fixed financing cost |
| DTL = DOL × DFL = Q(P − V) ÷ [Q(P − V) − F − C] | total leverage |
| Breakeven quantity = (F + C) ÷ (P − V); operating breakeven = F ÷ (P − V) | |
| Cost of trade credit = (1 + discount ÷ (1 − discount))^(365 ÷ days beyond discount period) − 1 | cost of skipping an early-payment discount |

## Equity investments

| Formula | What it says |
|---|---|
| Leverage ratio = 1 ÷ initial margin | |
| Margin call price = P₀ × (1 − initial margin) ÷ (1 − maintenance margin) | for a long position |
| Return on a margin purchase = (ending equity − beginning equity) ÷ beginning equity | includes dividends, interest and commissions |
| Price-weighted index = Σ prices ÷ divisor | high-priced stocks dominate; adjust divisor for splits |
| Market-cap-weighted: weightᵢ = (Pᵢ × Qᵢ) ÷ Σ(P × Q) | large companies dominate |
| Float-adjusted: use shares available to the public | |
| Equal-weighted: weight = 1 ÷ N | needs frequent rebalancing |
| Price return index vs total return index: total return = (P₁ − P₀ + income) ÷ P₀ | |
| Preferred share value = D_p ÷ r_p | perpetuity |
| Gordon growth model: V₀ = D₁ ÷ (r − g) = D₀(1 + g) ÷ (r − g) | r must exceed g |
| Multistage DDM: V₀ = Σ Dₜ ÷ (1 + r)ᵗ + Vₙ ÷ (1 + r)ⁿ, with Vₙ = Dₙ₊₁ ÷ (r − g) | high growth, then stable |
| FCFE model: V₀ = Σ FCFEₜ ÷ (1 + r)ᵗ | for companies that pay little in dividends |
| Implied required return: r = D₁ ÷ P₀ + g | |
| Justified forward P/E = (D₁ ÷ E₁) ÷ (r − g) | payout over (r − g) |
| Justified trailing P/E = payout × (1 + g) ÷ (r − g) | |
| Justified P/B = (ROE − g) ÷ (r − g) | |
| Enterprise value = market value of equity + debt + preferred + minority interest − cash and investments | |
| Equity value from EV = EV − debt − preferred − minority interest + cash | |
| Sustainable growth g = b × ROE | |

## Fixed income

### Prices and yields

| Formula | What it says |
|---|---|
| Price = Σ PMT ÷ (1 + r)ᵗ + FV ÷ (1 + r)ᴺ | a bond is a bundle of discounted payments |
| Price with spot rates = Σ PMTₜ ÷ (1 + Zₜ)ᵗ + FV ÷ (1 + Z_N)ᴺ | each cash flow at its own rate |
| Full price = PV at last coupon date × (1 + r)^(t ÷ T) | price between coupon dates |
| Accrued interest = (t ÷ T) × coupon | |
| Flat (clean) price = full price − accrued interest | the quoted price |
| Current yield = annual coupon ÷ flat price | income return only |
| Simple yield = (coupon + straight-line amortised gain or loss) ÷ flat price | |
| Yield to worst = lowest of yield to maturity and yields to each call date | |
| Periodicity conversion: (1 + APR_m ÷ m)ᵐ = (1 + APR_n ÷ n)ⁿ | compare yields with different frequencies |
| Money market, discount basis: PV = FV × [1 − (days ÷ year) × DR] | |
| Money market, add-on basis: PV = FV ÷ [1 + (days ÷ year) × AOR] | |
| Bond-equivalent yield = add-on rate on a 365-day basis | |
| Floating-rate note: coupon = reference rate + quoted margin; discount margin sets price | |
| Implied forward: (1 + Z_A)^A × (1 + IFR_A,B−A)^(B−A) = (1 + Z_B)^B | no arbitrage between maturities |
| G-spread = bond yield − government yield of same maturity; I-spread = bond yield − swap rate | |
| Z-spread: constant spread over every spot rate that reprices the bond | |
| Mortgage payment = loan × r ÷ [1 − (1 + r)^(−n)] | level-payment amortising loan |
| SMM = 1 − (1 − CPR)^(1/12) | monthly prepayment rate from the annual rate |

### Duration, convexity and credit

| Formula | What it says |
|---|---|
| Macaulay duration = Σ t × PV(CFₜ) ÷ price | weighted-average time to receive cash flows |
| Modified duration = Macaulay duration ÷ (1 + r) | % price change for a 1% change in yield |
| Approximate modified duration = (PV₋ − PV₊) ÷ (2 × Δyield × PV₀) | from two repricings |
| Approximate convexity = (PV₋ + PV₊ − 2PV₀) ÷ [(Δyield)² × PV₀] | curvature |
| Effective duration = (PV₋ − PV₊) ÷ (2 × Δcurve × PV₀) | for bonds with embedded options |
| %ΔPrice ≈ −ModDur × Δy + ½ × Convexity × (Δy)² | duration plus a curvature correction |
| Money duration = ModDur × full price of position | change in money terms per 1.00 change in yield |
| PVBP = (PV₋ − PV₊) ÷ 2, for a 1 bp shift | price value of a basis point |
| Portfolio duration ≈ Σ wᵢ × Durᵢ (market-value weights) | |
| Duration gap = Macaulay duration − investment horizon | positive: exposed to rising rates |
| Expected loss = probability of default × loss given default | |
| Loss given default = exposure × (1 − recovery rate) | |
| Yield spread ≈ expected loss + liquidity and risk premiums | |
| Return impact of a spread change ≈ −ModDur × Δspread + ½ × Convexity × (Δspread)² | |
| Credit enhancement of a tranche = principal of tranches below it ÷ pool | losses hit the most junior tranche first |

## Derivatives

| Formula | What it says |
|---|---|
| Forward price: F₀ = S₀ × (1 + r)ᵀ | no income or costs |
| With income and costs: F₀ = (S₀ − PV(income) + PV(costs)) × (1 + r)ᵀ | carry adjustments |
| Continuous: F₀ = S₀ × e^((r + c − i)T) | c = costs, i = income/convenience yield |
| Value of a long forward at t: Vₜ = Sₜ − F₀ ÷ (1 + r)^(T − t) | |
| Futures: daily settlement; margin call if balance < maintenance, top up to initial margin | |
| FRA settlement = notional × (MRR − FRA rate) × (days ÷ 360) ÷ [1 + MRR × (days ÷ 360)] | paid at the start of the period |
| Swap fixed rate = (1 − PV factor_N) ÷ Σ PV factors | fixed leg equals floating leg |
| Call payoff = max(0, S_T − X); put payoff = max(0, X − S_T) | |
| Profit = payoff − premium (long) | writers' profit is the reverse |
| Moneyness: call in the money if S > X; put if S < X | |
| Option value = intrinsic value + time value | |
| Lower bound of a European call = max(0, S₀ − X ÷ (1 + r)ᵀ) | |
| Put–call parity: S₀ + p₀ = c₀ + X ÷ (1 + r)ᵀ | protective put = fiduciary call |
| Put–call–forward parity: F₀ ÷ (1 + r)ᵀ + p₀ = c₀ + X ÷ (1 + r)ᵀ | |
| Binomial: π = (1 + r − d) ÷ (u − d) | risk-neutral probability of an up move |
| Option value = [π × V_up + (1 − π) × V_down] ÷ (1 + r) | discount the risk-neutral expectation |
| Hedge ratio h = (c₊ − c₋) ÷ (S₊ − S₋) | shares per option to replicate it |
| Covered call: max profit = X − S₀ + c₀; breakeven = S₀ − c₀ | |
| Protective put: max loss = S₀ − X + p₀; breakeven = S₀ + p₀ | |

## Alternative investments

| Formula | What it says |
|---|---|
| Management fee = rate × assets under management (start, end or average) | |
| Incentive fee = rate × (gain − hurdle), above any high-water mark | check: after or independent of the management fee? |
| Net return = (ending value − fees − beginning value) ÷ beginning value | |
| Fund-of-funds net return: apply both fee layers | |
| Carried interest (whole-of-fund) = carry rate × (total proceeds − committed capital) | deal-by-deal pays earlier |
| DPI = distributions ÷ paid-in capital; RVPI = NAV ÷ paid-in; TVPI = DPI + RVPI | private equity multiples |
| MOIC = (realised + unrealised value) ÷ invested capital | |
| Property value = NOI ÷ cap rate; cap rate = NOI ÷ value | direct capitalisation |
| NOI = rental income − vacancy − operating expenses (before interest, depreciation and tax) | |
| Commodity futures total return = spot return + roll return + collateral return | |
| Roll return > 0 in backwardation, < 0 in contango | |

## Portfolio management

| Formula | What it says |
|---|---|
| Utility: U = E(R) − ½Aσ² | A = risk aversion; returns in decimals |
| Capital allocation line: E(R_p) = R_f + [(E(R_i) − R_f) ÷ σᵢ] × σ_p | |
| Complete portfolio: E(R) = w R_risky + (1 − w)R_f; σ = w σ_risky | |
| Optimal risky weight y* = [E(R) − R_f] ÷ (Aσ²) | |
| Portfolio variance (2 assets) = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂ | |
| Total variance = β²σ_m² + σ_e² | systematic plus unsystematic |
| β = Cov(Rᵢ, R_m) ÷ σ_m² = ρ σᵢ ÷ σ_m | sensitivity to the market |
| Market model: Rᵢ = αᵢ + βᵢR_m + eᵢ | |
| CAPM / security market line: E(R) = R_f + β[E(R_m) − R_f] | return for systematic risk only |
| Capital market line: E(R_p) = R_f + [(E(R_m) − R_f) ÷ σ_m] × σ_p | efficient portfolios only |
| Sharpe ratio = (R_p − R_f) ÷ σ_p | excess return per unit of total risk |
| Treynor ratio = (R_p − R_f) ÷ β_p | excess return per unit of market risk |
| M² = R_f + (R_p − R_f) × (σ_m ÷ σ_p); M² alpha = M² − R_m | risk-adjusted, in percentage points |
| Jensen's alpha = R_p − [R_f + β_p(R_m − R_f)] | return above what the CAPM predicts |
| Parametric VaR ≈ (z × σ − μ) × portfolio value | z = 1.65 for 5%, 2.33 for 1% |

## How to remember them

- **Group them by idea**, not by chapter: most valuation formulas are "discount future cash", and most risk formulas are "variance plus a covariance term".
- **Write the sheet from memory** once a week and check the gaps against this page.
- **Understand the units**: a ratio of days to turnover, or of risk to return, is half the formula.
- **Practise with numbers:** work through the [Level I practice questions](cfa-level-1-practice-questions.html) and the [BA II Plus guide](blog-ba-ii-plus-calculator-guide.html), which shows the calculator steps for the time value, cash flow and statistics formulas.
- For the reasoning behind many of these, see the [prerequisite concepts](prerequisites.html).

## Questions people ask

### Is a formula sheet provided in the CFA exam?

No. You must know the formulas. Some questions give inputs you would otherwise derive, but you are never given a sheet.

### How many formulas are there in CFA Level I?

About 200, depending on how you count variations. The tables above list the ones used in Level I calculations. Around 80 of them come up often enough that you should be able to write them without thinking.

### Which Level I topics have the most formulas?

Quantitative methods, financial statement analysis and fixed income. Together they carry about a third of the exam, and most of their questions involve a calculation. Ethics has none.

### What is the best way to memorise CFA formulas?

Understand where each comes from, use them in practice questions daily, and rewrite them from memory regularly. Rote memorising alone fades quickly.

### Is there a formula sheet for Level II and Level III?

Yes: see the [Level II formula sheet](blog-cfa-level-2-formula-sheet.html) and the [Level III formula sheet](blog-cfa-level-3-formula-sheet.html).

## Sources

- [CFA Institute: Level I exam](https://www.cfainstitute.org/programs/cfa-program/candidate-resources/level-i-exam)
- [CFA Institute: CFA Program curriculum topics](https://www.cfainstitute.org/programs/cfa-program/curriculum)
