# AI Transformations — Session 3 Cheat Sheet: Investment allocation

As of 31 Oct 2026 · Session of 19 Oct · Source: "Capital Allocation & the Investment Case for AI" (pages 95–152 of *AI Strategy - Albert School - Master 2026.pdf*)

The course logic runs in order: diagnose readiness → pick the operating model → sequence the portfolio → prove it financially → manage the change. This session covers the fourth step; see [session_1_cheat_sheet.md](session_1_cheat_sheet.md) for the exam format. The Comex memo that wraps the case is in [session_4_cheat_sheet.md](session_4_cheat_sheet.md).

**The session's five skills**: build a 3-year envelope by cost category, build a 3-scenario expected-value analysis, compute portfolio IRR and test it against the hurdle and WACC, count the opportunity cost of not investing, draft a 2-page Comex memo.

**Closing line of the deck: "Not investing is not free. Allocate with discipline."**

## 0. Why it matters, and the golden rule

- **Investment alone does not create value: capital allocation discipline does.** BCG (Sept 2025, 1,250 firms): 5% are "future-built" (AI value at scale), 35% are scaling, 60% report hardly any value despite heavy spend. Future-built firms show 3.6× the 3-year TSR and plan over 2× the AI spend of laggards.
- **Pilots without a credible business case are cut first.** Gartner predicted 30% of GenAI projects would be abandoned after PoC by end-2025; it observed 50% (Jan 2026). The causes are poor data quality, weak risk controls, escalating costs and unclear business value.
- **Golden rule: speak the board's language.** Talk capital, risk, competitive advantage and timeline, never model architectures.

| Engineer says | Board hears |
| --- | --- |
| "We'll fine-tune a 70B model" | X capex, live in 9 months, cuts cost-to-serve 12% |
| "Accuracy is 94%" | Error rate halves; Y avoided claims or refunds |
| "We need a vector DB and GPUs" | A platform investment that every later initiative reuses |
| "The PoC worked" | Clears the hurdle in the base case; here is the downside |

## 1. Investment allocation: the financial toolkit

**NPV is the headline metric.** It measures value created in today's euros after paying the cost of capital. **Use ROI and payback to communicate; decide on NPV.** ROI and simple payback ignore when the money arrives, so a project can show a positive ROI and still destroy value.

### Cash vs profit

- **EBITDA** = operating cash proxy (sales − COGS − opex). **EBIT** = EBITDA − D&A.
- **Free cash flow** = EBITDA − cash taxes − capex (incl. capitalised AI) − change in working capital.
- **Capex** is capitalised and depreciated; **opex** hits the P&L now. Cloud AI shifts spend to opex. Under IAS 38, development-phase software can be capitalised; research is expensed.
- **D&A is non-cash**: it reduces profit, not cash, so add it back. **Tax shield** = D&A × tax rate (4M × 25% = 1M).
- **Appraise AI on free cash flow, not EBITDA**: timing and tax both matter.

### Formulas

Present value of one cash flow at year t, discounted at rate r (cost of capital or required return, not just inflation):

$$
PV = \frac{CF_t}{(1+r)^t}
$$

$$
ROI = \frac{\text{total benefits} - \text{total costs}}{\text{total costs}}
$$

NPV = discounted inflows (the DCF) minus the initial investment I0. I0 is paid at t = 0, so it is **not discounted**:

$$
NPV = \sum_{t=1}^{n} \frac{CF_t}{(1+r)^t} - I_0 = DCF - I_0
$$

IRR is the rate that makes NPV = 0. It has no closed form: use trial and error, interpolation (NPV@20% ≈ +1.0, NPV@21% ≈ −1.0, so IRR ≈ 20.5%) or Excel.

$$
\sum_{t=0}^{n} \frac{CF_t}{(1+IRR)^t} = 0
$$

**MIRR** fixes IRR's reinvestment assumption. It finances outflows at a finance rate and reinvests inflows at a reinvestment rate (often the cost of capital or WACC):

$$
MIRR = \left(\frac{FV(\text{positive CFs, at reinvestment rate})}{PV(\text{negative CFs, at finance rate})}\right)^{1/n} - 1
$$

- **Payback** = years until cumulative cash turns positive. **Discounted payback** = the same on cumulative PV. Payback speaks to liquidity but ignores cash after payback.
- Discount factor at 10%: year 1 = 0.909, year 2 = 0.826, year 3 = 0.751, year 4 = 0.683. 100 in three years is worth 75.1 today.
- **Why discounting bites in AI**: costs land early (platform, data, integration in Y1) and benefits land late (adoption ramps in Y3–5). So sequence quick wins early to pull value forward.

### Cost of capital and the hurdle rate

$$
WACC = \frac{E}{V} K_e + \frac{D}{V} K_d (1 - t) \qquad K_e = R_f + \beta (R_m - R_f)
$$

- **WACC** = what the firm's capital costs, blended. **Cost of equity Ke** = what shareholders require (CAPM above).
- **Hurdle = WACC + risk / strategic premium**, set by management case by case. **Typical practice: +2 to +6 points over WACC, set by Finance.**
- **Why AI carries a premium**: execution and adoption risk (value depends on people changing how they work), fast model obsolescence and vendor lock-in, data and integration uncertainty, regulatory exposure (EU AI Act).

### Excel: five functions for every investment case

| Function | Syntax | Watch out |
| --- | --- | --- |
| NPV | `=NPV(rate, CF1:CFn) + CF0` | Add the t0 outlay outside: NPV() treats its first value as year 1 |
| IRR | `=IRR(CF0:CFn)` | Needs a sign change |
| XIRR | `=XIRR(values, dates)` | For irregular dates |
| MIRR | `=MIRR(values, fin, reinv)` | Reinvest at the cost of capital |
| SUMPRODUCT | `=SUMPRODUCT(p, CF)` | Probabilities must sum to 100% |

Tip: one row per year, one column per scenario; the EV is then one SUMPRODUCT per year.

### Worked example: EUR 100M project, r = 10% (EUR M)

| Year | Cash flow | Cumulative | DF at 10% | PV | Cumulative PV |
| --- | --- | --- | --- | --- | --- |
| 0 | −100.0 | −100.0 | 1.000 | −100.0 | −100.0 |
| 1 | 30.0 | −70.0 | 0.909 | 27.3 | −72.7 |
| 2 | 40.0 | −30.0 | 0.826 | 33.1 | −39.7 |
| 3 | 50.0 | +20.0 | 0.751 | 37.6 | −2.1 |
| 4 | 40.0 | +60.0 | 0.683 | 27.3 | +25.2 |

| Metric | Result | How |
| --- | --- | --- |
| ROI | 60% | 60 ÷ 100 |
| Payback | 2.6 years | 2 + 30 ÷ 50 |
| Discounted payback | about 3.1 years | 3 + 2.1 ÷ 27.3 |
| NPV at 10% | EUR 25.2M | 125.2 − 100 |
| IRR | 20.5% | Rate where NPV = 0 |

Decision: **accept**, since NPV > 0 and IRR 20.5% > 10%. Discounting delays payback from 2.6 to 3.1 years. NPV falls as r rises: +60 at 0%, +25.2 at 10%, +1.0 at 20%, 0 at 20.5% (the IRR), −8.4 at 25%. NPV at 0% equals total net cash, the ROI numerator.

### Decision rules

- **NPV < 0 → no go. NPV ≥ 0 → go.** NPV = 0 means the project earns exactly the required return. NPV > 0: it earns more than the cost of capital. NPV < 0: investors could earn more elsewhere at the same risk.
- **IRR > hurdle rate → go.** IRR is the break-even cost of capital.
- **Hurdle rate** = minimum required return = the r used in NPV. It must rise with risk: an H3 bet needs a higher hurdle than an H1 rollout.
- **Why NPV wins**: it uses every cash flow, their timing and their risk, and NPVs add up across a portfolio.

### NPV vs IRR pitfalls

- **Scale**: IRR is a %, blind to size. EUR 1M at 50% IRR creates less value than EUR 100M at 20%. To rank mutually exclusive projects, trust NPV.
- **Sign changes**: if cash flows change sign more than once (for example a late decommissioning cost), there can be several IRRs or none.
- **Reinvestment**: IRR assumes interim cash is reinvested at the IRR, which is rarely true; NPV assumes r, which is more realistic. MIRR corrects this.
- **Additivity**: NPVs of projects add up; IRRs don't.

## 2. The three-year investment envelope

### Six cost categories

| Category | What it covers |
| --- | --- |
| Platform / compute | Cloud GPUs, inference tokens, infrastructure to train, host and run models; software |
| Talent | AI engineers, data scientists, product owners, plus upskilling the wider workforce |
| Integration | Connecting to ERP, CRM and core systems; workflow redesign and change management |
| Model ops | MLOps / LLMOps: monitoring, evaluation, retraining, run support in production |
| Data acquisition | Data preparation, labelling, third-party licensing, data pipelines |
| Governance | Responsible AI, risk and compliance (EU AI Act), audit and security |

### Hidden costs (industry estimates, indicative)

- **Only 45–60% of true AI TCO is visible** (licences, compute, development labour). The rest is integration, change, data, governance and run.
- **7–12%** of AI budgets go to governance in governance-mature organisations.
- **25–35%** of year-1 TCO is often integration with core systems and workflows.
- Gartner cost ranges: embedding GenAI APIs in custom apps costs **$750k–$1M upfront + up to $1,200 per user per year**; building custom models from scratch costs **$8M–$20M upfront**.
- **Model the run-rate, not just the build.** Some early AI projects saw cost surges driven by adoption, even as unit costs fall (LLM → SLM shifts). **FinOps discipline**: tag every euro of compute to a use case, track unit cost per transaction or user, review run-rate vs plan every month.

### Helios Group: a EUR 52M three-year envelope (fictional, ~EUR 2bn retailer, 4 use cases)

Use cases: customer-service agents, demand forecasting, procurement AI assistant, marketing content.

| EUR M | Y1 | Y2 | Y3 | Total | % |
| --- | --- | --- | --- | --- | --- |
| Compute | 6.0 | 3.5 | 3.0 | 12.5 | 24% |
| Talent | 4.0 | 5.0 | 4.5 | 13.5 | 26% |
| Integration | 5.0 | 3.0 | 1.5 | 9.5 | 18% |
| Model ops | 1.0 | 2.5 | 3.5 | 7.0 | 13% |
| Data acquisition | 3.0 | 1.5 | 1.0 | 5.5 | 11% |
| Governance | 1.0 | 1.5 | 1.5 | 4.0 | 8% |
| **Total** | **20.0** | **17.0** | **15.0** | **52.0** | 100% |

**Build, then scale, then run.** Y1 = build: compute + integration + data = 70% (infrastructure-heavy). Y2 = scale: talent leads at 29% (product teams, change, upskilling). Y3 = run: talent + model ops = 53%; model ops (23%) overtakes compute (20%); governance reaches 10%. Compute falls from 30% to 20% of yearly spend while model ops rises from 5% to 23%. **Budget model ops and governance from day 1.**

### MaisonRetail: a EUR 30M three-year envelope (fictional, ~EUR 2bn retailer, the class case)

| EUR M | Y1 | Y2 | Y3 | Total |
| --- | --- | --- | --- | --- |
| Compute | 3.0 | 2.5 | 2.0 | 7.5 |
| Talent | 3.0 | 3.5 | 3.0 | 9.5 |
| Integration | 2.5 | 2.0 | 1.0 | 5.5 |
| Model ops | 0.5 | 1.0 | 1.5 | 3.0 |
| Data acquisition | 1.5 | 0.75 | 0.5 | 2.75 |
| Governance | 0.5 | 0.5 | 0.75 | 1.75 |
| **Total** | **11.0** | **10.25** | **8.75** | **30.0** |

**Link to the portfolio (70-20-10)**: H1 efficiency EUR 21M, H2 augmentation EUR 6M, H3 new business model EUR 3M. Deviate only with an explicit justification.

### Funding model: who pays? (Microsoft AI Transformation Office)

| Year | Central (ATO) | Business units | Phase |
| --- | --- | --- | --- |
| 1 | 100% | 0% | Build capabilities |
| 2 | 60% | 40% | Accelerate and innovate |
| 3 | 40% | 60% | Scale |

**BU co-funding = skin in the game.** Keep 40% central in year 3: it preserves a decisive seat at the table and funds disruptive bets.

## 3. Scenarios, expected value and the hurdle test

**Why three scenarios: a single-point forecast hides risk.** (1) Make every assumption explicit. (2) Assign probabilities that sum to 100%. (3) **Lead with the worst case**: the board will ask for it first.

$$
ENPV = \sum_{s} p_s \times NPV_s
$$

### MaisonRetail scenarios (EUR M, 5 years, hurdle 12%, no terminal value)

Costs are the same in all scenarios (11.0, 10.25, 8.75, 2.0, 2.0). **The risk sits on the value side.**

| Scenario | p | Benefits Y1–Y5 | Net cash Y1–Y5 | Cumulative | NPV @12% | IRR |
| --- | --- | --- | --- | --- | --- | --- |
| Downside: slow adoption, value delayed | 30% | 0.5, 2.5, 5, 7, 8 | −10.5, −7.75, −3.75, 5.0, 6.0 | −11.0 | −11.6 | −21.8% |
| Base: plan delivered | 50% | 1, 5, 10, 14, 16 | −10.0, −5.25, 1.25, 12.0, 14.0 | +12.0 | +3.4 | 20.5% |
| Upside: fast adoption + H2 revenue lift | 20% | 1.5, 8, 15, 21, 24 | −9.5, −2.25, 6.25, 19.0, 22.0 | +35.5 | +18.7 | 57.6% |
| **Probability-weighted (EV)** | | | −10.05, −5.4, 0.75, 11.3, 13.2 | +9.8 | **+1.9** | **17.0%** |

ENPV = 0.3 × (−11.64) + 0.5 × 3.35 + 0.2 × 18.73 = **+1.9M: positive but thin; the downside is material.** In this case, year-1 cash flows are discounted one full year (no t = 0).

### Hurdle test

- **Hurdle 12% = WACC 8.5% + 3.5-point risk premium** (novelty, execution risk, a history of pilot purgatory).
- **EV IRR 17.0% > 12%: clears, with a 5-point cushion.** NPV at WACC (8.5%) = +3.7M vs ENPV +1.9M at the hurdle.
- **Always show NPV alongside IRR**: IRR has multiple-root and scale pitfalls. The case is conservative by design: 5-year horizon, no terminal value.

### Opportunity cost: doing nothing has a cost too

| "Do nothing" erosion, EUR M | Y1 | Y2 | Y3 | Y4 | Y5 | PV @12% |
| --- | --- | --- | --- | --- | --- | --- |
| Competitor catch-up | 0 | −0.5 | −1.0 | −2.0 | −3.0 | −4.1 |
| Talent exit | 0 | −0.5 | −1.0 | −1.0 | −1.0 | −2.3 |
| Regulatory exposure | 0 | 0 | −0.5 | −1.0 | −1.0 | −1.6 |
| **Total** | 0 | −1.0 | −2.5 | −4.0 | −5.0 | **−8.0** |

How to estimate each line:
- **Competitor catch-up** = share points at risk × margin × revenue.
- **Talent exit** = extra attrition × cost to replace digital talent.
- **Regulatory exposure** (shadow AI, non-compliance) = probability × impact.

**Decision value bridge**: invest ENPV +1.9M + avoided inaction losses +8.0M = **+9.9M incremental NPV**, incremental IRR **35.6%** (vs 17.0% alone). Note: the bridge slide (p133) prints 32.7%, but the previous slide and a recomputation both give 35.6%.

**Compare invest vs a decaying status quo, not vs zero.** But be explicit and defensible: boards discount hand-waved "strategic" value.

### Sanity-check against benchmarks (vendor-sponsored or survey data: use as ranges and stress-test)

| Source | Benchmark |
| --- | --- |
| IDC (Microsoft-sponsored, Nov 2024) | Under 8 months to deploy AI; value within ~13 months; about $3.70 back per $1 |
| Gartner (early GenAI adopters, 2024) | +15.8% revenue, 15.2% cost savings, 22.6% productivity |
| Microsoft ATO (rule of thumb) | 20–30% productivity gain for packaged AI in functions (developers, call centres, consultants) |
| BCG (Sept 2025) | Future-built firms get 5× the revenue increases and 3× the cost reductions from AI |

### Five ways investment cases mislead

| Pitfall | What it looks like | The fix |
| --- | --- | --- |
| 1. Double-counting benefits | Two use cases claim the same hours saved or revenue | One benefits register, reconciled by Finance |
| 2. Optimistic adoption curves | 80% adoption in month 3; no ramp, no resistance | S-curve ramp, benchmarked on pilots |
| 3. Ignoring run costs | Envelope stops at go-live; no model ops or governance | Budget run costs (Helios: EUR 6M/yr) |
| 4. Using WACC alone | Risky AI judged at 9% like a warehouse upgrade | Test at the hurdle: WACC + premium |
| 5. Sandbagging the downside | A "downside" that still clears the hurdle | Real downside: delay, partial scale, overrun |

## 4. Deploying the capital: the J-curve and stage gates

**Value dips before it climbs.** Cumulative net cash goes negative first. On the slide's chart, EV bottoms out at −27.6M in Y2, reaches +18.4M by Y5, and the base case breaks even in Y4. MaisonRetail's own EV turns positive only in Y5 (cumulative −10.05, −15.45, −14.7, −3.4, +9.8). Hyperscalers' AI capex follows the same shape.

**The productivity J-curve** (Brynjolfsson, Rock and Syverson, 2021): general-purpose technologies like AI need large complementary intangible investments (process redesign, skills, data) that are poorly measured. Early on the costs are visible and the asset is not; later the intangibles are harvested and measured productivity catches up. **Risk: Y1 over-spends on infrastructure, then impatience kills value in Y2–3.**

**Four reflexes against impatience**: fund H1 quick wins that show on the P&L in year 1; release capital in stage-gated tranches; a monthly ROI dashboard for the CEO, Exec and Board on the most capital-intensive projects; pre-agree kill criteria before you start.

**Six ways to survive the dip**:
1. **Stage gates with kill / scale criteria**: each gate has explicit thresholds to stop or scale.
2. **Leading before lagging indicators**: track adoption, cycle time and quality before EBIT moves.
3. **Quick wins funded in Year 1**: ship one or two fast-payback use cases to buy patience.
4. **A ring-fenced 3-year envelope**: commit the envelope; release it annually against gates.
5. **Benefits owned by the business P&L**: business leaders sign the benefits; Finance tracks them.
6. **Reinvest realised gains**: recycle savings into the next wave of use cases.

### Milestones a CEO can hold you to (MaisonRetail)

| | Month 12 (Y1 spend 11.0M) | Month 24 (Y2 spend 10.25M) | Month 36 (Y3 spend 8.75M) |
| --- | --- | --- | --- |
| Milestones | Data platform live; 3 H1 use cases in production; baseline KPIs measured | H1 scaled across BUs; H2 augmentation pilots generating revenue; BU co-funding at 40% | Run-rate benefits ≥ run-rate cost; H3 option tested; BUs fund 60% |

### Stage-gated capital: release capital only on evidence

Stages **Test → Scale → Democratise**, with gate questions per tranche: *Right data? Delivering expected ROI? Easy to scale?*

**Value-realisation discipline** (5 steps): (1) baseline KPIs before you build; (2) map each use case to P&L levers; (3) track the same KPIs after deployment; (4) report benefits in financial terms; (5) a governance board reviews monthly or quarterly.

### Worked memo: Helios (EUR M, the slide's model answer)

- **Thesis**: approve a 52M, 3-year envelope for four use cases. It clears the 13% hurdle on EV (IRR 17.8%), and waiting would cost an estimated 16.7M in PV.
- **Envelope**: 20 / 17 / 15 in Y1–3; talent 26%, compute 24%, integration 18%, model ops 13%, data 11%, governance 8%; run cost 6M a year from Y4.
- **Scenarios**: downside (30%) IRR −31.9%, NPV −27.3M; base (50%) IRR 24.5%, NPV +9.0M; upside (20%) IRR 57.2%, NPV +36.7M. EV benefits 82.35M over 5 years.
- **Hurdle**: EV IRR 17.8% vs 13% (WACC 9% + 4-point AI premium), so 4.8 points of headroom; NPV +3.7M at 13%, +7.3M at 9%.
- **Opportunity cost**: 16.7M PV; decision value +20.4M; incremental IRR 38.7%.
- **Risks**: the downside is deep. Mitigations: gate-based release, kill criteria per use case, benefits tracked in business P&Ls, governance funded from Y1.
- **Ask**: approve the 52M envelope; release 20M for Y1 now; release Y2–3 at Gate 1 (end of Y1) and Gate 2 (mid-Y2: run-rate benefits ≥ 8M).

## 5. Spotting planted flaws in a strategy memo

For each claim in the memo, ask which course rule it breaks, then name the rule in your answer. This checklist is built from the course rules above. It is not an official list.

| Flaw you might see | Why it is wrong | Rule to cite |
| --- | --- | --- |
| Investment justified by ROI or IRR alone | Ignores timing (ROI) or scale (IRR) | NPV is the headline metric; show NPV alongside IRR |
| I0 discounted, or CF0 put inside Excel NPV() | Year-0 cash is not discounted | NPV formula |
| Case appraised on EBITDA, not free cash flow | Ignores capex, tax and working-capital timing | Cash pays the bills, not profit |
| One hurdle rate for all projects, or the hurdle set at WACC | Ignores AI execution risk | Hurdle = WACC + 2–6 pt premium; pitfall 4 |
| One scenario only, or no probabilities | A point forecast hides risk | Three scenarios, explicit assumptions, p sums to 100% |
| A "downside" that still clears the hurdle | Sandbagged | Pitfall 5: real downside = delay, partial scale, overrun |
| 80% adoption by month 3 | No ramp, no resistance | Pitfall 2: S-curve benchmarked on pilots |
| Envelope stops at go-live; no model ops or governance line | Run costs ignored; model ops overtakes compute by Y3 | Six cost categories; pitfall 3 |
| Only licences and compute budgeted | Visible costs are only 45–60% of TCO | Hidden costs |
| Two use cases claim the same hours saved | Double-counting | Pitfall 1: one benefits register |
| Compared with "zero" instead of the status quo | Ignores the cost of inaction | Invest vs a decaying status quo |
| A big "strategic value" line with no method | Boards discount hand-waved value | Cost of inaction must be explicit and defensible |
| Whole envelope released upfront, no gates | No evidence before each tranche | Stage-gated capital; kill criteria |
| Expecting EBIT gains in year 1 on an H2/H3-heavy plan | Ignores the J-curve | Leading before lagging indicators; quick wins |
| 100% central funding in year 3 | No BU skin in the game | Funding model 100/0 → 60/40 → 40/60 |
| Benefits owned by IT or the AI team | No one in the business is accountable | Benefits owned by the business P&L |
| Vendor benchmarks used as point forecasts | Sponsored and survey data | Use as ranges and stress-test |
| Technical claims to the board ("94% accuracy") | Wrong language | Golden rule: capital, risk, advantage, timeline |

## 6. Cases and numbers worth citing

| Fact | Figure | Source |
| --- | --- | --- |
| Firms that are "future-built" / scaling / hardly any value | 5% / 35% / 60% | BCG, Sept 2025 |
| Future-built firms' 3-year TSR vs others | 3.6× | BCG, Sept 2025 |
| GenAI projects abandoned after PoC by end-2025 | 30% predicted, 50% observed | Gartner, Jul 2024 / Jan 2026 |
| Typical AI premium over WACC | +2 to +6 points | Course slide |
| Visible share of true AI TCO | 45–60% | Practitioner TCO estimates |
| Governance share of budget (mature orgs) | 7–12% | Practitioner TCO estimates |
| Integration share of year-1 TCO | 25–35% | Practitioner TCO estimates |
| Return per $1 invested in AI | about $3.70 | IDC, Nov 2024 (Microsoft-sponsored) |

## 7. Practice questions with answers

Q1–Q3 are the deck's quick quiz (p111); the answers to Q1 and Q3 come from your notes. The other answers are suggestions that apply the course frameworks, except where marked as from the slides.

1. **A project costs EUR 50M and returns EUR 20M a year for 3 years. What is its ROI, and why might it still destroy value at 10%?**
    - ROI = (60 − 50) / 50 = 20%. NPV = 20/1.1 + 20/1.1² + 20/1.1³ − 50 = 49.74 − 50 = −0.26M. **No go.** ROI ignores the time value of money; IRR is about 9.7%, below the 10% hurdle.
2. **Project A: 35% IRR on EUR 2M. Project B: 18% IRR on EUR 40M. Hurdle 13%. Which do you prefer, and what do you need to know?**
    - Both clear the hurdle. If capital allows, do both. If they are mutually exclusive, rank by **NPV, not IRR**: B likely creates far more absolute value because of scale. You need the cash-flow timing and duration, whether they are exclusive, the capital limit, each project's risk (and so its own hurdle), and whether cash flows change sign.
3. **Why test an AI programme against a hurdle rate above WACC, and what is the risk of setting it too high?**
    - WACC does not price the extra execution, adoption and tech risk that AI programmes carry. Set too high, the hurdle kills good H2 and H3 bets, pushes the portfolio toward H1 (failing strategically), and tempts teams to inflate forecasts.
4. **Re-weight MaisonRetail to 50% downside / 40% base / 10% upside. Does it still clear the hurdle? What would you cut or stage-gate?** (deck exercise, p136)
    - ENPV = 0.5 × (−11.6) + 0.4 × 3.4 + 0.1 × 18.7 = **−2.6M**; EV IRR falls to about 5%, below the 12% hurdle (and below WACC). **It no longer clears.** Including the 8.0M cost of inaction, the decision value is still about +5.4M, so the case rests on how defensible that number is. Response: release only tranche 1 and gate the rest on adoption evidence; protect the H1 quick wins; trim or delay the H2/H3 spend; add kill criteria so the downside is capped.
5. **What is the hurdle for a firm with WACC 9% and a 4-point AI premium? The EV IRR is 17.8%. Does it clear?**
    - Hurdle = 13%. 17.8% > 13%, with 4.8 points of headroom; it also clears WACC. Show the NPV too (Helios: +3.7M at 13%).
6. **The six board questions you must be ready for** (from the slides):

| Question | Your answer must contain |
| --- | --- |
| What is the worst case? | Downside NPV, its probability, and what you would do |
| What kills it, and when do we stop? | Pre-agreed kill criteria at each tranche gate |
| What does the competitor do if we don't? | The cost of inaction, quantified |
| Why this envelope and not half? | What half would cut: horizons, timing, value |
| When do we break even? | The J-curve: trough, then break-even year |
| Who in the business co-funds? | BU share by year: skin in the game |
