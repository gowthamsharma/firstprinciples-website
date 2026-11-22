---
title: BA II Plus calculator guide: every function, on a calculator you can press
slug: blog-ba-ii-plus-calculator-guide
order: 25
top: 1
layout: calc
summary: The complete guide to the BA II Plus for CFA candidates, built around a working replica of the calculator. Press the keys yourself or press Play and watch every keystroke: settings, clearing, memory, TVM, amortisation, bond pricing, NPV and IRR, interest conversion and statistics: the functions the CFA exams actually use, each with its formula and a picture.
figure: tvm_signs
caption: The rule behind every time-value answer: money you receive is positive, money you pay is negative. Change one sign and the answer flips or disappears.
tags: BA II Plus, BA II Plus guide, how to use BA II Plus, BA II Plus calculator, BA II Plus online, BA II Plus emulator, BA II Plus simulator, BA II Plus CFA, BA II Plus settings, BA II Plus TVM, BA II Plus NPV, BA II Plus IRR, BA II Plus cash flow, BA II Plus bond worksheet, BA II Plus amortization, BA II Plus statistics, BA II Plus memory, BA II Plus standard deviation, BA II Plus error 5, BA II Plus reset, BA II Plus Professional, financial calculator for CFA, CFA calculator tutorial, TI BA II Plus tutorial
group: Most searched: the guides candidates look for most
---
Most calculator guides tell you which keys to press. This one gives you the calculator. The calculator next to this text (or behind the **Calculator** tab at the bottom of your phone screen) is our own working replica of the BA II Plus: the same keys, the same second functions, the same worksheets and the same habits, down to the little ◁ that appears when a value is entered. Click its keys, type on your keyboard, or press **Play** on any of the grey boxes and watch each keystroke happen.

The guide follows the order you need things in an exam: set the calculator up, learn to clear it, then work through the calculations the CFA exams actually test. Every example shows the formula first, then a picture of the cash flows, then the keys. Each section explains **why** the calculator behaves as it does, because once you see the logic you stop making the mistakes that cost marks.

[[figure]]

## How the calculator thinks: three layers

Every key does up to two jobs, and many jobs open a **worksheet**:

- **The primary function** is printed on the key: digits, operations, the five time-value keys (N, I/Y, PV, PMT, FV), CPT and ENTER.
- **The second function** is printed above the key, in yellow here. Press **2ND** first, then the key. The small *2nd* indicator lights up so you know the next key will use its second job. Pressing 2ND again cancels it.
- **Worksheets** are small forms inside the calculator: cash flows, bonds, amortisation, statistics, depreciation, dates and more. You open one, move through its fields with **↑** and **↓**, type a number and press **ENTER** to store it, or press **CPT** to compute the field you are on. **2ND QUIT** always takes you back to the ordinary calculator.

Press **Key map** under the calculator to colour the keys by job. Blue keys are time value of money, green are cash flows, yellow-rimmed number keys open worksheets with 2ND, orange keys are memory and purple keys are arithmetic.

[[fig:lcd_anatomy|Read the display before you trust it: the label tells you which variable you are looking at, = means it holds this value, ◁ means you just entered it and * means the calculator computed it.]]

The display tells you more than the number. The indicators along the top say what the next key will do: **COMPUTE** means CPT will solve the field on screen, **ENTER** means the field accepts a typed value, **SET** means 2ND SET will switch a setting, and **↑↓** means there are more fields above or below. **BGN** stays lit whenever payments are set to the start of each period, which is the single most common hidden cause of wrong answers.

## The exam setup: four settings, two minutes

A new or reset calculator shows two decimals, works in **chain** order (it calculates strictly left to right) and may assume 12 payments a year. None of that suits the exam. Make these changes once; the calculator remembers them when it is switched off.

### 1. Show nine decimals (floating)

Two decimals hide information. If you compute a rate of 6.4878% and the screen shows 6.49, then reuse 6.49, every later step is slightly off. Setting **DEC = 9** makes the display float: it shows as many decimals as fit, up to ten digits in total. The calculator keeps 13 digits internally either way.

[[try:Set floating decimals|@fresh FORMAT 9 ENTER QUIT|You will see DEC = 9 while you are in the format worksheet, then 0. with no fixed decimals.]]

### 2. Switch from chain (Chn) to algebraic order (AOS)

In chain mode, 3 + 2 × 4 = 20, because the calculator adds first. In AOS mode it gives 11, the answer you learned at school, because multiplication comes first. The CFA exams are written with normal algebra in mind, so AOS saves you from typing brackets you would otherwise need. The setting sits four steps down the FORMAT worksheet.

[[try:The same keys in chain mode|@fresh 3 + 2 × 4 =|Chain mode gives 20.]]

[[try:Switch to AOS, then repeat|@fresh FORMAT ↓ ↓ ↓ ↓ SET QUIT 3 + 2 × 4 =|After switching to AOS, the same keys give 11.]]

### 3. One payment per year (P/Y = 1)

P/Y is the number of payments per year. When P/Y is 12, the calculator silently divides whatever you type into I/Y by 12. That is convenient for a mortgage and dangerous for everything else. With **P/Y = 1**, what you type is what you get: for monthly problems you divide the annual rate by 12 and multiply the years by 12 yourself, so you always see the per-period numbers. Setting P/Y also sets C/Y (compounding periods per year) to the same value.

[[try:Set one payment per year|@fresh P/Y 1 ENTER QUIT]]

### 4. Check END mode

The BGN worksheet shows **END** when payments happen at the end of each period (most loans, bonds and savings plans) and **BGN** for the beginning (leases, rent, insurance premiums, annuities due). It should normally read END. If the screen shows BGN, press 2ND SET to switch back.

[[try:Look at the payment timing|@exam BGN|The screen shows END. The BGN indicator in the top right is off.]]

### Reset: the clean slate

**2ND RESET ENTER** restores the factory state: two decimals, chain mode, P/Y = 12 on older units, and all worksheets and memories cleared. Reset when the calculator behaves strangely and you cannot see why, then redo the four settings. In this replica, the **Exam settings** button under the calculator does the reset and all four settings in one go.

[[try:Reset the calculator|@exam RESET ENTER|RST and 0 confirm the reset. The decimals and the order of operations are back to factory values, so redo your settings.]]

## Clearing: five different "clears" and what each one removes

Most calculator errors in exams come from **leftover values**, not wrong formulas. The calculator remembers what you typed into worksheets until you clear them, even after it switches itself off (it powers down after about five minutes without a key press).

| Keys | What it clears | When to use it |
|---|---|---|
| → | the last digit you typed | fixing a typo mid-number |
| CE/C | the number being typed; press again to clear the whole calculation | a wrong entry, or an error message |
| 2ND QUIT | leaves any worksheet; clears pending arithmetic | going back to normal calculations |
| 2ND CLR TVM | N, I/Y, PV, PMT and FV (not P/Y or BGN) | **before every time-value question** |
| 2ND CLR WORK | the worksheet you are in | before a new cash-flow, statistics or bond problem |

[[try:Fix a typo with the arrow key|@exam 3 × 1234.86 → → 56 =|You meant 1,234.56: delete two digits, type 56, and 3 × 1,234.56 = 3,703.68.]]

[[try:Clear only the last entry|@exam 2 × 3 CE/C 4 =|CE/C threw away the 3 but kept "2 ×", so the answer is 8.]]

[[try:Clear the time-value registers|@exam 5 N CLR_TVM RCL N|After 2ND CLR TVM, recalling N shows 0.]]

## Which functions the CFA exams actually need

The BA II Plus has more than a dozen worksheets, and most of them never appear in a CFA question. This guide keeps only what the exams use: **time value of money, amortisation, bond pricing, NPV and IRR, interest conversion, memory, and a little statistics and probability**. Each example below shows the formula first, then a picture of the cash flows, then the keys. Press **Play** and watch each key light up on the calculator.

What we left out, and why:

- **Regression, correlation and beta (the LIN worksheet).** Level I does teach simple linear regression, but questions give you the regression output or the summary figures, not twenty pairs of raw data to type in. If you do get a handful of numbers, the formula is quicker than the worksheet.
- **The BOND worksheet.** It works from calendar dates. CFA questions give you periods and fractions of a period instead, and the TVM keys plus one multiplication handle those (see *Bonds between coupon dates* below).
- **Depreciation, breakeven, profit margin, dates and the K constant.** Depreciation in financial reporting is simple arithmetic, and the rest are not tested.

## Everyday maths the exams use

### Powers and roots: the geometric mean return

Compounding is raising a number to a power, and **yˣ** does it. A root is a power too: the cube root is the power 1/3, so you type 3 and press **1/x** before =. The geometric mean return turns several years of different returns into the one constant rate that ends in the same place.

[[try:Geometric mean of +10%, −5% and +20%|@exam 1.1 × 0.95 × 1.2 = Y^X 3 1/X - 1 =|0.0784: a constant 7.84% a year gives the same result as the three actual years.|f=R<sub>G</sub> = ((1 + R<sub>1</sub>)(1 + R<sub>2</sub>)(1 + R<sub>3</sub>))<sup>1/3</sup> − 1;;= (1.10 × 0.95 × 1.20)<sup>1/3</sup> − 1|v=geo]]

### Continuous compounding: eˣ and LN

**eˣ** (2ND LN) gives the growth factor under continuous compounding. **LN** goes the other way: it turns a price change into a continuously compounded return.

[[try:1 grows continuously at 5% for three years|@exam 0.05 × 3 = e^x|1.161834243.|f=Growth factor = e<sup>r × T</sup> = e<sup>0.05 × 3</sup>|v=cont]]

[[try:Continuously compounded return when a price goes from 100 to 120|@exam 120 / 100 = LN|0.182321557, a continuous return of 18.23% (the simple return is 20%).|f=r<sub>cc</sub> = ln({P<sub>1</sub>}/{P<sub>0</sub>}) = ln({120}/{100})|v=lnret]]

### Counting: combinations

**nCr** (2ND +) counts the ways to choose r items from n when order does not matter. Level I probability uses it, for example to count portfolios or outcomes.

[[try:Ways to choose 3 stocks from 10|@exam 10 nCr 3 =|120.|f=<sub>n</sub>C<sub>r</sub> = {n!}/{(n − r)! × r!} = {10!}/{7! × 3!}|v=ncr]]

## Store a result, use it later: the ten memories

Long questions build an answer out of pieces. Writing each piece on paper wastes time and invites rounding errors. The calculator has ten memories, **M0 to M9**, so you can keep every piece at full precision:

- **STO 1** stores whatever is on screen in M1. **RCL 1** brings it back, and you can use it in the middle of a calculation.
- **STO + 1** adds the screen to what M1 already holds (STO −, STO × and STO ÷ work the same way).
- Use a different number for each piece, and note on your scrap paper which piece went where.
- **2ND MEM** (2ND 0) shows all ten memories as a list; 2ND CLR WORK inside it clears them.
- **2ND ANS** recalls the last answer, which is handy for one quick reuse.

[[try:Add three present values into one memory|@exam 100 / 1.05 = STO 1 200 / 1.05 Y^X 2 = STO + 1 300 / 1.05 Y^X 3 = STO + 1 RCL 1|535.7952705. STO + 1 kept a running total, so nothing was written down.|f=PV = {100}/{1.05} + {200}/{1.05<sup>2</sup>} + {300}/{1.05<sup>3</sup>}|v=sum3|m=M1: running total of the three present values]]

### A two-stage dividend model, one piece per memory

A stock will pay dividends of 2.00, 2.40 and 2.88 over the next three years. After that, dividends grow at 4% a year forever. The required return is 10%. The value today is the present value of the three dividends plus the present value of the price at the end of year 3. Each piece goes in its own memory, and the last step adds them up.

[[try:Value the stock with four memories|@exam 2 / 1.1 = STO 1 2.4 / 1.1 Y^X 2 = STO 2 2.88 × 1.04 / 0.06 = STO 3 + 2.88 = / 1.1 Y^X 3 = STO 4 RCL 1 + RCL 2 + RCL 4 =|V0 = 43.47107438.|f=P<sub>3</sub> = {D<sub>3</sub> × (1 + g)}/{r − g} = {2.88 × 1.04}/{0.10 − 0.04} = 49.92;;V<sub>0</sub> = {D<sub>1</sub>}/{1.1} + {D<sub>2</sub>}/{1.1<sup>2</sup>} + {D<sub>3</sub> + P<sub>3</sub>}/{1.1<sup>3</sup>}|v=ddm|m=M1: 2.00 ÷ 1.1 = 1.818;;M2: 2.40 ÷ 1.1² = 1.983;;M3: the year-3 price P3 = 49.92;;M4: (2.88 + 49.92) ÷ 1.1³ = 39.669]]

### Effective duration: three prices, three memories

Effective duration measures how much a bond's price moves when yields move. You price the bond at its current yield and at a yield a little lower and a little higher, then combine the three prices. Take a 10-year annual-pay bond with a 5% coupon, yielding 6%, and move the yield by 0.5% each way. The TVM keys keep N, PMT and FV, so you only change I/Y between prices.

[[try:Price three times, store each price, then combine|@exam 10 N 6 I/Y 5 PMT 100 FV CPT PV +/- STO 0 5.5 I/Y CPT PV +/- STO 1 6.5 I/Y CPT PV +/- STO 2 RCL 1 - RCL 2 = / ( 2 × RCL 0 × 0.005 ) =|Effective duration = 7.57: a 1% rise in yield cuts the price by about 7.6%.|f=ED = {PV<sub>−</sub> − PV<sub>+</sub>}/{2 × PV<sub>0</sub> × Δy} = {96.23 − 89.22}/{2 × 92.64 × 0.005}|v=dur|m=M0: price at 6% (PV0) = 92.64;;M1: price at 5.5% (PV−) = 96.23;;M2: price at 6.5% (PV+) = 89.22]]

## Time value of money: the five keys

Every time-value question has five numbers: **N** (number of periods), **I/Y** (interest rate per period, as a percentage), **PV** (present value), **PMT** (the level payment each period) and **FV** (future value). Give the calculator any four and it finds the fifth. To store a value, type it and press its key. To solve, press **CPT** and then the key you want.

The only real rule is the one in the diagram at the top: **cash you receive is positive, cash you pay is negative**. The calculator solves an equation that says all the cash flows, valued at the same moment, add up to zero. If every value has the same sign, no rate can balance them, and the calculator shows Error 5.

### Future value of a lump sum

You invest 1,000 today at 6% a year for five years. You pay the 1,000, so PV is negative. There are no payments in between, so PMT is 0.

[[try:Future value of 1,000 at 6% for 5 years|@exam 5 N 6 I/Y 1000 +/- PV 0 PMT CPT FV|FV = 1,338.225578. The answer is positive because you receive it.|f=FV = PV × (1 + r)<sup>N</sup> = 1,000 × 1.06<sup>5</sup>|v=fv]]

### Present value of a future amount

What is 5,000 received in ten years worth today at 7%? Store FV as positive (you receive it) and solve PV. The answer is negative: it is what you would pay today.

[[try:Present value of 5,000 in 10 years at 7%|@exam 10 N 7 I/Y 0 PMT 5000 FV CPT PV|PV = −2,541.746461.|f=PV = {FV}/{(1 + r)<sup>N</sup>} = {5,000}/{1.07<sup>10</sup>}|v=pv]]

### A monthly loan payment

A 300,000 mortgage for 30 years at 5.5% a year, paid monthly. Because P/Y = 1, you work in months yourself: N = 30 × 12 = 360 and I/Y = 5.5 ÷ 12. You can type the division straight into the key, and the calculator finishes the sum when you press I/Y.

[[try:Monthly payment on a 300,000 mortgage|@exam 360 N 5.5 / 12 = I/Y 300000 PV 0 FV CPT PMT|PMT = −1,703.367004 a month.|f=PMT = PV × {r}/{1 − (1 + r)<sup>−N</sup>};;r = 5.5% ÷ 12 = 0.4583% a month, N = 360|v=pmt]]

### Solving for the rate

An investment of 8,000 grows to 15,000 in ten years. What annual return is that? The calculator finds the rate that makes −8,000 today worth +15,000 later.

[[try:Find the annual return|@exam 10 N 8000 +/- PV 0 PMT 15000 FV CPT I/Y|I/Y = 6.487866803, so about 6.49% a year.|f=8,000 × (1 + r)<sup>10</sup> = 15,000;;r = ({15,000}/{8,000})<sup>1/10</sup> − 1|v=rate]]

### Solving for the number of periods

How long does it take to double money at 7%? The rule of 72 says about ten years; the calculator says exactly.

[[try:Years to double at 7%|@exam 7 I/Y 1000 +/- PV 0 PMT 2000 FV CPT N|N = 10.24476835 years.|f=1,000 × 1.07<sup>N</sup> = 2,000;;N = {ln 2}/{ln 1.07}|v=nper]]

### Annuity due: payments at the start (BGN)

Rent, leases and insurance premiums are paid at the **beginning** of each period. Switching to BGN moves every payment one period earlier, so each one is discounted one period less and the present value rises by exactly (1 + r).

[[try:20 payments of 10,000 at 5%, end of each year|@exam 20 N 5 I/Y 10000 +/- PMT 0 FV CPT PV|PV = 124,622.1034.|f=PV = PMT × {1 − (1 + r)<sup>−N</sup>}/{r} = 10,000 × {1 − 1.05<sup>−20</sup>}/{0.05}|v=annuity_end]]

[[try:The same payments at the start of each year|@exam BGN SET QUIT 20 N 5 I/Y 10000 +/- PMT 0 FV CPT PV|PV = 130,853.2086, which is 124,622.10 × 1.05. Notice the BGN indicator on the display.|f=PV<sub>BGN</sub> = PV<sub>END</sub> × (1 + r) = 124,622.10 × 1.05|v=annuity_bgn]]

### A two-stage retirement problem without retyping a number

Retirement questions chain two calculations: how much you need on retirement day, then how much to save each year to get there. The first answer is still on screen, so you flip its sign and store it straight into FV.

You want 40,000 a year for 25 years, paid at the start of each year, at 5%. You will save at the end of each year for 30 years at 7%.

[[try:Stage 1: the amount needed on retirement day|@exam BGN SET QUIT 25 N 5 I/Y 40000 PMT 0 FV CPT PV|PV = −591,945.6718: you need about 591,946 in the account.|f=PV = 40,000 × {1 − 1.05<sup>−25</sup>}/{0.05} × 1.05|v=retire]]

[[try:Stage 2: the yearly saving that builds it|@exam BGN SET QUIT 25 N 5 I/Y 40000 PMT 0 FV CPT PV +/- FV BGN SET QUIT 30 N 7 I/Y 0 PV CPT PMT|PMT = −6,266.575738 a year. The keys +/- FV moved stage 1's answer into stage 2, and BGN was switched back to END.|f=PMT = FV × {r}/{(1 + r)<sup>N</sup> − 1} = 591,946 × {0.07}/{1.07<sup>30</sup> − 1}|v=retire]]

### Perpetuities

A perpetuity never ends, so you do not need the TVM keys: its value is the payment divided by the rate. A perpetuity paying 50 a year at 4% is worth 50 ÷ 0.04 = 1,250. If the first payment comes immediately, add one payment: 1,300.

## Amortisation: interest and principal, period by period

Every level loan payment is part interest and part repayment. Early on the balance is large, so most of the payment is interest. The **AMORT** worksheet (2ND PV) splits the payments for any range you choose. Set up the loan in the TVM keys first, then open AMORT: **P1** and **P2** are the first and last payment of the range, **BAL** is the balance after P2, **PRN** is the principal repaid and **INT** the interest paid in the range.

[[try:Year 1 of the mortgage: balance left|@exam 360 N 5.5 / 12 = I/Y 300000 PV 0 FV CPT PMT AMORT 1 ENTER ↓ 12 ENTER ↓|BAL = 295,958.7316 after the first 12 payments.|f=Interest this month = balance × r;;Principal this month = PMT − interest|v=amort]]

[[try:Year 1: interest paid|@exam 360 N 5.5 / 12 = I/Y 300000 PV 0 FV CPT PMT AMORT 1 ENTER ↓ 12 ENTER ↓ ↓ ↓|INT = −16,399.13566, while the principal repaid (PRN, one step up) is only −4,041.27.|f=Interest in year 1 = 12 × PMT − principal repaid;;= 12 × 1,703.37 − (300,000 − 295,958.73)|v=amort]]

## Bonds: price, yield, and dates between coupons

### Price on a coupon date

A bond is an annuity (the coupons) plus a lump sum (the face value). Take a 5-year bond with a 6% coupon paid twice a year, priced to yield 8%. Work in half-years: N = 10, I/Y = 4, PMT = 3 (half of 6 per 100 of face value) and FV = 100.

[[try:Price a 5-year 6% bond at an 8% yield|@exam 10 N 4 I/Y 3 PMT 100 FV CPT PV|PV = −91.88910422: you pay about 91.89 per 100 of face value.|f=Price = 3 × {1 − 1.04<sup>−10</sup>}/{0.04} + {100}/{1.04<sup>10</sup>}|v=bond]]

### Yield to maturity

Going the other way, if the price is 95, solve I/Y and double it to get the annual yield, because I/Y is per half-year here.

[[try:Yield to maturity from a price of 95|@exam 10 N 95 +/- PV 3 PMT 100 FV CPT I/Y × 2 =|7.208747764: a yield of about 7.21% a year.|f=95 = 3 × {1 − (1 + y)<sup>−10</sup>}/{y} + {100}/{(1 + y)<sup>10</sup>};;YTM = 2 × y|v=ytm]]

### Bonds between coupon dates: full price, accrued interest, flat price

Trades usually settle between coupon dates. The CFA method has three steps: price the bond on the last coupon date, grow that price forward for the fraction of the period that has passed (t/T) to get the **full price**, then subtract **accrued interest** (the same fraction of one coupon) to get the **flat price** that is quoted. Same bond, yield 8%, settled 60 days into a 180-day coupon period. Two memories keep both prices.

[[try:Full price and flat price, 60 days after a coupon|@exam 10 N 4 I/Y 3 PMT 100 FV CPT PV +/- STO 1 × 1.04 Y^X ( 60 / 180 ) = STO 2 - 3 × 60 / 180 =|Flat price = 92.09831005. The full price, 93.09831005, is in M2.|f=Full price = PV × (1 + r)<sup>t/T</sup> = 91.889 × 1.04<sup>60/180</sup>;;Accrued interest = {t}/{T} × coupon = {60}/{180} × 3 = 1.00;;Flat price = full price − accrued interest|v=accrued|m=M1: price on the last coupon date = 91.889;;M2: full price = 93.098]]

## Cash flows: NPV and IRR for uneven flows

The TVM keys need level payments. When cash flows differ from year to year, use the **CF** worksheet. **CFo** is the cash flow today. **C01, C02, ...** are the later cash flows, and each has a frequency **F01, F02, ...**: how many times in a row that amount repeats.

Take a project that costs 50,000 today, returns 15,000 in year 1, 20,000 in each of years 2 to 4, and 25,000 in year 5. Open CF and clear it with 2ND CLR WORK first, or old flows from a previous question will still be there.

[[try:Enter the flows and compute NPV at 10%|@exam CF CLR_WORK 50000 +/- ENTER ↓ 15000 ENTER ↓ ↓ 20000 ENTER ↓ 3 ENTER ↓ 25000 ENTER NPV 10 ENTER ↓ CPT|NPV = 24,374.88746: positive, so the project earns more than 10%.|f=NPV = −50,000 + {15,000}/{1.1} + {20,000}/{1.1<sup>2</sup>} + {20,000}/{1.1<sup>3</sup>} + {20,000}/{1.1<sup>4</sup>} + {25,000}/{1.1<sup>5</sup>}|v=npv]]

[[try:Compute IRR for the same flows|@exam CF CLR_WORK 50000 +/- ENTER ↓ 15000 ENTER ↓ ↓ 20000 ENTER ↓ 3 ENTER ↓ 25000 ENTER IRR CPT|IRR = 26.28182395%: the discount rate at which NPV is exactly zero.|f=0 = −50,000 + {15,000}/{1 + IRR} + … + {25,000}/{(1 + IRR)<sup>5</sup>}|v=npv]]

### Money-weighted return is an IRR

The money-weighted return in the Level I portfolio readings is the IRR of the investor's own cash flows. You buy one share at 100. A year later it pays a dividend of 2 and you buy a second share at 110, so your net flow is −108. At the end of year 2 both shares pay 2 and you sell them at 120 each: +244.

[[try:Money-weighted return with the CF worksheet|@exam CF CLR_WORK 100 +/- ENTER ↓ 108 +/- ENTER ↓ ↓ 244 ENTER IRR CPT|IRR = 11.27552753: a money-weighted return of about 11.28% a year.|f=0 = −100 + {−108}/{1 + r} + {244}/{(1 + r)<sup>2</sup>}|v=mwrr]]

Two habits make the CF worksheet safe. **Check the count:** scroll down after entering, and the first C after your last flow should show 0. **Edit in place:** on any C or F field, 2ND DEL removes that flow and 2ND INS inserts one in front of it.

## Interest rate conversion (ICONV)

A rate of 12% "compounded monthly" is really more than 12% a year. The **ICONV** worksheet (2ND 2) converts a nominal annual rate (**NOM**) into the effective annual rate (**EFF**) for C/Y compounding periods a year, and back.

[[try:Effective rate of 12% compounded monthly|@exam ICONV 12 ENTER ↓ ↓ 12 ENTER ↑ CPT|EFF = 12.68250301.|f=EAR = (1 + {0.12}/{12})<sup>12</sup> − 1|v=ear]]

[[try:The monthly-compounded rate that gives 10% a year|@exam ICONV ↓ 10 ENTER ↓ 12 ENTER ↑ ↑ CPT|NOM = 9.568968515: 9.57% compounded monthly is the same as 10% a year.|f=NOM = 12 × ((1 + 0.10)<sup>1/12</sup> − 1)|v=nom]]

## Statistics: mean and standard deviation

Statistics live in two worksheets: **DATA** (2ND 7), where you type the numbers, and **STAT** (2ND 8), where you read the results. Clear DATA with 2ND CLR WORK before each new data set.

### Mean and sample standard deviation of returns

Enter each value as an X and leave each Y at 1. In STAT, press 2ND SET until **1-V** appears, then scroll: **n**, **x̄** (mean), **Sx** (sample standard deviation, dividing by n − 1) and **σx** (population, dividing by n).

[[try:Five annual returns: 12, −4, 9, 15, 3. Find the mean|@exam DATA 12 ENTER ↓ ↓ 4 +/- ENTER ↓ ↓ 9 ENTER ↓ ↓ 15 ENTER ↓ ↓ 3 ENTER STAT SET SET SET SET ↓ ↓|x̄ = 7.|f=x̄ = {12 + (−4) + 9 + 15 + 3}/{5}|v=mean]]

[[try:And the sample standard deviation|@exam DATA 12 ENTER ↓ ↓ 4 +/- ENTER ↓ ↓ 9 ENTER ↓ ↓ 15 ENTER ↓ ↓ 3 ENTER STAT SET SET SET SET ↓ ↓ ↓|Sx = 7.582875444.|f=s = √ {Σ(x − x̄)<sup>2</sup>}/{n − 1} = √ {230}/{4}|v=sd]]

### Expected return and risk from probabilities

Because Y is a frequency, you can type **probabilities × 100** into Y and the calculator weights each outcome. A stock returns 20% with probability 25%, 8% with probability 50% and −10% with probability 25%. Then x̄ is the expected return and **σx** (not Sx) is the standard deviation, because the probabilities describe every possible outcome.

[[try:Expected return from three scenarios|@exam DATA 20 ENTER ↓ 25 ENTER ↓ 8 ENTER ↓ 50 ENTER ↓ 10 +/- ENTER ↓ 25 ENTER STAT SET SET SET SET ↓ ↓|x̄ = 6.5%.|f=E(R) = 0.25 × 20 + 0.50 × 8 + 0.25 × (−10)|v=er]]

[[try:Standard deviation of those scenarios|@exam DATA 20 ENTER ↓ 25 ENTER ↓ 8 ENTER ↓ 50 ENTER ↓ 10 +/- ENTER ↓ 25 ENTER STAT SET SET SET SET ↓ ↓ ↓ ↓|σx = 10.71214264%.|f=σ = √ Σ p<sub>i</sub> × (R<sub>i</sub> − E(R))<sup>2</sup>;;= √ (0.25 × 13.5<sup>2</sup> + 0.5 × 1.5<sup>2</sup> + 0.25 × 16.5<sup>2</sup>)|v=sdp]]

## Error messages and what they mean

| Display | Meaning | Usual fix |
|---|---|---|
| Error 1 | Overflow or division by zero | check for a zero rate or zero count |
| Error 2 | Invalid input: root or log of a negative, x! of a non-integer | check the sign of the number |
| Error 3 | More than 8 pending operations or 15 open brackets | press = sooner |
| Error 4 | Value out of range (P/Y = 0, frequency above 9,999, decimals above 9) | re-enter the setting |
| Error 5 | No solution: usually every cash flow has the same sign | make outflows negative |
| Error 7 | The rate search did not converge | check the inputs; try a simpler problem |

Press CE/C to clear any error.

[[try:See Error 5 for yourself|@exam 5 N 8 I/Y 1000 PV 0 PMT 1500 FV CPT I/Y|Error 5: you "receive" 1,000 now and 1,500 later, so no interest rate can balance it. Make PV −1,000 and it works.|f=1,000 + {1,500}/{(1 + r)<sup>5</sup>} = 0 has no solution|v=err5]]

## When the answer is wrong but there is no error

Run this checklist before you assume you misunderstood the question:

1. **BGN lit?** Payments are being treated as at the start of each period.
2. **Leftover values?** A PMT or FV from the last question is still stored. Clear TVM every time.
3. **P/Y not 1?** Your I/Y is being divided by 12 behind your back.
4. **Chain mode?** 2 + 3 × 4 is giving 20 instead of 14.
5. **Rate per year or per period?** For semi-annual bonds and monthly loans, N and I/Y must use the same period.
6. **Too few decimals?** A rounded intermediate result was reused.
7. **Signs?** A positive PMT where you pay out will add to the value instead of offsetting it.

## Speed habits for exam day

- **Never retype an answer.** It is already on screen: store it in a TVM key, in memory, or use 2ND ANS.
- **Estimate first.** Decide roughly what the answer should be, then let the calculator confirm it. If 1,000 at 6% for five years gives 13,382, a decimal slipped.
- **Use the keystroke patterns you practise.** The same order every time (N, I/Y, PV, PMT, FV, then CPT) makes mistakes visible.
- **Practise on the calculator you will use.** Speed comes from your fingers knowing where 2ND and CPT are.
- **Bring a spare.** A second approved calculator or a fresh battery costs little; a dead calculator costs the exam.

## BA II Plus or BA II Plus Professional?

Both are permitted in the CFA exams, along with the HP 12C family. Everything on this page works on both models. The Professional adds a few extras to the worksheets: net future value and payback periods in the cash flow worksheet, and modified duration in the bond worksheet. It also has a sturdier case. The standard model is lighter and cheaper, and the extras are rarely needed because you can get them in one more step. Both use a CR2032 coin battery; replacing it clears your settings, so redo the setup afterwards.

## Questions people ask

### Is there an online BA II Plus calculator I can practise with?

Yes, this page. The calculator here is our own replica of the BA II Plus key layout and logic, built for learning. It runs in your browser on desktop and mobile, with no download. For the exam itself you need a physical approved calculator.

### What are the best BA II Plus settings for the CFA exam?

Floating decimals (2ND FORMAT 9 ENTER), AOS order of operations (2ND FORMAT, scroll to Chn, 2ND SET), one payment per year (2ND P/Y 1 ENTER) and END mode. Clear TVM before every time-value question.

### How do I calculate NPV and IRR on the BA II Plus?

Press CF, clear with 2ND CLR WORK, enter CFo and each later flow with its frequency, then press NPV, enter the rate as I, scroll down and press CPT. For IRR press IRR and CPT.

### Why does my BA II Plus show Error 5?

There is no solution to the problem as entered, almost always because all the cash flows have the same sign. Enter money you pay as negative (+/− after the number) and money you receive as positive.

### Do I need the regression worksheet for the CFA exam?

No. Level I covers simple linear regression, but the questions give you regression output or summary figures to interpret, not raw data to type in. Practise TVM, cash flows, memory and the 1-V statistics instead.

### How do I calculate standard deviation on the BA II Plus?

Enter the values in 2ND DATA (X only, Y = 1), open 2ND STAT, choose 1-V with 2ND SET and scroll to Sx for a sample or σx for a population.

### How do I reset the BA II Plus?

Press 2ND RESET (the +|− key) and then ENTER. All settings return to factory values, so redo the exam setup afterwards. For a calculator that will not respond, the hard-reset hole on the back does the same.

## Sources

- [Texas Instruments: BA II PLUS guidebook (PDF)](https://education.ti.com/-/media/5DC3E70F3C8040E499D704B583646E1D)
- [CFA Institute: calculator policy](https://www.cfainstitute.org/programs/cfa-program/policies)

BA II PLUS is a trademark of Texas Instruments. The calculator on this page is an independent replica written from scratch for teaching; it does not use Texas Instruments software, and Texas Instruments is not connected with First Principles.
