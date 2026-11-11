"""Reconcile an indicative top-down cost-category allocation to model cash costs."""
import csv
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
model = json.loads((root / 'work/finance/selected_chart_data.json').read_text(encoding='utf-8'))
categories = ['Compute and equipment', 'Talent and change', 'Integration', 'Model operations', 'Data engineering', 'Governance and legal']
# Indicative classification, not observed expenditure. Each column sums to 1.
shares = [[.30,.25,.20,.05,.15,.05], [.20,.25,.25,.08,.17,.05], [.20,.25,.15,.17,.16,.07], [.18,.24,.12,.22,.16,.08]]
totals = [sum(p['annual_cost'][year] for p in model['projects'].values()) for year in range(4)]
rows = [[name] + [totals[y] * shares[y][i] for y in range(4)] for i, name in enumerate(categories)]
target = root / 'work/finance/category_allocation.csv'
with target.open('w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['Category', 'Y0', 'Y1', 'Y2', 'Y3', 'Y0–Y3'])
    for row in rows: w.writerow([row[0]] + [f'{v:.6f}' for v in row[1:]] + [f'{sum(row[1:]):.6f}'])
    w.writerow(['Total'] + [f'{v:.6f}' for v in totals] + [f'{sum(totals):.6f}'])
for y in range(4): assert abs(sum(r[y + 1] for r in rows) - totals[y]) < 1e-9
print('Gross costs Y0–Y3:', ', '.join(f'{x:.6f}' for x in totals))
