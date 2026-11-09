# Independent tradeoff and correction roadmap review

**Date:** 9 November 2026. **Status:** independent analytical recommendation; no investment approval or primary-source certification. This review uses the current repository audit and financial review as local observations, not as independent evidence of company performance.

## Immediate decisions

1. Retain all authorized H3 learning costs in the funded-program cash flow while excluding unsupported H3 commercial receipts from its base case. Show the H3 option case separately; do not remove its costs to improve NPV.
2. Distinguish the authorized envelope, committed spend, conditional releases and actual cash payments. Allocate the envelope to 100%, including an explicit unallocated reserve where appropriate. Do not assume that every reserved project starts spending at inception.
3. Count rig-day reductions as cash only when a supported contract mechanism lowers TotalEnergies-attributable payments. Otherwise classify them as capacity, schedule or risk effects. Mero is Petrobras-operated: partner ownership alone neither grants operational control nor establishes cash entitlement.
4. Re-estimate P13 fixed and variable costs for the controlled eligible-site perimeter. Do not scale all costs mechanically by site count or retain gates exceeding the case's own mature benefit without explanation.
5. Let evidence and consistent scenarios determine returns and horizon mix. Do not force negative downside NPV, prescribed return shares or H3 classification. Existing Quadra VPP activity makes a novelty comparison necessary.
6. Model failed gates explicitly. Base-case inputs must be tested against gate thresholds; failed gates stop or delay subsequent costs and benefits. Sunk pilot costs, termination charges and irreversible commitments remain; zero stranded capital is not credible by default.

## Execution order and acceptance tests

| Order | Decision/output | Acceptance test |
| --- | --- | --- |
| 1 | Freeze decision-use claims; establish one dated assumptions register | Every material input has evidence class, source or assumption, scope, units, timing, owner and uncertainty; old headline returns are marked unvalidated. |
| 2 | Resolve project eligibility, existing capability and cash entitlement | P03 operator/contract/data rights and attributable payments are explicit; P11 novelty is tested against existing capabilities; P13 eligible-site count and ownership are identical across the case. |
| 3 | Rebuild scope-matched project economics and gate schedules | Fixed/variable/run/adoption costs, benefits and dependencies reconcile; gates can be reached in chronological order; no positive post-stop benefits without justified residual value. |
| 4 | Consolidate committed program and conditional options separately | Envelope totals 100%; scheduled spend reconciles to project costs; funded H3 costs remain; unsupported H3 revenues, soft savings and duplicate benefits are excluded from base cash. |
| 5 | Recompute finance and adverse scenarios | Dated flows reproduce NPV/IRR/payback independently; gate failures retain sunk/exit costs; downside assumptions are coherent without targeting a particular sign. |
| 6 | Reassess selection and governance, then synchronize tracking | Retained/rejected choices follow corrected economics and strategic fit; case/model/gate thresholds agree; any acceptance failure is reflected in both issue and roadmap by the authorized coordinator. |
| 7 | Derive report, memo, then slides and visuals | One validated dataset drives all figures; H3 has no invented payback; all outputs share dates, scope, costs and decision status. |

## Discount-rate decision

Follow `../finance/wacc_and_hurdle_review.md`: 7% is a documented historical post-tax impairment reference, not verified current AI policy. The proposed 10% hurdle is an explicit teaching-case assumption, with 7% and 12% comparison. Substituting a new rate cannot repair unsupported benefits or inconsistent tax treatment. Use consistently after-tax nominal cash flows for an after-tax NPV; otherwise clearly label the pre-tax analysis and do not claim post-tax hurdle clearance. Do not equate a spending-weighted rate with the sum of project NPVs at different rates.

## Sources and limits

- `../roadmap.md`: local observation of deliverable sequence, acceptance criteria and tracking rules; current completion marks require reconciliation with known failures.
- `correction_plan_preliminary.md`: local audit findings and primary-source leads, 9 November 2026; figures are diagnostic, not approved economics.
- `../finance/wacc_and_hurdle_review.md`: documented reference and assumptions, 9 November 2026.
- `../../AGENTS.md`, `../../README.md`, `../../.agents/README.md`: project conventions.

No external communication or roadmap/issue modification was performed in this review. Primary documents and workbook recalculation still require the responsible validation pass.

## Additional direct file checks

**Local observation — governance, 9 November 2026:** `../governance/gates_and_adoption.md` lines 262–336 retains a $38.79m envelope, a month-12 Mero gate and a P13 assertion that the $3.90m envelope less $1.20m inception CAPEX leaves $2.70m cancellable. These are proposed figures and commitments, not verified corporate arrangements. The subtraction is insufficient to establish cancellable cash at month 6: deduct all cash already spent and non-cancellable commitments by that date, then add exit costs. Reconcile each tranche with the dated model rather than treating the entire unpaid balance as recoverable.

**Recommendation:** Maintain two separate controls at each gate: (a) operational eligibility, safety and evidence thresholds; (b) prospective value of the next release using only future incremental costs and benefits. Report historical sunk losses transparently in the whole-program result, but do not let sunk expenditure determine whether further spending is worthwhile. Preserve alternative or delayed releases when a failed project has no causal dependency on another; avoid a portfolio-wide stop merely because an unrelated early pilot fails.

**Local observation — roadmap, 9 November 2026:** the table assigns owners through step 20, while its final paragraph still says steps 11–27 are unassigned. This is a definite internal documentation conflict; actual GitHub ownership was not inspected. Correct the paragraph only after comparing live issues with the table. Reopen only steps whose acceptance criteria materially fail, with a precise unmet test, rather than mechanically reopening all preceding research.
