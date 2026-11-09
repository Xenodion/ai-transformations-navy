# Pre-report review: course compliance and consistency (steps 01–20)

- **Reviewed:** 9 November 2026 by Alexandre Waerniers, with Claude Code, on `dev_alex` at `e40f435` (identical to `dev_vincent` at `2e1882d`).
- **Purpose:** before step 21 (full report), check that the work covers everything the course expects, follows AGENTS.md, and is internally consistent.
- **Course references used:**
  - [course/guidelines.md](../../course/guidelines.md) and [Vincent's notes](../../course/notes/vincent.md);
  - the course deck (SRC-033): p. 6 (evaluation), p. 48 (oral project), pp. 81–93 (portfolio rules), pp. 147–150 (investment-case checklist and board questions), pp. 155–156 (change plan), pp. 200–206 (board pack and Comex memo);
  - the four session cheat sheets in [course/exam/](../../course/exam/).

## 1. Verdict

The work covers almost every course topic, and the research base, the operating model, the canvas structure and the change plan are strong. Three problems remain, and the third is the one that matters most for the oral:

1. **The headline economics would not survive a sceptical CEO:** IRR 702%, payback under 1.2 years, NPV +$619M on $38.8M.
   - They come from summing first-pass value midpoints across 14 overlapping projects, including soft, unmonetised and H3 values.
   - They are set against a cost base that covers only the delivery squads.
   - They also contradict the course's J-curve.
2. **Several course items are missing:** the envelope split by the six cost categories, business-unit co-funding by year, "why not half the envelope", ADKAR, and a costed training plan.
3. **Some rules from AGENTS.md and the course are broken:**
   - H3 projects are valued with NPV, IRR and payback;
   - the bottleneck is generalised from Argedis;
   - the hurdle inputs have no source;
   - the cost of inaction double-counts.

Fixing these before step 21 is cheaper than fixing them in the report, the memo and the slides (AGENTS.md rule 8).

## 2. Course expectations checklist

✅ covered · ⚠️ partly covered or flawed · ❌ missing

| # | Course expectation | Course source | Where in our work | Status | Action |
| --- | --- | --- | --- | --- | --- |
| 1 | Readiness: 5 pillars, 5 stages, name the bottleneck pillar | Deck p. 48; session 1 | [readiness_bottleneck.md](../options/readiness_bottleneck.md) | ⚠️ | Pillars and stage are fine. The bottleneck conclusion generalises from Argedis (issue C6) |
| 2 | Operating model: CoE / hub-and-spoke / federated, 3 matching factors, decision tree, evolution path | Session 2 | [operating_model.md](../options/operating_model.md) | ✅ | Remove the contradiction with steps 09 and 11 on decision rights (C6) |
| 3 | Portfolio one-pager: canvas with horizon, capital % summing to 100%, thin-slice dependency, build/buy/partner, first milestone, owner and date | Guidelines; deck p. 89 | [portfolio_sequencing_canvas.md](../projects/portfolio_sequencing_canvas.md) §2 | ✅ | Columns complete and sum to 100% |
| 4 | Move away from 70-20-10 only with a written trigger and reason; example splits are "illustrative, not benchmarks"; "regulated or mission-critical → heavier H1" | Deck pp. 81–82 | Canvas §3 | ⚠️ | 50/30/20 is presented as a "Multi-Energy Target Benchmark" with no trigger (C7) |
| 5 | Each foundation funded with a use case; dependencies name a slice | Deck pp. 89, 92 | Canvas §5; E01 | ⚠️ | E01 is a separate 4.2% line. Either attach it to the four featured cases, as step 11 says, or justify it |
| 6 | Horizon-specific KPIs; "H3 earns learning metrics first" | Deck p. 92 | Cases, step 18 | ❌ | P11 and P12 carry NPV, IRR and payback (C2) |
| 7 | 3-year envelope by the 6 cost categories (compute, talent, integration, model ops, data, governance) | Deck pp. 148, 150 | Per case only | ❌ | Add a portfolio table by category |
| 8 | Three scenarios with explicit assumptions and probabilities; ENPV | Deck p. 148 | Step 18 §6 | ⚠️ | The downside is not a worst case (C4) |
| 9 | IRR versus hurdle = WACC + premium; always show NPV | Deck p. 150 | Step 18 §4 | ⚠️ | WACC inputs unsourced; two premiums outside +2 to +6 (C3) |
| 10 | Cost of inaction: a negative term in the EV, "explicit and defensible" | Deck p. 150 | [cost_of_inaction.md](../finance/cost_of_inaction.md) | ⚠️ | Double counting and unsupported competitor gap (C5) |
| 11 | Board Q1: worst case, its probability, what we do | Deck pp. 149, 204 | Step 18 §6 | ⚠️ | Downside NPV is +$355M; no portfolio loss cap (C4) |
| 12 | Board Q2: kill criteria at each tranche gate (metric, threshold, date, owner) | Deck pp. 149, 204 | [gates_and_adoption.md](../governance/gates_and_adoption.md) §6 | ✅ | Green / amber / red matrix per gate |
| 13 | Board Q3: what the competitor does if we don't | Deck p. 149 | S06, step 19 | ⚠️ | S06 is sound; step 19 overstates the gap (C5) |
| 14 | Board Q4: "Why this envelope and not half?" | Deck p. 149 | — | ❌ | Show what half would cut: horizons, timing, value |
| 15 | Board Q5: J-curve trough, then break-even year | Deck pp. 149, 150 | Step 18 says "self-financing in Y1" | ❌ | Show a credible trough (C1) |
| 16 | Board Q6: business-unit co-funding share by year | Deck p. 149; session 3 (100/60/40) | Principle only, step 10 §5 | ❌ | Add the co-funding schedule to the economics |
| 17 | Stage-gated tranches released on evidence; quick wins | Deck p. 150 | Step 20 §6; canvas §7 | ✅ | — |
| 18 | Milestones M12 / M24 / M36, each with owner, date, baseline, metric, gate | Deck p. 202 | Step 20 §6.3; cases | ✅ | Check the memo reuses them |
| 19 | Change plan (3 pages): 4 failure modes with mitigation, 4 stakeholder classes and cadence, 3 training tiers, kill criteria | Deck p. 155 | Step 20 | ✅ | It is 390 lines; condense to 3 pages for the report appendix |
| 20 | 10-20-70: "budget the 70%" (training, process redesign, communication) | Deck p. 156 | Step 20 §1 | ⚠️ | The three training tiers (101,513 + 1,200 + 250 people) are not costed in the envelope |
| 21 | ADKAR | Session 4 | — | ❌ | Add it, for example to diagnose the Translators' adoption stage |
| 22 | EU AI Act: inventory, classify use cases, "verify the current official timeline" | Deck p. 201 | E01; CLM-058, CLM-072 | ⚠️ | Read the amending regulation (Q16); classify each featured case |
| 23 | Competitor comparison ready for challenge | Guidelines | S06 | ✅ | Use S06's measured-versus-announced distinction in the report |
| 24 | CAPEX/OPEX split immediately clear; cash flows by year | Vincent's notes | Step 18 | ✅ | — |
| 25 | Bubble chart plus investment-mix and return-mix bars | Vincent's notes | Canvas §4, charts | ✅ | The return mix inherits issue C1 |
| 26 | 2-page Comex memo: thesis → portfolio → envelope → scenarios → hurdle → risks → ask; board-ready checklist | Deck pp. 150, 206 | Step 22 | Not started | — |
| 27 | Board pack: lead with the answer, assertion headlines, one message per slide, details in the appendix, honest uncertainty, traceable numbers | Deck p. 203 | Steps 24–25 | Not started | — |

## 3. Critical issues

### C1. The headline economics are not credible to a CEO

- **The claim** ([portfolio_economics.md](../finance/portfolio_economics.md) lines 38–44): $314M/yr run-rate, NPV +$619M, IRR 702.4%, payback under 1.2 years, "self-financing in Y1". Single projects show IRRs of 1,236% to 2,874% (table, lines 162–178).
- **Why a CEO would challenge it:**
  - the course examples clear hurdles with IRRs of about 17–25%;
  - the course teaches a J-curve, with costs first, a trough, then break-even.
- **Cause 1: value.** The steady values are the **midpoints of the first-pass ranges** in the step 08 long list, summed for all 14 projects. The long list said "first-pass order of magnitude, not a business case" and "do not add these rows up" because of overlaps. Of the $314M/yr, about $170M is not usable as cash:

  | Project | $M/yr in step 18 | Problem | Source of the problem |
  | --- | --- | --- | --- |
  | P11 VPP (H3) | 60 | Option value counted as cash | Rule 7; course p. 92 |
  | P12 e-SAF (H3) | 50 | Option value counted as cash; "0.5–1.0 Mt/y SAF mandate" is in fact TotalEnergies' own capacity target (CLM-060) | Rule 7 |
  | P07 Safety vision | 20 | No formula; the long list kept it as a safety KPI, not monetised | [reserve_cards.md](../projects/reserve_cards.md) line 138 |
  | P05 Copilot | 19.5 | Only $1–3M is hard cash; the rest is time saved. The card quotes the course warning itself, and step 11 rejects the same argument | Reserve cards line 98; thesis §2 |
  | P06 Procurement | 15 (35 in the reserve card) | Illustrative only, no spend baseline (Q17); two different values | Reserve cards line 118 |
  | E01 Value register | 5.5 | The long list claimed no standalone value | Long list E01 |

- **Cause 2: cost** (my part). The step 08 bottom-up costs cover only the delivery squads, at internal French rates, plus a few vendor lines. Missing:
  - the three-tier training in step 20;
  - change-management time beyond the squads;
  - vendor professional services;
  - enterprise-wide licences.

  So the cost side is thin while the value side is full.
- **Fix:**
  - The base case keeps only hard, formula-backed levers, with overlaps removed (P01/P10, P02/P03, P04 with existing trading tools, P03/P06 with the $12.5bn plan).
  - Time savings are shown separately, never in NPV.
  - H3 projects are taken out of NPV (C2).
  - The training and change costs of step 20 are added, or stated as absorbed by the existing training budget (about €210M a year, S04).
  - Show the J-curve.
  - Regenerate the Excel model with Vincent's script.

### C2. H3 projects are valued like cash projects

- **The claim:** P11 has NPV +$48.1M, IRR 204%, payback month 28 ([case_p11_virtual_power_plant.md](../projects/case_p11_virtual_power_plant.md) lines 174–190). P12 has NPV +$51.1M and IRR 204% (step 18 table).
- **Internal contradiction:** step 11 says P11's $98M is "option potential … not banked" ([thesis_and_selection.md](../options/thesis_and_selection.md) line 51), but step 18 banks it in the Tier 1 subtotal and the consolidated NPV.
- **Rules:**
  - AGENTS.md rule 7: do not fabricate a payback for an H3 option.
  - Roadmap quality rule: use learning milestones and option value.
  - Course p. 92 debrief: "H3 earns learning metrics first" and "same KPI for every horizon" is a common mistake.
- **Fix:** present P11 and P12 with learning gates (MW enrolled, revenue per MW, opt-out rate; candidates screened, lab hits), a capped cost, and option value described qualitatively or with an explicitly labelled illustration outside the portfolio NPV.

### C3. The hurdle rate has no source

- **Missing WACC inputs.** WACC 7.5% is computed from Rf 3.0%, beta 0.90 and MRP 5.5%, labelled `[Fact]` and cited to CLM-003, which only contains ROACE and gearing (step 18 line 130). None of the inputs is registered.
- **Premiums outside the course range.** The course's hurdle is WACC + 2 to 6 points (session 3; deck p. 150 example: 8.5% + 3.5% = 12%). Two premiums fall outside it: Integrated Power +1.5 (line 135) and H3 +7.5 (line 138). Our step 07 audit discarded the legacy draft's +6.8 for the same reason.
- **Fix:** register a WACC source, or label the WACC an assumption with its inputs; keep every premium between +2 and +6; leave H3 out of hurdle testing (C2).

### C4. The downside is not a worst case

- **The claim:** the downside is 60% value capture with probability 25%, giving NPV +$355M (step 18 line 189; table line 311).
- **The course rule:** lead with the worst case and quantify the downside, its probability and the response (deck pp. 149, 204). The course's own example has a negative downside NPV with probability 50% (session 3).
- **Fix:** a downside with delayed adoption, a much lower capture rate and wave 2 killed at gate 2, giving a negative or near-zero NPV, the loss cap (tranche 1 = $16.09M) and the action. The legacy audit flagged the same problem ("sandbagged downside").

### C5. The cost of inaction double-counts and overstates the competitor gap

[cost_of_inaction.md](../finance/cost_of_inaction.md):
- **1b imbalance penalties** (line 106):
  - assumes there is no algorithmic balancing, but Predictive Layer and Quadra already run in house (CLM-027);
  - the same penalties are claimed as benefits by P04 and P11, so "program ENPV + avoided inaction" counts them twice.
  - The step 07 audit flagged exactly this in the legacy draft.
- **1a refining** (line 94):
  - calls AspenTech/Inmation a "fragmented legacy setup", though it is the new platform being rolled out (CLM-018);
  - the "peer pressure" rests on a vendor claim (Shell/C3) and on BP's availability KPI, which S06 found is not attributed to AI.
- **1c rig-days** (line 118):
  - overlaps P03's rig-time savings;
  - quotes "Equinor $130M in verified savings" and "IEA up to 10% [Fact]", but S06 records the first as having no published method and including partners, and the second as a scenario for new deepwater projects only.
- **Driver 3:** applies AI Act high-risk conformity to all "10,000 uninventoried live models" (line 21). Annex III covers only safety components in gas or electricity supply (CLM-058), from 2 Dec 2027 (CLM-072, pending).
- **Rule 4:** S06 concluded that no evidence shows TotalEnergies lags any peer in AI value.
- **Fix:**
  - build inaction from TotalEnergies' own baseline (savings plan at risk, the Board's 2026 AI review, AI literacy duty already in force, talent);
  - remove overlaps with P03, P04 and P11;
  - label the competitor driver an assumption with a range.
- **Also:** step 19 quotes the step 18 ENPV as +$657.67M (line 28), but step 18 says +$602.70M (line 44). Step 19 also gives two incremental IRRs, 845.9% (lines 30, 57) and 766.8% (line 205).

### C6. The bottleneck is generalised from Argedis

- **Group claims from one subsidiary:**
  - [readiness_bottleneck.md](../options/readiness_bottleneck.md) line 52: "In TotalEnergies, decision rights and capital allocation are already firmly held by the branches".
  - Thesis line 29: "its branches already hold decision rights and allocate capital effectively".
  - The only evidence is CLM-074, one retail entity.
- **Contradiction:** [operating_model.md](../options/operating_model.md) line 22 still lists funding and decision rights as unknown (CLM-030, Q01).
- **Rules:** AGENTS.md rule 4 and #9's acceptance criterion ("without generalizing from Argedis").
- **Fix:** keep the Delivery Trios as the remedy, but present execution throughput as a hypothesis. Support it with group-level evidence: the ~100 solutions are "progressively being deployed" (CLM-017), no deployment rate is published (Q02), and Copilot value is unmeasured. Argedis is the illustration. Q01 and Q02 stay the tests.

### C7. The horizon mix drifted from the course rule

- **Mislabelled benchmark:** canvas §3 (line 75 onwards) calls 50/30/20 a "Multi-Energy Target Benchmark" from Nagji & Tuff. The course slide (deck p. 82) says example splits are "illustrative, not benchmarks", and lists "regulated or mission-critical → heavier H1" (80-15-5).
- **Relabelled projects:** P04 and P08 are H1 in the reserve cards (lines 68, 151) but H2 in the canvas and step 18. The long list classed both H1 on the course's four questions.
- **Fix:** either return to 70-20-10, or write the trigger and the reason for the deviation, as the course requires. Restore the course-question horizons for P04 and P08, or justify the change in each card.

## 4. Consistency and housekeeping

| Item | Location | Fix |
| --- | --- | --- |
| Lost dollar amounts (".20M", ".35M", ".79M", ".99M", "+.46M", "Total Capital ()") | Canvas lines 58, 62, 78–91; step 18 line 311 | Regenerate: the `$` signs were stripped during file generation |
| P06 value $35M/yr (reserve card) vs $15M/yr (step 18) | Reserve cards line 118; step 18 table | Align, once Q17 is answered |
| ENPV +$657.67M vs +$602.70M; incremental IRR 845.9% vs 766.8% | Steps 19 and 18 | Align after the C1 rebuild |
| Q11 cites CLM-072; the Argedis entry is CLM-074 | [open_questions.md](open_questions.md) line 19 | Change the ID |
| Argedis "~800 stations" vs 150–200 COCO stations | Readiness line 65 vs CLM-074 and P13 case | Use CLM-074; check with the Factbook (SRC-034) |
| CLM-074 marked "Verified" although it is attested by the observer only | Register | Mark it Pending (attested), as the closing audit recommended |
| Chart links use `file:///C:/Users/Vincent/...` | Canvas lines 116–126 | Use relative `assets/...` paths |
| Step 11's one-line summary says P03 saves "2–4% on $9.26bn E&P capex" | Thesis table | The case itself is scoped to 10 rigs; reword the summary |
| Course slide cited as "Session 2 Slide 98" | Canvas line 75 | The slide is session 2 deck p. 36, combined deck p. 82 |
| Nagji & Tuff (HBR 2012) not in the register | Canvas, step 18 | Cite it through the course deck (SRC-033, p. 81) or register it |

**GitHub issues versus the roadmap** (checked through the GitHub API on 9 Nov; AGENTS.md rule 6):
- #9 and #10 are **open**, with empty checklists and no output comment, while their roadmap boxes are ticked.
- #11–#17 are closed but unassigned, still labelled `needs-owner`, with unticked checklists, while the roadmap names owners.
- #20 is closed with its checklist unticked.
- #21–#27 are open, unassigned and not started; `deliverables/` contains only a README.

## 5. What is solid and should be kept

- **Research base:** S04–S06, the step 07 audit and the register (34 sources, 74 claims, consistent IDs).
- **Readiness:** the pillar scores and the stage placement (late Implementing).
- **Operating model:** the comparison, decision rights, funding phasing and evolution gates, with the Delivery Trios as a concrete remedy.
- **Case studies:** P01 and P03 are well scoped (P03: 10 rigs × spread rate). P13 is a credible quick win once its baseline is checked against the Factbook.
- **Canvas:** the structure, dependency graph, sourcing split and tranche logic.
- **Step 20:** the failure modes, stakeholder classes, inverted cadence, three tiers, telemetry and the green / amber / red kill matrix.
- **Cost rates:** sourced (Apec, INSEE, ECB) and used consistently.

## 6. Recommended order of work before step 21

Submission is due on the evening of 10 November; structure freezes at that point (rule 8).

1. **Team decision on the financial base case** (C1, C2, C4): hard value only, H3 as options, a real downside, training costed. Then regenerate the model and charts.
2. **Hurdle** (C3): WACC with a source or labelled as an assumption; premiums between +2 and +6.
3. **Cost of inaction** (C5): remove overlaps; base it on our own baseline.
4. **Wording of the bottleneck** (C6) and of the horizon mix (C7).
5. **Missing course items** (§2): six cost categories, co-funding by year, "why not half", J-curve, ADKAR. Add them in the report.
6. **Housekeeping** (§4) and the GitHub sync.
7. **Then step 21:** write the report in the course order (readiness → operating model → portfolio → financials → change), with the memo structure from deck p. 206 in mind.

## 7. Open questions that still affect the deliverables

Q01 (funding and decision rights), Q02 (deployment rate), Q03 (internal value tracking), Q05 (model inventory), Q06 and Q17 (savings-plan levers, procurement spend), Q16 (AI Act amendment), Q18–Q21 (baselines for P02, P03, P04, P08, P09).
