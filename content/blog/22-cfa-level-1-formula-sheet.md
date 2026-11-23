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

**Notation used throughout:** \(r\) = interest or discount rate per period, \(n\) = number of periods, \(t\) = tax rate, \(\sigma\) = standard deviation, \(\rho\) = correlation, \(\beta\) = beta, \(R_f\) = risk-free rate, \(D\) = dividend, \(E\) = earnings, \(P\) = price, \(V\) = value.

## Quantitative methods

### Rates and returns

| Formula | What it says |
|---|---|
| \(\text{HPR} = \dfrac{P_1 - P_0 + D_1}{P_0}\) | price change plus income, over the start price |
| \(\bar{R} = \dfrac{1}{n}\sum_{i=1}^{n} R_i\) | arithmetic mean: best estimate of a single period's return |
| \(\bar{R}_G = \left[\prod_{i=1}^{n}(1 + R_i)\right]^{1/n} - 1\) | geometric mean: the compound rate actually earned |
| \(\bar{X}_H = \dfrac{n}{\sum_{i=1}^{n} 1/X_i}\) | harmonic mean: average cost per share with equal amounts invested |
| \(\bar{X} \ge \bar{X}_G \ge \bar{X}_H\) | the gap widens with volatility |
| \(\sum_{t=0}^{T} \dfrac{CF_t}{(1 + \text{IRR})^t} = 0\) | money-weighted return: the investor's own return, sensitive to cash-flow timing |
| \(R_{TW} = \left[(1 + R_1)(1 + R_2)\cdots(1 + R_n)\right]^{1/\text{years}} - 1\) | time-weighted return: the manager's return |
| \(R_{\text{annual}} = (1 + R_{\text{period}})^{c} - 1\) | compound up to a year (\(c\) periods per year) |
| \(r_{cc} = \ln\!\left(\dfrac{P_1}{P_0}\right) = \ln(1 + \text{HPR})\) | continuously compounded return; adds across periods |
| \(1 + r_{\text{real}} = \dfrac{1 + r_{\text{nominal}}}{1 + \pi}\) | strip out inflation exactly (\(\approx r_{\text{nominal}} - \pi\)) |
| \(R_L = R_p + \dfrac{V_B}{V_E}(R_p - r_D)\) | leverage magnifies the spread over the borrowing cost |
| \(R_{\text{after tax}} = R(1 - t)\) | taxes reduce return |

### Time value of money

| Formula | What it says |
|---|---|
| \(FV = PV(1 + r)^n\) | money grows by compounding |
| \(PV = \dfrac{FV}{(1 + r)^n}\) | discounting is compounding in reverse |
| \(EAR = \left(1 + \dfrac{r_s}{m}\right)^m - 1\) | stated rate \(r_s\) compounded \(m\) times a year |
| \(EAR = e^{r_s} - 1;\quad FV = PV\,e^{r_s N}\) | continuous compounding |
| \(PV_{\text{annuity}} = A\,\dfrac{1 - (1 + r)^{-n}}{r}\) | level payments at the end of each period |
| \(FV_{\text{annuity}} = A\,\dfrac{(1 + r)^n - 1}{r}\) | the same payments, grown to the end |
| \(PV_{\text{due}} = PV_{\text{ordinary}} \times (1 + r)\) | payments at the start earn one more period |
| \(PV_{\text{perpetuity}} = \dfrac{A}{r}\) | a level payment forever |
| \(PV = \dfrac{A_1}{r - g}\) | growing perpetuity (\(r > g\)) |
| \(g = \left(\dfrac{FV_n}{PV}\right)^{1/n} - 1\) | implied compound growth rate |
| \((1 + S_2)^2 = (1 + S_1)(1 + f_{1,1})\) | forward rate from spot rates (no arbitrage) |
| \(PV = \sum_{t} \dfrac{CF_t}{(1 + r)^t}\) | cash flow additivity: value pieces separately and add |

### Statistics and probability

| Formula | What it says |
|---|---|
| \(s^2 = \dfrac{\sum (X_i - \bar{X})^2}{n - 1}\) | sample variance |
| \(\sigma^2 = \dfrac{\sum (X_i - \mu)^2}{N}\) | population variance |
| \(\text{MAD} = \dfrac{\sum \lvert X_i - \bar{X}\rvert}{n}\) | mean absolute deviation |
| \(s_{\text{target}} = \sqrt{\dfrac{\sum_{X_i \le B} (X_i - B)^2}{n - 1}}\) | target semideviation: downside risk below \(B\) |
| \(CV = \dfrac{s}{\bar{X}}\) | risk per unit of return |
| \(\text{Skewness} \approx \dfrac{1}{n}\,\dfrac{\sum (X_i - \bar{X})^3}{s^3}\) | negative: mean < median, long left tail |
| \(\text{Excess kurtosis} = \text{kurtosis} - 3\) | positive: fat tails (leptokurtic) |
| \(s_{XY} = \dfrac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{n - 1}\) | sample covariance |
| \(\rho_{XY} = \dfrac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}\) | covariance scaled to −1 … +1 |
| \(P(A \text{ or } B) = P(A) + P(B) - P(AB)\) | addition rule |
| \(P(AB) = P(A \mid B)\,P(B)\) | multiplication rule |
| \(P(A) = \sum_i P(A \mid S_i)\,P(S_i)\) | total probability over scenarios |
| \(P(E \mid I) = \dfrac{P(I \mid E)\,P(E)}{P(I)}\) | Bayes' formula: update a prior with new information |
| \(E(X) = \sum_i P(x_i)\,x_i\) | probability-weighted average |
| \(\text{Var}(X) = \sum_i P(x_i)\,[x_i - E(X)]^2\) | probability-weighted squared deviation |
| \(\text{Cov}(X, Y) = \sum_i P(s_i)\,[X_i - E(X)][Y_i - E(Y)]\) | covariance from scenarios |
| \(E(R_p) = \sum_i w_i\,E(R_i)\) | expected returns add with weights |
| \(\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\rho_{12}\sigma_1\sigma_2\) | risk does not add unless \(\rho = 1\) |
| \({}_nC_r = \dfrac{n!}{(n - r)!\,r!};\quad {}_nP_r = \dfrac{n!}{(n - r)!}\) | combinations (order does not matter) and permutations (it does) |
| \(P(X = x) = \binom{n}{x} p^x (1 - p)^{n - x};\quad \mu = np,\ \sigma^2 = np(1 - p)\) | binomial: \(x\) successes in \(n\) trials |
| \(z = \dfrac{X - \mu}{\sigma}\) | standard deviations from the mean |
| \(SFRatio = \dfrac{E(R_p) - R_L}{\sigma_p}\) | Roy's safety-first: choose the highest |
| \(\ln X \sim N(\mu, \sigma^2) \Rightarrow X \text{ is lognormal}\) | used for prices, which cannot fall below zero |

### Sampling, estimation and hypothesis tests

| Formula | What it says |
|---|---|
| \(s_{\bar{X}} = \dfrac{s}{\sqrt{n}}\) | standard error of the mean |
| \(\bar{X} \pm z_{\alpha/2}\,\dfrac{s}{\sqrt{n}}\) | confidence interval; \(z\) = 1.645 (90%), 1.96 (95%), 2.58 (99%) |
| \(t = \dfrac{\bar{X} - \mu_0}{s/\sqrt{n}},\quad df = n - 1\) | test of a mean |
| \(t = \dfrac{\bar{X}_1 - \bar{X}_2}{\sqrt{s_p^2/n_1 + s_p^2/n_2}}\) | difference in means (equal variances) |
| \(t = \dfrac{\bar{d} - \mu_{d0}}{s_{\bar{d}}}\) | paired comparisons (dependent samples) |
| \(\chi^2 = \dfrac{(n - 1)s^2}{\sigma_0^2},\quad df = n - 1\) | test of one variance |
| \(F = \dfrac{s_1^2}{s_2^2}\) | equality of two variances (larger on top); df \(n_1 - 1,\ n_2 - 1\) |
| \(t = \dfrac{r\sqrt{n - 2}}{\sqrt{1 - r^2}},\quad df = n - 2\) | is the correlation zero? |
| \(\text{Power} = 1 - P(\text{Type II error})\) | Type I: rejecting a true null (probability \(\alpha\)); Type II: failing to reject a false null |

### Simple linear regression

| Formula | What it says |
|---|---|
| \(\hat{b}_1 = \dfrac{\text{Cov}(X, Y)}{\text{Var}(X)}\) | slope: change in \(Y\) per unit of \(X\) |
| \(\hat{b}_0 = \bar{Y} - \hat{b}_1\bar{X}\) | the line passes through the means |
| \(SST = SSR + SSE\) | total = explained + unexplained variation |
| \(R^2 = \dfrac{SSR}{SST} = r^2\) | share of variation explained (one \(X\)) |
| \(MSR = \dfrac{SSR}{k};\quad MSE = \dfrac{SSE}{n - k - 1}\) | mean squares (\(k = 1\) here) |
| \(F = \dfrac{MSR}{MSE}\) | is the model useful at all? |
| \(s_e = \sqrt{MSE}\) | standard error of estimate: typical size of a residual |
| \(t = \dfrac{\hat{b}_1 - B_1}{s_{\hat{b}_1}},\quad df = n - 2\) | is the slope different from \(B_1\)? |
| \(\hat{Y} = \hat{b}_0 + \hat{b}_1 X;\quad \hat{Y} \pm t_c\,s_f\) | forecast and its prediction interval |
| \(\ln Y = b_0 + b_1X;\quad Y = b_0 + b_1\ln X;\quad \ln Y = b_0 + b_1\ln X\) | log-lin, lin-log and log-log forms |

## Economics

| Formula | What it says |
|---|---|
| \(E_P = \dfrac{\%\Delta Q}{\%\Delta P} = \dfrac{\partial Q}{\partial P}\cdot\dfrac{P}{Q}\) | own-price elasticity: \(\lvert E\rvert > 1\) elastic, \(< 1\) inelastic |
| \(E_I = \dfrac{\partial Q}{\partial I}\cdot\dfrac{I}{Q}\) | income elasticity: \(> 0\) normal good, \(< 0\) inferior good |
| \(E_{XY} = \dfrac{\partial Q_X}{\partial P_Y}\cdot\dfrac{P_Y}{Q_X}\) | cross-price: \(> 0\) substitutes, \(< 0\) complements |
| \(TR = P \times Q;\quad MR = P\left(1 - \dfrac{1}{\lvert E\rvert}\right)\) | total and marginal revenue |
| \(MR = MC\) | profit-maximising output in any market structure |
| \(P = ATC\) (breakeven); \(P < AVC\) (shut down in the short run) | cover all costs long term, variable costs short term |
| \(CR_N = \sum_{i=1}^{N} s_i\) | \(N\)-firm concentration ratio: ignores how the rest is split |
| \(HHI = \sum_i s_i^2\) | Herfindahl–Hirschman index: sensitive to the largest firms |
| \(GDP = C + I + G + (X - M)\) | expenditure approach |
| \(\text{GDP deflator} = \dfrac{\text{nominal GDP}}{\text{real GDP}} \times 100\) | the price level of output |
| \(\text{Fiscal multiplier} = \dfrac{1}{1 - MPC(1 - t)}\) | each unit of spending ripples through income |
| \(\text{Money multiplier} = \dfrac{1}{\text{reserve requirement}}\) | deposits created per unit of reserves |
| \(MV = PY\) | quantity theory: money + velocity growth ≈ inflation + real growth |
| \(i \approx r + \pi^e\) | Fisher effect |
| \(r_{\text{neutral}} = \text{trend real growth} + \pi^{\text{target}}\) | policy rate above it: contractionary |
| \(\dfrac{A}{B} = \dfrac{A}{C} \times \dfrac{C}{B}\) | cross rate through a common currency |
| \(\%\Delta \text{ base currency} = \dfrac{S_1}{S_0} - 1\) | for a quote in price/base |
| \(F = S\,\dfrac{1 + i_p \frac{\text{days}}{360}}{1 + i_b \frac{\text{days}}{360}}\) | covered interest rate parity |
| \(\text{Forward points} = (F - S) \times 10{,}000\) | quoted in pips |
| \(q_{d/f} = S_{d/f} \times \dfrac{P_f}{P_d}\) | real exchange rate |
| \(\omega_X\varepsilon_X + \omega_M(\varepsilon_M - 1) > 0\) | Marshall–Lerner: when depreciation improves the trade balance |

## Financial statement analysis

### Income statement and earnings per share

| Formula | What it says |
|---|---|
| \(\text{Basic EPS} = \dfrac{\text{NI} - \text{preferred dividends}}{\text{weighted average shares}}\) | |
| \(\text{Diluted EPS} = \dfrac{\text{NI} - \text{pref div} + \text{conv. pref div} + \text{conv. debt interest}(1 - t)}{\text{WASO} + \text{new shares}}\) | include only dilutive securities |
| \(\text{New shares} = n \times \dfrac{\bar{P} - X}{\bar{P}}\) | treasury stock method for options |
| \(\text{Comprehensive income} = \text{NI} + \text{OCI}\) | |
| \(\text{Gross margin} = \dfrac{\text{revenue} - \text{COGS}}{\text{revenue}}\) | |

### Inventories and long-lived assets

| Formula | What it says |
|---|---|
| \(\text{COGS} = \text{beginning inventory} + \text{purchases} - \text{ending inventory}\) | |
| \(\text{Inventory}_{\text{FIFO}} = \text{Inventory}_{\text{LIFO}} + \text{LIFO reserve}\) | converting LIFO to FIFO |
| \(\text{COGS}_{\text{FIFO}} = \text{COGS}_{\text{LIFO}} - \Delta\,\text{LIFO reserve}\) | |
| \(\text{NRV} = \text{selling price} - \text{costs to complete and sell}\) | lower of cost and NRV |
| \(\text{Straight-line} = \dfrac{\text{cost} - \text{residual}}{\text{useful life}}\) | |
| \(\text{DDB} = \dfrac{2}{\text{life}} \times \text{opening book value}\) | ignores residual until the floor |
| \(\text{Units of production} = (\text{cost} - \text{residual}) \times \dfrac{\text{units used}}{\text{total units}}\) | |
| \(\text{Average age} = \dfrac{\text{accumulated depreciation}}{\text{annual depreciation}}\) | |
| \(\text{Remaining life} = \dfrac{\text{net PP\&E}}{\text{annual depreciation}};\quad \text{total life} = \dfrac{\text{gross PP\&E}}{\text{depreciation}}\) | |
| IFRS impairment: carrying amount \(>\) recoverable amount \(= \max(\text{FV} - \text{costs to sell},\ \text{value in use})\) | |
| US GAAP: test if carrying amount \(>\) undiscounted cash flows; loss \(=\) carrying amount \(-\) fair value | |
| Capitalised interest: added to asset cost, shown in investing cash flows | raises interest coverage in the year |

### Income taxes, debt and leases

| Formula | What it says |
|---|---|
| \(\text{Tax expense} = \text{taxes payable} + \Delta\text{DTL} - \Delta\text{DTA}\) | |
| \(\text{DTL} = (\text{carrying amount} - \text{tax base}) \times t\) | asset with carrying amount above tax base: pay more tax later |
| \(\text{DTA} = (\text{tax base} - \text{carrying amount}) \times t\) | pay less tax later |
| \(\text{Effective tax rate} = \dfrac{\text{tax expense}}{\text{pre-tax income}}\) | |
| \(\text{Interest expense} = \text{carrying amount} \times r_{\text{market at issue}}\) | effective interest method |
| \(\text{Discount amortisation} = \text{interest expense} - \text{coupon paid}\) | |
| \(L_0 = \sum_t \dfrac{\text{lease payment}_t}{(1 + r)^t}\) | lease liability |
| \(\text{Interest}_t = L_{t-1} \times r;\quad L_t = L_{t-1} + \text{interest}_t - \text{payment}_t\) | lease liability over time |
| Lessee (IFRS 16): ROU depreciation + interest; US GAAP operating lease: single straight-line cost | |

### Cash flow statement

| Formula | What it says |
|---|---|
| \(\text{CFO} = \text{NI} + \text{non-cash charges} - \text{gains} + \text{losses} - \Delta\text{operating assets} + \Delta\text{operating liabilities}\) | indirect method |
| \(\text{Cash from customers} = \text{revenue} - \Delta\text{receivables}\) | direct method |
| \(\text{Cash to suppliers} = \text{COGS} + \Delta\text{inventory} - \Delta\text{payables}\) | |
| \(\text{FCFF} = \text{CFO} + \text{Int}(1 - t) - \text{FCInv}\) | to all capital providers |
| \(\text{FCFF} = \text{NI} + \text{NCC} + \text{Int}(1 - t) - \text{FCInv} - \text{WCInv}\) | |
| \(\text{FCFE} = \text{CFO} - \text{FCInv} + \text{net borrowing}\) | to shareholders |
| \(\dfrac{\text{CFO}}{\text{revenue}};\quad \dfrac{\text{CFO}}{\text{average total assets}};\quad \dfrac{\text{CFO}}{\text{NI}}\) | cash flow ratios (the last measures earnings quality) |
| \(\dfrac{\text{CFO}}{\text{total debt}};\quad \dfrac{\text{CFO} + \text{interest} + \text{taxes paid}}{\text{interest paid}}\) | debt and cash interest coverage |

### Ratios

| Formula | What it says |
|---|---|
| \(\text{Receivables turnover} = \dfrac{\text{revenue}}{\text{avg receivables}};\quad DSO = \dfrac{365}{\text{turnover}}\) | days to collect |
| \(\text{Inventory turnover} = \dfrac{\text{COGS}}{\text{avg inventory}};\quad DOH = \dfrac{365}{\text{turnover}}\) | days on the shelf |
| \(\text{Payables turnover} = \dfrac{\text{purchases}}{\text{avg payables}};\quad DPO = \dfrac{365}{\text{turnover}}\) | days to pay suppliers |
| \(\text{CCC} = DOH + DSO - DPO\) | days cash is tied up |
| \(\dfrac{\text{revenue}}{\text{avg working capital}};\quad \dfrac{\text{revenue}}{\text{avg net fixed assets}};\quad \dfrac{\text{revenue}}{\text{avg total assets}}\) | working capital, fixed asset and total asset turnover |
| \(\text{Current ratio} = \dfrac{\text{current assets}}{\text{current liabilities}}\) | |
| \(\text{Quick ratio} = \dfrac{\text{cash} + \text{ST investments} + \text{receivables}}{\text{current liabilities}}\) | leaves out inventory |
| \(\text{Cash ratio} = \dfrac{\text{cash} + \text{ST investments}}{\text{current liabilities}}\) | |
| \(\text{Defensive interval} = \dfrac{\text{cash} + \text{ST investments} + \text{receivables}}{\text{daily cash expenditures}}\) | days the company could survive |
| \(\dfrac{\text{debt}}{\text{assets}};\quad \dfrac{\text{debt}}{\text{debt} + \text{equity}};\quad \dfrac{\text{debt}}{\text{equity}}\) | solvency |
| \(\text{Financial leverage} = \dfrac{\text{avg total assets}}{\text{avg equity}}\) | |
| \(\text{Interest coverage} = \dfrac{\text{EBIT}}{\text{interest}};\quad \text{fixed charge coverage} = \dfrac{\text{EBIT} + \text{lease payments}}{\text{interest} + \text{lease payments}}\) | |
| \(\dfrac{\text{operating income}}{\text{revenue}};\quad \dfrac{\text{NI}}{\text{revenue}}\) | operating and net margin |
| \(ROA = \dfrac{\text{NI}}{\text{avg total assets}};\quad ROE = \dfrac{\text{NI}}{\text{avg equity}};\quad \text{return on capital} = \dfrac{\text{EBIT}}{\text{avg debt} + \text{equity}}\) | |
| \(ROE = \dfrac{\text{NI}}{\text{revenue}} \times \dfrac{\text{revenue}}{\text{assets}} \times \dfrac{\text{assets}}{\text{equity}}\) | DuPont: margin × turnover × leverage |
| \(ROE = \dfrac{\text{NI}}{\text{EBT}} \times \dfrac{\text{EBT}}{\text{EBIT}} \times \dfrac{\text{EBIT}}{\text{revenue}} \times \dfrac{\text{revenue}}{\text{assets}} \times \dfrac{\text{assets}}{\text{equity}}\) | five-step DuPont: tax burden × interest burden × EBIT margin × turnover × leverage |
| \(\text{Payout} = \dfrac{\text{dividends}}{\text{NI}};\quad b = 1 - \text{payout}\) | retention rate |
| \(g = b \times ROE\) | sustainable growth |
| \(\dfrac{P}{E},\ \dfrac{P}{CF},\ \dfrac{P}{S},\ \dfrac{P}{B}\) (per share) | valuation ratios |
| \(\dfrac{\text{EBITDA}}{\text{interest}};\quad \dfrac{\text{debt}}{\text{EBITDA}};\quad \dfrac{\text{FFO}}{\text{debt}}\) | credit ratios |

## Corporate issuers

| Formula | What it says |
|---|---|
| \(NPV = \sum_{t=1}^{n}\dfrac{CF_t}{(1 + r)^t} - CF_0\) | value added: accept if \(> 0\) |
| \(\sum_{t=0}^{n}\dfrac{CF_t}{(1 + \text{IRR})^t} = 0\) | accept if IRR \(>\) cost of capital |
| \(PI = \dfrac{PV(\text{future cash flows})}{CF_0} = 1 + \dfrac{NPV}{CF_0}\) | profitability index: accept if \(> 1\) |
| Payback = years until cumulative cash flow turns positive | ignores time value and later cash flows |
| \(\text{ROIC} = \dfrac{\text{after-tax operating profit}}{\text{avg invested capital}}\) | compare with the cost of capital |
| \(WACC = w_d r_d(1 - t) + w_p r_p + w_e r_e\) | target or market-value weights |
| \(r_p = \dfrac{D_p}{P_p}\) | cost of preferred |
| \(r_d(1 - t)\) | after-tax cost of debt |
| \(r_e = R_f + \beta[E(R_m) - R_f]\) | CAPM cost of equity |
| \(r_e = \dfrac{D_1}{P_0} + g\) | dividend discount cost of equity |
| \(r_e = r_d + \text{risk premium}\) | bond yield plus risk premium |
| \(r_e = R_f + \beta[E(R_m) - R_f + CRP]\) | with a country risk premium |
| \(\beta_A = \dfrac{\beta_E}{1 + (1 - t)\frac{D}{E}}\) | unlever a comparable's beta |
| \(\beta_E = \beta_A\left[1 + (1 - t)\dfrac{D}{E}\right]\) | relever for the project |
| \(V_L = V_U\) | MM I without taxes |
| \(r_e = r_0 + (r_0 - r_d)\dfrac{D}{E}\) | MM II without taxes |
| \(V_L = V_U + tD\) | MM I with taxes |
| \(r_e = r_0 + (r_0 - r_d)(1 - t)\dfrac{D}{E}\) | MM II with taxes |
| \(DOL = \dfrac{Q(P - V)}{Q(P - V) - F}\) | operating leverage |
| \(DFL = \dfrac{Q(P - V) - F}{Q(P - V) - F - C}\) | financial leverage (\(C\) = fixed financing cost) |
| \(DTL = DOL \times DFL = \dfrac{Q(P - V)}{Q(P - V) - F - C}\) | total leverage |
| \(Q_{BE} = \dfrac{F + C}{P - V};\quad Q_{OBE} = \dfrac{F}{P - V}\) | breakeven and operating breakeven |
| \(\text{Cost of trade credit} = \left(1 + \dfrac{\text{disc}}{1 - \text{disc}}\right)^{365/\text{days past discount}} - 1\) | cost of skipping an early-payment discount |

## Equity investments

| Formula | What it says |
|---|---|
| \(\text{Leverage ratio} = \dfrac{1}{\text{initial margin}}\) | |
| \(P = P_0\,\dfrac{1 - \text{initial margin}}{1 - \text{maintenance margin}}\) | margin call price for a long position |
| \(R = \dfrac{\text{ending equity} - \text{beginning equity}}{\text{beginning equity}}\) | margin return, including dividends, interest and commissions |
| \(\text{Price-weighted index} = \dfrac{\sum P_i}{\text{divisor}}\) | high-priced stocks dominate |
| \(w_i = \dfrac{P_iQ_i}{\sum_j P_jQ_j}\) | market-cap weighting (float-adjusted uses free-float shares) |
| \(w_i = \dfrac{1}{N}\) | equal weighting: needs frequent rebalancing |
| \(V_p = \dfrac{D_p}{r_p}\) | preferred share (perpetuity) |
| \(V_0 = \dfrac{D_1}{r - g} = \dfrac{D_0(1 + g)}{r - g}\) | Gordon growth model (\(r > g\)) |
| \(V_0 = \sum_{t=1}^{n}\dfrac{D_t}{(1 + r)^t} + \dfrac{V_n}{(1 + r)^n},\quad V_n = \dfrac{D_{n+1}}{r - g}\) | multistage dividend discount model |
| \(V_0 = \sum_t \dfrac{FCFE_t}{(1 + r)^t}\) | FCFE model |
| \(r = \dfrac{D_1}{P_0} + g\) | implied required return |
| \(\dfrac{P_0}{E_1} = \dfrac{D_1/E_1}{r - g}\) | justified forward P/E |
| \(\dfrac{P_0}{E_0} = \dfrac{(D_0/E_0)(1 + g)}{r - g}\) | justified trailing P/E |
| \(\dfrac{P_0}{B_0} = \dfrac{ROE - g}{r - g}\) | justified P/B |
| \(EV = \text{equity} + \text{debt} + \text{preferred} + \text{minority interest} - \text{cash}\) | enterprise value |
| \(g = b \times ROE\) | sustainable growth |

## Fixed income

### Prices and yields

| Formula | What it says |
|---|---|
| \(P = \sum_{t=1}^{N}\dfrac{PMT}{(1 + r)^t} + \dfrac{FV}{(1 + r)^N}\) | a bond is a bundle of discounted payments |
| \(P = \sum_{t=1}^{N}\dfrac{PMT_t}{(1 + Z_t)^t} + \dfrac{FV}{(1 + Z_N)^N}\) | each cash flow at its own spot rate |
| \(PV^{\text{full}} = PV \times (1 + r)^{t/T}\) | price between coupon dates |
| \(AI = \dfrac{t}{T} \times PMT\) | accrued interest |
| \(PV^{\text{flat}} = PV^{\text{full}} - AI\) | the quoted (clean) price |
| \(\text{Current yield} = \dfrac{\text{annual coupon}}{\text{flat price}}\) | income return only |
| \(\text{Simple yield} = \dfrac{\text{coupon} + \text{straight-line gain or loss}}{\text{flat price}}\) | |
| Yield to worst = lowest of the yield to maturity and the yields to each call date | |
| \(\left(1 + \dfrac{APR_m}{m}\right)^m = \left(1 + \dfrac{APR_n}{n}\right)^n\) | compare yields with different compounding |
| \(PV = FV\left(1 - \dfrac{\text{days}}{\text{year}} \times DR\right)\) | money market, discount basis |
| \(PV = \dfrac{FV}{1 + \frac{\text{days}}{\text{year}} \times AOR}\) | money market, add-on basis |
| Bond-equivalent yield = add-on rate on a 365-day basis | |
| \(\text{FRN coupon} = MRR + \text{quoted margin}\) | discount margin sets the price |
| \((1 + Z_A)^A(1 + IFR_{A,B-A})^{B-A} = (1 + Z_B)^B\) | implied forward rate |
| \(\text{G-spread} = y - y_{\text{gov}};\quad \text{I-spread} = y - \text{swap rate}\) | |
| \(P = \sum_t \dfrac{PMT_t}{(1 + z_t + Z)^t}\) | Z-spread \(Z\): one spread over every spot rate |
| \(A = \dfrac{rL}{1 - (1 + r)^{-n}}\) | level mortgage payment |
| \(SMM = 1 - (1 - CPR)^{1/12}\) | monthly prepayment rate |

### Duration, convexity and credit

| Formula | What it says |
|---|---|
| \(\text{MacDur} = \sum_t t \times \dfrac{PV(CF_t)}{P}\) | weighted-average time to receive cash flows |
| \(\text{ModDur} = \dfrac{\text{MacDur}}{1 + r}\) | % price change for a 1% change in yield |
| \(\text{ApproxModDur} = \dfrac{PV_- - PV_+}{2\,\Delta y\,PV_0}\) | from two repricings |
| \(\text{ApproxCon} = \dfrac{PV_- + PV_+ - 2PV_0}{(\Delta y)^2\,PV_0}\) | curvature |
| \(\text{EffDur} = \dfrac{PV_- - PV_+}{2\,\Delta\text{Curve}\,PV_0}\) | for bonds with embedded options |
| \(\%\Delta P \approx -\text{ModDur}\,\Delta y + \tfrac{1}{2}\,\text{Convexity}\,(\Delta y)^2\) | duration plus a curvature correction |
| \(\text{MoneyDur} = \text{ModDur} \times PV^{\text{full}}\) | change in money terms |
| \(PVBP = \dfrac{PV_- - PV_+}{2}\) for a 1 bp shift | price value of a basis point |
| \(D_p \approx \sum_i w_i D_i\) | portfolio duration |
| \(\text{Duration gap} = \text{MacDur} - \text{investment horizon}\) | positive: exposed to rising rates |
| \(EL = PD \times LGD;\quad LGD = \text{exposure}\times(1 - RR)\) | expected loss |
| \(\text{Spread} \approx EL + \text{liquidity and risk premiums}\) | |
| \(\%\Delta P \approx -\text{ModDur}\,\Delta s + \tfrac{1}{2}\,\text{Convexity}\,(\Delta s)^2\) | effect of a credit spread change |
| \(\text{Credit enhancement} = \dfrac{\text{tranches below}}{\text{pool}}\) | losses hit the most junior tranche first |

## Derivatives

| Formula | What it says |
|---|---|
| \(F_0 = S_0(1 + r)^T\) | forward price, no income or costs |
| \(F_0 = [S_0 - PV(I) + PV(C)](1 + r)^T\) | with income and costs of carry |
| \(F_0 = S_0\,e^{(r + c - i)T}\) | continuous compounding |
| \(V_t = S_t - \dfrac{F_0}{(1 + r)^{T - t}}\) | value of a long forward |
| Futures: daily settlement; margin call if the balance falls below maintenance, top up to initial margin | |
| \(\text{FRA settlement} = \dfrac{N(MRR - FRA)\frac{\text{days}}{360}}{1 + MRR\frac{\text{days}}{360}}\) | paid at the start of the period |
| \(s_N = \dfrac{1 - PV_N}{\sum_{i=1}^{N} PV_i}\) | swap fixed rate |
| \(c_T = \max(0, S_T - X);\quad p_T = \max(0, X - S_T)\) | option payoffs |
| \(\text{Profit} = \text{payoff} - \text{premium}\) | for the buyer; the writer's is the reverse |
| \(\text{Option value} = \text{intrinsic value} + \text{time value}\) | call in the money if \(S > X\), put if \(S < X\) |
| \(c_0 \ge \max\!\left(0, S_0 - \dfrac{X}{(1 + r)^T}\right)\) | lower bound of a European call |
| \(S_0 + p_0 = c_0 + \dfrac{X}{(1 + r)^T}\) | put–call parity |
| \(\dfrac{F_0}{(1 + r)^T} + p_0 = c_0 + \dfrac{X}{(1 + r)^T}\) | put–call–forward parity |
| \(\pi = \dfrac{1 + r - d}{u - d}\) | risk-neutral probability of an up move |
| \(V_0 = \dfrac{\pi V_u + (1 - \pi)V_d}{1 + r}\) | binomial option value |
| \(h = \dfrac{c_+ - c_-}{S_+ - S_-}\) | hedge ratio |
| Covered call: \(\max = X - S_0 + c_0\); breakeven \(= S_0 - c_0\) | |
| Protective put: \(\max\text{ loss} = S_0 - X + p_0\); breakeven \(= S_0 + p_0\) | |

## Alternative investments

| Formula | What it says |
|---|---|
| \(\text{Management fee} = \text{rate} \times AUM\) | on start, end or average assets |
| \(\text{Incentive fee} = \text{rate} \times (\text{gain} - \text{hurdle})\), above any high-water mark | check whether it is after the management fee |
| \(R_{\text{net}} = \dfrac{V_1 - \text{fees} - V_0}{V_0}\) | investor's net return |
| \(\text{Carried interest} = \text{carry rate} \times (\text{total proceeds} - \text{committed capital})\) | whole-of-fund waterfall |
| \(DPI = \dfrac{\text{distributions}}{\text{paid-in}};\quad RVPI = \dfrac{NAV}{\text{paid-in}};\quad TVPI = DPI + RVPI\) | private equity multiples |
| \(MOIC = \dfrac{\text{realised} + \text{unrealised value}}{\text{invested capital}}\) | |
| \(V = \dfrac{NOI}{\text{cap rate}}\) | direct capitalisation |
| \(NOI = \text{rental income} - \text{vacancy} - \text{operating expenses}\) | before interest, depreciation and tax |
| \(R = \text{spot return} + \text{roll return} + \text{collateral return}\) | commodity futures total return |

## Portfolio management

| Formula | What it says |
|---|---|
| \(U = E(R) - \tfrac{1}{2}A\sigma^2\) | utility; \(A\) = risk aversion, returns in decimals |
| \(E(R_p) = R_f + \dfrac{E(R_i) - R_f}{\sigma_i}\,\sigma_p\) | capital allocation line |
| \(E(R) = wR_{\text{risky}} + (1 - w)R_f;\quad \sigma = w\,\sigma_{\text{risky}}\) | complete portfolio |
| \(y^* = \dfrac{E(R) - R_f}{A\sigma^2}\) | optimal weight in the risky portfolio |
| \(\sigma_i^2 = \beta_i^2\sigma_m^2 + \sigma_e^2\) | systematic plus unsystematic risk |
| \(\beta_i = \dfrac{\text{Cov}(R_i, R_m)}{\sigma_m^2} = \rho_{i,m}\dfrac{\sigma_i}{\sigma_m}\) | sensitivity to the market |
| \(R_i = \alpha_i + \beta_i R_m + e_i\) | market model |
| \(E(R_i) = R_f + \beta_i[E(R_m) - R_f]\) | CAPM / security market line |
| \(E(R_p) = R_f + \dfrac{E(R_m) - R_f}{\sigma_m}\,\sigma_p\) | capital market line (efficient portfolios) |
| \(\text{Sharpe} = \dfrac{R_p - R_f}{\sigma_p}\) | excess return per unit of total risk |
| \(\text{Treynor} = \dfrac{R_p - R_f}{\beta_p}\) | excess return per unit of market risk |
| \(M^2 = R_f + (R_p - R_f)\dfrac{\sigma_m}{\sigma_p};\quad M^2\text{ alpha} = M^2 - R_m\) | risk-adjusted return in percentage points |
| \(\alpha_J = R_p - [R_f + \beta_p(R_m - R_f)]\) | Jensen's alpha |
| \(\text{VaR} \approx (z\sigma - \mu) \times \text{portfolio value}\) | \(z\) = 1.65 (5%), 2.33 (1%) |

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
