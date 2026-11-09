# Full Case Study: Featured Project 3 — P11 Virtual Power Plant for Customer Flexibility

- **Roadmap Step:** 14 — [#14](https://github.com/Xenodion/ai-transformations-navy/issues/14)
- **Status:** Complete Case Study (Featured Case 3 — Energy Transition & Real Option Pillar)
- **Date:** 9 November 2026
- **Authors:** Alexandre Waerniers & Vincent Lamy, Team 4.
- **Operating Branch:** Integrated Power
- **Provisional Horizon:** **Horizon 3** (Transformational Real Option / Decentralized Business Model)
- **Delivery Unit:** Power Venture Agile Trio (*Trinôme Exécutif*) inside Integrated Power Spoke
- **Evidence Base:**
  - `sources/primary/totalenergies_universal-registration-document-2025_2026_en.pdf` (URD 2025, pp. 6, 13, 41, 138)
  - `sources/primary/totalenergies_factbook-2025_2026_en.xlsx` (Factbook 2025, pp. 11, 26, 78, 79)
  - `sources/register.md` (`CLM-004`, `CLM-006`, `CLM-009`, `CLM-026`, `CLM-027`, `CLM-066`, `CLM-069`, `CLM-070`, `CLM-071`)
  - Course Framework: Sessions 1–4 (Case Study Standard Template, H3 Learning Gate Governance)

---

## 1. Problem Statement, Operational Scope, and Baseline

### 1.1 The Business Problem
TotalEnergies is executing a rapid strategic transformation into an integrated multi-energy major, targeting **100 to 120 TWh/year of net electricity production by 2030** with an industry-benchmark **12% ROACE** (`CLM-009` `[Fact]`). At year-end 2025, Integrated Power operated **34.1 GW of gross installed renewable capacity** (`Factbook 2025`, p. 78 `[Fact]`; `CLM-006`), generated **48.1 TWh of net electricity** (of which **31.4 TWh from solar and wind**, `CLM-006` `[Fact]`), and maintained **5.6 GW of flexible gas-fired CCGT plants** (`Factbook 2025`, p. 79 `[Fact]`). Simultaneously, TotalEnergies serves **6.0 million retail electricity customer sites** and operates or supervises **close to 90,000 electric vehicle (EV) charging points** (`URD 2025`, p. 13 `[Fact]`; `CLM-066`).

However, the rapid penetration of intermittent solar and wind generation creates acute structural challenges across European power markets:
- **Intraday Volatility & Negative Pricing:** Surging midday solar generation drives wholesale spot electricity prices to zero or negative levels, while evening demand peaks create severe price spikes ($200–$500/MWh).
- **The Balancing Challenge:** Transmission System Operators (TSOs, such as RTE in France, TenneT in Germany/Netherlands, and Elia in Belgium) require massive sub-second balancing capacity (Frequency Containment Reserves — FCR, and automatic Frequency Restoration Reserves — aFRR) to stabilize the 50 Hz grid frequency.
- **The Monetization Blind Spot:** TotalEnergies optimizes its own utility-scale solar/wind farms and CCGTs through Quadra Energy and Predictive Layer (`CLM-027` `[Fact]`), but **leaves customer-side decentralized energy resources completely uncoordinated**. Hundreds of thousands of decentralized customer batteries (including TotalEnergies' subsidiary **Saft** storage systems), smart bidirectional EV chargers, heat pumps, and commercial cold-storage units sit idle behind the meter.
- **The Commercial Threat:** Independent aggregators (e.g. Octopus Energy's KrakenFlex, Tesla Energy, Next Kraftwerke) are aggressively contracting retail customers, capturing lucrative grid balancing payments ($40k–$80k per MW/year) and disintermediating TotalEnergies from its own 6.0 million retail accounts.

### 1.2 Baseline Financial and Operational Metrics
- **Integrated Power Net Investments:** **$2,776M in 2025** ($3,869M in 2024, `Factbook 2025`, p. 26 `[Fact]`; `CLM-004`).
- **Renewable Production Baseline:** **31.4 TWh in 2025** (`Factbook 2025`, p. 78 `[Fact]`). To reach the 2030 target (70% of 100–120 TWh from renewables, `CLM-009` `[Fact]`), renewable output must expand by **2.2× to 2.7×**.
- **Customer & Asset Baseline:**
  - Retail Customer Base: **6.0 million electricity sites** across France, Spain, and Belgium (`URD 2025`, p. 13 `[Fact]`; `CLM-066`).
  - EV Charging Network: **89,900 charging points** (`Factbook 2025`, p. 11 `[Fact]`).
  - Battery Capability: Proprietary stationary storage systems developed by subsidiary **Saft** (`S05` `[Fact]`).
- **Project P11 Operational Scope:**
  - *Phase 1 Venture Pilot (Years 1–2):* Aggregate **1,000 residential battery systems (Saft/Enphase)** and **2,500 smart EV chargers** across France and Belgium (~25 MW aggregate capacity).
  - *Phase 2 Commercial Scale (Years 3–5):* Scale to **2,000 MW to 4,000 MW (2 to 4 GW)** of flexible capacity by enrolling commercial B2B fleets, industrial cold-storage, and residential EV smart charging.

---

## 2. Why AI and Non-AI Alternatives

### 2.1 Why Machine Learning is Required
Orchestrating 100,000+ decentralized battery inverters and EV chargers into a single responsive utility-grade generator requires sub-second stochastic optimization:
- **State-of-Charge (SoC) & Driving Pattern Prediction:** Machine learning models predict when individual EV owners will disconnect and commute, ensuring vehicles are fully charged by morning while dynamically bidding unused battery buffer into midnight grid reserves.
- **Sub-Second Grid Frequency Tracking:** TSOs require automated frequency response within **2 to 4 seconds**. The AI engine continuously recalculates optimal aggregate dispatch across thousands of micro-assets to fulfill grid response commitments without exceeding individual battery thermal limits.
- **Multi-Market Price Arbitrage:** Reinforcement learning agents co-optimize bids across three simultaneous markets: wholesale day-ahead (EPEX SPOT), intraday continuous, and TSO ancillary balancing reserves.

### 2.2 Rejection of Non-AI Alternatives

| Non-AI Alternative Evaluated | Operational Mechanism | Why It Fails / Is Sub-Optimal |
| :--- | :--- | :--- |
| **Option A: Static Time-of-Use Tariffs (Heuristic Peak/Off-Peak)** | Offer fixed contractual discounts for charging between 23:00 and 06:00. | **Creates secondary demand spikes:** Automatically triggers all EVs to charge simultaneously at 23:01, overloading local distribution substations; cannot respond to real-time grid frequency emergencies. |
| **Option B: Centralized Gas Peaker Plants (CCGT)** | Rely exclusively on TotalEnergies' 5.6 GW of gas-fired CCGTs (`Factbook p. 79`) to balance renewables. | **High carbon & operating cost:** Firing open-cycle gas turbines costs $80–$140/MWh in fuel and EU ETS carbon permits; cannot provide the sub-second response times delivered by distributed inverter-based batteries. |
| **Option C: Third-Party Turnkey Aggregator Partnerships** | Partner with a third-party software aggregator (e.g. Next Kraftwerke / KrakenFlex) on a revenue-share model. | **Strategic Surrender of Customer Margin:** Third parties capture 40% to 60% of the flexibility margin and control the customer relationship, disintermediating TotalEnergies from its electricity retail base. |

---

## 3. Horizon Justification: Why Horizon 3 (Transformational Real Option)

Applying the Course Session 2 Three Horizons framework (Baghai, Coley & White, 1999) using the **Four Placement Questions**:

| Placement Question | Project P11 Evaluation | Horizon Implication |
| :--- | :--- | :---: |
| **Q1: Does it change the customer?** | **YES.** Retail electricity consumers and EV drivers transform from passive commodity buyers into active decentralized energy producers and grid service providers (*prosumers*). | **H3 (Transformational)** |
| **Q2: Does it change the business model?** | **YES.** TotalEnergies shifts from earning a thin utility retail margin (0.5–1.0 c€/kWh) to earning high-margin aggregator commission fees and capacity market service margins ($15k–$25k/MW/yr). | **H3 (Transformational)** |
| **Q3: Is the underlying technology proven internally?** | **NO.** While Saft builds hardware and Quadra trades on wholesale exchanges, orchestrating a real-time decentralized customer VPP at sub-second speeds is a novel, AI-native capability for TotalEnergies. | **H3 (Transformational)** |
| **Q4: Is time to first value under 12 months?** | **NO (24 to 36 months).** Enrolling customer fleets, securing TSO regulatory certification, and qualifying hardware gateways requires multi-year stage-gating. | **H3 (Transformational)** |

*Governance Rule (AGENTS.md Rule 7 & Course Session 2):* **Never judge an H3 initiative by an H1 ROI.** Project P11 is governed strictly as an **Exploratory Real Option with Staged Learning Gates**. Initial capital is ring-fenced to validate customer enrollment and technical dispatch; full scaling capital is committed only when technical and commercial milestones are proven.

---

## 4. Data Assets and Dependencies (Hard vs Soft)

```
[Smart Meter / Linky Feeds] (Hard) ---+
  (10-minute interval data)           |---> [VPP AI Orchestration Engine] ---> [TSO Balancing Market]
[EV Charger / Saft BMS APIs] (Hard) --+          (Cloud / Edge Aggregator)            (RTE / TenneT Dispatch)
[TSO 4-Second Frequency API] (Hard) --+
[EPEX SPOT Price Feeds] (Soft)     ---+
```

### 4.1 Data Pipeline Dependencies
1. **TSO Grid Frequency & Dispatch Protocol (Hard Dependency):** Real-time 4-second SCADA frequency signal and automated dispatch interface with grid operators (RTE / TenneT / Elia). Requires formal TSO regulatory pre-qualification in Month 6.
2. **Device Telemetry & Control Protocol (Hard Dependency):** Secure bidirectional API connections to EV chargers (OCPP 2.0.1 protocol) and residential battery inverters (Modbus TCP / IEEE 2030.5).
3. **Smart Metering Infrastructure (Hard Dependency):** Enedis / Linky daily automated consumption curve access in France, authorized via customer consent under GDPR.
4. **EPEX SPOT Wholesale Price Feeds (Soft Dependency):** Day-ahead and 15-minute intraday continuous price curves. Already operational within Quadra Energy (`CLM-027` `[Fact]`).

---

## 5. Sourcing Strategy: Build, Buy, or Blend

Applying the Gartner (2025) Sourcing Framework for Horizon 3 (*"Upend: disrupt markets — Build or Blend"*):

| Sourcing Route | Technical Description | Strategic Evaluation & Decision |
| :--- | :--- | :--- |
| **Buy (Commercial SaaS DERMS)** | License a generic cloud Distributed Energy Resource Management System (e.g. AutoGrid, EnergyHub). | *High Recurring Cost & Rigidity:* Vendor charges $15–$25 per enrolled device/year; cannot interface dynamically with Quadra Energy's proprietary European trading desk algorithms. |
| **Build (100% In-House Software)** | Code all device drivers, telemetry protocols, and TSO gateways from scratch in Paris TDF. | *Rejected:* Re-invents standardized protocol stacks (OCPP, OpenADR); delays TSO regulatory certification by over 18 months. |
| **BLEND (Preferred Strategy)** | **Certified OpenDERMS Middleware + In-House Proprietary AI Dispatch & Trading Optimization.**<br/>• Procure certified, pre-qualified device gateway middleware for device connectivity and TSO protocol compliance.<br/>• TotalEnergies' Power Venture Trio builds the proprietary reinforcement learning dispatch engine, directly integrated with Quadra Energy's trading desks.<br/>• *Hardware Decoupling Architecture:* While the Phase 1 pilot equips 1,000 residential homes with physical telemetry gateways ($500/box = $0.50M CAPEX) for TSO laboratory certification, **Phase 2 and 3 commercial scaling incurs zero customer hardware capex**, connecting directly via native **cloud-to-cloud OEM APIs** (OCPP 2.0.1 for EV chargers, Enphase/Tesla/Saft cloud APIs, and industrial Modbus BMS gateways already funded by C&I customers). | **ACCEPTED.** Accelerates time-to-market, eliminates customer hardware subsidies at scale, ensures regulatory grid compliance, and retains 100% of proprietary algorithmic trading alpha and customer relationship equity. |

---

## 6. Pilot, Rollout, Governance, and Schedule

### 6.1 Delivery Engine: The Power Venture Agile Delivery Trio
To eliminate cross-entity delivery latency (`CLM-074`), P11 is executed by a dedicated **Agile Delivery Trio**:
- **Lead Data Scientist (TDF Hub / Power Seconded, Full-Time):** Reinforcement learning algorithms, stochastic battery degradation models, real-time dispatch optimization (`CLM-016` `[Disputed Fact]`).
- **Power Flexibility Business Champion (Integrated Power New Businesses, 40% Ring-Fenced Time):** Senior commercial manager co-funded by Integrated Power from Day 1 (`CLM-062` `[Fact]`). Owns customer recruitment, tariff design, TSO relationship, and signing P&L benefits.
- **Branch Data Engineer (Integrated Power IT Spoke, Dedicated):** Builds high-throughput IoT streaming pipelines, OCPP charger gateways, and TSO SCADA API connections.

### 6.2 Staged Deployment Phasing and Learning Gates

```
Month 00-06: Architecture & TSO Pre-Qualification (Middleware setup, RTE grid compliance test)
Month 07-12: Asset Enrollment Pilot (1,000 residential batteries & 2,500 smart EV chargers enrolled)
Month 13-18: Live Grid Balancing Trial (FCR & aFRR active dispatch; Month 18 Stop Rule)
Month 19-24: Commercial Rollout Wave 1 (Expansion to 100 MW flexible pool across France & Belgium)
Month 25-36: Full Scale Commercial Expansion (Expansion to 500 MW; roadmap to 2-4 GW by 2030)
```

| Milestone Gate | Target Date | Operational Deliverable | Staged Learning Gate & Decision Rule |
| :---: | :---: | :--- | :--- |
| **Gate 1 (TSO Prequalification)** | **Month 6** | Formal RTE / TenneT laboratory dispatch certification. | Sub-second telemetry latency verified; zero grid security defects. |
| **Gate 2 (Asset Enrollment)** | **Month 12** | 3,500 customer assets enrolled on smart VPP app. | Enrollment acquisition cost $< \$150/\text{asset}$; device connectivity uptime $\ge 98\%$. |
| **Gate 3 (Stage Gate 1 / Kill Gate)** | **Month 18** | 6-month live TSO grid balancing trial across 25 MW pool. | **3-Tier Gate Rule:**<br/>• **Tier 1 ($\ge 95\%$ dispatch success, $\le 5\%$ opt-out):** Full Go; release Year 3 capital ($0.71M).<br/>• **Tier 2 (90.0%–94.9% dispatch or 5.1%–9.9% opt-out):** 90-day technical probation.<br/>• **Tier 3 ($< 90.0\%$ dispatch or $\ge 10.0\%$ opt-out): Hard Stop Rule;** project terminated immediately. |
| **Gate 4 (Commercial Launch)** | **Month 24** | 100 MW commercial pool live in wholesale & reserve markets. | Net flexibility margin verified $\ge \$12,000/\text{MW/year}$; customer retention $\ge 92\%$. |
| **Gate 5 (Full Scale)** | **Month 36** | 500 MW live pool; commercial scaling toward 2–4 GW target. | Annual run-rate value reaches $\ge \$6.0\text{M/yr}$; clears transition to H2 scaling. |

---

## 7. Economic Model: CAPEX, OPEX, and Benefit Formulas

### 7.1 Three-Year Investment Budget ($2.46M Total)

Costs are built bottom-up using registered labor and equipment rates:
- Lead Data Scientist: €70k gross × 1.437 employer charges × 1.15 overhead × 1.13 USD/EUR = **$131k/yr** (`CLM-069`, `CLM-070`, `CLM-071` `[Calculation]`).
- Branch Data Engineer: €58k gross × 1.437 × 1.15 × 1.13 = **$108k/yr** (`CLM-069`, `CLM-070`, `CLM-071` `[Calculation]`).
- Business Champion (40% time + backfill allowance): $98.5k × 0.40 + $50k backfill = **$89.4k/yr** (`CLM-062` `[Fact]`, `[Calculation]`).
- Core squad personnel cost: **$328.4k/yr** (~$0.99M over 3 years) `[Calculation]`.

| Cost Category | Year 0 ($M) | Year 1 ($M) | Year 2 ($M) | Year 3 ($M) | 3-Year Total ($M) | Classification | Accounting Basis & Assumptions |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Power Venture Agile Trio** | 0.08 | 0.25 | 0.33 | 0.33 | **0.99** | OPEX | 1 Lead DS + 1 Branch DE + 1 Flexibility Champion (co-funded). |
| **Pilot IoT Gateways (1,000 Homes)** | 0.35 | 0.15 | 0.00 | 0.00 | **0.50** | CAPEX (Y0-Y1) | 1,000 pilot smart gateways at $500 each for TSO certification. Phase 2/3 scaling uses zero-capex cloud-to-cloud APIs. |
| **DERMS Middleware & TSO Testing** | 0.07 | 0.10 | 0.15 | 0.15 | **0.47** | OPEX | OpenDERMS cloud licenses & RTE/TenneT certification fees. |
| **Market Access & Aggregator Fees** | 0.00 | 0.05 | 0.22 | 0.23 | **0.50** | OPEX | Wholesale exchange market memberships & balancing reserve bonding. |
| **TOTAL PROJECT ENVELOPE** | **0.50** | **0.55** | **0.70** | **0.71** | **2.46** | **Band: $2.09M – $3.20M** | Clears within Integrated Power branch authority (`Factbook p. 26`). |

### 7.2 Commercial Valuation Formula (Scale Phase)
At full commercial scale (Years 4–5), economic value is generated through capacity reserve payments and wholesale peak/off-peak arbitrage:

$$\text{Total Annual Value} = \text{Capacity}_{\text{aggregated}} \times (\text{Margin}_{\text{FCR/aFRR}} + \text{Margin}_{\text{arbitrage}}) \times (1 - \text{Share}_{\text{customer}})$$

- **Aggregated Flexible Capacity (3,000 MW / 3 GW Target):**
  - *Commercial & Industrial (C&I) B2B Loads (50%):* **1,500 MW** (cold storage, manufacturing HVAC, water treatment; large individual loads of 1–10 MW connected via existing BMS gateways).
  - *EV Smart Charging Fleets (33%):* **1,000 MW** (100,000 connected EVs @ 10 kW flexible charging buffer across 89,900 public and workplace points, `CLM-066` `[Fact]`, connected via cloud-to-cloud OCPP 2.0.1 APIs).
  - *Residential Batteries & Solar Prosumers (17%):* **500 MW** (~70,000 residential batteries @ 7 kW flexible buffer connected via Enphase/Tesla/Saft cloud APIs).
- **Gross Market Value per MW/year:** **$35,000/MW/year** ($20k from TSO FCR/aFRR capacity payments + $15k from intraday wholesale price arbitrage) `[Assumption]`.
- **Customer Revenue Share:** 42.8% returned to participating customers via electricity bill credits ($15k/MW/year).
- **Net Retained TotalEnergies Value:**
  $$\text{Net Margin} = \$35,000 - \$15,000 = \mathbf{\$20,000 \text{ per MW/year}}$$
  $$\text{Total Steady-State Annual Run-Rate} = 3,000 \text{ MW} \times \$20,000/\text{MW/yr} = \mathbf{\$60.00M/yr} \quad (\text{range: } \$30.0\text{M} – \$90.0\text{M/yr}) \quad \text{`[Calculation on assumed inputs]`}$$

---

## 8. Multi-Scenario Economics and 5-Year Cash Flows

Applying Course Session 3 financial standards (**15.0% Real Option hurdle rate**, 5-year evaluation window, staged venture ramp):

### 8.1 Five-Year Cash Flow Waterfall (Base Case)

- **H3 Option Phasing:** Years 1–2 generate zero cash flow (venture development & pilot trials). Year 3 delivers initial commercial pilot revenue ($6.0M across 100 MW pool). Years 4–5 scale to 1.5 GW and 3.0 GW ($30.0M and $60.0M/yr).
- **Run-Rate Opex after Year 3:** $0.80M/yr (cloud telemetry, MLOps maintenance, and regulatory interface).

| Financial Metric ($M) | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | 5-Year Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Gross Value Generated** | 0.00 | 0.00 | 0.00 | 6.00 | 30.00 | 60.00 | **$96.00M** |
| **Project Expenditure (CAPEX+OPEX)** | -0.50 | -0.55 | -0.70 | -0.71 | -0.80 | -0.80 | **-$4.06M** |
| **Net Operational Cash Flow** | **-0.50** | **-0.55** | **-0.70** | **+5.29** | **+29.20** | **+59.20** | **+$91.94M** |
| **Discount Factor (15% H3 Hurdle)**| 1.000 | 0.870 | 0.756 | 0.658 | 0.572 | 0.497 | — |
| **Discounted Cash Flow (DCF)** | -0.50 | -0.48 | -0.53 | +3.48 | +16.70 | +29.42 | **NPV = +$48.10M** |

*Payback Accounting Methodology:* On an annual linear cash-flow interpolation, cumulative net cash turns positive in Year 3 (**Month 28.0 undiscounted / Month 29.2 discounted**); under operational venture accounting (where commercial revenues scale following Gate 5 full-scale deployment in Month 36), full cumulative equity payback is conservatively accounted at **Month 40 (3.3 years)**.  
*Corporate Hurdle Benchmarking:* Discounted at TotalEnergies' corporate 12% rate, **NPV = +$54.37M**.

### 8.2 Three-Scenario Sensitivity Analysis

| Scenario | Aggregated Capacity (2030) | Annual Run-Rate ($M/yr) | 5-Year Net Cash ($M) | NPV @ 15% Hurdle ($M) | NPV @ 12% Hurdle ($M) | Payback Period |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Downside Case (Delayed Scale)** | 1,500 MW | $30.00M/yr | +$40.9M | **+$22.6M** | **+$25.7M** | **45 months** |
| **Base Case (Target Ramp)** | **3,000 MW** | **$60.00M/yr** | **+$91.9M** | **+$48.1M** | **+$54.4M** | **40 months** |
| **Upside Case (Accelerated Grid Needs)** | 4,500 MW | $90.00M/yr | +$142.9M | **+$74.2M** | **+$83.8M** | **37 months** |

*Scenario Ramp Documentation:* Downside Case models slow market adoption (0% Y1–Y2, $3M Y3, $15M Y4, $30M Y5); Base Case models ($0M Y1–Y2, $6M Y3, $30M Y4, $60M Y5); Upside Case models ($0M Y1–Y2, $10M Y3, $45M Y4, $90M Y5).

---

## 9. Frontline Adoption, Change Management, Risks, and Kill Rules

### 9.1 Customer Adoption & Experience Protection
The primary failure mode in consumer VPPs is customer opt-out: if an EV owner wakes up in the morning to find their vehicle battery at 40% because the VPP discharged it overnight, they immediately cancel the service.
- **The "Guaranteed Mobility" SLA:** The customer mobile app features an explicit guarantee: *"Your vehicle will always be charged to at least 85% by your requested departure time (e.g. 07:00). TotalEnergies only flexes the top buffer during off-peak hours."*
- **Transparent Reward Sharing:** Customers receive a real-time monthly dashboard showing cash credits earned from grid balancing (*"You earned €42 this month by helping stabilize the French power grid"*).
- **Human Decision Doctrine:** Customers retain a one-touch "Boost Now" override button in the app that suspends VPP participation instantly (`CLM-026` `[Fact]`).

### 9.2 Risk Management and Regulatory Controls

| Risk Factor | Severity | Probability | Mitigation Mechanism |
| :--- | :---: | :---: | :--- |
| **Battery Accelerated Degradation** | High | Low | AI dispatch limits shallow cycling to $< 0.5\text{ C-rate}$; battery warranty backed by Saft engineering standards. |
| **Cybersecurity Attack on Grid** | Critical | Low | Zero direct internet control; encrypted mutual TLS connections; compliance with EU NIS 2 critical infrastructure directives. |
| **TSO Grid Non-Compliance Penalties** | High | Low | Automated failover pool: if a residential cluster drops offline, Saft utility-scale industrial BESS instantly absorbs the balancing commitment. |
| **Regulatory Grid Code Changes** | Medium | Medium | Active regulatory monitoring in Brussels / Paris via TotalEnergies Public Affairs; modular software interfaces adapt to market rule changes. |

### 9.3 Objective Stage-Gate Kill Rule (Month 18)
- **Review Date:** Month 18 (end of 6-month live balancing trial).
- **Accountable Gate Owners:** VP New Businesses Integrated Power and Lead Data Scientist.
- **Metric Measured:** Documented performance across 3,500 pilot customer assets in France and Belgium.
- **3-Tier Decision Threshold:**
  - **Tier 1 (Full Commercial Go):** Dispatch call success $\ge 95.0\%$, asset availability $\ge 90.0\%$, and customer opt-out rate $\le 5.0\%$. **Action: Approve commercial rollout ($0.71M Year 3 capital released).**
  - **Tier 2 (Conditional Probation):** Dispatch success 90.0%–94.9% or customer opt-out 5.1%–9.9%. **Action: 90-day technical probation; restrict dispatch to wholesale intraday arbitrage only.**
  - **Tier 3 (HARD STOP RULE):** Dispatch success $< 90.0\%$ or customer opt-out rate $\ge 10.0\%$. **Action: Terminate project immediately.** Unspent Year 2 budget ($0.35M) plus Year 3 capital ($0.71M), totaling **$1.06M in ring-fenced capital**, is canceled with zero stranded cost.

---

## 10. Precise Sources, Registered Claims, and Limits

- **Primary Financial & Operational Data:**
  - `Factbook 2025`, p. 78: 34.1 GW gross installed renewables; 48.1 TWh net power generation (31.4 TWh renewables) (`CLM-006` `[Fact]`).
  - `Factbook 2025`, p. 79: 5.6 GW flexible gas-fired CCGT capacity (`[Fact]`).
  - `Factbook 2025`, p. 26: $2,776M Integrated Power net investments in 2025 (`CLM-004` `[Fact]`).
  - `URD 2025`, p. 13: 6.0M electricity client sites; 2.7M gas sites; 89,900 EV charging points (`CLM-066` `[Fact]`).
  - `URD 2025`, p. 41: Integrated Power Modelling Strategic Program objectives (`[Fact]`).
  - `CLM-009`: Corporate target of 100–120 TWh/y net electricity production by 2030 with 12% ROACE (`[Fact]`).
- **Internal Capabilities & Labor Benchmarks:**
  - `S05` & `CLM-027`: Proprietary battery technology via Saft; algorithmic trading via Quadra Energy & Predictive Layer (`[Fact]`).
  - `SRC-030` & `SRC-031`: Apec Big Data executive salaries (€58k/€70k) and INSEE employer charges +43.7% (`CLM-069`, `CLM-070` `[Fact]`).
  - `CLM-062`: Group average loaded labor cost $98.5k/yr (`URD 2025`, p. 6 `[Fact]`).
- **Methodological Limitations:**
  - Flexibility margin calculations depend on European TSO reserve auction structures (RTE / TenneT); regulatory changes in capacity market remuneration could compress net margins by 10%–20%.
  - Customer enrollment assumes participation incentives remain attractive after electricity bill tax credits.
