"""Recompute cash schedules from the workbook's numeric input cells.

This is independent of Excel formula caches, but is not an Excel formula engine
and does not validate the economic assumptions or project-level timing.
"""
from pathlib import Path
from math import isclose
import openpyxl

path = Path(__file__).with_name('totalenergies_ai_portfolio_model.xlsx')
wb = openpyxl.load_workbook(path, data_only=False)
all_projects = []
for sheet, count in [('Tier1_Featured_DCF', 5), ('Tier2_Reserve_DCF', 9)]:
    ws = wb[sheet]
    for i in range(count):
        row = 4 + 14 * i
        title = str(ws.cell(row - 3, 1).value)
        values = [[ws.cell(row + offset, col).value for col in range(2, 8)] for offset in range(3)]
        assert all(isinstance(x, (int, float)) for line in values for x in line), title
        benefit, capex, opex = values
        flows = [b - c - o for b, c, o in zip(benefit, capex, opex)]
        all_projects.append((title, benefit, capex, opex, flows))

def irr(flows):
    # Valid only for these conventional flows: one initial negative followed by positives.
    assert flows[0] < 0 and all(x >= 0 for x in flows[2:])
    def npv(r): return sum(v / (1 + r) ** t for t, v in enumerate(flows))
    lo, hi = 0., 1.
    while npv(hi) > 0: hi *= 2
    for _ in range(100):
        mid = (lo + hi) / 2
        if npv(mid) > 0: lo = mid
        else: hi = mid
    return (lo + hi) / 2

benefit = [sum(p[1][t] for p in all_projects) for t in range(6)]
outflow = [sum(p[2][t] + p[3][t] for p in all_projects) for t in range(6)]
flows = [b - c for b, c in zip(benefit, outflow)]
variables = wb['Variables']
rates = {'P01': 8, 'P03': 7, 'P11': 12, 'P13': 10, 'E01': 11, 'P02': 7,
         'P04': 9, 'P05': 11, 'P06': 11, 'P07': 11, 'P08': 9, 'P09': 11,
         'P10': 8, 'P12': 12}
cost = {p[0][:3]: sum(p[2][:4]) + sum(p[3][:4]) for p in all_projects}
total_cost = sum(cost.values())
rate = sum(cost[k] * variables.cell(v, 3).value for k, v in rates.items()) / total_cost
npv = sum(v / (1 + rate) ** t for t, v in enumerate(flows))
sum_project_npv = sum(sum(v / (1 + variables.cell(rates[p[0][:3]], 3).value) ** t
                          for t, v in enumerate(p[4])) for p in all_projects)
assert isclose(sum(flows), sum(benefit) - sum(outflow), abs_tol=1e-8)
print('Projects:', len(all_projects))
print('Gross benefits Y0-Y5:', [round(x, 2) for x in benefit])
print('Outflows Y0-Y5:', [round(x, 2) for x in outflow])
print('Net cash Y0-Y5:', [round(x, 2) for x in flows])
print('Three-year envelope:', round(total_cost, 2))
print('Net cumulative:', round(sum(flows), 2))
print('Weighted rate:', round(rate * 100, 4), '%')
print('NPV at weighted rate:', round(npv, 2))
print('Sum of project NPVs:', round(sum_project_npv, 2))
print('IRR:', round(irr(flows) * 100, 2), '%')
print('These numbers are arithmetic on inputs, not validated forecasts or a workbook recalculation.')
