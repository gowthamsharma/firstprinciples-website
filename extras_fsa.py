# Extra, original material for the financial statement analysis concepts:
# tags = other names people search for; faq = (question, answer) pairs.
X = {
"01": ("financial reporting objective, conceptual framework, qualitative characteristics, relevance, faithful representation, materiality, CFA Level 1 financial reporting", [
 ("Who are financial statements written for?", "Mainly for people who provide money to a company and cannot demand custom reports: shareholders, bondholders, banks and anyone thinking of joining them. Managers, regulators and tax authorities use them too, but the rules are designed around outside capital providers."),
 ("What makes accounting information useful?", "Two things above all: it must be able to change a decision (relevance) and it must show what really happened, without slant or error (faithful representation). Comparability, verifiability, timeliness and understandability then make good information better."),
 ("Is being conservative the same as being neutral?", "No. Deliberately low numbers are as biased as deliberately high ones. Modern frameworks ask for neutrality and treat prudence as caution in judgement, not a licence to understate."),
]),
"02": ("three financial statements, how financial statements link, balance sheet, income statement, cash flow statement, statement of financial position, articulation", [
 ("Which financial statement is the most important?", "None on its own. Profit can be shaped by estimates, cash flow can be lumpy and the balance sheet is a snapshot. An analyst reads all three together, because a story that holds in one but not the others is a warning sign."),
 ("How does net income reach the balance sheet?", "Profit for the year, less any dividends declared, is added to retained earnings, which is part of equity. That single link is why the balance sheet still balances after a year of trading."),
 ("Why can a profitable company run out of cash?", "Profit counts sales when earned, not when paid. A fast-growing firm can book large profits while its cash is tied up in customer receivables and stock, so cash flow from operations is the check on profit quality."),
]),
"03": ("accrual accounting, accruals, matching principle, prepaid expenses, accrued expenses, unearned revenue, deferred revenue, cash vs accrual basis", [
 ("What is the difference between cash and accrual accounting?", "Cash accounting records money when it moves. Accrual accounting records revenue when it is earned and costs when they are used up, whatever the timing of the payment. Listed companies must use accruals, because cash timing alone hides performance."),
 ("What are the four types of accruals?", "Cash received before the work (unearned revenue), work done before the cash (accrued revenue), cash paid before the cost is used (prepaid expense) and cost used before it is paid (accrued expense). Each one parks a timing difference on the balance sheet."),
 ("Why do analysts watch accruals?", "Because they rest on estimates. When profit grows much faster than operating cash flow year after year, the gap is made of accruals, and large accruals have historically been followed by weaker earnings."),
]),
"04": ("revenue recognition, IFRS 15, ASC 606, five-step model, performance obligations, transaction price, contract revenue", [
 ("What are the five steps of revenue recognition?", "Find the contract, list the separate promises in it, set the total price, split that price across the promises by their stand-alone selling prices, and book each slice as the promise is fulfilled, at a point in time or over time."),
 ("When is revenue recognised over time rather than at a point?", "When the customer gets the benefit as the work proceeds, controls the asset while it is being built, or the seller builds something with no alternative use and has a right to be paid for work done so far. Long construction contracts are the typical case."),
 ("How do analysts spot aggressive revenue recognition?", "Watch receivables growing faster than sales, unusual end-of-quarter spikes, changes in estimates of contract progress and a rise in unbilled revenue. Each means revenue is running ahead of cash."),
]),
"05": ("allowance for doubtful accounts, bad debt expense, warranty provision, warranty expense, estimates in accounting, earnings management", [
 ("Why not wait until a customer actually defaults?", "Because the loss was caused by this year's credit sales. Booking it later would flatter this year and punish a later one. Estimating the expected loss now keeps each year's profit honest."),
 ("How can estimates be used to manage earnings?", "By setting the allowance or warranty provision too high in good years and releasing it in bad years. Profit then looks smoother than the business really is. A falling allowance while receivables rise deserves questions."),
 ("Where do these estimates appear in the accounts?", "The allowance sits against receivables on the balance sheet, so receivables are shown net. The warranty provision is a liability. Both changes run through the income statement as expenses."),
]),
"06": ("depreciation methods, straight-line depreciation, declining balance, double-declining balance, units of production, salvage value, useful life", [
 ("Which depreciation method gives higher profit?", "In the early years, straight-line does, because accelerated methods put more of the cost into the first years. Over the asset's whole life the total expense is the same; only the timing differs."),
 ("Does depreciation affect cash flow?", "Not directly: no cash leaves when depreciation is booked. It does matter for tax, because tax depreciation lowers the tax bill, and in the indirect cash flow statement it is added back to net income."),
 ("What happens when the useful life estimate changes?", "The change is applied going forward: the remaining book value is spread over the new remaining life. Past years are not restated. A sudden longer life is a classic way to lift profit."),
]),
"07": ("non-recurring items, discontinued operations, unusual items, restructuring charges, one-off costs, core earnings, operating vs non-operating income", [
 ("Why separate one-off items from recurring profit?", "Valuation is about the future. A gain from selling a building will not happen again, so an analyst removes it to see the earnings power the business can keep producing."),
 ("When is a business a discontinued operation?", "When a whole component that can be clearly distinguished, such as a major line of business or region, has been sold or is held for sale. Its results are shown separately, net of tax, below continuing operations."),
 ("Are restructuring charges really one-off?", "Not always. Some companies report them almost every year. If an item recurs, treat it as a normal cost of doing business, whatever the label says."),
]),
"08": ("common-size analysis, vertical analysis, horizontal analysis, common-size income statement, common-size balance sheet, financial ratio analysis", [
 ("What is the difference between vertical and horizontal analysis?", "Vertical (common-size) analysis divides every line by a base in the same year, such as revenue or total assets. Horizontal analysis tracks how one line changes across years. Using both shows structure and trend."),
 ("Why is common-size analysis useful for comparing companies?", "It strips out size. A company with revenue of 10 billion and one with 100 million can be compared line by line once everything is a percentage of revenue."),
 ("What should you look for first in a common-size income statement?", "Gross margin and the big expense lines. A shrinking gross margin points to pricing or input costs; rising overheads as a share of sales point to weaker cost control."),
]),
"09": ("other comprehensive income, OCI, comprehensive income, recycling, accumulated OCI, fair value through OCI, foreign currency translation", [
 ("What goes into other comprehensive income?", "Gains and losses that standard setters keep out of profit for now: currency translation of foreign subsidiaries, certain pension remeasurements, some fair value changes on investments and the effective part of hedges of future cash flows."),
 ("What does recycling mean?", "Moving a gain or loss that sat in OCI into profit when it is finally realised, for example when the hedged transaction happens. Under IFRS some OCI items are recycled and some never are."),
 ("Why should analysts look at comprehensive income?", "Because large losses can sit in OCI without ever touching net income. Comparing companies on comprehensive income shows the full change in owners' wealth from things other than dealings with owners."),
]),
"10": ("balance sheet classification, current assets, current liabilities, non-current assets, working capital, liquidity, statement of financial position", [
 ("Why does the current versus non-current split matter?", "It shows whether short-term obligations are covered by assets that will soon become cash. Working capital and the current ratio are both built on it."),
 ("Is a long-term loan always a non-current liability?", "No. The part falling due within the next year is moved to current liabilities, and the whole loan can become current if a covenant breach lets the lender demand repayment."),
 ("Do all companies order the balance sheet the same way?", "No. Many IFRS reporters list long-term items first; US companies usually start with cash. Banks often skip the split entirely and list items by liquidity."),
]),
"11": ("shareholders' equity, retained earnings, share capital, treasury shares, share buybacks, non-controlling interest, statement of changes in equity", [
 ("What are the main parts of shareholders' equity?", "Money put in by owners (share capital and share premium), profit kept in the business (retained earnings), accumulated other comprehensive income, minus any shares the company has bought back and holds. Non-controlling interest is shown within equity too."),
 ("How does a share buyback change equity?", "Cash goes out and equity falls by the same amount. Bought-back shares held by the company are shown as a deduction from equity, not as an asset."),
 ("Can equity be negative?", "Yes. Long losses or large buybacks funded by debt can push it below zero. That alone is not fatal, but it means ratios built on equity, such as return on equity or debt-to-equity, stop making sense."),
]),
"12": ("cash flow statement classification, operating cash flow, investing cash flow, financing cash flow, interest paid classification, IFRS vs US GAAP cash flows", [
 ("Where do interest and dividends go in the cash flow statement?", "Under US GAAP, interest paid and received and dividends received are operating, and dividends paid are financing. IAS 7 has allowed a choice: interest paid as operating or financing, interest and dividends received as operating or investing, dividends paid as operating or financing. IFRS 18, effective from 2027, removes most of that choice for non-financial companies."),
 ("Why does classification matter if total cash is the same?", "Because analysts value the operating figure most. Moving interest paid out of operating under IFRS makes operating cash flow look larger, which affects comparisons with US companies."),
 ("Which cash flows count as investing?", "Buying and selling long-term assets and investments: equipment, property, businesses and securities not held for trading. Capital expenditure is the largest item for most firms."),
]),
"13": ("indirect method cash flow, operating cash flow from net income, working capital changes, add back depreciation, direct vs indirect method", [
 ("Why add depreciation back to net income?", "Because it reduced profit without any cash leaving. The cash went out years earlier, when the asset was bought, and was shown then as investing cash flow."),
 ("How do working capital changes affect operating cash flow?", "A rise in an operating asset such as receivables or inventory uses cash, so it is subtracted. A rise in an operating liability such as payables keeps cash in the business, so it is added."),
 ("Do direct and indirect methods give different operating cash flow?", "No. The total is the same; only the presentation differs. The direct method lists cash received and paid; the indirect method reconciles from net income. Most companies use the indirect method."),
]),
"14": ("inventory cost, cost of inventory, capitalised inventory costs, freight-in, storage costs, abnormal waste, cost of goods sold", [
 ("Which costs are included in inventory?", "Purchase price, import duties, freight to bring goods in, and the labour and overheads of turning materials into finished products. In short, whatever had to be spent to make the goods ready to sell."),
 ("Which costs are expensed straight away?", "Abnormal waste, storage after production (unless it is part of the process, such as ageing wine), general administration and the costs of selling. These do not add to what the goods are worth."),
 ("Why does inventory costing affect profit?", "Costs placed in inventory wait on the balance sheet until the goods are sold. Putting more costs into inventory raises this period's profit and lowers a later period's."),
]),
"15": ("FIFO, LIFO, weighted average cost, inventory valuation methods, cost flow assumptions, FIFO vs LIFO inflation", [
 ("Which method gives higher profit when prices rise?", "FIFO. It charges the oldest, cheapest units to cost of sales, so profit and closing inventory are both higher. LIFO charges the newest, dearest units, lowering profit and tax."),
 ("Is LIFO allowed under IFRS?", "No. IFRS permits FIFO, weighted average and specific identification. LIFO is allowed only under US GAAP, mainly because of its tax advantage when prices rise."),
 ("Which balance sheet figure is more realistic?", "FIFO's, because closing inventory is made of the most recent purchases. Under LIFO, inventory can be valued at prices that are decades old."),
]),
"16": ("LIFO reserve, LIFO to FIFO conversion, LIFO liquidation, adjusting inventory, comparability across companies", [
 ("How do you convert LIFO inventory to FIFO?", "Add the LIFO reserve to LIFO inventory. Cost of sales under FIFO equals LIFO cost of sales minus the increase in the reserve during the year."),
 ("What is a LIFO liquidation?", "When a LIFO company sells more than it buys, old cheap layers flow into cost of sales. Profit jumps for a year, but the gain is temporary and not a sign of better business."),
 ("Why adjust equity when converting?", "The higher FIFO inventory would have meant higher past profits and therefore more tax. So the reserve is added to equity after tax, with the tax part going to a deferred tax liability."),
]),
"17": ("inventory write-down, net realisable value, NRV, lower of cost or market, inventory impairment, reversal of write-downs", [
 ("What is net realisable value?", "The expected selling price minus any costs still needed to finish and sell the goods. It is what the inventory is really worth to the business today."),
 ("Can an inventory write-down be reversed?", "Under IFRS, yes, up to the original cost, if the selling price recovers. Under US GAAP a write-down is permanent."),
 ("How does a write-down affect ratios?", "Profit falls in the year of the write-down, and lower inventory raises turnover ratios later. Gross margin in the next period can look better than the underlying business."),
]),
"18": ("inventory turnover, days of inventory on hand, DOH, inventory days, cash conversion cycle, working capital efficiency", [
 ("What does inventory turnover tell you?", "How many times a year the company sells through its average stock. Higher turnover means goods spend less time on the shelf, which ties up less cash."),
 ("Is a very high inventory turnover always good?", "Not necessarily. It can mean the firm keeps too little stock and loses sales when demand jumps. Compare with peers and look at sales growth before judging."),
 ("How does inventory fit into the cash conversion cycle?", "The cycle is days of inventory plus days of receivables minus days of payables. It measures how long cash is tied up from paying suppliers to collecting from customers."),
]),
"19": ("capitalise vs expense, capitalised costs, capital expenditure, research and development accounting, development costs, capitalised interest", [
 ("What decides whether a cost is capitalised?", "Whether it will bring benefits over more than one year. If so, it becomes an asset and is spread over its life through depreciation or amortisation; if not, it is an expense now."),
 ("How does capitalising change the cash flow statement?", "A capitalised cost is an investing outflow; an expensed cost reduces operating cash flow. Capitalising more therefore makes operating cash flow look stronger."),
 ("How are research and development treated?", "Under IFRS, research is expensed and development can be capitalised once strict conditions are met. Under US GAAP both are generally expensed, with software as a notable exception."),
]),
"20": ("revaluation model, cost model, fair value, investment property, IAS 16, IAS 40, revaluation surplus", [
 ("What is the revaluation model?", "An IFRS option to carry property, plant and equipment at fair value, updated regularly. Increases go to a revaluation surplus in equity; decreases go to profit unless they reverse an earlier increase."),
 ("Can US companies revalue assets upward?", "No. US GAAP requires the cost model for property, plant and equipment, with impairment write-downs but no upward revaluation."),
 ("How is investment property different?", "It is held to earn rent or grow in value, not to run the business. Under IFRS it can use a fair value model where every change goes straight to profit, which can make earnings volatile."),
]),
"21": ("deferred tax, deferred tax liability, deferred tax asset, temporary differences, permanent differences, tax base, income tax expense", [
 ("What creates a deferred tax liability?", "Paying less tax now than the accounts suggest, with the difference to be paid later. The classic cause is faster depreciation on the tax return than in the accounts."),
 ("What creates a deferred tax asset?", "Paying more tax now than the accounts suggest, or having losses that will reduce future tax. Warranty provisions and tax loss carryforwards are common examples."),
 ("Should analysts treat deferred tax liabilities as debt?", "Only if they are expected to reverse. A liability that keeps growing because the company keeps investing may never be paid and can be treated more like equity."),
]),
"22": ("tax rate change deferred tax, valuation allowance, deferred tax asset recoverability, effective tax rate, statutory tax rate", [
 ("What happens to deferred taxes when the tax rate changes?", "All deferred tax balances are remeasured at the new rate, and the adjustment flows through tax expense in that year. A rate cut shrinks both deferred tax assets and liabilities."),
 ("What is a valuation allowance?", "A US GAAP reduction of deferred tax assets for the part that will probably never be used, usually because the company may not earn enough taxable profit. IFRS reaches the same result by recognising only the recoverable amount."),
 ("Why watch changes in the valuation allowance?", "Because releasing it lowers tax expense and lifts profit without any change in the business. A sudden release can be a sign of earnings management, or of genuinely better prospects."),
]),
"23": ("bonds payable, effective interest method, bond discount, bond premium, amortised cost, interest expense on bonds, coupon vs market rate", [
 ("What is the effective interest method?", "Interest expense each period equals the bond's carrying amount at the start of the period times the market rate at issue. The difference from the cash coupon adjusts the carrying amount toward face value."),
 ("Why is interest expense different from the coupon paid?", "Because the bond was sold at a discount or premium. A discount means investors receive part of their return at maturity, so expense exceeds the coupon; a premium works the other way."),
 ("Where does the coupon go in the cash flow statement?", "Under US GAAP, interest paid is operating. Under IFRS it can be operating or financing. The money raised at issue and repaid at maturity is always financing."),
]),
"24": ("debt derecognition, early repayment of debt, gain on extinguishment, loss on redemption, bond buyback, debt covenants", [
 ("How is the gain or loss on early repayment calculated?", "Carrying amount of the debt minus the price paid to retire it. Paying more than the carrying amount gives a loss; paying less gives a gain."),
 ("Where is the gain or loss reported?", "In profit for the period, usually as a separate line or in non-operating items. Analysts typically remove it from recurring earnings."),
 ("Why would a company repay debt early?", "To refinance at a lower rate after rates fall, to escape restrictive covenants or to use spare cash. A gain from buying back debt cheaply often signals that the market doubts the company's credit."),
]),
"25": ("credit analysis, leverage ratios, interest coverage, debt to EBITDA, credit ratings, four Cs of credit, solvency ratios", [
 ("Which ratios matter most in credit analysis?", "Leverage (debt to EBITDA, debt to capital), coverage (EBITDA or EBIT to interest) and cash flow measures such as free cash flow to debt. Together they show how heavy the debt is and how easily it is serviced."),
 ("What are the four Cs of credit?", "Capacity to repay, collateral, covenants that protect lenders, and character of management. Ratios mostly measure capacity; the other three need judgement."),
 ("How do analysts adjust debt for credit analysis?", "By adding obligations that act like debt but sit outside it, such as lease liabilities under older rules, unfunded pension deficits and guarantees. Rating agencies make similar adjustments."),
]),
"26": ("analyst adjustments, comparability adjustments, adjusting financial statements, IFRS vs US GAAP differences, quality of earnings", [
 ("Why do analysts adjust reported numbers?", "To compare companies on the same basis. Different accounting choices, such as LIFO versus FIFO or capitalising versus expensing, can make similar businesses look different."),
 ("What are the most common adjustments?", "Converting LIFO to FIFO, removing goodwill or one-off items, adding off-balance-sheet obligations to debt and putting capitalised versus expensed costs on the same footing."),
 ("Is there one right set of adjustments?", "No. The right adjustment depends on the question. For credit analysis you add hidden debts; for valuation you focus on recurring earnings and economic assets."),
]),
}
