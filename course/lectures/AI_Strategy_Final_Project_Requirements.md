# Final Project Requirements: Comex Memo & Board-Level Defence
**Course:** AI Transformation Strategies (MSA-BUS09-01) — Albert School  
**Professor:** Lionel Gourvitch (Microsoft | Albert School)  
**Deliverable Weight:** 30% Oral Project (Final Capstone Evaluation)  
**Target Date:** 16 November 2026  
**Format:** 2-Page Executive Comex Memo + Detailed Topic Plans (Appendices) + 20-min Oral Board Defence  

---

## 1. Executive Summary & Evaluation Context

According to the official syllabus and course master deck (*AI Transformation Strategies*, Slides 6, 48, 145–150, 186–206), the final capstone project requires student teams to act as the executive AI leadership team for a real company (e.g., from the supplied corporate dossier such as TotalEnergies). 

The mission is to present and defend an enterprise-grade AI Transformation Strategy before a **sceptical Board of Directors / Comex (Executive Committee)**.

### Core Logistics & Constraints
* **Team Size:** Groups of 3 to 5 students (Slides 6 & 48).
* **Oral Defence Timing:** Strict **20 minutes total** (Slide 48):
  * **15 minutes:** Executive Strategy Pitch.
  * **5 minutes:** Q&A / Interrogation under sceptical board questioning.
* **Role-Play Dynamics:** The professor plays the role of the **sceptical CEO / Chairman of the Board**. The student team plays the role of the **Chief AI Officer / Transformation Steering Committee**.
* **Deliverable Formats (Slide 206):**
  1. **2-Page Executive Comex Memo:** The core decision paper (Executive Summary).
  2. **Detailed Plans & Topic Dossier:** In-depth backup analyses for each strategic dimension (Readiness & Bottlenecks, Operating Model, Portfolio Sequencing & Sourcing, Financial Model & 3-Year Envelope, 3-Page Change Management Plan).
  3. **Board Presentation Deck:** Visual decision pack with assertion headlines and traceable evidence.

---

## 2. Deliverable Architecture: The 2-Page Comex Memo

The Comex Memo is an executive decision contract, not an academic paper or a technical architectural document. It must adhere strictly to the **7 Blocks / 8 Components Structure** defined in Slides 190–196.

> **Absolute Rule (Slide 190):**  
> *"Two / Three pages maximum. No architecture diagrams. Numbers a decision-maker can audit."*  
> Page 1 covers Blocks 1 to 4; Page 2 covers Blocks 5 to 8.

```
+-----------------------------------------------------------------------------------------+
|                                2-PAGE COMEX MEMO STRUCTURE                              |
+-----------------------------------------------------------------------------------------+
| PAGE 1: STRATEGIC THESIS, PORTFOLIO & VALUE SCENARIOS                                   |
|   1. Thesis: Quantified decision, context, maturity stage, strategic rationale, call.   |
|   2. Portfolio: Three Horizons mix (H1/H2/H3), use cases, business owners, value levers.|
|   3. Investment Envelope: 3-year spend by 6 cost categories, Capex vs Opex, run-rate.   |
|   4. Scenarios: Downside / Base / Upside, explicit assumptions, probabilities, EV.      |
+-----------------------------------------------------------------------------------------+
| PAGE 2: CAPITAL CLEARANCE, GOVERNANCE, CHANGE & THE ASK                                 |
|   5. Hurdle Clearance: EV IRR vs Hurdle Rate (WACC + premium), NPV, Cost of Inaction.   |
|   6. Risks & Kill Criteria: Pre-agreed decision rules (Metric + Threshold + Date + Owner)|
|   7. Change Management & Operating Model: Archetype, 4 failure modes, 3 training tiers. |
|   8. The Ask: Exact capital amount, Tranche 1 release today, stage-gates, date.         |
+-----------------------------------------------------------------------------------------+
```

---

## 3. Section-by-Section Exact Requirements

### Block 1: The Investment Thesis & Decision (Slides 191, 192)
* **Lead with the Decision:** Write the thesis not as an aspiration, but as an auditable investment resolution.
* **Mandatory Syntactic Formula (Slide 192):**
  > *"Invest **[Amount]** over **[Period]** in **[Portfolio]** to achieve **[Business Outcome]**, with **[Downside Cap]** and **[Decision Gate]**."*
* **Anti-Pattern (Weak Phrasing):** *"We will become an AI-first organisation."* (Rejected by Board).
* **Strong Phrasing Example:** *"Invest €52M over 3 years across 4 enterprise use cases to unlock €82M in 5-year expected benefits, with losses capped at −€27.3M and Tranche 2 contingent on Gate 1 adoption."*
* **Context & "Why Now":** Concisely justify using company maturity stage, market disruption, competitor speed, and regulatory windows.
* **Call to Action:** State explicitly: *"We request this meeting for formal approval of Tranche 1 (€XM) to fund Year 1 operations."*

---

### Block 2: Portfolio & Sourcing Strategy (Slides 87–93, 190, 194)
* **Portfolio over Pilots:** Present a coherent strategic portfolio rather than a disconnected list of experiments.
* **Three Horizons Architecture (McKinsey / Baghai et al.):**
  * **Horizon 1 (H1 — Efficiency / Core):** Near-term productivity, cost-to-serve reduction, immediate workflow automation.
  * **Horizon 2 (H2 — Augmentation / Extension):** Enhanced decision-making, revenue acceleration, proprietary workflows.
  * **Horizon 3 (H3 — Transformation / New Models):** Long-term strategic options, new AI-native business models, defensibility.
* **Capital Allocation Heuristic (Nagji & Tuff):**
  * Baseline allocation rule: **70% H1 / 20% H2 / 10% H3**.
  * **Deviation Rule:** Deviate on purpose, never by drift. Any departure from 70-20-10 must be explicitly justified by industry context, risk appetite, or corporate debt profile.
* **Sourcing Classification (Gartner Build / Buy / Blend Matrix):**
  * Every use case must be designated: **BUY** (commodity / H1), **BLEND/PARTNER** (differentiating data + foundation models / H2), or **BUILD** (proprietary core advantage / H3).
* **Accountability:** Every single initiative must have a **named Business Owner (P&L sponsor)** and measurable value levers.

---

### Block 3: The 3-Year Investment Envelope (Slides 113–123, 143, 195)
* **The 6 Mandatory Cost Categories (Slide 114):**
  1. **Compute:** Cloud GPU/TPU capacity, token consumption, inference/training infrastructure.
  2. **Talent:** Internal AI engineering, product managers, data scientists, external contractors.
  3. **Integration:** Legacy ERP/CRM connectors, API middleware, enterprise system plumbing.
  4. **Model Operations (LLMOps/MLOps):** Monitoring, evals, drift detection, fine-tuning, latency optimization.
  5. **Data Acquisition & Engineering:** Data pipelines, labeling, synthetic data, vector databases, cleaning.
  6. **Governance & Legal:** Compliance auditing, EU AI Act certification, legal counsel, risk monitoring.
* **Spend Profile across Years 1, 2, and 3:**
  * Highlight Year 1 as the build-heavy foundation tranche.
  * Show the operational transition: Model Operations and Governance expand from Year 1 to Year 3 while initial compute setup and external integration taper.
* **Steady-State Run Costs:** Clearly state the annual operational run-cost from Year 4 onwards (e.g., *“Run cost €6M/year from Year 4”*).
* **Capex vs Opex Treatment (Slide 102):** Explicitly recognize that cloud AI shifts spend towards Opex, and distinguish software capitalization from expensed exploratory research.

---

### Block 4: Scenarios & Expected Value (EV) (Slides 125–130, 190, 196)
* **Honest Scenario Modeling:** Prohibit false precision. You must present three distinct, probability-weighted scenarios:
  1. **Downside Scenario (e.g., 20–30% probability):** Adoption lags, integration costs persist, model performance underwhelms. **Must show an honest negative NPV and negative IRR** alongside an explicit **Loss Cap** and corrective intervention trigger.
  2. **Base Scenario (e.g., 50% probability):** Measured adoption, target productivity gains realized, hurdle rate comfortably cleared.
  3. **Upside Scenario (e.g., 20–30% probability):** Rapid enterprise adoption, accelerated network effects, reinvestment option triggered.
* **Expected Net Present Value (ENPV):**
  $$\text{ENPV} = \sum_{i} p_i \times \text{NPV}_i$$
* **Parameters per Scenario:** For each scenario, state probability ($p$), user adoption rate, unit economics, cash-flow timing, and the pre-agreed executive response.

---

### Block 5: Financial Hurdle Clearance & Opportunity Cost (Slides 106–112, 128–133, 195)
* **The Hurdle-Rate Benchmark:**
  $$\text{Hurdle Rate} = \text{WACC} + \text{AI Strategic Risk Premium} \quad (\text{typically } +2\% \text{ to } +6\%)$$
  *(Example: WACC 8.5% + Premium 3.5% = 12.0% Hurdle Rate).*
* **Dual Acceptance Test:**
  * $\text{Expected IRR} > \text{Hurdle Rate}$ (Must demonstrate headroom, e.g., +4 to +5 percentage points).
  * $\text{ENPV} > 0$ evaluated at the Hurdle Rate (not just at WACC).
* **The Cost of Inaction (Opportunity Cost of Waiting) (Slides 131–133):**
  * Doing nothing is **not zero cost**. Inaction incurs competitor market share capture, customer churn, margin degradation, and talent attrition.
  * Quantify the **NPV of Inaction** as an explicit negative cash flow.
  * Calculate **Decision Value / Incremental NPV**:
    $$\text{Incremental NPV} = \text{NPV}(\text{Investment}) - \text{NPV}(\text{Inaction})$$
* **Productivity J-Curve Timing (Slides 138–143):**
  * State the cash-flow trough depth (maximum capital at risk) and the exact break-even year (typically Year 3 or Year 4).

---

### Block 6: Risks & Pre-Agreed Kill Criteria (Slides 170, 182, 197, 198)
* **Four Enterprise Risk Dimensions & Executive Owners (Slide 197):**
  * **Value Risk:** Failure to translate AI productivity into real P&L savings or revenue. *(Owner: CFO + Lead Business Sponsor).*
  * **Delivery Risk:** Technical debt, broken pipelines, vendor lock-in, latency bottlenecks. *(Owner: CIO / Chief AI Officer).*
  * **Trust & Compliance Risk:** Data privacy leaks, hallucinations, bias, regulatory breach. *(Owner: Chief Risk Officer / General Counsel / DPO).*
  * **People & Adoption Risk:** Workforce resistance, middle-management blocking, talent attrition. *(Owner: CHRO + BU Heads).*
* **Mandatory Kill Criterion Formulation (Slide 198):**
  * Every use case and every funding tranche must have an explicit stop rule following the mandatory 5-part formula:
  $$\mathbf{\text{Metric}} + \mathbf{\text{Threshold}} + \mathbf{\text{Date}} + \mathbf{\text{Owner}} + \mathbf{\text{Action}}$$
  * **Unacceptable Pseudo-Rule:** *“We will review adoption regularly.”* (Immediate board rejection).
  * **Acceptable Contractual Rule:** *“If verified active user adoption across plant supervisors is below 40% at Month 12, pause Tranche 2 disbursement; CFO and BU Head decide within 30 days whether to redesign or permanently kill.”*

---

### Block 7: Change Management & Operating Model (Slides 53–71, 164–185, 199, 200)
* **Target Operating Model Archetype:** Recommend and justify one of the three course archetypes: **Centralised CoE**, **Federated**, or **Hub-and-Spoke (Hybrid)**. Detail the split: *Hub owns platforms, standards, and governance; Spokes own use cases and P&L realization.*
* **The Four AI Failure Modes (Must show signals and owners) (Slide 170):**
  1. *Talent Flight* (Owner: CHRO).
  2. *Middle-Management Sabotage / The Frozen Permafrost* (Owner: BU Heads).
  3. *Governance Lag / Works Council Injunctions* (Owner: General Counsel / DPO).
  4. *Comex Impatience during the J-curve* (Owner: CEO / CFO).
* **Adoption Engine:**
  * **Inverted Communication Cadence:** Daily/weekly two-way huddles on the floor; monthly 1-page dashboards to the Comex.
  * **3 Training Tiers:** Tier 1 (All-employee AI literacy / EU AI Act Art. 4), Tier 2 (Practitioners & translators), Tier 3 (Executive leadership & board coaching).

---

### Block 8: The Formal Ask & Capital Tranches (Slides 143, 144, 189, 191)
* **Precise Capital Resolution:** State the total 3-year commitment requested (e.g., €52M) and the immediate authorization requested today (**Tranche 1 for Year 1**, e.g., €20M).
* **Stage-Gate Release Criteria:**
  * **Gate 1 (End of Year 1):** Specific evidence required to unlock Tranche 2 (e.g., data platform operational, 3 H1 use cases live in production, baseline KPIs measured, zero critical governance breaches).
  * **Gate 2 (End of Year 2):** Criteria for Tranche 3 (e.g., run-rate benefits $\ge$ run-rate costs, BU co-funding reaching 40%).
* **Decision Date:** State the formal vote date.

---

## 4. The Oral Defence & Sceptical Board Interrogation

### The Pitch Architecture (15 Minutes)
1. **Slide 1 — The Executive Recommendation:** Lead with the answer. State the ask, the portfolio ENPV, the hurdle clearance, and the downside cap immediately.
2. **Assertion Headlines Rule (Slide 203):** Every slide must have a single conclusive assertion headline rather than a descriptive topic.
   * *Weak Headline:* “AI Investment Overview.”
   * *Strong Assertion Headline:* “Release Tranche 2 Only After Year-1 Adoption Clears the 40% Gate.”
3. **One Idea Per Slide:** Clean visual storytelling; no wall of text; no ungrounded architecture diagrams. Detailed financial calculations belong in the appendix.
4. **Traceability Rule (Slide 203):** Every metric or financial figure presented must have an auditable **Unit**, **Period**, **Baseline**, **Owner**, and **Source**.

### The Sceptical Interrogation (5 Minutes Q&A)
The professor (acting as CEO) will challenge the team with the **Three Hardest Questions (Slide 204)**. Teams must deliver immediate, evidence-led, concise answers:

| Board Challenge Question | What the Board Is Testing | Required Defence Structure |
| :--- | :--- | :--- |
| **1. "What is the worst case?"** | Risk boundary & capital preservation. | Name downside ENPV, probability, loss cap mechanism, and exact operational cut-off. |
| **2. "What kills it — and when do we stop?"** | Executive discipline vs sunk-cost bias. | State the pre-agreed kill rule: Metric + Threshold + Date + Owner + Action. |
| **3. "What does the competitor do if we don't?"** | Strategic urgency vs reckless spending. | Present the quantified **Cost of Inaction** (PV of lost market share, margin erosion, talent drain). |
| **4. "Why this budget and not half?"** | Portfolio integrity & critical mass. | Explain what cutting 50% removes: cuts H2/H3 strategic advantage, leaves sub-scale foundations with zero ROI. |
| **5. "When do we break even?"** | J-curve comprehension. | State the trough depth, cash break-even month, and leading indicators tracked prior to EBIT impact. |
| **6. "Who in the business co-funds this?"** | Business skin in the game. | Show BU co-funding ramp-up (e.g., 0% Year 1, 40% Year 2, 60% Year 3) to prevent central IT waste. |

---

## 5. Grading Rubric: The 6 Observable Tests (Slide 205)

The oral presentation and memo are graded against **six observable, binary-auditable criteria**:

```
[TEST 1] Decision and ask are explicit
         -> Clear resolution, exact tranche amounts, decision date on page 1.
[TEST 2] Portfolio follows strategic logic
         -> Balanced Three Horizons mix; justified 70-20-10; build/buy/partner scored.
[TEST 3] Economics and assumptions are auditable
         -> 6-category envelope, ENPV, Hurdle > WACC, explicit probabilities.
[TEST 4] Downside and kill gates are credible
         -> Honest negative downside modeled, pre-agreed kill formulas, loss capped.
[TEST 5] Change and governance have owners
         -> Named C-suite owners for all 4 failure modes, 3 training tiers, inverted cadence.
[TEST 6] Answers are concise and evidence-led
         -> Zero hand-waving during Q&A; numbers, dates, and contracts cited immediately.
```

---

## 6. The Board-Ready Final Checklist (Slide 206)

Before entering the boardroom / oral defence, verify that every item on this checklist is resolved:

* [ ] **Decision:** Is the exact resolution to be voted on stated on Slide 1 / Page 1?
* [ ] **Strategy:** Why this specific portfolio of use cases, and why now?
* [ ] **Capital:** Where does every euro go across the 6 cost categories, and when does it return to the P&L?
* [ ] **Risk:** What is the quantified worst case, what is the loss cap, and who owns the control?
* [ ] **Execution:** Who changes their daily work, what enables adoption, and what proves progress before EBIT moves?
* [ ] **Discipline:** What specific, measurable criterion stops, pauses, or scales the programme?
* [ ] **Packaging:** Is the executive memo strictly 2 pages? Are detailed plans attached as clean appendices?
