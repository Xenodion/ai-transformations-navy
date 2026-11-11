# Full report V3 — task plan

**Status:** done and validated by Vincent, 11 November 2026. V3 is now `deliverables/report/full_strategy_report.md`.
**Goal:** one complete, internally consistent report (V3) from which the two-page memo and the deck are derived. Minimum necessary changes; portfolio and project selection are frozen.

## Frozen decisions (do not reopen)

- Portfolio: the current 10 initiatives (P01, P02, P03, P04, P05, P08, P09, P12, P13, E01); featured cases P01, P03, P12, P13.
- Three scenarios only (downside / base / upside). No severe-stress line.
- P12 keeps its conditional licence receipts and shows its base-case return; its strong downside already covers the uncertainty.
- The half-budget option stays as written (approximate, four featured cases).
- Five-year horizon (Y0–Y5): heavy industry with long asset cycles and limited disruption pace.
- Cost of inaction counted **only at portfolio level**; project economics are pure profitability.

## Writing rules for the report

- Voice: the group's digital-transformation team writing an internal document to the CEO and Board. Use "we" / "our". "Vincent" becomes "our insider".
- Do not cite the course, slides, frameworks or teaching examples. Do not explain model construction choices (double counting, method caveats). Justify the strategy with figures and the parameters that matter.
- Keep the evidence labels (fact / calculation / assumption / local observation / unknown) and source references, but trim repeated disclaimers to one statement per section.
- Text tables in Markdown; only numeric tables as figures.

## Tasks

Each task: files, actions, check. Tick only after the check passes.

### T0 — Safe baseline
- [x] Restore `course/lectures/AI Strategy - session 2.pdf` (`git restore`). Received course material must stay unchanged.
- [x] Commit the current V2 working tree as a snapshot on `dev_vincent` (explicit paths, no push), so V3 changes are reviewable as a diff.
- [x] Copy `deliverables/report/full_strategy_report.md` → `deliverables/report/full_strategy_report.md`. All edits below go to V3; the draft stays as V2 until V3 is validated.
- **Check:** `git status` clean except V3 file; PDF present.

### T1 — Scenario weights 30 / 50 / 20
- [x] `work/finance/build_workbook.mjs`: weights → downside 0.30, base 0.50, upside 0.20. Fix stale README notes in the builder (they still say "P12 has no commercial receipts", "No inaction uplift").
- [x] Rebuild the workbook (`node work/finance/build_workbook.mjs`), run `python work/finance/reconcile_selected.py` (without `-I`; the script imports a sibling module) to regenerate `selected_chart_data.json`.
- [x] Recompute the inaction overlay with the new weights (`inaction_overlay.json` → `inaction_overlay_results.json`).
- [x] Replace every "25% / 50% / 25%" mention and every derived number in V3, `work/finance/*.md`, `REPRODUCE_CHARTS.md`.
- **Expected impact (pre-check):** expected NPV ≈ +$5.62m (was +$6.30m); expected cumulative cash trough ≈ −$10.2m at end Y1; scenario NPVs/IRRs unchanged.
- **Check:** reconciliation passes; `pytest work/finance/tests` passes; weighted figures identical in workbook, JSON, charts and text.

### T2 — Cost of inaction at portfolio level only
- [x] V3 "Cost of inaction and decision value": portfolio-level paragraph only. Expected portfolio NPV (pure profitability) → avoided cost of inaction (rising refining margin exposure, rig rates, customer churn from Y2) → decision value. Board voice, no method discussion. Keep the one-year-delay figure as a separate timing cost.
- [x] Confirm no inaction amount appears in any project section, project table or project chart.
- [x] Bridge chart relabelled: "Expected portfolio NPV (projects only)" → "Avoided cost of inaction (portfolio)" → "Decision value".
- [x] Rewrite `work/finance/cost_of_inaction.md` to the same rule (it currently says zero is booked).
- **Check:** one bridge, one number set, identical in text, chart and work note.

### T3 — Bottleneck and operating model (core correction)
- [x] Remove all wording implying branches lack accountability (Context, Section 1, table 01 row "Make branch leaders accountable…").
- [x] New diagnosis (marked as local observation from our insider, to be tested in the pilots): a project is split across four actors without a common line:
  1. the branch project lead (usually branch digital-transformation head) who leads;
  2. the branch data engineer, not reporting to that lead;
  3. the TDF data scientist, who sets data-science rules but carries no financial objective and works like an external consultancy;
  4. the end user, who gives the need and feedback but has no decision power.
  Consequence: dispersed responsibility, widely spaced progress points, slow iterations, few projects per decision-maker.
- [x] Remedy: a dedicated trio per project (TDF data scientist, branch data engineer, business expert) spending a large share of their time on it, in permanent contact, reporting **both** to the project lead and to their own line managers. Faster, more agile work at team level; objectives and continuation gates unchanged; decision-makers can run more projects in parallel → higher deployment capacity; working side by side spreads AI culture into the branches.
- [x] Measures to test the model in the pilots: interval between progress reviews, delivery lead time, expert time actually available, projects per lead, adoption.
- [x] Apply to: V3 Context, Executive decision, Sections 1–2, tables 01–02 (Markdown), change-management subsections; `deliverables/report/change_management_plan.md`; `work/options/operating_model.md`; `work/options/readiness_bottleneck.md`.
- **Check:** grep for "accountable", "ownership", "champion" in V3 — every occurrence consistent with the new diagnosis.

### T4 — Missing board-level content (written as strategy, no course references)
- [x] Readiness: five dimensions scored (3 / 3 / 3.5 / 2.5 / 2.5) and stage "Implementing, approaching Scaling", Markdown table, from `readiness_bottleneck.md`, with the T3 bottleneck.
- [x] Executive decision opens with one resolution sentence: amount, period, portfolio, outcome, downside, gate.
- [x] Portfolio J-curve figures: base trough −$9.8m end Y1, downside −$11.5m, expected ≈ −$10.2m (after T1); break-even during Y4; capital actually at risk vs the $2.90m Y0 ceiling.
- [x] Envelope: one sentence on the five-year horizon (heavy industry); three-year view Y0–Y3 = $16.40m; run cost from Y4 ≈ $2.7–2.8m/year (exact from model); CAPEX/OPEX split already present.
- [x] Sourcing: six-factor score (differentiation, proprietary data, time-to-market, in-house skills, regulatory control, cost at scale) for the four featured cases, Markdown table, consistent with the current buy/blend labels.
- [x] Business-unit co-funding proposal: Y1 100% central, Y2 40% branch, Y3+ 60% branch (proposal, to be agreed with branches).
- [x] Programme tranche gates: Gate 1 (end Y1) and Gate 2 (end Y2) with metric, threshold, owner, action, linked to project gates.
- [x] Horizon mix: state the deliberate mix on one-time and on total spend (≈ 65 / 21 / 13 on total) and why.
- [x] One sentence on scale: a ~$22m programme proves the delivery model before group-wide extension.
- **Check:** each item present once, numbers match the model after T1.

### T5 — Adoption thresholds
- [x] Single staircase everywhere: ≥ 40% of eligible users active at month 6 (warning → remediation within 30 days); ≥ 60% of eligible decisions recorded through the tool at month 12 (continuation gate).
- [x] Apply to V3 (release discipline, gates table), `change_management_plan.md`, `work/governance/gates_and_adoption.md`.
- **Check:** grep "40%" / "60%" consistent across the three files.

### T6 — Tables back to Markdown
- [x] Convert text/mixed tables 01, 02, 03, 06, 07, 08, 11, 16, 20, 22, 23 to Markdown in V3 (content from `report_tables.json` / case files, updated by T3–T5).
- [x] Keep numeric figures 04, 05, 09, 10, 12–15, 17–19, 21; give them clean alt text (e.g. "P01 base cash flow, $m").
- [x] `render_report_tables.py` renders only the numeric tables; archive the 11 obsolete PNG/SVG pairs.
- **Check:** no image reference to a text table; all remaining images exist.

### T7 — Form and voice
- [x] Header: title, team, internal status, date.
- [x] Consistent numbering (Context and Executive decision as unnumbered lead, then 1–6; uniform sub-structure for the four cases, P12 included).
- [x] "Vincent suggests" → "our insider"; "we/our" throughout; define FDE or drop the acronym.
- [x] Trim repeated disclaimers; keep evidence labels and sources.
- **Check:** grep "Vincent", "course", "slide", "Helios" in V3 → zero hits.

### T8 — New and updated charts (TotalEnergies palette, PNG + SVG)
- [x] Operating model before/after: four dispersed actors vs. trio with dual reporting.
- [x] Decision-value bridge (T2 labels, T1 weights).
- [x] Readiness heatmap: five dimensions, current vs target.
- [x] Tranche and gate timeline: Y0, Gate 1, Gate 2, month 36.
- [ ] Optional, skipped (table figure already shows it): Y0–Y3 spend by six cost categories, stacked bars (from `category_allocation.csv`).
- [x] Regenerate all existing charts after T1 (scenario NPV/IRR, portfolio J-curve, half-budget, inaction bridge).
- **Check:** visual inspection of every figure; numbers read from JSON only.

### T9 — Align supporting files with V3
- [x] Rewrite: `work/finance/portfolio_economics.md` (10 initiatives, $21.94m, current scenarios), `work/options/selected_portfolio_decision.md` (10 initiatives, P12 receipts, inaction rule), `work/projects/portfolio_sequencing_canvas.md` (add P04, P08), `work/projects/REPRODUCE_CHARTS.md`, `work/projects/course_requirements_audit.md`.
- [x] Check `work/finance/discount_rate_policy.md`, `reserve_cards.md`, case files P01/P03/P12/P13 against V3 (weights, thresholds, voice).
- **Check:** grep for "16.287", "25%/50%/25%", "No commercial H3 receipt", "eight", "zero additional avoided" → no active hit outside the archive.

### T10 — Archive obsolete material → `work/archive/pre_v3_2026_11_11/`
- [x] Notes: `work/finance/half_budget_options.md`, `half_envelope_alternative.md`, `project_economics_decision_review.md`, `portfolio_model_14_notes.md`; `work/options/thesis_and_selection.md` (duplicate); `work/projects/chart_regeneration_spec.md` (8 IDs, 25/50/25, no receipts).
- [x] Models: `work/finance/portfolio_model_selected.xlsx` + `.inspect.ndjson`; delete lock file `~$portfolio_model_selected.xlsx`.
- [x] Scripts no longer used by the current chain (check imports first): `finalize_selected.py`, `revise_portfolio.py`, `update_selected_documents.py`, `proposed_eight_test.py`, `test_half_options.py`, `project_economics_review.py`, `verify_*.ps1`, `sync_selected_issues.ps1`, `work/projects/integrate_*.py`, `complete_report_requirements.py`; stray `__pycache__` test files.
- [x] Obsolete table images (T6). Regenerate `full_strategy_report.html` from V3 instead of keeping the stale render.
- **Check:** reconciliation, chart rendering and tests still run after the move.

### T11 — Roadmap
- [x] Update `work/roadmap.md` (dates, statuses of steps 09–21, link to V3). GitHub issues are **not** edited without separate approval.

### T12 — Final consistency pass
- [x] Run reconciliation, tests, chart and table renderers.
- [x] Cross-check key numbers between V3, workbook/JSON and work notes: $21.94m, $9.82m, $2.90m, scenario NPV/IRR, expected NPV and IRR, decision value, trough, break-even, run cost, horizon mix.
- [x] Full read-through as a sceptical CEO: worst case, stop rule, inaction, half budget, break-even, co-funding — each answered in V3 with a number.
- [x] Vincent reviews V3 → then V3 replaces the draft and the work is committed (explicit paths, no push).

## Out of scope

Project selection, scenario definitions, half-budget option, memo and deck (next session, derived from V3).
