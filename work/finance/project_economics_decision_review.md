# Project economics — decision review, 11 November 2026

Working comparison only. The active workbook, report and graphics are unchanged. All project benefits and costs remain planning assumptions. Figures below use the existing tax/FX convention; downside is a new operational candidate, not a calibrated probability or an approved forecast.

| Project | Gross cost USD m | Base IRR / hurdle | Base payback years | Candidate downside IRR | Downside cumulative Y5 USD m | Decision and decisive evidence |
| --- | ---: | --- | ---: | ---: | ---: | --- |
| P01 | 3.150 | 57.8% / 9.5% | 2.40 | 21.4% | +1.264 | Keep. Downside: recovery 0.4%, margin $5.5/bbl, repairs $0.15m. Validate incremental sold throughput and funded reliability integration. |
| P02 | 2.230 | 47.2% / 10.0% | 2.87 | 22.1% | +0.985 | Keep conditional. Downside: 120 recovered bbl/day/hub, slower adoption. Verify equity entitlement and that recovered output is incremental. |
| P03 | 3.650 | 43.2% / 11.0% | 3.09 | 12.8% | +0.949 | Keep conditional. Downside: 5 days/rig, 80% economic share, 65% avoidable payment. Split ownership from payment rights; six days are not cash until invoices change. |
| P05 | 0.730 | 81.8% / 9.0% | 2.06 | 25.9% | +0.322 | Conditional enabler. Downside: 12% seats cancelled, $25 net monthly price. Verify actual paid seats and cancellation date; licence pruning is not itself an AI transformation. |
| P09 | 1.040 | 22.3% / 10.0% | 3.65 | -1.8% | -0.039 | Re-scope or defer. Downside: fuel saving 1.5%, slower ramp. Small standalone margin; contract control and incremental fuel saving must be established. |
| P12 | 2.850 | n/a / 12.0% | n/a | n/a | -1.750 | Fund learning, not a positive project IRR. Downside stops after Y2 with closure expense; base funds the full experiment. No royalty revenue booked. |
| P13 | 1.697 | 24.6% / 9.0% | 3.16 | 1.6% | +0.056 | Redesign cost/scope before approval. Downside: waste/stock-out gains -20%, markdown -25%. Distinct markdown cohort and actual label quotes are decisive. |
| E01 | 0.940 | n/a / 9.0% | n/a | n/a | -1.034 | Include once within H1 for presentation; preserve explicit governance cost in accounts. No standalone return. |

## Portfolio tests

| Scope | Base IRR | Downside IRR | Base NPV at 10%, USD m | Downside NPV at 10%, USD m | Downside cumulative Y5, USD m |
| --- | ---: | ---: | ---: | ---: | ---: |
| Full selected portfolio | 26.4% | 2.6% | +3.491 | -1.609 | +0.753 |
| Existing constrained half-scope | 17.3% | -9.4% | +0.732 | -1.945 | -1.237 |

## Decisions before changing the model

1. Retain central P01/P02/P03 values for now; they already produce plausible short paybacks under their stated assumptions. P13 requires a one-time ceiling of about EUR 0.932m for a three-year base payback with its current EUR 0.585m annual benefits, unchanged recurring costs and proportional initial-cost split. This is a procurement threshold to test, not a new price assumption.
2. Apply the candidate downside to each named operating lever, not a blanket one-year delay to every project. All candidates here also carry 10% higher initial and recurring costs. Retain a common risk narrative: slower execution, weaker capture and cost overruns. These numerical severities still need operational support; a positive result does not validate them.
3. A positive Y5 cumulative cash balance is not the same as clearing the hurdle. Keep both tests. Do not solve benefits backwards from a desired IRR.
4. Do not force every H1 into a 2–3-year downside payback or every project just above its hurdle. Require 2–3 years in the central case for cash-led H1; governance is a cost enabler. The portfolio downside must pass its own cumulative-cash test, including H3 and shared costs.
5. Cost completeness is not established. Map FDE allocation, business-owner backfill (50–100%), branch data engineering, site travel, cloud/licences and support onto existing project costs; add only the uncovered incremental amount. No trio-driven acceleration or benefit uplift is booked in this review.
6. Exclude the cost of inaction at this stage. No weights or expected IRR are assigned to the new candidate scenarios before downside and upside assumptions are agreed.
7. Current central tax treatment ignores loss carry-forwards and working capital; economic ownership is especially material for upstream/drilling. Confirm these before describing the case as investment-grade.

## Margin of safety at unchanged base timing

Annual gross benefit needed for zero NPV at each project hurdle. This is a diagnostic calculation, not a forecast or a continuation gate. Amounts are native USD m except P13 EUR m.

- P01: central 2.116; break-even 1.080; headroom 49.0%.
- P02: central 1.643; break-even 0.904; headroom 45.0%.
- P03: central 2.880; break-even 1.660; headroom 42.4%.
- P05: central 0.540; break-even 0.231; headroom 57.2%.
- P09: central 0.600; break-even 0.469; headroom 21.9%.
- P13: central 0.585; break-even 0.446; headroom 23.8%.

Reproduce with `python work/finance/project_economics_review.py`. Input: selected workbook Inputs. Output: this review only. No assumptions are written back into the workbook.
