"""Independent arithmetic check and chart export from the selected workbook.

Reads inputs/scenarios and verifies every annual cash component against caches.
Never writes spreadsheet values. Run after build_workbook.mjs.
"""
from pathlib import Path
import json, sys
import openpyxl
from decision_cashflows import npv, conventional_irr, payback

ROOT=Path(__file__).resolve().parents[2]
w=openpyxl.load_workbook(ROOT/'work/finance/portfolio_model_working.xlsx',data_only=True)
names=['Downside','Base','Upside','Severe stress']
weights=[w['Portfolio'].cell(17,c).value for c in range(2,5)]
assert all(isinstance(v,(int,float)) and v>=0 for v in weights) and abs(sum(weights)-1)<1e-10
projects={}
for i,row in enumerate(w['Inputs'].iter_rows(min_row=2,max_row=11,max_col=21,values_only=True)):
    ident,name,h,rate,fx,book,c0,c1,launch,*rest=row
    op=rest[:5]; benefit=rest[5]; ramps=rest[6:11]
    p=dict(id=ident,name=name,horizon=h,hurdle=rate,fx=fx,one_time=(c0+c1+launch)*fx,annual_cost=[c0*fx]+[(o+(c1+launch if t==0 else 0))*fx for t,o in enumerate(op)],scenarios={})
    for j,n in enumerate(names):
        sr=32+i if j==3 else 2+i*3+j
        vals=[w['Scenarios'].cell(sr,k).value for k in range(1,15)]
        _,_,bf,inv,of,tax,*tail=vals
        ramp=tail[:5]; run,real,exit_cost=tail[5:]
        rows=[]
        for t in range(6):
            b=0 if t==0 else benefit*book*real*bf*ramp[t-1]*fx*(run if t>=3 else 1)
            o=0 if t==0 else (op[t-1]*of*(run if t>=3 else 1)+(launch*inv if t==1 else 0)+(exit_cost if t==3 else 0))*fx
            c=(c0 if t==0 else c1 if t==1 else 0)*inv*fx
            tx=0 if t==0 else max(0,b-o-(c0+c1)*inv*fx/5)*tax
            rows.append([b,o,c,tx,b-o-c-tx])
        cr=2+7*(30+i if j==3 else i*3+j)
        for t,r in enumerate(rows):
            for k,v in enumerate(r):
                cached=w['Cash flow build'].cell(cr+k+1,t+2).value
                assert isinstance(cached,(float,int)) and abs(v-cached)<1e-8,(ident,n,t,k,v,cached)
        cash=[r[-1] for r in rows]
        p['scenarios'][n]=dict(rows=rows,cash=cash,npv=npv(rate,cash),irr=conventional_irr(cash),payback=payback(cash) if ident!='E01' else None)
    projects[ident]=p

def aggregate(ids):
    out={}
    for n in names:
        cash=[sum(projects[k]['scenarios'][n]['cash'][t] for k in ids) for t in range(6)]
        out[n]=dict(cash=cash,npv=npv(.10,cash),irr=conventional_irr(cash))
    cash=[sum(out[n]['cash'][t]*a for n,a in zip(names,weights)) for t in range(6)]
    out['Weighted']=dict(cash=cash,npv=npv(.1,cash),irr=conventional_irr(cash),payback=payback(cash))
    out['annual_cost']=[sum(projects[k]['annual_cost'][t] for k in ids) for t in range(6)]
    out['gross_cost']=sum(out['annual_cost'])
    return out

full=aggregate(list(projects))
# Keep the same H3 experiment and common controls; defer entire projects, not fractions.
half_ids=['P01','P03','P12','P13']
half=aggregate(half_ids)
# Half envelope funds P12 through Y2 only, plus a $0.10m closure/transfer allowance.
half['gross_cost']=sum(half['annual_cost'])
cash=[sum(half[n]['cash'][t]*a for n,a in zip(names,weights)) for t in range(6)]
half['Weighted']=dict(cash=cash,npv=npv(.1,cash),irr=conventional_irr(cash),payback=payback(cash))
for j,n in enumerate(names[:3]):
    for t in range(6):
        assert abs(sum(full[n]['cash'][:t+1])-w['Portfolio'].cell(t+6,j+2).value)<1e-8
errors=[(s.title,c.coordinate,c.value) for s in w for row in s for c in row if c.data_type=='e']
assert not errors,errors
lt=w['Long-term DCF']; rate=lt['B2'].value; years=lt['B3'].value; retention=lt['B4'].value
longterm={'rate':rate,'continuation_years':years,'retention':retention,'projects':{},'horizons':{}}
for i,(ident,p) in enumerate(projects.items(),7):
    cash=p['scenarios']['Base']['cash']; val=npv(rate,cash)+sum(cash[-1]*retention/(1+rate)**t for t in range(6,6+int(years)))
    assert abs(val-lt.cell(i,6).value)<1e-8,(ident,val,lt.cell(i,6).value)
    longterm['projects'][ident]=val
    h='H1' if p['horizon']=='Enabler' else p['horizon']
    longterm['horizons'][h]=longterm['horizons'].get(h,0)+val
for i,h in enumerate(['H1','H2','H3'],7): assert abs(longterm['horizons'][h]-lt.cell(i,7).value)<1e-8
data=dict(version='selected-2026-11-10',units='USD million; native P13 EUR via fx',weights=dict(zip(names[:3],weights)),projects=projects,portfolio=full,half_ids=half_ids,half=half,longterm=longterm)
(ROOT/'work/finance/selected_chart_data.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in full.items() if k!='annual_cost'},indent=2))
print('Half budget',half['gross_cost'],'weighted NPV',half['Weighted']['npv'])
print('Verified: annual cash components and portfolio aggregation. Four-case spending is approximately half of the full portfolio.')
