"""Integrate the existing change plan and operational case detail in the full report."""
from pathlib import Path

root = Path(__file__).resolve().parents[2]
path = root / 'deliverables/report/full_strategy_report_draft.md'
report = path.read_text(encoding='utf-8')
if '#### Operational workflow and evidence plan' in report:
    raise SystemExit('Already integrated')

sections = {
 '### P03 — Deepwater drilling advisory (H2, provisional)': '''#### Operational workflow and evidence plan

Select critical rotating equipment with the site reliability team and document the existing inspection programme, historical events and process constraints. Establish whether the sensor and maintenance records can be joined at equipment level; where they cannot, repair only the interfaces needed for the pilot. The Digital Factory specialist and site expert review alert logic together. Alerts enter the existing maintenance workflow; a reliability engineer assesses severity, maintenance windows and false alarms. No model directs an automatic shutdown or bypasses safety procedures.

Before testing, Finance and operations agree comparable equipment and a period adjusted for maintenance schedules and production conditions. The evaluation follows the complete chain: eligible alert → verified failure mode → action taken → avoidable stop or repair → additional saleable throughput or paid invoice avoided. Log alerts that do not lead to intervention as well as missed events. Record additional output at the actual incremental contribution and deduct the effects of planned maintenance, demand or other bottlenecks; compare repair invoices separately to avoid counting the same event twice. The sponsor stops expansion if safe action, data quality or prospective economics are inadequate; a good prediction score alone is not a return.

''',
 '### P12 — AI-assisted e-SAF technology licensing option (H3)': '''#### Operational workflow and evidence plan

The drilling lead selects eligible campaigns and obtains operator, partner and contractor agreement before any data transfer. The project team combines approved historical well data, engineering records and contractor inputs to surface advisory recommendations for planning and execution. The drilling engineer and contractor assess each recommendation within existing HSE and well-control procedures; operational authority and the right to reject a recommendation remain unchanged.

Before the pilot, establish comparable well phases and the existing planning and non-productive-time baseline, with geological and operational differences recorded. For each recommendation, retain the evidence trail from planned activity to actual rig days and then to the relevant contract clause and invoice. Finance counts a benefit only when a shorter period actually reduces a payment or creates another documented cash effect, adjusted once for the group's contractual economic interest. Faster work without an invoice impact is reported separately. If the contract prevents capture, if the tool duplicates an existing capability, or if remaining prospective cash flows fail the 11% hurdle, the sponsor pauses expansion and selects a redesign or stop decision.

''',
 '### P13 — French retail demand and controlled markdowns (H1)': '''#### Operational workflow and evidence plan

OneTech and Legal first map existing research, partner rights and any current external licensing offer; the commercial lead defines the prospective developer and the problem the proposed process package would solve. Within existing laboratory capacity, researchers compare AI-assisted experiment selection with conventional design of experiments under a pre-registered protocol and the same experimental resources. Three independent runs must demonstrate repeatability; scientific leads set the technical improvement threshold before testing. A research result is not by itself proof that a third party will pay for the technology.

The commercial lead tests a defined application and benchmark with at least two qualified developers before Y2. Before Y3, OneTech and Legal review freedom to operate and technical results, and the commercial lead seeks documented willingness from at least one developer to enter a paid evaluation. Pricing, scope of support, partner rights and the cost of moving beyond laboratory work must be established before a commercial commitment. Stop or reclassify if the proposition only improves an internal process or duplicates an existing offer. The Y3–Y5 receipts are a conditional scenario rather than signed revenue; the downside assumes no receipts and includes closure costs.

''',
 '### Project-level release gates': '''#### Operational workflow and evidence plan

Start with a representative, instrumented subset of eligible stores. Retail operations confirms stock ownership, price authority, POS and label interfaces, then agrees a matched-store protocol with Finance before hardware is purchased at scale. Store managers receive recommended orders and markdowns through their existing workflow and retain approval authority. The team trains staff on exceptions, price controls and a manual fallback, and records the additional workload and backfill cost.

Compare current practice, rules-based ordering, forecasting without labels and forecasting with labels where the pilot design permits. Define separate SKU/day cohorts for waste reduction and markdown recovery before testing; measure stock-out recovery net of substitution and use incremental contribution rather than sales. Adjust for seasonality and promotions, and count urgent-delivery savings only against avoidable paid invoices. Finance checks the measured effects and remaining costs before further hardware release. If the label increment does not justify its cost, retain the option to use forecasting alone; if the prospective case fails the 9% hurdle, pause or stop expansion.

'''
}
for marker, block in sections.items():
    assert marker in report, marker
    report = report.replace(marker, block + marker, 1)

plan = (root / 'deliverables/report/change_management_plan.md').read_text(encoding='utf-8')
plan = plan[plan.index('## Page 1'):]
plan = plan.replace('## Page 1 — Risks, early warning and ownership', '### Change risks, early warning and ownership')
plan = plan.replace('## Page 2 — Stakeholders and communication', '### Stakeholders and communication')
plan = plan.replace('## Page 3 — Skills, measurement and stop rules', '### Skills, measurement and stop rules')
start = report.index('### Change plan: ownership, communication and skills')
end = report.index('## 6. Conditions for the final investment decision', start)
report = report[:start] + plan.strip() + '\n\n' + report[end:]

old = 'The [allocation basis](../../work/finance/category_allocation_notes.md) and [reproducible calculation](../../work/finance/category_allocation.py) document the proportions and reconciliation.'
new = ('The assumed category shares, in the order shown, are 30/25/20/5/15/5% for Y0, '
       '20/25/25/8/17/5% for Y1, 20/25/15/17/16/7% for Y2 and 18/24/12/22/16/8% for Y3. '
       'Each year’s gross spending is multiplied by those shares; the resulting classifications sum to the existing annual model totals. '
       'They are portfolio-level allocations and must not be read as a project-by-project breakdown. '
       'The [reproducible calculation](../../work/finance/category_allocation.py) retains the unrounded amounts.')
assert old in report
report = report.replace(old, new)
path.write_text(report, encoding='utf-8')
print('Integrated change plan, case workflows and cost allocation basis')
