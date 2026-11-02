# Monetization, Unit Economics and Go-to-Market for a Pakistan Fund Comparison/Analytics Product (as of Nov 2026)

Research date: 2 November 2026. Scope note: the work was capped at about 17 tool calls, so several sub-questions (B2B price points, CAC, churn, payment rails, sponsored-content rates) remain open and are listed under Gaps. Figures are labelled **[Verified]** when a cited source states them directly, and **[Estimate]** when they come from my own arithmetic or assumptions. FX assumption used for USD conversions: **~PKR 280/USD** [Estimate; not sourced in this session, approximate 2025–26 level].

---

## 1. Distribution economics in Pakistan (loads, fees, distributor share, SECP caps)

### Takeaway
SECP now caps **management fees** by category instead of TER, effective 1 July 2025: equity 3.00%, income 1.50%, money market 1.25% and ETF/index 0.75%. Front-end (sales) loads are capped at 3%, and none may be charged when an investor goes direct to the AMC. AMCs pay distributors out of the load and/or their own resources. I found no public figure for the trail percentage, so annual distributor income per PKR 1m of AUM can only be estimated. It is roughly PKR 2,500–15,000/yr depending on category and share. One-time loads on new money add PKR 7,500–25,000 per PKR 1m.

### Cited Findings
- **[Verified] Management fee caps for CIS, effective 1 Jul 2025** (article dated 16 Apr 2025): Equity 3.00%; Income and Aggressive Income 1.50%; Commodities 1.50%; Money Market 1.25%; Fixed Rate/Return 1.00%; ETF and Index 0.75%; Hybrid uses a weighted average; a Fund of Funds charges no management fee when it invests in the same AMC's schemes. These caps replace the old TER-cap regime, and AMCs must still disclose TER in detail — [Business Recorder, 16 Apr 2025](https://www.brecorder.com/news/40357852/amcs-pfms-secp-replaces-ter-capping-regime-with-caps-on-management-fees-wef-july-1)
- **[Verified] Pension fund (VPS) management fee caps:** Equity sub-fund 2.50%; Equity Index 0.75%; Money Market 1.00%; Debt 1.25%; Commodity 1.50% — [Business Recorder, 16 Apr 2025](https://www.brecorder.com/news/40357852/amcs-pfms-secp-replaces-ter-capping-regime-with-caps-on-management-fees-wef-july-1)
- **[Verified] Draft amendments notified 15 Jan 2025 for 1 Jul 2025:** reimbursement of indirect expenses from mutual funds is disallowed; a Market Development Fund is proposed for investor education; there is a digital roadmap and simpler onboarding — [Profit, 7 Feb 2025](https://profit.pakistantoday.com.pk/2025/02/07/secp-to-introduce-new-cost-reforms-in-mutual-funds-from-july-2025)
- **[Verified] Sales load cap:** SECP cut the maximum sales load from 5% to 3% (Circular 26 of 2015). No sales load may be charged when an investor applies directly to the AMC — [SECP press release](https://www.secp.gov.pk/wp-content/uploads/2016/05/SECP-caps-sales-load-on-mutual-funds-at-3.pdf)
- **[Reported proposal, not confirmed final]** In Aug 2024 SECP was reported to be seeking lower overall fees. A draft reportedly removes front-end loads and adds a one-time PKR 150 onboarding charge. I saw only the lede, which is behind a paywall, and could not confirm the proposal became final — [IFN Investor, 5 Aug 2024](https://ifninvestor.com/pakistan-cutting-fees-to-boost-mutual-pension-funds/)
- **[Verified] Distributor remuneration mechanics (Al Meezan offering documents):** the AMC pays distributors from its own resources, from the sales load, or both, and distributors must be MUFAP-registered. Front-end load differs by channel: direct with the AMC is 0–1% (0–2% in an older document), while a "digital platform / third party" can charge up to 1.5% — [Meezan Government Securities Fund OD, Mar 2026](https://www.almeezangroup.com/assets/uploads/2026/03/Meezan-Government-Securities-Fund-Offering-Document.pdf); [MGF Consolidated OD, 2023](https://www.almeezangroup.com/assets/uploads/2023/03/MGF-Consolidated-Offering-Document.pdf)
- **[Verified] Bank channel loads (Standard Chartered Pakistan wealth page, undated):** equity fund front-end load 2.5%; money market and income funds 0.75–1%; asset allocation and pension funds 3% — [Standard Chartered Pakistan](https://www.sc.com/pk/wealth-solutions/invest/mutual-funds/)
- **[Opinion/anecdote]** Retail commentators say "up to 3%" front-end loads are common through bank branches. One recounts a branch manager declining to disclose his commission, which shows how opaque bank distribution is — [Black Iron Substack](https://blackiron.substack.com/p/mutual-funds-vs-etfs-how-to-save); [Munaafa Substack](https://munaafa.substack.com/p/dont-pay-front-end-load)
- **[Verified] Mahaana (digital AMC, YC-backed):** PACRA reports AUM of PKR 3,827m in Dec 2025, up from PKR 1,852m in Dec 2024, about 2.1x YoY. Mahaana's Islamic Index ETF (MIIETF) was reported near PKR 1.95bn in Aug 2026. Profit describes the model as AMCs earning a percentage of AUM — [PACRA](https://pacra.com/finalPr/MTU1NTc=); [PACRA earlier note](https://pacra.com/finalPr/MTQxNTY=); [Yespress, 2026](https://yespress.io/muhammad-tariq); [Profit, 23 Aug 2022](https://profit.pakistantoday.com.pk/2022/08/23/ycombinator-backed-mahaana-wealth-announces-2-1mn-pre-seed-raise-to-launch-digital-wealth-management-company-in-pakistan/)
- **[Verified] Mahaana's first fund** was the first launched under SECP's Digital AMC framework, in Apr 2023 — [ProPakistani, 27 Apr 2023](https://propakistani.pk/2023/04/27/first-fund-launched-under-digital-amc-framework-of-secp/amp/)
- **[Reported, internally inconsistent] Market depth:** the Tribune (Feb 2026, "Assets under mutual funds triple in three years") is cited as saying Pakistan has only about 250,000 individual investors, or "0.02% penetration". That percentage does not match the count: 250k / ~240m people ≈ 0.1%. The page returned 403, so I could not verify it — [Tribune, Feb 2026](https://tribune.com.pk/story/2587410/assets-under-mutual-funds-triple-in-three-years)

### Inferences
- **[Estimate] What a digital distributor could earn per PKR 1m of AUM per year.** No source gives a trail %, so I assume trail shares of 20–50% of the management fee:
  - Money market (cap 1.25%; actual fees are usually below the cap): 1,000,000 × 1.25% × 20–50% = **PKR 2,500–6,250/yr** at the cap. At an assumed actual fee of 0.75%, it is PKR 1,500–3,750/yr.
  - Income (cap 1.5%): 1,000,000 × 1.5% × 20–50% = **PKR 3,000–7,500/yr**.
  - Equity (cap 3%): 1,000,000 × 3% × 20–50% = **PKR 6,000–15,000/yr**.
  - One-time front-end load on new subscriptions, if the distributor keeps it, which applies only when the investor does not go direct: equity 2.5% gives **PKR 25,000**; money market/income 0.75–1% gives **PKR 7,500–10,000**; the Meezan digital/third-party channel at ≤1.5% gives ≤ PKR 15,000.
- **[Estimate] Break-even AUM for distribution-only revenue.** At an assumed MVP burn of ~PKR 650k/month (see section 6), annual cost is PKR 7.8m. With a blended trail of 0.25%, the required AUM is 7.8m / 0.0025 = **PKR 3.1bn**. At 0.5% it is **PKR 1.56bn**. For comparison, Mahaana, a full digital AMC earning the whole management fee, reached PKR 3.8bn about 3.5 years after its 2022 licensing. A pure distributor would need Mahaana-scale AUM at a fraction of the fee, which is hard as a standalone model.
- **[Estimate] Mahaana revenue scale.** PKR 3,827m × an assumed ~1% blended fee ≈ PKR 38m/yr, or about USD 137k. This shows how small AUM-based revenue is at current Pakistani digital scale.
- Market mix matters. Most retail AUM sits in money market/income funds, which have the lowest fee caps, so a comparison tool that routes investors to cash funds earns the least per rupee. That last claim rests on general knowledge and was not sourced here; see Gaps.
- The 2015 rule that direct-to-AMC investments carry no load creates channel conflict. A comparison tool that sends users to invest direct cannot earn the load unless it is a registered distributor with an agreement.

### Gaps
- No published Pakistani trail commission % or load-sharing ratio (AMC → bank/distributor) was found. These need AMC distribution agreements, MUFAP distributor rules or industry interviews.
- Could not confirm whether SECP actually eliminated front-end loads or introduced the PKR 150 onboarding fee after the 2024 draft. The current NBFC Regulations text was not retrieved.
- Actual (vs capped) management fees/TERs by category: monthly FMRs from MUFAP/AMCs (e.g., [Meezan FMR Jan 2025](https://www.almeezangroup.com/assets/uploads/2025/01/FMR-January-2025.pdf)) would give these but were not parsed.
- No figure was found for Mahaana's user count or its distribution partners' economics.
- The industry total AUM and category split for late 2026 were not retrieved.

---

## 2. Consumer subscription willingness to pay in Pakistan

### Takeaway
Global streaming anchors in Pakistan cost roughly PKR 150–1,900/month. Spotify is about PKR 299 individual and PKR 149 student. Netflix figures conflict, at roughly PKR 800–1,900. That suggests a consumer finance subscription has to sit near PKR 300–1,000/month. The paid "stock tips" WhatsApp market exists, but SECP and PSX repeatedly flag it as fraudulent, which hurts trust in paid tips and opens room for a regulated, transparent tool.

### Cited Findings
- **[Verified, undated source] Spotify Pakistan:** Individual PKR 299; Duo PKR 390; Family PKR 479; Student PKR 149 per month — [Brandsynario](https://www.brandsynario.com/entertainment/spotify-pakistan-prices-of-subscription-packages-have-been-revealed/). Spotify announced a global price increase in Aug 2025 that covered South Asia, but no updated PKR figures were found — [ProPakistani, 5 Aug 2025](https://propakistani.pk/2025/08/05/spotify-announces-global-price-increase/)
- **[Conflicting] Netflix Pakistan:** one source lists Basic PKR 800 / Standard 1,400 / Premium 1,900, while an older report lists Standard PKR 800 / Premium 1,100. In 2023 Pakistan had "the cheapest Netflix among 245 countries" — [Shapes FAQ](https://shapes.inc/netflixpriceinp/faq); [Bolnews](https://www.bolnews.com/?p=280038); [ProPakistani, 8 Mar 2023](https://propakistani.pk/2023/03/08/pakistan-has-the-cheapest-netflix-among-245-countries-report/)
- **[Weak] YouTube Premium:** a reseller site quotes a student price of PKR 229/month. A 2024 report expected a price hike — [ProPakistani, 23 Sep 2024](https://propakistani.pk/2024/09/23/youtube-premium-is-getting-a-price-hike/amp/)
- **[Verified] Paid stock-tip groups.** SECP warns that WhatsApp/social groups offer "insider tips" for **membership fees** and ask for transfers to private accounts. On 21 Nov 2025 it flagged the "TSL WEALTH" app and the "A103-Topline Stock Strategies Hub" group, which falsely used Topline Securities' name, and escalated the case to FIA, PTA and SBP. The Sep 2024 warnings targeted sham "investment training courses" that charge membership fees, and PSX issued a parallel alert — [SECP press release, Nov 2025](https://www.secp.gov.pk/wp-content/uploads/2025/11/Press-Release-SECP-Warns-Public-About-Illegal-Trading-Application-Misusing-Names-of-Licensed-Brokerage-Houses-and-Pictures-of-Celebrities-FinFluencers-and-Br.pdf); [Profit, 21 Nov 2025](https://profit.pakistantoday.com.pk/2025/11/21/secp-flags-illegal-trading-app-using-broker-names-and-celebrity-images-to-lure-investors/); [SECP press release, 3 Sep 2024](https://secp.gov.pk/wp-content/uploads/2024/09/Press-Release-Sep-3-SECP-Issues-public-warning.pdf); [ProPakistani, 13 Sep 2024](https://propakistani.pk/2024/09/13/psx-issues-alert-against-fraudulent-whatsapp-groups-giving-investment-advice/)
- **[Verified] Fintech price sensitivity:** Pakistani EMIs such as SadaPay offer free transfers, which limits that revenue line. With VC funding scarce, fintechs could not keep subsidising acquisition and transaction costs. Papara acquired SadaPay in 2024, reportedly for under USD 50m against a prior USD 120m valuation — [Profit](https://profit.pakistantoday.com.pk/?p=162169); [Profit, 2 Jul 2023](https://profit.pakistantoday.com.pk/2023/07/02/fast-dependable-and-easy-to-use-can-sadapay-revolutionize-the-fintech-landscape-in-pakistan); [ProPakistani, 30 May 2024](https://propakistani.pk/2024/05/30/turkish-fintech-unicorn-papara-acquires-pakistans-sadapay/amp/)

### Inferences
- **[Estimate]** Pricing anchor for a consumer "premium" tier: **PKR 299–999/month**, or PKR 2,500–8,000/year. Going much above Spotify/Netflix price points (PKR 299–1,900) is likely to depress conversion sharply.
- **[Estimate] Subscriber break-even:** at PKR 650k/month burn and PKR 500/month net ARPU, you need 1,300 paying subscribers. After an assumed 15% store commission (not sourced here) and a 3–5% churn assumption, gross adds must be correspondingly higher.
- The fraud-tainted "tips" market suggests demand for paid signals but low trust. Positioning as SECP-compliant, fee-transparent and conflict-free is a differentiator, though "advice" may trigger SECP licensing (Investment Adviser) considerations, which were not researched here.

### Gaps
- No verified prices found for Dawn digital, Profit/Pakistan Today, Business Recorder or Sarmaaya premium subscriptions, or for typical stock-tip group fees in PKR.
- Payment rails were not researched in this session: JazzCash/Easypaisa subscription billing, Raast recurring payments, card penetration, and Google Play/App Store PKR billing and carrier billing.
- No churn benchmarks for EM finance apps were found.
- Current (2026) official Netflix/YouTube Premium PKR prices were not confirmed.

---

## 3. B2B options: buyers and price points for Pakistani fund/market data

### Takeaway
I found **no published price points** for Pakistani market data vendors (PSX data licensing, Mettis Global, Bloomberg in Pakistan) or research subscriptions. B2B pricing must come from direct vendor quotes and interviews. Likely buyers can be listed, but their willingness to pay is unverified.

### Cited Findings
- **[Caution: false match]** Searches for "PSX market data vendor fee" returned **Nasdaq PSX (Philadelphia)** fee filings: USD 500/yr delayed and USD 1,000/yr real-time admin fees in a 2010 filing. These are **not** Pakistan Stock Exchange fees and must not be used — [SEC filing 34-62876](https://www.sec.gov/files/rules/sro/phlx/2010/34-62876-ex5.pdf)
- **[Verified] Fund distribution is concentrated in AMCs and banks.** Bank wealth desks such as Standard Chartered Pakistan sell funds with loads, and AMCs pay MUFAP-registered distributors. Both are potential buyers of comparison widgets and analytics — [Standard Chartered Pakistan](https://www.sc.com/pk/wealth-solutions/invest/mutual-funds/); [Meezan OD 2026](https://www.almeezangroup.com/assets/uploads/2026/03/Meezan-Government-Securities-Fund-Offering-Document.pdf)
- **[Verified] Credit ratings and AMC data are published by PACRA**, a competing or complementary public data source — [PACRA](https://pacra.com/finalPr/MTU1NTc=)
- **[Verified] Fund-comparison sites already exist**, for example FinHisaab fund pages and PakFinance "best mutual funds 2026" guides — [FinHisaab](https://finhisaab.com/mutual-funds/mahaana-islamic-cash-fund); [PakFinance](https://pakfinance.pk/guides/best-mutual-funds-pakistan/)

### Inferences
- **[Estimate]** Candidate B2B buyers include:
  - AMCs: competitive benchmarking and peer-ranking data
  - Brokers and digital AMCs: embeddable fund-comparison widgets
  - Bank wealth desks: RM tools
  - Pension fund managers
  - Foreign frontier/EM investors and research houses: English-language clean datasets/APIs
  - Journalists, academics and researchers: low willingness to pay
- AMC count is small (~20–30, unverified here), so even well-priced B2B is a niche revenue line. **[Estimate]** If 10 AMCs/brokers pay PKR 50k–150k/month, B2B ARR is PKR 6m–18m, roughly USD 21k–64k. These are illustrative assumptions, not sourced prices.
- A white-label/API model fits the channel structure. AMCs already pay distributors and have marketing budgets, and the 2025 reforms disallow charging indirect expenses to funds, so marketing spend now comes from AMC P&Ls.

### Gaps
- Pakistan Stock Exchange data vendor/redistribution fee schedule
- Mettis Global, Bloomberg/Refinitiv terminal pricing in Pakistan
- Broker research subscription prices
- MUFAP data licensing terms
- AMC marketing budgets

None of these were found within the call budget.

---

## 4. Advertising/sponsorship economics, plus analysis of the Sarmaaya YouTube data

### Takeaway
Sarmaaya's ~870 YouTube videos have **13.17m lifetime views**, but the distribution is skewed: median 6,600, mean 15,168. At sourced Pakistani RPM benchmarks of USD 0.30–6.40, lifetime AdSense revenue is only about **USD 4k–84k**, with a plausible central case of USD 7k–38k. That makes YouTube ads a marketing channel, not a revenue model. Explainer content on mutual funds and "how to invest" draws the most views, which is direct evidence of demand for this product's topic.

### Cited Findings: RPM/CPM benchmarks
- **[Weak/aggregator] General Pakistani-audience CPM** is roughly USD 0.30–1.50 (some say 0.50–2.50 CPM, or ~0.30–1.40 RPM after YouTube's 45% share). Payouts are cited at about USD 350–1,000 per million views — [GoTest, 2025](https://gotest.com.pk/articles/how-much-does-youtube-pay-for-1-million-views-in-pakistan); [VideoDubbing, 2026](https://videodubbing.com/blog/post/youtube-rpm-earnings-per-1000-views-by-country-2026/); [Milx, 2026](https://milx.app/trends/youtube-cpm-rpm-rates-2026-average-niches-countries-more)
- **[Weak/calculator site] Finance & Investing channels with a Pakistani audience:** RPM of about USD 2.9–6.4 — [ytgrowth.io](https://ytgrowth.io/youtube-earnings/finance/pakistan)
- **[Outlier, likely unreliable]** A 2022 blog claims USD 0.02 per 1,000 views in Pakistan — [BlogPakistan, 2022](https://blogpakistan.pk/how-much-does-youtube-pay-for-1000-views-in-pakistan)

### Local data analysis: `/home/user/Files/sarmaaya_videos.csv`
Method: Python run with `-I`. 870 rows, 868 with valid view counts; 2 rows had a blank `views` field and were excluded. **The file has no upload dates, so views are lifetime totals and cannot be annualised.**

| Metric | Value |
|---|---|
| Videos (valid) | 868 |
| Total views | **13,166,210** |
| Mean views/video | 15,168 |
| Median views/video | **6,600** |
| P10 / P25 / P75 / P90 / P99 | 1,200 / 2,400 / 15,000 / 30,000 / 200,000 |
| Top 5 videos | 629k, 399k, 346k, 310k, 266k |
| Share of views from top 10 videos | 23.0% |
| Share of views from top 50 videos | 43.5% |
| Median duration | 830 s (~14 min); mean 1,623 s (~27 min) |
| Videos ≥ 8 min (mid-roll eligible) | 589 videos, 11.88m views (90% of total), median 10,000 |
| Videos ≤ 60 s (Shorts-like) | 22 videos, 47,587 views, median 1,550 |
| Titles containing "mutual fund" | 20 videos, 1.18m views (9% of total from 2.3% of videos) |
| Titles containing "fund" | 63 videos, 1.72m views |
| Titles containing "invest" | 157 videos, 3.06m views |
| Titles containing "stock" | 134 videos, 2.47m views |
| Titles containing "PSX" | 23 videos, 0.37m views |
| Titles containing "gold" | 26 videos, 0.49m views |

The top videos are beginner explainers:
1. "How to Double Your Money? #SarmaayaExplain" (629k)
2. "How to Open a Stock market Account" (399k)
3. "What is a Mutual Fund? A beginner's guide" (346k)
4. "How to open a Mutual Fund Account within 10 minutes #Sarmaaya #Mahaana" (266k), which is evidently a Mahaana collaboration or sponsorship

**[Estimate] Implied lifetime AdSense revenue = 13,166,210 / 1,000 × RPM:**

| RPM (USD) | Basis | Lifetime revenue (USD) | ≈ PKR @280 |
|---|---|---|---|
| 0.30 | low general PK | 3,950 | 1.11m |
| 0.50 | mid general PK | 6,583 | 1.84m |
| 1.00 | high general PK | 13,166 | 3.69m |
| 1.50 | top general PK | 19,749 | 5.53m |
| 2.90 | low finance-PK (weak source) | 38,182 | 10.7m |
| 6.40 | high finance-PK (weak source) | 84,264 | 23.6m |

Per typical video: the median of 6,600 views at RPM 0.5–2.9 gives **USD 3.30–19** lifetime, and the mean of 15,168 views gives **USD 7.60–44**.

### Inferences
- **[Estimate]** Even a top Pakistani finance-education channel earns low-five-figure USD lifetime AdSense. Revenue in this niche must come from sponsorships (AMC/broker integrations such as the Mahaana video), lead generation, or the product itself.
- High-performing topics include beginner "how to invest" content, opening mutual fund/stock accounts, and compounding. These map directly onto a fund-comparison product's acquisition funnel (SEO + YouTube), so the content is best treated as a CAC-reduction lever.
- Long-form (≥8 min) dominates; Shorts barely register for this channel (22 videos, 47k views). TikTok/Shorts potential cannot be judged from this sample.

### Gaps
- No sourced Pakistani sponsored-video rates were found (PKR per integration for finance creators). AMC marketing/advertising budgets were also not found.
- No upload dates exist in the CSV, so annual views and revenue run-rate cannot be computed. The audience geography split (Pakistan vs overseas Pakistanis, which carries a higher RPM) is unknown.
- RPM sources are SEO/calculator sites, not platform data. Treat the ranges as order-of-magnitude.

---

## 5. Go-to-market: channels, CAC and retention

### Takeaway
Direct evidence on Pakistani fintech CAC and retention was **not found**. Qualitative signals point to content-led acquisition, specifically YouTube explainers and SEO for "best mutual funds in Pakistan 2026". Partnerships with digital AMCs work too, as the Sarmaaya × Mahaana video showed. Paid WhatsApp communities carry regulatory/fraud stigma.

### Cited Findings
- **[Verified] SEO competition exists** for "best mutual funds Pakistan 2026" and "how to invest in mutual funds Pakistan 2026" queries (PakFinance, Pakera), so the keyword space is contested but young — [PakFinance](https://pakfinance.pk/guides/best-mutual-funds-pakistan/); [Pakera](https://pakera.pk/mutual-funds-invest-pakistan/)
- **[Verified, from CSV]** Sarmaaya's videos on "What is a Mutual Fund?" (346k views) and "How to open a Mutual Fund Account within 10 minutes #Mahaana" (266k) are among its top 5, out of 13.2m total views. The 20 "mutual fund" titled videos produce 9% of channel views — local file analysis, section 4
- **[Verified] WhatsApp/finfluencer channels carry fraud risk.** SECP has repeatedly warned against WhatsApp groups and impersonated finfluencers (Sep 2024, Nov 2025) — [SECP, Nov 2025](https://www.secp.gov.pk/wp-content/uploads/2025/11/Press-Release-SECP-Warns-Public-About-Illegal-Trading-Application-Misusing-Names-of-Licensed-Brokerage-Houses-and-Pictures-of-Celebrities-FinFluencers-and-Br.pdf)
- **[Verified] Funding environment:** Pakistani fintechs face scarce VC and cannot aggressively subsidise acquisition — [Profit](https://profit.pakistantoday.com.pk/?p=162169)
- **[Verified] Small investor base:** about 250k individual mutual fund investors (Tribune, Feb 2026, via search snippet; the penetration figure is inconsistent, see section 1) — [Tribune](https://tribune.com.pk/story/2587410/assets-under-mutual-funds-triple-in-three-years)
- **[Verified] Mahaana AUM growth** of ~2.1x in 2025 and +17.7% MoM in Feb 2026 shows digital-first fund acquisition is working at small scale — [PACRA](https://pacra.com/finalPr/MTU1NTc=); [Trade Chronicle](https://tradechronicle.com/?p=68544)

### Inferences
- **[Estimate]** The most capital-efficient GTM is likely:
  1. SEO and comparison pages targeting "best mutual fund in Pakistan / money market fund returns / Meezan vs …" queries
  2. YouTube collaborations with existing finance educators such as Sarmaaya
  3. Free tools (return calculators, fund rankings) that feed AMC/digital-AMC referral or affiliate deals

  Paid acquisition is hard to justify without a CAC benchmark and with low ARPU.
- With only ~250k individual investors, the near-term serviceable market of active fund investors is small. A product needs to widen the funnel to first-time savers (bank depositors) or to overseas Pakistanis (Roshan Digital Account), which was not researched here.

### Gaps
- No CAC figures were found for Pakistani or EM fintech (SadaPay, NayaPay, Mahaana or brokers), and no D30/D90 retention or churn benchmarks.
- Roshan Digital Account (RDA) investor numbers, and how overseas Pakistanis access mutual funds via RDA, were not retrieved.
- TikTok finance creator reach in Pakistan was not retrieved.

---

## 6. Cost side: MVP build/run cost and break-even

### Takeaway
Pakistani developer pay is low by global standards but varies widely by source. PayScale averages are about PKR 0.6m (entry) to 1.2m (mid-career) a year. WageIndicator gives PKR 95k–341k per month in 2025, which is PKR 1.1m–4.1m a year. A lean MVP team could plausibly run at about **PKR 0.5–1.0m/month (USD 1.8k–3.6k)**, which makes break-even reachable with roughly 1,000–2,000 paying subscribers. By contrast, distribution-only revenue needs PKR 1.5–3bn of AUM.

### Cited Findings
- **[Verified, self-reported data] PayScale (Pakistan):**
  - Entry-level software engineer (Karachi): median ~PKR 588,532/yr
  - Mid-career (Karachi): ~PKR 1,221,735/yr
  - Java-skilled (Karachi): ~PKR 1,166,528/yr
  - Overall averages: ~PKR 0.98m–1.17m/yr

  Sources: [PayScale entry-level](https://www.payscale.com/research/PK/Job=Software_Engineer/Salary/d0bac032/Entry-Level-Karachi); [PayScale mid-career](https://www.payscale.com/research/PK/Job=Software_Engineer/Salary/e0f013d2/Mid-Career-Karachi); [PayScale Java Karachi](https://www.payscale.com/research/PK/Job=Software_Engineer/Salary/2f14e5e8/Karachi-Java)
- **[Verified] WageIndicator (2025):** most software developers earn PKR 95,119–340,547 per month; entry-level net is about PKR 95k–194k per month — [WageIndicator](https://acc.wageindicator.org/en-pk/work-in-pakistan/jobs-and-pay/software-developers)
- **[Conflict]** PayScale annual figures, around PKR 1m/yr, sit well below WageIndicator monthly ranges, which annualise to PKR 1.1–4.1m. PayScale's samples are probably older and self-reported. Market rates for strong full-stack developers in 2026 are likely nearer the WageIndicator mid-to-upper range.

### Inferences
- **[Estimate] MVP monthly burn (assumptions):**

  | Item | PKR/month |
  |---|---|
  | 2 full-stack devs @ PKR 250k | 500,000 |
  | 0.5 designer/data analyst | 100,000 |
  | Hosting, data and tools (assumed USD 150–200) | ~50,000 |
  | **Total** | **~PKR 650,000 (≈ USD 2,300)** |
  | **Annual** | **≈ PKR 7.8m (≈ USD 28k)** |

  Founder salaries, legal and SECP licensing costs are excluded; a distributor or investment-adviser licence would add to this.
- **[Estimate] Break-even under each revenue model, at PKR 650k/month:**
  - **Consumer subscription** at PKR 500/month net: 1,300 paying users.
  - **Consumer subscription** at PKR 299/month: ~2,200 paying users.
  - **Distribution trail** at 0.25% / 0.5% blended: PKR 3.1bn / 1.56bn of AUM.
  - **Distribution with PKR 1m-equivalent load share:** per section 1, loads give PKR 7.5k–25k per PKR 1m of new inflows. That needs about PKR 30–100m of fresh inflows a month at a 0.75–2.5% load captured.
  - **B2B:** 5–13 clients at PKR 50k–150k/month.
  - **YouTube AdSense:** Sarmaaya's entire 13.2m-view library implies about PKR 1.1m–23.6m lifetime. That is between ~2 months and ~3 years of this burn in total, not per year.
- A hybrid looks most viable: a free comparison tool for SEO/content acquisition, plus B2B widgets/data for AMCs and brokers, plus referral fees from digital AMCs and distributors. Consumer premium would be an add-on.

### Gaps
- No P@SHA or Rozee.pk 2025/26 salary survey was retrieved, and no Pakistan-specific hosting/cloud cost data.
- SECP licensing costs and capital requirements for a distributor, investment adviser or digital platform were not researched.
- The FX rate (PKR ~280/USD) is an approximation and was not sourced in this session.
