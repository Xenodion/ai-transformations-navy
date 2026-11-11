"""Calculate the proposed eight-project scenarios without changing the workbook."""
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    import project_economics_review as m

gross={'P01':2.4995,'P03':3.36,'P13':.635}
down_gross={'P01':2.4995*.8,'P02':1.314,'P03':3.36*.8,'P05':.36,'P09':.54,'P13':.635*.9}
base={}; down={}
for k,c in m.cases.items():
    base[k]=m.flows(c,gross=gross.get(k))[0]
    if k=='P12':
        base[k]=[-.3,-.9,-.3,.18,.8175,1.38]
        down[k]=m.flows(c,cost=1.1,stop=3)[0]
    elif k=='E01': down[k]=m.flows(c,cost=1.1)[0]
    else:
        ramp=m.stress[k][1]
        if k=='P09': ramp=c['ramp']
        down[k]=m.flows(c,gross=down_gross[k],ramp=ramp,cost=1.05 if k in ('P09','P13') else 1.1)[0]
def result(label,ids):
    for name,part in [('Base',base),('Downside',down)]:
        cash=m.agg(part,ids); v=m.metrics(cash)
        print(label,name,'IRR',m.pct(v['irr']),'NPV',round(v['npv'],3),'payback',m.pb(v['payback']),'Y5',round(v['cash5'],3))
for k in m.cases: result(k,[k])
result('Four', ['P01','P03','P12','P13'])
result('Eight',list(m.cases))
