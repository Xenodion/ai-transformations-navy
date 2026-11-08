# Synthesis: How do Shell, BP and Equinor compare with TotalEnergies on AI, and which sector benchmarks are usable?

- Research date: 8 November 2026
- Scope (business, country, period): group-level AI, data and digital practice at Shell, BP and Equinor, compared with TotalEnergies; 2022–2026, mainly FY2025. Sector benchmarks from the IEA.
- Reviewer: Alexandre Waerniers, with Claude Code. Roadmap step 06, issue [#6](https://github.com/Xenodion/ai-transformations-navy/issues/6).
- Original documents read (IDs in [`sources/register.md`](../register.md)):
  - **Equinor:** SRC-017, news release "Use of artificial intelligence saved Equinor USD 130 million in 2025" (7 Jan 2026). SRC-018, *Annual Report 2025* (19 Mar 2026), PDF pp. 14, 23, 80–81, 289 read directly.
  - **Shell:** SRC-019, Capital Markets Day release (25 Mar 2025, SEC 6-K). SRC-020, Q4 2025 unaudited condensed financial report (5 Feb 2026, SEC 6-K EX-99.2). SRC-021, *Annual Report and Accounts 2025* (12 Mar 2026): SEC copy, printed pp. 4–17 and 70–71 read verbatim; local PDF downloaded by Alexandre, pp. 43, 72–73, 113, 127, 135, 143, 156, 170, 215 read directly (risk factors and governance by keyword search). SRC-022, C3 AI release on the Shell collaboration (4 Jun 2026, vendor). SRC-023, C3 AI blog interview with Shell's VP Computational Science & Digital Innovation (7 Mar 2022, vendor-published). SRC-024, SLB announcement of a Shell collaboration (11 Dec 2025, via trade press).
  - **BP:** SRC-025, *Annual Report and Form 20-F 2025*, strategic report section (published 6 Mar 2026), PDF pp. 2, 7, 10–11, 17, 21, 37, 51, 57–58, 66–70 of the strategic-report file read directly. SRC-028, *2026 AGM chief executive officer's speech* (Meg O'Neill, 23 Apr 2026), downloaded by Alexandre, read in full. The Palantir agreement (Sept 2024) could not be found on bp.com and was **not read**.
  - **Benchmark:** SRC-026, IEA, *Energy and AI* (10 Apr 2025), PDF pp. 113, 118–119, 128, 130, 232 read directly.
  - TotalEnergies: SRC-027, official release on the Mistral subsurface programme (15 Sep 2026), downloaded by Alexandre. Other TotalEnergies figures come from the [AI and organisation synthesis](2026-11-08_totalenergies_ai_data_organization.md) and the [strategy synthesis](2026-11-08_totalenergies_strategy_activities.md).

**Comparison rule** (from the research prompt): a partnership or announcement alone does not show that anyone leads or lags. Each row says whether the evidence is a **measured result**, a **vendor claim**, an **operational KPI** (a performance metric not attributed to AI), or an **announcement**.

## Verified facts

### 1. Side-by-side comparison

| Dimension | TotalEnergies | Shell | BP | Equinor |
| --- | --- | --- | --- | --- |
| **Published value from AI** | None published (CLM-029) | No $ value from Shell; the vendor claims the partnership is "delivering hundreds of millions of dollars in economic value", with no period and no Shell breakdown (SRC-022, C3 AI president). **Measured, company-published safety result:** T-Pulse AI CCTV monitoring: "Sites have achieved an average 70% reduction in the number of safety observations made by T-Pulse since the start of deployment" (SRC-021, PDF p. 113) | None found. Operational KPIs: upstream plant reliability 96.1% and refining availability 96.3% (record), the latter "driven by strengthened maintenance programmes, enhanced digital monitoring and improved outage recovery" (SRC-025, PDF pp. 11, 17); no AI share | **Measured, company-published:** "AI contributed to value creation and savings for Equinor and its partners amounting to USD 130 million in 2025"; "over 330 million USD" since 2020 (SRC-017). The annual report repeats "Approximate value created from AI: 130 million USD" (SRC-018, p. 23). Method not disclosed; includes partners |
| **Predictive maintenance at scale** | No scale figure published. Cognite platform being scaled across all operated upstream assets over 2025–2028 (announcement, SRC-008); 13,000 methane sensors (SRC-002, p. 29) | "more than 10,000 pieces of equipment" across upstream, manufacturing and integrated gas (2022, Shell executive in a vendor blog, SRC-023); "more than 13,000" (2026, vendor release, SRC-022) | Not found in the strategic report | "over 700 rotating machines with 24,000 sensors across all facilities"; "USD 120 million since 2020" (SRC-017) |
| **Models in production** | "more than 10,000 live AI models" (SRC-002, p. 42) | "over 10,000 production-grade ML models" (2022, SRC-023) | Not found | Not stated; "over a hundred new use cases have been identified" (SRC-017) |
| **Subsurface AI** | Mistral programme for subsurface frontier models, "more than €100 million" over 3 years, with a joint scientific laboratory (announced 15 Sep 2026, SRC-027); in-house Subsurface R&D line using AI (SRC-002, p. 42) | Agreement with SLB to "develop and deploy an open data and AI infrastructure" across subsurface, wells and production (announcement, SRC-024) | Seismic imaging "contributing to one of our best recorded years for exploration with 12 new discoveries"; well-trajectory tool plans routes "in days instead of weeks or months" (SRC-025, p. 11): no value figure | Seismic tool gives "a tenfold increase in interpretation capacity"; "2 million square kilometres were interpreted using the AI tool" in 2025 (SRC-017); "seismic data in hours instead of months" (SRC-018, p. 80) |
| **Generative AI for employees** | Copilot for Microsoft 365 since 2024; "first French company to widely implement Copilot" (SRC-012); training via the Digital Accelerator programme (SRC-002) | Not found in the sections read | Not found in the strategic report | "Our employees can use AI tools like copilots, chatbots and agentic AI" (SRC-017) |
| **Central digital / AI organisation** | OneTech Digital Line (since Sept 2025) + Digital Factory of ~500 experts in France and India; the CDO heads the Digital Line within the OneTech branch on the organisation chart (SRC-002, pp. 42, 50) | "Shell.ai, the overarching program for scaling AI at Shell" (2022, SRC-023); an **Executive Vice President Information and Digital Technology and Chief Information Officer** reports to the Audit and Risk Committee (SRC-021, PDF p. 215); no headcount found | No description found in the strategic report | **Technology, Digital & Innovation (TDI)** business area, 2,129 employees, led by an executive vice president (SRC-018, p. 23; SRC-017) |
| **R&D and digital spend** | R&D $810M (2025); "more than $1 billion in R&D, industrial innovation, digital developments" (SRC-002, p. 40) | R&D $1,170M (2025), combined with "digital solutions, often powered by AI" (SRC-021, PDF p. 72) | Not extracted | "Invested in R&D and digital in 2025: 730 million USD" (SRC-018, p. 23) |
| **Cost programme** | Cash savings (Capex + Opex) of $12.5bn over 2026–2030 (SRC-003) | Pre-tax structural cost reductions: $5–7bn cumulative by end-2028 vs 2022 (SRC-019); "$5.1 billion … since 2022" achieved, of which "$3.0 billion relates to operational efficiencies" and "$2.1 billion relates to portfolio changes" (SRC-021, pp. 10, 14) | Structural cost reductions: $2.8bn achieved in 2025 (SRC-025, p. 7); target raised to **$6.5–7.5bn by 2027** after the Gelsenkirchen and Castrol sales (SRC-028, p. 3; it was $5.5–6.5bn in the annual report) | Not extracted |
| **AI named as a cost lever?** | No AI contribution stated | Qualitative: "digital solutions, often powered by AI"; investing in "AI and quantum computing" to "make Shell a more efficient organisation" (SRC-021, p. 70). No dollar figure | Customers business: savings came from "procurement, supply chain efficiencies, organizational simplification and operating model changes" (SRC-025, p. 37); AI not quantified. The new CEO's first AGM speech (Apr 2026) does not mention AI or digital at all (SRC-028) | Not stated as a cost-programme lever in the pages read |
| **AI governance disclosed** | No fully autonomous decisions; final decisions by experts; traceability (SRC-012); Board review of AI (SRC-002) | Management and the Board "considered the emerging risks presented by … artificial intelligence and quantum computing" and the opportunities (SRC-021, PDF p. 127); the Audit and Risk Committee's 2026 priorities include "AI compliance" and "Finance systems and AI" (p. 170); risk factor cites the EU AI Act (p. 135). No standalone AI policy found | Risk factor: "Without clear organization-wide governance, bp may underperform, miss strategic upside, or fall behind on safe and compliant AI deployment"; internal requirements include "responsible AI" (SRC-025, pp. 66, 70) | "Equinor adopts a risk-based strategy towards AI, emphasising the safe and responsible application of technology" with "targeted upskilling programmes" (SRC-018, p. 80) |

### 2. Where TotalEnergies matches or leads (evidence-based only)

- **Models in production:** TotalEnergies reports "more than 10,000 live AI models" (FY2025). That is the same order of magnitude as Shell's "over 10,000 production-grade ML models" (2022). Definitions are not published by either company, so this is parity at best, not a lead.
- **Generative AI for employees:** TotalEnergies claims to be the first French company to deploy Copilot widely (2024). No comparable Shell or BP disclosure was found. That shows absence of evidence, not that peers lag.
- **Dedicated subsurface AI funding:** the Mistral programme ("more than €100 million" over 3 years, SRC-027) is the largest single AI commitment with a published amount among the four companies. Equinor already reports a measured subsurface output (2 million km² interpreted in 2025). An announced budget is not a result.

### 3. Where TotalEnergies is behind on evidence

- **Value measurement:** Equinor publishes an annual AI value figure (2025: $130M; 2020–2025: > $330M) in its annual report and press releases. Shell publishes a measured safety outcome for one AI tool (T-Pulse, −70% safety observations), but no $ value. TotalEnergies and BP publish neither. The gap is in published measurement. It does not show lower actual value.
- **Organisational weight:** Equinor's digital unit (TDI) is a business area of 2,129 people led by an EVP. TotalEnergies' Digital Line sits inside OneTech, under a CDO on the organisation chart (SRC-002, p. 50). This is a structural difference. Whether it matters is a question for step 10.

### 4. Sector benchmarks

| Metric | Value or range | Unit, year | Covered population | Method | Source | Comparability with TotalEnergies | Uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AI cost reduction, new deepwater oil project | "up to 10%" of costs of finding, developing and operating | %, scenario to 2035 | Illustrative new deepwater field (25 Mboe recoverable; ~$10/bbl development, ~$15/bbl operations) | IEA "Widespread Adoption Case": existing AI interventions scaled, barriers assumed overcome | SRC-026, PDF p. 118 | Relevant to TotalEnergies' deepwater projects (Brazil, US Gulf, Namibia); **new facilities only** | High: scenario, not observed |
| AI cost reduction, existing facilities | "It is unlikely that AI can reduce the costs of all oil and gas production": older facilities lack the infrastructure, and "retrofitting these facilities would carry additional costs" | Qualitative, 2025 | Global oil and gas | IEA expert assessment | SRC-026, PDF p. 118 | **Unfavourable benchmark**: limits savings claims on TotalEnergies' legacy assets | — |
| Predictive maintenance value | $120M cumulative over 2020–2025 | USD, 6 years | 700+ rotating machines, 24,000 sensors, all Equinor facilities; includes partners | Company-reported; method not disclosed | SRC-017 | Closest peer benchmark for an H1 maintenance case | High: undisclosed method, partner share included |
| Derived: predictive maintenance value per machine | ≈ $29,000 per machine per year | USD/machine/yr, 2020–2025 average | As above | **Calculation:** 120,000,000 / 6 years / 700 machines | From SRC-017 | Order-of-magnitude input only; assumes a constant fleet of 700 over 6 years, which overstates early years | Very high |
| Peer AI value relative to digital spend | $130M value vs $730M R&D and digital investment | USD, 2025 | Equinor group | Two company figures; not an ROI (the spend covers far more than AI) | SRC-018, p. 23 | Do not present as an AI ROI | High |
| Power plant O&M | "potential cost savings of up to USD 110 billion annually by 2035" | USD/yr, 2035 | Global power plants | IEA Widespread Adoption Case | SRC-026 (executive summary; chapter 5) | Relevant to Integrated Power | High: global scenario |
| Grid fault detection | "reducing outage durations by 30-50%" | %, 2025 | Grid operators | Case studies (basis not detailed) | SRC-026 (executive summary) | Indirect: TotalEnergies is not a grid operator | Medium |
| Grid operators using AI | 23% for real-time operations; 54% for grid development planning; nearly 70% for asset maintenance and operations planning | % of surveyed operators, 2024–2025 | Grid operators in 13 countries, incl. France | IEA survey | SRC-026, PDF p. 130 | Shows maintenance is the most mature use; not oil and gas | Medium |
| Expected benefits of AI | "Most energy companies surveyed by the IEA identified increased output and shorter project development cycles as the most significant outcome of AI" | Qualitative | Energy companies surveyed by the IEA | IEA survey | SRC-026, PDF p. 232 | Supports output and cycle-time KPIs over headcount KPIs | Medium |
| Barriers to adoption | Regulation, data access, interoperability, skills gaps, digital infrastructure, resistance to change; "persistent digital and physical security concerns, which often trump potential efficiency gains" | Qualitative | Energy sector | IEA analysis | SRC-026 (chapter 5; executive summary) | Matches TotalEnergies' own risk factors (SRC-002, pp. 136, 138) | — |

**No documented failed AI implementation in oil and gas was found.** The search returned only vendor success stories. The unfavourable benchmarks are the IEA's legacy-asset caveat above and the course's GenAI abandonment figures (Gartner: 30% predicted, 50% observed).

## Contradictions and unknowns

- **Shell's equipment count: 10,000 (2022) vs 13,000+ (2026).** These are growth over time, not a conflict. Both come through C3 AI channels; the 2022 figure is a Shell executive speaking, the 2026 figure is vendor text.
- **Equinor's $130M.** The headline says "saved"; the body says "value creation and savings" for "Equinor and its partners". Use "value creation and savings, including partners' share". No methodology is published (SRC-017).
- **Cost programmes are not comparable.** TotalEnergies counts cash savings (capex + opex); Shell counts pre-tax structural cost reductions against 2022; BP counts structural cost reductions on its own definition. No peer splits out AI.
- **Unknowns:**
  - bp's AI organisation, the Palantir agreement (not found on bp.com), and any bp GenAI deployment.
  - Shell's digital headcount and any standalone AI policy (not found by keyword search).
  - Equinor's measurement method.
  - Production sizes of the peers. Not extracted, so no per-barrel normalisation is attempted.
  - ExxonMobil and Chevron are out of scope for this step.
- **Conclusions the sources do not support:**
  - that TotalEnergies lags any peer in actual AI value, since no peer except Equinor measures it publicly;
  - that Shell's "hundreds of millions" is audited;
  - that any peer's cost programme is driven by AI.

## Assumptions or local observations (separate from facts)

| Statement | Type | Rationale | Test needed |
| --- | --- | --- | --- |
| Conditional implication 1: **if** TotalEnergies has no internal AI value register, then building one, so that it can publish an Equinor-style annual figure, is a credible H1 governance proposal | Assumption | Equinor shows the practice exists and is publishable; TotalEnergies publishes no such figure | Ask whether the Digital Factory tracks value per solution (open question Q03) |
| Conditional implication 2: **if** TotalEnergies' "10,000 live AI models" are comparable to Shell's production models, the gap is **scaling value, not building models**: the H1 focus should be adoption and value capture, not more pilots | Assumption | Parity on model counts, absence of value evidence | Model definitions; per-solution deployment data (Q02) |
| Conditional implication 3: **if** our case claims AI savings, it must be built bottom-up (for example, maintenance value per machine), because no peer attributes cost-programme savings to AI | Assumption | Shell, BP and TotalEnergies programmes are not split by lever | Step 18 must cite use-case benchmarks, never peer cost programmes |

## References to enter in `sources/register.md`

- [x] Links open the original documents. SRC-022 to SRC-024 are vendor or trade-press texts.
- [x] Pages and dates have been checked for SRC-017 to SRC-021 and SRC-025 to SRC-028.
