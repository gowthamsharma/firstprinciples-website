"""Write content/country/*.md: one page per country with exam centres, fees in local currency, pay,
employers, recognition and the local society. Run after changing the data below, then run build_site.py.
Facts were checked on 22 November 2026; sources are listed on each page."""
import pathlib, json

ROOT = pathlib.Path(__file__).resolve().parent
UPDATED = "2026-11-22"
FEES = {"I": (1140, 1490), "II": (1140, 1490), "III": (1240, 1590)}  # USD early, standard (CFA Institute, exams from Feb 2026)
RATE_NOTE = "European Central Bank reference rates of 20 November 2026"

TOP_EMP = "https://www.cfainstitute.org/programs/cfa-program/careers/employers-list"
CITIES = "https://cfainstitute.org/sites/default/files/docs/programs/cfa-program/cities-list-feb25.pdf"
FACTCARD = "https://www.cfainstitute.org/-/media/documents/factsheet/rpr-factsheet.pdf"
RPR = "https://www.cfainstitute.org/programs/candidate-resources/regulator-program-recognition"
FEESRC = "https://www.cfainstitute.org/programs/cfa-program/dates-fees"
ACCESS = "https://www.cfainstitute.org/programs/cfa-program/scholarships/access"
PAYSCALE = "https://www.payscale.com/research/{cc}/Certification=Chartered_Financial_Analyst_(CFA)/Salary"

C = [
 dict(alias=["CFA USA", "CFA exam United States", "Series 65 waiver CFA"], code="us", cc="US", name="the United States", short="the US", adj="American", cur="USD", sym="$", rate=1.0, fmt="{:,.0f}",
      photo="wall-street", demonym="US",
      cities_n=183, cities="more than 180 cities, in every state, from New York, Chicago, Boston and San Francisco to smaller cities such as Boise, Billings and Anchorage",
      sal=("$110,000", 110000, "1,826", "July 2026"),
      intro="The United States is where the charter began in 1963 and where the most charterholders still work. Asset managers, banks, pension funds and insurers in New York, Boston, Chicago and San Francisco list it in job adverts for research, portfolio management and risk roles, and in most states it also replaces the investment adviser licensing exam.",
      employers=[("JPMorgan Chase", "2,582"), ("Bank of America", "1,680"), ("Morgan Stanley", "1,640"), ("BlackRock", "1,365"), ("Citigroup", "1,365"), ("Goldman Sachs", "1,329"), ("Fidelity Investments", "1,198"), ("Wells Fargo", "850")],
      emp_note="Six of the ten largest employers of charterholders worldwide are headquartered in the United States. Asset managers such as Vanguard, T. Rowe Price, Wellington and Capital Group also employ more than 380 each.",
      recog=["**Investment adviser licensing.** Charterholders receive a waiver from the Uniform Investment Adviser Law Examination (Series 65) in the states that require a licensing exam for investment adviser representatives (NASAA and CFA Institute).",
             "**Research analysts.** A research analyst who has passed Levels I and II may request an exemption from FINRA's Series 86 (the analysis part of the research analyst exam); Series 87 is still required.",
             "**Employers.** There is no legal requirement to hold the charter, but many buy-side job adverts list it as preferred or required for senior research and portfolio roles."],
      society="The United States has dozens of local CFA societies, from CFA Society New York and CFA Society Chicago to CFA Society Los Angeles and CFA Society Boston. They run study groups, mock exams, networking events and the CFA Institute Research Challenge for university teams.",
      extra=("Taxes and employer support", "Many US employers reimburse exam fees and study materials, often after you pass. If you pay yourself, CFA exam fees may or may not be deductible depending on your situation and current tax law; ask a tax adviser before assuming either way."),
      faq=[("Does the CFA replace the Series 65?", "In the states that require the Series 65 exam for investment adviser representatives, charterholders can have it waived. You still need to register with your state, and broker-dealer roles still need the FINRA exams."),
           ("How many CFA test centres are there in the US?", "CFA Institute's planned list names more than 180 US cities. Seat availability varies by window, so book early if you need a particular centre.")],
      srcs=[("NASAA: exam FAQ (professional designation waivers)", "https://www.nasaa.org/exams/exam-faqs/")]),

 dict(alias=["CFA London", "CFA UK salary", "CFA vs IMC"], code="uk", cc="UK", name="the United Kingdom", short="the UK", adj="British", cur="GBP", sym="£", rate=0.76192, fmt="{:,.0f}",
      photo="city-of-london", demonym="UK",
      cities_n=13, cities="13 cities: London, Birmingham, Manchester, Leeds, Liverpool, Newcastle, Bristol, Southampton, Peterborough, Cardiff, Edinburgh, Glasgow and Belfast",
      sal=("£61,000", 61000, "210", "March 2026"),
      intro="London is Europe's largest asset-management centre, and the charter is commonly listed in its buy-side job adverts. UK candidates often pair it with the Investment Management Certificate (IMC), the entry-level exam many firms ask graduates to pass.",
      employers=[("HSBC", "1,424"), ("Barclays", "643"), ("Standard Chartered", "474"), ("Schroders", "457")],
      emp_note="Global firms with large London offices, such as BlackRock, JPMorgan, UBS and Goldman Sachs, are among the biggest employers of charterholders worldwide.",
      recog=["**Academic level.** UK NARIC (now Ecctis) benchmarked the CFA charter and Level III at Level 7 of the UK framework, the level of a master's degree. Level II is benchmarked at Level 6 (bachelor's) and Level I at Level 5.",
             "**FCA qualification routes.** For retail investment advice, the FCA recognises routes that combine the CFA with the Investment Management Certificate (IMC), sometimes with gap-fill study; check the FCA's current list of appropriate qualifications for your role.",
             "**Employers.** London buy-side firms often list the charter as preferred for analyst and portfolio roles; many pay for the exams."],
      society="CFA Society United Kingdom (CFA UK) is one of the largest societies in the world. It runs the IMC exam, career events and continuing education in London and online.",
      extra=("CFA or IMC first?", "If you are starting in a UK investment firm, your employer may ask for the IMC first because it covers UK regulation. The IMC is shorter and cheaper; the charter is far broader and globally portable. Many people do the IMC in their first year, then start Level I."),
      faq=[("Is the CFA equivalent to a master's degree in the UK?", "Ecctis (formerly UK NARIC) benchmarks the charter at Level 7, comparable to a master's degree. That is an academic comparison, not a degree: universities decide for themselves whether to give credit."),
           ("Where can I sit the CFA exam in the UK?", "In 13 cities including London, Manchester, Birmingham, Edinburgh, Glasgow, Cardiff and Belfast.")],
      srcs=[("CFA Institute: Ecctis benchmarks the CFA charter (2022)", "https://www.cfainstitute.org/about/press-releases/2022/ecctis-benchmarks-the-cfa-charter")]),

 dict(alias=["CFA Canada portfolio manager", "CFA Toronto"], code="canada", cc="CA", name="Canada", short="Canada", adj="Canadian", cur="CAD", sym="C$", rate=1.4307, fmt="{:,.0f}",
      photo=None, demonym="Canadian",
      cities_n=15, cities="15 cities: Toronto, Montreal, Vancouver, Calgary, Edmonton, Ottawa, Winnipeg, Halifax, Hamilton, London (Ontario), Quebec City, Regina, Saskatoon, St. John's and Victoria",
      sal=("C$89,000", 89000, "328", "April 2026"),
      intro="Canada has one of the largest charterholder communities in the world, and its banks and pension funds are among the largest employers of charterholders in the world. The charter also has a formal place in Canadian securities rules: it is one of the main routes to registering as a portfolio manager.",
      employers=[("RBC", "2,532"), ("TD", "1,481"), ("BMO Financial Group", "1,213"), ("CIBC", "1,071"), ("Scotiabank", "1,028"), ("Manulife", "626"), ("Sun Life", "515"), ("National Bank of Canada", "508"), ("Desjardins", "355")],
      emp_note="RBC employs more charterholders than any company in the world except JPMorgan Chase, and all five big Canadian banks are in the global top 16. Pension managers such as CPP Investments, Ontario Teachers' and the Caisse in Quebec are major employers too.",
      recog=["**Portfolio manager registration.** Under the national registration rules, an advising representative (portfolio management) qualifies with the CFA charter plus 12 months of relevant investment management experience in the previous 36 months. An associate advising representative qualifies with Level I passed plus 24 months of experience. The Canadian Investment Manager (CIM) designation is the main alternative route.",
             "**Quebec tax credit.** CFA Institute is a recognised educational institution for Revenu Québec, so Quebec residents may be able to claim a tax credit for exam fees.",
             "**Provincial rules differ in detail.** Check with your provincial securities commission before relying on a route."],
      society="CFA Societies Canada brings together the local societies, including CFA Society Toronto (one of the largest in the world), CFA Society Vancouver, CFA Montréal, CFA Society Calgary, CFA Society Edmonton, CFA Society Ottawa and others.",
      extra=("Fees in Canadian dollars", "CFA Institute charges in US dollars, so the Canadian-dollar cost moves with the exchange rate. Your card issuer will also add a foreign-currency fee unless your card has none."),
      faq=[("Do I need the CFA to be a portfolio manager in Canada?", "Not strictly: the CIM designation with more experience is the other main route. But the charter plus 12 months of relevant experience is the most common way to register as an advising representative."),
           ("Which Canadian employers hire the most charterholders?", "RBC, TD, BMO, CIBC and Scotiabank, then insurers such as Manulife and Sun Life, according to CFA Institute's 2025 employer list.")],
      srcs=[("AMF (Quebec): portfolio management proficiency requirements", "https://lautorite.qc.ca/en/becoming-a-professional/securities/portfolio-management")]),

 dict(alias=["CFA fees in rupees", "CFA course India", "CFA exam centres India", "CFA vs CA India"], code="india", cc="IN", name="India", short="India", adj="Indian", cur="INR", sym="₹", rate=92.68, fmt="{:,.0f}",
      photo=None, demonym="Indian",
      cities_n=30, cities="30 cities, from Mumbai, New Delhi, Bengaluru, Hyderabad, Chennai, Kolkata and Pune to Ahmedabad, Jaipur, Lucknow, Kochi, Indore, Guwahati, Surat and Visakhapatnam",
      sal=("₹10 lakh", 1000000, "394", "March 2026"),
      intro="India is one of the CFA Program's largest and fastest-growing markets. Candidates come from commerce, engineering and chartered accountancy, and many work in Mumbai's asset managers and brokers or in the research, valuation and analytics centres of global banks in Bengaluru, Hyderabad, Gurugram and Pune.",
      employers=[],
      emp_note="Global banks and the Big Four run large research, risk and valuation teams in India; worldwide, EY, PwC, Deloitte and KPMG together employ about 4,000 charterholders. In CFA Institute's India talent report, 54% of employers said they seek candidates who combine an MBA with the CFA charter.",
      recog=["**No regulator waiver.** SEBI's qualification rules for investment advisers and research analysts are met through a degree plus NISM certifications; the CFA charter does not replace the NISM exams.",
             "**Employers value it.** In CFA Institute's 2026 India study, charterholders awarded in 2024–2025 (about six years' experience on average) reported pay of about ₹32 lakh a year, and all charterholders about ₹67 lakh.",
             "**Exam access.** India has 30 test-centre cities, more than any country except the United States and mainland China."],
      society="CFA Society India is based in Mumbai and runs events, study support and the Research Challenge across the country.",
      extra=("What the fees mean in rupees", "At early registration the three exams cost about ₹3.3 lakh at today's rate, before study materials. Card payments in dollars add a foreign-currency markup, and banks may add tax on foreign card spending, so check the final charge with your bank. The Access Scholarship (below) is worth applying for if the fees are a stretch."),
      faq=[("Is the CFA recognised in India?", "Employers recognise it widely, especially in asset management, equity research, investment banking and risk. It is not a legal licence: SEBI-registered advisers and analysts still need NISM certifications."),
           ("Where are CFA exam centres in India?", "In 30 cities, including Mumbai, New Delhi, Noida, Gurugram, Bengaluru, Hyderabad, Chennai, Kolkata, Pune, Ahmedabad and Jaipur.")],
      srcs=[("CFA Institute: India talent report", "https://www.cfainstitute.org/sites/default/files/india-talent-report.pdf"),
            ("CFA Institute: impact study, India 2026", "https://www.cfainstitute.org/programs/cfa-program/impact-assessment-india")]),

 dict(alias=["CFA Deutschland", "CFA Frankfurt"], code="germany", cc="DE", name="Germany", short="Germany", adj="German", cur="EUR", sym="€", rate=0.90992, fmt="{:,.0f}",
      photo="frankfurt-bridge", demonym="German",
      cities_n=6, cities="six cities: Frankfurt, Munich, Berlin, Hamburg, Düsseldorf and Stuttgart",
      sal=("€76,000", 76000, "52", "September 2025"),
      intro="In Germany the charter is most useful in Frankfurt and Munich: at asset managers, banks, insurers, index and data providers, and the central banks in Frankfurt. It is an English-language qualification in a market where much of the work is done in German, so it signals international readiness as well as technical depth.",
      employers=[("Allianz (including PIMCO and Allianz Global Investors)", "1,011"), ("Deutsche Bank (including DWS)", "759")],
      emp_note="Insurers, savings and cooperative bank groups, index and data providers, and the ECB and Bundesbank also employ charterholders in Frankfurt.",
      recog=["**No general licence.** German rules for investment advisers (the Sachkunde requirement) set out their own accepted qualifications and experience; check with your employer's compliance team whether the charter counts for your role.",
             "**Deutsche Börse.** CFA Institute's recognition fact card lists Deutsche Börse accepting a pass at Level III as meeting the professional requirement to be an exchange trader.",
             "**Employers.** Frankfurt asset managers and banks often name the charter as preferred for portfolio management and research."],
      society="CFA Society Germany is based in Frankfurt and runs events, study support and continuing education in German and English.",
      extra=("Studying alongside a German job", "Most German candidates study alongside full-time work. Plan around the summer holiday and Christmas, and consider the August or November windows, which leave room for a quieter study period beforehand."),
      faq=[("Is the CFA recognised in Germany?", "It is widely known among asset managers, banks and insurers, especially in Frankfurt and Munich, but it is not a legal licence for retail investment advice."),
           ("Where can I take the CFA exam in Germany?", "In Frankfurt, Munich, Berlin, Hamburg, Düsseldorf and Stuttgart.")],
      srcs=[]),

 dict(alias=["CFA Dubai", "CFA Abu Dhabi", "CFA UAE recognition"], code="uae", cc="AE", name="the United Arab Emirates", short="the UAE", adj="Emirati", cur="AED", sym="AED ", rate=3.6725, fmt="{:,.0f}",
      photo=None, demonym="UAE",
      cities_n=2, cities="Dubai and Abu Dhabi",
      sal=("AED 175,000", 175000, "113", "September 2025"),
      intro="The UAE has become one of the fastest-growing places to hold the charter. Sovereign wealth funds and government-related investors in Abu Dhabi, banks and family offices across the country, and the asset managers in the Dubai International Financial Centre (DIFC) and Abu Dhabi Global Market (ADGM) all hire for investment roles where the charter is valued.",
      employers=[],
      emp_note="Sovereign wealth funds, government-related investors, banks, family offices and international asset managers in the DIFC and ADGM are the main employers. Packages often add housing and schooling allowances, and there is no personal income tax.",
      recog=["**Licensing equivalence (new in 2026).** On 8 October 2026 the UAE Capital Market Authority (formerly the Securities and Commodities Authority) approved recognising the CFA Program as equivalent to licensing exams from the Chartered Institute for Securities & Investment (CISI): Level I to CISI's Fundamentals of Financial Services and Global Securities Operations, Level II to the International Certificate in Wealth Management, and Level III (Private Markets pathway) to the Corporate Finance Technical Foundation and ICWIM Level 3.",
             "**Free zones.** The DIFC (regulated by the DFSA) and ADGM (regulated by the FSRA) set their own competence rules; check them for your role.",
             "**Employers.** Many investment roles in Abu Dhabi and Dubai list the charter as required or preferred."],
      society="CFA Society Emirates runs events, study support and continuing education in Dubai and Abu Dhabi.",
      extra=("Fees in dirhams", "Because the dirham is pegged to the US dollar at 3.6725, the dirham cost of the exams only changes when CFA Institute changes its fees."),
      faq=[("Is the CFA recognised in the UAE?", "Yes. In October 2026 the UAE Capital Market Authority approved treating CFA Program levels as equivalent to specific CISI licensing exams used in UAE licensing, and many employers list the charter in job adverts."),
           ("What is the CFA salary in Dubai?", "The average base salary reported by people with the CFA is about AED 175,000, before allowances. Housing and schooling allowances and the absence of income tax make packages larger than the base suggests.")],
      srcs=[("CFA Institute: UAE Capital Market Authority recognition", "https://www.cfainstitute.org/programs/cfa-program/cfa-program-uae-cma-recognition")]),

 dict(alias=["CFA Pakistan fees in PKR", "CFA Karachi", "CFA Lahore"], code="pakistan", cc="PK", name="Pakistan", short="Pakistan", adj="Pakistani", cur="PKR", sym="Rs ", rate=276.6, fmt="{:,.0f}",
      photo=None, demonym="Pakistani",
      cities_n=4, cities="four cities: Karachi, Lahore, Islamabad and Multan",
      sal=("Rs 1.0 million", 1000000, "42 (a small sample)", "July 2026"),
      intro="In Pakistan the charter is a strong signal precisely because it is still rare. Charterholders work in Karachi's asset management companies, brokerages and banks, at the Pakistan Stock Exchange and regulators, and increasingly for Gulf employers who recruit from Pakistan.",
      employers=[],
      emp_note="Asset management companies, commercial and investment banks, brokerages, insurers and development finance institutions are the main employers. Many Pakistani charterholders build careers in the Gulf, where the charter carries over directly.",
      recog=["**SECP research analyst exemption.** The Securities and Exchange Commission of Pakistan exempts charterholders from the mandatory research analyst certification, provided they pass the Pakistan Market Regulations (PMR) certification.",
             "**Employers.** Asset management companies and brokerages frequently list the charter or progress in the program in job adverts."],
      society="CFA Society Pakistan, based in Karachi with activity in Lahore and Islamabad, has been active for more than 20 years. It works with the SECP and runs charter award ceremonies, events and scholarships.",
      extra=("Fees in rupees", "At about Rs 276.6 per dollar, Level I at early registration costs about Rs 315,000. That is close to four months of the average base salary reported by people with the CFA in Pakistan, which is why the Access Scholarship matters so much here."),
      faq=[
           ("Where can I take the CFA exam in Pakistan?", "In Karachi, Lahore, Islamabad and Multan.")],
      srcs=[("CFA Society Pakistan: exemptions and waivers", "https://cfasociety.org/pakistan/society-news-resources/advocacy/regulator-outreach"),
            ("ARY News: US dollar closes at Rs 276.65 (November 2026)", "https://arynews.tv/us-dollar-closes-at-rs276-65-as-sbp-issues-m2m-rates")]),

 dict(alias=["CFA fees in naira", "CFA Lagos", "CFA Abuja"], code="nigeria", cc="NG", name="Nigeria", short="Nigeria", adj="Nigerian", cur="NGN", sym="₦", rate=1363.0, fmt="{:,.0f}",
      photo=None, demonym="Nigerian",
      cities_n=2, cities="Lagos and Abuja",
      sal=("₦6 million", 6000000, "36 (a small sample)", "October 2023"),
      intro="Nigeria has one of the fastest-growing CFA communities in Africa. The exams were first held in the country in June 2018, when about 870 candidates sat them in Lagos, and computer-based testing now runs in Lagos and Abuja. Charterholders work in asset management, pension fund administration, banking, stockbroking and private equity.",
      employers=[("Access (Access Holdings group)", "82 candidates, 11 charterholders")],
      emp_note="In CFA Society Nigeria's membership data (June 2026), Access employed the most CFA candidates in Nigeria and the second-largest number of charterholders. Pension fund administrators, asset managers, the large commercial banks and investment banks are the other main employers.",
      recog=["**No regulator waiver.** Nigerian regulators do not waive licensing requirements for charterholders, but CFA Society Nigeria works with the CBN, SEC, PenCom, NAICOM and NDIC on investor education and professional standards.",
             "**Employers.** Asset managers, pension fund administrators and banks value the charter for investment and research roles."],
      society="CFA Society Nigeria was founded in 2013. It runs the Research Challenge, an Ethics Challenge, investment conferences and a weekly financial literacy radio show, Money Talks.",
      extra=("Fees in naira", "The naira has moved sharply since 2023, so the naira cost of the exams changes from month to month. At about ₦1,363 per dollar (the official market rate in mid-November 2026), Level I at early registration costs about ₦1.55 million. Check whether your bank card supports dollar payments and what rate it applies."),
      faq=[("Where can I take the CFA exam in Nigeria?", "In Lagos and Abuja.")],
      srcs=[("Nairametrics: about 900 sit the first CFA exams in Nigeria (2018)", "https://nairametrics.com/2018/06/24/about-900-students-sit-for-first-ever-cfa-exams-in-nigeria/"),
            ("CFA Society Nigeria: who we are", "https://www.cfasociety.org/nigeria/who-we-are"),
            ("Arise News: Access leads Nigeria's employers of CFA candidates (2026)", "https://www.arise.tv/access-leads-nigerias-employers-of-cfa-candidates-ranks-second-for-charterholders/"),
            ("WithinNigeria: dollar to naira, 19 November 2026", "https://www.withinnigeria.com/2026/11/19/dollar-to-naira-today-november-19-2026-official-nfem-and-cbn-rate-near-%E2%82%A61363-as-black-market-climbs-to-%E2%82%A61460/?amp=1")]),

 dict(alias=["CFA Singapore CMFAS", "CFA Singapore salary"], code="singapore", cc="SG", name="Singapore", short="Singapore", adj="Singaporean", cur="SGD", sym="S$", rate=1.2884, fmt="{:,.0f}",
      photo="marina-bay", demonym="Singapore",
      cities_n=1, cities="Singapore",
      sal=("S$115,000", 115000, "131", "July 2025"),
      intro="Singapore is one of Asia's two big asset-management centres, home to regional headquarters of global managers, two state investors (GIC and Temasek) and a fast-growing wealth management industry. The charter is common among its investment professionals and expected in many buy-side roles.",
      employers=[("DBS", "305")],
      emp_note="DBS is the Singapore-headquartered bank with the most charterholders in CFA Institute's 2025 list. Global managers with regional hubs in Singapore, the state investors and private banks are major employers too.",
      recog=["**CMFAS modules.** CFA Institute's recognition fact card lists an exemption from several Capital Markets and Financial Advisory Services (CMFAS) exam modules for charterholders seeking a licence as a fund manager or financial adviser representative. MAS revised its competency rules from April 2024, so confirm the current position with MAS or your employer's compliance team.",
             "**Employers.** Asset managers, private banks and the state investors often list the charter as preferred or required for investment roles."],
      society="CFA Society Singapore runs events, career support and continuing education.",
      extra=("Bonuses matter", "In Singapore a large part of investment pay comes as a bonus; a typical portfolio manager's bonus is a quarter to a third of base pay. Compare total compensation, not base salary alone."),
      faq=[("Does the CFA exempt me from CMFAS exams?", "CFA Institute lists exemptions from several CMFAS modules for charterholders, but MAS changed its competency framework in 2024. Check the current MAS notice for your licence type before relying on an exemption."),
           ("What is the CFA salary in Singapore?", "The average base salary reported by people with the CFA is about S$115,000, before bonuses.")],
      srcs=[]),

 dict(alias=["CFA HK", "CFA SFC licensing"], code="hong-kong", cc="HK", name="Hong Kong", short="Hong Kong", adj="Hong Kong", cur="HKD", sym="HK$", rate=7.8389, fmt="{:,.0f}",
      photo="hk-harbour", demonym="Hong Kong",
      cities_n=1, cities="Hong Kong",
      sal=("HK$796,000", 796000, "78", "October 2025"),
      intro="Hong Kong has one of Asia's largest communities of charterholders. It is the gateway for international money into mainland China and home to the Asian headquarters of many global banks and asset managers.",
      employers=[("HSBC", "1,424 worldwide"), ("Standard Chartered", "474 worldwide")],
      emp_note="Global banks and asset managers with Asian headquarters in Hong Kong, mainland Chinese securities firms and fund houses, and private banks are the main employers.",
      recog=["**SFC licensing.** CFA Institute's recognition fact card lists the Securities and Futures Commission recognising Level I as a recognised industry qualification for licensed representatives, with some licensing exam papers waived, and the charter as a recognised professional qualification for responsible officers. Confirm the details in the SFC's current Guidelines on Competence.",
             "**Employers.** Many asset-management and research roles list the charter as required or preferred."],
      society="CFA Society Hong Kong is one of the largest and most active societies in Asia.",
      extra=("The dollar peg", "The Hong Kong dollar trades in a narrow band around 7.8 per US dollar, so the local cost of the exams barely changes."),
      faq=[("Does the CFA help with SFC licensing?", "CFA Institute lists Level I as a recognised industry qualification for SFC licensed representatives and the charter as a recognised qualification for responsible officers. Check the SFC's current Guidelines on Competence for your licence type."),
           ("What is the CFA salary in Hong Kong?", "The average base salary reported by people with the CFA is about HK$796,000, before bonuses, which are a large part of pay in Hong Kong.")],
      srcs=[("SFC: Guidelines on Competence", "https://sfc.hk/en/Rules-and-standards/Codes-and-guidelines/Guidelines/guidelines-on-competence")]),

 dict(alias=["CFA China exam centres", "CFA Shanghai", "CFA Beijing"], code="china", cc="CN", name="mainland China", short="mainland China", adj="Chinese", cur="CNY", sym="¥", rate=6.6777, fmt="{:,.0f}",
      photo=None, demonym="Chinese",
      cities_n=34, cities="34 cities, including Beijing, Shanghai, Shenzhen, Guangzhou, Hangzhou, Nanjing, Chengdu, Wuhan, Xi'an, Tianjin, Suzhou and Xiamen",
      sal=("¥300,000", 300000, "15 (a very small sample)", "April 2023"),
      intro="Mainland China became one of the CFA Program's largest sources of candidates in the 2010s, and CFA Institute opened its first mainland office in 2015. Candidates work at securities firms, fund houses, banks and insurers, and many study while at university.",
      employers=[("Bank of China", "509"), ("ICBC", "387"), ("China Merchants", "357")],
      emp_note="Bank of China, ICBC and China Merchants are the mainland-headquartered groups in CFA Institute's 2025 list of firms with 300 or more charterholders. Securities firms and fund management companies in Shanghai, Beijing and Shenzhen are the other major employers.",
      recog=["**No regulator waiver.** Chinese licensing exams for securities and fund practitioners are separate; the charter does not replace them.",
             "**Employers.** Large financial groups, securities firms and fund houses value the charter for research and investment roles."],
      society="There are CFA societies in Beijing, Shanghai and Shenzhen (the Shenzhen society was launched in 2017).",
      extra=("Paying the fees", "Fees are charged in US dollars, so pay with a card that supports international payments, and check your bank's limits on foreign-currency spending before registration day."),
      faq=[("Where can I take the CFA exam in China?", "In 34 mainland cities, including Beijing, Shanghai, Shenzhen, Guangzhou, Hangzhou, Nanjing, Chengdu and Wuhan."),
           ("Is the CFA useful in China?", "Yes for investment careers at securities firms, fund houses, banks and insurers, and for roles with international firms. It does not replace Chinese practitioner licensing exams.")],
      srcs=[("Advisor.ca: for the first time, China fields the most CFA hopefuls", "https://www.advisor.ca/practice/planning-and-advice/for-the-first-time-china-fields-the-most-cfa-hopefuls/"), ("CFA Institute: launch of CFA Society Shenzhen (2017)", "https://www.cfainstitute.org/about/press-room/2017/cfa-institute-builds-on-its-long-term-commitment-to-china-with-launch-of-cfa-society-shenzhen"),
            ("CFA Institute: first China office (2015)", "https://www.cfainstitute.org/about/press-room/2015/cfa-institute-opens-first-china-office")]),

 dict(alias=["CFA Sydney", "CFA Melbourne"], code="australia", cc="AU", name="Australia", short="Australia", adj="Australian", cur="AUD", sym="A$", rate=1.5002, fmt="{:,.0f}",
      photo=None, demonym="Australian",
      cities_n=7, cities="seven cities: Sydney, Melbourne, Brisbane, Perth, Adelaide, Canberra and Hobart",
      sal=("A$119,000", 119000, "116", "November 2025"),
      intro="Australia's compulsory superannuation system has built one of the world's largest pools of pension assets, and the funds and asset managers that invest it, mostly in Sydney and Melbourne, are the main employers of charterholders.",
      employers=[("Macquarie", "388")],
      emp_note="Macquarie is the Australian-headquartered firm with the most charterholders in CFA Institute's 2025 list. Superannuation funds, asset managers and the big four banks are the other major employers.",
      recog=["**Financial advice.** CFA Institute's fact card describes a route combining Level I with RG 146 gap training for retail financial advice. Australia replaced RG 146 with new education standards for advisers in 2019, so check ASIC's current requirements and approved qualifications.",
             "**Employers.** Super funds and asset managers often list the charter as preferred for investment roles."],
      society="CFA Societies Australia runs events and continuing education across the major cities.",
      extra=("Fees in Australian dollars", "Fees are charged in US dollars, so the Australian-dollar cost moves with the exchange rate."),
      faq=[("Where can I take the CFA exam in Australia?", "In Sydney, Melbourne, Brisbane, Perth, Adelaide, Canberra and Hobart."),
           ("What is the CFA salary in Australia?", "The average base salary reported by people with the CFA is about A$119,000, before bonuses and superannuation contributions.")],
      srcs=[])]


def money(c, usd):
    v = usd * c["rate"]
    if c["cur"] == "INR":
        return f"₹{v / 1e5:,.2f} lakh"
    if c["cur"] in ("NGN",) and v >= 1e6:
        return f"₦{v / 1e6:,.2f} million"
    step = 10 if v < 10000 else (100 if v < 1e6 else 1000)
    return c["sym"] + f"{round(v / step) * step:,.0f}"


def page(c, order):
    n = c["name"]; N = n
    e3 = sum(f[0] for f in FEES.values()); s3 = sum(f[1] for f in FEES.values())
    fee_rows = "\n".join(f"| Level {lv} | USD {e:,} | {money(c, e)} | USD {s:,} | {money(c, s)} |" for lv, (e, s) in FEES.items())
    weeks = e3 * c["rate"] / c["sal"][1] * 52
    sal_local, sal_num, sal_n, sal_date = c["sal"]
    usd_sal = sal_num / c["rate"]
    emp = ""
    if c["employers"]:
        emp = "\n".join(f"- **{a}**: {b}" + ("" if "candidates" in b or "worldwide" in b else " charterholders") for a, b in c["employers"]) + "\n\n"
    title = f"CFA in {c['short']}: exam centres, fees in {c['cur']}, salary and recognition"
    summary = (f"Where to sit the CFA exams in {n}, what they cost in {c['cur']}, what people with the CFA earn there, "
               f"which employers hire them and how local regulators treat the charter. Checked 22 November 2026.")
    short = c["short"]
    base = short.replace("the ", "")
    tags = [f"CFA in {base}", f"CFA {base}", f"CFA exam fees {base}", f"CFA fees in {c['cur']}", f"CFA exam centres in {base}",
            f"CFA salary in {base}", f"is CFA recognised in {base}", f"CFA Society {base}"] + c.get("alias", [])
    tags = list(dict.fromkeys(tags))
    faqs = [(f"How much does the CFA cost in {short}?", f"At early registration Level I costs USD 1,140, about {money(c, 1140)}, and all three levels USD 3,520, about {money(c, e3)} at November 2026 exchange rates. Standard registration costs more: USD 4,570 in total. Study materials are extra.")] + c["faq"]
    if c["cur"] == "USD":
        faqs[0] = ("How much does the CFA cost in the US?", "USD 1,140 for Level I or II and USD 1,240 for Level III at early registration, USD 3,520 for all three. At the standard rate the total is USD 4,570. Study materials are extra.")
    faqs.append(("Can I get a scholarship for the CFA exams?", f"Yes. CFA Institute's Access Scholarship cuts the exam fee to USD 400 for candidates who need financial help. Applications open four times a year; the window for the November 2027 exams opens on 9 February 2027."))
    faq_md = "\n\n".join(f"### {q}\n\n{a}" for q, a in faqs)
    srcs = [("CFA Institute: dates and fees", FEESRC), ("CFA Institute: test centre locations by country (planned list)", CITIES),
            ("CFA Institute: top employers of charterholders (2025)", TOP_EMP), ("CFA Institute: regulator and program recognition", RPR),
            ("CFA Institute: recognition fact card", FACTCARD), ("CFA Institute: Access Scholarship", ACCESS),
            (f"PayScale: CFA salary, {short} (retrieved 16 November 2026)", PAYSCALE.format(cc=c["cc"]))]
    if c["cur"] not in ("USD", "AED", "PKR", "NGN"):
        srcs.append(("European Central Bank reference rates via Frankfurter, 20 November 2026", "https://api.frankfurter.dev/v1/latest?from=USD"))
    srcs += c["srcs"]
    src_md = "\n".join(f"- [{a}]({b})" for a, b in srcs)
    RD = {"AED": "the fixed peg of AED 3.6725 per US dollar", "PKR": "about Rs 276.6 per US dollar (interbank rate, November 2026)",
          "NGN": "about ₦1,363 per US dollar (official market rate, 19 November 2026)"}
    fx = "" if c["cur"] == "USD" else f"Local amounts use {RD.get(c['cur'], RATE_NOTE + f' (1 USD = {c[chr(114) + chr(97) + chr(116) + chr(101)]:g} {c[chr(99) + chr(117) + chr(114)]})')} and are rounded."
    weeks_txt = ("Salary data for Nigeria predate the naira's fall, so we do not compare fees with pay there" if c["cur"] == "NGN" else f"At early registration, the three exams together cost about **{weeks:.0f} weeks** of the average base salary reported by people with the CFA in {short}"
                 if weeks < 26 else f"At early registration, the three exams together cost about **{weeks / 4.33:.0f} months** of the average base salary reported by people with the CFA in {short}")
    body = f"""{c['intro']}

[[figure]]

## Where to take the CFA exams in {N}

The exams are computer-based and run at Prometric test centres. CFA Institute's planned list names {c['cities']}. You choose a centre and a time when you schedule, after registering; popular centres fill up, so schedule as soon as your window opens. You need a valid international passport, and the name on it must match your CFA account exactly.

## What the CFA costs in {c['cur']}

CFA Institute charges the same US-dollar fees everywhere. {fx}

| Exam | Early (USD) | Early ({c['cur']}) | Standard (USD) | Standard ({c['cur']}) |
|---|---|---|---|---|
{fee_rows}
| **All three levels** | **USD {e3:,}** | **{money(c, e3)}** | **USD {s3:,}** | **{money(c, s3)}** |

- There is **no enrolment fee** any more; it was abolished in April 2025.
- Rescheduling within your window costs **USD 250**. From February 2027 the paid deferral option ends: if you miss an exam you lose the fee.
- Study materials come on top: CFA Institute's own curriculum is included with registration, while third-party courses cost anywhere from a few hundred to a couple of thousand dollars per level.
- {weeks_txt}.

See [2027 exam dates and fees](cfa-dates-fees.html) for every window and deadline, and [the total cost of the CFA](blog-cfa-total-cost.html) for materials and retakes.

## What people with the CFA earn in {N}

The average base salary reported to PayScale by people who list the CFA in {short} is **{sal_local}** a year (about US${usd_sal / 1000:,.0f},000), based on {sal_n} profiles, last updated {sal_date}. That group mixes charterholders with candidates and juniors with seniors, so treat it as a typical figure, not a charterholder's ceiling. Bonuses come on top.

Compare it with [CFA salaries in 19 countries](blog-cfa-salary.html) and [pay by job](blog-cfa-jobs-salaries.html).

## Who hires charterholders in {N}

{emp}{c['emp_note']}

CFA Institute's employer figures are self-reported by charterholders and count people worldwide, not only in {short}.

## How the charter is recognised in {N}

{chr(10).join('- ' + r for r in c['recog'])}

Rules change. Before you rely on any exemption, confirm it with the regulator or your employer's compliance team.

## The local CFA society

{c['society']} Membership is open to charterholders and, as affiliate or candidate members in many societies, to people still working through the exams.

## {c['extra'][0]}

{c['extra'][1]}

## Scholarships

CFA Institute's **Access Scholarship** reduces the exam fee to **USD 400** for candidates with financial need. It opens four times a year for about three weeks. The window for the **November 2027** exams opens on **9 February 2027** and closes on 2 March 2027. Universities that are CFA Institute affiliates also receive student scholarships to distribute.

## Questions people ask

{faq_md}

## Sources

{src_md}
"""
    fm = {"title": title, "slug": f"cfa-in-{c['code']}", "order": str(order), "summary": summary,
          "figure": f"country_{c['code'].replace('-', '_')}",
          "caption": f"The exam fees in {c['cur']} at early and standard registration, at November 2026 exchange rates.",
          "tags": ", ".join(tags), "updated": UPDATED}
    if c["photo"]:
        fm["photo"] = c["photo"]
    head = "\n".join(f"{k}: {v}" for k, v in fm.items())
    return f"---\n{head}\n---\n{body}"


def figure_data():
    return {f"country_{c['code'].replace('-', '_')}": dict(name=c["short"], cur=c["cur"], rate=c["rate"], fees=FEES,
            labels={lv: (money(c, e), money(c, s)) for lv, (e, s) in FEES.items()}) for c in C}


if __name__ == "__main__":
    out = ROOT / "content" / "country"
    out.mkdir(parents=True, exist_ok=True)
    for i, c in enumerate(C):
        (out / f"{i + 1:02d}-{c['code']}.md").write_text(page(c, i + 1), encoding="utf-8")
    (ROOT / "data" / "country_figs.json").write_text(json.dumps(figure_data(), ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", len(C), "country pages")
