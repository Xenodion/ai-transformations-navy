# WACC and hurdle rates: branch reference and project adjustments

**Fixed working policy — 10 November 2026.** This document is the single rate reference for the complete candidate portfolio. It supersedes the earlier project-only grid, the old 7.5% WACC and all rates in the unreconciled financial workbook. The values below are fixed modeling assumptions, not TotalEnergies' published investment policy. Revisit only if a project's scope or evidence materially changes; record and propagate any change.

## 1. What TotalEnergies actually publishes

**[Fact]** TotalEnergies' FY2025 consolidated accounts use a **7.0% post-tax WACC estimate** to discount the specified impairment-test cash flows, calculated from historical market data. The corresponding estimate was 7.0% in 2024 and 8.0% in 2023. Local source: `sources/primary/totalenergies_universal-registration-document-2025_2026_en.pdf`, PDF and printed pp. 462 and 472 (SRC-002, CLM-075). This does not establish a current market WACC or the group's investment hurdles.

**[Unknown]** Publicly verified branch-specific WACCs and AI hurdle rates. Consequently, the 7.0% column in the first table is the **same group proxy applied to each branch**; it is not evidence that each branch has a published WACC of 7%. The branch risk premiums, branch reference hurdles and project adjustments are **our own assumptions**.

The local `sources/primary/totalenergies_factbook-2025_2026_en.xlsx`, sheet `Avg. cap. emplyd. & ROACE (p24)`, reports group and segment ROACE. ROACE is not WACC and cannot be substituted for a discount rate. The URD's 7%–14% **pre-tax** impairment rates are also not directly comparable to the post-tax hurdles below. The course deck (SRC-033, combined PDF p. 107) presents +2 to +6 percentage points as typical AI-project practice, set case by case; it is guidance, not an official TotalEnergies rate.

## 2. Branch-level reference grid

All percentages are **nominal annual post-tax**. `pp` means percentage points. These references express relative risk for a representative AI project in each branch. Project-specific adjustment comes afterward; it is not another WACC. The portfolio's actual projects may span several currencies and jurisdictions, so check cash-flow currency, ownership and tax before applying the grid.

| TotalEnergies business branch | Group WACC proxy | Assumed branch premium | Branch reference hurdle | Reason for relative reference |
| --- | ---: | ---: | ---: | --- |
| Exploration & Production | 7.0% | +3.0 pp | **10.0%** | Offshore and upstream operating constraints, contractor interfaces and execution exposure. |
| Integrated LNG | 7.0% | +2.5 pp | **9.5%** | Physical supply-chain integration, contractual dependencies and market exposure. |
| Integrated Power | 7.0% | +2.5 pp | **9.5%** | Operational and market integration, asset data and adoption risks. |
| Refining & Chemicals | 7.0% | +2.5 pp | **9.5%** | Industrial site integration, operational safety and maintenance windows. |
| Marketing & Services | 7.0% | +2.0 pp | **9.0%** | Established retail workflows, with POS integration and frontline adoption risk. |
| Corporate / Group functions | 7.0% | +2.0 pp | **9.0%** | Common digital delivery, organizational adoption and governance risk. |

**Important:** Corporate / Group functions is shown for enterprise projects; it is not one of the five operating segments. HSE and OneTech / R&D are cross-functional perimeters, not additional group business branches. For cross-functional candidates below, Corporate's 9.0% is a transparent starting reference and the specific additional risk is stated per project; actual sponsorship and benefit attribution remain to be confirmed.

## 3. Fixed project-level hurdle grid: all candidates

`Project hurdle = branch reference hurdle + project-specific adjustment`. Adjustments express risk relative to the representative branch project. They are deliberately not tuned to a target NPV or IRR. All values are assumptions applying to the currently described scope; the horizon classification and project scope are resolved separately in project selection.

| ID | Candidate | Branch / reference | Group WACC proxy | Branch premium | Project adjustment | **Project hurdle** | Specific rationale |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| P01 | Refining predictive maintenance | Refining & Chemicals / 9.5% | 7.0% | +2.5 pp | +0.0 pp | **9.5%** | Representative brownfield industrial use; site rollout and integration are already in the branch reference. |
| P02 | Upstream production surveillance | E&P / 10.0% | 7.0% | +3.0 pp | +0.0 pp | **10.0%** | Typical operated-asset data and production-workflow integration risk. |
| P03 | Deepwater drilling advisory | E&P / 10.0% | 7.0% | +3.0 pp | +1.0 pp | **11.0%** | Additional deepwater contractor, operator/partner approval and cash-attribution uncertainty. |
| P04 | Renewable fleet availability | Integrated Power / 9.5% | 7.0% | +2.5 pp | +0.5 pp | **10.0%** | Additional multi-OEM telemetry and dispersed-fleet execution risk. |
| P05 | Copilot workflow redesign | Corporate / 9.0% | 7.0% | +2.0 pp | +0.0 pp | **9.0%** | Established software; ordinary workflow adoption and license-realisation risk. |
| P06 | Procurement analytics | Corporate / 9.0% | 7.0% | +2.0 pp | +0.5 pp | **9.5%** | Additional supplier-data, sourcing and benefit-attribution complexity. |
| P07 | Safety computer vision | Corporate / 9.0% (cross-functional HSE) | 7.0% | +2.0 pp | +1.0 pp | **10.0%** | Additional site safety, privacy and acceptance requirements. |
| P08 | Power and gas customer retention | Integrated Power / 9.5% | 7.0% | +2.5 pp | +0.0 pp | **9.5%** | Representative customer-data and adoption risk for the branch. |
| P09 | LNG voyage optimisation | Integrated LNG / 9.5% | 7.0% | +2.5 pp | +0.5 pp | **10.0%** | Additional controlled-voyage, charter and route-execution uncertainty. |
| P10 | Steam-cracker optimisation | Refining & Chemicals / 9.5% | 7.0% | +2.5 pp | +0.5 pp | **10.0%** | Additional process integration and operational safety constraints. |
| P11 | Customer-side flexibility | Integrated Power / 9.5% | 7.0% | +2.5 pp | +1.5 pp | **11.0%** | Additional enrolment, dispatch, market-access and business-model risk; conditional H3 illustration only. |
| P12 | e-SAF catalyst discovery | Corporate / 9.0% (cross-functional OneTech R&D) | 7.0% | +2.0 pp | +3.0 pp | **12.0%** | Additional scientific, scale-up and commercialisation uncertainty; conditional H3 illustration only. |
| P13 | Retail demand forecasting | Marketing & Services / 9.0% | 7.0% | +2.0 pp | +0.0 pp | **9.0%** | Representative retail adoption and POS risk; proposed pilot assumes 100 French COCO stations, per CLM-078. |
| E01 | AI value register | Corporate / 9.0% | 7.0% | +2.0 pp | +0.0 pp | **9.0%** | Representative enterprise governance and adoption risk. Include its costs in the programme. |

The full list covers P01–P13 and E01, including reserve candidates. Rates are set even if a candidate is not funded; this does not imply its costs or returns are included in the base portfolio. P12 carries a total +5 pp premium, demonstrating that the reference grid permits high-risk options. A further +6 pp / 13% rate is possible for a specifically justified project, but is not assigned automatically. P11/P12 rates are applicable to clearly labelled conditional commercial illustrations, not evidence that the H3 options have a defensible payback.

## 4. Calculation and decision rules

1. Apply each project hurdle to the project's **incremental nominal post-tax unlevered cash flows** on the same period, currency and ownership basis. Explicitly model operating expenses, capital expenditure, depreciation and cash taxes, working capital and the programme counterfactual. Do not combine a post-tax hurdle with pre-tax cash flows.
2. For conventional H1/H2 cases, calculate NPV, project IRR and discounted payback at the project rate; an IRR must be compared to that same hurdle. If no IRR or payback exists, report it. A base case that clears the hurdle by a modest, plausible margin is acceptable; no target return is imposed.
3. For H3, include authorised learning costs in the programme and use learning milestones and option value. A commercial NPV or IRR may be shown only as an explicitly conditional illustration with its project hurdle; do not invent H3 payback or book speculative proceeds as assured base cash.
4. For a portfolio NPV, sum appropriately attributed project NPVs at their project hurdles, counting shared costs once. If a single-rate portfolio comparison is desired, choose and disclose a separate common rate; an investment-weighted average hurdle is not generally equivalent to the sum of NPVs at different rates. Portfolio IRR is calculated from consolidated dated cash flows; its comparison hurdle must be separately defined and justified, not averaged silently.
5. Sensitivity: vary the common WACC proxy to **6%, 7%, 8%** while retaining the branch and project premiums. For example P01 uses 8.5%, 9.5%, 10.5%; P03 uses 10%, 11%, 12%; P13 uses 8%, 9%, 10%; conditional P11 uses 10%, 11%, 12%; conditional P12 uses 11%, 12%, 13%. Also vary operational drivers, timing and costs separately. These are team sensitivity assumptions, not sourced 2026 market rates.
6. No blanket country surcharge is added. If material country risk is not already captured in project cash scenarios or the project premium, identify it and justify a separate adjustment, avoiding double counting.

**Implementation status:** the old workbook and core-only portfolio scenario are superseded. `portfolio_model_14_revised.xlsx` is a working, editable 14-initiative model using this grid and the 100-station retail pilot. Its assumptions, portfolio overlap and H3 treatment still require review before use in the report, memo or slides.
