"""Enumerate whole-project half-budget options, with H3 stopped after year two."""
import contextlib
import io
from itertools import combinations
with contextlib.redirect_stdout(io.StringIO()):
    import project_economics_review as m

cap=sum(r['cost'] for r in m.rows)/2
mandatory=['E01','P12']
optional=['P01','P02','P03','P05','P09','P13']
base=dict(m.base); base['P12']=m.flows(m.cases['P12'],stop=3)[0]
cost={k:sum(m.flows(c,stop=3 if k=='P12' else None)[1]) for k,c in m.cases.items()}
options=[]
for n in range(len(optional)+1):
    for group in combinations(optional,n):
        ids=mandatory+list(group); spending=sum(cost[k] for k in ids)
        if spending>cap: continue
        b=m.metrics(m.agg(base,ids)); d=m.metrics(m.agg(m.down,ids))
        options.append((b['npv'],ids,spending,b,d))
lines=['# Half-budget options — whole projects', '',f'Five-year gross spending ceiling: USD {cap:.3f}m (half of the current full portfolio). P12 is funded through Y2 with an assumed USD 0.1m closure in Y3; E01 is fully included. Downside uses the project-specific candidate assumptions in the companion review. No project is fractionally scaled.', '', '| Projects | Base spending $m | Base IRR | Downside IRR | Base NPV $m | Downside NPV $m | Downside cash Y5 $m |', '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
for _,ids,sp,b,d in sorted(options,reverse=True)[:12]:
    lines.append(f"| {', '.join(ids)} | {sp:.3f} | {m.pct(b['irr'])} | {m.pct(d['irr'])} | {b['npv']:+.3f} | {d['npv']:+.3f} | {d['cash5']:+.3f} |")
lines+=['','The ranking is by base NPV, not a recommendation to maximize financial return alone. H3 closure cost and the ability to stop must be validated. Downside costs may exceed the base budget ceiling; it is an overrun scenario, not a funded budget. These are tests, not approved forecasts. Reproduce with `python work/finance/test_half_options.py`.']
(m.ROOT/'work/finance/half_budget_options.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('\n'.join(lines))
