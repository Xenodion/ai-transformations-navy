# Non-Featured Candidate Projects: Reserve Cards and Sequencing

- **Roadmap Step:** 16 — [#16](https://github.com/Xenodion/ai-transformations-navy/issues/16)
- **Status:** Complete Deliverable (Step 16)
- **Date:** 9 November 2026
- **Authors:** Alexandre Waerniers & Vincent Lamy, Team 4.
- **Purpose:** Document short evaluation cards for the nine non-featured candidate initiatives from the long list (`work/projects/long_list.md`), providing indicative economics, uncertainty ratings, and explicit sequencing triggers for subsequent transformation waves.
- **Primary Evidence Inputs:**
  - `sources/primary/totalenergies_universal-registration-document-2025_2026_en.pdf` (URD 2025)
  - `sources/primary/totalenergies_factbook-2025_2026_en.xlsx` (Factbook 2025)
  - `sources/register.md` (`SRC-001` to `SRC-034`, `CLM-001` to `CLM-074`)
  - `work/options/thesis_and_selection.md` (Step 11 Core Selection)
  - `work/finance/totalenergies_ai_portfolio_model.xlsx` (Master Financial Model)

---

## 1. Portfolio Synthesis & Phasing Overview

While the transformation proposal focuses its initial 3-year execution capacity on the **Four Featured Projects** (P01 Refining, P03 Drilling, P11 VPP, P13 Retail M&S) plus Enabler E01 ($16.09M budget, `work/options/thesis_and_selection.md`), TotalEnergies maintains a rich pool of **nine secondary candidate initiatives**.

These projects are not discarded; they represent an **expansion reserve envelope of $22.70M** across 3 years `[Calculation]`, sequentially unlocked as the initial Agile Delivery Trios prove delivery velocity and generate self-financing cash flows.

| ID | Project Name | Operating Branch | Horizon | 3-Yr Cost ($M) `[Calculation]` | Annual Benefit ($M/yr) `[Calculation]` | Time to First Value / Payback | Uncertainty | Portfolio Status | Activation Trigger |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **P02** | Upstream Production Surveillance | E&P | **H1** | $2.57M | $24.5M ($5–44M) | 6–12 mo / 9 mo | High | **Reserve (Wave 2)** | Gate 3 of P03 cleared; Cognite APM slice live on operated platforms. |
| **P04** | Renewable Fleet Availability | Integrated Power | **H1** | $2.20M | $26.5M ($7–46M) | 3–9 mo / 6 mo | High | **Reserve (Wave 2)** | Interconnection telemetry stabilized across 100+ utility solar/wind sites. |
| **P05** | Copilot Workflow Redesign | Enterprise / Digital | **H1** | $1.74M | $19.5M ($5–34M) | 3–6 mo / 4.5 mo | Medium | **Reserve (Wave 2 — Self-Financing)** | Audited M365 license inactivity via E01; funded directly out of software clawback ($1–3M/yr). |
| **P06** | Procurement Spend Analytics | Corporate Procurement| **H1** | $2.95M | $35.0M ($10–60M) | 6–9 mo / 7.5 mo | Very High | **Reserve (Wave 2)** | Formal audit of third-party addressable spend base (Q17 closed). |
| **P07** | Worksite Safety Computer Vision | HSE Operations | **H1** | $3.00M | $20.0M ($10–30M) | 6–12 mo / 6–10 mo | Medium | **Reserve (Wave 2)** | Works council (CSE) consultation & site camera ATEX certification completed. |
| **P08** | Retail B2B Retention & Service | Integrated Power | **H1** | $2.35M | $11.0M ($2–20M) | 6–9 mo / 7.5 mo | High | **Reserve (Wave 2)** | Integrated Power smart-meter billing data stabilized & B2B churn baseline consolidated. |
| **P09** | LNG Voyage Optimization | Integrated LNG | **H2** | $2.05M | $20.5M ($10–31M) | 12–18 mo / 15 mo | High | **Reserve (Wave 2)** | Controlled LNG carrier charter contracts & AIS data pipeline qualified (Q20). |
| **P10** | Steam-Cracker Yield & Circular Feed | Refining & Chemicals | **H2** | $2.11M | $9.0M ($3–15M) | 9–15 mo / 12 mo | High | **Reserve (Wave 2)** | Restricted to Normandy & Antwerp Cracker 2, excluding retiring Cracker 1 (CLM-061); post-P01. |
| **P12** | e-SAF Catalyst Discovery | OneTech R&D | **H3** | $3.73M | $50.0M ($25–75M) | 24–48 mo / Option | Very High | **Reserve (Wave 3)** | Feluy laboratory screening milestones reached & EU ReFuelEU airline off-take contracts signed. |
| **TOTAL**| **9 Reserve Candidates** | **All Segments** | — | **$22.70M** | **Non-additive (~$80–120M/yr cash potential)\*** | — | — | — | — |

*\*Note on Benefits (AGENTS.md Rule 7 & long_list.md:61)*: Individual candidate benefits must never be naively added up into a single headline. They reflect gross unconstrained potential across overlapping scopes and wide uncertainty bands. In practice, secondary projects are filtered and funded in sequential waves based on verified P&L realization.

---

## 2. Detailed Project Evaluation Cards

---

### Card 01 — P02: Upstream Production Surveillance & Deferment Avoidance

* **Operating Branch & Lead Entity:** Exploration & Production (E&P), Affiliate Operations.
* **Provisional Horizon:** **Horizon 1** (Core Production Optimization).
* **Business Problem & Operational Baseline:**
  - TotalEnergies produces **2,529 kboe/d of hydrocarbons** (`Factbook 2025`, p. 11 `[Fact]`; `CLM-005`).
  - Production deferment (unscheduled choke throttling, sand ingress, gas-lift instability, electrical submersible pump trips) causes an estimated 0.5% to 1.5% in avoidable deferred production across operated upstream platforms.
* **AI Solution & Technical Approach:**
  - Deploy automated production surveillance models on top of **Cognite Data Fusion** (`URD 2025`, p. 43 `[Fact]`; `CLM-019`).
  - Physics-augmented neural networks ingest real-time downhole pressure/temperature gauges, multiphase flowmeters, and surface chokes to detect well liquid loading and gas-lift instability 5 to 10 days before production deferment occurs.
* **Indicative Economics:**
  - *3-Year Investment:* **$2.57M** (Band: $2.19M–$3.34M; pilot squad in Year 1, scaling to 4 operated affiliates in Years 2–3).
  - *Annual Benefit at Scale:* **$24.5M/yr** (Range: $5.0M – $44.0M/yr `[Calculation on assumed inputs]`), based on avoiding 1 to 4 kboe/d of deferred production at an upstream cash margin of $15–$30/boe (`CLM-005`, `long_list.md`, A2).
  - *Expected Payback:* **9 months**.
* **Key Uncertainties & Limits:**
  - Overlap with Cognite's native out-of-the-box asset performance monitoring (APM) tools. TotalEnergies must avoid paying twice for what Cognite software already delivers.
* **Decision & Sequencing Status:** **RESERVE (Wave 2).**
  - *Activation Trigger:* Commenced upon successful completion of P03 Gate 3 (Month 12), ensuring the Cognite upstream ingestion pipeline is fully hardened before adding production well surveillance.

---

### Card 02 — P04: Renewable Fleet Availability & Imbalance Triage

* **Operating Branch & Lead Entity:** Integrated Power, Asset Management and Power Trading.
* **Provisional Horizon:** **Horizon 1** (Asset Performance Management).
* **Business Problem & Operational Baseline:**
  - TotalEnergies operated **34.1 GW of gross installed renewables** at end-2025 (`Factbook p. 78`, `CLM-006` `[Fact]`), generating **31.4 TWh of renewable electricity** (`Factbook p. 78`, `CLM-006` `[Fact]`), with targets to reach 100–120 TWh/y by 2030 (`CLM-009` `[Fact]`).
  - Expanding wind and solar assets face inverter clipping, wake loss degradation, and grid balancing penalties (imbalance settlement costs) when actual generation deviates from day-ahead forecasts.
* **AI Solution & Technical Approach:**
  - Advanced SCADA alarm clustering and automated inverter fault classification to recover 0.3 to 1.0 percentage points of technical availability across utility-scale solar and onshore wind plants.
  - High-resolution localized satellite cloud-cover and anemometer forecasting to reduce imbalance volumes by 10% to 25%.
* **Indicative Economics:**
  - *3-Year Investment:* **$2.20M** (Band: $1.87M–$2.86M; squad personnel + $0.30M fleet monitoring integration + $0.15M/yr weather data APIs).
  - *Annual Benefit at Scale:* **$26.5M/yr** (Range: $7.0M – $46.0M/yr `[Calculation on assumed inputs]`), multiplying 31.4 TWh by 0.3–1.0 pt availability gain at $40–$70/MWh plus imbalance triage savings.
  - *Expected Payback:* **6 months**.
* **Key Uncertainties & Limits:**
  - Incremental uplift over existing trading and forecasting algorithms already operated by subsidiaries **Predictive Layer** and **Quadra Energy** (`CLM-027` `[Fact]`).
* **Decision & Sequencing Status:** **RESERVE (Wave 2).**
  - *Activation Trigger:* Commenced in Month 12 once OEM telemetry data agreements are standardized across third-party inverter suppliers (Vestas, Siemens Gamesa, Sungrow).

---

### Card 03 — P05: GenAI Copilot Value Capture & Workflow Redesign

* **Operating Branch & Lead Entity:** Enterprise & Digital Line, in collaboration with Group HR and Procurement.
* **Provisional Horizon:** **Horizon 1** (Workforce Productivity / License Cost Optimization).
* **Business Problem & Operational Baseline:**
  - TotalEnergies deployed Microsoft 365 Copilot widely starting in 2024 (`CLM-022` `[Fact]`), with trade press reporting > 30,000 licenses (`CLM-023` `[Fact, Pending]`) representing an estimated annual license commitment of ~$10.8M/yr ($30/user/month).
  - Zero audited productivity gains or P&L cost savings have been published (`CLM-029` `[Unknown]`). As observed locally (`CLM-074` `[Local observation]`), generic deployment without workflow redesign leads to low active utilization and staff resorting to unmanaged consumer AI.
* **AI Solution & Technical Approach:**
  - Automated Copilot telemetry audit to right-size licenses: reallocate licenses from inactive staff to high-frequency users ($1.0M–$3.0M/yr hard cash savings).
  - Redesign 4 specific business workflows (contract review, HSE incident synthesis, joint-venture partner reporting, technical translation) with dedicated prompt templates and time-redeployment tracking.
* **Indicative Economics:**
  - *3-Year Investment:* **$1.74M** (Band: $1.48M–$2.26M; change management team of 1 lead and 3 specialists for 2 years + $0.40M training content; zero new licenses).
  - *Annual Benefit at Scale:* **$19.5M/yr** (Range: $5.0M – $34.0M/yr `[Calculation on assumed inputs]`), of which $1.0M–$3.0M/yr is hard cash license savings, and $4.0M–$31.0M/yr is soft time-savings redeployed to core business tasks.
  - *Expected Payback:* **4.5 months** (on hard license savings alone).
* **Key Uncertainties & Limits:**
  - Course Session 4 warning: *"Soft productivity gains (hours saved) destroy value unless management actively redeploys saved time or cuts external contractor spend."*
* **Decision & Sequencing Status:** **RESERVE (Wave 2 — Self-Financing License Clawback Candidate).**
  - *Activation Trigger:* Activated in Month 12 once Enabler E01 completes the automated Microsoft 365 license inactivity audit; funded directly out of the $1.0M–$3.0M/yr in clawed-back software spend, preserving the core Wave 1 budget ($16.09M) for industrial and operational cases.

---

### Card 04 — P06: Procurement & Contract Analytics

* **Operating Branch & Lead Entity:** Group Corporate Procurement.
* **Provisional Horizon:** **Horizon 1** (Indirect Cost Optimization).
* **Business Problem & Operational Baseline:**
  - TotalEnergies manages a massive supply chain of **"over 100,000 suppliers of goods and services in more than 150 countries"** (`URD 2025`, p. 138 `[Fact]`; `CLM-067`).
  - The group announced a corporate **$12.5bn cash-savings plan over 2026–2030** (`SRC-003`, p. 14 `[Fact]`; `CLM-007`), but levers and procurement splits remain undisclosed. TotalEnergies' third-party addressable spend figure is not publicly disclosed (`Q17` `[Unknown]`).
* **AI Solution & Technical Approach:**
  - Machine learning spend classification, duplicate invoice detection, cross-affiliate rate card benchmarking, and automated contract anomaly analysis across multi-ERP instances (SAP, Oracle).
* **Indicative Economics:**
  - *3-Year Investment:* **$2.95M** (Band: $2.51M–$3.83M; pilot squad + spend analytics software at $0.50M/yr).
  - *Annual Benefit at Scale:* **$35.0M/yr** (Illustrative range: $10.0M – $60.0M/yr `[Calculation on assumed inputs]`), assuming an addressable third-party spend base of $10bn–$20bn and 0.1%–0.3% incremental savings.
  - *Expected Payback:* **7.5 months** `[Calculation on assumed inputs]`.
* **Key Uncertainties & Limits:**
  - High risk of double counting: AI savings must be strictly incremental to the baseline $12.5bn corporate savings plan. Cannot be validated until Q17 (addressable spend base) is resolved.
* **Decision & Sequencing Status:** **RESERVE (Wave 2).**
  - *Activation Trigger:* Unlocked once Group Procurement and Finance complete the baseline third-party spend reconciliation (Q17).

---

### Card 05 — P07: Worksite Safety Computer Vision at Scale

* **Operating Branch & Lead Entity:** HSE Division, in coordination with Site Directors.
* **Provisional Horizon:** **Horizon 1** (Operational Risk Mitigation / Safety KPI).
* **Business Problem & Operational Baseline:**
  - TotalEnergies operates hazardous industrial environments (offshore drilling rigs, high-pressure refineries, chemical plants, LNG terminals).
  - In 2025, TotalEnergies established the *Digital for HSE* Strategic R&T Program (`URD 2025`, p. 42 `[Fact]`), including the Smart Worksite Safety program. Peer benchmark: Shell deployed C3 AI / T-Pulse computer vision, achieving an average 70% reduction in safety observations (`CLM-048` `[Fact]`).
* **AI Solution & Technical Approach:**
  - Edge AI computer-vision analytics on site security cameras (CCTV) to detect precursor safety events: PPE non-compliance (harnesses, helmets in red zones), exclusion zone intrusions during crane lifting, and blocked emergency escape routes.
* **Indicative Economics:**
  - *3-Year Investment:* **$3.00M** (Band: $2.55M–$3.90M; pilot squad on 2 sites + $0.90M CAPEX for 300 edge cameras/processors + $5k/site-yr analytics across 20 industrial sites).
  - *Annual Economic Benefit:* **$20.0M/yr** (Risk-mitigated range: $10.0M – $30.0M/yr `[Calculation on assumed inputs]`), evaluated as avoided major industrial shutdown days, incident insurance premium reductions, and contractor liability mitigation.
  - *Expected Payback:* **6 to 10 months** `[Calculation on risk-avoidance basis]` (avoiding a single major unit trip or containment shutdown across 20 high-risk sites pays back the entire $3.0M program).
  - *Primary Non-Monetary KPI:* 50% to 70% reduction in high-potential (HiPo) safety incidents per 1,000 operating hours.
* **Key Uncertainties & Limits:**
  - Works council (CSE / CSSCT in France) consultation and strict GDPR compliance: system must monitor safety zones exclusively with zero facial recognition or individual worker tracking.
* **Decision & Sequencing Status:** **RESERVE (Wave 2).**
  - *Activation Trigger:* Commenced upon completion of statutory CSE consultation and ATEX Zone 1 camera certification across target sites.

---

### Card 06 — P08: Retail Power & Gas Customer Retention & Service

* **Operating Branch & Lead Entity:** Integrated Power, B2C/B2B Marketing & Customer Care.
* **Provisional Horizon:** **Horizon 1** (Customer Churn & Cost-to-Serve Optimization).
* **Business Problem & Operational Baseline:**
  - TotalEnergies serves **6.0 million power client sites and 2.7 million gas client sites** (`Factbook 2025`, p. 11 `[Fact]`; `CLM-066`).
  - European retail utility markets experience high customer churn (12% to 18% annual churn in competitive retail power) and escalating call-center operational costs.
* **AI Solution & Technical Approach:**
  - Predictive churn modeling using smart meter consumption dynamics and customer service logs.
  - GenAI customer service agents handling routine tier-1 inquiries (billing explanations, contract changes, moving notifications) 24/7, building on the existing customer app (`URD 2025`, p. 43 `[Fact]`). Benchmark: Klarna automated two-thirds of customer chats, saving $40M/yr (Course Session 1).
* **Indicative Economics:**
  - *3-Year Investment:* **$2.35M** (Band: $2.00M–$3.05M; pilot squad + $0.30M CRM integration + $0.20M/yr cloud inference).
  - *Annual Benefit at Scale:* **$11.0M/yr** (Range: $2.0M – $20.0M/yr `[Calculation on assumed inputs]`), based on 0.5–1.5 pt churn reduction across 8.7M customer sites ($50–$150 annual margin per retained site).
  - *Expected Payback:* **7.5 months** `[Calculation on assumed inputs]`.
* **Key Uncertainties & Limits:**
  - High customer privacy constraints (GDPR); customer margin data is commercially confidential (`Q21` `[Unknown]`).
* **Decision & Sequencing Status:** **RESERVE (Wave 2).**
  - *Activation Trigger:* Commenced in Month 18 once Integrated Power smart-meter billing data pipelines are stabilized and B2B churn baselines are consolidated (independent of retail motorway operations).

---

### Card 07 — P09: LNG Voyage and Cargo Optimisation

* **Operating Branch & Lead Entity:** Integrated LNG, Shipping and Trading.
* **Provisional Horizon:** **Horizon 2** (Cross-Functional Adjacent Innovation).
* **Business Problem & Operational Baseline:**
  - TotalEnergies sold **43.9 Mt of LNG in 2025 at an average price of $9.14/Mbtu** (`URD 2025`, pp. 13, 94 `[Fact]`; `CLM-065`), representing approximately **$20.9bn in total LNG sales volume**.
  - LNG shipping involves boil-off gas (BOG) losses (0.08% to 0.15% of cargo volume per day at sea) and heavy bunker fuel consumption. Speed, weather routing, and regasification slot scheduling across global trade routes (US Gulf Coast, Qatar, Europe, Asia) are managed with siloed decision handoffs between shipping logistics and commodity trading desks.
* **AI Solution & Technical Approach:**
  - Integrated hydrodynamic and thermodynamic digital twin of LNG carriers combined with global AIS vessel tracking, metocean wave forecasts, and intraday LNG spot cargo arbitrage price spreads.
  - Dynamically optimizes boil-off reliquefaction vs fuel combustion, vessel speed, and destination cargo diversion.
* **Indicative Economics:**
  - *3-Year Investment:* **$2.05M** (Band: $1.74M–$2.66M; squad with shipping/trading specialists + $0.20M/yr AIS & metocean weather data).
  - *Annual Benefit at Scale:* **$20.5M/yr** (Range: $10.0M – $31.0M/yr `[Calculation on assumed inputs]`), capturing 0.05% to 0.15% efficiency on controlled vessel cargo volumes.
  - *Expected Payback:* **15 months** `[Calculation on assumed inputs]`.
* **Key Uncertainties & Limits:**
  - TotalEnergies' chartered vs spot-market vessel share is unverified (`Q20` `[Unknown]`); savings apply strictly to cargoes transported on TotalEnergies-controlled ships.
* **Decision & Sequencing Status:** **RESERVE (Wave 2).**
  - *Activation Trigger:* Commenced upon completion of Q20 audit (chartered fleet charter-party performance clauses).

---

### Card 08 — P10: Steam-Cracker Yield and Circular Feed Optimisation

* **Operating Branch & Lead Entity:** Refining & Chemicals, Petrochemicals Division.
* **Provisional Horizon:** **Horizon 2** (Advanced Process Control & Circular Transition).
* **Business Problem & Operational Baseline:**
  - TotalEnergies produced **4,967 kt of petrochemical monomers and 4,658 kt of polymers** in 2025 (`Factbook p. 10`, `CLM-064` `[Fact]`) across major steam crackers (Normandy, Antwerp).
  - Group target: reach **1 Mt/y of circular polymers by 2030** (`URD p. 365`, `CLM-067` `[Fact]`). Antwerp already co-processes chemically recycled pyrolysis oil from plastic waste (`CLM-061` `[Fact]`).
  - *Scope Restriction:* TotalEnergies announced the permanent closure of its oldest Antwerp steam cracker by end-2027 (`CLM-061` `[Fact]`). P10 scope is strictly restricted to modern crackers at **Normandy and Antwerp Cracker 2**, deliberately excluding the retiring asset.
  - Furnace yields on steam crackers fluctuate with feedstock composition (naphtha, ethane, circular pyrolysis oil), requiring real-time furnace temperature and residence-time optimization.
* **AI Solution & Technical Approach:**
  - Physics-informed neural network (PINN) modeling furnace cracking kinetics to optimize high-value ethylene and propylene yields (+0.2% to +0.5%) while dynamically adjusting for pyrolysis oil impurities.
* **Indicative Economics:**
  - *3-Year Investment:* **$2.11M** (Band: $1.79M–$2.74M; squad at Normandy/Antwerp + process model licenses).
  - *Annual Benefit at Scale:* **$9.0M/yr** (Range: $3.0M – $15.0M/yr `[Calculation on assumed inputs]`).
  - *Expected Payback:* **12 months** `[Calculation on assumed inputs]`.
* **Key Uncertainties & Limits:**
  - Delineation from P01: P01 optimizes mechanical equipment uptime (pumps/compressors), while P10 optimizes chemical cracking furnace yield.
* **Decision & Sequencing Status:** **RESERVE (Wave 2).**
  - *Activation Trigger:* Commenced in Month 18 once P01 predictive maintenance stabilizes on Normandy rotating equipment.

---

### Card 09 — P12: AI-Accelerated Catalyst Discovery for e-SAF

* **Operating Branch & Lead Entity:** OneTech R&D, New Molecules & Catalyst Division (Feluy, Belgium).
* **Provisional Horizon:** **Horizon 3** (Frontier Scientific Materials Discovery).
* **Business Problem & Operational Baseline:**
  - The EU ReFuelEU Aviation mandate mandates 2% SAF blending by 2025, 6% by 2030, and 70% by 2050. TotalEnergies targets **0.5 Mt/y of SAF capacity by 2028** (`CLM-060` `[Fact]`).
  - Synthetic aviation fuel (e-SAF via Power-to-Liquid / Fischer-Tropsch using green hydrogen and captured CO2) suffers from low catalyst selectivity and extreme synthesis capital costs. Traditional wet-lab catalyst synthesis and autoclaving takes 5 to 10 years per chemical breakthrough.
* **AI Solution & Technical Approach:**
  - Generative molecular models and graph neural networks (GNNs) running on in-house supercomputers (`URD 2025, p. 42`, `CLM-021` `[Fact]`) to predict catalytic binding energies and reaction pathways for CO2 hydrogenation, accelerating laboratory screening by 10×.
* **Indicative Economics:**
  - *3-Year Investment:* **$3.73M** (Band: $3.17M–$4.85M; research squad of 1 lead, 2 ML engineers, 2 quantum chemists + $0.50M/yr lab wet validation).
  - *Long-Term Option Value:* **$50.0M/yr** ($25.0M – $75.0M/yr commercial potential in Years 4–5 `[Assumption]`) based on 3% to 8% opex reduction across the 0.5–1.0 Mt/y SAF mandate.
  - *Staged Learning Gates (Rule 7):* Candidates screened per month; lab-validated catalyst hits; international patents filed. Zero short-term cash payback claimed.
* **Key Uncertainties & Limits:**
  - High scientific exploration risk; independent of power grid VPP operations.
* **Decision & Sequencing Status:** **RESERVE (Wave 3).**
  - *Activation Trigger:* Activated as an exploratory R&D option once OneTech R&D Feluy laboratory screening achieves 10× throughput milestones and commercial airline off-take contracts are signed under the EU ReFuelEU mandate.

---

## 3. Review and Verification Status

- [x] Short evaluation cards completed for all nine non-featured candidate initiatives.
- [x] Indicative benefits, 3-year costs, paybacks, and option values documented with transparent uncertainty bands.
- [x] Reconciled against `long_list.md`, `totalenergies_ai_portfolio_model.xlsx`, and `thesis_and_selection.md`.
- [x] All material claims typed strictly according to AGENTS.md Rule 3 (`[Fact]`, `[Calculation]`, `[Assumption]`, `[Local observation]`, `[Unknown]`).
- [x] Explicit activation triggers and sequencing dependencies established for Waves 2 and 3.
