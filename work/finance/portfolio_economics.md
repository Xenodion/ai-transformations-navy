# Selected portfolio economics

 Consolidated financial decision

**Calculation on assumptions:** gross base programme cost **$16.287m**, covering Y0 and five operating years. Y0 is the decision period; Y1–Y5 are annual periods after it. Gross cost excludes cash tax; NPV includes modelled tax. All cash is nominal, post-tax, unlevered and translated at the unchanged 1.1165 USD/EUR assumption. The 10% common screen is a team assumption (7% published impairment WACC proxy plus 3pp), not a disclosed corporate investment hurdle. Project screens retain 9–12% rates.

| Scenario | NPV at 10%, USD m | IRR |
| --- | --- | --- |
| Downside | -5.370 | -12.3% |
| Base | +3.491 | 26.4% |
| Upside | +6.884 | 41.6% |
| Weighted | +2.124 | 19.6% |
| Severe stress | -8.045 | -26.9% |


**Scenario assumptions:** downside has 75% of central unit benefits, 115% of capital, launch and recurring costs, and benefits delayed one year (no catch-up outside Y5). Base retains the original ramp. Upside has 115% unit benefits and each central adoption fraction multiplied by 1.15, capped at 100%, at base costs. These are judgments, not calibrated frequencies. The H3 downside stops after Y2 and retains a $0.10m Y3 exit allowance. H1/H2 downside conservatively retains full operating spending: gate savings are not assumed. A separate severe stress also delays benefits one year, uses 65% benefits and 120% costs, and retains H3 spending. It measures failed cost control, not the expected gated response.

Weights are subjective 25%/50%/25%. Weighted IRR is computed from weighted annual cash, never an average of IRRs. No terminal value, H3 receipts or avoided-inaction uplift is booked. H3 costs are retained in base and upside even though revenue is zero. The severe stress is unweighted and is not a maximum-loss estimate.

| Annual cash, USD m | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 |
| --- | --- | --- | --- | --- | --- | --- |
| Downside | -2.641 | -6.666 | -1.239 | 0.741 | 2.417 | 3.460 |
| Base | -2.297 | -4.748 | 1.649 | 3.417 | 4.758 | 4.708 |
| Upside | -2.297 | -4.409 | 2.579 | 4.854 | 5.707 | 5.657 |
| Weighted | -2.383 | -5.143 | 1.160 | 3.107 | 4.410 | 4.633 |

| Base gross cost | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 |
| --- | --- | --- | --- | --- | --- | --- |
| Annual release ceiling | 2.297 | 5.797 | 1.762 | 2.094 | 2.144 | 2.194 |


Weighted cumulative cash trough is −$7.526m; simple interpolated payback is 3.74 years. Fund the trough, not just CAPEX. A base gross ceiling is not a promise that overruns are funded: the downside quantifies an overrun requiring a stop, resize or new approval.

**Accounting limits:** 25% cash tax on positive annual surplus after straight-line depreciation of CAPEX over five years; no loss carry-forward, working capital, financing or terminal value. This simplified tax convention and unchanged cost assumptions need jurisdictional and procurement validation. Costs include launch training but do not prove all staff backfill is funded. Before G0, reconcile vendor quotes and staff days against the ceiling; do not treat existing employee time as free. The initial spending is not a contractual loss cap.

#
## Reproduction and limits

Run `node work/finance/build_workbook.mjs`, then bundled Python `work/finance/reconcile_selected.py`. The checker independently recomputes all 960 annual benefit/OPEX/CAPEX/tax/net cells from workbook inputs and scenarios, checks the 18 consolidated cumulative flows, scans cached formula errors and verifies the half-budget limit. JSON is a derived chart export, not an editable second model. Re-run after any change. Native Excel recalculation has not been performed for this version.

**Why the half-budget portfolio is not simply the four featured cases.** The featured cases were selected to explain the strategy and its different decision mechanisms, not to fit a 50% spending limit. P01 + P03 + P12 + P13 cost **$11.347m**; retaining the required E01 controls brings that to **$12.287m**, or **75.4%** of the full envelope, against **$8.144m** available. Even limiting P12 to Y0–Y2 plus closure gives **$11.037m**. Keeping all four at half budget would therefore require redesigned asset/store scopes, fixed-versus-variable costs and benefit ramps. Proportional scaling would be misleading. The constrained alternative instead preserves complete, costed operating cases and one bounded H3 experiment. It is a feasible response, not a claim of an optimized subset across all possible scope redesigns.
