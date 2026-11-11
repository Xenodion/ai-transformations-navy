# Selected portfolio verification — 10 November 2026

The revision preserves the existing cash-flow architecture and central P01/P03 amounts, with a smaller selection, revised P13 benefit booking and operationally differentiated scenarios. It is a classroom proposal based on explicit hypotheses, not a validation of internal TotalEnergies project performance.

## Checks completed

- `build_workbook.mjs` exported the selected workbook. Changing retail stores from 100 to 110 changed portfolio cash; the input was restored before export.
- `reconcile_selected.py` independently reproduced all 960 annual benefit/OPEX/CAPEX/tax/net cells using cached Inputs and Scenarios, checked 18 cumulative portfolio figures, scanned cached Excel error cells and checked the half-budget limit.
- `review_selected.py` reconciled the six cost categories to gross spend; verified the half-budget workbook and JSON cash/NPV; checked local links in the report/navigation and exclusion of retired project IDs from the report.
- Visual inspection covered the portfolio preview and supporting ranges in Inputs, Focus drivers, Scenarios, Metrics, Cash flow build, H3 horizon, Read me and Half budget. Tables were readable; no clipped material labels were observed in those ranges. This is sampled workbook layout verification, not a review of every cell or exported presentation chart.
- Current model: gross cost $16.28708m; common-10% base NPV $3.490711m, weighted NPV $2.123740m; downside NPV -$5.370054m; severe stress -$8.045008m. Half response costs $7.460m, below $8.14354m, with weighted NPV $0.069846m. The latter has very limited margin for additional cost.

## Remaining limits

Native Excel recalculation has not been performed on the revised file. Cached values were independently checked against formulas' economic logic; this does not certify every Excel-specific feature. Public sources cannot validate site eligibility, partner economic shares, supplier costs, markdown attribution or licensing novelty. These remain explicit decision gates.

Charts are intentionally not regenerated in this task: the user requested specifications for lower-cost rendering agents. The specification and checked JSON are ready. Old chart assets and notebook are archived, and the report does not reference them. Memo/slides remain downstream.

GitHub issues remain open. Connector updates returned HTTP 403. A local CLI read succeeded, but automatic approval review rejected the bulk update for insufficiently verified disclosure to the remote destination. No further write workaround was attempted. The local roadmap records pending synchronization; the prepared script has not been authorized to run.


## Figure production completed, 11 November 2026

Fourteen PNG/SVG figures were generated from the checked JSON and visually reviewed. Nine figures are embedded in the analytical report; a self-contained HTML reading copy is available. The notebook and CLI share `work/projects/render_selected_charts.py`. See `work/projects/REPRODUCE_CHARTS.md`. Full financial acceptance remains open; no original source PDF or financial assumption was changed for rendering.
