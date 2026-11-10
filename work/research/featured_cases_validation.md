# Featured-case validation record

**Date:** 10 November 2026. **Status:** Arithmetic verified; economic and operational assumptions remain unverified. This is not approval to close issues 12–15 or a representation of TotalEnergies actuals.

## Arithmetic and hurdle checks

The project models calculate net cash as `incremental benefit − recurring OPEX − one-time expensed implementation − CAPEX − cash tax`. The documented tax calculation assumes 25% on positive taxable profit, five-year straight-line depreciation of assumed eligible capital assets, no immediate tax credit for losses and no terminal value. These conventions are assumptions; accounting eligibility, taxes and currency/ownership are not independently established. `test_featured_case_reconciliation.py` independently discounts the documented annual flows and verifies the project rates against the fixed policy. The wider test suite checks stopping, assumptions and case mathematics.

| Case | Model currency | Hurdle | Base NPV at 1 pp lower / fixed / 1 pp higher | Base IRR | Interpretation |
| --- | --- | ---: | --- | ---: | --- |
| P01 | USD m | 9.5% | +2.219 / +2.116 / +2.017 | 57.8% | Numerical calculation only; two-site throughput and incremental margin need validation. |
| P03 | USD m | 11.0% | +1.972 / +1.859 / +1.752 | 43.2% | Numerical calculation only; operator authority, rig contracts and cash entitlement are essential. |
| P11 | USD m | 11.0% | +0.403 / +0.328 / +0.256 | 16.2% | Conditional commercial illustration, not approved H3 option value or guaranteed receipts. |
| P13 | EUR m | 9.0% | +1.022 / +0.972 / +0.924 | 49.5% | Pilot size, investment, target, benefit drivers and cost split are assumptions informed by local experience. |

P13 uses a hypothetical 100-store, approximately €1m pilot including labels (CLM-078) and a 2–3-year modelling objective (CLM-079), informed by Vincent's local experience. They do not describe an actual project or realised result. The model's 2.33-year simple and 2.55-year discounted paybacks are interpolated calculations. Currency must be converted consistently and dated before combining EUR and USD in a portfolio.

## Challenge: drivers that can change the decision

Holding each base case's cost, ramp and simplified tax assumptions fixed and scaling all gross benefits equally, the modeled zero-NPV levels are approximately **51.0%** of P01's benefits ($1.080m/year at full scale), **57.6%** of P03's benefits ($1.660m/year), **91.2%** of P11's conditional benefits ($3.418m/year), and **54.0%** of P13's benefits (€0.446m/year). These calculations are sensitivities, not observations, safe thresholds, or predictions of a loss cap. Varying costs, ramp, tax or the composition of benefits changes them.

P11 is especially sensitive: at an unchanged cost and ramp, it needs most of its assumed 250 MW and $15k/MW-year net contribution for a positive conditional NPV. Existing Quadra activity must be mapped before presenting the proposed service as new. P03 depends on two eligible operated campaigns, actual contracts that reduce invoices and the correct company share; the Mero correction does not identify a replacement asset. P01's assumed throughput and margin cannot be inferred from a group-wide refining marker. P13's assumed annual avoidable urgent deliveries and distinct markdown recoveries are substantial; overlap, stock ownership and vendor costs require evidence. None of these assumptions becomes a fact because the NPV clears a hurdle.

## Minimum validation before acceptance

1. Check selected asset/site perimeter, existing programme and operator or contracting rights for all four cases.
2. Challenge each benefit driver, adoption ramp, full recurring cost, year-zero spend and tax basis against available local sources; label any remaining assumption and its sensitivity.
3. Check each downside, actual stop/exit commitment, owner, date, baseline, threshold and release amount against the same project schedule. Current downside estimates are proportional sensitivities; they are not yet a full gate-failure analysis.
4. Independently verify the model in the replacement spreadsheet, including formulas, rates, taxes, currency conversions and the chart source. A successful Python test is not an Excel recalculation.
5. Review shared E01 and training costs and overlaps with the other candidates; then determine the authorised portfolio and update its issues and roadmap when acceptance criteria genuinely pass.

Until these checks pass, the project documents and workbook visuals remain working material, not final slide content.
