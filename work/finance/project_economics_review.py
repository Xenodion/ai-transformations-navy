"""Read-only project challenge. Produces one decision table; does not edit workbook."""
from pathlib import Path
import json
import openpyxl
from decision_cashflows import npv, conventional_irr, payback

ROOT=Path(__file__).resolve().parents[2]
w=openpyxl.load_workbook(ROOT/'work/finance/portfolio_model_selected.xlsx',data_only=True)
cases={}
for row in w['Inputs'].iter_rows(min_row=2,max_row=9,max_col=21,values_only=True):
    ident,name,h,rate,fx,book,c0,c1,launch,*rest=row
    cases[ident]=dict(name=name,h=h,rate=rate,fx=fx,c0=c0,c1=c1,launch=launch,op=rest[:5],gross=rest[5]*book,ramp=rest[6:11])

def flows(c,gross=None,ramp=None,cost=1,initial=1,stop=None):
    g=c['gross'] if gross is None else gross;r=c['ramp'] if ramp is None else ramp
    cap=(c['c0']+c['c1'])*cost*initial
    cash=[-c['c0']*cost*initial];spend=[c['c0']*cost*initial]
    for t in range(1,6):
        if stop is not None and t>=stop:
            cash.append(-.1 if t==stop else 0);spend.append(.1 if t==stop else 0);continue
        b=g*r[t-1];o=c['op'][t-1]*cost+(c['launch']*cost*initial if t==1 else 0)
        cp=c['c1']*cost*initial if t==1 else 0
        tax=max(0,b-o-cap/5)*.25
        cash.append(b-o-cp-tax);spend.append(o+cp)
    return [v*c['fx'] for v in cash],[v*c['fx'] for v in spend]

def metrics(cash,rate=.1):
    return dict(npv=npv(rate,cash),irr=conventional_irr(cash),payback=payback(cash),cash5=sum(cash))

# Operational downside candidates, assumptions to validate; not fitted to return targets.
stress={
'P01':(250000*365*.004*.70*5.5/1e6+.15,[.15,.5,.8,1,1]),
'P02':(2*120*365*15/1e6,[.1,.35,.65,.9,1]),
'P03':(2*5*.4*.8*.65,[0,.25,.6,.9,1]),
'P05':(10000*.12*25*12/1e6,[.2,.5,.85,1,1]),
'P09':(30*1*.015,[0,.25,.6,.9,1]),
'P13':(.245*.8+.200*.75+.140*.8,[.4,.7,.9,1,1]),
'P12':(0,[0]*5),'E01':(0,[0]*5)}
notes={
'P01':'Keep. Downside: recovery 0.4%, margin $5.5/bbl, repairs $0.15m. Validate incremental sold throughput and funded reliability integration.',
'P02':'Keep conditional. Downside: 120 recovered bbl/day/hub, slower adoption. Verify equity entitlement and that recovered output is incremental.',
'P03':'Keep conditional. Downside: 5 days/rig, 80% economic share, 65% avoidable payment. Split ownership from payment rights; six days are not cash until invoices change.',
'P05':'Conditional enabler. Downside: 12% seats cancelled, $25 net monthly price. Verify actual paid seats and cancellation date; licence pruning is not itself an AI transformation.',
'P09':'Re-scope or defer. Downside: fuel saving 1.5%, slower ramp. Small standalone margin; contract control and incremental fuel saving must be established.',
'P12':'Fund learning, not a positive project IRR. Downside stops after Y2 with closure expense; base funds the full experiment. No royalty revenue booked.',
'P13':'Redesign cost/scope before approval. Downside: waste/stock-out gains -20%, markdown -25%. Distinct markdown cohort and actual label quotes are decisive.',
'E01':'Include once within H1 for presentation; preserve explicit governance cost in accounts. No standalone return.'}
base={};down={};rows=[]
for k,c in cases.items():
    b,sp=flows(c);g,r=stress[k];dc,dsp=flows(c,g,r,cost=1.10,stop=3 if k=='P12' else None)
    base[k]=b;down[k]=dc;bm=metrics(b,c['rate']);dm=metrics(dc,c['rate'])
    # Break-even annual gross benefit at unchanged base cost/ramp.
    low,high=0,20
    for _ in range(80):
        mid=(low+high)/2
        if npv(c['rate'],flows(c,mid)[0])>0: high=mid
        else:low=mid
    threshold=(low+high)/2
    rows.append(dict(id=k,base=bm,down=dm,gross=c['gross'],gross_floor=threshold,cost=sum(sp),note=notes[k]))

def agg(parts,ids):return [sum(parts[k][t] for k in ids) for t in range(6)]
fullbase=agg(base,list(cases));fulldown=agg(down,list(cases))
# Existing half-scope, with the same tested unit assumptions, H3 closure in every path.
halfids=['P01','P05','P09','P12','E01']
hb=dict(base);hd=dict(down)
hb['P12']=flows(cases['P12'],stop=3)[0]
halfb=agg(hb,halfids);halfd=agg(hd,halfids)
def pct(v):return 'n/a' if v is None else f'{100*v:.1f}%'
def pb(v):return '>5' if v is None else f'{v:.2f}'
out=['# Project economics — decision review, 11 November 2026','',
'Working comparison only. The active workbook, report and graphics are unchanged. All project benefits and costs remain planning assumptions. Figures below use the existing tax/FX convention; downside is a new operational candidate, not a calibrated probability or an approved forecast.',
'', '| Project | Gross cost USD m | Base IRR / hurdle | Base payback years | Candidate downside IRR | Downside cumulative Y5 USD m | Decision and decisive evidence |',
'| --- | ---: | --- | ---: | ---: | ---: | --- |']
for r in rows:
    k=r['id'];c=cases[k]
    out.append(f"| {k} | {r['cost']:.3f} | {pct(r['base']['irr'])} / {pct(c['rate'])} | {pb(r['base']['payback']) if k not in ['P12','E01'] else 'n/a'} | {pct(r['down']['irr'])} | {r['down']['cash5']:+.3f} | {r['note']} |")
out+=['','## Portfolio tests', '', '| Scope | Base IRR | Downside IRR | Base NPV at 10%, USD m | Downside NPV at 10%, USD m | Downside cumulative Y5, USD m |','| --- | ---: | ---: | ---: | ---: | ---: |']
for name,b,dc in [('Full selected portfolio',fullbase,fulldown),('Existing constrained half-scope',halfb,halfd)]:
    bm=metrics(b);dm=metrics(dc)
    out.append(f"| {name} | {pct(bm['irr'])} | {pct(dm['irr'])} | {bm['npv']:+.3f} | {dm['npv']:+.3f} | {dm['cash5']:+.3f} |")

# Retail investment ceiling for 3-year undiscounted payback, unchanged benefits and ramp.
c=cases['P13'];lo,hi=0,2
for _ in range(80):
    mid=(lo+hi)/2
    if sum(flows(c,initial=mid)[0][:4])>=0:lo=mid
    else:hi=mid
retail_cap=(lo+hi)/2*(c['c0']+c['c1']+c['launch'])
out+=['', '## Decisions before changing the model','',
f"1. Retain central P01/P02/P03 values for now; they already produce plausible short paybacks under their stated assumptions. P13 requires a one-time ceiling of about EUR {retail_cap:.3f}m for a three-year base payback with its current EUR 0.585m annual benefits, unchanged recurring costs and proportional initial-cost split. This is a procurement threshold to test, not a new price assumption.",
'2. Apply the candidate downside to each named operating lever, not a blanket one-year delay to every project. All candidates here also carry 10% higher initial and recurring costs. Retain a common risk narrative: slower execution, weaker capture and cost overruns. These numerical severities still need operational support; a positive result does not validate them.',
'3. A positive Y5 cumulative cash balance is not the same as clearing the hurdle. Keep both tests. Do not solve benefits backwards from a desired IRR.',
'4. Do not force every H1 into a 2–3-year downside payback or every project just above its hurdle. Require 2–3 years in the central case for cash-led H1; governance is a cost enabler. The portfolio downside must pass its own cumulative-cash test, including H3 and shared costs.',
'5. Cost completeness is not established. Map FDE allocation, business-owner backfill (50–100%), branch data engineering, site travel, cloud/licences and support onto existing project costs; add only the uncovered incremental amount. No trio-driven acceleration or benefit uplift is booked in this review.',
'6. Exclude the cost of inaction at this stage. No weights or expected IRR are assigned to the new candidate scenarios before downside and upside assumptions are agreed.',
'7. Current central tax treatment ignores loss carry-forwards and working capital; economic ownership is especially material for upstream/drilling. Confirm these before describing the case as investment-grade.',
'', '## Margin of safety at unchanged base timing', '',
'Annual gross benefit needed for zero NPV at each project hurdle. This is a diagnostic calculation, not a forecast or a continuation gate. Amounts are native USD m except P13 EUR m.', '']
for r in rows:
    if r['id'] not in ['P12','E01']:out.append(f"- {r['id']}: central {r['gross']:.3f}; break-even {r['gross_floor']:.3f}; headroom {100*(1-r['gross_floor']/r['gross']):.1f}%.")
out+=['','Reproduce with `python work/finance/project_economics_review.py`. Input: selected workbook Inputs. Output: this review only. No assumptions are written back into the workbook.']
(ROOT/'work/finance/project_economics_decision_review.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
print('\n'.join(out))
