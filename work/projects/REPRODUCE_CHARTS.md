# Reproduce the working charts

From the repository root, with Python packages `openpyxl`, `numpy`, and `matplotlib`:

```powershell
python work/finance/reconcile_selected.py
python work/projects/render_selected_charts.py
```

The input is the recalculated `work/finance/portfolio_model_working.xlsx`. The first command checks annual cash components and exports `work/finance/selected_chart_data.json`. The second creates PNG and SVG figures in `work/projects/assets/` and copies PNGs to `deliverables/report/assets/`. The notebook invokes the same renderer. The builder `node work/finance/build_workbook.mjs` regenerates the working workbook from its coded assumptions and overwrites manual edits.

The four featured projects are P01, P03, P12 and P13. Their spending represents 51.7% of the current full portfolio; the comparison displays the exact amounts. P12 base-case licensing revenue is conditional. The report and cards use the current working figures.

The `Long-term DCF` worksheet adds a separate base-case Y15 sensitivity. Its blue cells set the common discount rate, number of continuation years and fraction of Y5 net cash retained in each subsequent year. The baseline holds Y5 net cash constant in Y6–Y15, then stops, with no terminal value or renewal investment. Recalculate and save the workbook before running the commands above. The renderer uses the TotalEnergies palette in `sources/assets/TotalEnergie_colors.svg`.

The scenario NPV and IRR figures use the cash flows and weights in `selected_chart_data.json`. The additional inaction bridge reads the editable assumptions in `work/finance/inaction_overlay.json`, calculates the scenario-weighted incremental cash flows for P01, P03 and P08 and saves them to `work/finance/inaction_overlay_results.json`. This overlay is a separate sensitivity and does not modify the workbook or portfolio results.

For the report's table figures, edit `work/projects/report_tables.json`, then run `work/projects/report_tables.ipynb` or `python work/projects/render_report_tables.py`. It generates matching PNG and editable vector SVG figures in `deliverables/report/assets/`. The JSON is the source of these table figures; changing the financial model does not automatically update it. Reconcile financial entries with the model whenever figures change.
