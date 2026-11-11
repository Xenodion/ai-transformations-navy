# Portfolio sequencing canvas

**Status:** Rebuild pending completion and review of the four featured cases and the short cards for all remaining candidates. [Issue #17](https://github.com/Xenodion/ai-transformations-navy/issues/17) remains open. The previous charts and envelope were removed from active use because they contained unreconciled and unsupported figures; tracked versions remain in Git history.

The candidate list comprises P01–P13 plus E01. Project descriptions and existing-capability leads are in [long list](long_list.md); refreshed assumptions, horizons and economics take precedence when the cards are completed. Use [discount rate policy](../finance/discount_rate_policy.md) for the branch and project hurdles.

| Required field | Rule for the rebuilt canvas |
| --- | --- |
| Project and horizon | Explain classification from the course questions; distinguish unapproved options from committed work. |
| Funding and capital mix | Show the defined authorization envelope and reconcile to 100%; distinguish reserve ceilings from released and paid amounts. |
| Dependencies | Specify the minimum use-case-specific slice, identify hard versus soft dependencies and avoid linking unrelated projects artificially. |
| Sourcing | Build, buy or blend, with the existing company capability as the starting point. |
| Milestones and decision owner | Give an owner, date, measurable result and condition for each release. |
| Value | Match amount, units, cash timing, costs, tax and uncertainty to the case; exclude unsupported H3 paybacks. |

## Reconciled working visuals

The figures below use the cached results of [`portfolio_model_14_revised.xlsx`](../finance/portfolio_model_14_revised.xlsx), including all 14 initiatives. They are reproducible assumptions-based decision visuals, not company forecasts. [Visual methods and reconciliation](portfolio_visuals.md) states exactly what each axis, area and mix means.

- [Portfolio bubble map](assets/notebook_portfolio_bubble.png). All initiatives share the same time-to-scale and gross-potential axes; these do not represent payback. The H3 points use explicit, unverified long-term assumptions.
- [Three investment and value mixes](assets/notebook_portfolio_mix.png). The third bar is a separate hypothetical 15-year net-value illustration; its H3 scale, cost and probability assumptions are editable and unverified.
- [Net value contribution by horizon](assets/notebook_net_contributions.png). H3 and E01 are negative within the modelled five years; they are not converted into misleading positive shares.
- [14-initiative J-curve](assets/notebook_portfolio_jcurve.png); each of the four project cards links its own scenario J-curve. All visuals are generated in [one notebook](portfolio_charts.ipynb).

The scope, incremental overlap, hurdle-premium interpretation and H3 commercial assumptions remain subject to evidence review. Longer-term H3 value is not captured by the five-year gross-benefit bar. Do not copy values from the historical long list or use the course's illustrative horizon mix as a forecast.

## Working sequencing canvas — all 14 initiatives

**Planning assumptions, 10 November.** Proposed roles, milestones, sourcing and dependency classifications are not company commitments. A hard dependency is required for the first safe and lawful test; a soft dependency improves scale but need not delay a narrow pilot. Each milestone is due by the end of the stated model year. Y0 is the decision/preparation period; actual calendar dates and owners remain to be agreed. Shares below use the existing $11.2665m one-time modelled investment (CAPEX plus launch) and include E01 once. A share is not a released budget; modelled recurring OPEX and tax are outside this denominator. Percentages are rounded and may not sum to precisely 100%. Build/buy/blend choices are proposals subject to procurement and security checks, not claims about current contracts.

| ID / horizon | Capital share | Minimum hard dependency; soft dependency | Proposed sourcing | Accountable role; first measurable milestone and release condition |
| --- | ---: | --- | --- | --- |
| P01 / H1 | 12.43% | Hard: permission and time-stamped failure and maintenance data for a pilot asset; soft: wider AspenTech integration. | Blend existing platform with site-specific models | Refinery operations lead; Y1 approved baseline and matched intervention log; no release without safe access and signed baseline. |
| P02 / H1 | 7.99% | Hard: operated hub and well telemetry access; soft: integration across additional hubs. | Blend existing data platform and surveillance workflow | Upstream asset lead; Y1 pilot well baseline and exception log; pause without operational ownership. |
| P03 / H2 | 12.43% | Hard: operated campaign, contractor access and cash-releasing contract terms; soft: multi-rig data integration. | Blend internal expertise and contractor tools | Drilling operations lead; Y1 contract and eligible campaign confirmed; no live pilot without operator and safety approval. |
| P04 / H1 | 3.55% | Hard: fleet telemetry and dispatch rights; soft: cross-OEM integration. | Blend OEM monitoring with common analytics | Renewables operations lead; Y1 pilot-asset availability baseline; pause absent data and attribution rights. |
| P05 / H1 | 2.66% | Hard: actual licence inventory and cancellation rights; soft: wider workflow redesign. | Buy existing productivity tooling; configure workflows | Corporate productivity lead; Y1 verified licence baseline and cancellable scope; no saving booked without a cancelled invoice. |
| P06 / H1 | 4.44% | Hard: eligible contract/spend data and procurement authority; soft: supplier-wide integration. | Blend procurement software with business rules | Procurement lead; Y1 baseline for one spend category and signed exclusion of existing savings; pause if attribution is impossible. |
| P07 / H1 | 5.33% | Hard: site HSE, privacy and workforce approvals and baseline; soft: deployment at other sites. | Blend existing safety systems with approved vendor tools | HSE lead; Y1 safety and privacy review plus near-miss measurement protocol; stop unsafe or unapproved use; no incident cash booked. |
| P08 / H1 | 5.33% | Hard: eligible customer cohort, data consent and margin baseline; soft: additional channels. | Blend customer tooling with retention analytics | Customer business lead; Y1 matched-cohort and contribution baseline; pause without legal approval or a control group. |
| P09 / H2 | 4.44% | Hard: controlled voyage data and charter fuel-cost entitlement; soft: fleet-wide integrations. | Blend existing routing tools and analytics | LNG shipping lead; Y1 controlled-voyage baseline and contract review; pause without attributable fuel costs. |
| P10 / H1 | 6.66% | Hard: safe plant data access and process-owner approval; soft: model transfer across plants. | Blend process expertise with site analytics | Chemicals operations lead; Y1 yield baseline and P01 overlap check; no scale without positive prospective economics and safety approval. |
| P11 / H3 | 13.31% | Hard: customer consent, market access and independent offer definition versus Quadra; soft: additional asset classes. | Blend commercial partnership and existing trading capability | Integrated Power venture lead; Y1 customer and market-access test; release only the next learning tranche if novelty and access are substantiated. |
| P12 / H3 | 8.88% | Hard: lab access, eligible scientific hypothesis and IP rights; soft: scale-up partnerships. | Blend internal research and specialist partner | OneTech R&D lead; Y1 registered screening protocol and reproducibility baseline; stop if laboratory or IP permissions fail. |
| P13 / H1 | 9.91% | Hard: hypothetical store POS data, stock ownership and matched-store permission; soft: expansion to further categories and labels. | Blend existing POS with forecasting and label suppliers | Retail operations lead; Y1 matched-store baseline and stock-ownership review; no rollout without attributable results and employee training. |
| E01 / shared | 2.66% | Hard: Finance-approved value definitions and model-owner inventory for pilot scope; soft: enterprise-wide automated feeds. | Blend existing registers and a common reporting layer | Group Finance / AI governance lead; Y1 pilot register with named owners and finance sign-off; avoid duplicating existing tools. |

Capital denominator is the modelled one-time envelope, not the five-year gross ceiling. Proposed pilot milestones are evidence gates, not claims of actual delivery. The full model includes all 14 candidates, including P07 and P10; the table does not approve any one of them. At G0, classify the precise data slice, confirm sourcing and contract rights, and assign a person and fiscal date. Continue with the project only when its remaining prospective case, safety and acceptance criteria support release; keep incurred and non-cancellable costs on a stop.
