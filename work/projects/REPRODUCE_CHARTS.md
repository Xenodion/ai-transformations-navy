# Reproduce the model, charts and tables

From the repository root (Python with `openpyxl`, `numpy`, `matplotlib`; Node for the workbook builder):

```powershell
node work/finance/build_workbook.mjs              # rebuild the workbook from coded assumptions (overwrites manual edits)
python work/finance/reconcile_selected.py         # check every cash cell, export selected_chart_data.json
python work/projects/render_selected_charts.py    # financial charts + inaction overlay results
python work/projects/render_v3_charts.py          # operating model, readiness, funding gates
python work/projects/render_report_tables.py      # numeric table figures from report_tables.json
```

Charts go to `work/projects/assets/` (PNG + SVG) and PNGs are copied to `deliverables/report/assets/`.

- Scenario weights (30% downside / 50% base / 20% upside) live in the workbook (`Portfolio!B17:D17`, set in `build_workbook.mjs`) and flow into the JSON and all chart labels.
- The cost of inaction is a portfolio-level overlay: inputs in `work/finance/inaction_overlay.json`, results in `inaction_overlay_results.json`; it never enters project cash flows.
- `report_tables.json` holds only the numeric tables; it does not update automatically from the model, so reconcile its figures after any model change.
- The `Long-term DCF` worksheet is a separate base-case sensitivity and is not used in the report.
