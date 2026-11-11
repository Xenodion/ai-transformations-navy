# Portfolio economics (V3, 11 November 2026)

**Scope:** ten initiatives (P01, P02, P03, P04, P05, P08, P09, P12, P13, E01). Source of truth: [working workbook](portfolio_model_working.xlsx), built by `build_workbook.mjs` and checked by `reconcile_selected.py`; derived data in `selected_chart_data.json`. USD million, nominal, after 25% cash tax, unlevered, no terminal value; P13 translated at 1.1165 USD/EUR.

**Envelope:** gross $21.94m over Y0–Y5; one-time $9.82m ($5.69m CAPEX, $4.12m launch expense); recurring $12.12m. Annual gross cost: Y0 2.90, Y1 8.55, Y2 2.31, Y3 2.64, Y4 2.74, Y5 2.79. Three-year view Y0–Y3: $16.40m.

| Scenario | Weight | NPV at 10% | IRR | Cumulative cash Y5 |
| --- | ---: | ---: | ---: | ---: |
| Downside | 30% | −1.30 | 5.7% | +2.27 |
| Base | 50% | +7.11 | 32.6% | +13.78 |
| Upside | 20% | +12.28 | 48.2% | +20.83 |
| Expected | — | **+5.62** | **27.8%** | +11.74 |

| Annual net cash | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Downside | −3.156 | −8.301 | 0.895 | 3.053 | 4.665 | 5.119 |
| Base | −2.897 | −6.918 | 2.329 | 5.295 | 7.704 | 8.267 |
| Upside | −2.897 | −6.393 | 3.593 | 7.416 | 9.326 | 9.785 |
| Expected | −2.975 | −7.228 | 2.152 | 5.047 | 7.117 | 7.626 |

**J-curve:** cumulative trough at end Y1: base −9.8, expected −10.2, downside −11.5. Payback: base 3.3 years, expected 3.4, downside about 4.6.

**Scenario definitions:** project-specific. Typical downside: 80–90% of full-scale benefits, 105–110% of costs, slower ramp; P12 stops after Y2 with no receipts and a $0.10m closure cost. Upside: 115% of benefits, ramp accelerated by 15% (capped), base costs. P12 base includes conditional licence receipts of 0.60 / 1.50 / 2.30 in Y3–Y5. Weights 30/50/20 are judgemental. The workbook also carries an unreported severe-stress sheet; it is not part of the decision case.

**Discount rates:** 10% portfolio screen = 7% published impairment WACC + 3 pp execution premium; project hurdles 9–12% ([policy](discount_rate_policy.md)).

**Half budget (approximate):** the four featured cases cost $11.35m (51.7%), base IRR 34.8%, downside 6.4%, expected NPV +$3.35m; E01 excluded.

**Cost of inaction:** portfolio-level only, see [cost_of_inaction.md](cost_of_inaction.md): +$1.32m, decision value $6.94m. One-year delay of the base programme: −$0.65m NPV.

**Reproduce:** `node work/finance/build_workbook.mjs` → `python work/finance/reconcile_selected.py` → `python work/projects/render_selected_charts.py` → `python work/projects/render_v3_charts.py` (from the repository root).
