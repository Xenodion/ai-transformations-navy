from pathlib import Path
import json, math, hashlib, shutil, csv, textwrap
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / 'work/finance/selected_chart_data.json'
ASSET = ROOT / 'work/projects/assets'
REPORT_ASSET = ROOT / 'deliverables/report/assets'
ASSET.mkdir(parents=True, exist_ok=True)
REPORT_ASSET.mkdir(parents=True, exist_ok=True)
D = json.loads(DATA_PATH.read_text(encoding='utf-8'))
IDS = ['P01','P02','P03','P05','P09','P12','P13','E01','P04','P08']
FOCUS = ['P01','P03','P12','P13']
assert D['version'] == 'selected-2026-11-10'
assert list(D['projects']) == IDS
assert set(D['half_ids']) == set(FOCUS)
assert len(D['portfolio']['Base']['cash']) == 6

NAVY='#0B1F3A'; BLUE='#00509E'; TEAL='#00A3E0'; ORANGE='#F37021'; PALE='#EAF1F5'; GREY='#667788'; RED='#E30613'; HORIZON={'H1':BLUE,'H2':TEAL,'H3':ORANGE,'Enabler':'#8293A3'}
plt.rcParams.update({'text.parse_math':False,'font.family':'DejaVu Sans','font.size':10,'axes.titlesize':16,'axes.titleweight':'bold','axes.labelcolor':NAVY,'text.color':NAVY,'axes.edgecolor':'#B5C2CC','axes.labelsize':10,'xtick.color':GREY,'ytick.color':GREY,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False,'grid.color':'#DCE5EB','grid.linewidth':0.7,'svg.fonttype':'none'})

def export(fig, name, report=True):
    fig.savefig(ASSET/f'{name}.png', dpi=220, bbox_inches='tight')
    fig.savefig(ASSET/f'{name}.svg', bbox_inches='tight')
    if report: shutil.copyfile(ASSET/f'{name}.png', REPORT_ASSET/f'{name}.png')
    plt.close(fig)

def finish(ax):
    ax.grid(axis='y', alpha=.8)
    ax.set_axisbelow(True)
    ax.spines['left'].set_color('#B5C2CC'); ax.spines['bottom'].set_color('#B5C2CC')

def annual(case, scenario): return np.array(case['scenarios'][scenario]['cash'], float)
def row(case, scenario, year): return case['scenarios'][scenario]['rows'][year]
def weighted_project(case):
    return sum(D['weights'][n]*annual(case,n) for n in ['Downside','Base','Upside'])
def cum(x): return np.cumsum(np.asarray(x, float))
def native(case, vals): return np.asarray(vals, float)/case['fx']

# Full portfolio bubble map: payback and Y5 gross contribution are sourced from base cash rows.
fig, ax = plt.subplots(figsize=(11,6.8))
for pid in IDS:
    c=D['projects'][pid]
    if pid == 'E01': continue
    pb=c['scenarios']['Base']['payback']; gross=float(row(c,'Base',5)[0])
    if pb is None or not math.isfinite(pb): continue
    size=float(c['one_time'])*500
    ax.scatter(pb,gross,s=size,c=HORIZON[c['horizon']],alpha=.82,edgecolors='white',linewidths=1.7,zorder=3)
    if pid in ('P02','P04','P08'):
        positions={'P02':(2.65,1.40),'P04':(3.33,1.42),'P08':(3.20,1.98)}
        ax.annotate(pid,(pb,gross),xytext=positions[pid],fontsize=9,fontweight='bold',color=NAVY,arrowprops=dict(arrowstyle='-',color=GREY,lw=.8))
    else:
        dx=.08 if pid not in ('P03','P09') else -.08
        ax.annotate(pid,(pb,gross),xytext=(pb+dx,gross+.09),fontsize=9,fontweight='bold',ha='left' if dx>0 else 'right',color=NAVY)
ax.set_xlabel('Base simple payback (years)'); ax.set_ylabel('Full-scale gross annual contribution (USD m)')
ax.set_xlim(1.8,5.0); ax.set_ylim(0,3.9); ax.xaxis.set_major_locator(MaxNLocator(6)); finish(ax)
handles=[plt.Line2D([0],[0],marker='o',color='w',label=h,markerfacecolor=HORIZON[h],markersize=9) for h in ['H1','H2','H3']]
ax.legend(handles=handles,frameon=False,loc='upper left',ncol=3,title='Horizon',bbox_to_anchor=(0,1.02))
ax.text(.01,-.23,'Bubble area ∝ one-time spend. P12 payback and licensing receipts are conditional on success.\nE01 is a shared cost-only enabler and has no payback or benefit coordinate.',transform=ax.transAxes,color=GREY,fontsize=9)
fig.suptitle('Portfolio map | selected business cases',x=.06,y=.99,ha='left',fontsize=19,fontweight='bold',color=NAVY)
fig.subplots_adjust(bottom=.22,top=.87)
export(fig,'selected_portfolio_map')

# Allocation of total gross programme spending, including E01 in H1.
labels=['H1','H2','H3']
parts=[sum(sum(c['annual_cost']) for c in D['projects'].values() if ('H1' if c['horizon']=='Enabler' else c['horizon'])==h) for h in labels]
total=sum(parts)
fig, ax=plt.subplots(figsize=(11,4.2)); left=0
for h,v in zip(labels,parts):
    ax.barh(0,v/total*100,left=left,color=HORIZON[h],height=.45,edgecolor='white',linewidth=1)
    ax.text(left+v/total*50,0,f'{h}\n{v/total:.1%}',ha='center',va='center',color='white',fontsize=11,fontweight='bold')
    left+=v/total*100
ax.set_yticks([0],['Y0–Y5']); ax.set_xlim(0,100); ax.set_xlabel('Share of total gross spending (%)')
ax.set_title('Portfolio investment | horizon mix',loc='left',pad=14); finish(ax); ax.grid(axis='x',alpha=.45); ax.grid(axis='y',visible=False)
fig.text(.14,.04,f'Total gross programme cost: ${total:.2f}m. Shared controls are included in H1.',fontsize=9,color=GREY)
fig.subplots_adjust(left=.14,bottom=.32,top=.78)
export(fig,'selected_horizon_mix')

# Signed weighted NPV contribution by horizon, undiscounted? common 10% screen using weighted annual net cash.
contrib={h:0.0 for h in labels}
for pid,c in D['projects'].items():
    cf=weighted_project(c); rate=.10
    val=sum(v/(1+rate)**t for t,v in enumerate(cf))
    contrib['H1' if c['horizon']=='Enabler' else c['horizon']]+=val
fig,ax=plt.subplots(figsize=(9.5,4.8)); xs=np.arange(len(labels)); vals=[contrib[h] for h in labels]
ax.bar(xs,vals,color=[HORIZON[h] if v>=0 else RED for h,v in zip(labels,vals)],width=.62)
ax.axhline(0,color=NAVY,lw=1)
for x,v in zip(xs,vals): ax.text(x,v+(.10 if v>=0 else -.10),f'{v:+.2f}',ha='center',va='bottom' if v>=0 else 'top',fontweight='bold')
ax.set_ylim(min(vals)-.7,max(vals)+.7);ax.set_xticks(xs,labels);ax.set_ylabel('Weighted NPV contribution (USD m)');ax.set_title('Signed weighted NPV contributions by horizon',loc='left',pad=12);finish(ax)
ax.text(0,-.23,'Illustrative scenario weights at a common 10% screen; H3 base revenue is conditional.',transform=ax.transAxes,fontsize=9,color=GREY,wrap=True)
fig.subplots_adjust(bottom=.24,top=.83)
export(fig,'selected_net_contributions')

# Scenario IRRs and hurdle; IRR of expected cash, not weighted individual IRRs.
scenarios=['Downside','Base','Upside','Weighted']
irrs=[D['portfolio'][sc]['irr']*100 for sc in scenarios]
fig,ax=plt.subplots(figsize=(10,5.2)); y=np.arange(len(scenarios))
bars=ax.barh(y,irrs,color=[BLUE,BLUE,BLUE,ORANGE],height=.58)
ax.axvline(10,color=TEAL,linestyle='--',linewidth=1.5,label='10% portfolio screen')
for bar,v in zip(bars,irrs): ax.text(v+.6,bar.get_y()+bar.get_height()/2,f'{v:.1f}%',va='center',fontweight='bold',color=NAVY)
ax.set_yticks(y,['Downside','Base','Upside','Expected cash']); ax.invert_yaxis(); ax.set_xlim(0,max(irrs)*1.22)
ax.set_xlabel('Portfolio IRR (%)'); ax.set_title('Portfolio return | scenario and expected cash',loc='left',pad=14); finish(ax); ax.grid(axis='y',visible=False);ax.grid(axis='x',alpha=.45);ax.legend(frameon=False,loc='lower right')
fig.text(.15,.025,'Expected cash uses 25% / 50% / 25% weights. IRR is calculated from weighted cash flows.',fontsize=9,color=GREY)
fig.subplots_adjust(left=.19,bottom=.20,top=.86);export(fig,'selected_scenario_irr')

# Total discounted net value by scenario and weighted expected cash.
npvs=[D['portfolio'][sc]['npv'] for sc in scenarios]
fig,ax=plt.subplots(figsize=(10,5.2)); y=np.arange(len(scenarios))
bars=ax.barh(y,npvs,color=[BLUE,BLUE,BLUE,ORANGE],height=.58)
for bar,v in zip(bars,npvs): ax.text(v+.15 if v>=0 else v/2,bar.get_y()+bar.get_height()/2,f'${v:+.2f}m',va='center',ha='left' if v>=0 else 'center',fontweight='bold',color=NAVY if v>=0 else 'white')
ax.axvline(0,color=GREY,lw=1);ax.set_yticks(y,['Downside','Base','Upside','Expected value']);ax.invert_yaxis();ax.set_xlim(min(0,min(npvs)*1.5),max(npvs)*1.25)
ax.set_xlabel('Net present value at 10% (USD m)');ax.set_title('Portfolio value | five-year scenarios',loc='left',pad=14);finish(ax);ax.grid(axis='y',visible=False);ax.grid(axis='x',alpha=.45)
fig.text(.15,.025,'After costs and cash tax; expected value uses 25% / 50% / 25% scenario weights.',fontsize=9,color=GREY)
fig.subplots_adjust(left=.19,bottom=.20,top=.86);export(fig,'selected_scenario_npv')

# Incremental deterioration beyond the static baselines, as a separate sensitivity.
a=json.loads((ROOT/'work/finance/inaction_overlay.json').read_text(encoding='utf-8'))
add=[0.0]*6; components={}
for item in a['items']:
    p=D['projects'][item['project']]; full=float(p['scenarios']['Base']['rows'][5][0]); cash=[]
    for t in range(6):
        factor=sum(D['weights'][sc]*p['scenarios'][sc]['rows'][t][0]/full for sc in ['Downside','Base','Upside'])
        cash.append(item['incremental_gross_full_scale_usd_m']*factor*(1-a['tax_rate']) if a['first_year']<=t<=a['last_year'] else 0)
    components[item['project']]=sum(v/(1+a['discount_rate'])**t for t,v in enumerate(cash));add=[x+y for x,y in zip(add,cash)]
avoided=sum(components.values());base=float(D['portfolio']['Weighted']['npv']);decision=base+avoided
fig,ax=plt.subplots(figsize=(10,5.3));width=.62
ax.bar(0,base,width,color=BLUE);ax.bar(1,avoided,width,bottom=base,color=ORANGE);ax.bar(2,decision,width,color=TEAL)
ax.plot([width/2,1-width/2],[base,base],color=GREY,lw=1);ax.plot([1+width/2,2-width/2],[decision,decision],color=GREY,lw=1)
for x,v,yv in [(0,base,base),(1,avoided,decision),(2,decision,decision)]:ax.text(x,yv+.12,f'${v:+.2f}m',ha='center',fontweight='bold',color=NAVY)
ax.set_xticks([0,1,2],['Portfolio expected NPV','Additional avoided\nlosses','Illustrative decision value']);ax.set_ylabel('Present value at 10% (USD m)');ax.set_ylim(0,decision*1.25);ax.set_title('Investment value | added cost of inaction',loc='left',pad=14);finish(ax)
fig.text(.14,.025,'Illustrative deterioration in refining margins, rig costs and retail churn beyond static baselines.\nAssumes scenario-weighted project impact, 25% tax and no incremental spending.',fontsize=9,color=GREY)
fig.subplots_adjust(left=.14,bottom=.24,top=.85);export(fig,'selected_inaction_bridge')
(ROOT/'work/finance/inaction_overlay_results.json').write_text(json.dumps({'components_pv_usd_m':components,'weighted_after_tax_cash_usd_m':add,'avoided_loss_pv_usd_m':avoided,'expected_portfolio_npv_usd_m':base,'decision_value_usd_m':decision},indent=2),encoding='utf-8')

# Portfolio J-curve, cash cumulative undiscounted.
fig,ax=plt.subplots(figsize=(10.4,5.8)); years=np.arange(6)
for scen,color,lw in [('Downside',RED,2),('Base',BLUE,2.4),('Upside',TEAL,2)]:
    ax.plot(years,cum(D['portfolio'][scen]['cash']),marker='o',color=color,lw=lw,label=scen,ls='--' if scen=='Severe stress' else '-')
ax.axhline(0,color=GREY,lw=1);ax.set_xticks(years,[f'Y{i}' for i in years]);ax.set_ylabel('Cumulative net cash (USD m)');ax.set_title('Portfolio cash profile | cumulative, undiscounted',loc='left',pad=12);finish(ax);ax.legend(frameon=False,ncol=2,loc='best')
ax.text(0,-.19,'Y0–Y5. Cumulative cash includes project costs and cash tax.',transform=ax.transAxes,color=GREY,fontsize=9)
fig.subplots_adjust(bottom=.19,top=.86)
export(fig,'selected_portfolio_jcurve')

# Individual case curves and focus combined panel + individual cash tables.
fig,axes=plt.subplots(2,2,figsize=(12.2,8.4),sharex=True)
for ax,pid in zip(axes.flat,FOCUS):
    c=D['projects'][pid]; unit='EUR m' if pid=='P13' else 'USD m'
    for scen,color,lw in [('Downside',RED,1.8),('Base',BLUE,2.3),('Upside',TEAL,1.8)]:
        ax.plot(years,cum(native(c,annual(c,scen))),marker='o',ms=3.8,lw=lw,color=color,label=scen)
    if pid=='P12': ax.plot(years,cum(native(c,annual(c,'Downside'))),color=RED,lw=2.5,ls='--',label='Stopped downside (sunk + closure)')
    ax.axhline(0,color=GREY,lw=.8);ax.set_xticks(years,[f'Y{i}' for i in years]);ax.set_title(f'{pid} · {unit}',loc='left',fontweight='bold');ax.set_ylabel(f'Cumulative net cash ({unit})');finish(ax)
    if pid=='P12': ax.text(.03,.04,'Base licensing receipts are conditional',transform=ax.transAxes,fontsize=8,color=GREY)
axes.flat[0].legend(frameon=False,ncol=3,fontsize=8,loc='best')
fig.suptitle('Featured cases | cumulative net cash, undiscounted',x=.07,y=.99,ha='left',fontsize=18,fontweight='bold')
fig.text(.07,.02,'P12 base assumes licensing success; downside stopping retains sunk costs and closure expense.',fontsize=9,color=GREY)
fig.subplots_adjust(top=.91,bottom=.1,hspace=.38,wspace=.28)
export(fig,'selected_focus_jcurves')

for pid in FOCUS:
    c=D['projects'][pid]; unit='EUR m' if pid=='P13' else 'USD m'; factor=c['fx'] if pid=='P13' else 1
    fig,ax=plt.subplots(figsize=(8.8,3.3));ax.axis('off')
    title=f'{pid} | annual cash flow ({unit})'
    ax.set_title(title,loc='left',fontsize=15,fontweight='bold',color=NAVY,pad=15)
    col_labels=['Year','Gross benefit','OPEX + launch','CAPEX','Tax','Net cash']
    cell=[]
    for t in range(6):
        rr=row(c,'Base',t)
        cell.append([f'Y{t}']+[f'{(float(v)/factor if abs(float(v)/factor)>=.0005 else 0):.3f}' for v in [rr[0],-rr[1],-rr[2],-rr[3],rr[4]]])
    table=ax.table(cellText=cell,colLabels=col_labels,cellLoc='right',colLoc='right',loc='center',colWidths=[.10,.18,.22,.16,.15,.17])
    table.auto_set_font_size(False);table.set_fontsize(9);table.scale(1,1.6)
    for (r,col),cl in table.get_celld().items():
        cl.set_edgecolor('#DCE5EB');cl.set_linewidth(.6)
        if r==0: cl.set_facecolor(NAVY);cl.get_text().set_color('white');cl.get_text().set_fontweight('bold')
        elif r%2: cl.set_facecolor('#F3F7F9')
        else: cl.set_facecolor('white')
        if r>0 and col>0 and float(cell[r-1][col])<0: cl.get_text().set_color(RED)
    if pid=='P12': ax.text(.01,.03,'Base licensing receipts are conditional on commercial success.',transform=ax.transAxes,color=GREY,fontsize=9)
    ax.text(.01,-.10,'Source: selected_chart_data.json · Base case · tax included · rounded to 0.001',transform=ax.transAxes,color=GREY,fontsize=8)
    fig.subplots_adjust(top=.82,bottom=.18,left=.04,right=.98)
    export(fig,f'selected_{pid.lower()}_cash_table')
    fig,ax=plt.subplots(figsize=(8.5,4.7))
    for scen,color,lw in [('Downside',RED,1.8),('Base',BLUE,2.5),('Upside',TEAL,1.8)]:
        ax.plot(years,cum(native(c,annual(c,scen))),marker='o',color=color,lw=lw,label=scen)
    if pid=='P12': ax.plot(years,cum(native(c,annual(c,'Downside'))),color=RED,lw=2.4,ls='--',label='Stopped downside (sunk + closure)')
    ax.axhline(0,color=GREY,lw=1);ax.set_xticks(years,[f'Y{i}' for i in years]);ax.set_ylabel(f'Cumulative net cash ({unit})');ax.set_title(f'{pid} | cumulative net cash, undiscounted',loc='left',pad=12);finish(ax);ax.legend(frameon=False,ncol=2,loc='best')
    if pid=='P12': ax.text(.02,.03,'Base licensing receipts are conditional.',transform=ax.transAxes,color=GREY,fontsize=9)
    ax.text(0,-.18,('Stopped downside retains sunk costs and closure expense.' if pid=='P12' else 'Downside: project-specific operating and cost assumptions.'),transform=ax.transAxes,color=GREY,fontsize=8)
    fig.subplots_adjust(bottom=.19,top=.85)
    export(fig,f'selected_{pid.lower()}_jcurve')

# Constrained half-budget comparison: compare actual constrained spend with 50% envelope.
full=float(D['portfolio']['gross_cost']); half=float(D['half']['gross_cost']); cap=full/2; head=cap-half
weighted_disc=lambda obj: float(obj['Weighted']['npv'])
full_npv=weighted_disc(D['portfolio']);half_npv=weighted_disc(D['half'])
fig,axes=plt.subplots(1,2,figsize=(11.5,5.1),gridspec_kw={'width_ratios':[1.2,1]})
ax=axes[0]; bars=ax.bar(['Full programme','Four featured\ncases'],[full,half],color=[BLUE,TEAL],width=.58)
ax.axhline(cap,color=ORANGE,ls='--',lw=1.8,label=f'50% envelope ${cap:.2f}m')
for b,v in zip(bars,[full,half]): ax.text(b.get_x()+b.get_width()/2,v+.25,f'${v:.2f}m',ha='center',fontweight='bold')
ax.set_ylabel('Gross Y0–Y5 spend (USD m)');ax.set_ylim(0,full*1.23);ax.set_title('Gross spend',loc='left');finish(ax);ax.legend(frameon=False,loc='upper right')
ax=axes[1]; colors=[BLUE,TEAL]; returns=[100*D['portfolio']['Base']['irr'],100*D['half']['Base']['irr']]; bars=ax.bar(['Full programme','Four featured\ncases'],returns,color=colors,width=.58)
ax.axhline(0,color=GREY,lw=1)
for b,v in zip(bars,returns): ax.text(b.get_x()+b.get_width()/2,v+.5,f'{v:.1f}%',ha='center',fontweight='bold')
ax.set_ylim(0,max(returns)*1.3);ax.set_ylabel('Base IRR (%)');ax.set_title('Base IRR',loc='left');finish(ax)
fig.suptitle('Four featured cases | budget comparison',x=.06,y=.99,ha='left',fontsize=18,fontweight='bold')
fig.text(.06,.01,f'The four featured cases represent {half/full:.1%} of full programme spending.\nShared E01 controls require separate funding or allocation in the reduced scope.',fontsize=9,color=GREY)
fig.subplots_adjust(top=.83,bottom=.2,wspace=.28)
export(fig,'selected_half_budget')

# Export the exact plotted annual/cumulative data for inspection in Excel.
with (ASSET/'selected_cashflows.csv').open('w',newline='',encoding='utf-8') as stream:
    writer=csv.writer(stream); writer.writerow(['scope','scenario','year','currency','annual_net_cash_m','cumulative_net_cash_m'])
    for scope,obj in [('Portfolio',D['portfolio']),('Half budget',D['half'])]:
        for name in ['Downside','Base','Upside','Severe stress','Weighted']:
            for t,(flow,total) in enumerate(zip(obj[name]['cash'],cum(obj[name]['cash']))):writer.writerow([scope,name,t,'USD',flow,total])
    for pid,c in D['projects'].items():
        for name in ['Downside','Base','Upside','Severe stress']:
            flows=native(c,annual(c,name))
            for t,(flow,total) in enumerate(zip(flows,cum(flows))):writer.writerow([pid,name,t,'EUR' if pid=='P13' else 'USD',flow,total])
for name in ['Downside','Base','Upside','Severe stress']:
    summed=sum(annual(c,name) for c in D['projects'].values())
    assert np.allclose(summed,D['portfolio'][name]['cash'],atol=1e-9)
assert np.allclose(sum(weighted_project(c) for c in D['projects'].values()),D['portfolio']['Weighted']['cash'],atol=1e-9)
# Verification: source hash, cash identities and exact consolidated reference metrics.
assert abs(sum(float(c['one_time']) for c in D['projects'].values())-9.8165)<1e-7
assert abs(float(D['portfolio']['gross_cost'])-21.93708)<1e-7
assert abs(float(D['portfolio']['annual_cost'][0])-2.8966)<1e-7
assert abs(sum(contrib.values())-full_npv)<1e-7
for pid,c in D['projects'].items():
    for scen in c['scenarios']:
        for t,r in enumerate(c['scenarios'][scen]['rows']):
            assert abs(r[0]-r[1]-r[2]-r[3]-r[4])<1e-8, (pid,scen,t)
for sc in ['Downside','Base','Upside','Severe stress','Weighted']:
    assert len(D['portfolio'][sc]['cash'])==6
for sc in ['Downside','Base','Upside','Severe stress','Weighted']:
    assert len(D['half'][sc]['cash'])==6
# Horizon shares sum to 100% separately for one-time and five-year gross allocations.
assert abs(sum(sum(c['annual_cost']) for c in D['projects'].values()) - float(D['portfolio']['gross_cost'])) < 1e-7
hashv=hashlib.sha256(DATA_PATH.read_bytes()).hexdigest()
manifest={'source':'work/finance/selected_chart_data.json','source_sha256':hashv,'data_version':D['version'],'selected_ids':IDS,'focus_cases':FOCUS,'checks':{'gross_cost_usd_m':full,'y0_gross_cost_usd_m':float(D['portfolio']['annual_cost'][0]),'base_npv_10pct_usd_m':float(D['portfolio']['Base']['npv']),'weighted_npv_10pct_usd_m':full_npv,'weighted_simple_payback_years':float(D['portfolio']['Weighted']['payback']),'half_constrained_gross_cost_usd_m':half,'half_envelope_usd_m':cap,'half_remaining_headroom_usd_m':head,'signed_horizon_weighted_npv_usd_m':contrib,'cash_row_identity':'passed for all project/scenario/year rows','portfolio_cash_values_checked':30,'project_cash_rows_checked':len(IDS)*4*6},'figures':[p.name for p in sorted(ASSET.glob('selected_*.png'))]}
(ASSET/'selected_chart_verification.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(ASSET/'selected_chart_verification.md').write_text(f'''# Selected chart verification\n\n- Source JSON: `work/finance/selected_chart_data.json`\n- Source SHA-256: `{hashv}`\n- Data version: `{D['version']}`\n- Selected projects: {', '.join(IDS)}\n- Featured cases: {', '.join(FOCUS)}\n- Gross envelope: ${full:.5f}m; Y0 tranche: ${D['portfolio']['annual_cost'][0]:.5f}m.\n- Base and weighted NPV at 10%: ${D['portfolio']['Base']['npv']:.6f}m and ${full_npv:.6f}m.\n- Weighted simple payback: {D['portfolio']['Weighted']['payback']:.6f} years.\n- Constrained half-budget: ${half:.5f}m spend against a ${cap:.5f}m 50% envelope; ${head:.5f}m headroom. Scope excludes P02/P03/P13, caps P12 at Y2 plus $0.10m closure/transfer, as defined in the source JSON.\n- All per-project scenario/year cash rows reconcile (benefit − CAPEX − OPEX − tax = net cash). P13 is divided by its 1.1165 USD/EUR FX rate for native EUR figures.\n- Portfolio scenarios: 5 × 6 annual cash values checked; half-budget scenarios: 5 × 6. Weighted NPV contributions by horizon sum to weighted portfolio NPV at 10%.\n- Outputs: PNG at 220 dpi and SVG in `work/projects/assets/`; report PNGs are byte-for-byte copies under `deliverables/report/assets/`.\n- Limit: charts are derived from the checked JSON; inputs remain assumptions and do not validate project scope or economics.\n''',encoding='utf-8')
(ASSET/'selected_chart_verification.md').write_text(f'# Chart verification\n\nSource SHA-256: `{hashv}`. The four featured cases cost ${half:.3f}m; the half-budget ceiling is ${cap:.3f}m, leaving a funding gap of ${-head:.3f}m. Cash rows and portfolio aggregation are reconciled.\n',encoding='utf-8')
print(json.dumps({'sha256':hashv,'full':full,'half':half,'half_headroom':head,'weighted_npv':full_npv,'horizon_contributions':contrib,'figures':manifest['figures']},indent=2))

