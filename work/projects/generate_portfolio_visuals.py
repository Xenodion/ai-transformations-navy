"""Generate decision visuals from the *cached*, recalculated Excel workbook.

Read-only workbook access: the financial model is never rewritten. Recalculate
and save it in Excel before running this script after changing assumptions.
Amounts are nominal USD millions except the P13 focus chart, which uses EUR.
"""
from collections import defaultdict
from math import sqrt
from pathlib import Path
import json
import openpyxl
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / 'finance' / 'portfolio_model_14_revised.xlsx'
OUT = Path(__file__).resolve().parent / 'assets'
OUT.mkdir(exist_ok=True)
book = openpyxl.load_workbook(MODEL, data_only=True)
inp, calc, metrics, portfolio = (book[x] for x in ('Inputs','Cash flow build','Metrics','Portfolio'))
INK, MUTED, BG, GRID = '#15283f', '#57697d', '#f2f5f9', '#d7e0eb'
COLORS = {'H1':'#1763a1','H2':'#ed8a27','H3':'#8054a5','Enabler':'#7b8899'}
CASE_COLORS = {'Downside':'#bc5348','Base':'#1763a1','Upside':'#30a086'}
FONT = 'C:/Windows/Fonts/segoeui.ttf'
BOLD = 'C:/Windows/Fonts/segoeuib.ttf'

def ft(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT,size)

def text(draw, xy, value, size=24, color=INK, bold=False, anchor=None):
    draw.text(xy, str(value), font=ft(size,bold), fill=color, anchor=anchor)

def frame(title, subtitle, width=2000, height=1200):
    im=Image.new('RGB',(width,height),BG); d=ImageDraw.Draw(im)
    text(d,(55,30),title,36,INK,True);text(d,(58,88),subtitle,21,MUTED)
    return im,d

def save(im,name):
    im.save(OUT/name, optimize=True)

weights=[portfolio.cell(17,c).value for c in (2,3,4)]
if abs(sum(weights)-1)>1e-9 or any(x<0 for x in weights):
    raise ValueError('Scenario weights must be nonnegative and sum to 100%')
rows=[]
for n in range(14):
    r=n+2; ident=inp.cell(r,1).value; horizon=inp.cell(r,3).value
    fx=inp.cell(r,5).value; included=inp.cell(r,21).value
    if included not in (0,1): raise ValueError('Include controls must be 0 or 1')
    investment=sum(inp.cell(r,c).value for c in (7,8,9))*fx*included
    # Y1–Y5 benefits before OPEX and tax; scenario weights are judgmental.
    benefit=[]
    for s in range(3):
        start=2+(3*n+s)*7
        benefit.append(sum(calc.cell(start+1,c).value for c in range(3,8))*included)
    gross=inp.cell(r,15).value*fx*inp.cell(r,6).value
    metricrow=2+3*n+1
    payback=metrics.cell(metricrow,7).value
    rows.append(dict(id=ident,horizon=horizon,investment=investment,gross=gross,
                     payback=payback,benefit=benefit,include=included,
                     expected=sum(x*w for x,w in zip(benefit,weights))))
if [x['id'] for x in rows] != [f'P{x:02}' for x in range(1,14)]+['E01']:
    raise ValueError('Unexpected portfolio project set')

def portfolio_map():
    im,d=frame('AI portfolio | projects, payback and long-term options',
        'Base scenario · illustrative assumptions · bubble area = initial investment · USD million')
    x0,x1,y0,y1=150,1230,225,780
    d.rounded_rectangle((55,140,1270,890),radius=18,fill='white',outline=GRID,width=2)
    text(d,(105,166),'H1 / H2: modeled 5-year payback',25,INK,True)
    text(d,(105,200),'Gross annual benefit at full adoption, before OPEX and tax ($m)',19,MUTED)
    def pt(x,y): return (x0+(x/5)*(x1-x0),y1-y/3.25*(y1-y0))
    for x in range(6):
        xx,_=pt(x,0); d.line((xx,y0,xx,y1),fill=GRID,width=2);text(d,(xx,y1+12),x,20,MUTED,anchor='mt')
    for y in (0,.5,1,1.5,2,2.5,3):
        _,yy=pt(0,y);d.line((x0,yy,x1,yy),fill=GRID,width=2);text(d,(x0-16,yy),f'{y:.1f}',19,MUTED,anchor='rm')
    text(d,((x0+x1)/2,840),'Simple payback (years, interpolated from annual cash flow)',20,MUTED,anchor='mm')
    offsets={'P01':(-70,-48),'P02':(-70,-50),'P03':(18,-26),'P04':(-105,23),'P05':(-70,-49),
             'P06':(27,19),'P08':(25,-48),'P09':(25,-45),'P13':(-40,35)}
    for item in rows:
        if not item['include'] or item['horizon'] not in ('H1','H2') or not isinstance(item['payback'],(int,float)): continue
        x,y=pt(item['payback'],item['gross']);radius=24*sqrt(item['investment'])
        d.ellipse((x-radius,y-radius,x+radius,y+radius),fill=COLORS[item['horizon']],outline='white',width=3)
        dx,dy=offsets.get(item['id'],(15,-30)); lx,ly=x+dx,y+dy
        d.line((x,y,lx+18,ly+12),fill='#8a9bad',width=2)
        d.ellipse((x-radius,y-radius,x+radius,y+radius),fill=COLORS[item['horizon']],outline='white',width=3)
        text(d,(lx,ly),item['id'],21,INK,True)
    d.rounded_rectangle((1300,140,1945,890),radius=18,fill='white',outline=GRID,width=2)
    text(d,(1332,165),'H3 | long-term options',27,INK,True)
    text(d,(1332,210),'Shown separately: no invented payback.',20,MUTED)
    for yy,ident in [(286,'P11'),(416,'P12')]:
        item=next(q for q in rows if q['id']==ident);radius=24*sqrt(item['investment'])
        d.ellipse((1365-radius,yy-radius,1365+radius,yy+radius),fill=COLORS['H3'],outline='white',width=3)
    text(d,(1410,260),'P11  Customer flexibility',23,COLORS['H3'],True)
    text(d,(1410,297),'Conditional $3.75m/year at 250 MW;',19,INK)
    text(d,(1410,327),'commercial scope remains to be proven.',19,INK)
    text(d,(1410,390),'P12  e-SAF catalyst discovery',23,COLORS['H3'],True)
    text(d,(1410,427),'No monetary benefit or maturity date',19,INK)
    text(d,(1410,457),'estimated in the five-year model.',19,INK)
    text(d,(1332,526),'Other initiatives outside the plot',22,INK,True)
    for y,line in enumerate(['P07: safety benefit not booked as cash',
                              'P10: no payback within five years',
                              'E01: shared governance cost only']):text(d,(1332,565+y*37),line,19,INK)
    text(d,(1332,708),'H1',22,COLORS['H1'],True);text(d,(1400,708),'H2',22,COLORS['H2'],True);text(d,(1470,708),'H3',22,COLORS['H3'],True)
    text(d,(1332,765),'All 14 initiatives are represented;',19,MUTED)
    text(d,(1332,794),'no approved investment is implied.',19,MUTED)
    # A separate timeline prevents years beyond the financial window from
    # being presented as measured paybacks or specific maturity dates.
    d.rounded_rectangle((55,920,1945,1138),radius=18,fill='white',outline=GRID,width=2)
    text(d,(85,942),'H3 horizon',22,INK,True)
    text(d,(140,978),'Y0',18,MUTED,anchor='mt');text(d,(960,978),'Y5',18,MUTED,anchor='mt');text(d,(1780,978),'Y10+',18,MUTED,anchor='mt')
    d.line((140,1020,1780,1020),fill=GRID,width=8)
    d.line((140,1020,960,1020),fill=COLORS['H3'],width=8)
    for x in range(975,1770,45):d.line((x,1020,x+24,1020),fill=COLORS['H3'],width=5)
    d.line((960,987,960,1060),fill=INK,width=2)
    text(d,(95,1068),'Modelled valuation window',19,MUTED)
    text(d,(1000,1068),'Beyond Y5: timing and commercial value not estimated',19,MUTED)
    save(im,'portfolio_bubble.png')

def mix_chart():
    im,d=frame('Portfolio mix | funding and expected gross benefits',
        'Same 14 initiatives · USD million · 25% / 50% / 25% scenario weights are assumptions',1900,970)
    d.rounded_rectangle((55,140,1845,875),radius=18,fill='white',outline=GRID,width=2)
    vals={k:sum(x['investment'] for x in rows if x['horizon']==k) for k in COLORS}
    returns={k:sum(x['expected'] for x in rows if x['horizon']==k) for k in COLORS}
    def bar(y,headline,items):
        total=sum(items.values()); text(d,(110,y-70),f'{headline}  |  ${total:,.2f}m',25,INK,True)
        start=110; width=1590
        for k in COLORS:
            val=items[k];x2=start+width*val/total
            if val>0:
                d.rectangle((round(start),y,round(x2),y+82),fill=COLORS[k])
                if x2-start>100:text(d,((start+x2)/2,y+41),f'{k} {val/total:.1%}',20,'white',True,'mm')
            start=x2
        return total
    capital_total=bar(270,'One-time investment (CAPEX + launch; excludes recurring cost)',vals)
    benefit_total=bar(530,'Probability-weighted gross cash benefits, Y1–Y5',returns)
    for j,k in enumerate(COLORS):
        x=110+j*405;d.rounded_rectangle((x,666,x+25,691),radius=4,fill=COLORS[k]);text(d,(x+37,665),k,20,INK,True)
        text(d,(x+37,700),f'Investment ${vals[k]:.2f}m',18,MUTED)
        text(d,(x+37,730),f'Gross benefits ${returns[k]:.2f}m',18,MUTED)
    text(d,(110,800),'Gross benefits are before OPEX, capital spending and tax; this is not a mix of net returns or NPVs.',19,MUTED)
    text(d,(110,830),'P11 benefits are conditional; P12 has no monetized benefit. E01 is shared cost only.',19,MUTED)
    save(im,'portfolio_mix.png')
    return vals, returns, capital_total, benefit_total

def curves():
    selected=[('P01','Refining predictive maintenance',0),('P03','Deepwater drilling advisory',2),
              ('P11','Customer flexibility — conditional',10),('P13','Retail demand pilot',12)]
    for ident,title,n in selected:
        unit='EUR million' if ident=='P13' else 'USD million';fx=inp.cell(n+2,5).value if ident=='P13' else 1
        im,d=frame(f'{ident} | {title}',f'Cumulative cash flow · {unit} · discounted metrics use the project hurdle',1500,900)
        d.rounded_rectangle((55,140,1445,810),radius=18,fill='white',outline=GRID,width=2)
        x0,x1,y0,y1=160,1370,235,690
        series={}
        for j,name in enumerate(('Downside','Base','Upside')):
            r=2+(3*n+j)*7;series[name]=[calc.cell(r+6,c).value/fx for c in range(2,8)]
        allv=[v for vlist in series.values() for v in vlist]+[0];lo=min(allv)-.3;hi=max(allv)+.3
        def pt(t,v):return (x0+(x1-x0)*t/5,y1-(y1-y0)*(v-lo)/(hi-lo))
        for t in range(6):
            x,_=pt(t,0);d.line((x,y0,x,y1),fill=GRID,width=2);text(d,(x,y1+13),f'Y{t}',20,MUTED,anchor='mt')
        for k in range(5):
            v=lo+(hi-lo)*k/4;_,y=pt(0,v);d.line((x0,y,x1,y),fill=GRID,width=2);text(d,(x0-12,y),f'{v:.1f}',19,MUTED,anchor='rm')
        _,z=pt(0,0);d.line((x0,z,x1,z),fill='#7b8899',width=2)
        for j,(name,vals) in enumerate(series.items()):
            points=[pt(t,v) for t,v in enumerate(vals)];d.line(points,fill=CASE_COLORS[name],width=5)
            for x,y in points:d.ellipse((x-5,y-5,x+5,y+5),fill=CASE_COLORS[name])
            x=180+j*300;d.line((x,760,x+38,760),fill=CASE_COLORS[name],width=6);text(d,(x+50,747),name,20,INK)
        if ident=='P11':text(d,(1080,748),'H3: no payback asserted',18,MUTED)
        save(im,f'{ident.lower()}_jcurve.png')

def portfolio_curve():
    im,d=frame('14 initiatives | cumulative portfolio cash flow',
               'USD million · unlevered after-tax cash · three assumption-based scenarios',1500,900)
    d.rounded_rectangle((55,140,1445,810),radius=18,fill='white',outline=GRID,width=2)
    x0,x1,y0,y1=160,1370,235,690
    series={name:[portfolio.cell(6+t,2+j).value for t in range(6)] for j,name in enumerate(('Downside','Base','Upside'))}
    allv=[v for s in series.values() for v in s]+[0];lo=min(allv)-1;hi=max(allv)+1
    def pt(t,v):return (x0+(x1-x0)*t/5,y1-(y1-y0)*(v-lo)/(hi-lo))
    for t in range(6):
        x,_=pt(t,0);d.line((x,y0,x,y1),fill=GRID,width=2);text(d,(x,y1+13),f'Y{t}',20,MUTED,anchor='mt')
    for k in range(5):
        v=lo+(hi-lo)*k/4;_,y=pt(0,v);d.line((x0,y,x1,y),fill=GRID,width=2);text(d,(x0-12,y),f'{v:.1f}',19,MUTED,anchor='rm')
    _,z=pt(0,0);d.line((x0,z,x1,z),fill='#7b8899',width=2)
    for j,(name,vals) in enumerate(series.items()):
        points=[pt(t,v) for t,v in enumerate(vals)];d.line(points,fill=CASE_COLORS[name],width=5)
        for x,y in points:d.ellipse((x-5,y-5,x+5,y+5),fill=CASE_COLORS[name])
        x=180+j*300;d.line((x,760,x+38,760),fill=CASE_COLORS[name],width=6);text(d,(x+50,747),name,20,INK)
    save(im,'portfolio_jcurve.png')

def net_contributions():
    values=defaultdict(float)
    for n,item in enumerate(rows):
        values[item['horizon']]+=item['include']*sum(weights[j]*metrics.cell(2+3*n+j,5).value for j in range(3))
    total=sum(values.values())
    if abs(total-portfolio['B18'].value)>1e-7:raise ValueError('Net horizon NPV does not reconcile')
    im,d=frame('Portfolio | weighted net value by horizon',
               'Scenario-weighted sum of project NPVs, each at its own hurdle · USD million',1700,790)
    d.rounded_rectangle((55,140,1645,700),radius=18,fill='white',outline=GRID,width=2)
    x0=750;scale=170;d.line((x0,230,x0,570),fill='#889bad',width=2)
    for j,k in enumerate(COLORS):
        y=220+j*85;v=values[k];text(d,(120,y+24),k,24,INK,True)
        x=x0+v*scale;d.rounded_rectangle((min(x,x0),y,max(x,x0),y+52),radius=4,fill=COLORS[k])
        text(d,(x+15 if v>=0 else x-15,y+25),f'${v:+.2f}m',21,INK,True,'lm' if v>=0 else 'rm')
    text(d,(120,610),f'Sum = ${total:+.2f}m  |  P11 income is conditional; P12 and E01 are cost-only within Y0–Y5.',20,MUTED)
    text(d,(120,644),'Negative contributions are shown as negative; no 100% positive-share transformation is applied.',19,MUTED)
    save(im,'portfolio_net_contributions.png')
    return dict(values)

portfolio_map(); investments, benefits, initial, gross = mix_chart();curves();portfolio_curve();net_values=net_contributions()
summary={'weights':weights,'investment_by_horizon':investments,'expected_gross_benefits_by_horizon':benefits,
         'one_time_total':initial,'expected_gross_benefits_total':gross,'weighted_net_npv_by_horizon':net_values,'projects':rows}
(OUT/'visuals_data.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps({'investment':investments,'gross_benefits':benefits,'gross_total':gross},indent=2))
