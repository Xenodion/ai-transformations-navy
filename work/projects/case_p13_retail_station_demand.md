# P13 — Retail demand forecasting and dynamic pricing

**Status:** Rebuilt working case, 10 November 2026. Project and scenario figures are assumptions unless explicitly identified as facts or local observations; they require financial and operational validation before submission. The active scenario calculations are in `../finance/portfolio_model_14_revised.xlsx`. The decision does not yet authorise deployment.

## 1. Decision and existing situation

**Proposal [Assumption]:** Pilot demand forecasting and replenishment assistance with electronic shelf labels and controlled dynamic markdowns in 100 large company-operated French service stations. A successful pilot may justify a separately approved expansion. The pilot does not assume the 800- or 1,500-station footprint of the discarded draft.

**Calibration [Assumption]:** For this proposed case, Vincent suggests an indicative **€1m investment for 100 large French COCO stations, including electronic labels**, and a **2–3 year payback objective** (CLM-078, CLM-079). These are inputs informed by local experience, not evidence of an actual project, company budget or realised result. Scope, contracts and operational baseline require validation.

The programme is presented as a **proposed pilot**. Before investment, map existing retail capabilities and funded initiatives, so the business case counts only incremental costs and benefits. TotalEnergies' worldwide retail footprint is not used as the pilot denominator (SRC-002 p.13). The comparative baseline retains existing replenishment, pricing, staff and systems.

## 2. Problem, alternatives and horizon

**Problem [Hypothesis]:** Store-level volatility creates avoidable perishable losses, out-of-stocks and urgent deliveries; static ordering and pricing may not capture local traffic and seasonality. Actual losses and baseline performance across the 100 stores are unknown.

| Alternative | Approach | Decision rationale |
| --- | --- | --- |
| Existing process | Current ordering, promotions and local adjustments continue | Counterfactual. Measure its actual outcomes; do not assume it is ineffective. |
| Forecast only | Improve orders and stock visibility; no new labels | Lower hardware spend may make this preferable. Compare pilot cost and benefits before selection. |
| Forecast + labels | Forecast demand and apply approved markdown recommendations using electronic labels | Working base case: combines the proposed pilot's components. Each label/markdown gain must be incremental to forecasting. |
| Manual rules | Improve min/max thresholds and expiry rules without ML | Benchmark on the same stores and outcomes; AI is justified only if it adds measurable net value over this option. |

**H1 rationale [Judgment]:** Improve an existing retail workflow for existing customers using established methods. Forecasts and prices remain subject to human control and pricing rules; the first validated benefit is targeted within the pilot, not assumed before it operates.

## 3. Scope, dependencies and implementation

- **Scope:** 100 selected French company-operated stores. Verify stock ownership, price authority, POS coverage and category mix before funding.
- **Hard dependencies:** permission to use station/SKU sales and stock history; an eligible POS and label interface; a process for updating shelf prices; data-protection and commercial review. Existing pricing systems and pre-funded label costs are part of the baseline, not repurchased.
- **Soft dependencies:** weather and traffic feeds. Begin with a representative pilot if they are unavailable; do not wait for a group-wide data platform.
- **Delivery [Assumption]:** a branch retail owner, data engineer and data scientist work with station managers and finance; buy/partner for label hardware, integrate with existing systems, and build or configure the forecasting layer. Contract terms and data rights determine the final sourcing choice.
- **Timeline [Assumption]:** Y0 late 2026 decision and setup; Y1 pilot rollout and baseline validation; Y2 expand to the eligible 100 stores after a successful gate; Y3–Y5 operate and measure. These are hypothetical model periods.

## 4. Investment and operating costs

Amounts are **€m**, nominal. The €1m one-time investment, allocation, timing, CAPEX treatment and recurring costs are business-case assumptions, not a company quotation. The split must be tested against the proposed scope and supplier contracts.

| Cost item | Y0 | Y1 | Total one-time | Treatment assumed |
| --- | ---: | ---: | ---: | --- |
| Electronic labels, connectivity and eligible software | 0.400 | 0.400 | 0.800 | Capital expenditure, depreciated evenly over five years from Y1 for illustration. |
| Integration, installation and initial training | 0 | 0.200 | 0.200 | One-time operating expense in Y1. |
| **Total one-time investment** | **0.400** | **0.600** | **1.000** | Includes labels; do not add them a second time. |

Incremental recurring cloud, data, support and store enablement are assumed at €0.060m in Y1, €0.100m in Y2 and €0.120m/year in Y3–Y5, separate from the €1m. Verify supplier fees, replacement hardware, internal capacity and backfill. No expansion cost or benefit beyond the 100 sites is included.

## 5. Benefit drivers and evidence

All following amounts are **assumptions**, not reported Argedis results. They are per year at full adoption and refer to the same 100-site perimeter. Finance must verify the baseline and the incremental effect using comparable stores and seasonality before crediting cash.

| Non-overlapping lever | Formula | Annual gross benefit |
| --- | --- | ---: |
| Perishable waste reduction | 100 stores × €350,000 perishable sales/store × 70% inventory cost/sales × 4% baseline waste × 25% reduction | €245,000 |
| Dynamic markdowns | 100 stores × 1,000 **distinct, non-overlapping** at-risk items/store × €2 incremental net recovery | €200,000 |
| Fewer stock-outs | 100 stores × €50,000 baseline missed sales/store × 8% recovered × 35% incremental contribution margin | €140,000 |
| Urgent deliveries avoided | 100 stores × 80 baseline urgent deliveries/store/year × 50% reduction × €60 variable cost/delivery | €240,000 |
| **Total** | Sum of distinct cash drivers | **€825,000/year** |

The 1,000 markdown items must be excluded from the waste-reduction pool; if not, subtract the overlap. The assumption of 80 urgent deliveries per store and a 50% reduction is material and must be tested against invoices and store data. Missed sales, avoidable deliveries, the €2 recovery and the 35% margin must be evidenced by station data and supplier contracts. Savings from released inventory working capital are excluded until a separate balance-sheet bridge proves they are incremental and not recurring earnings.

The model assumes realised benefit ramps to 50% of full scale in Y1, 80% in Y2 and 100% in Y3–Y5. A 25% cash-tax rate and five-year straight-line depreciation of the assumed €0.8m capitalised portion are scenario assumptions; losses generate no immediate tax credit. The applicable tax base, treatment of software and timing must be checked before an investment decision.

## 6. Five-year cash flow and J-curve

**Base [Calculation on assumptions]**, €m. Y0 is the end-2026 decision point; Y1–Y5 are annual model periods. Depreciation is not a cash outflow; it reduces taxable operating surplus. No terminal value is assumed.

| €m | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Gross incremental benefit | 0 | 0.4125 | 0.6600 | 0.8250 | 0.8250 | 0.8250 |
| Recurring operating cost | 0 | -0.0600 | -0.1000 | -0.1200 | -0.1200 | -0.1200 |
| One-time implementation expense | 0 | -0.2000 | 0 | 0 | 0 | 0 |
| Capital expenditure | -0.4000 | -0.4000 | 0 | 0 | 0 | 0 |
| Cash tax | 0 | 0 | -0.1000 | -0.13625 | -0.13625 | -0.13625 |
| **Net incremental cash** | **-0.4000** | **-0.2475** | **0.4600** | **0.56875** | **0.56875** | **0.56875** |
| **Cumulative net cash** | **-0.4000** | **-0.6475** | **-0.1875** | **0.38125** | **0.9500** | **1.51875** |

At the fixed P13 hurdle of **9%** (`../finance/discount_rate_policy.md`), the model produces NPV **+€0.972m**, IRR **49.5%**, simple payback **2.33 years**, and discounted payback **2.55 years**. Paybacks interpolate annual cash uniformly and are not observed month-by-month. The result is consistent with the assumed 2–3 year target, but does not validate the inputs.

## 7. Scenarios, hurdle and sensitivities

The downside assumes 90% of the base benefit and 105% of initial and recurring costs. P13 also uses slower 35% / 60% / 80% / 100% / 100% adoption; other cases retain their base ramp. Upside assumes 115% benefits and base costs; P13 uses 65% / 90% / 100% / 100% / 100% adoption. These are illustrative assumptions, not observed probabilities. A separate severe stress uses 65% benefits and 120% costs. Actual stop costs, delays, contract terms and attribution must be validated before approval.

| Scenario | NPV at project hurdle | IRR | Simple payback (years) |
| --- | ---: | ---: | ---: |
| Downside | €+0.422m | 24.8% | 3.32 |
| Base | €+0.972m | 49.5% | 2.33 |
| Upside | €+1.434m | 72.1% | 1.81 |

## 8. Gates, adoption and decision rights

| Gate | Owner | Evidence / action |
| --- | --- | --- |
| Baseline and permission, before spend | M&S sponsor, station representatives, finance, IT | Agree 100 eligible stores, existing capabilities and spend, baseline, treatment/control design, data rights, accounting scope and exact €1m components. |
| Pilot validation, Y1 | Retail product owner, station managers, finance | Track forecast accuracy, inventory losses, markdown event ledger, lost sales, urgent-delivery invoices, adoption and customer impact against comparable stores. Pre-agree sample, threshold and observation window; no assumed 100-store expansion if evidence fails. |
| Scale release, Y2 | M&S sponsor and finance | Release the next stage only if a prospective after-tax business case clears 9% and operational/safety conditions are met. Assess a forecast-only alternative. |
| Stop | Sponsor with finance | Stop or redesign if agreed outcomes fail; retain already incurred costs, contract commitments and exit costs. Do not assume all unspent budget is recoverable. |

Station staff must retain pricing oversight, receive training during working hours and have a feedback route; ensure no unsafe expiry practices and involve employee representatives when applicable. Baselines, thresholds and detailed worker time remain to be established.

**Illustrative financial threshold [Calculation]:** with base costs, timing and tax unchanged, the five-year NPV at 9% reaches zero at about **€0.446m/year of realised gross benefit at full scale**, or 54.0% of the assumed €0.825m. This is not a measured store target. Before further funding, finance should use observed store-level incremental cash and the *remaining* avoidable costs to test whether the prospective continuation case clears 9%.

## 9. Sources, limits and next validation

- **CLM-078 / CLM-079:** Vincent's calibration guidance for the hypothetical case: ~€1m including labels for 100 stations and a 2–3-year target. Neither is a company filing or a verified actual result.
- **SRC-002 p.13 / CLM-066:** group service-station footprint, context only; it does not establish the 100-store pilot's sales or loss levels.
- **Rate:** `../finance/discount_rate_policy.md`, P13 9% assumed project hurdle on a 7% group impairment WACC reference.
- **Calculation:** `../finance/portfolio_model_14_revised.xlsx` and the independent cash-flow checks. Base annual amounts and the break-even sensitivity are illustrative; scenario definitions in the older Python retail model are superseded by the spreadsheet.
- **Open:** validate cost allocation, supplier contracts, data availability, station mix, contribution margins, tax, labour and baseline. The 100-store scope, €1m investment, 2–3 year objective, benefit drivers and future cash are assumptions for the hypothetical case.
