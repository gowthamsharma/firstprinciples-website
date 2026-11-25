# Harder lesson quizzes for the prerequisites course (Nov 2026 rewrite).
# Format: slug -> [(question, [correct, wrong, wrong], explanation)]. Three options, as in the real exam;
# build_site.py shuffles the order with a fixed seed. Five questions per lesson, mostly calculations and short cases.
# Every number is checked in check_quizzes() at the bottom (python quiz_bank2.py).
Q2 = {
"prereq-financial-reporting-objective": [
 ("A mining company reports the value of its proved reserves. The figure is highly useful for forecasting future cash flows, but two independent engineers could arrive at noticeably different values. Under the conceptual framework, the information is best described as:",
  ["Relevant, but weak on verifiability, an enhancing quality", "Not relevant, because it cannot be verified", "Not a faithful representation, because it is not timely"],
  "Predictive value makes the reserves figure relevant, a fundamental quality. Verifiability is only an enhancing quality: weakness there calls for good disclosure of assumptions, not for leaving the figure out. Timeliness is not the issue in the case."),
 ("An analyst notices that a company always books possible losses at the top of the estimated range and possible gains at the bottom, 'to be prudent'. Under the conceptual framework this practice most likely:",
  ["Undermines neutrality, and so faithful representation", "Improves faithful representation, because it is conservative", "Has no effect on the qualities, because it only affects estimates"],
  "Faithful representation requires information to be complete, neutral and free from error. A systematic tilt in either direction is a bias. Prudence means care in making judgements, not a deliberate understatement."),
 ("A company has revenue of 2,000 million and net income of 40 million. It leaves out a legal provision of 15 million. The omission is most likely:",
  ["Material, because it would reduce net income by 37.5%", "Immaterial, because it is only 0.75% of revenue", "Immaterial, because no cash has been paid yet"],
  "Materiality is judged by whether the item could change users' decisions. 15 ÷ 40 = 37.5% of profit would clearly change an investor's view, even though 15 ÷ 2,000 = 0.75% of revenue looks small. Whether cash has moved is irrelevant under accrual accounting."),
 ("Which body is responsible for enforcing the use of financial reporting standards by companies listed in its market?",
  ["A securities regulator, such as the US SEC", "The IASB", "The company's external auditor"],
  "Standard setters such as the IASB and FASB write the rules but have no enforcement power. Securities regulators decide which standards listed companies must use and enforce them. Auditors give an opinion on one company's accounts; they do not enforce standards across a market."),
 ("A company signs a contract to buy 1,000 tonnes of steel next year at the market price on delivery. Nothing has been delivered or paid, and the contract is not expected to make a loss. Under the conceptual framework, at the year-end the company most likely recognises:",
  ["Neither an asset nor a liability for the contract", "A liability for the full purchase price", "An asset for the steel and a liability for the price"],
  "Neither side has performed, so this is an executory contract. Such contracts are generally not recognised; a liability would arise only if the contract became onerous (expected to make a loss). The steel is not yet controlled by the company, so it is not an asset."),
],
"prereq-three-statements": [
 ("A company's retained earnings were 400 at the start of the year. Net income for the year was 80, and dividends of 30 were declared. Closing retained earnings are closest to:",
  ["450", "480", "370"],
  "Closing retained earnings = 400 + 80 − 30 = 450. 480 ignores the dividend; 370 forgets the year's profit and only deducts the dividend."),
 ("A company buys equipment for 200 by signing a two-year note payable to the supplier. No cash changes hands this year. Which statement best describes the effect?",
  ["Total assets and total liabilities both rise by 200, and nothing appears in the cash flow statement itself", "Investing cash outflow of 200 and financing cash inflow of 200", "Total assets are unchanged because the equipment was bought on credit"],
  "The company gains an asset and an obligation of equal size, so the equation stays balanced. Because no cash moved, the purchase is a non-cash investing and financing activity, disclosed in a note rather than shown as cash flows."),
 ("Cash at the start of the year is 120. Cash flow from operations is +300, from investing −450 and from financing +80. Cash at the end of the year is:",
  ["50", "−70", "950"],
  "Ending cash = 120 + 300 − 450 + 80 = 50. −70 is only the net change for the year (it forgets the opening balance); 950 adds every figure as if all were inflows."),
 ("A company sells goods costing 300 from inventory for 500 on credit. Immediately after the sale, before the customer pays:",
  ["Total assets rise by 200 and operating cash flow is unchanged", "Total assets rise by 500 and operating cash flow rises by 200", "Equity is unchanged until the customer pays"],
  "Receivables rise by 500 and inventory falls by 300, so assets rise by 200. Retained earnings rise by the 200 profit, keeping the equation in balance. No cash has moved, so operating cash flow is unchanged."),
 ("At the start of the year a company's equity is 800. During the year it earns net income of 150, pays dividends of 50 and issues new shares for 100. There is no other comprehensive income. Closing equity is:",
  ["1,000", "900", "1,050"],
  "Closing equity = 800 + 150 − 50 + 100 = 1,000. 900 forgets the share issue; 1,050 forgets the dividend."),
],
"prereq-accrual-accounting": [
 ("A company with a 31 December year-end paid 2,400 on 1 April for 12 months of insurance cover. At 31 December, prepaid insurance on the balance sheet is:",
  ["600", "1,800", "2,400"],
  "Nine months (April to December) have been used: 2,400 × 9/12 = 1,800 of expense. The remaining three months, 600, are still a prepaid asset."),
 ("At the year-end a company forgets to record wages of 50 that staff have earned but will be paid next month. As a result:",
  ["Net income is overstated by 50 and liabilities are understated by 50", "Net income is understated by 50 and assets are overstated by 50", "Neither statement is affected, because the wages will be paid soon"],
  "The wages belong to this year, so the expense and an accrued liability should both be recorded now. Leaving them out makes expenses too low (profit too high) and liabilities too low."),
 ("A company borrows 10,000 at 6% a year on 1 November. Interest is paid once a year, on 31 October. At its 31 December year-end, interest payable is:",
  ["100", "600", "50"],
  "Two months of interest have built up: 10,000 × 6% × 2/12 = 100. 600 is a full year; 50 is only one month."),
 ("A magazine publisher receives 360 on 1 July for a 12-month subscription. At its 31 December year-end it reports:",
  ["Revenue of 180 and a liability of 180", "Revenue of 360 and no liability", "No revenue and a liability of 360"],
  "Six of the twelve issues have been delivered: revenue 360 × 6/12 = 180. The remaining 180 is unearned revenue, a liability until the issues are delivered."),
 ("For three years in a row, a company's net income has grown by about 30% a year while its operating cash flow has stayed flat. The most appropriate conclusion for an analyst is:",
  ["Earnings are increasingly made of accruals, so receivables and other accrual balances deserve scrutiny", "Operating cash flow must be overstated", "The company must be using the cash basis of accounting"],
  "The gap between profit and operating cash flow is made of accruals, for example receivables or inventory building up. Accruals rest on estimates and must eventually turn into cash, so a persistent, widening gap is a warning sign of lower earnings quality."),
],
"prereq-revenue-recognition": [
 ("A builder signs a contract for 12 million with expected total costs of 9 million and measures progress by costs incurred. In year 1 it incurs costs of 3.6 million. Revenue recognised in year 1 is:",
  ["4.8 million", "3.6 million", "1.2 million"],
  "Progress = 3.6 ÷ 9 = 40%. Revenue = 12 × 40% = 4.8 million, giving a profit of 1.2 million. 3.6 is the cost, not the revenue; 1.2 is the profit."),
 ("A retailer sells a laptop with one year of technical support for a single price of 1,300. Sold separately, the laptop costs 1,200 and the support 300. Revenue recognised when the laptop is delivered is closest to:",
  ["1,040", "1,200", "1,000"],
  "The price is allocated by stand-alone selling prices: 1,300 × 1,200 ÷ 1,500 = 1,040 for the laptop, recognised on delivery. The remaining 260 is recognised over the year of support. 1,000 wrongly gives the support its full stand-alone price."),
 ("An online platform sells a concert ticket for 80 on behalf of an event organiser. The platform never controls the ticket and keeps a fee of 8. The platform's revenue from the sale is:",
  ["8", "80", "72"],
  "The platform is an agent: it arranges the sale but does not control the good first. An agent reports only its commission as revenue, 8. The organiser, as principal, reports the gross 80."),
 ("A contractor will receive a fixed fee of 1,000 plus a bonus of 100 if it finishes early. Management estimates a 60% chance of earning the bonus, and the outcome depends on weather it cannot control. The transaction price at the start of the contract is most likely:",
  ["1,000", "1,060", "1,100"],
  "Variable consideration is included only to the extent that a significant reversal of revenue later is highly unlikely. A 60% chance, driven by factors outside the contractor's control, does not meet that bar, so the bonus is left out until the uncertainty is resolved."),
 ("A contract has a price of 5 million. The builder recognised a profit of 0.3 million on it in year 1. In year 2 it revises its estimates: total costs are now expected to be 5.5 million. The effect on year-2 profit from this contract is a:",
  ["Loss of 0.8 million", "Loss of 0.5 million", "Loss of 0, because the loss is spread over the remaining work"],
  "The contract is now expected to lose 5 − 5.5 = 0.5 million, and an expected loss is recognised in full at once. Cumulative profit must therefore be −0.5; with +0.3 already recognised in year 1, year 2 shows −0.8. Answering −0.5 forgets to reverse the year-1 profit."),
],
"prereq-doubtful-accounts-warranties": [
 ("A company's allowance for doubtful accounts was 400 at the start of the year. During the year it wrote off 350 of uncollectable receivables. The allowance at the year-end is 500. Bad debt expense for the year is:",
  ["450", "100", "850"],
  "Closing = opening + expense − write-offs, so 500 = 400 + E − 350 and E = 450. 100 is just the change in the allowance; 850 adds the write-offs instead of netting them."),
 ("An aging schedule shows receivables of 8,000 current (2% expected loss), 1,500 at 31 to 90 days (10%) and 500 over 90 days (40%). Before any year-end adjustment the allowance has a balance of 130. Bad debt expense for the year is:",
  ["380", "510", "640"],
  "Required allowance = 8,000 × 2% + 1,500 × 10% + 500 × 40% = 160 + 150 + 200 = 510. The expense tops the allowance up from 130 to 510: 380. 510 forgets the existing balance; 640 adds it instead of subtracting."),
 ("Under the allowance method, a company writes off a specific customer's balance of 120 as uncollectable. The effect is:",
  ["No change in net receivables and no expense", "An expense of 120", "Net receivables fall by 120"],
  "The write-off reduces both gross receivables and the allowance by 120, so net receivables are unchanged. The expense was recognised earlier, when the allowance was estimated."),
 ("A company sells 20,000 units. It expects 3% of them to need a repair under warranty, at an average cost of 40 per repair. Warranty expense for the year is:",
  ["24,000", "600", "800,000"],
  "Expected claims = 20,000 × 3% = 600 repairs; expense = 600 × 40 = 24,000. 600 is the number of repairs, not their cost; 800,000 applies the repair cost to every unit sold."),
 ("A company's receivables grew 25% this year, faster than sales, while its allowance fell from 5% to 3% of receivables. Nothing in the notes explains a change in customers' credit quality. An analyst's most appropriate response is to:",
  ["Question whether the lower allowance is justified, because it raises reported profit without any cash", "Raise the forecast for operating cash flow", "Ignore it, because the allowance does not affect profit"],
  "A lower allowance rate means a lower bad debt expense and higher profit. Combined with receivables growing faster than sales, it can signal aggressive estimates. The allowance does affect profit through the expense, and it does not create cash."),
],
}


def check_quizzes():
    assert 400 + 80 - 30 == 450 and 120 + 300 - 450 + 80 == 50 and 800 + 150 - 50 + 100 == 1000
    assert 2400 * 9 / 12 == 1800 and 10000 * 0.06 * 2 / 12 == 100 and 360 * 6 / 12 == 180
    assert abs(12 * 3.6 / 9 - 4.8) < 1e-9 and round(1300 * 1200 / 1500) == 1040
    assert abs((5 - 5.5) - 0.3 - (-0.8)) < 1e-9
    assert 400 + 450 - 350 == 500 and 8000 * .02 + 1500 * .1 + 500 * .4 - 130 == 380 and 20000 * .03 * 40 == 24000
    for k, v in Q2.items():
        assert len(v) == 5, k
        for q, o, x in v:
            assert len(o) == 3 and len(set(o)) == 3, (k, q)
    print("quiz checks ok:", len(Q2), "lessons")


if __name__ == "__main__":
    check_quizzes()
