---
title: CFA Level III formula sheet: every formula you need, by topic
slug: blog-cfa-level-3-formula-sheet
order: 41
summary: The complete Level III formula sheet for the core curriculum and the three pathways: capital market expectations, asset allocation, derivatives and currency overlays, fixed income and equity portfolio management, after-tax wealth, trading costs, performance attribution and private markets, each with a one-line note.
figure: frontier
caption: Level III is about building and defending a portfolio; the formulas size the positions and measure the results.
tags: CFA level 3 formulas, CFA level 3 formula sheet, CFA level III formula sheet, CFA level 3 formulas list, CFA level 3 fixed income formulas, CFA level 3 derivatives formulas, CFA level 3 private wealth formulas, CFA level 3 performance attribution
group: Tools: formulas, calculator and self-study
updated: 2026-11-23
seo_title: CFA Level III formula sheet: core and pathway formulas (2026–2027)
meta: The complete CFA Level III formula sheet: capital market expectations, asset allocation, futures overlays, currency hedging, fixed income returns, after-tax wealth, attribution and private markets.
---
Level III has fewer formulas than Level II, but the exam uses them differently. In constructed-response questions you must **show the calculation and justify the result**: why a hedge ratio, why that asset allocation, what the attribution says about the manager. This sheet covers the core curriculum, which every candidate sits, plus the formulas specific to each pathway: Portfolio Management, Private Wealth and Private Markets.

Formula sheets for the other levels: [Level I](blog-cfa-level-1-formula-sheet.html) · [Level II](blog-cfa-level-2-formula-sheet.html). For the pathway choice itself, see [choosing your Level III pathway](blog-level-3-pathways.html).

[[figure]]

## How to learn from this sheet

Reading a list of formulas doesn't make them stick. Recalling them does. So this sheet is built to be worked, not just read:

1. **Start with the one idea.** Each topic opens with a short card: the single idea behind the topic, how the other formulas follow from it, a sanity check to catch a wrong answer, and the trap examiners set most often. If you understand the card, you can rebuild a formula you've forgotten.
2. **Test yourself.** Switch on *Quiz me* below. The formulas are hidden behind their meanings (or the other way round); try to write each one down, then reveal it and mark *Knew it* or *Not yet*.
3. **Come back to the gaps.** Your marks are saved in this browser. Tick *Only show the ones I'm still learning* and work just those, a few minutes a day, until every topic is complete.

[[studymode]]

## Capital market expectations

> **The one idea.** Long-run expected returns are built from parts you can forecast: income, growth and changes in valuation. Each model adds the same pieces in a different way.
>
> **Build the rest from it.** Grinold–Kroner: \(E(R_e) \approx \tfrac{D}{P} - \%\Delta S + i + g + \%\Delta\tfrac{P}{E}\). Singer–Terhaar blends a fully integrated premium \(\rho\sigma_i\tfrac{RP_{GM}}{\sigma_{GM}}\) with a fully segmented one (set \(\rho = 1\)).
>
> **Sanity check.** If valuations are stable (\(\%\Delta P/E = 0\)) and no shares are issued, the expected return is the dividend yield plus nominal earnings growth.
>
> **Exam trap.** In Singer–Terhaar, add the illiquidity premium after blending, not before.

| Formula | What it says |
|---|---|
| \(E(R_e) \approx \dfrac{D}{P} - \%\Delta S + i + g + \%\Delta\dfrac{P}{E}\) | Grinold–Kroner: income + nominal earnings growth + repricing |
| \(E(R_e) \approx \left(\dfrac{D}{P} - \%\Delta S\right) + (i + g) + \%\Delta\dfrac{P}{E}\) | the same in three parts; \(\%\Delta S\) = change in shares outstanding |
| \(RP_i = \rho_{i,GM}\,\sigma_i\,\dfrac{RP_{GM}}{\sigma_{GM}}\) | Singer–Terhaar, fully integrated |
| \(RP_i = \sigma_i\,\dfrac{RP_M}{\sigma_M}\) | Singer–Terhaar, fully segmented |
| \(RP_i = \varphi\,RP_i^{\text{int}} + (1 - \varphi)RP_i^{\text{seg}} + LP_i\) | blend by degree of integration \(\varphi\), plus a liquidity premium |
| \(i^* = r_{\text{neutral}} + \pi^e + 0.5(\pi^e - \pi^{\text{target}}) + 0.5(\hat{Y}^e - \hat{Y}^{\text{trend}})\) | Taylor rule |
| \(g_{\text{trend}} = g_{\text{labour force}} + g_{\text{labour productivity}}\) | trend real GDP growth |
| \(E(R_{\text{bond}}) \approx YTM\) | if held to maturity with no default |
| \(E(R) = R_f + ERP;\quad E(R_{\text{bond}}) = R_f + \text{term} + \text{credit} + \text{liquidity premiums}\) | building blocks |
| \(\dfrac{F}{S} = \dfrac{1 + i_p}{1 + i_b}\) | covered interest parity |

## Asset allocation

> **The one idea.** Allocation balances expected return against risk the investor dislikes. For pension and insurance funds, the risk that matters is relative to the liabilities.
>
> **Build the rest from it.** Utility: \(U = E(R) - 0.005\lambda\sigma^2\) with returns in percent. For a liability-driven investor, track the surplus: \(\text{Surplus} = A - PV(L)\), with return \(\tfrac{\Delta A - \Delta L}{A_0}\).
>
> **Sanity check.** A risk-neutral investor (\(\lambda = 0\)) simply picks the highest expected return.
>
> **Exam trap.** Use 0.005 only when returns are in percent; with decimals the factor is 0.5.

| Formula | What it says |
|---|---|
| \(U_m = E(R_m) - 0.005\,\lambda\,\sigma_m^2\) | mean–variance utility with returns in percent |
| \(\text{Surplus} = A - PV(L)\) | |
| \(R_{\text{surplus}} = \dfrac{\Delta A - \Delta L}{A_0}\) | surplus return |
| \(\text{Funded ratio} = \dfrac{A}{PV(L)}\) | |
| \(HC_0 = \sum_{t=1}^{N}\dfrac{p(s_t)\,w_{t-1}(1 + g_t)}{(1 + r_f + y)^t}\) | human capital: survival-weighted PV of earnings |
| \(\text{Financial capital} + \text{human capital} = \text{liabilities} + \text{net wealth}\) | economic balance sheet |
| \(R_{\text{required}} \approx (1 + \text{spending})(1 + \pi)(1 + \text{costs}) - 1\) | multiplicative |
| Rebalancing corridor = target \(\pm\) range; wider when costs are high or volatility is low | |
| \(MCTR_i = \beta_{i,P}\,\sigma_P;\quad ACTR_i = w_i\,\beta_{i,P}\,\sigma_P\) | marginal and absolute contribution to risk |
| \(\%CTR_i = w_i\,\beta_{i,P}\) | sums to 100% |
| \(w_i\,\text{Cov}(R_i, R_P) = \dfrac{1}{n}\sigma_P^2\) | risk parity: equal risk contributions |

## Derivatives and risk management

> **The one idea.** Futures let you change a portfolio's exposure without trading the assets. The number of contracts is the risk you want to add or remove, divided by the risk one contract carries.
>
> **Build the rest from it.** Equity: \(N_f = \tfrac{\beta_T - \beta_S}{\beta_f} \times \tfrac{S}{F}\). Bonds: \(N_f = \tfrac{BPV_T - BPV_P}{BPV_f}\), with \(BPV_f \approx \tfrac{BPV_{CTD}}{CF_{CTD}}\). Same shape each time: (target − current) ÷ per-contract exposure.
>
> **Sanity check.** If the target beta equals the current beta, \(N_f = 0\): no trade.
>
> **Exam trap.** A negative \(N_f\) means sell futures. Check the sign before you round.

| Formula | What it says |
|---|---|
| \(N_f = \dfrac{\beta_T - \beta_S}{\beta_f} \times \dfrac{S}{F}\) | equity futures to change beta; \(F\) = futures price \(\times\) multiplier |
| \(N_f = \dfrac{BPV_T - BPV_P}{BPV_f}\) | bond futures to change duration |
| \(BPV_f \approx \dfrac{BPV_{CTD}}{CF_{CTD}}\) | BPV of a bond future |
| \(BPV = \text{ModDur} \times MV \times 0.0001\) | basis point value |
| \(N_f = \dfrac{V(1 + r)^T}{F \times \text{multiplier}}\) | cash equitisation |
| \(Dur_{\text{receive-fixed swap}} \approx Dur_{\text{fixed}} - Dur_{\text{floating}}\) | swap duration |
| \(N_{\text{swap}} = \dfrac{BPV_T - BPV_P}{BPV_{\text{swap per unit}}}\) | swap notional to hit a target |
| Covered call: \(\max\text{ gain} = X - S_0 + c_0\); breakeven \(= S_0 - c_0\) | |
| Protective put: \(\max\text{ loss} = S_0 - X + p_0\); breakeven \(= S_0 + p_0\) | |
| Collar: buy put \(X_L\), sell call \(X_H\); outcomes between \(X_L\) and \(X_H\) less the net premium | |
| Bull call spread: \(\max\text{ gain} = X_H - X_L - \text{net premium}\) | |
| \(\text{Straddle breakevens} = X \pm (c_0 + p_0)\) | a bet on volatility, not direction |
| \(\text{Payoff} = N_{\text{var}}(\sigma^2_{\text{realised}} - K^2),\quad N_{\text{var}} = \dfrac{N_{\text{vega}}}{2K}\) | variance swap |
| \(N_{\text{options}} = -\dfrac{\text{portfolio delta}}{\text{option delta}}\) | delta hedge |
| \(h^* = \rho\,\dfrac{\sigma_S}{\sigma_F}\) | minimum-variance hedge ratio |
| \(\text{VaR} = [z\sigma - E(R)] \times \text{value}\) | \(z\) = 1.65 (5%), 2.33 (1%) |
| CVaR (expected shortfall) = average loss beyond VaR | |

## Currency management

> **The one idea.** A foreign asset earns two returns that multiply: the asset's local return and the currency's move. Hedging removes the second, at the cost of the interest-rate differential.
>
> **Build the rest from it.** \(R_{DC} = (1 + R_{FC})(1 + R_{FX}) - 1\). The variance adds the two risks and their covariance: \(\sigma^2(R_{DC}) \approx \sigma^2(R_{FC}) + \sigma^2(R_{FX}) + 2\rho\,\sigma_{FC}\sigma_{FX}\).
>
> **Sanity check.** If the currency doesn't move (\(R_{FX} = 0\)), the domestic return equals the foreign return.
>
> **Exam trap.** Hedging a currency that trades at a forward premium earns roll yield; one at a forward discount costs it.

| Formula | What it says |
|---|---|
| \(R_{DC} = (1 + R_{FC})(1 + R_{FX}) - 1\) | domestic-currency return |
| \(R_{DC} = \sum_i w_i\,(1 + R_{FC,i})(1 + R_{FX,i}) - 1\) | multi-currency portfolio |
| \(\sigma^2(R_{DC}) \approx \sigma^2(R_{FC}) + \sigma^2(R_{FX}) + 2\rho\,\sigma(R_{FC})\,\sigma(R_{FX})\) | currency adds risk unless negatively correlated |
| \(\sigma(R_{DC}) \approx \sigma(R_{FC})\) | if currency risk is fully hedged |
| \(\dfrac{F - S}{S} \approx i_p - i_b\) | forward premium or discount: the roll yield on a hedge |
| \(\text{Hedge ratio} = \dfrac{\text{hedged notional}}{\text{market value of foreign assets}}\) | rebalance as values change |
| Regress \(R_{DC}\) on \(R_{FX}\): slope = minimum-variance hedge ratio | |
| \(R_{\text{carry}} \approx i_{\text{high}} - i_{\text{low}} - \%\Delta S_{\text{high}}\) | carry trade |

## Fixed income portfolio management

> **The one idea.** A bond portfolio's return over a horizon has five sources: the yield you earn, rolling down the curve, yield changes, credit losses and currency. Add them and you have the forecast.
>
> **Build the rest from it.** \(E(R) \approx \text{yield income} + \text{rolldown} + E(\Delta P) - E(\text{credit losses}) \pm E(\text{currency})\), where \(E(\Delta P) \approx -\text{ModDur} \times \Delta y + \tfrac{1}{2}\text{Convexity}(\Delta y)^2\).
>
> **Sanity check.** With a flat, unchanging curve and no defaults, the return is simply the yield.
>
> **Exam trap.** Rolldown assumes the curve stays where it is. Forecast yield changes separately, or you count them twice.

| Formula | What it says |
|---|---|
| \(E(R) \approx \text{yield income} + \text{rolldown} + E(\Delta P_{\text{yields}}) - E(\text{credit losses}) \pm E(\text{currency})\) | the decomposition used throughout Level III |
| \(\text{Yield income} = \dfrac{\text{annual coupon}}{P_0}\) | plus reinvestment income |
| \(\text{Rolldown return} = \dfrac{P_{\text{rolled}} - P_0}{P_0}\) | stable curve |
| \(E(\Delta P) \approx -\text{ModDur}\,\Delta y + \tfrac{1}{2}\,\text{Convexity}\,(\Delta y)^2\) | price change from yield views |
| Single liability: MacDur = horizon; \(PV_A \ge PV_L\); minimise convexity (dispersion) | immunisation |
| Multiple liabilities: \(BPV_A = BPV_L\); convexity\(_A >\) convexity\(_L\); \(PV_A \ge PV_L\) | |
| \(\text{Cushion} = PV_A - PV_L\) at the immunisation rate | contingent immunisation |
| \(\text{Convexity} = \dfrac{\text{MacDur}^2 + \text{MacDur} + \text{dispersion}}{(1 + r)^2}\) | lower dispersion, lower structural risk |
| \(E(XS) \approx s_0 - (\text{EffSpreadDur} \times \Delta s) - (POD \times LGD)\) | expected excess spread return |
| \(R_P = r_I + \dfrac{V_B}{V_E}(r_I - r_B)\) | leveraged portfolio return |
| \(\sum \text{key rate durations} \approx \text{effective duration}\) | key rate duration: sensitivity to one point on the curve |
| Barbell gains when the curve flattens and from convexity; bullet when it steepens | |
| \(D_P = \sum_i w_i D_i\) | portfolio duration (market-value weights) |
| \(SD_P = \sum_i w_i\,SD_i\) | portfolio spread duration |

## Equity portfolio management

> **The one idea.** Active management is measured against the benchmark. Return above it is only worth something relative to the extra risk taken to get it.
>
> **Build the rest from it.** Active return \(R_A = R_P - R_B\), active risk \(\sigma_A = \sigma(R_P - R_B)\), and \(IR = \tfrac{R_A}{\sigma_A}\). Active share counts how different the holdings are: \(\tfrac{1}{2}\sum |w_{P,i} - w_{B,i}|\).
>
> **Sanity check.** An index fund has active share near 0 and tracking error near 0.
>
> **Exam trap.** High active share with low tracking error means many small, diversified bets. High tracking error with low active share means concentrated factor bets.

| Formula | What it says |
|---|---|
| \(R_A = R_P - R_B\) | active return |
| \(\sigma_A = \sigma(R_P - R_B)\) | active risk (tracking error) |
| \(IR = \dfrac{R_A}{\sigma_A}\) | information ratio |
| \(\text{Active share} = \tfrac{1}{2}\sum_i \lvert w_{P,i} - w_{B,i}\rvert\) | how different the holdings are |
| \(\sigma_A^2 = \text{active factor risk} + \text{active specific risk}\) | factor bets and stock-specific bets both add risk |
| \(\text{Net} = \text{long} - \text{short};\quad \text{gross} = \text{long} + \text{short}\) | long-short exposure |
| \(\beta_{130/30} \approx 1.3\,\beta_{\text{long}} - 0.3\,\beta_{\text{short}}\) | |

## Trading, performance evaluation and manager selection

> **The one idea.** Every trade costs something relative to a paper portfolio that traded instantly at the decision price. Implementation shortfall measures that gap and splits it into parts.
>
> **Build the rest from it.** \(IS = \text{delay} + \text{execution} + \text{opportunity cost} + \text{fees}\). Delay \(= Q_{\text{traded}}(P_{\text{arrival}} - P_{\text{decision}})\) for a buy. Performance attribution splits return into allocation and selection the same way.
>
> **Sanity check.** An order filled in full at the decision price with no fees has an implementation shortfall of zero.
>
> **Exam trap.** Opportunity cost applies only to the shares you didn't trade.

| Formula | What it says |
|---|---|
| \(IS = R_{\text{paper}} - R_{\text{actual}}\) | implementation shortfall |
| \(IS = \text{delay} + \text{execution} + \text{opportunity cost} + \text{fees}\) | its components |
| \(\text{Delay cost} = Q_{\text{traded}}(P_{\text{arrival}} - P_{\text{decision}})\) | for a buy |
| \(\text{Execution cost} = Q_{\text{traded}}(\bar{P}_{\text{exec}} - P_{\text{arrival}})\) | |
| \(\text{Opportunity cost} = Q_{\text{unfilled}}(P_{\text{close}} - P_{\text{decision}})\) | |
| \(\text{VWAP cost} = Q(\bar{P}_{\text{exec}} - VWAP)\) | |
| \(A_i = (w_{P,i} - w_{B,i})(R_{B,i} - R_B)\) | Brinson–Fachler allocation |
| \(S_i = w_{B,i}(R_{P,i} - R_{B,i})\) | selection |
| \(I_i = (w_{P,i} - w_{B,i})(R_{P,i} - R_{B,i})\) | interaction |
| \(R_A = \sum_i (A_i + S_i + I_i)\) | total active return |
| Fixed income: yield income + rolldown + duration + curve + spread + selection | fixed income attribution |
| \(\dfrac{R_P - R_f}{\sigma_P}\) | Sharpe ratio |
| \(\dfrac{R_P - R_f}{\beta_P}\) | Treynor ratio |
| \(\dfrac{R_P - MAR}{\sigma_{\text{downside}}}\) | Sortino ratio: penalises only returns below the minimum acceptable return |
| \(AR = \dfrac{\alpha_J}{\sigma_\varepsilon}\) | appraisal ratio |
| \(UC = \dfrac{R_P}{R_B}\Big\rvert_{R_B > 0};\quad DC = \dfrac{R_P}{R_B}\Big\rvert_{R_B < 0};\quad CR = \dfrac{UC}{DC}\) | upside, downside and capture ratio |
| Maximum drawdown = largest peak-to-trough fall | |

## Private wealth pathway

> **The one idea.** Taxes change returns depending on when they are paid: every year, at sale, or on withdrawal. The longer tax is deferred, the more the untaxed money compounds.
>
> **Build the rest from it.** Taxed every year: \(FV = [1 + r(1 - t_i)]^n\). Taxed once at the end: \(FV = (1 + r)^n(1 - t_{cg}) + t_{cg}B\). Tax-deferred account: \((1 + r)^n(1 - t_n)\). Tax-exempt: \((1 + r)^n\).
>
> **Sanity check.** Over one year, with a cost basis equal to today's value (\(B = 1\)), accrual and deferred taxation give the same result: \(1 + r(1 - t)\).
>
> **Exam trap.** In the deferred capital-gains formula, \(B\) is the cost basis as a fraction of current value, not a currency amount.

| Formula | What it says |
|---|---|
| \(FV = [1 + r(1 - t_i)]^n\) | accrual taxation: taxed every year |
| \(FV = (1 + r)^n(1 - t_{cg}) + t_{cg}B\) | deferred capital gains; \(B\) = cost basis as a share of value |
| \(FV = (1 + r)^n(1 - t_n)\) | tax-deferred account: taxed on withdrawal |
| \(FV = (1 + r)^n\) | tax-exempt account |
| \(FV = [(1 + r)(1 - t_w)]^n\) | wealth tax |
| \(t^* = p_it_i + p_dt_d + p_{cg}t_{cg}\) | blended tax rate by type of return |
| \(T^* = t_{cg}\,\dfrac{1 - p_i - p_d - p_{cg}}{1 - p_it_i - p_dt_d - p_{cg}t_{cg}}\) | effective capital gains rate |
| \(R_{AE} = \left(\dfrac{FV}{PV}\right)^{1/n} - 1\) | accrual equivalent return |
| \(T_{AE} = 1 - \dfrac{R_{AE}}{r}\) | accrual equivalent tax rate |
| \(\text{Tax saving} = t \times \text{loss realised}\) | tax-loss harvesting (current year) |
| \((1 + r)^n(1 - t)\) vs \([1 + r(1 - t)]^n\) | after-tax wealth: deferred vs taxable account |
| \(\text{Excess capital} = \text{assets} - \text{core capital}\) | core capital = PV of spending needs plus a reserve |
| \(PV = \sum_t \dfrac{p(\text{survival}_t)\times\text{spending}_t}{(1 + r)^t}\) | probability-weighted spending |

## Private markets pathway

> **The one idea.** Private fund performance is judged by multiples of money: what came back, what is still in the fund, and the two together. IRR adds the timing.
>
> **Build the rest from it.** \(DPI = \tfrac{\text{distributions}}{\text{paid-in}}\), \(RVPI = \tfrac{NAV}{\text{paid-in}}\), so \(TVPI = DPI + RVPI\). IRR solves \(\sum \tfrac{CF_t}{(1 + IRR)^t} = 0\).
>
> **Sanity check.** Early in a fund's life DPI is near zero and TVPI is mostly RVPI, which is an estimate.
>
> **Exam trap.** A high TVPI with a low DPI is still mostly unrealised value. Ask how much cash has actually come back.

| Formula | What it says |
|---|---|
| \(DPI = \dfrac{\text{cumulative distributions}}{\text{paid-in capital}}\) | cash returned |
| \(RVPI = \dfrac{NAV}{\text{paid-in capital}}\) | value still in the fund |
| \(TVPI = DPI + RVPI\) | total value multiple |
| Net IRR: IRR of the fund's net cash flows to limited partners | sensitive to timing and subscription lines |
| \(KS\text{-}PME = \dfrac{PV(\text{distributions} + NAV)}{PV(\text{contributions})}\), discounted at index returns | above 1: beat the public market |
| \(POST = \dfrac{\text{exit value}}{(1 + r)^n};\quad \text{ownership} = \dfrac{I}{POST}\) | venture capital method |
| \(\text{IRR}_{\text{equity}} = \left(\dfrac{\text{exit equity}}{\text{entry equity}}\right)^{1/n} - 1\), with exit equity \(=\) exit EV \(-\) net debt | leveraged buyout |
| Value creation = EBITDA growth + multiple expansion + debt paydown | |
| \(\text{Carry} = \text{carry rate} \times (\text{proceeds} - \text{contributed capital} - \text{preferred return})\), after catch-up | European waterfall |
| \(E(R_{\text{private debt}}) \approx \text{yield} - PD \times LGD - \text{fees}\) | |
| \(V = \dfrac{NOI}{\text{cap rate}};\quad R_L \approx R_U + \dfrac{D}{E}(R_U - r_D)\) | real estate value and levered return |

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
