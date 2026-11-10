# AI readiness and competing bottlenecks

- **Step:** 09 — [#9](https://github.com/Xenodion/ai-transformations-navy/issues/9). Co-authored by Alexandre Waerniers & Vincent Lamy, with Claude Code.
- **Acceptance criterion:** score the five pillars and readiness stage with evidence and limits; compare bottleneck candidates without generalising from Argedis.
- **Inputs:** [S04 strategy](../../sources/synthesis/2026-11-08_totalenergies_strategy_activities.md), [S05 AI and organisation](../../sources/synthesis/2026-11-08_totalenergies_ai_data_organization.md), [S06 competitors](../../sources/synthesis/2026-11-08_competitors_benchmarks.md), [legacy plan audit](../research/legacy_plan_audit.md), [long list](../projects/long_list.md), [register](../../sources/register.md), [Factbook 2025](../../sources/primary/totalenergies_factbook-2025_2026_en.xlsx), [URD 2025](../../sources/primary/totalenergies_universal-registration-document-2025_2026_en.pdf).
- **Framework:** course session 1: 5 maturity pillars, 5 readiness stages, name the bottleneck pillar ([cheat sheet](../../course/exam/session_1_cheat_sheet.md)).
- **Status:** provisional outside-in assessment under revision. Scores and the proposed bottleneck are hypotheses, not an internal audit or a verified company-wide ranking.

## 1. Limits of this assessment

- **Outside-in and ground-level reconciliation.** Every source is public or registered primary data (URD 2025, Factbook 2025, FY2025 releases), paired with Vincent's recorded local observation at Argedis (CLM-074).
- **Absence of disclosure is not absence of practice.** Non-disclosure of AI value is common among peers (S06:40) and does not prove lack of value. Conversely, published tool rollouts do not prove frontline operational adoption.
- **Group level.** The sources describe the group, OneTech and the Digital Factory, not operating sites. Maturity is uneven: subsurface and trading are further advanced than industrial sites and retail.
- **Local observation boundary.** Vincent's Argedis testimony (CLM-074) is an illustrative downstream signal of delivery friction; it is not extrapolated to deepwater E&P or power trading (AGENTS.md rule 4).

## 2. Pillar scores

**Scale:** 1 = Exploring, 2 = Planning, 3 = Implementing, 4 = Scaling, 5 = Realizing, using each pillar's stage descriptors from the course.

**Confidence:**
- High: several primary sources agree.
- Medium: primary sources, but partial or company claims.
- Low: the score rests mainly on missing evidence.

| Pillar | Score (range) | Evidence for a higher score | Evidence for a lower score | Confidence |
| --- | --- | --- | --- | --- |
| **Business strategy** | **3** (3–4) | Four named AI priorities for 2026 (CLM-024). Board review of AI in 2025 and a planned 2026 review (CLM-025). Large funded programmes: Mistral subsurface, > €100M (CLM-021); Cognite and AspenTech rollouts (CLM-018, CLM-019). Digital is about 30% of > $1bn of R&D, innovation and digital effort (CLM-013) | No AI budget or value target is disclosed. No AI contribution is stated for the $12.5bn savings plan (CLM-007). The Board itself plans to "review the assessment of the impact of technological disruptions, including artificial intelligence" (CLM-025), so the link to value is still being assessed | Medium |
| **Technology and data** | **3** (2.5–3.5) | > 10,000 live AI models (CLM-017) imply production infrastructure. In-house HPC for subsurface (S05). Global methane data centralised in Pau (S05) | The industrial data foundation is still being built: AspenTech until about 2027 and Cognite until about 2028 (CLM-018, CLM-019). The OneTech president's aim of a foundation "which unifies our industrial data globally" implies it was not unified in 2025 (S05). The company says "without robust data, there can be no effective AI" (SRC-011, p. 10). The IEA notes that legacy assets lack the infrastructure (CLM-044) | Medium |
| **AI strategy and experience** | **3.5** (3–4) | Digital Factory of ~500 experts since 2020, about 100 solutions, 60% with AI (CLM-016, CLM-017). Long-standing subsurface AI (S05). In-house trading ML: Predictive Layer, Quadra (CLM-027). Model count on a par with Shell's (CLM-041) | The course's scaling criterion is "repeatable processes for systematic ROI", and no ROI or value is published for any solution (CLM-029). Solutions are "progressively being deployed", with no deployment rate (Q02) | Medium |
| **Organisation and culture** | **2.5** (2–3) | A Digital Line created in Sept 2025 coordinates the branches' digital plans (CLM-015). Copilot rolled out widely from 2024 (CLM-022). GenAI training season of the Digital Accelerator (S05). Close to 510,000 training days a year (CLM-073). Local branch decision-making was observed at Argedis (CLM-074); group-wide rights remain unknown (CLM-030) | Local observation reports delivery and business-capacity friction at Argedis (CLM-074); group-wide prevalence is unknown. URD p. 138 explicitly names the pace of organization and skills adaptation as a material operational risk (CLM-014) | Medium |
| **AI governance** | **2.5** (2–3) | A published principle: no fully autonomous decisions, with traceability (CLM-026). Board oversight (CLM-025). AI and cyber appear in the risk factors (CLM-014, S04) | No AI charter, central model inventory or AI Act classification found for > 10,000 live models (Q05). At scaling and realizing, the course expects "systems that log use cases, performance and limits". Obligations are coming: AI literacy already applies (CLM-059); Annex III high-risk uses from 2 Dec 2027 per the amended timeline (CLM-072, pending) | Low (absence of evidence) |

**Reading the scores:** strategy, data and expertise reflect substantial corporate investment. Possible organisation and governance constraints require internal testing; public non-disclosure does not establish that value tracking or deployment practices are absent.

## 3. Readiness stage

**Provisional Stage 3: Implementing (potential transition to Stage 4: Scaling).** Confidence: low to medium because deployment coverage and internal measurement are not public.

- **For Implementing:**
  - pilots and solutions are in production but "progressively being deployed" (CLM-017);
  - data foundations are still rolling out to 2027–2028 (CLM-018, CLM-019);
  - technical costs are high (> €100M Mistral, ~500 TDF specialists, platform licenses) while P&L value is not publicly disclosed (CLM-029).
  - This matches the classic **"Implementing Trap"** (Course Session 1): 36% of enterprises sit here, where costs peak before measurable value arrives, and only 23% report seeing significant value (vs 61% at Scaling).
- **For Scaling:**
  - the volume of production models (> 10,000 deployed instances);
  - group-wide platforms (Cognite, AspenTech) and employee Copilot access;
  - in-house trading AI and proprietary subsurface HPC.
- **Why Scaling is not established:** the course defines Scaling by repeatable processes and cross-organizational adoption. Internal value tracking, deployment coverage and delivery latency are unknown (Q01–Q03); absence of public disclosure does not prove their absence.

## 4. Competing bottlenecks and the execution flywheel

A bottleneck is the constraint that most limits progress. **Working hypothesis:** delivery and adoption may constrain selected use cases. The group-wide binding constraint, decision rights and funding remain unknown (CLM-030); compare alternatives before generalizing Argedis observations.

| # | Candidate | Pillar | Evidence for | Evidence against | Test before step 11 | Strategic Role in the Transformation | Rank |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | Industrial (OT) data not yet unified across sites | Technology and data | Company calls data the precondition; rollouts run to 2027–2028; IEA legacy caveat (CLM-044); industrial use cases depend on it | Already contracted and funded (CLM-018, CLM-019); > 10,000 models run; thin slices unblock specific use cases | Which sites lack a usable slice at end-2027? | Handled by sequencing thin data slices with use cases, not by a new platform | 2 |
| B2 | No system to measure and capture AI value | Governance, and AI strategy | No value published in filings (CLM-029); Board wants impact reviewed in 2026 (CLM-025); savings plan levers undisclosed (CLM-007) | Branches track project progress internally; absence of filing publication is not lack of internal awareness | Look for internal value tracking (Q03) | **Essential governance dashboard (Enabler E01)**: required for kill criteria and proving cash returns | 2 (Enabler) |
| **B3** | **Execution throughput, delivery velocity & frontline adoption** | **Organisation and culture (Pillar 4)** | Local Argedis observation suggests handoff friction and limited protected business time (CLM-074); the URD names organisational adaptation as a risk (CLM-014). Neither establishes group-wide prevalence. | Other constraints may dominate; delivery time, decision rights and resource allocation across branches are unknown (Q01–Q03). | At month 3, compare timestamps, blocked work, available business time and adoption across selected projects and branches. | **Candidate bottleneck**; retain alternatives pending evidence. | **Hypothesis** |
| B4 | Model risk and AI Act compliance across > 10,000 live models | AI governance | No public inventory found (Q05); Annex III high-risk applicability for gas/power safety components (CLM-058) | Human-in-the-loop principle established (CLM-026); HSE safety culture strong | Check internal MLOps logging | Merged into the E01 Value Register governance workflow | 4 |
| B5 | Scarce AI talent | Organisation and culture | Headcount ambiguity (~500 vs 500 by 2027, CON-001) | ~500 TDF experts + India center (CLM-016); > 3,000 OneTech engineers; Mistral partnership (CLM-021); talent is present, delivery interface is missing | Vacancy rates in branch teams | Solved by Agile Trios pairing central DS with branch champions | 5 |
| B6 | Cross-entity delivery coordination drag | Organisation and culture | Digital Line coordinates group plans (CLM-015); CLM-074 reports local coordination friction. Group-level authority and ownership are not established. | Existing branch capabilities may already handle coordination | Test handoff times and decision ownership across several branches | Trial Agile Delivery Trios where the evidence supports them | Related to B3 |

## 5. Ground-level evidence from Argedis (CLM-074)

Vincent Lamy's observation at Argedis (CLM-074; approximately 150–200 company-operated sites in the recorded observation) illustrates possible local execution friction; it does not establish a group-wide bottleneck:
1. **The Central Funnel:** Technical data science expertise is centralized at the Digital Factory in France. Branches request projects, which queue in the central intake backlog.
2. **Delivery Latency & Multi-BU Drag:** Progress reviews involve 3–4 entities without direct hierarchical reporting (branch data engineering, central TDF data scientists, operating business users, and branch digital transformation lead). Workload saturation across entities extends delivery cycles.
3. **The Business Ownership Gap:** Business domain users are motivated but lack protected, ring-fenced time. Solutions arrive as external consulting deliverables ("au compte-goutte"), dampening local ownership and pushing frustrated staff toward unmanaged Shadow AI.
4. **Local decision reality:** Branch management was observed giving Go/No-Go and allocating budget locally. Group-wide decision rights and whether they constrain delivery remain unknown (Q01).

## 6. Unified strategic conclusion for step 11

**Candidate bottleneck: delivery and operational adoption (Pillar 4: Organization & Culture).**
TotalEnergies has substantial digital capability and active data-platform initiatives. The hypothesis that handoffs and business capacity constrain deployment must be compared with data, governance, funding and skills constraints across several business units:

$$\text{Agile Delivery Trios} \implies \text{Faster Delivery Velocity} + \text{Higher Frontline Adoption} \implies \text{Faster Verified P\&L ROI} \implies \text{Capital Unlocked for Secondary Projects}$$

- **The proposed constraint to test:** Pillar 4 (organisation and culture): possible handoff delays and insufficient protected business time; compare with alternative constraints and internal measurements.
- **The Strategic Remedy (Step 10):** A **Hub-and-Spoke Operating Model powered by Agile Delivery Trios** (*Trinômes Exécutifs*), pairing a Lead Data Scientist (Hub) with a ring-fenced Business Champion (Branch) and a Branch Data Engineer.
- **The Governance Vehicle:** The **AI Value Register (Enabler E01 / B2)**, serving as the Comex control dashboard to verify P&L delivery and enforce stage-gate kill criteria.

## 7. Consistency checks

- Reconciled with registered claims CLM-001 to CLM-074, SRC-002 (URD 2025, p. 138), and SRC-034 (Factbook 2025).
- Stage 3 placement aligns with S05 and S06.
- Direct operational bridge established to Step 10 (Operating Model) and Step 11 (Portfolio Selection).
