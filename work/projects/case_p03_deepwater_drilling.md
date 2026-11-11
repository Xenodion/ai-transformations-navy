### 6.2 P03 — Deepwater drilling advisory (H2, provisional)

**Status:** Working case aligned with the financial model on 11 November 2026. All financial inputs are planning assumptions; the existing operational baseline and contractual terms must be validated. Model: [working workbook](../finance/portfolio_model_working.xlsx); independent annual cash-flow check: [reconciliation](../finance/reconcile_selected.py).

#### 1. Proposal and starting point

**Proposal:** Test a human-supervised planning and drilling advisory workflow across **two eligible operated deepwater rigs or campaigns**. Identify actual operated assets and obtain agreement from the operator, drilling contractor and relevant partners before committing to a pilot. Existing Cognite deployments and drilling practices remain in the counterfactual (CLM-019); count only incremental capability and cash.

**Fact:** Mero is operated by Petrobras; TotalEnergies' reported interest was 19.3% in the 2025 announcement (SRC-037, CLM-077). The previous claim that Mero is operated by TotalEnergies was incorrect. This case therefore does not assume the ability to deploy unilaterally at Mero, nor apply the 19.3% figure mechanically to a different contract.

**Problem [Hypothesis]:** Better use of well and drilling data may reduce non-productive time. A faster operation does not automatically save cash: the contract must permit an earlier rig release, reduce variable charges or create another documented financial benefit. BP's published well-planning example is context, not proof of a TotalEnergies gap or saving (CLM-068).

#### 2. Alternatives, horizon and delivery

| Option | Assessment |
| --- | --- |
| Existing drilling workflow | Counterfactual, including existing engineering and contracted tools. |
| Improved manual or rules-based planning | Benchmark using the same wells, staff and contractor terms. |
| Commercial drilling tools alone | Consider existing contract features and compare total costs, data rights and actual incremental gains. |
| Blended advisory workflow | Working proposal: integrate existing data and proven software with company drilling expertise, with no autonomous steering. |

**H2 [Judgment, provisional]:** A cross-functional redesign of the well-planning and operational workflow is proposed. Horizon placement must reflect the selected workflow and adoption cycle, not a desire to rebalance the portfolio. HSE and drilling experts retain operational authority.

#### 3. Scope and incremental benefit formula

**Annual assumptions at full scale:** two eligible operated rigs/campaigns; six avoidable rig-days per rig per year; $0.400m/day fully avoidable gross spread cost; 80% assumed economic share × 75% payment avoidability = 60% combined realization. These are **not verified company figures**. Both factors are explicit hypotheses for the same eligible campaigns, not verified contract terms. Do not apply ownership a second time. If the actual economic share is 40%, otherwise unchanged benefit halves to $1.440m/year, below the approximately $1.660m break-even reference.

`2 rigs × 6 days/rig/year × $0.400m/day × 60% = $2.880m/year` gross incremental cash **[Calculation on assumptions]**. Verify invoices, full rate composition, actual rig release rights, partner allocation and whether the company already planned the saving. Any time saving without reduced cash payment is reported as capacity or schedule value, not this cash benefit. Avoid overlap with existing procurement savings and the existing savings plan.

#### 4. Costs, data and timing

Amounts **$m**, nominal; calendar and procurement terms are assumptions. The one-time investment is **$1.4m**: $0.8m assumed capitalised integration/software ($0.4m Y0 + $0.4m Y1) and $0.6m of one-time integration, commissioning and training expense in Y1. Confirm the accounting treatment and reuse of existing platforms. Recurring software, data engineering, contractor support and run cost are assumed at $0.30m, $0.45m, $0.50m, $0.50m, $0.50m in Y1–Y5.

Assumed benefit ramp: 0%, 30%, 70%, 100%, 100% in Y1–Y5. This assumes a pilot, followed by conditional release, not autonomous operation. The model assumes a 25% cash-tax rate, straight-line depreciation of $0.8m over five years from Y1 and no immediate credit for annual losses; actual jurisdiction, ownership and tax terms must be confirmed. No terminal value or country premium is assumed separately.

**Hard dependencies:** rights to selected drilling data, contractor integration, operator consent, safely bounded advisory workflow and finance access to invoices. Cognite on operated assets is an existing foundation, not a promise that a specific rig is connected on a chosen date. Well engineering lead and contractor representatives own validation.

#### 5. Reconciled cash and scenarios

Amounts USD m.

Downside assumes 80% of full-scale benefits, 110% of investment and operating costs, and a slower 0% / 25% / 60% / 90% / 100% benefit ramp. Upside assumes 115% of full-scale benefits and accelerates the base ramp by 15%, capped at 100%, at base costs. The 11% hurdle is a project screening assumption.

| Base cash flow | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 |
| --- | --- | --- | --- | --- | --- | --- |
| Gross benefit | 0.0000 | 0.0000 | 0.8640 | 2.0160 | 2.8800 | 2.8800 |
| Operating and launch expense | 0.0000 | -0.9000 | -0.4500 | -0.5000 | -0.5000 | -0.5000 |
| CAPEX | -0.4000 | -0.4000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Cash tax | 0.0000 | 0.0000 | -0.0635 | -0.3390 | -0.5550 | -0.5550 |
| Net cash | -0.4000 | -1.3000 | 0.3505 | 1.1770 | 1.8250 | 1.8250 |

| Scenario | NPV at project hurdle | IRR | Simple payback |
| --- | ---: | ---: | ---: |
| Downside | +0.415 | 18.4% | 3.94 years |
| Base | +1.859 | 43.2% | 3.09 years |
| Upside | +2.791 | 57.4% | 2.69 years |

#### 7. Sources, limitations and challenge

- SRC-037 / CLM-077: Mero operator and 2025 participation; not evidence of operated two-rig scope.
- SRC-008 / CLM-019: Cognite partnership, announced deployment scope; not proof that the selected rigs or advisory tool are ready.
- SRC-025 / CLM-068: BP's well-planning example; no TotalEnergies savings or cash entitlement can be inferred.
- Project hurdle: `work/finance/discount_rate_policy.md`. Recompute in the replacement workbook and verify scope, actual contracts, tax, prices, timeline and scenarios. The main CEO question is whether rig-day savings reduce payments under the actual contract.


**Cost allocation:** The detailed planning allocation of this existing envelope across equipment, integration, training, staff and recurring support is maintained in the [full report](../../deliverables/report/full_strategy_report_draft.md#cost-composition-of-the-four-featured-cases). It is an indicative breakdown, not additional spending.
