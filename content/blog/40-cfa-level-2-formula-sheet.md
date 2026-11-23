---
title: CFA Level II formula sheet: every formula you need, by topic
slug: blog-cfa-level-2-formula-sheet
order: 40
summary: The complete Level II formula sheet: multiple regression and time series, currencies and growth, pensions and multinational accounting, residual income and free cash flow valuation, bond trees and credit default swaps, Black–Scholes–Merton, real estate and private equity, and multifactor models, each with a one-line note.
figure: ddm_stack
caption: Most of Level II valuation is the Level I idea taken further: forecast the cash, then discount it at the right rate.
tags: CFA level 2 formulas, CFA level 2 formula sheet, CFA level II formula sheet, CFA level 2 formulas list, CFA level 2 equity valuation formulas, CFA level 2 fixed income formulas, CFA level 2 derivatives formulas, CFA level 2 quant formulas
group: Tools: formulas, calculator and self-study
updated: 2026-11-23
seo_title: CFA Level II formula sheet: every formula by topic (2026–2027)
meta: The complete CFA Level II formula sheet: regression, currencies, pensions, FCFF and residual income, bond trees, CDS, Black–Scholes–Merton, real estate and multifactor models.
---
Level II builds on Level I: you still need everything on the [Level I formula sheet](blog-cfa-level-1-formula-sheet.html), and Level II adds the valuation and modelling tools below. The exam does not give you a formula sheet, and item-set vignettes rarely tell you which formula to use. That is why knowing **when** a formula applies matters as much as remembering it.

Formula sheets for the other levels: [Level I](blog-cfa-level-1-formula-sheet.html) · [Level III](blog-cfa-level-3-formula-sheet.html).

[[figure]]

## How to learn from this sheet

Reading a list of formulas doesn't make them stick. Recalling them does. So this sheet is built to be worked, not just read:

1. **Start with the one idea.** Each topic opens with a short card: the single idea behind the topic, how the other formulas follow from it, a sanity check to catch a wrong answer, and the trap examiners set most often. If you understand the card, you can rebuild a formula you've forgotten.
2. **Test yourself.** Switch on *Quiz me* below. The formulas are hidden behind their meanings (or the other way round); try to write each one down, then reveal it and mark *Knew it* or *Not yet*.
3. **Come back to the gaps.** Your marks are saved in this browser. Tick *Only show the ones I'm still learning* and work just those, a few minutes a day, until every topic is complete.

[[studymode]]

## Quantitative methods

### Multiple regression

> **The one idea.** Multiple regression is simple regression with more than one lever. Each slope is the effect of one variable while the others are held still; every test asks whether what the model explains beats what it misses.
>
> **Build the rest from it.** Split the variation as before, \(SST = SSR + SSE\), but now charge for every variable: \(F = \tfrac{SSR/k}{SSE/(n - k - 1)}\) and \(\bar{R}^2 = 1 - \tfrac{n - 1}{n - k - 1}(1 - R^2)\). One coefficient at a time: \(t = \tfrac{\hat{b}_j}{s_{\hat{b}_j}}\).
>
> **Sanity check.** Add a useless variable and \(R^2\) still rises (or stays the same), but \(\bar{R}^2\) can fall. That is the point of adjusting.
>
> **Exam trap.** Degrees of freedom are \(n - k - 1\): one is used for the intercept, \(k\) for the slopes. Using \(n - 2\) here is the most common slip.

| Formula | What it says |
|---|---|
| \(\hat{Y} = \hat{b}_0 + \hat{b}_1X_1 + \cdots + \hat{b}_kX_k\) | each slope holds the other variables constant |
| \(t = \dfrac{\hat{b}_j - B_j}{s_{\hat{b}_j}},\quad df = n - k - 1\) | is one coefficient significant? |
| \(F = \dfrac{SSR/k}{SSE/(n - k - 1)}\) | are the slopes jointly zero? |
| \(R^2 = \dfrac{SSR}{SST}\) | share of variation explained |
| \(\bar{R}^2 = 1 - \dfrac{n - 1}{n - k - 1}(1 - R^2)\) | adjusted \(R^2\): penalises extra variables |
| \(AIC = n\ln\!\left(\dfrac{SSE}{n}\right) + 2(k + 1)\) | lower is better; for prediction |
| \(BIC = n\ln\!\left(\dfrac{SSE}{n}\right) + \ln(n)(k + 1)\) | lower is better; stronger penalty, for goodness of fit |
| \(F = \dfrac{(SSE_R - SSE_U)/q}{SSE_U/(n - k - 1)}\) | joint test: do \(q\) excluded variables matter? |
| \(BP = n \times R^2_{\hat{\varepsilon}^2},\ \chi^2_k\) | Breusch–Pagan test for conditional heteroskedasticity |
| Breusch–Godfrey: regress residuals on the \(X\)s and lagged residuals; \(F\) or \(\chi^2\) test | serial correlation |
| \(VIF_j = \dfrac{1}{1 - R_j^2}\) | above 5 a concern, above 10 serious multicollinearity |
| \(h_{ii} > \dfrac{3(k + 1)}{n}\) | high-leverage observation |
| \(D_i > 0.5\) possibly, \(> 1\) likely influential | Cook's distance: combines leverage and residual size |
| \(\ln\!\left(\dfrac{p}{1 - p}\right) = b_0 + b_1X_1 + \cdots\) | logistic regression: log odds are linear |
| \(p = \dfrac{1}{1 + e^{-(b_0 + b_1X_1 + \cdots)}}\) | probability from the logit |

### Time series

> **The one idea.** A time series forecasts the future from its own past. It only works if the series has a stable mean to return to (it is covariance-stationary).
>
> **Build the rest from it.** AR(1): \(x_t = b_0 + b_1x_{t-1} + \varepsilon_t\). Set \(x_t = x_{t-1} = \bar{x}\) and solve: the mean-reverting level is \(\tfrac{b_0}{1 - b_1}\). If \(b_1 = 1\), that level doesn't exist: a unit root, so first-difference the series.
>
> **Sanity check.** With \(b_0 = 2\) and \(b_1 = 0.5\), the series reverts to \(2/0.5 = 4\). Start at 4 and the forecast stays at 4.
>
> **Exam trap.** Test for a unit root with Dickey–Fuller, not with the ordinary t-test on \(b_1\).

| Formula | What it says |
|---|---|
| \(y_t = b_0 + b_1t + \varepsilon_t\) | linear trend: constant amount of growth |
| \(\ln y_t = b_0 + b_1t + \varepsilon_t\) | log-linear trend: constant rate of growth |
| \(x_t = b_0 + b_1x_{t-1} + \varepsilon_t\) | AR(1): today depends on yesterday |
| \(\hat{x} = \dfrac{b_0}{1 - b_1}\) | mean-reverting level |
| \(t = \dfrac{\hat{\rho}_k}{1/\sqrt{T}}\) | residual autocorrelations should be zero |
| \(x_t = x_{t-1} + \varepsilon_t\quad(b_1 = 1)\) | random walk (unit root): first-difference before modelling |
| add \(x_{t-4}\) (quarterly) or \(x_{t-12}\) (monthly) | seasonal lag |
| \(\hat{\varepsilon}_t^2 = a_0 + a_1\hat{\varepsilon}_{t-1}^2 + u_t\) | ARCH(1): if \(a_1\) is significant, variance is predictable |
| \(\hat{\sigma}_{t+1}^2 = \hat{a}_0 + \hat{a}_1\hat{\varepsilon}_t^2\) | predicted variance |
| \(RMSE = \sqrt{\dfrac{1}{n}\sum(\text{actual} - \text{forecast})^2}\) | out-of-sample forecast accuracy |
| Engle–Granger: regress \(y\) on \(x\), test the residuals for a unit root | cointegration |

### Machine learning and big data

> **The one idea.** Every classification score comes from one 2×2 table: what the model predicted against what was true. Each ratio picks a different row or column of that table.
>
> **Build the rest from it.** Precision divides by the predicted-positive column: \(\tfrac{TP}{TP + FP}\). Recall divides by the actually-positive row: \(\tfrac{TP}{TP + FN}\). \(F_1\) is their harmonic mean: \(\tfrac{2PR}{P + R}\).
>
> **Sanity check.** A model that labels everything positive has recall of 1 and poor precision; the \(F_1\) score exposes it.
>
> **Exam trap.** Accuracy misleads when classes are unbalanced: predicting \"no default\" for every borrower can score 98% and be useless.

| Formula | What it says |
|---|---|
| \(\text{Precision} = \dfrac{TP}{TP + FP}\) | of predicted positives, how many are right |
| \(\text{Recall} = \dfrac{TP}{TP + FN}\) | of actual positives, how many are found |
| \(\text{Accuracy} = \dfrac{TP + TN}{N}\) | |
| \(F1 = \dfrac{2 \times \text{precision} \times \text{recall}}{\text{precision} + \text{recall}}\) | balances precision and recall |
| \(X' = \dfrac{X - X_{\min}}{X_{\max} - X_{\min}}\) | normalisation to 0–1 |
| \(Z = \dfrac{X - \mu}{\sigma}\) | standardisation to mean 0, standard deviation 1 |
| \(TF = \dfrac{\text{count of a token}}{\text{total tokens}}\) | term frequency for text features |

## Economics

> **The one idea.** Currency quotes are prices of one money in another, so they chain and invert like fractions. Parity conditions say money earns the same everywhere once currencies are converted.
>
> **Build the rest from it.** Chain: \(\tfrac{A}{C} = \tfrac{A}{B} \times \tfrac{B}{C}\). Invert: \(\text{bid}(B/A) = 1/\text{offer}(A/B)\). Covered parity: \(F = S\,\tfrac{1 + i_p\frac{\text{days}}{360}}{1 + i_b\frac{\text{days}}{360}}\). Uncovered parity replaces \(F\) with the expected spot rate.
>
> **Sanity check.** Equal interest rates at home and abroad mean the forward equals spot.
>
> **Exam trap.** When you invert a quote, the bid and offer swap sides. The dealer always wins the spread, so check that your bid is below your offer.

| Formula | What it says |
|---|---|
| \(\text{bid}(A/C) = \text{bid}(A/B) \times \text{bid}(B/C)\); offer \(=\) offer \(\times\) offer | cross rates for quotes that chain |
| \(\text{bid}(B/A) = \dfrac{1}{\text{offer}(A/B)}\) | invert and swap sides |
| \(F = S\,\dfrac{1 + i_p\frac{\text{days}}{360}}{1 + i_b\frac{\text{days}}{360}}\) | covered interest rate parity |
| \(F - S = S\,\dfrac{(i_p - i_b)\frac{\text{days}}{360}}{1 + i_b\frac{\text{days}}{360}}\) | forward premium or discount |
| \(V = \dfrac{(F_{\text{new}} - F_{\text{old}}) \times \text{size}}{1 + i_p\frac{\text{days left}}{360}}\) | mark-to-market of a currency forward |
| \(E(\%\Delta S_{p/b}) \approx i_p - i_b\) | uncovered interest parity |
| \(\%\Delta S_{p/b} \approx \pi_p - \pi_b\) | relative purchasing power parity |
| \(i_p - i_b \approx E(\pi_p) - E(\pi_b)\) | international Fisher effect |
| \(r_p - r_b = E(\%\Delta q_{p/b})\) | real interest rate parity |
| \(R_{\text{carry}} \approx i_{\text{high}} - i_{\text{low}} - \%\Delta S\) | carry trade return |
| \(Y = AK^{\alpha}L^{1-\alpha}\) | Cobb–Douglas production function |
| \(\%\Delta Y = \%\Delta A + \alpha\,\%\Delta K + (1 - \alpha)\,\%\Delta L\) | growth accounting |
| \(g_{\text{potential}} = g_{\text{labour force}} + g_{\text{labour productivity}}\) | |
| \(g_{Y/L} = \%\Delta A + \alpha(\%\Delta K - \%\Delta L)\) | capital deepening plus technology |
| \(g^* = \dfrac{\theta}{1 - \alpha}\) | neoclassical steady state; \(\theta\) = total factor productivity growth |

## Financial statement analysis

> **The one idea.** Intercorporate investments come down to how much control you have: little (fair value), significant influence (equity method, one line), or control (consolidate everything, line by line).
>
> **Build the rest from it.** Equity method: \(\text{Investment}_t = \text{cost} + \text{share of NI} - \text{dividends}\). Consolidation adds 100% of the subsidiary and carves out the non-controlling interest. Goodwill is the price paid above the fair value of what can be identified.
>
> **Sanity check.** Equity method and consolidation give the same net income and equity attributable to the parent; only the size of the lines differs.
>
> **Exam trap.** Dividends from an equity-method investee reduce the investment; they are not income.

| Formula | What it says |
|---|---|
| \(\text{Investment}_t = \text{cost} + \text{share of NI} - \text{dividends received}\) | equity method |
| \(\text{Goodwill}_{\text{partial}} = \text{price} - \text{share of FV of identifiable net assets}\) | IFRS option |
| \(\text{Goodwill}_{\text{full}} = \text{FV of acquiree} - \text{FV of identifiable net assets}\) | US GAAP; IFRS option |
| \(NCI = \text{NCI share} \times \text{FV of subsidiary}\) | under full goodwill |
| \(\text{Funded status} = FV_{\text{plan assets}} - DBO\) | negative: net pension liability |
| \(DBO_1 = DBO_0 + SC + IC + PSC \pm \text{actuarial losses/gains} - \text{benefits paid}\) | defined benefit obligation |
| \(\text{Assets}_1 = \text{Assets}_0 + \text{actual return} + \text{contributions} - \text{benefits paid}\) | plan assets |
| \(\text{IFRS P\&L cost} = SC + r_{\text{disc}} \times \text{net DB liability}\) | remeasurements go to OCI |
| \(\text{US GAAP cost} = SC + IC - \text{expected return} + \text{amortisation}\) | |
| \(\text{TPPC} = \text{contributions} - (\text{FS}_1 - \text{FS}_0)\) | total periodic pension cost: the economic cost of the year |
| \(\text{Share-based expense} = \dfrac{\text{FV at grant}}{\text{vesting period}}\) | |
| Current rate method: assets and liabilities at \(S_{\text{current}}\), income statement at \(\bar{S}\), equity historical; CTA in OCI | functional ≠ presentation currency |
| Temporal method: monetary items at \(S_{\text{current}}\), non-monetary at \(S_{\text{historical}}\); gain or loss in NI | functional = parent's currency |
| \(CET1 \text{ ratio} = \dfrac{CET1}{RWA}\) | bank solvency |
| \(LCR = \dfrac{HQLA}{\text{30-day net cash outflows}} \ge 100\%\) | liquidity coverage |
| \(NSFR = \dfrac{\text{available stable funding}}{\text{required stable funding}} \ge 100\%\) | net stable funding |
| \(\text{Combined ratio} = \text{loss ratio} + \text{expense ratio}\) | insurer: below 100% is an underwriting profit |
| \(\dfrac{NOA_1 - NOA_0}{\overline{NOA}}\) | balance sheet accruals ratio |
| \(\dfrac{NI - (CFO + CFI)}{\overline{NOA}}\) | cash flow accruals ratio |
| \(Z = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E\) | Altman Z-score |

## Corporate issuers

> **The one idea.** Capital structure, payouts and buybacks change how value is split and taxed, not (in a perfect market) how much value there is. The formulas measure the frictions: taxes and the cost of funds.
>
> **Build the rest from it.** Modigliani–Miller with taxes: \(V_L = V_U + tD\) and \(r_e = r_0 + (r_0 - r_d)(1 - t)\tfrac{D}{E}\). Buyback test: EPS rises when the earnings yield \(E/P\) exceeds the after-tax cost of the funds used.
>
> **Sanity check.** With \(D = 0\), \(V_L = V_U\) and \(r_e = r_0\).
>
> **Exam trap.** A buyback above book value per share lowers BVPS even if EPS goes up. Judge them separately.

| Formula | What it says |
|---|---|
| \(EPS_{\text{after}} = \dfrac{\text{earnings} - \text{after-tax cost of funds}}{\text{shares after buyback}}\) | rises if earnings yield \(>\) after-tax cost of debt |
| \(BVPS_{\text{after}} = \dfrac{\text{equity} - \text{buyback cost}}{\text{shares after}}\) | falls if price \(>\) BVPS |
| \(t_{\text{eff}} = t_c + (1 - t_c)\,t_i\) | double taxation of dividends |
| \(t_{\text{eff}} = t_{c,d} + (1 - t_{c,d})\,t_i\) | split-rate system |
| \(\dfrac{NI}{\text{dividends}};\quad \dfrac{FCFE}{\text{dividends} + \text{buybacks}}\) | payout coverage |
| \(r_e = R_f + ERP + \text{size premium} + \text{specific risk premium}\) | build-up method |
| \(ERP = ERP_{\text{developed}} + \text{country spread}\) | country spread model |
| \(V_{AT} = V_A + V_T + S - C\) | combined value after a merger |
| \(\text{Gain}_T = \text{premium} = P_T - V_T;\quad \text{Gain}_A = S - (P_T - V_T)\) | who captures the synergies |
| \(\Delta HHI = 2\,s_A\,s_B\) | antitrust screening |

## Equity valuation

### Return concepts and dividend models

> **The one idea.** Required return is what investors demand for the risk; expected return is what you think the price implies. Dividend models link the two through growth.
>
> **Build the rest from it.** Gordon: \(V_0 = \tfrac{D_1}{r - g}\) rearranges to \(r = \tfrac{D_1}{P_0} + g\). Multi-stage models discount the high-growth dividends one by one and then add a Gordon terminal value. H-model: \(V_0 = \tfrac{D_0(1 + g_L) + D_0H(g_S - g_L)}{r - g_L}\).
>
> **Sanity check.** If \(H = 0\) (no extra growth period), the H-model collapses to Gordon.
>
> **Exam trap.** Discount the terminal value from the year it is calculated, not from the year after.

| Formula | What it says |
|---|---|
| \(r = R_f + \beta_{mkt}MKT + \beta_{size}SMB + \beta_{value}HML\) | Fama–French |
| \(ERP = \dfrac{D_1}{P_0} + g - R_f\) | Gordon implied equity risk premium |
| \(\alpha = E(R) - r\) | expected minus required return |
| \(V_0 = \dfrac{D_1}{r - g}\) | Gordon growth |
| \(V_0 = \dfrac{E_1}{r} + PVGO\) | value of growth opportunities |
| \(\dfrac{P_0}{E_1} = \dfrac{1 - b}{r - g};\quad \dfrac{P_0}{E_0} = \dfrac{(1 - b)(1 + g)}{r - g}\) | justified leading and trailing P/E |
| \(V_0 = \dfrac{D_0(1 + g_L)}{r - g_L} + \dfrac{D_0\,H\,(g_S - g_L)}{r - g_L}\) | H-model; \(H\) = half the decline period |
| \(g = b \times ROE\) | sustainable growth |
| \(g = b \times \dfrac{NI}{S} \times \dfrac{S}{TA} \times \dfrac{TA}{E}\) | PRAT model |
| \(r = \dfrac{D_0}{P_0}\left[(1 + g_L) + H(g_S - g_L)\right] + g_L\) | implied return from the H-model |

### Free cash flow models

> **The one idea.** Free cash flow is cash the business throws off after it reinvests. FCFF belongs to everyone who funded the firm; FCFE is what is left for shareholders after debt holders are paid.
>
> **Build the rest from it.** Start anywhere and add back what isn't cash: \(FCFF = EBIT(1 - t) + Dep - FCInv - WCInv\). Then \(FCFE = FCFF - Int(1 - t) + \text{net borrowing}\). Discount FCFF at WACC (firm value) and FCFE at \(r_e\) (equity value).
>
> **Sanity check.** A firm with no debt has \(FCFF = FCFE\), and WACC equals the cost of equity.
>
> **Exam trap.** Match the cash flow to the rate: FCFF with WACC, FCFE with the cost of equity. Mixing them is a guaranteed wrong answer.

| Formula | What it says |
|---|---|
| \(FCFF = NI + NCC + Int(1 - t) - FCInv - WCInv\) | to all capital providers |
| \(FCFF = CFO + Int(1 - t) - FCInv\) | |
| \(FCFF = EBIT(1 - t) + Dep - FCInv - WCInv\) | |
| \(FCFF = EBITDA(1 - t) + Dep \cdot t - FCInv - WCInv\) | |
| \(FCFE = FCFF - Int(1 - t) + \text{net borrowing}\) | to shareholders |
| \(FCFE = NI + NCC - FCInv - WCInv + \text{net borrowing}\) | |
| \(FCFE = NI - (1 - DR)(FCInv - Dep) - (1 - DR)\,WCInv\) | with a target debt ratio \(DR\) |
| \(V_{\text{firm}} = \dfrac{FCFF_1}{WACC - g};\quad V_{\text{equity}} = V_{\text{firm}} - \text{debt}\) | |
| \(V_{\text{equity}} = \dfrac{FCFE_1}{r - g}\) | |

### Residual income, multiples and private companies

> **The one idea.** Residual income is profit above the rent on the owners' capital. Value is what's on the books today plus the present value of all future profit above that rent.
>
> **Build the rest from it.** \(RI_t = E_t - rB_{t-1} = (ROE - r)B_{t-1}\). Value: \(V_0 = B_0 + \sum \tfrac{RI_t}{(1 + r)^t}\). With constant growth: \(V_0 = B_0 + \tfrac{(ROE - r)B_0}{r - g}\), which gives the justified \(P/B = 1 + \tfrac{ROE - r}{r - g}\).
>
> **Sanity check.** If \(ROE = r\), residual income is zero and the firm is worth exactly book value: \(P/B = 1\).
>
> **Exam trap.** Use beginning-of-period book value in \(rB_{t-1}\).

| Formula | What it says |
|---|---|
| \(RI_t = E_t - rB_{t-1} = (ROE_t - r)B_{t-1}\) | profit above the cost of equity |
| \(V_0 = B_0 + \sum_{t=1}^{\infty}\dfrac{RI_t}{(1 + r)^t}\) | book value plus PV of residual income |
| \(V_0 = B_0 + \dfrac{(ROE - r)B_0}{r - g}\) | single-stage residual income |
| \(\dfrac{P_0}{B_0} = 1 + \dfrac{ROE - r}{r - g} = \dfrac{ROE - g}{r - g}\) | justified P/B |
| \(PV_{\text{terminal}} = \dfrac{RI_T}{1 + r - \omega}\) | persistence \(\omega\) between 0 and 1 |
| \(B_t = B_{t-1} + E_t - D_t\) | clean surplus |
| \(EVA = NOPAT - WACC \times \text{invested capital}\) | |
| \(\dfrac{P_0}{S_0} = \dfrac{(E_0/S_0)(1 - b)(1 + g)}{r - g}\) | justified P/S |
| \(PEG = \dfrac{P/E}{g\ (\%)}\) | |
| \(\overline{P/E}_H = \dfrac{n}{\sum 1/(P/E)_i}\) | harmonic mean P/E |
| \(DLOC = 1 - \dfrac{1}{1 + \text{control premium}}\) | discount for lack of control |
| \(\text{Total discount} = 1 - (1 - DLOC)(1 - DLOM)\) | discounts multiply |
| \(V = \dfrac{FCFF_1}{WACC - g}\) | capitalised cash flow method |

## Fixed income

> **The one idea.** One curve prices everything. Spot rates, forward rates and par rates are three views of the same discount factors, and arbitrage keeps them consistent.
>
> **Build the rest from it.** Forward rate model: \((1 + z_B)^B = (1 + z_A)^A(1 + f_{A,B-A})^{B-A}\). Binomial trees value bonds with options by backward induction: at each node, \(V = \tfrac{0.5(V_u + C) + 0.5(V_d + C)}{1 + r}\). Option value \(= V_{\text{straight}} - V_{\text{callable}}\).
>
> **Sanity check.** In a flat curve, spot = forward = par = the same rate.
>
> **Exam trap.** A call option benefits the issuer, so it lowers the bond's value; a put benefits the holder and raises it.

| Formula | What it says |
|---|---|
| \(P(T^*) = P(T) \times F(T, T^*)\) | forward pricing model |
| \((1 + z_B)^B = (1 + z_A)^A(1 + f_{A,B-A})^{B-A}\) | forward rate model |
| Bootstrapping: solve each spot rate from par yields in sequence | |
| \(\text{Swap spread} = s_N - y_{\text{gov},N}\) | |
| \(\text{Rolldown return} = \dfrac{P_{\text{rolled}} - P_0}{P_0}\) | stable curve |
| \(V = \dfrac{\tfrac{1}{2}(V_u + C) + \tfrac{1}{2}(V_d + C)}{1 + r_{\text{node}}}\) | binomial tree, backward induction |
| \(r_u = r_d\,e^{2\sigma}\) | adjacent rates in a lognormal tree |
| \(V_{\text{callable}} = V_{\text{straight}} - V_{\text{call}}\) | |
| \(V_{\text{putable}} = V_{\text{straight}} + V_{\text{put}}\) | |
| OAS: constant spread over the tree that reprices the bond | removes the option's effect |
| \(ED = \dfrac{PV_- - PV_+}{2\,\Delta\text{Curve}\,PV_0}\) | effective duration |
| \(EC = \dfrac{PV_- + PV_+ - 2PV_0}{(\Delta\text{Curve})^2\,PV_0}\) | effective convexity (negative for callables at low rates) |
| \(V_{\text{capped}} = V_{\text{straight}} - V_{\text{cap}};\quad V_{\text{floored}} = V_{\text{straight}} + V_{\text{floor}}\) | floaters with caps and floors |
| \(\text{Conversion price} = \dfrac{\text{par}}{\text{conversion ratio}}\) | |
| \(\text{Conversion value} = S \times \text{conversion ratio}\) | |
| \(\text{Market conversion price} = \dfrac{P_{\text{convertible}}}{\text{conversion ratio}}\) | |
| \(\text{Premium per share} = \text{market conversion price} - S\) | |
| \(V_{\min} = \max(\text{straight value}, \text{conversion value})\) | |
| \(EL = PD \times LGD\) | expected loss |
| \(P(\text{survival to } t) = (1 - h)^t\) | hazard rate \(h\) |
| \(CVA = \sum_t EL_t \times DF_t\) | credit valuation adjustment |
| \(\text{Spread} \approx h(1 - RR)\) | |
| \(\text{Upfront} \approx (\text{spread} - \text{fixed coupon}) \times \text{CDS duration}\) | CDS upfront premium |
| \(\text{Price per 100} \approx 100 - \text{upfront}(\%)\) | |
| \(\Delta V \approx \Delta\text{spread} \times \text{CDS duration} \times \text{notional}\) | |

## Derivatives

> **The one idea.** Carry arbitrage: the forward price is the spot price grown at the financing rate, less whatever the asset pays you while you hold it.
>
> **Build the rest from it.** \(F_0 = [S_0 - PV(\text{income})](1 + r)^T\), or \(S_0e^{(r - \delta)T}\) with a yield. Value mid-life \(= PV(\text{new forward price} - \text{old forward price})\). Swaps are a portfolio of forwards; options use the binomial model or Black–Scholes–Merton.
>
> **Sanity check.** An asset that pays nothing and costs nothing to hold gives \(F_0 = S_0(1 + r)^T\), the Level I result.
>
> **Exam trap.** Value a long forward as (current underlying value − PV of the agreed price), not as the difference in forward prices left undiscounted.

| Formula | What it says |
|---|---|
| \(F_0 = [S_0 - PV(D)](1 + r)^T\) | equity forward with discrete dividends |
| \(F_0 = S_0\,e^{(r - \delta)T}\) | with a dividend yield |
| \(V_t = [S_t - PV(D)] - \dfrac{F_0}{(1 + r)^{T - t}}\) | value of a long equity forward |
| \(F_0 = \dfrac{(B_0 + AI_0)(1 + r)^T - AI_T - FVCI}{CF}\) | bond futures; \(CF\) = conversion factor |
| \(F_0 = S_0\,\dfrac{(1 + r_p)^T}{(1 + r_b)^T}\) | currency forward |
| \(V_{FRA} = N(\text{FRA}_{\text{new}} - \text{FRA}_{\text{old}})\dfrac{\text{days}}{360}\), discounted | |
| \(s = \dfrac{1 - PV_N}{\sum_{i=1}^{N} PV_i}\) | swap fixed rate |
| \(V_{\text{pay-fixed}} = (s_{\text{new}} - s_{\text{old}})\sum PV_i \times N\) | receive-fixed is the reverse |
| \(c_0 = \dfrac{\pi^2c_{uu} + 2\pi(1 - \pi)c_{ud} + (1 - \pi)^2c_{dd}}{(1 + r)^2}\) | two-period binomial |
| \(c = S_0N(d_1) - Xe^{-rT}N(d_2)\) | Black–Scholes–Merton call |
| \(p = Xe^{-rT}N(-d_2) - S_0N(-d_1)\) | BSM put |
| \(d_1 = \dfrac{\ln(S_0/X) + (r + \sigma^2/2)T}{\sigma\sqrt{T}};\quad d_2 = d_1 - \sigma\sqrt{T}\) | |
| replace \(S_0\) with \(S_0e^{-\delta T}\) | with a dividend yield |
| \(c = e^{-rT}[F_0N(d_1) - XN(d_2)]\) | Black model (futures options) |
| \(\Delta_c = N(d_1);\quad \Delta_p = N(d_1) - 1\) | delta (times \(e^{-\delta T}\) with dividends) |
| \(\Delta c \approx \Delta \cdot \Delta S + \tfrac{1}{2}\Gamma(\Delta S)^2\) | delta–gamma approximation |
| \(N_{\text{options}} = -\dfrac{\text{portfolio delta}}{\text{option delta}}\) | delta hedge |
| Cap = portfolio of caplets; floor = portfolio of floorlets | |

## Alternative investments

> **The one idea.** Real estate is a stream of rent, valued like a bond. The cap rate is the property's current yield; growth is what turns it into a total return.
>
> **Build the rest from it.** \(V = \tfrac{NOI_1}{\text{cap rate}}\) and \(\text{cap rate} \approx r - g\): Gordon growth with NOI instead of dividends. A REIT's NAV sums the properties at market cap rates, less debt.
>
> **Sanity check.** A 5% cap rate on NOI of 1 million means a value of 20 million. Raise the cap rate to 6% and value falls to 16.7 million.
>
> **Exam trap.** FFO adds depreciation back to net income; AFFO then subtracts recurring capital spending. AFFO is the better measure of cash available to pay out.

| Formula | What it says |
|---|---|
| \(V = \dfrac{NOI_1}{\text{cap rate}}\) | direct capitalisation |
| \(\text{cap rate} \approx r - g\) | |
| \(V = \sum_t \dfrac{NOI_t}{(1 + r)^t} + \dfrac{NOI_{N+1}/\text{terminal cap rate}}{(1 + r)^N}\) | DCF valuation |
| \(LTV = \dfrac{\text{loan}}{\text{value}};\quad DSCR = \dfrac{NOI}{\text{debt service}}\) | |
| \(\text{Equity dividend rate} = \dfrac{\text{first-year cash flow}}{\text{equity}}\) | cash-on-cash return |
| \(NAVPS = \dfrac{\text{market value of assets} - \text{liabilities}}{\text{shares}}\) | REIT net asset value |
| \(FFO = NI + \text{depreciation} - \text{gains on sales} + \text{losses}\) | |
| \(AFFO = FFO - \text{recurring capex (and straight-line rent)}\) | |
| \(POST = \dfrac{\text{exit value}}{(1 + r)^N};\quad PRE = POST - I\) | venture capital method |
| \(f = \dfrac{I}{POST};\quad \text{new shares} = \text{shares}_{\text{pre}} \times \dfrac{f}{1 - f}\) | ownership and shares issued |
| \(F_0 = S_0\,e^{(r + c - y)T}\) | commodity forward; \(c\) = storage, \(y\) = convenience yield |
| \(R = \text{spot} + \text{roll} + \text{collateral return}\) | commodity futures return |

## Portfolio management

> **The one idea.** Returns come from exposure to a few common factors plus what is specific to each asset. Active management is the bet on differences from the benchmark, measured per unit of active risk.
>
> **Build the rest from it.** APT: \(E(R) = R_f + \sum \beta_k\lambda_k\). Active return splits into factor tilts and security selection. Fundamental law: \(IR \approx IC\sqrt{BR}\): skill times the square root of the number of independent bets.
>
> **Sanity check.** A manager with no skill (\(IC = 0\)) has an expected IR of zero however many bets they make.
>
> **Exam trap.** Breadth counts independent decisions, not trades. Ten correlated bets are closer to one.

| Formula | What it says |
|---|---|
| \(E(R) = R_f + \beta_1\lambda_1 + \cdots + \beta_k\lambda_k\) | arbitrage pricing theory |
| \(R_A = \sum (\beta_{p,k} - \beta_{b,k})F_k + \text{security selection}\) | active return attribution |
| \(\sigma_A^2 = \text{active factor risk} + \text{active specific risk}\) | |
| \(IR = \dfrac{R_A}{\sigma_A};\quad TE = \sigma(R_p - R_b)\) | information ratio and tracking error |
| \(E(R_A) = TC \times IC \times \sqrt{BR} \times \sigma_A\) | fundamental law of active management |
| \(IR \approx TC \times IC \times \sqrt{BR}\) | |
| \(\sigma_A^* = \dfrac{IR}{SR_B}\,\sigma_B\) | optimal active risk |
| \(SR_P^2 = SR_B^2 + IR^2\) | Sharpe ratio after adding optimal active risk |
| \(\text{VaR} = [z\sigma - E(R)] \times \text{value}\) | parametric value at risk |
| \(\text{VaR}_T \approx \text{VaR}_1\sqrt{T}\) | scaling, assuming independent returns |
| Expected shortfall = average loss beyond VaR | |
| \(E(R_{\text{bond}}) = r_{\text{real}} + \pi + \text{term} + \text{credit} + \text{liquidity premiums}\) | economics and markets |

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
