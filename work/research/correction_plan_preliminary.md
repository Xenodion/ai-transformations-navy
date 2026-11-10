# Correction plan: strategy, financial model and portfolio visuals

> **Historical audit:** The old workbook, generated charts and redundant reviews discussed below were removed from active use on 10 November; their tracked versions remain in Git history. Current cases and checks are indexed in [work README](../README.md). This file records the audit findings, not current scenario values.

Status: preliminary review, 9 November 2026. This plan is not a sign-off: the workbook has not been independently recalculated and every file and underlying source has not yet been checked. Do not derive the memo or slides from the current figures.

## Confirmed blockers

1. `finance/portfolio_economics.md` reports $913.01m cumulative cash and $619.19m NPV in its headline, but $796.51m and $523.58m in its annual waterfall. Rebuild from one set of cash flows; reconcile every table and chart.
2. The waterfall spends $5.95m at year 0 across all projects, including the reserve pool, whereas `projects/portfolio_sequencing_canvas.md` makes later projects conditional on month 12 or 24 gates. Define the actual dated approvals, spending and benefits and model a gate-failure branch.
3. The same finance document says H3 has no fabricated short-term payback, then reports P11 payback and H3 value as if established. The course's Three Horizons characteristics slide says H3 should use learning, milestones and options, and not H1 ROI. Keep exploratory expenditure in the portfolio; exclude unsupported H3 commercial proceeds from the base case, or present clearly specified conditional scenarios separately.
4. The workbook's `Strategic_Reconciliations` contains a hard-coded $330m H3 mature annual value and 70% target. The chart generator claims to validate the 10/20/70 inversion. The course describes the split as approximate; it is not evidence for this portfolio. Remove unsupported target-driven conclusions and trace all chart data to the approved model.
5. The workbook includes hard-coded payback text and static mature values. Recalculate payback from dated flows with an explicit interpolation convention; reconcile every static output and remove hard-coded economic outputs from the calculation chain.
6. The inaction bridge subtracts a negative status quo from the program flows. Establish whether program benefits already represent improvement versus the same baseline before adding avoided deterioration: otherwise double counting is possible. Demonstrate the bridge driver by driver.
7. P01's case states $15m annual benefit, 25% in year 1 and a month 9 payback, although its annual flows start with -$0.25m then +$2.55m. Linear interpolation on those annual flows produces approximately month 1.2; actual timing cannot be inferred from annual totals. Build a monthly pilot schedule and make the evidence gate and cash timing consistent.
8. P03's year 2 saving is allocated to two rigs while its scale formula uses ten rigs; validate the implied asset base, operated interest, day-rate savings, ramp and contractor incentives. Its month 14 interpolation and month 22 operational payback are distinct assumptions and require dated evidence and a single primary convention.
9. The project's diagnostic is based on public disclosure and a local Argedis observation. The preferred constraint must remain a testable hypothesis, not established group-wide ground truth; compare competing constraints and identify disconfirming evidence.

## Ordered correction and acceptance gates

1. **Evidence and course:** map the course's readiness, operating-model, horizons, financial and change requirements to outputs and exact slide pages. Verify each material company and benchmark claim against original source, scope and date. Treat older audits as leads and recheck current versions.
2. **Decision and cases:** revisit the bottleneck and selection against existing capabilities, alternatives and rejected options. For each case define a bounded site/asset population, counterfactual, baseline, economic owner, adoption, incremental intervention, attributable benefit and non-AI alternative. Specifically test P11's novelty against existing TotalEnergies flexibility activities and P13's controlled station perimeter.
3. **Build a dated model:** make one assumptions register and project-level annual or monthly schedules; show all cash outflows including deployment, run, change and internal time, CAPEX/OPEX, ownership share, tax treatment and units. Separate committed projects from optional projects, and make gates affect both costs and revenues. Derive portfolio metrics from schedules, use project-specific rates for project NPVs, and justify any portfolio-wide rate; a capital-weighted average hurdle is not automatically equivalent to a sum of risk-adjusted NPVs.
4. **Challenge economics:** independently recompute NPV, IRR and payback from flows, including timing. Model a genuinely adverse scenario with delay, lower adoption and cost overruns; make probabilities assumptions. Test baseline overlap, incremental cash rather than accounting savings, avoided costs versus released capacity, existing investment plans, and inaction. Do not extrapolate unsupported benefits to all sites or customers.
5. **Governance:** align every gate, owner, decision, threshold, deadline, cost at risk and release with the case and model. Budget training, workforce time, integration, security and consultation; label legal assertions for specialist verification. Check that prerequisites can precede the gate that depends on them.
6. **Visuals and report:** generate charts from reconciled data, label units, scope and uncertainty, size bubbles by area, and place unvalued H3 options outside the payback axis. Avoid presenting hypotheses as facts. Build and challenge the full report before the executive memo and slides.
7. **Tracking and final validation:** reconcile each affected roadmap step with its GitHub issue, including closure status, and verify acceptance criteria before treating it as complete. Run independent formula, sensitivity, scope and source checks, then reconcile report, memo and slides.

## Verification limitation

`audit_workbook.py` now runs with the bundled Python and openpyxl without numpy-financial. Its existing checks assert selected formula strings and recompute an IRR on hard-coded example flows; they do not recalculate the workbook or establish economic validity. A real spreadsheet engine and independent numerical checks remain required.

## Independent review update: workbook arithmetic and file-specific findings

The independent script `work/finance/independent_cash_check.py` reads the numeric inputs of all 14 project schedules directly from the workbook. It does not evaluate Excel formulas or validate the inputs. Results ($m unless stated):

| Check | Independent result | Conflicting published figure / implication |
| --- | ---: | --- |
| Y0–Y5 benefits | 0; 5.13; 72.65; 184.02; 271.50; 314.00 | Agrees with the waterfall, not its headline |
| Y0–Y5 costs | 5.95; 9.54; 12.82; 10.48; 6.00; 6.00 | Total 50.79; 38.79 covers Y0–Y3 only |
| Net cash | -5.95; -4.41; 59.83; 173.54; 265.50; 308.00 | Cumulative 796.51, not 913.01 |
| Weighted assumed rate | 10.9812% | A modeling convention, not a proven corporate hurdle |
| NPV at that rate | 523.56 | Headline 619.19; waterfall 523.58 differs slightly |
| Sum of project NPVs at project rates | 515.25 | Canvas 513.81; finance narrative 612.32 |
| Annual-flow portfolio IRR | 315.80% | Finance headline 702.4%; chart displays 315.8% |

The scope is all 14 projects including reserve and unproven H3 revenues, so these are arithmetic checks, not defensible investment returns. Excel COM failed to start in this session (Windows logon-session error); the actual Excel calculation engine and every workbook formula have not been independently verified.

### Diagnosis and decision (`options/`)

- `readiness_bottleneck.md` states non-disclosure does not prove absence, but then asserts company-wide delivery bottlenecks and says the group lacks an audited value register. Evidence is insufficient for those assertions. The URD (PDF page 43) supports roughly 500 experts, almost 100 solutions and more than 10,000 live AI models, not group-wide delivery cycle times or lack of business ownership. Preserve the Argedis observation as local and use 90-day evidence gates to test the competing constraints.
- `operating_model.md` appropriately compares alternatives and documents the current Digital Line, but assumes decision rights, funding and maturity that its own unknowns do not resolve. Design a conditional hub-and-spoke proposal with business-owner accountability, differentiated spokes and explicit opportunity cost for scarce staff.
- `thesis_and_selection.md` labels the bottleneck ground truth and dismisses decision rights/talent constraints without group evidence. The retail matrix still claims $18m/year and 4–8 month cash although the case is $2.5m/year and much later payback; its CEO defense cites a $14.14m budget and $100k/year backfill while the latest model says $16.09m and $50k. Re-select or retain cases against transparent criteria after scope and economics are repaired.

### Project documents (`projects/`)

- `long_list.md`: P03 is still H1 and $46–185m while the selected case uses H2 and $35m; P10's $3–15m relates to yield, while the chart relabels it H2 as circular feed. Validate the value mechanism and classify the same slice everywhere.
- P01: a global $7.1/b refining margin marker is applied to assumed recovered throughput; incremental contribution margin and the sites' eligible throughput are unverified. The 520-machine Equinor cross-check is selected to fit the target and does not prove comparable asset economics; document the peer's scope and avoid claiming validation. The two month-9 stop rules are different. Its 9-month payback is not calculable from annual cash flows without a monthly schedule.
- P03: scope has improved compared with the legacy audit, but 10 operated rigs and $1.6425bn addressable spend, savings ownership, attribution and the speed of measured savings still need evidence. Annual interpolation versus month-22 campaign accounting needs one dated model; contractor incentives and baseline drilling programs matter.
- P11: the year-3 schedule says $6m across 100 MW, implying $60k/MW/year, whereas its gate says 500 MW at $12k/MW/year or the full-scale assumption is $20k/MW/year. Resolve capacity, dates, contract margin, enrollment, cost and shared infrastructure. Its classification as a new business model remains contestable given existing company flexibility activities. TSO qualification, cloud APIs and zero hardware costs at scale are assumptions until substantiated.
- P13: the pilot and scale sections define 100 to 250 eligible sites while the implementation and cost plan refer to 800 and 1,500. Gates demand $5m and $12m per year while modeled mature benefit is $2.5m. The listed $0.61m + $0.85m + $0.80m totals $2.26m, not $2.50m; using 250 stores for the first lever gives roughly $0.85m, but mixes perimeters. Avoid counting recovered markdowns and spoilage savings twice, verify stock ownership and test against a seasonal control group.
- `reserve_cards.md`: P05 explicitly labels most of $19.5m as redeployed time, yet the workbook counts the full amount as cash. P06 is described as requiring unresolved Q17, yet the card also says Q17 is closed. P07 models avoided incident risk as certain annual cash; separate expected loss from cash. Confirm P02/P04 operated shares, P08 customer margin and P09 controlled voyages; exclude unsourced cash flows until a scope-matched case exists. The remaining candidates and E01 need the same incremental-benefit and overlap audit.
- `portfolio_sequencing_canvas.md` mixes commitments, annual outflows, benefits and gate decisions; reconcile one schedule with the workbook. Gate dependencies must be causal rather than artificial, and H3 cash must remain conditional.

### Finance and governance (`finance/`, `governance/`)

- `build_financial_model.py`: all reserve project cash inputs begin in Y0 despite later conditional approvals; P05 includes soft savings, P11/P12 include commercial cash despite option language, and cost of capital and tax inputs are not a complete WACC derivation or tax cash schedule. Y0–Y3 is four dated columns, so explicitly define the three-year spending convention and fiscal years.
- `cost_of_inaction.md`: the five drivers are assumptions, not proof of loss or value avoided by this particular program. Baseline activities continue without the proposed program; show what each proposed intervention actually prevents and when. Current 2025 Y0 / 2026 Y1 dates are inconsistent with a November 2026 decision. The hard-coded annual losses sum to $276.02m and discount to approximately $184.08m at the model's exact rate, but this arithmetic does not validate the causal bridge. The text claims 10,000 models lack documentation, although Q05 says the inventory is unknown.
- `gates_and_adoption.md`: reconcile thresholds, dates, accountable owners and workforce/training budget with cases and the financial schedule. Do not describe risk thresholds or legal classifications as established company facts. Confirm statutory dates and applicability with primary legal sources before finalizing.
- `audit_workbook.py`: selected formula string checks and an IRR of a hard-coded example are useful smoke checks only; they cannot certify all formulas or inputs. `independent_cash_check.py` adds reproducible arithmetic from workbook input cells, but not Excel recalculation or sensitivity tests.

### Charts, notebook and assets

- `generate_simple_charts.py` reads the long list but uses hard-coded overrides, NPVs and copied arrays, then labels the workbook as the source. It cannot reliably update when the workbook changes. The bubble's horizontal axis is time to *first value*, whereas the roadmap asks for payback; those are different measures. It also treats 12/24-month lines as horizon boundaries, although course PDF pp. 77–78 uses customer, business model, proven technology and time as a combined test.
- Visual inspection of all four PNGs shows the bubble chart's legend/table text overlaps and source is clipped. It calls values audited; H3 is given plotted commercial outcomes. The mix chart claims it validates the 10/20/70 return inversion using $330m of hard-coded H3 mature value. The J-curve labels multiple project endpoints inconsistently and uses the unvalidated full portfolio; the branch chart has categories requiring reconciliation. Regenerate the notebook and all PNG/SVG outputs from one verified dataset after decisions are made.

### Research, source integrity and tracking

- `source_verification_and_peer_audit.md` treats no URD search result as proof no activity exists; that is invalid. It repeats a stale $18m P13 value. Its assurance language and the older `agent_review_*.md` findings are not independent proof; recheck each point against current files.
- `open_questions.md` Q11 still identifies Argedis as CLM-072, but the register uses CLM-074 for the observation and CLM-072 for the AI Act timeline. Q17 is open despite the reserve table claiming closure. Correct IDs and open status after verifying evidence.
- `roadmap.md` marks steps 09–20 complete despite the identified acceptance failures, and its owner table conflicts with its final issue-tracking paragraph. Review issue state and outputs before changing either side; synchronize both as required by the project rules.
- `legacy_plan_unverified.md` is historical and must not be evidence. Existing agent reviews and the previous strategy audit are historical leads, not present-day sign-off. `work/README.md` is navigational. The final report, memo and slides are not yet ready.

### Course alignment (PDF page numbers)

- pp. 21, 190–191: readiness, bottleneck, operating model, portfolio, investment and adoption connect to the board decision and two-page memo.
- pp. 77–78: horizon-specific KPIs; four placement questions; not every long-dated project is H3.
- pp. 96, 104, 107: three-year costs, five-year scenarios, IRR and hurdle; NPV supports investment decisions; WACC requires equity and debt weights/costs and tax, and a risk premium must be explicit.
- pp. 124–132: scenario probabilities, cash-flow timing and cost of inaction, with the teaching case's numbers illustrative rather than company evidence.
- pp. 182–184, 197–200: adoption, skills, social dialogue, ownership and measurable gates.

### Remaining limits before sign-off

This is a substantive cross-document review, not a line-by-line verification of every historical review or every claim against original sources. Primary-source checks, independent recalculation in Excel, dated project scenarios, issue synchronization, and final report-quality checks remain open. The presence of a cited source does not establish that it supports the calculation or causal inference.

## Verified source updates, 9 November

- TotalEnergies' 2025 URD pp. 462 and 472 gives a 7% post-tax WACC estimate for specified impairment tests (CLM-075). It does not establish an internal AI hurdle. The earlier single-hurdle proposal is superseded by `work/finance/discount_rate_policy.md`; do not use pre-tax cash flows to claim an after-tax NPV.
- Quadra Energy already had a 9 GW renewable-generation VPP in the 2023 acquisition announcement (SRC-036, CLM-076). Existing customer-side EV/battery capability is not established either way; P11's novelty and horizon require a fresh comparison.
- The original Equinor source (SRC-017) says predictive maintenance generated $120m since 2020, with more than 700 machines monitored. A $20m/year figure is an assumed six-year average, not an annual figure disclosed by Equinor. The per-machine extrapolation assumes a constant fleet and compatible value; it is not an independent validation of P01.
- Regulation (EU) 2026/1744 Article 1(40), p. 35 (SRC-035), confirms specified Annex III and Annex I dates; classify individual systems and check transitions. Q11 and Q16 references are corrected in the question log.
- The 26 May 2025 TotalEnergies Mero-4 release (SRC-037, CLM-077) states that Petrobras operates Mero and lists TotalEnergies' interest as 19.3%. P03 and the selection thesis incorrectly describe Mero among TotalEnergies-operated rigs. Reassess pilot decision rights, operator and partner consent, contract data rights and the group's actual net cash entitlement; ownership percentage alone is not a substitute for contract economics.
