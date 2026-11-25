# Lesson quizzes for the prerequisites course: slug -> [(question, [options], correct_index, explanation)]
Q = {
"prereq-financial-reporting-objective": [
 ("Who are financial statements mainly prepared for?", ["Tax authorities", "Investors and lenders deciding whether to provide capital", "The company's managers", "Regulators setting interest rates"], 1, "The framework's stated objective is to help existing and potential investors and lenders decide whether to provide resources to the company."),
 ("Which two qualities are the fundamental qualitative characteristics of useful information?", ["Timeliness and comparability", "Relevance and faithful representation", "Verifiability and understandability", "Prudence and consistency"], 1, "Relevance and faithful representation are fundamental; comparability, verifiability, timeliness and understandability enhance them."),
 ("An item is 'material' if:", ["It is larger than 5% of revenue", "Omitting or misstating it could change users' decisions", "Auditors have checked it", "It involves cash"], 1, "Materiality is judged by its effect on decisions, not by a fixed percentage."),
],
"prereq-three-statements": [
 ("Which statement shows a company's position at a single point in time?", ["Income statement", "Cash flow statement", "Balance sheet", "Statement of comprehensive income"], 2, "The balance sheet is a snapshot; the income and cash flow statements cover a period."),
 ("Net income for the year, minus dividends paid, flows into which balance sheet item?", ["Cash", "Retained earnings", "Share capital", "Accounts payable"], 1, "Profits kept in the business add to retained earnings, part of equity."),
 ("The change in cash on the balance sheet over a year should equal:", ["Net income", "The net change shown on the cash flow statement", "Operating cash flow only", "Revenue minus expenses"], 1, "Operating, investing and financing cash flows together explain the change in the cash balance."),
],
"prereq-accrual-accounting": [
 ("A company delivers services in December but is paid in January. When is revenue recorded?", ["January", "December", "Split between both", "When the invoice is sent"], 1, "Revenue is recorded when it is earned (December); the unpaid amount sits in accounts receivable."),
 ("A customer pays in advance for a service to be delivered next year. Today the company records:", ["Revenue", "A liability (unearned revenue)", "An expense", "Nothing until delivery"], 1, "Cash received before the service is delivered creates an obligation: unearned (deferred) revenue."),
 ("Wages earned by staff in the last week of the year but paid next year create:", ["An accrued expense (liability)", "A prepaid expense (asset)", "Unearned revenue", "No entry"], 0, "The expense belongs to this year, so it is recorded now with a liability for the unpaid amount."),
],
"prereq-revenue-recognition": [
 ("In the five-step model, what comes immediately after identifying the contract?", ["Determine the price", "Identify the separate performance obligations", "Recognise revenue", "Allocate the price"], 1, "Contract, then performance obligations, then transaction price, allocation, and recognition when each obligation is satisfied."),
 ("A phone is sold with two years of support for one price. How is revenue recognised?", ["All at the sale", "All over two years", "Price is allocated: the phone part at sale, the support part over two years", "Only when the support ends"], 2, "Each distinct promise gets its share of the price, recognised when that promise is delivered."),
 ("Revenue from a long construction contract delivered gradually is usually recognised:", ["Only at completion", "Over time, as the work progresses", "When cash is collected", "At contract signing"], 1, "When control passes to the customer over time, revenue is recognised as the obligation is satisfied."),
],
"prereq-doubtful-accounts-warranties": [
 ("Why does a company record bad debt expense before any customer has actually defaulted?", ["Tax rules require it", "To match the expected cost of credit sales to the period of those sales", "To reduce cash", "Auditors insist on round numbers"], 1, "The matching principle puts the estimated cost of uncollectable sales in the same period as the revenue."),
 ("The allowance for doubtful accounts appears as:", ["A liability", "A reduction of accounts receivable", "An addition to revenue", "Part of equity"], 1, "It is a contra-asset: receivables are shown net of the amount not expected to be collected."),
 ("A company sells products with a one-year warranty. When should the warranty cost be expensed?", ["When repairs happen", "In the period of the sale, as an estimate", "When the warranty expires", "Never; it is a cash item"], 1, "The expected warranty cost is estimated and expensed when the product is sold, with a provision (liability)."),
],
"prereq-depreciation-methods": [
 ("Compared with straight-line, an accelerated method in an asset's early years gives:", ["Higher depreciation and lower profit", "Lower depreciation and higher profit", "The same profit", "Higher cash flow from operations before tax effects"], 0, "Accelerated methods front-load the expense; total depreciation over the life is the same."),
 ("A machine costs 10,000, has a salvage value of 2,000 and a life of 4 years. Straight-line depreciation per year is:", ["2,500", "2,000", "3,000", "1,500"], 1, "(10,000 − 2,000) ÷ 4 = 2,000 a year."),
 ("Over the whole life of an asset, the choice of depreciation method changes:", ["Total depreciation", "Only the timing of depreciation", "The asset's cost", "Total cash spent"], 1, "The method decides when the cost is expensed, never how much in total."),
],
"prereq-non-recurring-items": [
 ("Why do analysts separate discontinued operations from continuing operations?", ["They are taxed differently", "Forecasts should be based on the business that will continue", "They are always losses", "Auditors require it"], 1, "Valuation depends on future earnings, so analysts focus on the repeatable core."),
 ("A large one-off restructuring charge should, in a forecast of next year's earnings, usually be:", ["Repeated every year", "Excluded or treated separately, if it is truly non-recurring", "Doubled", "Added to revenue"], 1, "Non-recurring items distort the trend; but check whether 'one-offs' keep recurring."),
 ("A gain from selling a factory is best described as:", ["Operating revenue", "A non-operating or non-recurring gain", "Other comprehensive income", "A financing cash flow"], 1, "It does not come from the company's ordinary trading activity and is unlikely to repeat."),
],
"prereq-common-size": [
 ("In a common-size income statement, every line is divided by:", ["Net income", "Revenue", "Total assets", "Equity"], 1, "Expressing lines as a percentage of revenue shows margins and cost structure."),
 ("Company A has revenue of 50m and gross profit of 20m; Company B has revenue of 900m and gross profit of 270m. Which has the higher gross margin?", ["A (40%)", "B (30%)", "They are equal", "Cannot tell"], 0, "20 ÷ 50 = 40% against 270 ÷ 900 = 30%: size no longer hides the comparison."),
 ("In a common-size balance sheet, items are usually shown as a percentage of:", ["Revenue", "Total assets", "Net income", "Market value"], 1, "Each asset, liability and equity line is divided by total assets."),
],
"prereq-comprehensive-income": [
 ("Total comprehensive income equals:", ["Net income only", "Net income + other comprehensive income", "Revenue − expenses", "Dividends + retained earnings"], 1, "It captures every change in equity that does not come from transactions with owners."),
 ("Which of these goes to other comprehensive income rather than profit?", ["Interest expense", "Some foreign currency translation gains on overseas subsidiaries", "Sales revenue", "Depreciation"], 1, "Translation adjustments are classic OCI items, along with certain revaluation and pension remeasurement gains."),
 ("Dividends paid to shareholders are:", ["Part of comprehensive income", "A transaction with owners, not part of comprehensive income", "An expense", "Part of OCI"], 1, "Comprehensive income excludes owner transactions such as dividends and share issues."),
],
"prereq-balance-sheet-classification": [
 ("A liability is classified as current if it must be settled:", ["Within five years", "Within one year (or the operating cycle if longer)", "Only if it bears interest", "Before the next dividend"], 1, "The current/non-current split is about timing and liquidity."),
 ("Current ratio = 3,000 current assets ÷ 1,500 current liabilities = ?", ["0.5", "1.5", "2.0", "4,500"], 2, "3,000 ÷ 1,500 = 2.0: two units of short-term assets for each unit of short-term obligations."),
 ("Which is normally a non-current asset?", ["Inventory", "Accounts receivable", "Property, plant and equipment", "Cash"], 2, "PP&E is used over many years; the others turn into cash within the operating cycle."),
],
"prereq-equity-components": [
 ("Equity is best defined as:", ["Cash in the bank", "Assets minus liabilities", "Share price × shares", "Retained earnings only"], 1, "It is the owners' residual claim after all liabilities."),
 ("A company buys back its own shares (treasury shares). Total equity:", ["Rises", "Falls", "Does not change", "Moves to liabilities"], 1, "Cash leaves the company and equity is reduced by the cost of the repurchased shares."),
 ("Retained earnings increase by:", ["Share issues", "Net income kept after dividends", "Borrowing", "Revaluation of land only"], 1, "Retained earnings accumulate profits not paid out."),
],
"prereq-cash-flow-classification": [
 ("Buying a new factory is classified as a cash flow from:", ["Operating activities", "Investing activities", "Financing activities", "None"], 1, "Purchases of long-term assets are investing outflows."),
 ("Under US GAAP, dividends paid are classified as:", ["Operating", "Investing", "Financing", "Either operating or financing"], 2, "US GAAP requires financing; IFRS allows operating or financing."),
 ("Under US GAAP, interest paid is classified as:", ["Operating", "Investing", "Financing", "Choice of operating or financing"], 0, "US GAAP: interest paid is operating. IFRS allows operating or financing."),
],
"prereq-indirect-method": [
 ("Net income is 100, depreciation is 20 and accounts receivable rose by 15. Operating cash flow is:", ["135", "105", "85", "95"], 1, "100 + 20 (non-cash expense) − 15 (cash not yet collected) = 105."),
 ("An increase in accounts payable during the year is, in the indirect method:", ["Subtracted", "Added", "Ignored", "Moved to financing"], 1, "Expenses were recorded but not yet paid in cash, so cash flow is higher than net income."),
 ("A gain on selling equipment is subtracted from net income because:", ["It is taxed", "The full cash proceeds are shown in investing activities", "It is an expense", "It reduces inventory"], 1, "The gain is non-operating; the cash received is reported as an investing inflow."),
],
"prereq-inventory-cost": [
 ("Which cost is included in the cost of inventory?", ["Freight to bring raw materials to the factory", "Abnormal waste", "Selling costs", "General administrative overheads"], 0, "Costs needed to bring inventory to its present location and condition are capitalised."),
 ("Storage costs for finished goods waiting to be sold are usually:", ["Included in inventory", "Expensed as incurred", "Capitalised in PP&E", "Deferred forever"], 1, "Storage after production (unless needed in the production process) is a period expense."),
 ("Capitalising a cost in inventory rather than expensing it:", ["Delays the expense until the goods are sold", "Removes it permanently", "Increases revenue", "Has no effect on profit timing"], 0, "The cost waits on the balance sheet and becomes cost of sales when the goods are sold."),
],
"prereq-fifo-lifo-weighted-average": [
 ("Prices are rising. Which method gives the highest cost of sales?", ["FIFO", "LIFO", "Weighted average", "All equal"], 1, "LIFO sends the newest, most expensive costs to cost of sales first."),
 ("Prices are rising. Which method shows the most up-to-date inventory value on the balance sheet?", ["FIFO", "LIFO", "Weighted average", "None"], 0, "Under FIFO the most recent purchases remain in inventory."),
 ("Which method is not permitted under IFRS?", ["FIFO", "Weighted average", "LIFO", "Specific identification"], 2, "IFRS prohibits LIFO; US GAAP allows it."),
],
"prereq-lifo-reserve": [
 ("LIFO inventory is 800 and the LIFO reserve is 200. FIFO inventory would be:", ["600", "800", "1,000", "200"], 2, "FIFO inventory = LIFO inventory + LIFO reserve = 1,000."),
 ("The LIFO reserve rose from 150 to 200 during the year. FIFO cost of sales compared with LIFO cost of sales is:", ["50 higher", "50 lower", "200 lower", "The same"], 1, "FIFO COGS = LIFO COGS − increase in the LIFO reserve."),
 ("A LIFO liquidation (inventory falling below earlier layers) in a period of rising prices tends to:", ["Lower gross margin", "Temporarily inflate gross margin", "Have no effect", "Increase the LIFO reserve"], 1, "Old, cheap costs flow into cost of sales, boosting margins in a way that will not repeat."),
],
"prereq-inventory-writedowns": [
 ("Under IFRS, inventory is measured at:", ["Cost", "The lower of cost and net realisable value", "Fair value", "Replacement cost"], 1, "It cannot be carried above what it is expected to sell for, less costs to complete and sell."),
 ("Can an inventory write-down be reversed when prices recover?", ["Yes under IFRS (up to original cost); no under US GAAP", "Never", "Yes under both", "Only under US GAAP"], 0, "IFRS allows reversal up to the original write-down; US GAAP does not."),
 ("A write-down of inventory affects the current year by:", ["Raising profit", "Reducing profit and inventory", "Raising cash", "Only changing OCI"], 1, "The loss is recognised in profit (often within cost of sales) and the asset is reduced."),
],
"prereq-inventory-ratios": [
 ("Cost of sales is 1,200 and average inventory is 300. Inventory turnover is:", ["0.25", "4", "900", "1,500"], 1, "1,200 ÷ 300 = 4 times a year."),
 ("With a turnover of 4, days of inventory on hand are about:", ["4", "91", "365", "1,460"], 1, "365 ÷ 4 ≈ 91 days."),
 ("A turnover far above industry peers could signal efficient management, or:", ["Too much inventory", "Inventory so low that sales are being lost", "Rising prices only", "A LIFO reserve"], 1, "Very high turnover can mean stock-outs; always compare with sales growth."),
],
"prereq-capitalise-or-expense": [
 ("Compared with expensing, capitalising a cost in the year it is incurred gives:", ["Lower profit", "Higher profit this year and higher operating cash flow", "Lower assets", "Lower investing outflows"], 1, "The cost becomes depreciation over time; the cash outflow moves from operating to investing."),
 ("Over the asset's whole life, capitalising rather than expensing:", ["Increases total profit", "Leaves total profit the same; only timing changes", "Decreases total cash", "Removes the expense"], 1, "The same total cost is expensed eventually, through depreciation."),
 ("Which spending is usually capitalised?", ["Routine repairs", "A new production line expected to last ten years", "Advertising", "Staff training"], 1, "Benefits that last beyond the current year justify an asset."),
],
"prereq-revaluation-model": [
 ("Which framework permits the revaluation model for property, plant and equipment?", ["US GAAP", "IFRS", "Both", "Neither"], 1, "IFRS allows the revaluation model; US GAAP requires the cost model."),
 ("Under the revaluation model, a first upward revaluation goes to:", ["Profit", "Other comprehensive income (revaluation surplus)", "Revenue", "Liabilities"], 1, "An increase above cost goes to OCI, unless it reverses an earlier loss taken to profit."),
 ("Revaluation makes the balance sheet more relevant but:", ["Less reliable, because estimates enter", "Less relevant", "Removes depreciation", "Raises cash"], 0, "Current values are more useful but depend on valuations and judgment."),
],
"prereq-deferred-tax": [
 ("Tax depreciation is faster than accounting depreciation. This creates:", ["A deferred tax asset", "A deferred tax liability", "No temporary difference", "A permanent difference"], 1, "Less tax is paid now and more later, so a liability for future tax is recorded."),
 ("A warranty expense is recognised in the accounts now but deducted for tax only when paid. This creates:", ["A deferred tax asset", "A deferred tax liability", "A permanent difference", "Income tax payable only"], 0, "Tax will be lower in future when the deduction is taken: a future benefit, so an asset."),
 ("A fine that will never be tax-deductible creates:", ["A deferred tax asset", "A deferred tax liability", "A permanent difference with no deferred tax", "A valuation allowance"], 2, "Permanent differences never reverse, so no deferred tax is recorded; they change the effective tax rate."),
],
"prereq-tax-rate-changes-valuation-allowance": [
 ("The tax rate is cut from 30% to 25%. A company's deferred tax liability:", ["Rises", "Falls", "Is unchanged", "Becomes an asset"], 1, "Deferred taxes are remeasured at the new rate, so the future tax owed shrinks."),
 ("Under US GAAP, a valuation allowance is used when:", ["Future taxable profit may not be enough to use a deferred tax asset", "Tax rates rise", "Deferred tax liabilities are large", "Profits are high"], 0, "It reduces the deferred tax asset to the amount more likely than not to be realised."),
 ("Increasing the valuation allowance in a year:", ["Raises reported profit", "Lowers reported profit", "Has no effect on profit", "Increases the asset"], 1, "The increase is recorded as additional tax expense."),
],
"prereq-bonds-effective-interest": [
 ("A bond with a 5% coupon is issued when market rates are 6%. It is issued at:", ["A premium", "Par", "A discount", "Face value plus interest"], 2, "Investors demand 6%, so they pay less than face value for a 5% coupon."),
 ("Under the effective interest method, interest expense equals:", ["Coupon rate × face value", "Market rate at issue × carrying amount", "Current market rate × face value", "Coupon paid"], 1, "Expense uses the rate at issue on the current carrying amount; the coupon uses the coupon rate on face value."),
 ("For a bond issued at a discount, the carrying amount over time:", ["Falls towards face value", "Rises towards face value", "Stays constant", "Falls to zero"], 1, "Interest expense exceeds the coupon, and the difference adds to the carrying amount until it reaches face value."),
],
"prereq-debt-derecognition": [
 ("A company repurchases bonds with a carrying amount of 980 for 1,000. It records:", ["A gain of 20", "A loss of 20", "No gain or loss", "A gain of 1,000"], 1, "Gain or loss = carrying amount − amount paid = 980 − 1,000 = −20 (a loss)."),
 ("Where does the gain or loss on extinguishing debt appear?", ["In profit (income statement)", "Only in OCI", "Directly in retained earnings", "Nowhere"], 0, "It is recognised in profit, often shown separately."),
 ("In the cash flow statement, the cash paid to retire the bonds is a:", ["Operating outflow", "Investing outflow", "Financing outflow", "Non-cash item"], 2, "Repaying borrowings is a financing activity."),
],
"prereq-credit-analysis": [
 ("EBIT is 300 and interest expense is 60. Interest coverage is:", ["0.2", "5", "240", "360"], 1, "300 ÷ 60 = 5 times."),
 ("Which ratio measures leverage relative to what the company generates?", ["Current ratio", "Debt ÷ EBITDA", "Gross margin", "Inventory turnover"], 1, "Debt/EBITDA shows how many years of operating earnings the debt represents."),
 ("Why do lenders focus on downside protection more than growth?", ["They are paid fixed amounts and do not share in upside", "They own the company", "They receive dividends", "Regulation forbids growth"], 0, "A lender's best case is being repaid in full; what matters is the cushion before default."),
],
"prereq-analyst-adjustments": [
 ("To compare a LIFO company with a FIFO company, an analyst should:", ["Ignore the difference", "Restate the LIFO company to FIFO using the LIFO reserve", "Convert both to cash", "Use revenue only"], 1, "The LIFO reserve allows inventory and cost of sales to be put on a FIFO basis."),
 ("Purpose of analyst adjustments:", ["To increase reported profit", "To put companies on the same basis before comparing them", "To meet tax rules", "To audit the company"], 1, "Different choices and standards make raw numbers incomparable."),
 ("Off-balance-sheet obligations are often added back to debt because:", ["They are illegal", "They create economic obligations similar to borrowing", "Auditors missed them", "They raise equity"], 1, "Economic leverage matters to lenders whatever the presentation."),
],
"prereq-price-elasticity": [
 ("Price rises by 10% and quantity demanded falls by 20%. Price elasticity of demand (absolute) is:", ["0.5", "2", "10", "30"], 1, "20% ÷ 10% = 2: demand is elastic."),
 ("If demand is elastic, a price increase will:", ["Raise total revenue", "Lower total revenue", "Leave revenue unchanged", "Raise quantity"], 1, "Quantity falls proportionally more than price rises."),
 ("Demand tends to be more elastic when:", ["There are few substitutes", "The good is a small share of the budget", "There are many close substitutes", "It is a necessity"], 2, "Buyers switch easily when close substitutes exist."),
],
"prereq-income-cross-elasticity": [
 ("Incomes rise 10% and demand for a good falls 5%. The good is:", ["A luxury", "A necessity", "An inferior good", "A complement"], 2, "Negative income elasticity means an inferior good."),
 ("The price of coffee rises and demand for tea rises. Tea and coffee are:", ["Complements", "Substitutes", "Inferior goods", "Unrelated"], 1, "Positive cross-price elasticity signals substitutes."),
 ("Income elasticity of 2 for a good suggests it is:", ["A necessity", "A luxury (normal good with elastic income response)", "Inferior", "Giffen"], 1, "Demand rises faster than income: a luxury."),
],
"prereq-substitution-income-effects": [
 ("When a good's price falls, the substitution effect always:", ["Reduces quantity demanded", "Increases quantity demanded", "Has no effect", "Depends on income"], 1, "The good is relatively cheaper, so buyers substitute towards it."),
 ("For an inferior good, the income effect of a price fall:", ["Increases demand", "Reduces demand", "Is zero", "Equals the substitution effect"], 1, "Feeling richer, buyers move away from the inferior good."),
 ("A Giffen good is one where:", ["Demand rises when income rises", "Quantity demanded rises when its price rises, because a strong income effect outweighs substitution", "The good is a luxury", "Supply is fixed"], 1, "A very strong negative income effect can dominate the substitution effect."),
],
"prereq-marginal-returns": [
 ("Diminishing marginal returns means that, with other inputs fixed, each extra worker eventually adds:", ["More output than the last", "Less output than the last", "No output", "Negative cost"], 1, "Fixed capital limits how much each additional worker can add."),
 ("Diminishing marginal returns applies in:", ["The long run, when all inputs vary", "The short run, when some inputs are fixed", "Only monopolies", "Only perfect competition"], 1, "It describes the short run with at least one fixed input."),
 ("If marginal product is falling, marginal cost is:", ["Falling", "Rising", "Constant", "Zero"], 1, "Each extra unit needs more of the variable input, so it costs more."),
],
"prereq-short-run-costs": [
 ("Total cost rises from 1,000 to 1,060 when output rises from 100 to 103 units. Marginal cost is:", ["10", "20", "60", "1,060"], 1, "ΔTC ÷ ΔQ = 60 ÷ 3 = 20."),
 ("Rent that must be paid regardless of output is a:", ["Variable cost", "Fixed cost", "Marginal cost", "Sunk benefit"], 1, "Fixed costs do not change with output in the short run."),
 ("Marginal cost cuts average total cost:", ["At its maximum", "At its minimum", "Never", "At zero output"], 1, "When MC is below ATC it pulls the average down; above, it pulls it up."),
],
"prereq-profit-maximisation-shutdown": [
 ("A firm maximises profit where:", ["Total revenue is highest", "Marginal revenue equals marginal cost", "Average cost is lowest", "Price equals average fixed cost"], 1, "Producing more adds less revenue than cost beyond that point."),
 ("In the short run a loss-making firm should keep operating as long as price covers:", ["Average total cost", "Average variable cost", "Average fixed cost", "Marginal revenue"], 1, "It then covers its variable costs and contributes something to fixed costs it must pay anyway."),
 ("Breakeven occurs where price equals:", ["Average variable cost", "Average total cost", "Marginal cost only", "Average fixed cost"], 1, "At P = ATC, revenue just covers all costs."),
],
"prereq-market-structures": [
 ("A market with many firms selling differentiated products and easy entry is:", ["Perfect competition", "Monopolistic competition", "Oligopoly", "Monopoly"], 1, "Differentiation gives some pricing power, but entry limits long-run profit."),
 ("Which structure has a few large interdependent firms?", ["Monopoly", "Oligopoly", "Perfect competition", "Monopolistic competition"], 1, "In oligopoly each firm's decisions depend on its rivals'."),
 ("Which firm has the least pricing power?", ["A monopolist", "An oligopolist", "A perfectly competitive firm", "A firm with a patent"], 2, "It is a price taker: identical products and many rivals."),
],
"prereq-perfect-competition": [
 ("In long-run equilibrium under perfect competition, economic profit is:", ["Positive", "Zero", "Negative", "Equal to price"], 1, "Profits attract entry until price falls to minimum average total cost."),
 ("A perfectly competitive firm faces a demand curve that is:", ["Downward sloping", "Perfectly elastic (horizontal) at the market price", "Vertical", "Upward sloping"], 1, "It can sell any quantity at the market price, and nothing above it."),
 ("If firms in a competitive industry are making economic profits, in the long run:", ["Firms leave", "New firms enter and price falls", "Price rises", "Nothing changes"], 1, "Free entry competes the profit away."),
],
"prereq-monopoly": [
 ("For a monopolist, marginal revenue is:", ["Equal to price", "Below price", "Above price", "Zero"], 1, "To sell one more unit it must cut the price on all units."),
 ("Compared with a competitive market, a monopoly typically produces:", ["More at a lower price", "Less at a higher price", "The same", "More at a higher price"], 1, "It restricts output to where MR = MC and charges the price on the demand curve."),
 ("A monopolist sets quantity where MR = MC and then sets price:", ["At MC", "From the demand curve at that quantity", "At ATC", "At MR"], 1, "Demand tells it the highest price buyers will pay for that quantity."),
],
"prereq-price-discrimination": [
 ("A buyer would pay up to 50 for a ticket and pays 30. Consumer surplus is:", ["20", "30", "50", "80"], 0, "50 − 30 = 20."),
 ("Price discrimination requires that the seller can:", ["Raise all prices", "Separate buyers with different willingness to pay and prevent resale", "Lower costs", "Advertise"], 1, "Otherwise low-price buyers resell to high-price buyers."),
 ("Student discounts at cinemas are an example of:", ["Perfect competition", "Price discrimination", "A price ceiling", "Inferior goods"], 1, "Different groups pay different prices for the same product."),
],
"prereq-gdp": [
 ("Which is included in GDP?", ["A used car resold", "A new house built this year", "Shares traded on the stock market", "Unemployment benefits"], 1, "GDP counts final goods and services produced in the period; transfers and resales are excluded."),
 ("GDP = C + I + G + (X − M). Imports are subtracted because:", ["They are bad for the economy", "They are included in C, I and G but were produced abroad", "They are taxed", "They are investment"], 1, "Spending on imports is removed so only domestic production is counted."),
 ("Nominal GDP rose 7% and the GDP deflator rose 3%. Real GDP grew about:", ["10%", "7%", "4%", "3%"], 2, "Real growth ≈ nominal growth − inflation = 4%."),
],
"prereq-saving-investment-identity": [
 ("From S − I = (G − T) + (X − M): a country with a government deficit and private saving equal to investment must have:", ["A trade surplus", "A trade deficit", "Balanced trade", "Higher saving"], 1, "If S − I = 0 and G − T > 0, then X − M must be negative."),
 ("A government deficit means:", ["T > G", "G > T", "X > M", "S > I"], 1, "Spending exceeds tax revenue."),
 ("If private saving exceeds investment and the budget is balanced, the trade balance is:", ["In deficit", "In surplus", "Zero", "Undetermined"], 1, "S − I > 0 with G − T = 0 means X − M > 0."),
],
"prereq-aggregate-demand-supply": [
 ("In the short run, a fall in aggregate demand leads to:", ["Higher output and prices", "Lower output and lower prices", "Higher prices only", "No change"], 1, "AD shifts left along the upward-sloping short-run AS curve."),
 ("The long-run aggregate supply curve is vertical because:", ["Prices are fixed", "In the long run output returns to potential, set by resources and technology", "Demand is fixed", "Wages never change"], 1, "Only the price level adjusts in the long run."),
 ("A sudden rise in oil prices (a negative supply shock) tends to cause:", ["Higher output, lower prices", "Lower output and higher prices (stagflation)", "Lower output, lower prices", "No change"], 1, "SRAS shifts left: prices up, output down."),
],
"prereq-economic-growth": [
 ("Why can capital accumulation alone not sustain growth in output per worker forever?", ["Capital is illegal", "Capital has diminishing marginal returns", "Labour falls", "Technology is fixed"], 1, "Each extra unit of capital adds less, so long-run growth per worker needs technology."),
 ("In growth accounting, the part of growth not explained by labour and capital is attributed to:", ["Inflation", "Total factor productivity (technology)", "Exports", "Government spending"], 1, "The residual measures how efficiently inputs are used."),
 ("Labour grows 1%, capital 4%, capital's share is 0.3 and TFP grows 1%. Output grows about:", ["2.9%", "3.0%", "6%", "1%"], 0, "1% + 0.3 × 4% + 0.7 × 1% = 1 + 1.2 + 0.7 = 2.9%."),
],
"prereq-business-cycle": [
 ("Which phase follows a contraction?", ["Expansion", "Recovery", "Slowdown", "Peak"], 1, "Recovery, expansion, slowdown, contraction, then recovery again."),
 ("Which spending usually falls hardest in a recession?", ["Food", "Business investment and durable goods", "Healthcare", "Utilities"], 1, "Postponable, big-ticket spending is the most cyclical."),
 ("Inventories relative to sales usually rise sharply:", ["Early in a recovery", "As an expansion turns into a slowdown or contraction", "In the middle of an expansion", "Never"], 1, "Sales fall faster than firms can cut production, so stocks pile up."),
],
"prereq-unemployment": [
 ("Labour force 50m, unemployed 3m. The unemployment rate is:", ["3%", "6%", "5.7%", "47%"], 1, "3 ÷ 50 = 6%."),
 ("A coal miner who loses a job because the industry is shrinking is:", ["Frictionally unemployed", "Structurally unemployed", "Cyclically unemployed", "Not in the labour force"], 1, "A mismatch between skills and available jobs is structural."),
 ("People who have stopped looking for work because they believe none is available are:", ["Counted as unemployed", "Discouraged workers, outside the labour force", "Employed", "Frictionally unemployed"], 1, "They are not counted, which can make the unemployment rate look better than the labour market is."),
],
"prereq-inflation-price-indexes": [
 ("Inflation falls from 6% to 3%. This is:", ["Deflation", "Disinflation", "Hyperinflation", "Stagflation"], 1, "Prices are still rising, just more slowly."),
 ("A price index rises from 200 to 210. Inflation is:", ["10%", "5%", "2%", "210%"], 1, "(210 − 200) ÷ 200 = 5%."),
 ("Core inflation excludes:", ["Housing", "Volatile food and energy prices", "Services", "Imports"], 1, "It aims to show the underlying trend."),
],
"prereq-money-creation": [
 ("With a 10% reserve requirement, the simple money multiplier is:", ["0.1", "1", "10", "100"], 2, "1 ÷ 0.10 = 10."),
 ("Which is not a function of money?", ["Medium of exchange", "Unit of account", "Store of value", "Guarantee of return"], 3, "Money's three functions are exchange, unit of account and store of value."),
 ("Most money in a modern economy is created when:", ["The central bank prints notes", "Commercial banks make loans", "Governments tax", "Gold is mined"], 1, "A new loan creates a new deposit."),
],
"prereq-quantity-theory-fisher": [
 ("In MV = PY, if velocity and real output are constant and money supply rises 5%, prices rise about:", ["0%", "5%", "10%", "2.5%"], 1, "With V and Y fixed, P moves one-for-one with M."),
 ("Real interest rate 2%, expected inflation 3%. The Fisher effect implies a nominal rate of about:", ["1%", "3%", "5%", "6%"], 2, "Nominal ≈ real + expected inflation."),
 ("Which is a cost of unexpected inflation?", ["Lenders gain at borrowers' expense", "Wealth is redistributed from lenders to borrowers", "Real wages always rise", "Taxes fall"], 1, "Repayments are worth less in real terms than lenders expected."),
],
"prereq-comparative-advantage": [
 ("Country A can make 10 cloth or 5 wine; Country B 6 cloth or 2 wine. Who has the comparative advantage in wine?", ["A", "B", "Neither", "Both"], 0, "A gives up 2 cloth per wine; B gives up 3. A's opportunity cost is lower."),
 ("Comparative advantage is based on:", ["Absolute productivity", "Opportunity cost", "Exchange rates", "Tariffs"], 1, "Even a less productive country has something it gives up least to make."),
 ("If each country specialises according to comparative advantage and trades:", ["Total output falls", "Both can consume more than they could alone", "Only the richer country gains", "Prices must rise"], 1, "Specialisation raises total output, and trade shares the gains."),
],
"prereq-ricardo-heckscher-ohlin": [
 ("In the Ricardian model, comparative advantage comes from differences in:", ["Factor endowments", "Labour productivity (technology)", "Tastes", "Currencies"], 1, "Ricardo uses one factor and differences in technology."),
 ("Under Heckscher–Ohlin, a capital-rich country exports:", ["Labour-intensive goods", "Capital-intensive goods", "Nothing", "Raw labour"], 1, "It specialises in goods that use its abundant factor intensively."),
 ("Heckscher–Ohlin predicts that opening to trade benefits mainly:", ["The scarce factor", "The abundant factor", "No one", "Consumers only"], 1, "Demand for the abundant factor rises, so its owners gain; the scarce factor may lose."),
],
"prereq-balance-of-payments": [
 ("A country runs a current account deficit. Its financial account will be:", ["In deficit", "In surplus (net inflow of capital)", "Zero", "Unrelated"], 1, "The deficit is financed by selling assets or borrowing abroad."),
 ("Exports of goods and services are recorded in the:", ["Capital account", "Current account", "Financial account", "Reserve account only"], 1, "Trade, income and transfers belong to the current account."),
 ("A foreign company builds a factory in the country. This is recorded in the:", ["Current account", "Financial account (direct investment inflow)", "Capital account", "Trade balance"], 1, "Cross-border investment is a financial account flow."),
],
"prereq-exchange-rates": [
 ("The quote USD/EUR = 1.10 means:", ["1 USD buys 1.10 EUR", "1 EUR costs 1.10 USD", "Both currencies are equal", "Inflation is 10%"], 1, "In this convention the base currency is EUR, priced in USD."),
 ("Nominal rate unchanged, but domestic inflation is higher than foreign inflation. The domestic currency's real value:", ["Falls", "Rises (real appreciation)", "Is unchanged", "Cannot be known"], 1, "Domestic goods become relatively more expensive: a real appreciation that hurts competitiveness."),
 ("The real exchange rate matters for trade because:", ["It ignores prices", "It reflects the relative price of goods across countries", "It is set by central banks", "It equals the nominal rate"], 1, "Trade responds to how expensive goods are in real terms."),
],
"prereq-trade-balance-approaches": [
 ("The Marshall–Lerner condition says a depreciation improves the trade balance if:", ["Export and import demand elasticities sum to more than 1", "Imports are inelastic", "Interest rates fall", "Inflation is zero"], 0, "Volumes must respond enough to outweigh the higher price of imports."),
 ("The J-curve describes:", ["A trade balance that first worsens, then improves after a depreciation", "Rising interest rates", "A falling currency forever", "GDP growth"], 0, "Volumes adjust slowly, so the price effect dominates at first."),
 ("Under the absorption approach, a depreciation improves the trade balance only if:", ["Domestic spending falls relative to income", "Spending rises", "Exports fall", "The budget deficit grows"], 0, "X − M = income − absorption, so spending must fall relative to income."),
],
}


# Nov 2026: harder five-question quizzes replace the originals lesson by lesson
from quiz_bank2 import Q2  # noqa: E402
Q.update(Q2)
