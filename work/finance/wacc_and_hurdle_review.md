# WACC and investment hurdle review

**Status:** evidence and recommendation for the corrected model, 9 November 2026. No investment return in the current workbook is approved for decision use.

## Evidence and scope

- **Fact — historical WACC proxy:** TotalEnergies' 2025 Universal Registration Document, PDF and printed pp. 462 and 472 (SRC-002, CLM-075), describes **7% post-tax** as its weighted-average cost of capital estimated from historical market data, used for specified cash-generating units' impairment value-in-use tests. It states 7% for 2024 and 8% for 2023. Those cash flows are post-tax and incorporate asset-specific risks. This is a disclosed accounting valuation assumption, not necessarily a market WACC as of November 2026 or the company's internal AI capital hurdle.
- **Unknown:** TotalEnergies' actual marginal AI investment hurdle, current debt and equity market weights, prospective borrowing cost, equity beta and ERP, project-level effective tax rate, loss offsets and depreciation. Do not cite CLM-003 (ROACE and gearing) as evidence for a 7.5% WACC. The gearing figure is not the WACC debt weight; net debt/book equity cannot simply substitute for market debt/(debt + equity).
- **Course:** the professor's course, PDF p. 107, uses WACC = E/(D+E) × cost of equity + D/(D+E) × pre-tax cost of debt × (1 − marginal tax rate), and distinguishes WACC from a risk-adjusted hurdle. The numbers shown in a worked example are illustrative.

## Proposed treatment — explicitly assumed, not corporate policy

1. Use **7% post-tax** as the documented 2025 reference, with **6%–9%** sensitivity, clearly identifying its date and impairment context. It is an anchor, not a claim of a current market estimate.
2. For a transparent course-case decision rule, compare a single clearly labeled **10% illustrative nominal post-tax hurdle** (7% reference + 3 percentage points assumed project premium) against 7% and 12% sensitivity. This premium is a judgment, not TotalEnergies' published rate. Validate it with the actual sponsor before committing capital. If financial cash flows are explicitly risk-adjusted expected cash flows, explain the incremental risk premium so execution or probability risk is not charged twice.
3. Do not mix nominal cash flows with a real rate or post-tax WACC with pre-tax cash. Derive after-tax unlevered free cash flows using jurisdiction-specific marginal taxes, deductible operating costs, depreciation or amortization where supported, working capital and asset ownership; disclose losses and timing. The workbook's 25% tax variable is not currently a tax calculation, and a group-wide uniform rate is not verified. If reliable tax treatment cannot be established, show pre-tax cash and sensitivity without calling NPV a post-tax investment case.
4. The 9%–15% project rates in the current workbook are unsupported assumptions, not observed branch hurdles. A branch-specific WACC or decision hurdle must be supported with risk exposure, currency, leverage and tax basis. A 12% ROACE target is a ratio to book capital, not an NPV discount rate and cannot directly justify a 9% hurdle.
5. Sum NPVs evaluated at consistently justified project rates; do not treat a cost-weighted average rate as mathematically equivalent to the sum, since timing and risk exposures differ. A common hurdle may be shown as a comparison, with transparent limits. For H3, approve staged spend using learning gates; any commercial scenario is explicitly conditional and must not be banked as base case without evidence.
6. Recalculate project and portfolio NPV, IRR, cash timing, EV and hurdle comparisons from the same dated, incremental, after-tax schedules; show an independent reference calculation and bridge to financial statements. Do not treat IRR in isolation as value, and do not add a separate cost-of-inaction estimate if the same counterfactual is already in the cash flow.

## Current-model failures

`Variables!C6` hard-codes 7.5% and calls it Group WACC, while the proposed CAPM components omit the debt rate and capital weights required to reproduce it. `Variables!C5` hard-codes 25% without implementing a complete tax schedule. The project inputs and published waterfall use operational savings less implementation costs, with no demonstrated cash taxes, depreciation or ownership adjustments. `Portfolio_Consolidation!I24` weights branch assumptions by spending, an illustrative arithmetic statistic rather than an established company hurdle. `Scenario_Sensitivity_ENPV` hard-codes two scenario IRRs. Therefore substituting 7% or 10% directly into the present model would produce misleadingly precise results.

## Required validation

- Source the corporate reference above and specify valuation date, nominal currency and period.
- Reconcile taxes and operating cash flows on every project; document whether savings are pre-tax and whose interest is counted.
- Rebuild scenarios and gated timing before computing sensitivity at 7%, 10% and 12%.
- Independently recompute formulas and check model outputs in a spreadsheet engine; test source-linked assumptions and realistic downside, including failed gates.
