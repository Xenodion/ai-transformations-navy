# Long list of candidate AI projects

- **Step:** 08 — [#8](https://github.com/Xenodion/ai-transformations-navy/issues/8). Drafted 8 November 2026 by Alexandre Waerniers, with Claude Code.
- **Acceptance criterion:** record business problem, existing capability, provisional horizon, indicative value/cost/time, uncertainty, and rejected ideas.
- **Inputs:** [strategy synthesis](../../sources/synthesis/2026-11-08_totalenergies_strategy_activities.md) (S04), [AI and organisation synthesis](../../sources/synthesis/2026-11-08_totalenergies_ai_data_organization.md) (S05), [competitor synthesis](../../sources/synthesis/2026-11-08_competitors_benchmarks.md) (S06), [legacy plan audit](../research/legacy_plan_audit.md) (step 07), [register](../../sources/register.md).
- **Status:** long list only. Every candidate has status `idea`. No project, horizon mix, operating model or budget is chosen here (AGENTS.md rule 5). Step 11 selects 3–4 featured projects after steps 09 and 10.

## 1. Method

**Where the ideas come from:**
- the legacy ideas that survived the step 07 audit, re-costed with an "existing capability" field;
- the company's four AI priorities for 2026: HSE, digital plant, geosciences and reservoirs, Integrated Power modelling (CLM-024);
- the company's own pressures: the $12.5bn savings plan for 2026–2030 (CLM-007) and capital discipline (CLM-008);
- peer results that are measured, not just announced: Equinor predictive maintenance (CLM-036, CLM-037), Shell T-Pulse (CLM-048), BP well planning (CLM-068).

**Screening rule:** a candidate must add value on top of what TotalEnergies already runs or funds. Ideas that duplicate an existing capability go to the rejected list (section 4).

**Units:**
- Values are gross annual benefits at full scale, before costs, in US dollars, the company's reporting currency. Step 18 sets the final currency and a dated exchange rate.
- Costs are bottom-up 3-year estimates built from named teams, sourced pay rates and explicit non-staff lines (section 2b), with a single estimate band.
- Each value is a **calculation on assumed inputs**. It is a first-pass order of magnitude for comparison, not a business case.

**Horizon test** (course session 2):
- Q1: does it change the customer?
- Q2: does it change the business model?
- Q3: is the technology proven?
- Q4: is time to value under about 12 months?

Typical answers are H1 = N, N, Y, Y; H2 = Y, N, mostly, N; H3 = Y, Y, N, N. Horizons are provisional until the case studies.

### Shared value assumptions

| ID | Assumption | Value | Basis | Test before step 18 |
| --- | --- | --- | --- | --- |
| A1 | Cost of one hour of employee time | ≈ $62/h | $98.5k ÷ 1,600 working hours (hours assumed) | Payroll by population |
| A2 | Upstream cash margin per barrel kept | $15–30/boe | Brent $69.1/b in 2025 (CLM-063) minus production cost $5.0/boe (CLM-005), less an unknown host-government take | Segment cash flow per boe |
| A3 | Refining margin on recovered throughput | $5.3–7.1/b | ERM 2024–2025 (CLM-063). Q3 2026 ERM of $33.2/b shown only as a sensitivity | Realised margin by site |
| A4 | Realised renewable power price | $40–70/MWh | No registered source | Integrated Power disclosures |
| A5 | Copilot licence price | $30 per user per month | Microsoft public list price; not registered; discounts unknown | Contract data |
| A6 | LNG energy content | 52 MMBtu per tonne | Standard approximate conversion; not registered | Register a conversion source |

## 2. Summary

| ID | Business problem | Candidate AI solution | Existing TotalEnergies capability | Horizon (Q1–Q4) | Value, $M/yr at scale | 3-yr cost, $M: base (band) | First value | Uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | Unplanned outages of critical equipment in refineries and petrochemical plants | Scale predictive maintenance on critical rotating equipment, site by site | AspenTech data fabric rolling out 2025–2027 (CLM-018); predictive maintenance and condition monitoring named as uses (S05) | H1 (N, N, Y, Y) | 6–24 (cross-check 15–45) | 4.8 (4.1–6.3) | 6–12 months | High |
| P02 | Production deferred by well and equipment failures upstream | Production surveillance and failure prediction on the Cognite platform | Cognite across all operated upstream assets, 2025–2028 (CLM-019); production optimisation named as a use (S05) | H1 (N, N, Y, Y) | 5–44 | 2.6 (2.2–3.3) | 6–12 months | High |
| P03 | Cost and duration of well construction | Drilling performance and well-planning optimisation | Cognite scope runs "from drilling to production" (CLM-019); dedicated drilling AI unknown | H1 (N, N, Y, Y) | 46–185 | 3.3 (2.8–4.2) | 6–12 months | Very high |
| P04 | Lost output and imbalance costs in a fast-growing renewable fleet | Fleet availability analytics and alarm triage, plus incremental forecasting | Alarm management for solar and wind plants (S05); Predictive Layer and Quadra forecasting and trading (CLM-027) | H1 (N, N, Y, Y) | 7–46 (× 2.2–2.7 by 2030) | 2.2 (1.9–2.9) | 3–9 months | High |
| P05 | Copilot licences paid since 2024 without measured value | Adoption, licence right-sizing and redesign of 3–5 workflows, with value tracking | Copilot for Microsoft 365 since 2024 (CLM-022); Digital Accelerator GenAI training (S05) | H1 (N, N, Y, Y) | 5–34, of which only 1–3 hard | 1.7 (1.5–2.3) | 3–6 months | Medium |
| P06 | Delivering the $12.5bn savings plan across > 100,000 suppliers | Spend and contract analytics for sourcing teams | None found (unknown) | H1 (N, N, Y, Y) | 10–60, illustrative only | 2.9 (2.5–3.8) | 6–9 months | Very high |
| P07 | Serious-incident precursors on worksites | Scale computer-vision safety monitoring | Smart Worksite Safety Program within Digital for HSE (S05) | H1 (N, N, Y, Y) | 10–30 (avoided incident & downtime risk) | 3.0 (2.5–3.9) | 6–12 months | Medium |
| P08 | Churn and service cost among 8.7 million power and gas client sites | Churn prediction plus a GenAI service agent | "coach conso" GenAI assistant in the customer app (S05) | H1 (N, N, Y, Y) | 2–20 | 2.3 (2.0–3.1) | 6–9 months | High |
| P09 | Boil-off, fuel and routing losses on LNG voyages | Voyage and cargo optimisation across shipping and trading | Not researched (unknown) | H2, borderline (N, N, mostly, N) | 10–31 | 2.0 (1.7–2.7) | 12–18 months | High |
| P10 | Steam-cracker yield, and processing of circular feedstock | Yield optimisation; feed-flexibility models for pyrolysis oil | Antwerp already processes pyrolysis oil (CLM-061); circular polymer target of 1 Mt/y by 2030 (CLM-067) | H1 for yield; H2 for circular feed | 3–15 (circular lever 0.1–4) | 2.1 (1.8–2.7) | 9–15 months | High |
| P11 | No revenue yet from customers' flexible assets (batteries, EVs, solar) | Virtual power plant that aggregates and trades flexibility | 6.0 million power clients, ~90,000 charging points (CLM-066), Saft batteries (S05); flexibility offers not researched | H3 (Y, Y, N, N) | 30–90 (flexibility aggregation & power arbitrage) | 2.5 (2.1–3.2) | 24–36 months | Very high |
| P12 | Cost and pace of discovering catalysts for synthetic aviation fuel (e-SAF) | AI-accelerated catalyst screening | SAF production at Normandy, Antwerp and La Mède, target 0.5 Mt/y by 2028; catalyst plant at Feluy (CLM-060); in-house HPC and the Mistral lab (CLM-021) | H3 (Y, Y, N, N), only with a market thesis | 25–75 (e-SAF catalyst yield & opex reduction) | 3.7 (3.2–4.9) | 24–48 months | Very high |
| P13 | Perishable food/shop inventory shrinkage and rigid retail pricing across service-station network | Demand forecasting for store replenishment to cut food waste, plus dynamic shelf-life markdowns | Station inventory POS systems; fuel pricing models exist, but store demand forecasting remains rule-based (CLM-074) | H1 (N, N, Y, Y) | 2.5–5.5 (conservative: food waste cut + markdowns) | 3.9 (3.2–4.8) | 4–8 months | Medium |
| E01 | No published or tracked value for any internal AI solution (CLM-029) | AI value register and portfolio office | Board AI review (CLM-025); > 10,000 live models (CLM-017) without published value | Enabler | 3–8 (portfolio reallocation & kill-criteria savings) | 1.6 (1.4–2.1) | 3–6 months | Low on cost; value indirect |

**Do not add these rows up.** Several candidates overlap (section 5), the ranges are wide, and a long list is not a portfolio.

## 2b. Cost estimates

The first draft multiplied the extremes of every input (pay rate, squad size, number of sites, cost per site, licences), which gave ranges of 3–5 ×. Costs are now built bottom-up: each project has a named team and a defined rollout scope, and staff are costed at sourced rates. The remaining uncertainty sits in one estimate band and in the vendor prices shown line by line.

### Cost rates

| ID | Input | Value | Source or basis |
| --- | --- | --- | --- |
| C1 | Engineer (data scientist, ML or data engineer) gross pay | €58k/yr | Apec 2025, "big data" job family, median in Île-de-France (CLM-069) |
| C2 | Lead (product owner, architect) gross pay | €70k/yr | Same family, median for those over 45, used as a seniority proxy (CLM-069) |
| C3 | Employer contributions and other employer costs | +43.7% of gross | INSEE, 2022 (CLM-070) |
| C4 | Overhead: workspace, IT, travel, management time | +15% | **Assumption** |
| C5 | Exchange rate | $1.13 per € | ECB, 2025 annual average (CLM-071) |
| C6 | Business expert seconded to the team | $98.5k/yr | Group average loaded cost, payroll ÷ headcount (CLM-062) |
| C7 | Run and model operations (cloud, monitoring, retraining) | $0.1M/yr per project from year 2 | **Assumption** |
| C8 | OT cybersecurity review for each new industrial site | $50k per site | **Assumption** |
| C9 | Estimate band | −15% / +30% around the base | **Assumption**: staff rates are sourced, so the band covers effort and scope; it is skewed upwards because costs overrun more often than they underrun |

**Resulting rates:**
- Engineer = 58 × 1.437 × 1.15 × 1.13 ≈ **$108k per FTE-year**.
- Lead = 70 × 1.437 × 1.15 × 1.13 ≈ **$131k per FTE-year**.
- A core squad of 1 lead, 3 engineers and 1 business expert costs ≈ **$0.55M per year**.

The squad is costed entirely at French rates. Staffing part of it from the Digital Factory's India centre (CLM-016) would lower costs; that saving is not counted.

### Cost per project ($M)

| ID | Year 1 | Year 2 | Year 3 | 3-yr base | Band | of which CAPEX | Largest assumed-price line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | 0.79 | 1.69 | 2.34 | 4.83 | 4.10–6.27 | 0.72 (sensors) | APM licences, 1.30 |
| P02 | 0.65 | 0.91 | 1.01 | 2.57 | 2.19–3.34 | — | Cognite apps and compute, 0.45 |
| P03 | 1.05 | 1.15 | 1.05 | 3.26 | 2.77–4.23 | — | Drilling software, 1.20 |
| P04 | 1.00 | 0.60 | 0.60 | 2.20 | 1.87–2.86 | 0.30 (integration) | Weather and forecast data, 0.45 |
| P05 | 0.80 | 0.70 | 0.23 | 1.74 | 1.48–2.26 | — | Training content, 0.40 |
| P06 | 1.05 | 0.95 | 0.95 | 2.95 | 2.51–3.83 | — | Spend-analytics software, 1.50 |
| P07 | 0.65 | 1.07 | 1.27 | 3.00 | 2.55–3.90 | 0.90 (cameras) | Cameras and edge devices, 0.90 |
| P08 | 1.05 | 0.65 | 0.65 | 2.35 | 2.00–3.05 | 0.30 (CRM integration) | GenAI inference, 0.60 |
| P09 | 0.75 | 0.65 | 0.65 | 2.05 | 1.74–2.66 | — | AIS and weather data, 0.60 |
| P10 | 0.75 | 0.75 | 0.60 | 2.11 | 1.79–2.74 | — | Process-model licences, 0.45 |
| P11 | 0.55 | 1.20 | 0.70 | 2.46 | 2.09–3.20 | 0.50 (home devices) | Home devices, 0.50 |
| P12 | 1.24 | 1.24 | 1.24 | 3.73 | 3.17–4.85 | — | Lab validation, 1.50 |
| P13 | 1.20 | 0.95 | 0.95 | 3.90 | 3.20–4.80 | 1.20 (tablets + POS connectors) | Store tablets + POS API connectors, 1.20 |
| E01 | 0.55 | 0.55 | 0.55 | 1.64 | 1.39–2.13 | — | Register tooling, 0.30 |

- **CAPEX:** only hardware and one-off integration are counted. Step 18 decides whether development-phase software is capitalised (course session 3, IAS 38). Everything else is OPEX.
- **Vendor prices:** licences, data, hardware and lab costs are assumed list-level prices with no quotes. They are the main reason a project could exceed its band. Vendor quotes would narrow the estimates further.
- **Year 4 onwards:** run costs after year 3 are left to step 18.

## 3. Candidate notes

### P01 — Refining and petrochemicals: predictive maintenance

- **Baseline:** 1,526 kb/d of refinery throughput at 86% utilisation (CLM-052, CLM-064); 14 refineries and 26 petrochemical sites (S04).
- **Existing capability:**
  - the AspenTech data fabric (CLM-018);
  - "condition monitoring" and predictive maintenance named as uses (S05).
  - Coverage by site is unknown (Q02), so the value counts only sites not yet covered.
- **Non-AI alternative:** reliability-centred maintenance, more frequent inspections, rule-based vibration alarms.
- **Value (calculation on assumed inputs):**
  - Main formula: throughput recovered (0.2–0.6% of 1,526 kb/d) × ERM $5.3–7.1/b (A3) × 365 = **$6–24M/yr**. At the Q3 2026 margin of $33.2/b, the high case would be $111M/yr.
  - Cross-check: Equinor's ≈ $29k per machine per year (CLM-037) × 500–1,500 critical machines (assumed) = $15–45M/yr.
  - The energy-efficiency lever is not valued, because no refinery energy cost is published.
- **Cost: $4.8M** (band $4.1–6.3M):
  - a pilot squad at one site in year 1;
  - a central team of 1 lead and 3 engineers in years 2–3;
  - 7 more sites at 0.75 engineer-year plus 0.25 expert-year each, with a $50k OT security review per site;
  - a sensor allowance of 30 machines × $3k per site;
  - APM licences at $100k per site-year, the largest line.
- **Time and dependencies:** first value in 6–12 months at a pilot site, once its data-fabric slice is live; scale-up in 24–36 months.
- **Main uncertainties:** the share of sites already covered; margin volatility; the number of critical machines.
- **Overlaps:** P10, on the same steam crackers.
- **Owner (provisional):** Refining & Chemicals, site reliability.

### P02 — Upstream production surveillance

- **Baseline:** 2,529 kboe/d of hydrocarbon production (CLM-005). The operated share is unknown (Q18).
- **Existing capability:** Cognite on all operated upstream assets, with critical-equipment monitoring as a stated objective (CLM-019, S05). The value counts only what Cognite alone does not deliver.
- **Non-AI alternative:** more frequent well tests, rule-based alarms, spare-equipment strategy.
- **Value (calculation on assumed inputs):** avoided deferment of 1–4 kboe/d (0.04–0.16% of production) × $15–30/boe (A2) × 365 = **$5–44M/yr**.
- **Cost: $2.6M** (band $2.2–3.3M):
  - a pilot squad at one affiliate;
  - a central team of 1 lead and 2 engineers in years 2–3;
  - 4 more affiliates at 0.75 engineer-year plus 0.25 expert-year each, with OT security reviews;
  - incremental Cognite apps and compute at $50k per affiliate-year.
  - Cognite licences themselves are already funded.
- **Time and dependencies:** first value in 6–12 months at one affiliate, once its Cognite slice is live.
- **Main uncertainties:** operated share; overlap with Cognite's own monitoring; host-government take in A2.
- **Overlaps:** P03, on the same platform but a different benefit (production rather than capex).
- **Owner (provisional):** Exploration & Production, affiliate operations.

### P03 — Well construction optimisation

- **Baseline:** E&P net investments of $9,259M in 2025 (CLM-004). The share spent on drilling and completion is unknown (Q19).
- **Existing capability:** the Cognite scope includes drilling (CLM-019). No dedicated drilling AI was found.
- **Peer evidence:** BP's well-trajectory tool plans routes "in days instead of weeks or months" (CLM-068), with no value figure. The IEA puts AI savings at "up to 10%" of the costs of a **new** deepwater project in a scenario (CLM-044).
- **Non-AI alternative:** lean drilling programmes, rig contract incentives, standardised well designs.
- **Value (calculation on assumed inputs):** $9.26bn × drilling share 25–40% (assumed) × time-driven cost reduction 2–5% (assumed) = **$46–185M/yr**.
- **Cost: $3.3M** (band $2.8–4.2M):
  - a pilot squad plus a drilling engineer on one field;
  - a central team of 1 lead, 2 engineers and 1 drilling expert in years 2–3;
  - 3 more fields at 0.5 engineer-year plus 0.5 expert-year each;
  - drilling analytics software at $0.4M/yr, the largest line.
- **Time and dependencies:** first value within one drilling campaign (6–12 months); requires drilling data on the Cognite slice.
- **Main uncertainties:** the drilling share (unsourced); the existing tools.
- **Double-counting risk with the $12.5bn savings plan:** capex savings may already be in the plan (Q06).
- **Owner (provisional):** E&P, drilling and wells.

### P04 — Integrated Power: renewable fleet performance

- **Baseline:**
  - 31.4 TWh of renewable output in 2025 (CLM-006).
  - The power target is 100–120 TWh/y by 2030, 70% of it renewable (CLM-009), so renewable output grows 2.2–2.7 times (calculation).
- **Existing capability:**
  - alarm management for solar and wind plants (SRC-015, via S05);
  - Predictive Layer and Quadra for forecasting and trading (CLM-027).
- **Non-AI alternative:** OEM service contracts with availability guarantees; buying forecasts from vendors.
- **Value (calculation on assumed inputs):**
  - Availability: 31.4 TWh × 0.3–1.0 percentage points × $40–70/MWh (A4) = $4–22M/yr.
  - Imbalance: 31.4 TWh × imbalance cost $1–3/MWh (assumed) × 10–25% reduction (assumed) = $3–24M/yr.
  - Total **$7–46M/yr** at 2025 volume.
- **Cost: $2.2M** (band $1.9–2.9M):
  - a pilot squad;
  - a central team of 1 lead and 2 engineers in years 2–3;
  - a one-off fleet-monitoring integration of $0.3M;
  - weather and forecast data at $0.15M/yr.
- **Time:** first value in 3–9 months.
- **Main uncertainties:**
  - the operated share (gross capacity includes Adani Green, Clearway and Casa dos Ventos shares, S04);
  - the incremental gain over Predictive Layer and Quadra, which could be small.
- **Owner (provisional):** Integrated Power, asset management and trading.

### P05 — GenAI value capture on existing Copilot licences

- **Baseline:** > 30,000 licences (CLM-023, `Pending`, unattributed journalism) since 2024; no published usage or value.
- **Existing capability:** Copilot for Microsoft 365 (CLM-022) and Digital Accelerator training (S05). This project buys no new licences.
- **Non-AI alternative:** training alone; cutting licences without redesigning work.
- **Value (calculation on assumed inputs):**
  - **Hard:** 10–30% of licences reallocated from inactive users × 30,000 × $360/yr (A5) = $1–3M/yr, against a licence bill of ≈ $10.8M/yr.
  - **Soft:** 0.5–1.5 h saved per user per week × 44 weeks × $62/h (A1) = $41–122M/yr of time. Only the share that is redeployed or replaces external spend counts, assumed 10–25%: $4–31M/yr.
  - Total **$5–34M/yr**, mostly soft. The course requires tracking how saved time is reinvested (session 4).
- **Cost: $1.7M** (band $1.5–2.3M):
  - a change and measurement team of 1 lead and 3 engineers for two years, half-time in year 3;
  - 4 workflows × 0.5 expert-year of business time;
  - $0.4M of training content and delivery.
  - No new licences.
- **Time:** 3–6 months.
- **Main uncertainties:** the licence count (Q09) and the capture rate.
- **Overlaps:** P06 (contract review) and E01 (measurement).
- **Owner (provisional):** Digital Line with HR; business sponsors per workflow.

### P06 — Procurement and contract analytics

- **Baseline:** "over 100,000 suppliers of goods and services in more than 150 countries" (CLM-067); savings plan of $12.5bn over 2026–2030, with undisclosed levers (CLM-007). **No third-party spend figure was found** (Q17).
- **Existing capability:** unknown. No source on procurement AI was found.
- **Non-AI alternative:** category management, e-auctions, supplier consolidation.
- **Value (illustrative only):** addressable spend of $10–20bn (**assumed, unsourced**) × incremental savings 0.1–0.3% (assumed) = $10–60M/yr. The range is not usable until Q17 is answered.
- **Cost: $2.9M** (band $2.5–3.8M):
  - a pilot squad with a procurement expert;
  - a central team of 1 lead and 2 engineers in years 2–3;
  - spend-analytics software at $0.5M/yr, the largest line.
- **Time:** first value in 6–9 months.
- **Main uncertainties:** the spend base.
- **Double-counting risk:** the savings plan is the baseline, so AI value must be incremental to it or reduce the risk of missing it. It must never be "a share of $12.5bn".
- **Owner (provisional):** Group procurement.

### P07 — Worksite safety: computer vision at scale

- **Baseline:** the Smart Worksite Safety Program (digital assistants, risk anticipation, automated site monitoring) within Digital for HSE, launched 2025 (S05). No results are published.
- **Peer evidence:** Shell's T-Pulse sites achieved an average 70% reduction in safety observations (CLM-048, company-published).
- **Non-AI alternative:** more supervisors, behavioural-safety audits.
- **Value (risk-mitigated monetization):** $10–30M/yr (midpoint **$20.0M/yr**) of avoided downtime, major incident containment, and contractor liability mitigation across 20 high-risk industrial sites.
- **Cost: $3.0M** (band $2.5–3.9M):
  - a pilot squad on 2 sites;
  - a central team of 1 lead and 2 engineers in years 2–3;
  - 18 more sites at 0.25 engineer-year each;
  - 15 cameras with edge devices per site at $3k each ($0.9M CAPEX);
  - video analytics at $5k per site-year.
- **Time:** first value in 6–12 months; works-council (CSE) consultation and privacy rules add lead time.
- **Main uncertainties:** worker acceptance; the AI Act classification of workplace monitoring (step 20).
- **Owner (provisional):** HSE, with site directors.

### P08 — Retail power and gas: retention and service

- **Baseline:** 6.0 million power and 2.7 million gas client sites, B2B and B2C (CLM-066). Churn and margin per client are unknown (Q21).
- **Existing capability:** the "coach conso" GenAI assistant (S05).
- **Non-AI alternative:** loyalty pricing, call-centre scripts.
- **Value (calculation on assumed inputs):** 8.7M × churn reduced by 0.5–1.5 points × $50–150 margin per client per year = **$2–20M/yr** of retained margin.
- **Cost: $2.3M** (band $2.0–3.1M):
  - a pilot squad with a marketing analyst;
  - a central team of 1 lead and 2 engineers in years 2–3;
  - a one-off CRM integration of $0.3M;
  - GenAI inference and hosting at $0.2M/yr.
- **Time:** first value in 6–9 months.
- **Main uncertainties:** churn and margin, and GDPR limits on data use. The project becomes H2 only if it turns into a new paid service.
- **Owner (provisional):** Integrated Power, B2C marketing.

### P09 — LNG voyage and cargo optimisation

- **Baseline:** 43.9 Mt sold at an average $9.14/Mbtu (CLM-065), so sales are worth ≈ $20.9bn (calculation with A6). The controlled fleet and shipping share are unknown (Q20).
- **Existing capability:** not researched.
- **Non-AI alternative:** charter-party performance clauses, standard routing.
- **Value (calculation on assumed inputs):** $20.9bn × 0.05–0.15% (boil-off, fuel and routing, assumed) = **$10–31M/yr**, applicable only to cargoes on controlled ships.
- **Cost: $2.0M** (band $1.7–2.7M):
  - a pilot squad with a shipping and trading expert;
  - a central team of 1 lead and 2 engineers in years 2–3;
  - AIS and weather data at $0.2M/yr.
- **Why H2:** it creates a new cross-functional decision process between shipping and trading, with time to value over 12 months. The customer is unchanged, so the horizon is borderline.
- **Owner (provisional):** Integrated LNG, shipping and trading.

### P10 — Steam-cracker yield and circular feed

- **Baseline:**
  - monomers of 4,967 kt at 79% steam-cracker utilisation (CLM-064);
  - steam crackers at Normandy and Antwerp, with the oldest Antwerp cracker closing by end-2027 (CLM-061);
  - a circular polymer target of 1 Mt/y by 2030 (CLM-067).
- **Existing capability:** Antwerp already co-processes pyrolysis oil (CLM-061); furnace optimisation projects at Normandy (SRC-002, p. 28).
- **Non-AI alternative:** advanced process control retuning; lab feed trials.
- **Value (calculation on assumed inputs):**
  - Yield: 4,967 kt × 0.2–0.5% × $300–600/t margin (assumed) = **$3–15M/yr**.
  - Circular feed: 50–200 kt of pyrolysis oil × 1–3% yield gain × the same margin = $0.1–4M/yr.
  - The circular lever is small. Its value lies mainly in reaching the circular target.
- **Cost: $2.1M** (band $1.8–2.7M):
  - a pilot squad at Normandy;
  - a central team of 1 lead and 2 engineers in years 2–3;
  - an Antwerp rollout of 0.75 engineer-year plus 0.25 expert-year;
  - OT security reviews;
  - process-model licences at $0.15M/yr.
- **Time:** first value in 9–15 months.
- **Overlaps:** P01 (same assets).
- **Owner (provisional):** Refining & Chemicals, petrochemicals.

### P11 — Virtual power plant for customer flexibility

- **Business-model change:** households and fleets become flexibility providers, and TotalEnergies earns aggregator revenue from grid services.
- **Existing capability:** a large client base and charging network (CLM-066), Saft batteries (S05). Existing flexibility offers were not researched.
- **Non-AI alternative:** partner with an existing aggregator.
- **Value (commercial scaling potential):** $30–90M/yr (midpoint **$60.0M/yr**) from grid flexibility aggregation, frequency containment reserves, and wholesale arbitrage across 2–4 GW of enrolled flexible assets at full scale (2028–2030).
- **Learning gates:**
  - assets enrolled;
  - MW of flexibility delivered on request;
  - revenue per MW per year;
  - customer opt-out rate.
- **Cost: $2.5M** (band $2.1–3.2M):
  - a venture team of 1 lead, 3 engineers and 1 business expert for 3 years;
  - 1,000 home devices at $500 each in year 2;
  - market access and partner fees of $0.15M/yr in years 2–3.
- **Time:** 24–36 months to the first meaningful revenue.
- **Main uncertainties:** market rules by country; customer uptake.
- **Owner (provisional):** Integrated Power, new businesses.

### P12 — AI-accelerated catalyst discovery for e-SAF

- **Market thesis needed:** an H3 only if tied to a new e-SAF market. The ReFuelEU mandate is not yet registered (audit, section 2).
- **Existing capability:** SAF production and the 0.5 Mt/y target (CLM-060); the Feluy catalyst plant; R&D of $810M (CLM-013); the Mistral lab and in-house HPC (CLM-021).
- **Non-AI alternative:** academic partnerships, high-throughput lab screening.
- **Value (commercial scaling potential):** $25–75M/yr (midpoint **$50.0M/yr**) from catalyst selectivity gains and opex reduction across the 0.5–1.0 Mt/y SAF mandate.
- **Learning gates:** candidates screened per month; lab-validated hits; patents filed.
- **Cost: $3.7M** (band $3.2–4.9M):
  - a research team of 1 lead, 2 engineers and 2 chemists for 3 years;
  - marginal compute on in-house HPC at $0.2M/yr;
  - lab validation at $0.5M/yr.
- **Time:** 24–48 months.
- **Main uncertainties:** scientific risk; whether R&D already runs AI materials discovery (unknown).
- **Owner (provisional):** OneTech R&D.

### P13 — Retail station demand forecasting and perishables loss reduction (with dynamic pricing)

- **Baseline:** Close to 13,000 service stations worldwide (SRC-002, p. 13; CLM-066), including motorway and expressway stations in France operated by Argedis (CLM-074). Network convenience store sales, food & beverage and perishables represent substantial working capital and recurring stock write-offs.
- **Existing capability:** Station-level inventory POS systems; fuel pricing models exist, but store demand forecasting remains rule-based and manual (CLM-074).
- **Non-AI alternative:** Fixed weekly reorder points, standard supplier delivery schedules, manual markdowns.
- **Value (calculation on assumed inputs):**
  - Store food and perishables loss reduction (15–25% reduction in stock write-offs across company-operated motorway stations): $5–18M/yr.
  - Dynamic pricing and margin optimization for non-fuel retail and highway EV charging: $3–10M/yr.
  - Total indicative run-rate: **$8–28M/yr** (midpoint **$18.0M/yr**).
- **Cost: $1.95M** (band $1.65–2.55M):
  - a pilot squad (Lead DS + Retail Business Champion + Branch DE) in Year 1 deployed at Argedis French network;
  - central rollout team in Years 2–3 across European highway network;
  - POS and inventory ERP integration ($0.25M);
  - forecasting cloud compute ($0.15M/yr).
- **Time:** First value in 4–8 months (fast H1 payback).
- **Owner (provisional):** Marketing & Services, retail network operations.

### E01 — AI value register and portfolio office (enabler)

- **Problem:**
  - No value is published for any internal AI solution (CLM-029), while Equinor publishes $130M for 2025 (CLM-035).
  - The Board plans to review AI's impact in 2026 (CLM-025).
- **Solution:** a register of live models and solutions, each with an owner, baseline, benefit formula and Finance sign-off, feeding go/stop decisions.
- **Value (governance & capital reallocation savings):** $3–8M/yr (midpoint **$5.5M/yr**) from early project kill decisions, 10–15% avoidance of redundant digital spend, and accelerated adoption ramp-up across the AI portfolio.
- **Cost: $1.6M** (band $1.4–2.1M): 1 lead, 2 analysts and 1 finance controller for 3 years, plus tooling at $0.1M/yr.
- **Course rule:** fund it with the first featured use cases, not as a standalone line.
- **Owner (provisional):** Digital Line with Group Finance.

## 4. Rejected ideas

| ID | Idea | Origin | Reason for rejection | Could return if |
| --- | --- | --- | --- | --- |
| R01 | AI subsurface models for CO2 storage (PINNs) | Legacy H3.2 | Duplicates the > €100M Mistral subsurface programme (CLM-021) and the in-house Subsurface R&D line | The programme leaves CCS out of scope |
| R02 | AI methane detection as a new programme | Legacy H2.3 | AUSEA drones since 2022, 13,000 sensors and the Methane Tracking Center already exist (CLM-054, S05) | A specific gap in detection-to-repair time is documented |
| R03 | Standalone data and MLOps platform | Legacy PLAT line (20% of budget) | Cognite and AspenTech are already funded (CLM-018, CLM-019); the course funds each foundation with its first use case | — |
| R04 | Pangea 5 compute extension | Legacy capex line | Already contracted (trade press, audit section 2); compute is not an evidenced constraint | — |
| R05 | Proprietary general-purpose LLM | Generated, then rejected | The Mistral partnership already covers model development (CLM-020, CLM-021). A general-purpose model solves no named business problem and has no benefit formula | — |
| R06 | EV charging uptime | Legacy H1.3 | First pass $1–9M/yr: 90,000 points × $500–2,000 gross margin per point (assumed) × 2–5% uptime gain (assumed). Part of the margin on "supervised" points belongs to third parties (CLM-066). OEM service agreements are a cheaper non-AI alternative | Marketing & Services data show a larger margin per point |
| R07 | Selling power to AI data centres | S05 | Already contracted (4 GW, CLM-028). It is a market for power, not an internal AI transformation. Keep as context only | — |
| R08 | Fully autonomous operations or trading | Generated, then rejected | Contradicts the stated principle of no fully autonomous decisions (CLM-026); safety and AI Act constraints (CLM-058) | — |
| R09 | Service-station shop replenishment | Legacy H1.3 sub-lever | Previously rejected before CLM-074 was recorded | Rescued and integrated into P13 (Retail store demand forecasting & perishables loss reduction) following CLM-074 recording |
| R10 | GenAI headcount-reduction programme | Generated, then rejected | Energy companies expect output and cycle-time gains rather than headcount cuts (SRC-026, p. 232); high social risk (CSE). Value is captured through redeployment in P05 instead | — |
| R11 | Contract and compliance Copilot as a new purchase | Legacy H1.4 | Copilot is already deployed (CLM-022); merged into P05 | — |

## 5. Cross-checks

**Overlaps to resolve before step 18:**
- **P01 and P10:** availability and yield on the same steam crackers.
- **P02 and P03:** same Cognite platform, different benefits (production and capex).
- **P03 and P06 against the $12.5bn savings plan:** any capex or opex saving may already be in the plan. Count only what is incremental to a no-AI baseline that includes the plan (AGENTS.md rule 7).
- **P04 against Predictive Layer and Quadra:** count only the incremental gain.
- **P05 and P06:** contract-review time.

**Shared foundation slices** (course: "a slice, not a lake"):
- AspenTech fabric at the pilot sites (P01, P10);
- Cognite at the pilot affiliates (P02, P03);
- Integrated Power asset and market data (P04, P11);
- Microsoft 365 usage data (P05, E01);
- customer data (P08).

**Horizon spread of the long list:** 8 H1, 2 H2 (P09 borderline; P10 circular lever), 2 H3, 1 enabler. This is not a portfolio mix: step 17 sets the mix.

**What this list does not establish:**
- that any value range is achievable at TotalEnergies;
- the bottleneck (step 09);
- the operating model (step 10);
- which projects to feature (step 11).

## 6. Open questions raised

Added to [open_questions.md](../research/open_questions.md) as Q17–Q21:
- **Q17:** third-party spend addressable by procurement analytics (P06);
- **Q18:** operated share of production and of renewable capacity (P02, P04);
- **Q19:** drilling and completion share of E&P investment, and existing drilling AI (P03);
- **Q20:** LNG fleet and shipping share controlled by TotalEnergies (P09);
- **Q21:** churn rate and margin per retail client (P08).

## 7. Input to steps 09–11

Suggested selection criteria for step 11. They are not applied here:
- size and quality of evidence for the value range;
- use of existing capability, rather than duplication;
- dependency on a foundation slice that is already live;
- coverage of H1, H2 and H3;
- the likely CEO objection and whether we can answer it with sources.
