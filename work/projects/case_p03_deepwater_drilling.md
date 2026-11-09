# Full Case Study: Featured Project 2 — P03 Deepwater Drilling & Well Planning Optimisation

- **Roadmap Step:** 13 — [#13](https://github.com/Xenodion/ai-transformations-navy/issues/13)
- **Status:** Complete Case Study (Featured Case 2 — Upstream Scaling Pillar)
- **Date:** 9 November 2026
- **Authors:** Alexandre Waerniers & Vincent Lamy, Team 4.
- **Operating Branch:** Exploration & Production (E&P)
- **Provisional Horizon:** **Horizon 2** (Adjacent Process Innovation / Cross-Functional Rig Integration)
- **Delivery Unit:** Agile Delivery Trio (*Trinôme Exécutif*) inside E&P Drilling & Wells Spoke
- **Evidence Base:**
  - `sources/primary/totalenergies_universal-registration-document-2025_2026_en.pdf` (URD 2025, pp. 6, 38, 42, 43, 89, 138)
  - `sources/primary/totalenergies_factbook-2025_2026_en.xlsx` (Factbook 2025, pp. 26, 93, 125)
  - `sources/register.md` (`CLM-004`, `CLM-005`, `CLM-019`, `CLM-026`, `CLM-044`, `CLM-053`, `CLM-068`, `CLM-069`, `CLM-070`, `CLM-071`)
  - Course Framework: Sessions 1–4 (Case Study Standard Template)

---

## 1. Problem Statement, Operational Scope, and Baseline

### 1.1 The Business Problem
TotalEnergies is a global upstream operator producing **2,529 kboe/d of hydrocarbons in 2025** (`Factbook 2025`, p. 11 `[Fact]`; `CLM-005`). Exploration & Production is the group's primary capital consumer, absorbing **$9,259M in net investments in 2025** (`Factbook 2025`, p. 26 `[Fact]`; `CLM-004`) out of $17,091M group-wide net investments (54.2% of corporate capital). 

A core strategic pillar of TotalEnergies' multi-energy strategy is maintaining its hydrocarbon portfolio at an industry-leading upstream production cost of **$5.0/boe** (`Factbook 2025`, p. 11 `[Fact]`; `CLM-005` `[Fact]`) and a corporate pre-dividend organic cash breakeven strictly below **$30/b** ($26.4/b in 2025, `CLM-053` `[Fact]`). Achieving this requires strict capital discipline in deepwater offshore well construction, which represents approximately **25% to 35% of total upstream development capex** (`long_list.md` `[Assumption]`).

In offshore deepwater drilling, rig operations face extreme physical and financial exposure:
- **Capital Intensity:** Ultra-deepwater 7th generation drillships and dynamically positioned semi-submersibles operating in water depths exceeding 2,000 meters cost between **$400,000 and $500,000 per day** on a full-spread basis (including rig charter, support vessels, drilling fluids, directional logging, and ROV services) `[Assumption]`.
- **Complex Subsurface Geomechanics:** Drilling deepwater pre-salt wells in Brazil or deepwater turbidites in Angola involves narrow drilling margins between pore pressure and formation fracture pressure, reactive shale swelling, heavy salt creep, and lost circulation zones.
- **The Problem:** Non-productive time (NPT) and sub-optimal rate of penetration (ROP). Conventional well-planning relies on static pre-drill geological models and manual directional steering. A typical deepwater development well takes **45 to 80 days to drill**, costing **$20M to $45M per well**. Unplanned sidetracks, stuck pipe incidents, or premature bit degradation cost $3M to $10M per occurrence.

### 1.2 Baseline Financial and Operational Metrics
- **E&P Net Investments Baseline:** **$9,259M in 2025** ($8,853M in 2024, `Factbook 2025`, p. 26 `[Fact]`; `CLM-004`).
- **Target Offshore Rig Fleet in Scope:**
  - Rather than making the ungrounded claim of applying AI across 100% of global upstream spending (which distorted earlier drafts), this case study rigorously scopes P03 to TotalEnergies' **core operated deepwater drilling fleet: 8 to 12 dynamically positioned drillships operating in Brazil and Angola** (`URD 2025`, pp. 38, 89 `[Fact]`; `Factbook 2025`, p. 125 `[Fact]`):
    * *Brazil Santos Basin (Pre-Salt):* Operated developments on Mero (Mero 1, 2, 3, 4 FPSOs), Atapu, and Sepia (`URD 2025`, p. 89 `[Fact]`).
    * *Angola Lower Congo Basin:* Deepwater Block 17 and Block 32 (Kaombo, CLOV infill drilling) (`URD 2025`, p. 38 `[Fact]`).
  - Total annual direct drilling expenditure across 10 operated rigs at $450k/day spread rate:
    $$10 \text{ rigs} \times 365 \text{ days} \times \$450,000/\text{day} = \mathbf{\$1,642.5M/yr \text{ direct drilling capex base}} \quad \text{`[Calculation on assumed inputs]`}$$
- **Cognite Upstream Foundation:** In September 2025, TotalEnergies expanded its enterprise contract with Cognite to deploy **Cognite Data Fusion across all operated upstream assets over 2025–2028** (`URD 2025`, p. 43 `[Fact]`; `CLM-019`), specifically providing the upstream industrial data infrastructure "from drilling to production".

---

## 2. Why AI and Non-AI Alternatives

### 2.1 Why Machine Learning is Required
Deepwater well construction requires optimizing complex, dynamic multi-variable interactions in real time:
- **Real-Time Telemetry Ingestion (WITSML):** While drilling, downhole measurement-while-drilling (MWD) and logging-while-drilling (LWD) sensors stream real-time data: weight-on-bit (WOB), top-drive RPM, torque-and-drag, standpipe pressure, gamma ray, annular pressure-while-drilling (APWD), and acoustic vibration.
- **Predictive ROP & Geomechanical Optimization:** Machine learning models (trained on historical well logs and seismic velocity cubes on Cognite) predict downhole lithology changes 50 to 100 meters ahead of the bit, continuously calculating the optimal combination of WOB, RPM, and mud flow to maximize ROP while preventing bit balling, stick-slip vibration, and formation fracturing.
- **Automated Well Trajectory Steering:** Precedent established by peer competitor BP, which explicitly deployed an AI well-trajectory planning tool that plans routes *"in days instead of weeks or months"* (`CLM-068` `[Fact]`, BP Strategic Report 2025, p. 11).

### 2.2 Rejection of Non-AI Alternatives

| Non-AI Alternative Evaluated | Operational Mechanism | Why It Fails / Is Sub-Optimal |
| :--- | :--- | :--- |
| **Option A: Static Pre-Drill Engineering Models (Status Quo)** | Well engineering team designs fixed wellbore trajectory in CAD; rig crew follows static drilling program. | **Fails when geology drifts:** Deepwater salt and fault formations deviate from seismic predictions; static programs cannot adapt to real-time pore pressure shifts, causing stuck pipe and sidetracks. |
| **Option B: Manual Geomechanical Real-Time Monitoring Centers** | Onshore geoscientists manually watch WITSML log curves on computer monitors 24/7 and telephone the rig floor. | **Cognitive overload & latency:** Human engineers cannot process high-frequency (10 Hz) drilling dynamics across multiple rigs simultaneously; advice arrives hours after the bit has already entered the trouble zone. |
| **Option C: Commercial Turnkey Drilling Rig Incentives** | Contractual performance bonuses paid to drilling contractors (e.g. Transocean, Valaris) for early well completion. | **Conflicting incentives:** Drilling contractors earn revenue per rig day; their paramount commercial priority is rig safety and contract duration, not minimizing billable days on site. |

---

## 3. Horizon Justification: Why Horizon 2 (Adjacent Innovation)

Applying Course Session 2 Three Horizons criteria (Baghai, Coley & White, 1999) using the **Four Placement Questions**:

| Placement Question | Project P03 Evaluation | Horizon Implication |
| :--- | :--- | :---: |
| **Q1: Does it change the customer?** | **NO.** TotalEnergies continues to produce and market crude oil and natural gas. | Core (H1) |
| **Q2: Does it change the business model?** | **NO.** TotalEnergies remains an upstream E&P operator earning upstream cash margins. | Core (H1) |
| **Q3: Is the underlying technology proven at scale?** | **PARTIALLY (Adjacent).** While seismic AI is proven in Pau (`URD p. 42`), automated real-time closed-loop drilling telemetry optimization with offshore drilling contractors is an adjacent innovation requiring complex rig integration. | **H2 (Adjacent)** |
| **Q4: Is time to first value under 12 months?** | **NO (12 to 18 months).** Deepwater drilling campaigns operate on multi-month spud schedules; validating drilling AI safely on live offshore rigs requires 12–18 months across successive well sections. | **H2 (Adjacent)** |

*Resolution of the Horizon Paradox:* In early unverified drafts, P03 was incorrectly placed in H1 at an exaggerated $115.5M/yr, creating an artificial 90% concentration in H1. **Reclassifying P03 into Horizon 2 (Adjacent Process Innovation)** accurately reflects its multi-month campaign deployment cycle and technical sophistication, rebalancing the 5-year portfolio to a healthy **~48% H1 / 38% H2 / 12% H3** distribution.

---

## 4. Data Assets and Dependencies (Hard vs Soft)

```
[Cognite Data Fusion Upstream] (Hard) ---+
  (Deploying 2025-2028 across E&P)       |---> [Well Construction ML Engine] ---> [Offshore Rig Cabin Advisory]
[Rig WITSML Streaming Feeds] (Hard)   ---+         (Cloud / Edge Inference)            (Real-Time Advisory Card)
[Subsurface Velocity Models] (Soft)   ---+
```

### 4.1 Data Dependencies
1. **Cognite Data Fusion Ingestion Layer (Hard Dependency):** Centralized upstream platform contracted across all operated assets (`URD 2025`, p. 43 `[Fact]`; `CLM-019`). P03 utilizes the Cognite drilling data ingestion pipeline deployed in Month 2.
2. **WITSML Rig Telemetry Streaming (Hard Dependency):** Real-time 1 Hz surface and downhole streaming protocols (hookload, torque, ROP, standpipe pressure, MWD directional surveys) from rig contractors (Transocean, Saipem, Valaris).
3. **Pau High-Performance Subsurface Models (Soft Dependency):** 3D seismic velocity cubes and pre-drill pore pressure predictions generated by TotalEnergies' Pangea computing center (`URD p. 42`, `S05` `[Fact]`). Model operates on MWD logs alone if full seismic velocity inversion is pending.

---

## 5. Sourcing Strategy: Build, Buy, or Blend

Applying the Gartner (2025) Sourcing Framework for Horizon 2 (*"Extend: transform processes — Blend"*):

| Option | Architecture | Strategic Evaluation & Decision |
| :--- | :--- | :--- |
| **Buy (Turnkey Oilfield Service Software)** | License proprietary drilling software from oilfield service majors (e.g. SLB DrillOps, Landmark Compass). | *Rejected:* High annual software subscription costs ($1.2M+/yr); locks TotalEnergies into proprietary contractor ecosystems and prevents cross-rig benchmarking across competing rig contractors. |
| **Build (100% In-House R&D)** | Code proprietary drilling mechanics models and hydraulic simulators from scratch in Pau. | *Rejected:* Slow time-to-market (> 24 months); duplicates standardized open drilling mechanics equations. |
| **BLEND (Preferred Strategy)** | **Cognite Upstream Platform + Open Geomechanical Simulators + In-House AI Trajectory Optimization.**<br/>• Use Cognite Data Fusion for ingestion.<br/>• Blend open-source drilling physics libraries (hydraulics, torque & drag) with in-house machine learning models trained on TotalEnergies' proprietary pre-salt well databases. | **ACCEPTED.** Preserves proprietary pre-salt drilling know-how, ensures independence from drilling contractors, and integrates seamlessly with existing E&P data infrastructure. |

---

## 6. Pilot, Rollout, Governance, and Schedule

### 6.1 Delivery Engine: The Deepwater E&P Agile Delivery Trio
To eliminate cross-entity delivery latency (`CLM-074`), P03 is executed by a dedicated **Agile Delivery Trio**:
- **Lead Data Scientist (TDF / Hub, Seconded Full-Time):** Time-series geomechanical modeling, anomaly classification, reinforcement learning for ROP optimization (`CLM-016` `[Disputed Fact]`).
- **Senior Drilling Business Champion (E&P Deepwater Brazil/Angola, 30% Ring-Fenced Time):** Experienced drilling superintendent with operational credibility over offshore rig supervisors. Co-funded by E&P from Day 1 with backfill allowance (`CLM-062` `[Fact]`). Signs off on operational adoption and rig-time savings.
- **Branch Data Engineer (E&P IT / Cognite Spoke, Dedicated):** Connects WITSML rig data feeds into Cognite Data Fusion; ensures low-latency data streaming from offshore rigs to cloud inference.

### 6.2 Deployment Phasing and Milestones

```
Month 00-03: Setup & Architecture (Cognite WITSML connectors, historical Mero well data ingestion)
Month 04-09: Pilot Calibration & Validation (Live advisory monitoring on 2 deepwater rigs at Mero, Brazil)
Month 10-18: First Campaign Value Capture (Full section drilling optimization on 2 rigs; Month 12 Kill Gate)
Month 19-24: Wave 1 Rollout (Expansion to 6 rigs across Brazil pre-salt and Angola Block 17)
Month 25-36: Wave 2 Full Scale (10 operated deepwater rigs live across Brazil and Angola)
```

| Milestone Gate | Target Date | Operational Deliverable | Gate Threshold (Go / Stop Rule) |
| :---: | :---: | :--- | :--- |
| **Gate 1 (Streaming Live)** | **Month 3** | WITSML streaming active from 2 Mero rigs into Cognite. | Telemetry latency $< 2\text{ seconds}$; data completeness $\ge 99\%$. |
| **Gate 2 (Pilot Advisory Live)** | **Month 6** | Real-time ROP advisory tool running in onshore drilling center. | Recommended WOB/RPM envelope verified by directional drillers. |
| **Gate 3 (Stage Gate 1 / Kill Gate)** | **Month 12** | Completion of 2 full deepwater development wells on Mero using AI advisory. | **3-Tier Gate Rule:**<br/>• **Tier 1 ($\ge 1.8\%$ saving):** Full Go; release Wave 1 capital ($1.15M).<br/>• **Tier 2 (1.2%–1.7% saving):** Conditional 3-month probation on 1 additional well.<br/>• **Tier 3 ($< 1.2\%$ saving): Hard Stop Rule;** project terminated immediately. |
| **Gate 4 (Wave 1 Complete)** | **Month 24** | 6 deepwater rigs live across Brazil and Angola. | Verified rig capex savings $\ge \$18.0\text{M/yr}$ signed by E&P Finance. |
| **Gate 5 (Full Scale)** | **Month 36** | 10 deepwater rigs live; full fleet coverage. | Verified net capex savings $\ge \$35.0\text{M/yr}$; NPT down by 20%. |

---

## 7. Economic Model: CAPEX, OPEX, and Benefit Formulas

### 7.1 Three-Year Investment Budget ($3.26M Total)

Costs are built bottom-up using registered labor and vendor rates:
- Lead Data Scientist: €70k gross × 1.437 employer charges × 1.15 overhead × 1.13 USD/EUR = **$131k/yr** (`CLM-069`, `CLM-070`, `CLM-071` `[Calculation]`).
- Branch Data Engineer: €58k gross × 1.437 × 1.15 × 1.13 = **$108k/yr** (`CLM-069`, `CLM-070`, `CLM-071` `[Calculation]`).
- Business Champion (30% time + backfill allowance): $98.5k × 0.30 + $50k backfill = **$79.5k/yr** (`CLM-062` `[Fact]`, `[Calculation]`).
- Core squad personnel cost: **$318.5k/yr** ($0.96M over 3 years) `[Calculation]`.

| Cost Category | Y0 Setup (M0–M3) | Y1 Pilot (M4–M12) | Y2 Wave 1 (M13–M24) | Y3 Wave 2 (M25–M36) | 3-Year Total ($M) | Classification | Accounting Basis & Assumptions |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Agile Delivery Trio Personnel** | 0.08 | 0.24 | 0.32 | 0.32 | **0.96** | OPEX | 1 Lead DS + 1 Branch DE + 1 Drilling Champion (co-funded). |
| **Cognite WITSML Ingestion Connectors** | 0.30 | 0.05 | 0.05 | 0.05 | **0.45** | CAPEX (Y0) / OPEX | Rig-to-cloud WITSML streaming pipeline connectors on Cognite. |
| **Offshore Rig Deployment & Calibration** | 0.05 | 0.15 | 0.35 | 0.25 | **0.80** | OPEX | Rig crew onboarding, telemetry calibration across 10 drillships. |
| **Specialized Drilling Analytics Software** | 0.02 | 0.16 | 0.43 | 0.44 | **1.05** | OPEX | Specialized geomechanical modelling toolkits & cloud compute. |
| **TOTAL PROJECT ENVELOPE** | **0.45** | **0.60** | **1.15** | **1.06** | **3.26** | **Band: $2.77M – $4.23M** | Clears within E&P branch capex authority (`Factbook p. 26` `[Fact]`). |

### 7.2 Benefit Quantification Formula
Annual economic benefit is derived strictly from rig-time reduction on operated deepwater drilling campaigns:

$$\Delta \text{Value}_{\text{drilling}} = N_{\text{rigs}} \times 365 \times \text{Rate}_{\text{spread}} \times \Delta T_{\text{reduction}}$$

- **Target Rig Fleet:** 10 operated deepwater drillships across Brazil (Mero, Atapu) and Angola (Block 17/32) (`Factbook 2025`, p. 125 `[Fact]`).
- **Spread Day-Rate:** **$450,000 per day** `[Assumption]`.
- **Annual Direct Drilling Spend Base:**
  $$10 \text{ rigs} \times 365 \text{ days} \times \$450,000/\text{day} = \mathbf{\$1,642.5M/yr} \quad \text{`[Calculation on assumed inputs]`}$$
- **Conservative Rig-Time Reduction Target:** **2.13% net reduction** (saving an average of **7.78 rig days per rig-year**, or ~1.3 days per 60-day deepwater well):
  $$\Delta \text{Value}_{\text{drilling}} = \$1,642.5\text{M} \times 2.13\% = \mathbf{\$35.00M/yr} \quad (\text{conservative range: } \$20.0\text{M} – \$60.0\text{M/yr}) \quad \text{`[Calculation on assumed inputs]`}$$
- **International Benchmark Grounding:** In its *Energy and AI* flagship report, the International Energy Agency estimates that AI-driven drilling and subsea optimization can reduce deepwater upstream capital costs by **"up to 10%"** (`SRC-026, p. 118`, `CLM-044` `[Fact]`). Our 2.13% target represents barely one-fifth of the IEA's theoretical potential, ensuring absolute conservatism against CEO challenge.

---

## 8. Multi-Scenario Economics and 5-Year Cash Flows

Applying Course Session 3 financial standards (**12.0% E&P hurdle rate**, 5-year evaluation window, conservative deployment ramp):

### 8.1 Five-Year Cash Flow Waterfall (Base Case)

- **H2 Ramp Assumption:** 0% in Year 1 (pilot build & calibration), 25% in Year 2 ($8.75M on 2 rigs), 60% in Year 3 ($21.00M on 6 rigs), 100% in Years 4–5 ($35.00M/yr across 10 rigs).
- **Run-Rate Opex after Year 3:** $0.65M/yr (ongoing cloud compute, model recalibration, and data engineering support).

| Financial Metric ($M) | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | 5-Year Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Gross Value Generated** | 0.00 | 0.00 | 8.75 | 21.00 | 35.00 | 35.00 | **$99.75M** |
| **Project Expenditure (CAPEX+OPEX)** | -0.45 | -0.60 | -1.15 | -1.06 | -0.65 | -0.65 | **-$4.56M** |
| **Net Operational Cash Flow** | **-0.45** | **-0.60** | **+7.60** | **+19.94** | **+34.35** | **+34.35** | **+$95.19M** |
| **Discount Factor (12% E&P Hurdle)**| 1.000 | 0.893 | 0.797 | 0.712 | 0.636 | 0.567 | — |
| **Discounted Cash Flow (DCF)** | -0.45 | -0.54 | +6.06 | +14.20 | +21.83 | +19.49 | **NPV = +$60.59M** |

*Payback Accounting Methodology:* On an annual DCF linear interpolation, payback is mathematically reached at **14 months** (1.14 years); however, under operational deepwater campaign accounting (where rig-time savings are audited post-well completion after section total depth is reached), verified cumulative cash breakeven is reached at **Month 22 (1.8 years)**.

### 8.2 Three-Scenario Sensitivity Analysis

| Scenario | Annual Value at Scale ($M/yr) | 5-Year Net Cash Flow | NPV @ 12% Hurdle ($M) | NPV @ 15% Sensitivity ($M) | IRR (%) | Payback Period |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Downside Case (1.22% rig-time saving)** | $20.00M/yr | +$50.4M | **+$30.2M** | **+$26.4M** | **195%** | **28 months** |
| **Base Case (2.13% rig-time saving)** | **$35.00M/yr** | **+$95.2M** | **+$60.6M** | **+$54.6M** | **385%** | **22 months** |
| **Upside Case (3.65% rig-time saving)** | $60.00M/yr | +$167.5M | **+$110.8M** | **+$101.4M** | **520%** | **17 months** |

*Scenario Ramp Documentation:* Downside Case models a delayed adoption ramp (15% Y2, 55% Y3, 100% Y4–Y5); Base Case models (25% Y2, 60% Y3, 100% Y4–Y5); Upside Case models (30% Y2, 65% Y3, 100% Y4–Y5). Even under Downside conditions, **NPV @ 12% is +$30.2M**, clearing the hurdle by a wide margin.

---

## 9. Frontline Adoption, Change Management, Risks, and Kill Rules

### 9.1 Frontline Change Management with Rig Contractors
Directional drillers and rig toolpushers operate in high-risk environments and will reject automated control recommendations if they feel safety is compromised.
- **The "Drilling Advisory" Model:** Recommendations appear on rig cabin displays as a dynamic advisory envelope (*"Optimal ROP window: 22–25 m/h at WOB 12–14 tonnes and RPM 110; 92% confidence pore pressure margin remains > 0.8 ppg"*).
- **Human Decision Doctrine:** Rig drillers retain 100% manual control over drawworks and mud pumps (`CLM-026` `[Fact]`). AI never executes closed-loop steering without human validation.
- **Contractor Alignment & Data Rights:** TotalEnergies explicitly establishes contractual ownership of all raw 1 Hz WITSML rig telemetry streams in offshore charter contracts. Furthermore, E&P introduces a **10% shared-savings contractor bonus pool** paid to rig crews for verified NPT reduction, aligning contractor crew incentives with TotalEnergies' drilling velocity.

### 9.2 Risk Management and Safety Interlocks

| Risk Factor | Severity | Probability | Mitigation Mechanism |
| :--- | :---: | :---: | :--- |
| **Blowout / Well Control Risk** | Critical | Low | System has zero interface with rig Blowout Preventer (BOP) or safety trip interlocks; hard stop protocols remain 100% mechanical. |
| **WITSML Telemetry Latency** | High | Low | Edge computing unit installed directly in offshore rig doghouse; operates locally if satellite link degrades. |
| **Drilling Contractor Friction** | Medium | Medium | Joint calibration sessions with Transocean/Valaris technical leads during pre-drill campaign planning; 10% shared-savings pool. |

### 9.3 Objective Stage-Gate Kill Rule (Month 12)
- **Review Date:** Month 12 (completion of 2 deepwater wells on Mero, Brazil).
- **Accountable Gate Owners:** VP Drilling & Wells E&P and Lead Data Scientist.
- **Metric Measured:** Audited duration of 12 ¼" and 8 ½" reservoir drilling sections vs offset wells in identical geomechanical formations.
- **3-Tier Decision Threshold:**
  - **Tier 1 (Verified Rig-Time Saving $\ge 1.8\%$):** Full Go. Approve Wave 1 expansion across 6 rigs ($1.15M released).
  - **Tier 2 (Verified Rig-Time Saving between $1.2\%$ and $1.7\%$):** Conditional 3-month probation on 1 additional development well.
  - **Tier 3 (HARD STOP RULE — Saving $< 1.2\%$):** Terminate project immediately. Remaining $2.21M in Year 2–3 capital is canceled and returned to the E&P budget.

---

## 10. Precise Sources, Registered Claims, and Limits

- **Primary Financial & Operational Data:**
  - `Factbook 2025`, p. 26: $9,259M E&P net investments in 2025 (`CLM-004` `[Fact]`).
  - `Factbook 2025`, p. 125 & `URD 2025`, pp. 38, 89: Deepwater development assets and operated rigs in Brazil (Mero, Atapu) and Angola (Block 17/32) (`[Fact]`).
  - `Factbook 2025`, p. 11 & `SRC-003`, p. 6: 2,529 kboe/d hydrocarbon production (`CLM-005` `[Fact]`).
  - `URD 2025`, p. 43: Cognite Data Fusion contract across all operated upstream assets 2025–2028 (`CLM-019` `[Fact]`).
  - `URD 2025`, p. 138: Risk disclosure on organization and skills adaptation pace (`CLM-014` `[Fact]`).
- **Peer Precedents & Labor Rates:**
  - `SRC-025`, p. 11: BP well-trajectory planning tool benchmark (`CLM-068` `[Fact]`).
  - `SRC-026`, p. 118: IEA *Energy and AI* drilling cost reduction scenario (`CLM-044` `[Fact]`).
  - `SRC-030` & `SRC-031`: Apec Big Data executive salaries (€58k/€70k) and INSEE employer charges +43.7% (`CLM-069`, `CLM-070` `[Fact]`).
  - `CLM-062`: Group average loaded labor cost $98.5k/yr (`URD 2025`, p. 6 `[Fact]`).
- **Methodological Limitations:**
  - Rig-time reduction calculations assume deepwater drilling campaigns proceed without major geopolitical or subsea pipeline interruptions.
  - Savings apply strictly to TotalEnergies' operated rig fleet where TotalEnergies acts as operator and manages the well engineering design.
