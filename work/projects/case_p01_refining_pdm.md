# Full Case Study: Featured Project 1 — P01 Refining Predictive Maintenance

- **Roadmap Step:** 12 — [#12](https://github.com/Xenodion/ai-transformations-navy/issues/12)
- **Status:** Complete Case Study (Featured Case 1 — Industrial Cornerstone)
- **Date:** 9 November 2026
- **Authors:** Alexandre Waerniers & Vincent Lamy, Team 4.
- **Operating Branch:** Refining & Chemicals (R&C)
- **Provisional Horizon:** **Horizon 1** (Core Industrial Optimization / Proven Peer Technology)
- **Delivery Unit:** Agile Delivery Trio (*Trinôme Exécutif*) inside Refining & Chemicals Spoke
- **Evidence Base:**
  - `sources/primary/totalenergies_universal-registration-document-2025_2026_en.pdf` (URD 2025, pp. 28, 41, 43, 138)
  - `sources/primary/totalenergies_factbook-2025_2026_en.xlsx` (Factbook 2025, pp. 16, 26, 134, 135)
  - `sources/register.md` (`CLM-004`, `CLM-018`, `CLM-037`, `CLM-041`, `CLM-063`, `CLM-064`, `CLM-069`, `CLM-070`, `CLM-071`)
  - Course Framework: Sessions 1–4 (Case Study Standard Template)

---

## 1. Problem Statement, Operational Scope, and Baseline

### 1.1 The Business Problem
TotalEnergies operates **14 refineries and 26 petrochemical sites worldwide** (`S04`), with a worldwide refining throughput of **1,526 kb/d in 2025** (`Factbook 2025`, p. 135 `[Fact]`; `CLM-064`) at an average refinery utilization rate of **86%** (`Factbook 2025`, p. 135 `[Fact]`). 

Within continuous-process refining and petrochemical assets, production uptime is dictated by the mechanical reliability of heavy rotating machinery:
- **Critical Asset Classes:** Multistage centrifugal gas compressors (wet gas, hydrogen recycle), crude distillation charge pumps, fluid catalytic cracking (FCC) air blowers, boiler feed water pumps, and steam turbine drives.
- **The Cost of Unplanned Outages:** A single unexpected bearing seizure or mechanical seal failure on a primary compressor forces an immediate emergency unit shutdown. This triggers:
  1. *Unplanned Throughput Loss:* 3 to 7 days of lost processing capacity while the unit is cooled, purged, repaired, and restarted ($1.5M to $5.0M in lost refining margin per major incident).
  2. *Flaring and Environmental Penalties:* Emergency trips force significant emergency hydrocarbon flaring, increasing greenhouse gas emissions and risking regulatory environmental sanctions.
  3. *Costly Emergency Maintenance:* Expedited parts shipping, emergency contractor call-outs, and secondary collateral damage to adjacent impellers and shafts (2× to 4× the cost of planned preventative intervention).

### 1.2 Baseline Financial and Operational Metrics
- **Worldwide Throughput Baseline:** **1,526 kb/d** (`Factbook 2025`, p. 135 `[Fact]`), split across regions:
  - France: **470 kb/d** (Normandy, Donges, Feyzin).
  - Rest of Europe: **606 kb/d** (Antwerp, Zeeland).
  - North America: **196 kb/d** (Port Arthur, Texas).
  - Asia and Middle East: **253 kb/d** (Satorp Jubail, etc.).
- **European Refining Margin Marker (ERM) Baseline:** **$7.1/b in 2025** ($5.3/b in 2024, `Factbook 2025`, p. 16 `[Fact]`; `CLM-063`). Q3 2026 ERM rose to $33.2/b (`SRC-005` `[Fact]`), demonstrating high sensitivity to margin spikes.
- **Scope Phasing:**
  - *Phase 1 Pilot (Year 1):* Normandy Platform (TotalEnergies' flagship French refining & petrochemical hub, 250 kb/d capacity, `Factbook p. 134`), instrumenting **~120 critical rotating machines** across the crude distillation (CDU), hydrocracker, and steam cracker units.
  - *Phase 2 Rollout (Years 2–3):* Expansion across **7 major operated platforms** (Antwerp, Donges, Feyzin, Zeeland, Port Arthur, Leuna...) covering **~800 critical rotating machines** in total.
- **Branch Capital Base:**
  - Refining & Chemicals Net Investments: **$1,437M in 2025** (`Factbook 2025`, p. 26 `[Fact]`; `CLM-004`). P01's 3-year cost ($4.83M) represents approximately 0.3% of annual branch capex.

---

## 2. Why AI and Non-AI Alternatives

### 2.1 Why Machine Learning is Required
Rotating machinery failure modes (subsurface fatigue spalling, cavitation erosion, lube-oil film breakdown, aerodynamic surging) develop over weeks through subtle multi-parameter interactions that simple univariate thresholds cannot detect:
- **Multidimensional Anomaly Detection:** The ML engine evaluates high-frequency vibration spectra (accelerometers), bearing metal temperatures, suction/discharge pressures, seal oil differential pressures, motor winding currents, and process flow rates simultaneously.
- **14 to 30 Days Early Warning:** Detects incipient micro-vibration shifts and thermal drift 2 to 4 weeks before conventional alarm thresholds are crossed, enabling maintenance planners to schedule repair interventions during routine unit shift windows rather than suffering emergency shutdowns.

### 2.2 Rejection of Non-AI Alternatives

| Non-AI Alternative Evaluated | Operational Mechanism | Why It Fails / Is Sub-Optimal |
| :--- | :--- | :--- |
| **Option A: Static Vibration Threshold Alarms (Status Quo ISO 10816)** | DCS triggers alarm when overall vibration velocity exceeds fixed threshold (e.g. 7.1 mm/s). | **Fails to prevent damage:** By the time overall vibration crosses the hard threshold, the bearing or impeller is already catastrophically destroyed, forcing emergency shutdown. |
| **Option B: Time-Based Preventative Overhauls (Preventative Maintenance)** | Strip and overhaul compressors on fixed calendar intervals (e.g. every 24 or 36 months). | **Costly and counter-productive:** Replaces healthy parts unnecessarily. Up to 40% of rotating machinery failures are maintenance-induced (infant mortality from reassembly misalignment). |
| **Option C: Increased Human Vibration Rounds** | Reliability technicians manually probe bearing housings with portable vibration pens weekly. | **Too infrequent:** Intermittent sampling misses rapid-onset bearing cage failures occurring between weekly rounds; cannot inspect hazardous ATEX Zone 1 areas continuously. |

---

## 3. Horizon Justification: Why Horizon 1

Applying the Course Session 2 Three Horizons framework (Baghai, Coley and White, 1999) using the **Four Placement Questions**:

| Placement Question | Project P01 Evaluation | Horizon Implication |
| :--- | :--- | :---: |
| **Q1: Does it change the customer?** | **NO.** The customer remains the wholesale refined products market, petrochemical clients, and commercial mobility network. | Core (H1) |
| **Q2: Does it change the business model?** | **NO.** TotalEnergies continues to earn the refining margin (ERM) on processed crude oil and chemical monomers. | Core (H1) |
| **Q3: Is the underlying technology proven?** | **YES.** Industrial predictive maintenance (PdM) is the most proven AI application in the energy sector (Shell > 10,000 machines `CLM-041`; Equinor ~$20M/yr `CLM-037`). | Core (H1) |
| **Q4: Is time to first value under 12 months?** | **YES.** First verified avoided unplanned compressor trip achieved at Normandy pilot in **6 to 9 months**. | Core (H1) |

*Horizon Verdict:* **Horizon 1 (Core Optimization).** P01 optimizes the availability and throughput of core existing assets using proven technology. It generates reliable, verifiable cash flows that help self-finance the group's broader transformation.

---

## 4. Data Assets and Dependencies (Hard vs Soft)

```
[AspenTech Inmation Fabric] (Hard) ---+
  (Deploying 2025-2027 worldwide)     |---> [PdM Anomaly Detection Engine] ---> [SAP PM Work Orders]
[DCS Process Historian] (Hard)     ---+          (Cloud / Edge Inference)             (Maintenance Triage)
[Vibration IoT Edge Sensors] (Hard) --+
```

### 4.1 Data Pipeline Dependencies
1. **AspenTech Inmation™ Industrial Data Fabric (Hard Dependency):** Real-time industrial telemetry ingestion contracted across sites worldwide (`URD 2025`, p. 43 `[Fact]`; `CLM-018`). P01 thin-slices the Normandy site slice in Month 2.
2. **DCS Historian Feeds (Hard Dependency):** High-frequency 1-second process telemetry (Yokogawa Centum / Honeywell TDC 3000) capturing temperatures, pressures, and flow rates.
3. **Wireless Vibration & Acoustic Edge Sensors (Hard Dependency):** Retrofitting high-frequency triaxial vibration sensors on un-instrumented critical pumps ($3k per machine, 30 machines per site = $90k/site CAPEX).
4. **SAP PM Historical Maintenance Logs (Soft Dependency):** 5 years of historical work orders and failure records. Used for supervised labeling; model functions via unsupervised anomaly detection if logs are incomplete.

---

## 5. Sourcing Strategy: Build, Buy, or Blend

Applying the Gartner (2025) Sourcing Framework for Horizon 1 (*"Defend: augment productivity — Buy or Blend"*):

| Sourcing Route | Technical Description | Strategic Evaluation & Decision |
| :--- | :--- | :--- |
| **Buy (Commercial APM Suite)** | License turnkey commercial APM software (e.g. C3 AI Reliability, Aspen Mtell, GE Vernova SmartSignal). | *High Recurring Cost:* Software licenses average $100k per site-year ($1.30M/yr across 8 sites). However, proprietary algorithms are pre-trained on millions of industrial machine hours. |
| **Build (100% In-House Code)** | TotalEnergies Digital Factory codes custom deep autoencoders from scratch. | *Rejected:* High development time (> 18 months); risks recreating algorithms already standardized by specialized vendors. |
| **BLEND (Preferred Strategy)** | **Commercial Vendor Engine + In-House AspenTech Pipeline Integration.**<br/>• Procure enterprise APM licenses (Aspen Mtell / C3 AI) pre-integrated with AspenTech Inmation.<br/>• In-house Agile Delivery Trio customizes equipment anomaly templates, integrates refinery operating context, and embeds alerts into site maintenance workflows. | **ACCEPTED.** Combines vendor algorithmic maturity with TotalEnergies process knowledge and data fabric integration. |

---

## 6. Pilot, Rollout, Governance, and Schedule

### 6.1 Delivery Engine: The Refining Agile Delivery Trio
To eliminate the delivery handoff drag identified in Step 09 (`CLM-074`), P01 is executed by a dedicated **Agile Delivery Trio**:
- **Lead Data Scientist (TDF / Hub, Seconded Full-Time):** ML pipeline configuration, anomaly threshold calibration, model integration with AspenTech Inmation (`CLM-016` `[Disputed Fact]`).
- **Site Reliability Business Champion (Normandy Maintenance Superintendent, 30% Ring-Fenced Time):** Senior rotating equipment engineer with operational authority over work orders. Co-funded with rotational backfill (`CLM-062` `[Fact]`). Signs off on P&L benefit realization.
- **Branch Data Engineer (Refining & Chemicals IT Spoke, Dedicated):** Connects site AspenTech telemetry, ensures DCS data hygiene, and configures automated SAP PM maintenance notifications.

### 6.2 Deployment Phasing and Milestones

```
Month 01-03: Setup & Data Thin-Slicing (AspenTech Inmation slice live at Normandy; sensor retrofits)
Month 04-06: Pilot Calibration & Live Monitoring (120 machines at Normandy platform)
Month 07-09: First Value Capture & Validation (First verified avoided unplanned trip; Month 9 Kill Gate)
Month 10-24: Wave 1 Rollout (Antwerp, Donges, Feyzin, Zeeland: 4 additional platforms)
Month 25-36: Wave 2 Rollout (Port Arthur, Leuna, Satorp: 3 additional platforms; 8 total)
```

| Milestone Gate | Target Date | Operational Deliverable | Gate Threshold (Go / Stop Rule) |
| :---: | :---: | :--- | :--- |
| **Gate 1 (Data Slice Live)** | **Month 3** | AspenTech Inmation connected for 120 critical machines at Normandy. | Sensor ingestion latency $< 5\text{ seconds}$; data completeness $\ge 98\%$. |
| **Gate 2 (Pilot Validation)** | **Month 6** | Unsupervised anomaly detection running live in Normandy control room. | False alarm rate $< 1\text{ per machine per quarter}$. |
| **Gate 3 (Stage Gate 1 / Kill Gate)** | **Month 9** | 90-day operational review with Site Reliability Manager. | **Stop Rule:** If system fails to detect at least **2 verified machine degradation precursors** without false trips, project stops before committing Year 2 capex. |
| **Gate 4 (Wave 1 Complete)** | **Month 24** | 5 platforms live (Normandy + 4 sites); 500+ machines monitored. | Verified net throughput recovery $\ge \$8.0\text{M/yr}$ signed by Finance. |
| **Gate 5 (Full Scale)** | **Month 36** | 8 platforms live; ~800 critical rotating machines monitored. | Verified net throughput recovery $\ge \$15.0\text{M/yr}$; maintenance lead time cut by 30%. |

---

## 7. Economic Model: CAPEX, OPEX, and Benefit Formulas

### 7.1 Three-Year Investment Budget ($4.83M Total)

Costs are built bottom-up using registered labor and vendor rates:
- Lead Data Scientist: €70k gross × 1.437 employer charges × 1.15 overhead × 1.13 USD/EUR = **$131k/yr** (`CLM-069`, `CLM-070`, `CLM-071` `[Calculation]`).
- Branch Data Engineer: €58k gross × 1.437 × 1.15 × 1.13 = **$108k/yr** (`CLM-069`, `CLM-070`, `CLM-071` `[Calculation]`).
- Business Champion (30% time + backfill allowance): $98.5k × 0.30 + $50k backfill = **$79.5k/yr** (`CLM-062` `[Fact]`, `[Calculation]`).
- Core squad personnel cost: **$318.5k/yr** ($0.96M over 3 years) `[Calculation]`.

| Cost Category | Year 0 ($M) | Year 1 ($M) | Year 2 ($M) | Year 3 ($M) | 3-Year Total ($M) | Classification | Accounting Basis & Assumptions |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Agile Delivery Trio Personnel** | 0.08 | 0.24 | 0.32 | 0.32 | **0.96** | OPEX | 1 Lead DS + 1 Branch DE + 1 Reliability Champion. |
| **Sensor Hardware & Edge Retrofits** | 0.09 | 0.36 | 0.27 | 0.00 | **0.72** | CAPEX (Y0-Y2) | Phased hardware: Normandy pilot 30 machines ($0.09M in Y0); 4 sites Y1 ($0.36M); 3 sites Y2 ($0.27M). |
| **Site Deployment & OT Cyber Reviews** | 0.05 | 0.10 | 0.20 | 0.15 | **0.50** | OPEX | $50k/site OT cybersecurity certification + field calibration (`long_list.md`). |
| **APM Software Licences & Cloud MLOps** | 0.03 | 0.50 | 1.00 | 1.12 | **2.65** | OPEX | Vendor APM licences scaling to $100k/site-yr across 8 platforms + Azure cloud. |
| **TOTAL PROJECT ENVELOPE** | **0.25** | **1.20** | **1.79** | **1.59** | **4.83** | **Band: $4.10M – $6.27M** | Clears within branch authority (`Factbook 2025`, p. 26 `[Fact]`). |

### 7.2 Benefit Quantification Formula
Annual economic value is derived from throughput recovery and secondary maintenance cost avoidance:

$$\text{Total Annual Value} = \Delta \text{Value}_{\text{throughput}} + \Delta \text{Value}_{\text{repair}}$$

1. **Lever 1: Refinery Throughput Recovery ($\Delta \text{Value}_{\text{throughput}}$):**
   $$\Delta \text{Value}_{\text{throughput}} = \text{Capacity}_{\text{scope}} \times \Delta \text{Availability} \times \text{ERM} \times 365$$
   - Across 8 major operated refineries (capacity ~1,000 kb/d out of 1,526 kb/d worldwide, `Factbook 2025`, p. 135 `[Fact]`; `CLM-052`, `CLM-064` `[Fact]`):
   - At a conservative availability recovery of **0.55%** (avoiding 2 major compressor trips per refinery-year):
     $$\Delta \text{Value}_{\text{throughput}} = 1,000,000 \text{ b/d} \times 0.55\% \times \$7.1/\text{b} \times 365 = \mathbf{\$14.25M/yr}$$
2. **Lever 2: Collateral Damage & Expedited Repair Avoidance ($\Delta \text{Value}_{\text{repair}}$):**
   Avoiding secondary impeller destruction and emergency weekend contractor rates: **$0.75M/yr**.
3. **Total Steady-State Annual Run-Rate:** **$15.00M/yr** (Conservative range: $5.6M – $24.0M/yr) `[Calculation on assumed inputs]`.
4. **Peer Benchmark Cross-Check:** Equinor reports saving ~$29,000 per machine per year through predictive maintenance (`CLM-037` `[Calculation, Equinor offshore benchmark]`). Across the 8 target platforms, approximately 800 critical machines exist (~100/platform). Our base-case target focuses on the **~520 highest-criticality unspared machines (Tier-1 critical, 65% of fleet)** where an unplanned trip directly shuts down the operating unit:
   $$520 \text{ Tier-1 machines} \times \$29,000/\text{machine/yr} = \mathbf{\$15.08M/yr}$$
   *The peer cross-check validates our $15.0M/yr target within 1% error. Expanding predictive maintenance to the entire 800-machine fleet represents the $23.2M/yr Upside Case.*

---

## 8. Multi-Scenario Economics and 5-Year Cash Flows

Applying Course Session 3 financial standards (10.0% R&C hurdle rate, 5-year evaluation window, conservative deployment ramp):

### 8.1 Five-Year Cash Flow Waterfall (Base Case)

- **Investment Phasing:** Year 0 upfront commitment of **$0.25M** (Normandy pilot sensors and AspenTech slice).
- **Ramp Assumption:** 25% of steady-state in Year 1 ($3.75M), 75% in Year 2 ($11.25M), 100% in Years 3–5 ($15.00M/yr).
- **Run-Rate Opex after Year 3:** $0.85M/yr (APM software licenses and continuous MLOps support).

| Financial Metric ($M) | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | 5-Year Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Gross Value Generated** | 0.00 | 3.75 | 11.25 | 15.00 | 15.00 | 15.00 | **$60.00M** |
| **Project Expenditure (CAPEX+OPEX)** | -0.25 | -1.20 | -1.79 | -1.59 | -0.85 | -0.85 | **-$6.53M** |
| **Net Operational Cash Flow** | **-0.25** | **+2.55** | **+9.46** | **+13.41** | **+14.15** | **+14.15** | **+$53.47M** |
| **Discount Factor (10% R&C Hurdle)**| 1.000 | 0.909 | 0.826 | 0.751 | 0.683 | 0.621 | — |
| **Discounted Cash Flow (DCF)** | -0.25 | +2.32 | +7.81 | +10.07 | +9.66 | +8.79 | **NPV = +$38.40M** |

*Intra-Year Payback:* Cumulative net cash turns positive in **Month 9** `[Calculation on cash flows]`.
*Internal Rate of Return:* Standard financial IRR is **215%**; Modified IRR (MIRR at 10% reinvestment rate) is **58.2%** `[Calculation]`.

### 8.2 Three-Scenario Sensitivity Analysis

| Scenario | Annual Value at Scale ($M/yr) | 5-Year Net Cash Flow | NPV @ 10% Hurdle ($M) | NPV @ 12% Hurdle ($M) | IRR (%) | Payback Period |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Downside Case (Low Margin $5.3/b, 0.25% gain)** | $5.59M/yr | +$15.82M | **+$11.14M** | **+$9.82M** | **88%** | **16 months** |
| **Base Case (Target ERM $7.1/b, 0.55% gain)** | **$15.00M/yr** | **+$53.47M** | **+$38.40M** | **+$35.34M** | **215%** | **9 months** |
| **Upside Case (High Margin / 800 machines)** | $24.00M/yr | +$89.47M | **+$66.30M** | **+$61.50M** | **312%** | **5 months** |

*Economic Verdict:* Even in the Downside Case (refining margins compress to $5.3/b `CLM-063` `[Fact]` and throughput gain drops to 0.25% yielding $5.59M/yr), **the project delivers +$11.14M in NPV and pays back within 16 months**.

---

## 9. Frontline Adoption, Change Management, Risks, and Kill Rules

### 9.1 Frontline Change Management & Social Dialogue
The primary operational failure mode is alert fatigue: control room operators ignore algorithmic alerts if false-positive rates exceed 5%, leading to unmanaged equipment failures.
- **Explainable Anomaly Cards:** Instead of black-box risk scores, alerts show exact contributing sensors (*"Compressor 101-C-1: 82% anomaly score driven by axial bearing vibration 1.4× baseline and inboard seal oil temperature +4.2°C drift"*).
- **Maintenance Integration:** Pre-cleared SAP PM work order templates automatically populate with recommended inspection steps.
- **Human Decision Doctrine:** Control room operators retain full authority to accept or dismiss maintenance work orders, respecting TotalEnergies' core AI principle (`CLM-026` `[Fact]`).
- **Social Dialogue (CSE / CSSCT):** In accordance with French labor law, the works council (CSE) and health & safety committee (CSSCT) are formally informed during Month 2 on the deployment of IoT predictive maintenance sensors, confirming that sensors monitor equipment health exclusively, with zero worker surveillance.

### 9.2 Risk Management and Regulatory Controls

| Risk Factor | Severity | Probability | Mitigation Mechanism |
| :--- | :---: | :---: | :--- |
| **OT Cybersecurity Breach** | High | Low | Edge sensors communicate via read-only unidirectional data diodes; zero writeback to DCS control loops (`long_list.md`, C8). |
| **ATEX Zone 1 Explosion Risk** | Critical | Low | All wireless IoT vibration transmitters certified ATEX Zone 1 / IECEx. |
| **SEVESO Industrial Compliance** | High | Low | AI recommendations supplement but never bypass statutory safety instrumented systems (SIS) or SIL-rated trip interlocks. |
| **Turnaround Schedule Conflict** | Medium | Medium | Squad coordinates installation during scheduled unit shutdowns to avoid hot-tapping. |

### 9.3 Objective Stage-Gate Kill Rule (Month 9)
- **Review Date:** Month 9 (end of Normandy pilot).
- **Accountable Gate Owners:** VP Industrial Reliability R&C and Lead Data Scientist.
- **Composite Verification Metrics:**
  1. *Historical Replay Accuracy:* System must achieve **$\ge 85\%$ detection accuracy** on historical replay backtests of documented Normandy compressor trips over 2021–2025 historian records.
  2. *Live False Alarm Rate:* False-positive alert rate must remain **$< 1.0$ per machine per quarter** during 90 consecutive days of live monitoring.
  3. *Operator Trust:* $\ge 80\%$ of generated alerts verified and accepted by Normandy reliability engineers.
- **HARD STOP RULE:** If historical backtest accuracy is $< 80\%$ or the live false alarm rate exceeds $2.0$ per machine per quarter, **the project is terminated immediately**. The remaining $3.38M in Year 2–3 capital is canceled and returned to the R&C capital budget.

---

## 10. Precise Sources, Registered Claims, and Limits

- **Primary Operational Data:**
  - `Factbook 2025`, p. 135: Worldwide refinery throughput 1,526 kb/d; regional breakdown (`CLM-064` `[Fact]`).
  - `Factbook 2025`, p. 134: Capacities of Normandy (250 kb/d), Antwerp (338 kb/d), Port Arthur (235 kb/d) (`CLM-064` `[Fact]`).
  - `Factbook 2025`, p. 16: European Refining Margin Marker $7.1/b in 2025 (`CLM-063` `[Fact]`).
  - `Factbook 2025`, p. 26: $1,437M Refining & Chemicals net investment in 2025 (`CLM-004` `[Fact]`).
  - `URD 2025`, p. 43: Contracted AspenTech Inmation rollout across industrial sites (`CLM-018` `[Fact]`).
  - `URD 2025`, p. 41: Digital Plant Strategic Program objectives (`CLM-024` `[Fact]`).
- **Peer Benchmarks & Labor Rates:**
  - `SRC-017` & `CLM-037`: Equinor ~$20M/yr savings, ~$29k/machine/yr (`CLM-037` `[Calculation, Equinor offshore benchmark]`).
  - `SRC-021` & `CLM-041`: Shell > 10,000 machines monitored globally (`CLM-041` `[Fact, Pending: Shell vendor claim]`).
  - `SRC-030` & `SRC-031`: Apec Big Data executive salaries (€58k/€70k) and INSEE employer charges +43.7% (`CLM-069`, `CLM-070` `[Fact]`).
- **Methodological Limitations:**
  - Throughput recovery assumes AspenTech Inmation deployment proceeds according to contracted schedule; if a refinery site slice is delayed, deployment shifts to Zeeland or Port Arthur.
  - Value estimates reflect market marker ERM $7.1/b; high-margin environments (e.g. Q3 2026 $33.2/b) generate substantially higher upside (+300%).
