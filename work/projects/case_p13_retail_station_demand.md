### 6.4 P13 — French retail demand and controlled markdowns (H1)

**Status:** Working case aligned with the financial model on 11 November 2026. All financial inputs are planning assumptions; the existing operational baseline and contractual terms must be validated. Model: [working workbook](../finance/portfolio_model_working.xlsx); independent annual cash-flow check: [reconciliation](../finance/reconcile_selected.py).

#### 1. Decision and existing situation

**Proposal [Assumption]:** Pilot demand forecasting and replenishment assistance with electronic shelf labels and controlled dynamic markdowns in 100 large company-operated French service stations. A successful pilot may justify a separately approved expansion. The pilot does not assume the 800- or 1,500-station footprint of the discarded draft.

**Calibration [Local observation]:** Our insider, drawing on French retail network experience, suggests an indicative **€1m investment for 100 large French company-operated stations, including electronic labels** (CLM-078, CLM-079). This informs our assumptions; it is not evidence of an actual project, company budget or realised result.

The programme is presented as a **proposed pilot**. Before investment, map existing retail capabilities and funded initiatives, so the business case counts only incremental costs and benefits. TotalEnergies' worldwide retail footprint is not used as the pilot denominator (SRC-002 p.13). The comparative baseline retains existing replenishment, pricing, staff and systems.

#### 2. Problem, alternatives and horizon

**Problem [Hypothesis]:** Store-level volatility creates avoidable perishable losses, out-of-stocks and urgent deliveries; static ordering and pricing may not capture local traffic and seasonality. Actual losses and baseline performance across the 100 stores are unknown.

| Alternative | Approach | Decision rationale |
| --- | --- | --- |
| Existing process | Current ordering, promotions and local adjustments continue | Counterfactual. Measure its actual outcomes; do not assume it is ineffective. |
| Forecast only | Improve orders and stock visibility; no new labels | Lower hardware spend may make this preferable. Compare pilot cost and benefits before selection. |
| Forecast + labels | Forecast demand and apply approved markdown recommendations using electronic labels | Working base case: combines the proposed pilot's components. Each label/markdown gain must be incremental to forecasting. |
| Manual rules | Improve min/max thresholds and expiry rules without ML | Benchmark on the same stores and outcomes; AI is justified only if it adds measurable net value over this option. |

**H1 rationale [Judgment]:** Improve an existing retail workflow for existing customers using established methods. Forecasts and prices remain subject to human control and pricing rules; the first validated benefit is targeted within the pilot, not assumed before it operates.

#### 3. Scope, dependencies and implementation

- **Scope:** 100 selected French company-operated stores. Verify stock ownership, price authority, POS coverage and category mix before funding.
- **Hard dependencies:** permission to use station/SKU sales and stock history; an eligible POS and label interface; a process for updating shelf prices; data-protection and commercial review. Existing pricing systems and pre-funded label costs are part of the baseline, not repurchased.
- **Soft dependencies:** weather and traffic feeds. Begin with a representative pilot if they are unavailable; do not wait for a group-wide data platform.
- **Delivery [Assumption]:** a branch retail owner, data engineer and data scientist work with station managers and finance; buy/partner for label hardware, integrate with existing systems, and build or configure the forecasting layer. Contract terms and data rights determine the final sourcing choice.
- **Timeline [Assumption]:** Y0 late 2026 decision and setup; Y1 pilot rollout and baseline validation; Y2 expand to the eligible 100 stores after a successful gate; Y3–Y5 operate and measure. These are hypothetical model periods.

#### 4. Investment and operating costs

Amounts are **€m**, nominal. The €1m one-time investment, allocation, timing, CAPEX treatment and recurring costs are business-case assumptions, not a company quotation. The split must be tested against the proposed scope and supplier contracts.

| Cost item | Y0 | Y1 | Total one-time | Treatment assumed |
| --- | ---: | ---: | ---: | --- |
| Electronic labels, connectivity and eligible software | 0.400 | 0.400 | 0.800 | Capital expenditure, depreciated evenly over five years from Y1 for illustration. |
| Integration, installation and initial training | 0 | 0.200 | 0.200 | One-time operating expense in Y1. |
| **Total one-time investment** | **0.400** | **0.600** | **1.000** | Includes labels; do not add them a second time. |

Incremental recurring cloud, data, support and store enablement are assumed at €0.060m in Y1, €0.100m in Y2 and €0.120m/year in Y3–Y5, separate from the €1m. Verify supplier fees, replacement hardware, internal capacity and backfill. No expansion cost or benefit beyond the 100 sites is included.

#### 5. Benefit drivers and revised financial case

All inputs are assumptions for 100 eligible stores. The central annual benefit is **€0.635m**: €0.245m waste reduction + €0.250m incremental markdown recovery + €0.140m stock-out recovery. Urgent-delivery savings are excluded until invoices establish avoidable cash.

- Waste: 100 × €350,000 perishable sales × 70% inventory cost × 4% baseline waste × 25% reduction = €245,000/year.
- Markdowns: 100 × 1,000 at-risk items × €2.50 net incremental recovery = €250,000/year. These items must be outside the waste pool. Define SKU/day cohorts and measure net margin after cannibalization, discounts and extra handling. If this cannot be demonstrated, remove the markdown stream.
- Stock-outs: 100 × €50,000 missed sales × 8% recovery × 35% contribution = €140,000/year. Measure incremental category contribution, not substitution between products.

These equations are transparent planning hypotheses, not observed baselines. A pilot must compare forecasting only, rules-based ordering and forecasting plus labels using matched stores and seasonality. The €1m remains the 100-store rollout ceiling; release only a small instrumented slice before buying all hardware.

Amounts EUR m below. Costs and the central adoption ramp are preserved.

Downside assumes 90% of full-scale benefits, 105% of investment and operating costs, and a slower 40% / 70% / 90% / 100% / 100% benefit ramp. Upside assumes 115% of full-scale benefits and accelerates the base ramp by 15%, capped at 100%, at base costs. Values in the table are in EUR millions; the portfolio converts at the model assumption of $1.1165/€. The 9% hurdle is a project screening assumption.

| Base cash flow | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 |
| --- | --- | --- | --- | --- | --- | --- |
| Gross benefit | 0.0000 | 0.3175 | 0.5080 | 0.6350 | 0.6350 | 0.6350 |
| Operating and launch expense | 0.0000 | -0.2600 | -0.1000 | -0.1200 | -0.1200 | -0.1200 |
| CAPEX | -0.4000 | -0.4000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Cash tax | 0.0000 | 0.0000 | -0.0620 | -0.0888 | -0.0888 | -0.0888 |
| Net cash | -0.4000 | -0.3425 | 0.3460 | 0.4263 | 0.4263 | 0.4263 |

| Scenario | NPV at project hurdle | IRR | Simple payback |
| --- | ---: | ---: | ---: |
| Downside | +0.144 | 14.8% | 3.77 years |
| Base | +0.485 | 30.0% | 2.93 years |
| Upside | +0.835 | 46.0% | 2.34 years |


**Attribution sensitivity:** without the €0.250m markdown stream, annual benefit falls to €0.385m, below the existing approximately €0.446m full-project break-even threshold at 9%. The case therefore requires evidence of incremental markdown value or a lower-cost forecasting-only design. It is not robust merely because all drivers are labelled assumptions. The previous delivery-saving assumption is an unbooked upside lead, not an offset to this risk.

**Release rule:** retail sponsor and Finance pre-register the matched-store protocol, baseline waste cohorts, margin and paid delivery invoices before Y0 release. Before Y2 hardware expansion, require positive prospective NPV at 9% using measured incremental margin and remaining avoidable costs. Stop hardware rollout if labels do not outperform forecasting-only after their incremental costs. Store managers retain pricing authority. Count training, installation and staff backfill inside the cost envelope or reprice the case.

**Sources and limits:** local calibration CLM-074/078/079 establishes neither a group baseline nor a realized saving. The €1m/100-store envelope is an explicit planning assumption. The source register and retail case preserve these distinctions.


**Cost allocation:** The detailed planning allocation of this existing envelope across equipment, integration, training, staff and recurring support is maintained in the [full report](../../deliverables/report/full_strategy_report.md#cost-composition-of-the-four-featured-cases). It is an indicative breakdown, not additional spending.
