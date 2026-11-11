"""Archive superseded artifacts and reconcile active navigation safely."""
from pathlib import Path
import shutil,re,json
R=Path(__file__).resolve().parents[2]; A=R/'work/archive/pre_selection_2026_11_10'
def archive(rel,move=False):
    src=(R/rel).resolve(); dst=(A/rel).resolve()
    assert src.is_relative_to(R) and dst.is_relative_to(A)
    if not src.exists():return
    dst.parent.mkdir(parents=True,exist_ok=True)
    if not dst.exists():shutil.copy2(src,dst)
    if move:src.unlink()
for rel in ['work/projects/case_p11_virtual_power_plant.md','work/projects/long_list.md','work/projects/focus_financial_tables.ipynb','work/projects/portfolio_charts.ipynb','work/finance/portfolio_model_14_revised.xlsx','work/report_completion_inputs.md']:
    archive(rel,True)
for directory in ['work/projects/assets','deliverables/report/assets']:
    for p in (R/directory).glob('notebook*'):archive(str(p.relative_to(R)),True)
for rel in ['work/options/thesis_and_selection.md','work/options/operating_model.md','work/projects/case_rebuild_decisions.md','work/governance/gates_and_adoption.md','work/finance/discount_rate_policy.md','work/projects/portfolio_sequencing_canvas.md','work/projects/portfolio_visuals.md']:
    archive(rel)
decision=(R/'work/options/selected_portfolio_decision.md').read_text()
(R/'work/options/thesis_and_selection.md').write_text(decision)
(R/'work/projects/case_rebuild_decisions.md').write_text('# Active featured cases\n\n- [P01](case_p01_refining_pdm.md)\n- [P03](case_p03_deepwater_drilling.md)\n- [P12](case_p12_esaf_licensing.md)\n- [P13](case_p13_retail_station_demand.md)\n\nSee [selection decision](../options/selected_portfolio_decision.md).\n')
(R/'work/projects/portfolio_visuals.md').write_text('# Active visual methods\n\nSee [chart production specification](chart_regeneration_spec.md). Rendering is pending. The old visual assets and notebook are archived and are not compatible with the active report.\n')
report=(R/'deliverables/report/full_strategy_report_draft.md').read_text()
(R/'work/governance/gates_and_adoption.md').write_text('# Gates and adoption\n\n'+report.split('## 9.')[1].split('## 10.')[0])
op=(R/'work/options/operating_model.md').read_text()
op=op.replace('(P11, P12)','(P12)').replace('TotalEnergies is at hub-and-spoke.','Strong hub-and-spoke is the proposed delivery arrangement; current internal decision rights remain unverified.')
(R/'work/options/operating_model.md').write_text(op)
rate=(R/'work/finance/discount_rate_policy.md').read_text()
rate=re.sub(r'^\| P(?:04|06|07|08|10|11) .*\n','',rate,flags=re.M)
rate=re.sub(r'The full list covers.*?\n\n','The grid covers the selected initiatives. H3 discounting measures learning cost, not a validated commercial option value.\n\n',rate,flags=re.S)
rate=rate.replace('e-SAF catalyst discovery','e-SAF technology licensing option').replace('conditional P11 uses 10%, 11%, 12%; ','')
rate=re.sub(r'\*\*Implementation status:\*\*.*','**Implementation status:** `portfolio_model_selected.xlsx` is the active eight-line model. See `portfolio_economics.md` for assumptions and verification.',rate,flags=re.S)
(R/'work/finance/discount_rate_policy.md').write_text(rate)
(R/'work/README.md').write_text('''# Active work

- [Roadmap](roadmap.md) and matching GitHub issues track acceptance.
- [Selection decision](options/selected_portfolio_decision.md).
- [Selected workbook](finance/portfolio_model_selected.xlsx), [economics](finance/portfolio_economics.md), [half-budget response](finance/half_envelope_alternative.md).
- [Featured cases](projects/case_rebuild_decisions.md), [sequencing](projects/portfolio_sequencing_canvas.md), [governance](governance/gates_and_adoption.md).
- [Chart production specification](projects/chart_regeneration_spec.md); graphical regeneration remains pending.
- [Full report](../deliverables/report/full_strategy_report_draft.md), source for the future memo and slides.

The previous selection, workbook, charts and decisions are preserved under `archive/pre_selection_2026_11_10/`. Historical research and old unit models are not active calculation sources. Use `build_workbook.mjs` and `reconcile_selected.py` for current figures.
''')
(A/'rejection_decisions.md').write_text('''# Retired candidates and reasons

These are archived selection decisions, not active portfolio entries. No original source document was changed.

- P04: narrow incremental value and multi-OEM/contract attribution uncertainty; defer until eligibility and a distinct gain over existing monitoring are established.
- P06: modest case with procurement overlap and incomplete separation from contractor and voyage savings; narrow scope favors operational cases with direct invoices.
- P07: current model books no financial benefit; a safety pilot can be justified separately but mandatory safety controls remain in the baseline. Do not imply safety is optional or monetize speculative avoided incidents to rescue the case.
- P08: unverified distinct customer cohort and overlap with the previous inaction narrative; no evidence-based priority over selected workflows.
- P10: negative central standalone NPV and overlap risk with refining reliability. Do not fund solely to preserve an industrial-learning label.
- P11: proposed customer flexibility may duplicate existing services and does not establish business-model novelty; commercial receipts depended on unverified scale and margin. Retired rather than forcing H3 classification.

Retained P12 is materially sharpened toward third-party technology licensing. Existing catalyst research costs are preserved as a feasibility ceiling, not evidence of licensing demand. The archive preserves the previous report and assumptions for audit.
''')
(R/'work/projects/portfolio_sequencing_canvas.md').write_text('''# Selected portfolio sequencing canvas

All roles, scopes and dates are proposed assumptions. Y0 means approval; Y1–Y5 are subsequent annual periods. Gross spend and allocation reconcile to the active workbook. Existing platforms and safety controls are in the baseline.

| ID | Minimum slice / hard dependency | Sourcing | Accountable role | First decision and scale |
| --- | --- | --- | --- | --- |
| P01 | Two eligible refining sites; sensor history, sold throughput and cash margin | Blend existing industrial platform and reliability expertise | Refining sponsor + Finance | G0 asset eligibility; Y1 supervised trial; Y2 scale only on incremental cash |
| P02 | Two production hubs; ownership, data access and distinct production events | Blend existing upstream data and surveillance tools | Upstream sponsor | Y1 event baseline; Y2 scale with sold attributable output |
| P03 | Two operated campaigns; contractor release rights and economic share | Buy/blend proven advisory and internal engineering | Drilling lead + Finance | Y0 rights; Y1 supervised trial; Y2 invoice-backed continuation |
| P05 | Existing paid licence cohort; cancellation rights and protected required functions | Existing contracts plus workflow redesign | Corporate IT + procurement | Y1 cohort test; Y2 remove only documented redundant expense |
| P09 | 30 eligible voyages; charter control, fuel entitlement, weather/route data | Buy/blend existing routing capability | LNG operations + Finance | Y1 baseline; Y2 controlled optimization with fuel invoices |
| P12 | Existing lab access, non-duplicate IP and external buyer hypothesis | Partner laboratory and IP/commercial expertise | OneTech + Legal | Y0 novelty/rights; Y2 technical and buyer gate before any Y3 continuation |
| P13 | Matched-store slice before 100-store rollout; POS/labels, stock and price rights | Buy labels, blend forecasting and POS integration | Retail sponsor + store managers | Y1 matched trial; before Y2 compare forecast-only against labels |
| E01 | Baseline/model inventory for all seven cases; no new enterprise platform | Reuse existing governance tooling | Finance + Digital Line | Y0 register; quarterly cash and risk reviews |

Hard dependencies block releases. Weather/traffic enhancements are soft for retail and must not delay a minimal POS-based trial. P01/P02/P03 benefits must use distinct events and ownership scopes. E01 is counted once. No automatic return is assigned to governance or H3 learning.
''')
road=(R/'work/roadmap.md').read_text()
road=road.replace('**Updated:** 9 November 2026','**Updated:** 10 November 2026')
road=road.replace('**Rework in progress (9 Nov):**','**Rework in progress (10 Nov):**')
road+='''
## Authorized refinement, 10 November 2026

Steps 11–21 remain open. Active selection is P01/P02/P03/P05/P09/P12/P13/E01; featured cases are P01/P03/P12/P13. Previous selection and graphics are archived. Scope is a selective programme, not all five branches by construction. Owners and dependencies in the table remain unchanged; role assignments do not claim internal TotalEnergies approval.

| Step / issue | Current output and remaining acceptance work |
| --- | --- |
| 11 / #11 | `work/options/selected_portfolio_decision.md`; challenge selection and H3 novelty |
| 12 / #12 | `work/projects/case_p01_refining_pdm.md`; revised scenario check |
| 13 / #13 | `work/projects/case_p03_deepwater_drilling.md`; economic share and avoidable payment assumptions explicit |
| 14 / #14 | `work/projects/case_p12_esaf_licensing.md`; external licensing hypothesis and learning gates |
| 15 / #15 | `work/projects/case_p13_retail_station_demand.md`; delivery cash excluded, markdown attribution sensitivity |
| 16 / #16 | `work/projects/reserve_cards.md`; selected complementary cases only |
| 17 / #17 | `work/projects/portfolio_sequencing_canvas.md`, `work/projects/chart_regeneration_spec.md`; chart rendering pending |
| 18 / #18 | `work/finance/portfolio_model_selected.xlsx`, `work/finance/portfolio_economics.md`; independent arithmetic checks completed, final finance review open |
| 19 / #19 | `work/finance/cost_of_inaction.md`; no unsupported cash uplift |
| 20 / #20 | `work/governance/gates_and_adoption.md`; role-based release conditions and committed-exposure limits |
| 21 / #21 | `deliverables/report/full_strategy_report_draft.md`; revised text/tables, final challenge and graphics pending |

No acceptance box is checked by this refinement. Memo and slides have not been generated.
'''
(R/'work/roadmap.md').write_text(road)
with (R/'sources/register.md').open('a',encoding='utf-8') as f:f.write('''
## Additional H3 qualification sources, 10 November 2026

- SRC-H3-01: TotalEnergies, “Innovating to Accelerate the Energy Transition”, https://totalenergies.com/company/strength/innovation-rd, accessed 10 Nov 2026; sections on six strategic R&T programmes and SAF partnerships. Verified public disclosure of existing capabilities, not proof of a new licensing gap.
- SRC-H3-02: Infinium, “Projects”, https://infinium.energy/projects, accessed 10 Nov 2026, Southeast Asia section describing April 2026 technology licensing. Company announcement; no independently verified financial return. Supports a business-model archetype only.
- H3 proposal, buyer economics, novelty, IP rights and the $2.85m feasibility ceiling remain explicit assumptions/unknowns. See `sources/synthesis/2026-11-10_h3_licensing_option.md`.
''')
