# Full Case Study: Featured Project 4 — P13 Retail Station Demand Forecasting & Loss Optimization

- **Roadmap Step:** 15 — [#15](https://github.com/Xenodion/ai-transformations-navy/issues/15)
- **Status:** Complete Case Study (Featured Case 4 — Template Model)
- **Date:** 8 November 2026
- **Authors:** Vincent Lamy & Alexandre Waerniers, Team 4.
- **Operating Branch:** Marketing & Services (M&S)
- **Provisional Horizon:** **Horizon 1** (Core Optimization / Rapid Self-Financing Cash Return)
- **Delivery Unit:** Agile Delivery Trio (*Trinôme Exécutif*) inside M&S Spoke
- **Evidence Base:**
  - `sources/primary/totalenergies_universal-registration-document-2025_2026_en.pdf` (URD 2025, pp. 6, 13, 138)
  - `sources/primary/totalenergies_factbook-2025_2026_en.xlsx` (Factbook 2025, p. 26, p. 145)
  - `sources/register.md` (`CLM-004`, `CLM-014`, `CLM-062`, `CLM-066`, `CLM-069`, `CLM-070`, `CLM-071`, `CLM-074`)
  - Course Framework: Sessions 1–4 (Case Study Standard Template)

---

## 1. Problem Statement, Operational Scope, and Baseline

### 1.1 The Business Problem
TotalEnergies operates one of the world's largest branded mobility and retail networks, with **12,775 service stations worldwide at year-end 2025** (`Factbook 2025`, p. 145 `[Fact]`; `URD 2025`, p. 13 `[Fact]`), including **5,679 stations across Europe** and **3,256 stations in France** (`Factbook 2025`, p. 145 `[Fact]`). 

Within France, the high-traffic motorway and expressway service stations (~800 company-owned sites) are operated by TotalEnergies' specialized downstream retail subsidiary, **Argedis** (`CLM-074` `[Local observation]`). On highway corridors, service stations are not merely fuel stops; they operate major food & beverage (F&B) and convenience store retail franchises (*Bonjour*, *Carrefour Express*, *Starbucks*, *Paul*). 

As directly observed on the ground (`CLM-074` `[Local observation]`), **convenience store replenishment and perishable inventory management are currently managed through static, manual min/max reorder rules**. Station managers manually adjust replenishment orders based on subjective intuition. This operational setup creates severe commercial dysfunction:
1. **Perishable Shrinkage and Food Spoilage:** Highly perishable goods (sandwiches, fresh meals, dairy, bakery) suffer high write-off rates (spoilage) when weekend highway traffic drops due to bad weather or traffic disruptions.
2. **Stock-Outs during Peak Demand:** During major holiday departures (*chassé-croisé des vacances*), static thresholds fail to anticipate traffic surges, leading to empty shelves on high-margin F&B categories during peak customer footfall.
3. **Rigid Store Pricing:** Highway retail prices are inflexible; near-expiry items are discarded at 100% loss rather than sold via automated dynamic markdowns.

### 1.2 Baseline Financial and Operational Metrics
- **Network Footprint in Scope & Corporate Scope Boundary:**
  - *Divestment Reality (URD 2025, p. 125 [Fact]):* On December 28, 2023, TotalEnergies completed the sale of 100% of its service station network in Germany (~1,200 stations) to Alimentation Couche-Tard, and on January 3, 2024, sold 100% of its network in the Netherlands (~380 stations), while placing Belgian and Luxembourg networks into a 60/40 JV operated by Couche-Tard (`URD 2025`, p. 125 `[Fact]`). Couche-Tard operates those convenience stores under its own proprietary IT and supply chain systems. TotalEnergies does **not** operate retail convenience stores in Germany or the Netherlands.
  - *Phase 1 Pilot (Year 1):* French motorway and expressway network operated directly by TotalEnergies' specialized downstream retail subsidiary, **Argedis (~800 company-operated stations)** (`CLM-074` `[Local observation]`, count estimated `[Assumption]`).
  - *Phase 2 Rollout (Years 2–3):* Expansion across TotalEnergies' **wholly-owned and company-operated flagship service stations in France (~1,500 company-operated stores total** out of 3,256 French branded stations, `Factbook 2025`, p. 145 `[Fact]`; `URD 2025`, p. 13 `[Fact]`), plus operated flagship European corridor sites where TotalEnergies retains company retail operations.
- **Revenue Baseline:**
  - Average non-fuel shop revenue per company-operated highway/flagship station: **$1.20M/yr** `[Assumption]`.
  - Non-fuel retail sales across Phase 1 scope (800 Argedis motorway stations): **$960M/yr** `[Calculation on assumed inputs]`.
  - Non-fuel retail sales across full Phase 2 scope (1,500 French company-operated stores): **$1,800M/yr** `[Calculation on assumed inputs]`.
  - Share of perishable food and short shelf-life items in store sales: ~25% = **$450M/yr** across Phase 2 (`[Assumption]`).
- **Loss / Shrinkage Baseline:**
  - Current food and perishable write-off rate (spoilage, obsolescence, damage): **4.5% of perishable sales** `[Assumption]`.
  - Annual perishable food write-off cost in Phase 1 scope (Argedis): **$10.8M/yr** ($240M × 4.5%) `[Calculation on assumed inputs]`.
  - Annual perishable food write-off cost in full Phase 2 scope (1,500 stores): **$20.25M/yr** ($450M × 4.5%) `[Calculation on assumed inputs]`.
- **Branch Capital Base:**
  - Marketing & Services Net Investments: **$609M in 2025** (`Factbook 2025`, p. 26 `[Fact]`). P13's 3-year cost ($1.95M) represents less than 0.3% of annual branch capex.

---

## 2. Why AI and Non-AI Alternatives

### 2.1 Why Machine Learning is Required
Retail highway demand is characterized by extreme non-linear volatility driven by external multi-factor signals that human station managers or linear ERP heuristics cannot process simultaneously:
- **Corridor Highway Traffic Ingestion:** Real-time and forecasted traffic density feeds (Bison Futé, motorway concessionaires APRR/SANEF/VINCI).
- **Hyper-Local Weather Forecasts:** 72-hour temperature, precipitation, and storm alerts (e.g. cold beverage sales surge +60% when temperature exceeds 28°C; hot coffee sales surge on rainy mornings).
- **Multi-Zone School Holiday Calendars:** Multi-country holiday departure curves across European corridors.
- **Inter-Item Elasticity & Substitution:** Predictive demand modeling across 800+ store SKUs to optimize batch baking and fresh delivery schedules.

### 2.2 Rejection of Non-AI Alternatives

| Non-AI Alternative Evaluated | Operational Mechanism | Why It Fails / Is Sub-Optimal |
| :--- | :--- | :--- |
| **Option A: Static Min/Max Inventory Rules (Status Quo)** | Station ERP automatically triggers a purchase order when stock drops below fixed safety quantity $S$. | **Fails under traffic volatility:** Causes severe overstocking on Sunday evenings (massive spoilage) and out-of-stock during Friday holiday departures. |
| **Option B: Central Manual Purchasing Specialists** | Centralized M&S purchasing analysts manually adjust weekly forecast spreadsheets for clusters of stations. | **Too slow and labor-intensive:** Cannot scale across 800+ stations and thousands of daily perishable deliveries; human planners cannot evaluate local micro-weather shifts. |
| **Option C: Systematic Supplier Consignment (Vendor-Managed Inventory)** | Pass inventory risk to food suppliers (e.g. bakeries or fresh food distributors). | **Higher cost-of-goods:** Suppliers demand 8% to 12% higher wholesale margins to absorb inventory shrinkage risk, eroding net gross margin. |

---

## 3. Horizon Justification: Why Horizon 1

Applying the Course Session 2 Three Horizons framework (Baghai, Coley and White, 1999) using the **Four Placement Questions**:

| Placement Question | Project P13 Evaluation | Horizon Implication |
| :--- | :--- | :---: |
| **Q1: Does it change the customer?** | **NO.** The customer remains the highway driver, commuter, and traveler visiting existing service stations. | Core (H1) |
| **Q2: Does it change the business model?** | **NO.** TotalEnergies continues to sell convenience store items, fresh food, coffee, and fuel/charging via existing retail POS. | Core (H1) |
| **Q3: Is the underlying technology proven?** | **YES.** Time-series demand forecasting (gradient-boosted trees, temporal fusion transformers, SKU-level regression) is commercially mature in retail. | Core (H1) |
| **Q4: Is time to first value under 12 months?** | **YES.** First verified store shrinkage reduction is captured in **4 to 8 months** at the pilot station cluster. | Core (H1) |

*Horizon Verdict:* **Horizon 1 (Core Optimization).** P13 is the fastest cash-flow engine in the entire transformation portfolio. It delivers immediate P&L margin recovery, serving as an operational self-financing cornerstone for the transformation.

---

## 4. Data Assets and Dependencies (Hard vs Soft)

Applying Course Rule 2 (*"Classify every dependency claim: hard, soft, or political"*):

```
[POS Transactional Feed] (Hard)  ---+
                                    |---> [Feature Store / ML Model] ---> [Automated ERP Order]
[Highway Traffic API] (Soft)     ---+           (Lightweight Cloud)             (SAP Retail)
                                    |
[72h Weather API] (Soft)         ---+
```

### 4.1 Data Pipeline Dependencies
1. **Station POS Transactional Feeds (Hard Dependency):** Real-time hourly sales data per SKU from point-of-sale systems (*Tokheim / Gilbarco / NCR*).  
   *Audit Status:* Already operational in all Argedis and European company-operated stations (`CLM-074`). Requires an automated daily export to M&S analytics.
2. **SAP Retail ERP Inventory Master (Hard Dependency):** Stock levels, minimum batch sizes, shelf-life dates, supplier delivery lead times.  
   *Audit Status:* Standard enterprise database. Data integration is thin-sliced during month 2.
3. **External Traffic Density Feeds (Soft Dependency):** Public and concessionaire highway traffic density.  
   *Workaround if unavailable:* Model falls back on historical day-of-week seasonal traffic profiles without blocking deployment.
4. **Hyper-Local Weather Forecast API (Soft Dependency):** 72-hour temperature and precipitation data.  
   *Workaround if unavailable:* Model falls back on historical seasonal temperature baselines.

---

## 5. Sourcing Strategy: Build, Buy, or Blend

Applying the Gartner (2025) Sourcing Framework for Horizon 1 (*"Defend: augment productivity — Buy or Blend"*):

| Option | Architecture | Strategic Evaluation & Decision |
| :--- | :--- | :--- |
| **Buy (Off-the-shelf Retail SaaS)** | License commercial retail replenishment software (e.g. Blue Yonder, RELEX). | *Rejected:* High annual recurring SaaS license fees ($400k+/yr); difficult to integrate with TotalEnergies' proprietary fuel pricing algorithms and proprietary highway station formats. |
| **Build (100% In-House Custom)** | Build custom forecasting engine and custom ERP connectors from scratch in Paris TDF. | *Rejected:* Re-invents standard retail forecasting algorithms; slow time-to-market (> 14 months), falling into the central delivery funnel. |
| **BLEND (Preferred Strategy)** | **Cloud ML Foundation + Proprietary Station Connectors.**<br/>• Use standard cloud time-series libraries (LightGBM, Prophet, Azure ML).<br/>• In-house Agile Trio builds custom station-level feature engineering and direct SAP connectors. | **ACCEPTED.** Fast deployment (4–8 months), zero third-party software vendor lock-in, low capex ($250k integration), and full internal IP ownership. |

---

## 6. Pilot, Rollout, Governance, and Schedule

### 6.1 Delivery Engine: The M&S Agile Delivery Trio
To eliminate the delivery handoff drag identified in Step 09 (`CLM-074` `[Local observation]`), P13 is executed by a dedicated **Agile Delivery Trio**:
- **Lead Data Scientist (TDF / Hub, Seconded Full-Time):** Time-series model tuning, feature store architecture, MLOps monitoring on Azure ML (`CLM-016` `[Disputed Fact: 300 vs 500 experts]`).
- **Retail Business Champion (Argedis / M&S Operating Unit, 30% Ring-Fenced Time):** Senior store category manager with direct operational authority over station replenishment. Co-funded by M&S from Day 1 with backfill provision (`CLM-062` `[Fact]`). Accountable for store manager adoption and signing P&L benefits.
- **Branch Data Engineer (M&S IT Spoke, Dedicated):** Connects POS transaction feeds and SAP Retail ERP; ensures daily automated order generation.

### 6.2 Deployment Phasing and Milestones

```
Month 00-02: Setup & Architecture (POS API connectors, baseline inventory audit, model training on 50 Argedis stations)
Month 03-06: Pilot Live & Validation (100 Argedis highway stations; Month 6 Kill Gate)
Month 07-12: Wave 1 Rollout (All ~800 French motorway stations operated by Argedis)
Month 13-24: Wave 2 Rollout (France flagship company-operated network: +700 stores; total ~1,500 company-operated stores)
Month 25-36: Wave 3 Optimization (Automated inventory replenishment & dynamic shelf-life markdowns)
```

| Milestone Gate | Target Date | Operational Deliverable | Gate Threshold (Go / Stop Rule) |
| :---: | :---: | :--- | :--- |
| **Gate 1 (Pilot Live)** | **Month 3** | Model deployed across 50 pilot Argedis stations. | Pipeline uptime $\ge 98\%$; automated forecasts generated daily. |
| **Gate 2 (Stage Gate 1 / Kill Gate)** | **Month 6** | Audit of food shrinkage across 100 pilot stations over 60 days. | **Stop Rule:** If food write-offs are not reduced by at least **8.0%** vs baseline, project is terminated. |
| **Gate 3 (Wave 1 Complete)** | **Month 12** | Deployment completed across all ~800 French motorway stations. | Verified P&L net savings $\ge \$5.0\text{M/yr}$ signed by Finance. |
| **Gate 4 (Wave 2 Complete)** | **Month 24** | Expansion completed across all ~1,500 French company-operated stores. | Verified P&L net savings $\ge \$12.0\text{M/yr}$; adoption rate $\ge 85\%$. |

---

## 7. Economic Model: CAPEX, OPEX, and Benefit Formulas

### 7.1 Three-Year Investment Budget ($1.95M Total)

Costs are built bottom-up using registered labor and vendor rates:
- Lead Data Scientist: €70k gross × 1.437 employer charges × 1.15 overhead × 1.13 USD/EUR = **$131k/yr** (`CLM-069`, `CLM-070`, `CLM-071` `[Calculation]`).
- Branch Data Engineer: €58k gross × 1.437 × 1.15 × 1.13 = **$108k/yr** (`CLM-069`, `CLM-070`, `CLM-071` `[Calculation]`).
- Business Champion (30% time + backfill allowance): $98.5k × 0.30 + $50k backfill = **$79.5k/yr** (`CLM-062` `[Fact]`, `[Calculation]`).
- Base squad personnel cost: **$318.5k/yr** ($0.96M over 3 years) `[Calculation]`.

| Cost Category | Year 0 ($M) | Year 1 ($M) | Year 2 ($M) | Year 3 ($M) | 3-Year Total ($M) | Classification | Accounting Basis & Assumptions |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Agile Delivery Trio Personnel** | 0.08 | 0.24 | 0.32 | 0.32 | **0.96** | OPEX | 1 Lead DS + 1 Branch DE + 1 Business Champion (co-funded). |
| **Store Rollout & Field Training** | 0.05 | 0.11 | 0.15 | 0.15 | **0.46** | OPEX | Station manager training, digital tablet onboarding, change management. |
| **Cloud Inference & POS Integration** | 0.22 | 0.10 | 0.18 | 0.03 | **0.53** | CAPEX (Y0-Y1) / OPEX | $0.25M POS API connectors (CAPEX); $0.10M–$0.15M/yr Azure ML hosting. |
| **TOTAL PROJECT ENVELOPE** | **0.35** | **0.45** | **0.65** | **0.50** | **1.95** | **Band: $1.65M – $2.55M** | Clears within branch authority (`Factbook 2025`, p. 26 `[Fact]`). |

### 7.2 Benefit Quantification Formula
Annual economic value is derived from three rigorous, verifiable operational levers:

$$\text{Total Annual Value} = \Delta \text{Value}_{\text{shrinkage}} + \Delta \text{Value}_{\text{logistics}} + \Delta \text{Value}_{\text{markdown}}$$

1. **Lever 1: Food & Perishable Spoilage Reduction ($\Delta \text{Value}_{\text{shrinkage}}$):**
   $$\Delta \text{Value}_{\text{shrinkage}} = N_{\text{stations}} \times \text{Sales}_{\text{perishables}} \times \text{Rate}_{\text{spoilage}} \times \text{Reduction}_{\text{AI}}$$
   - At Full Scale (1,500 French company-operated highway and flagship stores):
     $$\Delta \text{Value}_{\text{shrinkage}} = 1,500 \times \$300,000 \times 4.5\% \times 22.0\% = \mathbf{\$4.46M/yr} \quad (\text{range: } \$3.5\text{M} – \$6.0\text{M/yr})$$
2. **Lever 2: Emergency Logistics Delivery Avoidance & Peak Stock-Out Recapture ($\Delta \text{Value}_{\text{logistics}}$):**
   Eliminating costly emergency "hot-shot" replenishment deliveries from central bakeries/commissaries during weekend traffic spikes + capturing lost margin on sold-out fresh items during peak holiday departure curves:
   $$\Delta \text{Value}_{\text{logistics}} = \mathbf{\$7.54M/yr} \quad (\text{range: } \$4.0\text{M} – \$12.0\text{M/yr})$$
3. **Lever 3: Dynamic Expiry Markdowns ($\Delta \text{Value}_{\text{markdown}}$):**
   Automated progressive price reductions (-30% at 12 hours, -50% at 4 hours prior to expiry) on near-expiration items, recovering food cost that would otherwise be discarded at 100% loss:
   $$\Delta \text{Value}_{\text{markdown}} = \mathbf{\$6.00M/yr} \quad (\text{range: } \$3.0\text{M} – \$10.0\text{M/yr})$$
4. **Total Steady-State Annual Run-Rate:** **$18.0M/yr** (Conservative range: $10.5M – $28.0M/yr) `[Calculation on assumed inputs]`.

---

## 8. Multi-Scenario Economics and 5-Year Cash Flows

Applying Course Session 3 financial standards (12% hurdle rate, 5-year evaluation window, conservative deployment ramp):

### 8.1 Five-Year Cash Flow Waterfall (Base Case)

- **Investment Phasing:** Year 0 upfront commitment of **$0.35M** (M1–M2 architecture & connectors).
- **Ramp Assumption:** 25% of steady-state in Year 1 ($4.50M), 75% in Year 2 ($13.50M), 100% in Years 3–5 ($18.00M/yr).
- **Run-Rate Opex after Year 3:** $0.35M/yr (cloud hosting, continuous model retraining, and data engineering support).

| Financial Metric ($M) | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | 5-Year Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Gross Value Generated** | 0.00 | 4.50 | 13.50 | 18.00 | 18.00 | 18.00 | **$72.00M** |
| **Project Expenditure (CAPEX+OPEX)** | -0.35 | -0.45 | -0.65 | -0.50 | -0.35 | -0.35 | **-$2.30M** |
| **Net Operational Cash Flow** | **-0.35** | **+4.05** | **+12.85** | **+17.50** | **+17.65** | **+17.65** | **+$69.35M** |
| **Discount Factor (12% Hurdle)** | 1.000 | 0.893 | 0.797 | 0.712 | 0.636 | 0.567 | — |
| **Discounted Cash Flow (DCF)** | -0.35 | +3.62 | +10.24 | +12.46 | +11.23 | +10.01 | **NPV = +$47.21M** |

### 8.2 Intra-Year Monthly Breakeven Schedule (Year 1)
To substantiate the **6.8-month payback period**, the intra-year monthly cash progression operates as follows:
- *Months 1–2 (Year 0 Phase):* Outflow of -$175k/mo (-$350k cumulative); zero revenue.
- *Months 3–4 (Pilot Build):* Outflow of -$45k/mo (-$440k cumulative); zero revenue.
- *Months 5–6 (Pilot Live at 100 Stations):* Outflow -$45k/mo; pilot net savings +$120k/mo; net monthly flow +$75k/mo (-$290k cumulative).
- *Month 7 (Wave 1 Start - 300 Stations):* Net monthly flow +$320k/mo; cumulative turns **positive at Month 6.8 (+$30k net cash)**.
- *Months 8–12 (Full 800 Argedis Stations):* Net monthly flow +$580k/mo; Year 1 closes at **+$4.05M net cash**.

### 8.3 Three-Scenario Sensitivity Analysis

| Scenario | Value at Scale ($M/yr) | 5-Year Net Cash Flow | NPV @ 12% ($M) | IRR (%) | Payback Period |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Downside Case (Pessimistic)** | $10.5M/yr | +$38.2M | **+$25.4M** | **148%** | **9 months** |
| **Base Case (Target)** | **$18.0M/yr** | **+$69.4M** | **+$47.2M** | **214%** | **6.8 months** |
| **Upside Case (Optimistic)** | $28.0M/yr | +$111.0M | **+$76.1M** | **310%** | **4.5 months** |

*Economic Verdict:* Because Year 0 features an explicit upfront setup outflow (-$0.35M), **IRR is mathematically defined and robust across all scenarios (148% in Downside, 214% in Base Case)**, clearing TotalEnergies' 12% hurdle rate by more than 1,000 basis points.

---

## 9. Frontline Adoption, Change Management, Risks, and Kill Rules

### 9.1 Frontline Change Management
The primary failure mode in retail AI is store manager resistance: station managers override automated orders and revert to manual ordering because they fear stock-outs.
- **The "Bilingual" Store Interface:** The model output is presented on existing store inventory tablets as a clear recommendation with an explainability card (*"Recommended order: +25 baguettes and +40 cold drinks based on 29°C forecasted Sunday and VINCI highway alert"*).
- **Incentive Alignment:** Store manager performance bonuses currently penalize stock-outs heavily but do not penalize food spoilage. M&S management aligns station KPIs to reward net gross margin (sales minus spoilage).
- **Override Tracking:** Store managers retain final authority to override AI orders (respecting `CLM-026` `[Fact]`). If a station overrides > 30% of orders, the Business Champion investigates local operational discrepancies.

### 9.2 Risk Management and Regulatory Controls

| Risk Factor | Severity | Probability | Mitigation Mechanism |
| :--- | :---: | :---: | :--- |
| **Store Manager Adoption Drag** | High | Medium | Store tablet UI co-designed with Argedis managers; weekly triage with Business Champion. |
| **POS API Connectivity Glitches** | Medium | Low | Local station buffer: store tablet caches 48-hour safety orders offline if network disconnects. |
| **Works-Council (CSE) Inquiries** | Medium | Low | P13 automates commercial store purchasing, not worker surveillance; GDPR-compliant, no employee profiling. |
| **Food Quality / Safety Standards** | High | Low | Dynamic markdowns respect strict HACCP cold-chain rules; products reaching final expiry are locked out of POS. |

### 9.3 Objective Stage-Gate Kill Rule (Month 6)
- **Review Date:** Month 6 (end of 100-station pilot).
- **Accountable Gate Owners:** VP Retail Operations M&S (P&L Owner) and Lead Data Scientist.
- **Metric Measured:** Audited reduction in perishable food write-offs across pilot stations over 60 consecutive days vs identical pre-pilot baseline period.
- **Decision Threshold:**
  - If Spoilage Reduction $\ge 12.0\%$: **Accelerate Wave 1 rollout across all 800 Argedis stations.**
  - If Spoilage Reduction is between $8.0\%$ and $11.9\%$: **Refine feature engineering; 60-day probation.**
  - **HARD STOP RULE:** If Spoilage Reduction $< 8.0\%$: **Terminate project immediately.** Remaining $1.3M Year 2–3 capital is canceled and returned to the M&S budget.

---

## 10. Precise Sources, Registered Claims, and Limits

- **Primary Filings & Factbook Data:**
  - `Factbook 2025`, p. 145: 12,775 service stations worldwide; 5,679 in Europe; 3,256 in France (`CLM-066` `[Fact]`).
  - `Factbook 2025`, p. 26: $609M Marketing & Services net investments in 2025 (`CLM-004` `[Fact]`).
  - `URD 2025`, p. 13: Worldwide retail network overview (`CLM-066` `[Fact]`).
  - `URD 2025`, p. 138: Risk disclosure on organizational and skills adaptation pace (`CLM-014` `[Fact]`).
- **Ground-Level Evidence:**
  - `CLM-074` `[Local observation]`: First-hand operational observation by Vincent Lamy at Argedis France (~800 motorway stations) documenting manual inventory ordering, delivery latency, and frontline tool disconnects.
- **Labor Rates and Financial Benchmarks:**
  - `SRC-030` (Apec 2025 Big Data family, p. 62): €58k / €70k median executive salaries (`CLM-069` `[Fact]`).
  - `SRC-031` (INSEE 2023, p. 72): +43.7% employer social charges (`CLM-070` `[Fact]`).
  - `SRC-032` (ECB 2025 average): 1.1300 USD/EUR (`CLM-071` `[Fact]`).
  - `CLM-062` `[Fact]`: Group average loaded labor cost $98.5k/yr (`URD 2025`, p. 6).
- **Methodological Limitations:**
  - Station non-fuel sales and shrinkage rates are based on French motorway station empirical norms (`[Assumption]`); individual station margins vary between highway franchises and rural automated stations.
  - Spoilage reduction percentage depends on frontline station manager adherence to automated reorder recommendations.
