# Cost of inaction (V3, 11 November 2026)

**Rule:** the cost of inaction is counted **only at portfolio level**. Project NPVs, IRRs, paybacks and J-curves are pure profitability against today's operating baseline and never include it.

**Mechanism:** project benefits are measured against a static baseline. Without investment the baseline itself deteriorates; the avoided part of that deterioration is a separate effect, added once in the portfolio decision bridge.

| Exposure from Y2 (assumption) | Linked scope | Additional gross benefit at full adoption, $m/year |
| --- | --- | ---: |
| Refining margin per unrecovered barrel +$1/bbl | P01 sites | 0.287 |
| Avoidable rig spread cost +$0.05m/day | P03 campaigns | 0.360 |
| Churn +1 pp on 1.2m eligible accounts | P08 | 0.162 |

Cash is scaled by each project's scenario-weighted benefit ramp (30/50/20), taxed at 25% and discounted at 10%.

| Item | PV at 10%, $m |
| --- | ---: |
| Expected portfolio NPV (projects only) | 5.62 |
| Avoided cost of inaction (P01 0.51, P03 0.54, P08 0.27) | 1.32 |
| **Decision value** | **6.94** |

Separate timing view: delaying the base programme one year costs $0.65m of NPV. Inputs: [inaction_overlay.json](inaction_overlay.json); results: [inaction_overlay_results.json](inaction_overlay_results.json), produced by `work/projects/render_selected_charts.py`. The three exposures are assumptions tracked as leading indicators, not forecasts.
