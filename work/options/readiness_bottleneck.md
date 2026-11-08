# AI readiness and competing bottlenecks

- **Step:** 09 — [#9](https://github.com/Xenodion/ai-transformations-navy/issues/9). Drafted 8 November 2026 by Alexandre Waerniers, with Claude Code.
- **Acceptance criterion:** score the five pillars and readiness stage with evidence and limits; compare bottleneck candidates without generalising from Argedis.
- **Inputs:** [S04 strategy](../../sources/synthesis/2026-11-08_totalenergies_strategy_activities.md), [S05 AI and organisation](../../sources/synthesis/2026-11-08_totalenergies_ai_data_organization.md), [S06 competitors](../../sources/synthesis/2026-11-08_competitors_benchmarks.md), [legacy plan audit](../research/legacy_plan_audit.md), [long list](../projects/long_list.md), [register](../../sources/register.md).
- **Framework:** course session 1: 5 maturity pillars, 5 readiness stages, name the bottleneck pillar ([cheat sheet](../../course/exam/session_1_cheat_sheet.md)).
- **Status:** a scored assessment and a ranked comparison. The thesis and the final bottleneck are chosen in step 11.

## 1. Limits of this assessment

- **Outside-in only.** Every source is public, and most are published by the company. The course warns that firms overstate their own maturity, so the scores may be biased upwards.
- **Absence of disclosure is not absence of practice.** Several low scores rest on what the company does not publish (value, model inventory, AI Act classification). Each such point is marked and has a test.
- **Group level.** The sources describe the group, OneTech and the Digital Factory, not sites. Maturity is probably uneven: subsurface and trading look more advanced than industrial sites and retail.
- **No local observation is used.** Vincent's Argedis experience is not yet recorded (Q11), so it plays no part in any score (section 5).

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
| **Organisation and culture** | **3** (2.5–3.5) | A Digital Line created in Sept 2025 coordinates the branches' digital plans (CLM-015). Copilot was rolled out widely from 2024 (CLM-022). GenAI training season of the Digital Accelerator (S05). Close to 510,000 training days a year (CLM-073). The risk factors name the pace of AI adoption as a risk, so leadership is aware (CLM-014) | The structure is new (Sept 2025) with no track record. The CDO sits inside OneTech on the organisation chart (S05), whereas Equinor's digital unit is an EVP-led business area of 2,129 people (CLM-038, S06). Decision rights and funding are unknown (CLM-030). Culture and adoption cannot be observed from outside | Low |
| **AI governance** | **2.5** (2–3) | A published principle: no fully autonomous decisions, with traceability (CLM-026). Board oversight (CLM-025). AI and cyber appear in the risk factors (CLM-014, S04) | No AI charter, central model inventory or AI Act classification found for > 10,000 live models (Q05). At scaling and realizing, the course expects "systems that log use cases, performance and limits". Shell's Audit and Risk Committee lists "AI compliance" as a 2026 priority (CLM-050). Obligations are coming: AI literacy already applies (CLM-059); Annex III high-risk uses from 2 Dec 2027 per the amended timeline (CLM-072, pending) | Low (absence of evidence) |

**Reading the scores:** strategy, data and organisation are at implementing level, and expertise is above it. Governance, in the course's sense of systems that log use cases, performance and limits, is the lowest score and also the least certain one.

## 3. Readiness stage

**Late Implementing, with pockets close to Scaling.** Confidence: medium.

- **For Implementing:**
  - pilots and solutions are in production but "progressively being deployed" (CLM-017);
  - foundations are still being rolled out to 2027–2028 (CLM-018, CLM-019);
  - cost is visible (large programmes) while value is not (CLM-029).
  - This matches the course's "low value, high cost" description, the trap where most firms (36%) sit.
- **For Scaling:**
  - the volume of production models (> 10,000);
  - group-wide platforms and an employee GenAI rollout;
  - in-house trading AI and long-standing subsurface AI.
- **Why not Scaling yet:** the course defines Scaling by "very high value" (61% of scaling firms see significant value). No value is evidenced, so Scaling cannot be claimed from public sources.
- **What would move the placement up:** an internal value register showing material, measured P&L impact (Q03).

## 4. Competing bottlenecks

A bottleneck here is the constraint that most limits the move from Implementing to Scaling. A good candidate is one that an incremental Comex decision can actually unblock.

| # | Candidate | Pillar | Evidence for | Evidence against | Not visible from outside | Test before step 11 | Does a new Comex decision unblock it? | Rank |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | Industrial (OT) data not yet unified across sites | Technology and data | The company calls data the precondition; rollouts run to 2027–2028; IEA legacy-asset caveat (CLM-044); the industrial use cases P01, P02, P03 and P10 depend on it | **Already funded and under way** (CLM-018, CLM-019). The course warns that "dependency claims are often excuses": a slice, not a lake. > 10,000 models already run | Site-by-site coverage and timing | Which sites will still lack a usable slice at end-2027? | Partly. Money is not the constraint; sequencing slices with use cases is | 2 |
| B2 | No system to measure and capture AI value | Governance, and AI strategy and experience | No value published for any internal solution (CLM-029), while Equinor publishes $130M (CLM-035). The Board wants AI's impact assessed in 2026 (CLM-025). Savings-plan levers are undisclosed (CLM-007). Without value data, the company cannot prioritise or stop use cases among > 10,000 models | Absence of publication is not absence of internal tracking (Q03). Equinor's figure has no published method (CLM-035) | Whether the Digital Factory tracks value per solution | Q03: look for internal value tracking (Digital Factory blog, talks, job posts for "value office" roles) | **Yes.** It is cheap (E01: $1.6M over 3 years), sits within the Comex's own remit, and is required for kill criteria | **1** |
| B3 | Adoption and scaling beyond pilot sites | Organisation and culture | About 100 solutions "progressively" deployed, rate unknown (CLM-017). Copilot usage and value unmeasured (CLM-023, pending). The course's top blockers include skills (19%) and culture (14%) | No source supports or refutes "struggles to industrialise" (CON-005). Large training programmes exist (CLM-073) | Deployment rate and active use per solution | Q02: count deployments per solution | Partly. It needs change management per use case (step 20), not a single decision | 3 |
| B4 | Model risk and AI Act compliance across > 10,000 live models | AI governance | No inventory or classification found (Q05). Safety-critical industry; Annex III covers safety components in gas and electricity supply (CLM-058). Peers have formalised AI compliance (CLM-050, CLM-043) | Stated principle of human final decisions (CLM-026); strong general HSE and risk culture | Whether an internal inventory exists | Q05 | Yes, and it shares its foundation with B2: one register can log value, performance and limits | Merged with B2 |
| B5 | Scarce AI talent | Organisation and culture | Headcount ambiguity: ~500 now vs "500 by 2027" (CON-001); the course says only 33% of firms have enough talent | ~500 Digital Factory experts plus an India centre (CLM-016); > 3,500 researchers (CLM-013); OneTech's > 3,000 engineers (S05) | Vacancy and attrition data | Q04 | Not a priority on current evidence | 5 |
| B6 | Unclear decision rights and funding between the Digital Line and the branches | Organisation and culture | The Digital Line "coordinates", without described decision or funding rights (CLM-015, CLM-030); the structure is new | No evidence of conflict or delay | Who funds and who decides | Q01, Q10; step 10 | Yes, through the operating-model choice (step 10) | 4 |

## 5. Argedis

Vincent's experience at Argedis is a possible signal of operational friction (B3). It is **not used** here, for three reasons:
1. It is not yet recorded with observer, entity, period and what was seen (Q11).
2. One retail entity cannot establish group culture or adoption (AGENTS.md rule 4).
3. No group-level source corroborates or contradicts it yet (CON-005).

**How to test it once recorded:** check whether the friction it describes also appears in group-level evidence, for example the deployment rate of Digital Factory solutions (Q02) or Copilot usage (Q09). If it does, it supports B3; if not, it stays a local observation.

## 6. Provisional conclusion for step 11

**Leading hypothesis:** the bottleneck is **AI value and governance**, B2 merged with B4. TotalEnergies runs AI at production scale and is already funding its data foundations, but it shows no system that logs each use case's value, performance and limits. The course names this system as the condition for the Scaling and Realizing stages. Without it, the company cannot prove AI's contribution to its own priorities (the $12.5bn plan, the Board's 2026 review), cannot apply kill criteria, and cannot show AI Act compliance.

This hypothesis is consistent with:
- the S06 implication that "the gap is scaling value, not building models";
- the long-list enabler E01 and the value-capture candidate P05.

**Data (B1) stays the second constraint for industrial use cases.** It is handled by funding the thin slices each featured project needs, not by a new platform (audit, rejected R03).

**What would overturn the hypothesis:**
- Evidence that TotalEnergies already tracks value and inventories models internally (Q03, Q05). In that case B3 (adoption) or B1 (data) becomes the leading candidate.
- Evidence of a measured value gap against peers on a comparable scope. None exists so far (S06).

## 7. Consistency checks

- Scores cite only registered claims or the syntheses; no score uses the legacy draft's numbers, whose pillar scores were discarded (audit, section 3).
- The stage placement agrees with S05 ("progressively being deployed") and S06 (parity on model counts, no value evidence).
- Open questions that could change a score: Q02, Q03, Q04, Q05, Q09, Q11.
