# Chart regeneration specification for delegated production

Status: implemented and visually checked on 11 November 2026. See REPRODUCE_CHARTS.md. Do not edit financial assumptions. All authored labels must be English.

## Source contract

- Active workbook: `work/finance/portfolio_model_selected.xlsx`.
- Derived, independently checked data: `work/finance/selected_chart_data.json`, version `selected-2026-11-10`.
- Read `work/finance/portfolio_economics.md` and `deliverables/report/full_strategy_report_draft.md` before rendering.
- Read chart data, never copy numbers from archived images. Data values are USD million. For P13 native EUR charts divide every cash value by its `fx`; do not convert percentage metrics or years.
- Selected IDs exactly P01, P02, P03, P05, P09, P12, P13, E01. Featured cases exactly P01, P03, P12, P13.
- No post-Y5 extrapolation, inaction uplift, invented H3 return, or scenario probability change. Scenario weights are subjective 25/50/25. Cumulative cash is the running sum of annual net cash, not NPV.
- Use one notebook, `work/projects/portfolio_charts.ipynb`, to load JSON and export all figures. Preserve the existing navy palette where legible. Do not run the archived notebook or its embedded financial assumptions.

## Outputs

1. Portfolio map: H1/H2 base simple payback in years on x; full-scale gross annual contribution in USD m on y; bubble area proportional to one-time investment (not radius). Use linear axes. Read payback from each case Base. Derive annual gross contribution from the explicit case drivers or base Y5 gross (all cash cases reach full scale); show uncertainty in caption. Put P12 in a separate learning-option panel with $2.85m gross ceiling and Y2 evidence gate. E01 gets a separate shared-cost label, no fictitious benefit/payback point.
2. Investment allocation: two clearly labelled bars, one-time spend and full Y0–Y5 gross spend, each H1/H2/H3/Enabler and summing to 100%. H3 returns are unestimated. If showing value by horizon, use signed weighted NPV contributions at the common 10% screen and show negative contributions; do not represent them as a positive 100% return split.
3. Portfolio J-curves: downside/base/upside plus optional dashed weighted cash. Y0–Y5, USD m, cumulative undiscounted cash, zero line, legend. Separate severe stress rather than mixing it into the weights.
4. Four case J-curves and cash tables: P01/P03/P12 USD m; P13 EUR m. P12 must say “learning expenditure; no commercial receipts modelled” and must not show IRR/payback. Show the stopped downside correctly: sunk costs and closure expense remain.
5. Full versus half-budget comparison: gross spend, common-rate weighted NPV and remaining headroom. The half scenario funds P12 only through Y2 plus $0.10m closure/transfer, not a full five-year P12. Label constrained scope clearly. Do not suggest near-zero positive NPV is a robust margin.

Export PNG at presentation resolution and SVG under `work/projects/assets/`; copy PNGs needed by the report into `deliverables/report/assets/`. Use stable names `selected_portfolio_map`, `selected_horizon_mix`, `selected_portfolio_jcurve`, `selected_focus_jcurves`, `selected_half_budget`, plus `selected_p01/p03/p12/p13_cash_table` and `_jcurve`. Do not restore obsolete filenames. Add figure references to the relevant report sections only after verification.

## Acceptance checks

- Assert exact eight IDs and four focus cases; validate data version.
- Match workbook/report gross envelope, Y0 tranche, base/weighted NPV and all 18 portfolio cumulative cash values to 1e-7 before rounding.
- Cash tables match source rows including tax. Costs and cash must not switch signs twice.
- Horizon shares sum to 100%; H3 costs and E01 included once.
- No discarded initiatives in legends, labels or embedded metadata. No long-term imaginary coordinates.
- Inspect every figure at normal size for clipped labels, signs, legends and units. Use accessible contrast and consistent colors.
- Deliver notebook, exports and a short verification record listing the source JSON SHA-256 and checks. Do not change financial content to make a chart look better.

This specification authorizes graphics production only. Memo and slides must continue to derive from the revised report after the visual check.
