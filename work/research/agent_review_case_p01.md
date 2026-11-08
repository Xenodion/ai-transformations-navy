# Adversarial Comex & CEO Review: Featured Case Study 1 (`work/projects/case_p01_refining_pdm.md`)

- **Document Under Review:** `work/projects/case_p01_refining_pdm.md`
- **Roadmap Step:** 12 — Full Case Study: Featured Project 1 ([#12](https://github.com/Xenodion/ai-transformations-navy/issues/12))
- **Review Date:** 9 November 2026
- **Reviewers:** Executive Committee (Comex) Capital Committee & Skeptical Professor (acting as CEO Patrick Pouyanné)
- **Framework & Governance:** `AGENTS.md` rules, Course Sessions 1–4 Case Study Standard Template, `sources/register.md`, `sources/primary/totalenergies_universal-registration-document-2025_2026_en.pdf` (URD 2025), `sources/primary/totalenergies_factbook-2025_2026_en.xlsx` (Factbook 2025)

---

## 1. Executive Verdict & Quality Gate

```
+--------------------------------------------------------------------------------------------------+
|                                    EXECUTIVE VERDICT                                             |
|                                                                                                  |
|   🔴 REQUEST CHANGES (High Confidence)                                                           |
|                                                                                                  |
|   Project P01 (Refining Predictive Maintenance) is an operationally compelling, strategically     |
|   sound proposal. It rightfully anchors the industrial core of TotalEnergies' AI portfolio in    |
|   Horizon 1 (Core Optimization), leverages the contracted AspenTech Inmation fabric (CLM-018),   |
|   and addresses a verified, high-cost operational pain point (unplanned refinery trip downtime).  |
|                                                                                                  |
|   However, the proposal contains a glaring arithmetic contradiction in the Downside Case         |
|   (narrative inputs yield $5.59M/yr, while Table 8.2 models $8.00M/yr, inflating downside NPV     |
|   by +57%), an arbitrary machine-count fudge in the Equinor peer cross-check (slashing 800 to     |
|   520 machines to force a 1% match), a logically perverse Month 9 stop rule that penalizes       |
|   well-maintained equipment, a severe Capex phasing front-loading anomaly in Year 0 ($0.45M for  |
|   5 sites before the pilot runs), and a hallucinated citation citing the ECB forex rate for      |
|   payback (CLM-071).                                                                             |
|                                                                                                  |
|   Six concrete, numbered revisions are required before Step 12 can be formally approved.         |
+--------------------------------------------------------------------------------------------------+
```

---

## 2. Key Strengths (5 Points)

1. **Disciplined 10-Section Structure and Flawless Horizon 1 Clearance:**
   The case study rigorously adheres to the Course Sessions 1–4 Case Study Standard Template. It walks methodically through the Baghai, Coley & White (1999) Three Horizons framework and answers all four placement questions with crisp discipline:
   - *Q1 (New Customer?):* No (existing wholesale fuels and petrochemical clients).
   - *Q2 (New Business Model?):* No (earning standard refining margins, ERM).
   - *Q3 (Proven Technology?):* Yes (mature industrial vibration anomaly detection, Shell > 10,000 machines `CLM-041`, Equinor `CLM-037`).
   - *Q4 (Value < 12 Months?):* Yes (first verified avoided trip at Normandy in 6–9 months).
   Classifying P01 as Horizon 1 Core Optimization creates the high-probability cash generator ($15.0M/yr) required to self-finance broader transformation.

2. **Strategic Alignment with the AspenTech Inmation Data Fabric (`CLM-018`):**
   Rather than proposing an expensive, multi-year bespoke data lake, P01 builds directly on TotalEnergies' contracted industrial data fabric (`URD 2025`, p. 43 `[Fact]`; `CLM-018`). Adopting the course doctrine (*"a slice, not a lake"*), the squad thin-slices the Normandy telemetry feed in Month 2, minimizing infrastructure lead time and sunk IT risk.

3. **Methodologically Sound Bottom-Up Personnel Costing:**
   The squad budget is grounded in registered French market benchmarks rather than arbitrary lump sums:
   - Lead Data Scientist: €70k gross × 1.437 employer charges (`CLM-070 [Fact]`) × 1.15 overhead × 1.13 USD/EUR (`CLM-071 [Fact]`) = **$130.7k/yr** (`[Calculation]`).
   - Branch Data Engineer: €58k gross × 1.437 × 1.15 × 1.13 = **$108.3k/yr** (`[Calculation]`).
   - Business Champion: $98.5k group average (`CLM-062 [Fact]`) × 30% ring-fenced time + $50k backfill = **$79.5k/yr** (`[Calculation]`).
   This bottom-up total of **$318.5k/yr** ($0.96M over 3 years) provides exemplary accounting transparency.

4. **Realistic Engineering Architecture and Safety Boundaries:**
   Section 9 properly isolates AI software from Safety Instrumented Systems (SIS) and SIL-rated emergency trip interlocks. The inclusion of ATEX Zone 1 / IECEx certified wireless hardware and unidirectional data diodes for OT cybersecurity ensures that the proposal respects upper-tier SEVESO industrial safety mandates.

5. **Pragmatic Blend Sourcing Strategy:**
   Applying Gartner's 2025 Sourcing Framework for H1 (*"Defend: augment productivity — Buy or Blend"*), the proposal firmly rejects a 100% in-house build (> 18 months development time, reinventing mature algorithms) and pure SaaS lock-in, correctly selecting a **Blend** strategy (commercial APM engine integrated into TotalEnergies' AspenTech Inmation fabric).

---

## 3. Vulnerabilities during Oral Defense (Forensic CEO & Professor Scrutiny)

During the Comex capital allocation pitch, CEO Patrick Pouyanné (played by the professor) and the Refining & Chemicals leadership will aggressively exploit five critical vulnerabilities:

### Attack 1: The Downside Case Arithmetic Contradiction ($5.59M vs $8.00M / +$11.1M vs +$17.4M NPV)
- **CEO Patrick Pouyanné Pushback:**
  > *"Messieurs, look at your own text in Section 8.2 (Line 199). You explicitly define your Downside Case: 'refining margins compress to $5.3/b, availability gain drops to 0.25%'. Let's do the math on my pocket calculator right now: 1,000,000 barrels per day × 0.25% availability × $5.3 per barrel × 365 days = $4.836M/yr in throughput recovery. Add your $0.75M/yr repair savings, and your downside value is **$5.59M/yr**. Yet in Table 8.2, you write down an Annual Value at Scale of **$8.00M/yr** and claim an NPV of **+$17.4M**! Where did the missing $2.41M/yr come from? To get $8.00M/yr at $5.3/b margin, you need a 0.38% availability gain, not 0.25%! If I plug your real downside inputs ($5.59M/yr) into your cash flow model, 5-year net cash drops from $25.5M to **$15.8M**, and NPV @ 10% collapses from $17.4M to **$11.1M**! Did you fudge your downside table to make it look safer to Comex?"*
- **Forensic Finding:** There is an undeniable mathematical mismatch between the narrative assumptions in Line 199 and the figures tabulated in Table 8.2. Table 8.2 models an $8.00M/yr run-rate (cash flows: `[-0.72, +1.21, +4.31, +6.37, +7.15, +7.15]`), yielding an NPV @ 10% of **+$18.05M** (written as +$17.4M). If the narrative parameters (0.25% gain, $5.3/b ERM = $5.59M/yr) are modeled (cash flows: `[-0.72, +0.61, +2.50, +3.96, +4.74, +4.74]`), the true Downside NPV @ 10% is **+$11.06M**. Furthermore, Table 8.2 labels the Upside Case as "(High Margin $33/b)", but lists Annual Value at Scale as **$24.00M/yr**. At $33/b ERM and 0.55% availability, value would be **$66.25M/yr**! A $24.0M/yr upside implies margins of only $11.5/b.

### Attack 2: The "520 vs 800" Cherry-Picked Machine Count Fudge
- **CEO Patrick Pouyanné Pushback:**
  > *"In Section 1.2 (Line 39) and Section 6.2 (Line 130), you state that your full 8-platform rollout covers **~800 critical rotating machines** (averaging 100 per site, which makes sense given 120 at Normandy). But then in Section 7.2 (Line 165), you introduce Equinor's peer benchmark of $29,000 per machine per year (`CLM-037`). And suddenly, you multiply $29,000 by **520 machines** to get $15.08M/yr, boasting that 'the peer cross-check validates our $15.0M target within 1% error'! Where did 280 machines disappear to? If you have 800 machines, Equinor's benchmark says **$23.2M/yr**. You obviously divided $15.0M by $29,000, got 517 machines, rounded it to 520, and presented it as an independent validation! Don't manufacture coincidences in front of this committee."*
- **Forensic Finding:** Scaling Equinor's $29,000/machine/yr benchmark across 520 machines contradicts the stated scope of 800 machines across the 8 platforms. In addition, `CLM-037` in `sources/register.md` is registered as `[Calculation]`, not `[Fact]`, and is based on offshore North Sea turbomachinery (where deferred oil production and helicopter maintenance make outage costs much higher than onshore downstream refining). Citing it as a direct onshore `[Fact]` without highlighting the offshore-to-onshore transfer limitation violates `AGENTS.md` Rule 3.

### Attack 3: The "Break-or-Die" Month 9 Kill Gate Perversity
- **Refining & Chemicals VP / Comex Pushback:**
  > *"Look at your Stop Rule in Section 6.2 (Gate 3) and Section 9.3: 'If system fails to detect at least 2 verified machine degradation precursors... terminate rollout immediately; remaining $4.04M capital is canceled.' On 120 critical machines at Normandy over 6 months of live monitoring, what if our rotating machinery runs smoothly and nothing breaks? You are going to terminate a $1.5M project and scrap the rollout because our maintenance crews did their job and no pump suffered bearing failure between Month 4 and Month 9?! That is a perverse stop rule!"*
- **Forensic Finding:** A stop rule based purely on live failure occurrence over a short 6-month observation window creates an operational paradox. If zero degradation events occur naturally, the model cannot demonstrate live precursor detection. A defensible stop rule must measure: (1) algorithm detection performance on historical replayed telemetry (backtesting against 5 years of recorded Normandy compressor trips), (2) false positive alarm rates (< 1 alarm per machine per quarter / false positive rate < 5%), and (3) maintenance superintendent user acceptance.

### Attack 4: The $0.45M Sensor Pre-Commitment Capex Flaw
- **Comex CFO Pushback:**
  > *"In Table 7.1, you allocate **$0.45M** in Year 0 for 'Sensor Hardware & Edge Retrofits'. At $90k per site (30 machines × $3k), $0.45M buys hardware for **5 refineries**! Why are we purchasing vibration sensors for Antwerp, Donges, and Feyzin in Year 0 when you haven't even proven the concept at Normandy? If you trigger your Month 9 Kill Gate and shut the project down, we will be left holding $450,000 worth of wireless IoT sensors in a warehouse! Furthermore, you claim in Line 226 that stopping at Month 9 cancels $4.04M. But Year 0 ($0.72M) plus 9 months of Year 1 ($0.59M) equals $1.31M spent, which leaves $3.52M remaining, not $4.04M!"*
- **Forensic Finding:** Year 0 hardware capex should strictly cover the Normandy pilot (30 machines × $3k = $90k = $0.09M). Committing $0.45M in Year 0 front-loads capital across non-pilot sites before passing Stage Gate 3, violating stage-gate capital discipline. Table 7.1 must re-phase sensor hardware: $0.09M in Year 0 (Normandy), $0.36M in Year 1 (Wave 1, 4 sites), and $0.27M in Year 2 (Wave 2, 3 sites).

### Attack 5: Citation Mismatches & The Hallucinated "CLM-071 Payback"
- **Comex Audit & Governance Pushback:**
  > *"In Section 8.1 (Line 189), you state: 'Cumulative net cash turns positive in Month 9 (CLM-071 [Calculation])'. I looked up CLM-071 in your claim register: it is the European Central Bank EUR/USD exchange rate reference (1.1300)! What does an ECB forex rate have to do with intra-year operational payback at the Normandy refinery? Furthermore, you tag Shell's claim of 10,000 machines as a verified Fact (CLM-041), but your register admits it is an unaudited quote from a vendor marketing press release (C3 AI) with 'Pending' status!"*
- **Forensic Finding:** Several citation tags in `case_p01_refining_pdm.md` are inaccurate:
  - `CLM-071` is the ECB foreign exchange rate, not an operational cash-flow calculation.
  - `CLM-037` (Equinor benchmark) is registered as `[Calculation]`, but cited as `[Fact]`.
  - `CLM-041` (Shell equipment count) is registered as `Pending` (vendor marketing channel), but cited as `[Fact]`.
  - `CLM-064` is cited for refinery throughput (1,526 kb/d), whereas `CLM-052` is the registered claim for throughput by area.
  - Key operational assumptions ($0.75M repair savings, $100k/site software licenses, 120 pilot machines, 800 total machines) lack explicit evidence tags (`[Assumption]`).

### Attack 6: Unexplained IRR Mechanics (172% vs 562%)
- **Comex Finance Pushback:**
  > *"Table 8.2 reports Base Case IRR = 172%. But if I take the net operational cash flows from your own Table 8.1 ([-0.72, +2.96, +9.56, +13.37, +14.15, +14.15]), the Excel XIRR / numpy IRR is **561.9%**! Because you invest only $0.72M upfront and generate $2.96M net in Year 1, your internal rate of return is astronomically high. Where does 172% come from? If you used a Modified IRR (MIRR) or divided by total 3-year expenditure ($4.83M), you must state your formula! You cannot report arbitrary IRR figures to a corporate finance committee."*
- **Forensic Finding:** The IRR figures in Table 8.2 (172% Base, 94% Downside, 255% Upside) do not match the standard internal rate of return of the cash flow streams shown. The document must explicitly define the calculation method (e.g. MIRR with 10% reinvestment rate, or annualized return on cumulative peak capital outlay).

---

## 4. Detailed Section-by-Section Audit

| Section | Course & AGENTS.md Requirement | Status in Case Study | Forensic Evaluation & Deficiencies |
| :--- | :--- | :---: | :--- |
| **1. Problem & Baseline** | Global scope (1,526 kb/d, Factbook p. 135), ERM $7.1/b, asset classes, downtime cost. | ⚠️ Compliant with minor gaps | • Excellent operational framing of rotating machinery failure modes.<br/>• Throughput cites `CLM-064` instead of `CLM-052`.<br/>• Outage costs ($1.5M–$5.0M) and machine counts (120 / 800) lack `[Assumption]` tags. |
| **2. Why AI & Non-AI** | Rejection of conventional alternatives; early warning mechanism (multi-parameter). | 🟢 Fully Compliant | • Comprehensive evaluation of ISO 10816 thresholds, PM overhauls, and manual rounds.<br/>• Clear explanation of 14–30 day early warning multi-sensor anomaly detection. |
| **3. Horizon Justification** | Three Horizons framework; 4 placement questions; Horizon 1 defense. | 🟢 Fully Compliant | • Rigorous evaluation of Q1 (Customer), Q2 (Business Model), Q3 (Proven Tech), Q4 (Time to Value < 12 mo).<br/>• Unambiguous Horizon 1 classification. |
| **4. Data Assets & Dependencies** | Hard vs soft dependencies; AspenTech Inmation slice (`CLM-018`); architecture. | ⚠️ Compliant with minor gaps | • Strong architecture flow and thin-slice discipline.<br/>• Needs explicit ATEX Zone 1 wireless protocol definition (WirelessHART / ISA100.11a).<br/>• Classify site security approvals as political/organizational dependencies. |
| **5. Sourcing Strategy** | Build vs Buy vs Blend; Gartner (2025) H1 framework. | 🟢 Fully Compliant | • Well-reasoned rejection of pure build and pure buy.<br/>• Adopts Blend (vendor APM + internal AspenTech pipeline).<br/>• *Comex note:* Negotiate APM licenses within existing AspenTech enterprise contract. |
| **6. Pilot, Rollout & Governance** | Agile Delivery Trio; pilot at Normandy; multi-site phasing; milestone gates. | 🔴 Deficiencies Identified | • Agile Delivery Trio is well-structured.<br/>• **Fatal Stop Rule flaw:** Month 9 Kill Gate requires $\ge 2$ physical degradation events on 120 machines over 6 months; penalizes healthy assets.<br/>• Superintendent labor rate underprices French refinery senior cadres. |
| **7. Economic Model & Costs** | Bottom-up 3-yr budget ($4.83M); benefit formulas; peer cross-check. | 🔴 Deficiencies Identified | • Squad labor costing is mathematically sound.<br/>• **Fatal capex phasing error:** $0.45M sensor capex committed in Year 0 for 5 sites before pilot runs.<br/>• **Fatal benchmark fudge:** Equinor benchmark multiplied by 520 machines instead of 800 in scope. |
| **8. Cash Flows & Scenarios** | 5-year cash flows; 10% hurdle rate; Base/Downside/Upside NPV and IRR. | 🔴 Deficiencies Identified | • **Fatal Downside contradiction:** Narrative ($5.59M/yr) contradicts Table 8.2 ($8.00M/yr). True downside NPV is +$11.1M, not +$17.4M.<br/>• Upside labeled "$33/b" but valued at only $24.0M/yr ($33/b gives $66.25M/yr).<br/>• Base IRR of 172% does not match standard cash flow IRR (562%).<br/>• Line 189 cites ECB exchange rate (`CLM-071`) for payback. |
| **9. Adoption, Risks & Controls** | Alert fatigue; human-in-the-loop (`CLM-026`); ATEX/SEVESO; Stop rule. | ⚠️ Compliant with minor gaps | • Excellent explainable anomaly cards and SIS protection.<br/>• Stop rule needs backtesting metric.<br/>• **Missing labor relations:** No mention of French statutory employee consultation (CSE / CSSCT) for refinery technician workflow changes. |
| **10. Sources & Limits** | Registered claims, limits, primary sources (Factbook, URD, Apec, INSEE). | ⚠️ Compliant with minor gaps | • Good coverage of primary documents.<br/>• `CLM-037` should be `[Calculation]`, `CLM-041` should be `Pending`.<br/>• Refine throughput claim reference to `CLM-052`. |

---

## 5. Numbered Actionable Recommendations for Approval

To obtain formal approval from the Executive Committee and achieve submission readiness for Step 12, the authors must implement the following **six corrective actions**:

### Fix 1: Reconcile Downside and Upside Scenario Mechanics in Section 8.2
- **Downside Case:** Harmonize the narrative in Line 199 with Table 8.2. Either:
  - *Option A (Recommended — Rigorous):* Adopt the true parameters (0.25% availability gain + $5.3/b ERM + $0.75M repair savings = **$5.59M/yr**). Update Table 8.2: Annual Value = **$5.59M/yr**, 5-Year Net Cash Flow = **+$15.8M**, NPV @ 10% = **+$11.1M**, NPV @ 12% = **+$10.3M**.
  - *Option B:* Retain the $8.00M/yr figure in Table 8.2, but correct the narrative in Line 199 to state: *"refining margins compress to $5.3/b and availability gain drops to 0.38% (or ERM remains $7.1/b with availability gain dropping to 0.28%)"*.
- **Upside Case:** Fix the misleading header in Table 8.2. Change `Upside Case (High Margin $33/b)` to **`Upside Case (Moderate Margin Surge $11.5/b or High Availability Recovery 0.85%)`**, or if keeping $33/b, calculate the true upside value at **$66.25M/yr** (NPV @ 10% = +$178M).

### Fix 2: Resolve the 520 vs 800 Machine Fleet Discrepancy in Section 7.2
- Remove the artificial 520-machine calculation that manufactures a 1% match.
- State transparently:
  > *"Across TotalEnergies' 8 target operated platforms (~800 critical rotating machines total): applying Equinor's full peer benchmark of ~$29,000/machine/yr (`CLM-037 [Calculation]`) yields a gross potential of **$23.2M/yr**. If we conservatively assume that only ~65% of machines (~520 machines) achieve full alert-driven trip avoidance in the first 3 years, the Equinor benchmark indicates **$15.08M/yr**, perfectly aligning with our bottom-up throughput recovery estimate of $15.00M/yr."*
- Explicitly note the limitation: Equinor's benchmark originates from offshore North Sea turbomachinery, where logistics and deferral costs exceed onshore refining. Retype `CLM-037` to `[Calculation]`.

### Fix 3: Reformulate the Month 9 Kill Gate Stop Rule in Sections 6.2 and 9.3
- Eliminate the perverse requirement that machines must physically break during the 6-month live monitoring phase.
- Redefine Gate 3 threshold to a 3-part composite rule:
  1. **Historical Backtest Detection Rate:** Model successfully detects $\ge 80\%$ of documented historical failure precursors on 5-year replayed Normandy DCS telemetry logs.
  2. **Operational False Positive Rate:** Running live on 120 machines, false alarm rate is strictly $< 1\text{ per machine per quarter}$ (or $< 5\%$ of total alert volume).
  3. **Operational Buy-In:** Site Maintenance Superintendent and reliability team sign off on explainable anomaly card usability.
  - *Hard Stop:* If historical detection is $< 70\%$ or false alarm rate exceeds $10\%$, rollout is terminated.

### Fix 4: Re-Phase Sensor Hardware Capex in Table 7.1
- Restructure the Sensor Hardware line in Table 7.1 to respect stage gates:
  - **Year 0 (Normandy Pilot):** 30 un-instrumented machines × $3k = **$0.09M** (CAPEX).
  - **Year 1 (Wave 1 — 4 platforms):** 4 × 30 machines × $3k = **$0.36M** (committed only after Month 9 Gate 3 clearance).
  - **Year 2 (Wave 2 — 3 platforms):** 3 × 30 machines × $3k = **$0.27M**.
  - **Year 3:** $0.00M.
  - *Total Hardware CAPEX:* **$0.72M** (unchanged total, but risk-free phasing).
- Update Line 226: Stopping at Month 9 commits $0.09M hardware + $0.08M Trio + $0.05M cyber + $0.14M software in Y0 ($0.36M), plus 9 months of Y1 ($0.59M) = **$0.95M spent**, canceling **$3.88M** in remaining capital.

### Fix 5: Clean Up Citation Tags and Unpack Untyped Assumptions
- **Correct Line 189:** Remove `(CLM-071 [Calculation])`. Replace with `[Calculation on internal project cash flows]`.
- **Retype Peer Claims:**
  - `CLM-037`: Label as `[Calculation]` (Equinor $29k/machine derived from $120M / 6 / 700).
  - `CLM-041`: Label as `[Pending vendor claim]` (Shell 10,000+ machines from C3 AI vendor marketing).
- **Refine Throughput Citation:** Reference `CLM-052 [Fact]` for the 1,526 kb/d throughput and regional breakdown (France 470, Europe 606, RoW 449).
- **Tag Assumptions:** Explicitly add `[Assumption]` to:
  - Line 26: $1.5M–$5.0M lost margin per major trip.
  - Line 38–39: 120 pilot machines at Normandy; ~800 machines across 8 platforms.
  - Line 162: $0.75M/yr secondary repair avoidance.
  - Line 149: $100k/site-yr APM software license.

### Fix 6: Clarify IRR Methodology in Table 8.2
- Explain the basis of the reported IRR figures:
  - If standard Excel/numpy cash flow IRR is used, report **562%** for Base Case and **296%** for Downside Case (reflecting the tiny $0.72M upfront outlay against immediate Year 1 operational cash generation).
  - If a Modified IRR (MIRR with 10% reinvestment rate) or return on cumulative 3-year commitment ($4.83M) was used to arrive at 172%, provide the explicit formula in a footnote.

### Fix 7: Integrate French Social Dialogue (CSE / CSSCT) into Section 9
- In Section 9.1, add a dedicated paragraph addressing French industrial labor relations:
  > *"Social Dialogue & Works Council Engagement: At French platforms (Normandy, Donges, Feyzin), digital workflow modifications and tablet-based maintenance alerts fall under the consultation purview of the Comité Social et Économique (CSE) and Commission Santé, Sécurité et Conditions de Travail (CSSCT). The Business Champion will lead early ergonomics and workload briefings with employee representatives to position the tool as an operator safety and workload-reduction assistant, mitigating union pushback."*

---

## 6. Review Conclusion

Case Study P01 is an industrial cornerstone with outstanding technical and operational depth. It captures the essence of TotalEnergies' refining optimization challenge and makes brilliant use of the contracted AspenTech Inmation fabric.

Once the **six actionable fixes** above are integrated—reconciling the downside mathematics, harmonizing the fleet benchmark, fixing the stop rule, re-phasing sensor capex, cleaning citation tags, and clarifying the IRR—`work/projects/case_p01_refining_pdm.md` will be an unassailable, submission-ready exemplar for the executive committee and course examiners.

**Verdict:** 🔴 **REQUEST CHANGES** pending resolution of Fixes 1–6.
