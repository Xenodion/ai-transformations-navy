"""Final documentation checks and retained cost-category allocation."""
from pathlib import Path
import json,re,openpyxl
R=Path(__file__).resolve().parents[2]
d=json.loads((R/'work/finance/selected_chart_data.json').read_text())
w=openpyxl.load_workbook(R/'work/finance/portfolio_model_selected.xlsx',data_only=True)
alloc={'Compute / platform':(.2,0,.1),'Talent / training':(0,.2,.2),'Integration / workflow':(.6,.5,0),'Model operations':(0,0,.55),'Data preparation':(.2,.2,.05),'Governance / controls':(0,.1,.1)}
components=[[0.,0.,0.] for _ in range(6)]
for row in w['Inputs'].iter_rows(min_row=2,max_row=9,max_col=21,values_only=True):
    fx=row[4]
    components[0][0]+=row[6]*fx;components[1][0]+=row[7]*fx;components[1][1]+=row[8]*fx
    for t in range(1,6):components[t][2]+=row[8+t]*fx
rows={name:[sum(a*b for a,b in zip(factors,c)) for c in components] for name,factors in alloc.items()}
assert abs(sum(map(sum,rows.values()))-d['portfolio']['gross_cost'])<1e-8
table='| Category, USD m | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 | Total |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n'
for name,values in rows.items():table+='| '+name+' | '+' | '.join(f'{v:.3f}' for v in values+[sum(values)])+' |\n'
text='''### Cost-category allocation

**Planning classification, not supplier quotes:** preserve the existing allocation method: CAPEX is 20% compute, 60% integration and 20% data; launch is 20% talent, 50% integration, 20% data and 10% governance; recurring OPEX is 10% compute, 20% talent, 55% model operations, 5% data and 10% governance. These categories classify the same cash once and add no expenditure. Replace the allocators with vendor and staff cost lines before commitments; they do not establish that backfill is fully funded.

'''+table+'\n'
for rel in ['deliverables/report/full_strategy_report_draft.md','work/finance/portfolio_economics.md']:
    p=R/rel;s=p.read_text(encoding='utf-8');marker='### 7.1 If only half the budget is available'
    if '### Cost-category allocation' not in s:s=s.replace(marker,text+marker)
    p.write_text(s,encoding='utf-8')
p=R/'work/options/operating_model.md';s=p.read_text(encoding='utf-8')
a=s.index('## 5. Funding');b=s.index('## 6.',a)
s=s[:a]+'''## 5. Funding

The selected programme has a five-operating-year ceiling plus Y0. Each segment sponsor and Finance signs its case; Corporate sponsors P05/E01 and OneTech sponsors the P12 licensing experiment with commercial/IP support. These are proposed responsibilities, not observed funding transfers. Do not apply the course's illustrative 100/60/40 central funding path as a TotalEnergies fact. Actual hub/BU contributions require agreement before release, without changing consolidated cash or counting internal transfers twice.

'''+s[b:]
s=s.replace('directly resolving the frontline adoption lag and Shadow AI bypass observed in downstream operations (CLM-074).','testing whether protected business capacity improves the local delivery friction observed at Argedis (CLM-074); group-wide causality is not established.')
p.write_text(s,encoding='utf-8')
with (R/'work/roadmap.md').open('a',encoding='utf-8') as f:f.write('''
**Issue synchronization pending:** on 10 Nov, the connected GitHub tool returned HTTP 403. The CLI read succeeded, but automatic approval review rejected the proposed bulk issue edit as insufficiently verified disclosure to the remote destination. No issue closure or accepted status change occurred. Local scope/output changes above are pending remote synchronization; do not treat the remote issue bodies as current until that operation is authorized and completed.
''')
with (R/'.gitignore').open('a',encoding='utf-8') as f:f.write('\n# Local artifact runtime and review previews\nwork/finance/node_modules/\nwork/finance/*preview*.png\nwork/finance/*.inspect.ndjson\n')
# Check active report local links; project links are resolved in their own directory.
bad=[]
for rel in ['deliverables/report/full_strategy_report_draft.md','work/README.md','work/projects/case_rebuild_decisions.md']:
    p=R/rel
    for link in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
        if '://' in link or link.startswith('#'):continue
        from urllib.parse import unquote
        if not (p.parent/unquote(link.split('#')[0])).exists():bad.append((rel,link))
assert not bad,bad
assert abs(w['Half budget']['H13'].value-d['half']['gross_cost'])<1e-8
for t in range(6):assert abs(w['Half budget'].cell(5,t+2).value-d['half']['Weighted']['cash'][t])<1e-8
assert abs(w['Half budget']['H5'].value-d['half']['Weighted']['npv'])<1e-8
report=(R/'deliverables/report/full_strategy_report_draft.md').read_text(encoding='utf-8')
assert not re.search(r'P04|P06|P07|P08|P10|P11|27\.637|0\.825',report)
print('PASS: active report links, retired-ID exclusion, six-category budget reconciliation and half-budget workbook/JSON equality.')
