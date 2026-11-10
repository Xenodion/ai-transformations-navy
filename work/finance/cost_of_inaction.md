# Step 19 — Cost of Inaction & Decision Value Bridge

> **Review status (9 November 2026): Under reconstruction. Figures, gates and claims in this draft are not approved for decision use; see [independent review](../research/astra_tradeoffs_review.md) and [correction plan](../research/correction_plan_preliminary.md).

## Revised comparison and accounting rule

**Decision definition:** compare the proposed staged programme against a continuation case that retains TotalEnergies' existing AI teams, vendor contracts and savings initiatives. Any future cash-flow paths must use the same calendar, currency, ownership, tax and baseline. For each period, the incremental programme flow is `programme cash − continuation cash`; its NPV is the discounted sum of those incremental flows. The old $276.02m erosion estimate and resulting incremental NPV/IRR are withdrawn from decision use until causality, exposure, overlap and ownership are demonstrated.

For delay, model the same programme starting later against an otherwise identical continuation case. The early-start minus delayed-start cash-flow difference is the cost of waiting or benefit of acting earlier; it must not be added again to an NPV already measured against that delayed case. The comparison is implemented and checked in `counterfactual.py` and `test_counterfactual.py`.

| Prior driver | Revised treatment |
| --- | --- |
| Refining margin slippage | No cash loss assumed from competitor announcements alone. Quantify only an evidenced gap to an identified continuation baseline and reconcile it with P01/P10. |
| Power imbalance | Existing trading and aggregation capability belongs in the continuation baseline (CLM-027, CLM-076). Demonstrate eligible exposure and avoid overlap with P04/P11. |
| Drilling delay | Include only contractual incremental cash attributable to TotalEnergies; reconcile with P03 and partner/operator rights (CLM-077). |
| Talent attrition | Incremental departures, replacement expenses and the programme's effect are unknown; do not add an unsupported avoided loss. |
| Regulatory and cyber risk | Classify individual systems and estimate incremental expected loss only with a defensible probability, severity and counterfactual. An undisclosed inventory is not proof that all 10,000 models are non-compliant. |

The earlier unsupported numerical estimates are removed from the active document. The previous tracked version remains in Git history.
