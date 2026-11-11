"""Add reconciled cost bridge and proposed decision gates to the report once."""
import csv
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
data = root / 'work/projects/report_tables.json'
report = root / 'deliverables/report/full_strategy_report_draft.md'
tables = json.loads(data.read_text(encoding='utf-8'))
if any(x['id'] == 'report_table_21' for x in tables):
    raise SystemExit('Already applied')
with (root / 'work/finance/category_allocation.csv').open(encoding='utf-8', newline='') as f:
    cost = list(csv.reader(f))
cost = [[row[0]] + [f'{float(x):.2f}' for x in row[1:]] for row in cost[1:]]
cost.insert(0, ['Cost category, $m', 'Y0', 'Y1', 'Y2', 'Y3', 'Y0–Y3'])
gates = [
 ['Initiative / owner', 'Month-12 evidence and threshold', 'If threshold is missed'],
 ['P01 — Refining sponsor', 'Safe pilot, documented baseline and prospective NPV above zero at 9.5%.', 'Pause site expansion; redesign or stop.'],
 ['P02 — Upstream sponsor', 'Eligible sold output and event baseline confirmed; prospective NPV above zero at 10%.', 'Pause rollout; redesign or stop.'],
 ['P03 — Drilling sponsor', 'Contractual ability to avoid rig payments confirmed; prospective NPV above zero at 11%.', 'Pause expansion; redesign or stop.'],
 ['P04 — Renewables sponsor', 'Saleable generation and entitlement measured against baseline; prospective NPV above zero at 10%.', 'Pause asset expansion; redesign or stop.'],
 ['P05 — Corporate IT / procurement', 'Cancellation rights and eligible redundant licence cohort verified; prospective NPV above zero at project hurdle.', 'Pause removals; redesign or stop.'],
 ['P08 — Customer business sponsor', 'Controlled test demonstrates positive incremental net retention; prospective NPV above zero at 9.5%.', 'Pause expansion; redesign or stop.'],
 ['P09 — LNG operations sponsor', 'Fuel-payment rights and invoice baseline verified; prospective NPV above zero at project hurdle.', 'Pause rollout; redesign or stop.'],
 ['P12 — OneTech / commercial lead', 'IP and lab access cleared and two qualified developer discussions initiated before Y2.', 'Stop avoidable commercial expansion or redesign the option.'],
 ['P13 — Retail sponsor', 'Matched-store trial and baseline established; prospective NPV above zero at 9% and incremental label economics positive.', 'Pause hardware expansion; prefer forecast-only or stop.'],
 ['E01 — Finance / Digital Line', 'Named owners, model inventory and baseline register cover all launched pilots.', 'Pause release of any pilot lacking required controls.']]
canvas = [
 ['Initiative', 'Business owner / sourcing', 'Dependency before release'],
 ['P01', 'Refining sponsor / blend', 'Eligible site data and reliability workflow'],
 ['P02', 'Upstream sponsor / blend', 'Production access and distinct events'],
 ['P03', 'Drilling sponsor / buy and blend', 'Contract terms and avoidable rig payments'],
 ['P04', 'Renewables sponsor / blend', 'O3C and OEM baseline, entitlement and saleability'],
 ['P05', 'Corporate IT and procurement / existing tools', 'Licence and cancellation rights'],
 ['P08', 'Customer business sponsor / blend', 'CRM access, privacy and controlled test'],
 ['P09', 'LNG operations sponsor / buy and blend', 'Routing baseline, charter rights and fuel invoices'],
 ['P12', 'OneTech and commercial lead / partner', 'Lab access, IP rights and external demand'],
 ['P13', 'Retail sponsor / buy and blend', 'POS access, stock and pricing rights'],
 ['E01', 'Finance and Digital Line / reuse', 'Existing governance tools and named owners']]
tables.extend([{'id':'report_table_21','title':'Indicative allocation of existing costs','rows':cost},
               {'id':'report_table_22','title':'Portfolio ownership, sourcing and dependencies','rows':canvas},
               {'id':'report_table_23','title':'Proposed initiative release gates','rows':gates}])
s = report.read_text(encoding='utf-8')
marker = '### Portfolio economics'
block = '''### Indicative cost allocation\n\nThe following top-down planning allocation classifies the existing model costs into six categories. Y1–Y3 form the three-year operating view; Y0 is the upfront decision period and is shown separately. This classification does not add spending or change CAPEX/OPEX. It is an indicative allocation, not a project-level costing or supplier quote: cost owners must replace its assumed shares with staff, procurement and contract evidence before release. Compute and equipment includes physical assets such as retail labels; talent includes training and backfill. Amounts may differ by rounding.\n\n![Indicative allocation of existing costs](assets/report_table_21.png)\n\nThe [allocation basis](../../work/finance/category_allocation_notes.md) and [reproducible calculation](../../work/finance/category_allocation.py) document the proportions and reconciliation.\n\n'''
assert marker in s
s = s.replace(marker, block + marker, 1)
marker = '### Spending and funding sequence'
block = '''### Portfolio ownership and dependencies\n\nThe roles below are proposed accountable functions, subject to appointment. The listed dependencies are checked before each case is released; shared controls are funded once through E01 in the full portfolio.\n\n![Portfolio ownership, sourcing and dependencies](assets/report_table_22.png)\n\n'''
assert marker in s
s = s.replace(marker, block + marker, 1)
marker = '## 5. Implementation and adoption'
block = '''### Project-level release gates\n\nAt month 12 the sponsor and Finance apply these proposed tests before releasing expansion. Prospective NPV uses only remaining cash flows and the project's hurdle; sunk spending is excluded. Where a pilot starts later, the same evidence is required before its first expansion, with the revised review date recorded by the sponsor. Critical safety, security or legal failure triggers an immediate pause. Owners must validate operational thresholds and appoint decision-makers before launch.\n\n![Proposed initiative release gates](assets/report_table_23.png)\n\nFor P05 and P09, use the project-specific rates in the [hurdle policy](../../work/finance/discount_rate_policy.md). At the month-24 gate, branch sponsors and Finance approve further funding only if the remaining case has positive prospective NPV at its project hurdle and its operational and control conditions remain satisfied; P12 instead requires technical, IP and paid-evaluation evidence before commercial continuation. At month 36, the steering group reviews each case against the same continuation principle. If a condition is not met, the owner pauses new commitments and decides whether to redesign or stop; existing contractual obligations and closure costs remain.\n\n'''
assert marker in s
s = s.replace(marker, block + marker, 1)
s = s.replace('## 6. Conditions for the final investment decision', 'The [supporting change management plan](change_management_plan.md) sets out the risk owners, stakeholder cadence, three training tiers and adoption measures in more detail.\n\n## 6. Conditions for the final investment decision', 1)
data.write_text(json.dumps(tables, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
report.write_text(s, encoding='utf-8')
print('Added allocation, ownership and gate tables to report')
