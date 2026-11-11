"""One-time migration preserving the existing workbook calculation architecture."""
from pathlib import Path
import shutil, re

root = Path(__file__).resolve().parents[2]
archive = root/'work/archive/pre_selection_2026_11_10'
archive.mkdir(parents=True, exist_ok=True)
paths = ['deliverables/report/full_strategy_report_draft.md','work/finance/build_workbook.mjs','work/finance/portfolio_model_14_revised.xlsx','work/finance/portfolio_model_14_notes.md','work/finance/portfolio_economics.md','work/finance/half_envelope_alternative.md','work/finance/cost_of_inaction.md','work/projects/reserve_cards.md','work/projects/portfolio_sequencing_canvas.md','work/projects/portfolio_visuals.md','work/projects/portfolio_charts.ipynb']
for p in paths:
    target=archive/p
    target.parent.mkdir(parents=True,exist_ok=True)
    if not target.exists(): shutil.copy2(root/p,target)
s=(root/'work/finance/build_workbook.mjs').read_text(encoding='utf-8')
keep=['P01','P02','P03','P05','P09','P12','P13','E01']
s=re.sub(r"^ \['(P\d+|E01)'.*\n",lambda m:m[0] if m[1] in keep else '',s,flags=re.M)
s=s.replace('e-SAF catalyst option','e-SAF technology licensing option')
# Retain cost assumptions. Retail central case excludes unproven urgent-delivery cash.
s=s.replace('],.825,[.50','],.585,[.50')
s=s.replace("['Urgent delivery reduction',.50]","['Urgent delivery reduction',0]")
s=s.replace("['Cash capture fraction',.60]","['Cash capture fraction (ownership x avoidability)',.60]")
s=s.replace("f(inputs,'O12',\"='Focus drivers'!B16\");",'')
s=s.replace("f(inputs,'O14'","f(inputs,'O8'")
s=s.replace("['P11 | customer flexibility MW',250],['Retained margin USD m per MW / yr',.015],['P11 conditional gross USD m / yr',null]","['P03 economic share assumption',.80],['P03 avoidable payment fraction',.75],['P03 combined capture',null]")
s=s.replace("f(drivers,'B16','=B14*B15');","f(drivers,'B16','=B14*B15');f(drivers,'B12','=B16');")
s=re.sub(r" \['P11 flexibility'.*\n",'',s)
s=s.replace("A1:M5","A1:M4")
s=s.replace("['P01','P03','P11','P13']","['P01','P03','P12','P13']")
# Operational downside: one year benefit delay, 25% lower unit gains and 15% costs.
s=s.replace("name==='Downside'?.90","name==='Downside'?.75").replace("name==='Downside'?1.05","name==='Downside'?1.15")
start=s.index('for(let i=0;i<data.length;i++)for(let j=0;j<3;j++)for(let y=0;y<5;y++){')
end=s.index('const stress=',start)
s=s[:start]+'''for(let i=0;i<data.length;i++)for(let j=0;j<3;j++)for(let y=0;y<5;y++){
 const addr=`${String.fromCharCode(71+y)}${2+i*3+j}`;
 f(scenarios,addr,j===0?(y===0?'=0':`=Inputs!${String.fromCharCode(79+y)}${2+i}`):`=MIN(1,Inputs!${String.fromCharCode(80+y)}${2+i}*${j===2?1.15:1})`);
}
''' + s[end:]
for a,b in [('A2:U15','A2:U9'),('D2:U15','D2:U9'),('D2:D15','D2:D9'),('G2:O15','G2:O9'),('P2:T15','P2:T9'),('A2:N43','A2:N25'),('C2:N43','C2:N25'),('C2:M43','C2:M25'),('N2:N43','N2:N25'),('A44:N57','A26:N33'),('C44:N57','C26:N33'),('C44:M57','C26:M33'),('44+i','26+i')]: s=s.replace(a,b)
s=s.replace('14-INITIATIVE','8-INITIATIVE').replace('14 initiatives','8 initiatives').replace('14 indicative','8 indicative').replace('All 14 projects','All 8 projects').replace('all 14 projects','all 8 projects').replace('nine estimates','three estimates')
s=s.replace('portfolio_model_14_revised.xlsx','portfolio_model_selected.xlsx')
s=s.replace('90% benefits, 105% costs','75% benefits, 115% costs, one-year benefit delay')
s=s.replace('Four cases are detailed; other project inputs are rough estimates.','Four cases are detailed; other project inputs are rough estimates. No inaction uplift is booked.')
# Remove obsolete P11 assertions from explanatory strings.
s=s.replace('P11 conditional commercial receipts are scenario assumptions, not committed revenue; edit its scenario realisation factor.','P12 tests third-party technology licensing; no commercial receipts are booked.')
s=s.replace('P07 avoided incidents are not booked as certain cash; E01 is cost-only.','P12 and E01 are cost-only.')
s=s.replace('P11 conditional revenue depends on each scenario.','P12 carries costs but no commercial revenue.')
s=s.replace('P11 revenues are conditional assumptions; downside H3 stop retains exit costs.','P12 downside stop retains exit costs.')
s=s.replace('P11 base assumes conditional 250 MW commercial success; it is not guaranteed revenue or an observed probability.','P12 has no booked royalty revenue, terminal value, IRR or payback.')
s=s.replace('P07 safety benefit is unverified expected risk reduction; excluded from cash unless explicitly enabled.','Retail urgent-delivery cash is excluded from the central case pending evidence.')
s=s.replace('P11 and P12','P12').replace('P11 base is the conditional 250 MW case; downside stops. Verify contracts, exit costs and market access.','P12 downside stops after Y2; validate IP, lab results and third-party demand.')
s=s.replace('H3 costs continue with no P11 receipts','H3 costs continue without commercial receipts')
s=s.replace('P11 base and upside commercial receipts are conditional.','P12 has no commercial receipts in any scenario.')
(root/'work/finance/build_workbook.mjs').write_text(s,encoding='utf-8')
