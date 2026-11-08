# Operating-model options

- **Step:** 10 — [#10](https://github.com/Xenodion/ai-transformations-navy/issues/10). Drafted 8 November 2026 by Alexandre Waerniers, with Claude Code.
- **Acceptance criterion:** compare CoE, hub-and-spoke and federated models against size, regulation, talent and maturity; specify decision rights, funding, controls and evolution.
- **Inputs:** [S04](../../sources/synthesis/2026-11-08_totalenergies_strategy_activities.md), [S05](../../sources/synthesis/2026-11-08_totalenergies_ai_data_organization.md), [S06](../../sources/synthesis/2026-11-08_competitors_benchmarks.md), [readiness assessment](readiness_bottleneck.md) (step 09), [long list](../projects/long_list.md), [register](../../sources/register.md).
- **Framework:** course session 2 ([cheat sheet](../../course/exam/session_2_cheat_sheet.md)): three archetypes, three matching factors, decision tree, evolution path. Funding phases come from course session 3 ([cheat sheet](../../course/exam/session_3_cheat_sheet.md)).
- **Status:** comparison with a provisional preference. Step 11 confirms it together with the thesis.

## 1. Starting point: what exists today

This section reports evidence only. The legacy draft's "hub-and-spoke" recommendation ignored this structure and was discarded as a decision (audit, section 3).

| Element | What it does | Source |
| --- | --- | --- |
| OneTech | Central technical branch since 2021, > 3,000 engineers, technicians and researchers | S05 (SRC-002, pp. 39, 43) |
| Digital Line (in OneTech, since Sept 2025) | "Coordinating the branches' digital transformation plan", providing data and digital services, deploying applications through the Digital Factory; leads the Digital Plant and Digital for HSE programmes | CLM-015 |
| Digital Factory | ~500 digital and AI experts in France and India; about 100 solutions since 2020 | CLM-016, CLM-017 |
| Group platforms | Cognite (all operated upstream assets) and AspenTech (industrial sites), rolling out to 2027–2028 | CLM-018, CLM-019 |
| AI inside the segments | Integrated Power: in-house trading and forecasting ML (Predictive Layer, Quadra). E&P: Subsurface R&D line. Saft: AI in battery R&D. Retail: GenAI customer assistant | CLM-027; S05 |
| Group partnerships | Mistral (lab and subsurface programme), Microsoft (Copilot) | CLM-020, CLM-021, CLM-022 |
| Oversight | Board Strategy & CSR Committee reviews AI; the Executive Committee authorises capex | CLM-025; S04 |
| **Unknown** | Who funds Digital Factory solutions and who prioritises use cases; size of digital teams inside the segments | CLM-030, Q01, Q10 |

**Observation:** this already looks like a central hub with capabilities embedded in the segments, that is, an informal hub-and-spoke. What is missing from the public record is the formal part: decision rights, funding rules and a shared register.

## 2. Matching factors (course session 2)

| Factor | Evidence | What it points to |
| --- | --- | --- |
| **Size and complexity** | 5 segments in distinct markets (oil and gas, LNG, power, refining and chemicals, retail), about 120 countries, 101,513 employees (S04, CLM-001) | Large multi-BU firm: **hub-and-spoke**. The course notes that pure hub models struggle beyond about 4 BUs. It is not a conglomerate of unrelated businesses, so federated is not the default |
| **Regulatory exposure** | Safety-critical industrial sites. AI used as a safety component in gas or electricity supply is high-risk under Annex III (CLM-058), applicable from 2 Dec 2027 per the amended timeline (CLM-072, pending). AI literacy duty in force (CLM-059). Cyber risk named in the risk factors (S04). Many uses (subsurface, trading, back office) are not high-risk | **Mixed but high where it matters.** The course decision tree says "CoE or strong hub": "an auditor won't accept four different answers from four BUs" |
| **Talent footprint** | Concentrated centrally (Digital Factory, OneTech), with deep pockets in segments (trading, subsurface, Saft) and two regions (France, India) (CLM-016, CLM-027) | "Deep talent in BUs → spokes"; "spread across regions → hub with regional spokes" |
| **Maturity** | Late Implementing (step 09); shared platforms still rolling out to 2027–2028 | Past pilots, so hub-and-spoke. **Not ready to federate**: the course says federating needs a mature shared platform first |

**Decision tree:**
1. High regulatory exposure? Yes for safety-critical uses, so **CoE or strong hub**.
2. Several BUs in distinct markets? Yes.
3. Mature, with a strong shared platform? Not yet (2027–2028), so **hub-and-spoke**.

Both branches converge on a **strong hub with spokes in the segments**.

## 3. Options compared

| | O1 — Central CoE | O2 — Strong hub-and-spoke (formalise today's structure) | O3 — Federated |
| --- | --- | --- | --- |
| **How it would work** | Digital Line and Digital Factory build, deploy and run all AI; segments submit requests | Hub (Digital Line and Digital Factory) owns platforms, standards, the model and value register, vendors and shared services. Spokes in each segment choose and deliver use cases with a named business owner | Each segment runs its own AI team, tools and vendors under light group standards |
| **Fit with size** | Poor: 5 segments and 120 countries make a single team a queue (course: bottleneck at scale) | Good | Good on size |
| **Fit with regulation** | Strongest control | Strong, if the hub holds classification, inventory and validation | Weakest: risk of "four different answers" on safety-critical uses |
| **Fit with talent** | Ignores existing segment capability (trading ML, subsurface) | Uses both central and segment talent | Duplicates scarce skills |
| **Fit with maturity** | Suited to early maturity; TotalEnergies is past that | Suited to "enterprises past pilots" | Premature until platforms are complete (2027–2028) |
| **Cost** | High talent need in one pool | Core plus embedded | Course: 2–3 × platform spend by year two |
| **Course failure modes** | Bottleneck, ivory tower, ownership vacuum, talent leaving, shadow AI | Coordination drag, unclear decision rights | Sprawl, duplicated tools, no model inventory, a governance blind spot until an incident |
| **Disruption** | High: pulls capability out of the segments | **Low: builds on the Sept 2025 structure** | High: dismantles the Digital Line's role |
| **Verdict** | Rejected: does not fit size or talent | **Preferred (provisional)** | Rejected for now; it is the target of the evolution path (section 6) |

**Peer signals (context, not proof):**
- Equinor runs digital as an EVP-led business area of 2,129 people (CLM-038, S06).
- Shell's EVP Information and Digital Technology reports to the Audit and Risk Committee (CLM-050).
- Both place digital at executive level. TotalEnergies' CDO sits inside OneTech (S05). Whether the hub needs a seat closer to the Executive Committee is an open design choice for step 11, not a finding.

## 4. Decision rights in the preferred option (O2)

Course roles: the business signs the benefits, and Finance tracks them.

| Decision | Hub (Digital Line and Digital Factory) | Spoke (segment digital team plus business owner) | Group Finance | Risk, Legal, HSE, works council |
| --- | --- | --- | --- | --- |
| Which use cases to pursue | Sets intake criteria; one front door; portfolio view | **Proposes and prioritises** within its segment | Checks the benefit formula and baseline | Classifies risk tier |
| Portfolio approval and stage gates | Prepares the quarterly portfolio review | Presents results against kill criteria | **Co-chairs the review**: releases tranches | Veto on safety or legal grounds |
| Platforms, data slices, tools | **Owns** (Cognite, AspenTech, MLOps, GenAI stack) | Uses; requests slices | — | Cyber review for OT connections |
| Vendors and partnerships | **Negotiates group contracts** (Mistral, Microsoft, Cognite, AspenTech) | Selects among approved vendors | Approves spend | — |
| Model inventory and AI Act classification | **Owns the register** (E01) | Registers every model before go-live | — | **Validates high-risk classifications** |
| Value sign-off | Consolidates the group AI value figure | Business owner **signs** the benefit | **Tracks** and audits | — |
| Talent | Core hiring, standards, training and rotation | Hosts embedded data scientists; owns domain experts | — | — |
| Stop or kill a use case | Recommends | Executes | **Decides with the business owner** at the gate | Can stop on safety or legal grounds |
| Workforce changes | — | Designs with managers | — | **Works council consulted early** (course session 4) |

**Human control:** every high-impact decision stays with an expert, in line with the published principle of no fully autonomous decisions (CLM-026).

## 5. Funding

- **Model:** the course's three-year phasing (Microsoft AI Transformation Office example):

  | Year | Hub (central) | Segments | Phase |
  | --- | --- | --- | --- |
  | 1 | 100% | 0% | Build capabilities |
  | 2 | 60% | 40% | Accelerate |
  | 3 | 40% | 60% | Scale |

- **How it would apply** (assumption, to test with Q01):
  - The hub pays for the register (E01), the thin data slices and the first pilot of each featured use case.
  - Segments co-fund the rollout of use cases that clear their gate. Co-funding is the segments' "skin in the game".
  - The hub keeps 40% in year 3 to keep a decisive seat at the table and to fund H3 bets (P11, P12). H3 bets stay central because no segment would fund an option without payback.
- **Approval:** the envelope is ring-fenced for 3 years and released in annual tranches against gates (course session 3). It sits within the Executive Committee's capex authority. The Board reviews commitments above 1% of shareholders' equity and approves them above 3% (S04); equity is not registered yet, so step 18 checks whether the envelope comes anywhere near these thresholds.

## 6. Controls

- **One register** for every model and use case: owner, risk tier, baseline, benefit formula, performance, limits. This is E01, and it also serves AI Act documentation.
- **Risk tiers with a fast lane:** low-risk uses (back-office GenAI) get a light review. Safety components in gas or electricity supply get full validation and human oversight (CLM-058).
- **Stage gates with kill criteria** (metric, threshold, date, owner, action), defined in step 20.
- **OT cybersecurity review** before any model connects to site systems (long list, C8).
- **Reporting cadence** (course session 4): a monthly one-page dashboard for the sponsor and a quarterly portfolio review. No weekly 40-page steering deck.

## 7. Evolution path and gates

**Course path:** experiment → centralise → hub-and-spoke → federated or advisory, once governance is embedded in the platform. TotalEnergies is at hub-and-spoke.

**Gates to federate a segment** (thresholds are assumptions for step 20):
1. The segment's shared platform slice is live across its target sites: Cognite for upstream, AspenTech for industrial sites (expected 2027–2028).
2. At least 90% of the segment's live models are in the register with an owner and a risk tier.
3. At least two consecutive quarterly reviews with Finance-signed value on the segment's main use cases.
4. No open high-risk compliance findings.

**Signals that the model is failing** (course):
- approval delays;
- knowledge bottlenecks in the hub;
- the hub and segments arguing over priorities;
- shadow AI found outside the register.

**Review:** once a year, at the portfolio review that closes year 1.

## 8. Rejected options and reasons

| Option | Reason |
| --- | --- |
| O1 Central CoE | Does not fit 5 segments in distinct markets; ignores segment talent already in place (trading, subsurface); would recreate the bottleneck the course warns about |
| O3 Federated now | Platforms are not complete (2027–2028); safety-critical regulation needs one answer; course cost and sprawl risks. Kept as the end state of the evolution path |
| Legacy "asymmetric hub-and-spoke by horizon" (hub = Digital Factory + CSTJF) | Built without the Digital Line; discarded as a decision in step 07. One idea is kept: H3 bets are funded centrally (section 5) |
| A new reorganisation | The Digital Line is barely a year old; formalising rights is cheaper and less disruptive than another restructure |

## 9. Open points for step 11

- Funding route and decision rights today (Q01). If segments already fund the Digital Factory, the funding phasing starts later.
- Size of the segment digital teams (Q10). If they are large, the spokes can take more delivery.
- Whether the hub should report closer to the Executive Committee (peer signals, section 3).
- The sponsor: a Comex member who owns the AI portfolio and the monthly dashboard.
