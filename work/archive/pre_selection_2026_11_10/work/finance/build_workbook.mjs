import fs from 'node:fs/promises';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

// Source: the four project cards, reserve_case_models.py, discount_rate_policy.md.
// Units: native currency millions; portfolio translated at the editable FX rate.
const data = [
 ['P01','Refining predictive maintenance','H1',.095,1,1,.50,.50,.40,[.20,.35,.40,.40,.40],2.11625,[.20,.60,.85,1,1]],
 ['P02','Upstream surveillance','H1',.10,1,1,.35,.25,.30,[.18,.25,.30,.30,.30],1.6425,[.10,.40,.70,1,1]],
 ['P03','Deepwater drilling advisory','H2',.11,1,1,.40,.40,.60,[.30,.45,.50,.50,.50],2.88,[0,.30,.70,1,1]],
 ['P04','Renewable fleet availability','H1',.10,1,1,.15,.15,.10,[.05,.07,.10,.10,.10],.3942,[.20,.50,.80,1,1]],
 ['P05','Copilot workflow redesign','H1',.09,1,1,.10,.10,.10,[.05,.08,.10,.10,.10],.54,[.25,.60,1,1,1]],
 ['P06','Procurement analytics','H1',.095,1,1,.20,.20,.10,[.08,.10,.12,.12,.12],.5,[.10,.40,.70,1,1]],
 ['P07','Safety computer vision','H1',.10,1,0,.20,.20,.20,[.10,.15,.18,.18,.18],.5,[.10,.40,.70,1,1]],
 ['P08','Customer retention','H1',.095,1,1,.20,.20,.20,[.10,.15,.20,.20,.20],.75,[.10,.40,.70,1,1]],
 ['P09','LNG voyage optimisation','H2',.10,1,1,.15,.15,.20,[.08,.10,.12,.12,.12],.6,[0,.35,.70,1,1]],
 ['P10','Steam-cracker optimisation','H1',.10,1,1,.25,.25,.25,[.10,.15,.20,.20,.20],.5,[0,.30,.70,1,1]],
 ['P11','Customer flexibility option','H3',.11,1,1,.40,.40,.70,[.35,.55,.75,.90,1],3.75,[0,.10,.30,.60,1]],
 ['P12','e-SAF catalyst option','H3',.12,1,0,.30,.30,.40,[.20,.30,.40,.45,.50],0,[0,0,0,0,0]],
 ['P13','Retail demand pilot (EUR)','H1',.09,1.1165,1,.40,.40,.20,[.06,.10,.12,.12,.12],.825,[.50,.80,1,1,1]],
 ['E01','Shared AI value register','Enabler',.09,1,0,.05,.05,.20,[.10,.12,.14,.14,.14],0,[0,0,0,0,0]],
];
const wb=Workbook.create();
const summary=wb.worksheets.add('Portfolio');
const focus=wb.worksheets.add('Focus curves');
const horizon=wb.worksheets.add('H3 horizon');
const metrics=wb.worksheets.add('Metrics');
const inputs=wb.worksheets.add('Inputs');
const drivers=wb.worksheets.add('Focus drivers');
const scenarios=wb.worksheets.add('Scenarios');
const calc=wb.worksheets.add('Cash flow build');
const notes=wb.worksheets.add('Read me');
function block(s,range,values){s.getRange(range).values=values;}
function f(s,addr,formula){s.getRange(addr).formulas=[[formula]];}
function header(s,range){s.getRange(range).format={fill:'#17365D',font:{name:'Arial',bold:true,color:'#FFFFFF',size:10}};}
for(const s of [summary,focus,horizon,metrics,inputs,drivers,scenarios,calc,notes]) s.getRange('A1:AZ330').format.font={name:'Arial',size:10};
summary.getRange('A:A').format.columnWidth=21;summary.getRange('B:D').format.columnWidth=14;
focus.getRange('A:A').format.columnWidth=19;focus.getRange('B:D').format.columnWidth=14;
inputs.getRange('A:A').format.columnWidth=10;inputs.getRange('B:B').format.columnWidth=34;inputs.getRange('C:U').format.columnWidth=16;
scenarios.getRange('A:K').format.columnWidth=17;calc.getRange('A:A').format.columnWidth=29;calc.getRange('B:H').format.columnWidth=15;
notes.getRange('A:A').format.columnWidth=130;metrics.getRange('A:I').format.columnWidth=18;
drivers.getRange('A:A').format.columnWidth=46;drivers.getRange('B:B').format.columnWidth=20;
horizon.getRange('A:A').format.columnWidth=20;horizon.getRange('B:M').format.columnWidth=18;
block(horizon,'A1:M5',[
 ['H3 | conditional base planning horizon beyond 5-year valuation',null,null,null,null,null,null,null,null,null,null,null,null],
 ['Years','Y0','Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8','Y9','Y10','Beyond Y10'],
 ['P11 flexibility','Design','Pilot','Trial','Conditional scale','Conditional scale','250 MW scenario','Unestimated','Unestimated','Unestimated','Unestimated','Unestimated','Unestimated'],
 ['P12 catalyst','Design','Lab','Lab gate','Conditional R&D','Conditional R&D','Conditional R&D','Unestimated','Unestimated','Unestimated','Unestimated','Unestimated','Unestimated'],
 ['This is a planning timeline, not payback; beyond Y5 there are no forecast cash flows or estimated maturity dates.',null,null,null,null,null,null,null,null,null,null,null,null]
]);header(horizon,'A1:M1');header(horizon,'A2:M2');
block(inputs,'A1:U1',[['ID','Project','Horizon','Hurdle','USD / native','Book benefit 1/0','Capex Y0','Capex Y1','Launch Y1','Opex Y1','Opex Y2','Opex Y3','Opex Y4','Opex Y5','Benefit at scale / yr','Ramp Y1','Ramp Y2','Ramp Y3','Ramp Y4','Ramp Y5','Include 1/0']]);header(inputs,'A1:U1');
block(inputs,'A2:U15',data.map(d=>[...d.slice(0,9),...d[9],d[10],...d[11],1]));
inputs.getRange('D2:U15').format.font={name:'Arial',size:10,color:'#0055AA'};
inputs.getRange('D2:D15').format.numberFormat='0.0%';
inputs.getRange('G2:O15').format.numberFormat='0.000';
inputs.getRange('P2:T15').format.numberFormat='0%';
block(inputs,'A18:A20',[['Blue numbers are editable assumptions; amounts are native currency millions (P13 EUR, others USD).'],['P11 conditional commercial receipts are scenario assumptions, not committed revenue; edit its scenario realisation factor.'],['P07 avoided incidents are not booked as certain cash; E01 is cost-only. All 14 projects are included by default.']]);
block(drivers,'A1:B29',[
 ['FOCUS BENEFIT DRIVERS','Editable assumptions'],['P01 | throughput barrels / day',250000],['Operating days per year',365],['Recoverable availability fraction',.005],['Sold / cash-realised fraction',.70],['Margin USD per barrel',6],['Additional repairs avoided USD m / yr',.20],['P01 gross benefit USD m / yr',null],
 ['P03 | operated rigs',2],['Avoidable days per rig / yr',6],['Cost per day USD m',.4],['Cash capture fraction',.60],['P03 gross benefit USD m / yr',null],
 ['P11 | customer flexibility MW',250],['Retained margin USD m per MW / yr',.015],['P11 conditional gross USD m / yr',null],
 ['P13 | number of stores',100],['Perishable sales per store EUR',350000],['Inventory cost share',.70],['Waste fraction',.04],['Waste reduction',.25],['Markdown items per store / yr',1000],['Net recovery per item EUR',2],['Lost sales per store EUR / yr',50000],['Lost sales recapture',.08],['Incremental margin',.35],['Urgent deliveries per store / yr',80],['Urgent delivery reduction',.50],['Variable cost per delivery EUR',60]
]);
block(drivers,'A30:A31',[['P13 gross benefit EUR m / yr'],['P13 lines represent distinct benefit pools; validate baselines and avoid double counting.']]);
drivers.getRange('B2:B29').format.font={name:'Arial',size:10,color:'#0055AA'};header(drivers,'A1:B1');
f(drivers,'B8','=B2*B3*B4*B5*B6/1000000+B7');f(drivers,'B13','=B9*B10*B11*B12');f(drivers,'B16','=B14*B15');
f(drivers,'B30','=B17*(B18*B19*B20*B21+B22*B23+B24*B25*B26+B27*B28*B29)/1000000');
f(inputs,'O2',"='Focus drivers'!B8");f(inputs,'O4',"='Focus drivers'!B13");f(inputs,'O12',"='Focus drivers'!B16");f(inputs,'O14',"='Focus drivers'!B30");

block(scenarios,'A1:N1',[['ID','Scenario','Benefit factor','Investment factor','Opex factor','Tax rate','Ramp Y1','Ramp Y2','Ramp Y3','Ramp Y4','Ramp Y5','Y3–5 run factor','Realisation factor','Y3 stop cost']]);header(scenarios,'A1:N1');
const scen=[];
for(const d of data){for(const name of ['Downside','Base','Upside']){
 const ret=d[0]==='P13'; const ramp=ret&&name==='Downside'?[.35,.60,.80,1,1]:ret&&name==='Upside'?[.65,.90,1,1,1]:d[11];
 const stop=name==='Downside'&&['P11','P12'].includes(d[0]);
 const realisation=d[0]==='P11'?(name==='Downside'?0:1):1;
 scen.push([d[0],name,name==='Downside'?.90:name==='Upside'?1.15:1,name==='Downside'?1.05:1,name==='Downside'?1.05:1,.25,...ramp,stop?0:1,realisation,stop?(d[0]==='P11'?.15:.10):0]);
}}
block(scenarios,'A2:N43',scen);scenarios.getRange('C2:N43').format.font={name:'Arial',size:10,color:'#0055AA'};scenarios.getRange('C2:M43').format.numberFormat='0%';scenarios.getRange('N2:N43').format.numberFormat='0.000';scenarios.getRange('L:N').format.columnWidth=20;
for(let i=0;i<data.length;i++)for(let j=0;j<3;j++)for(let y=0;y<5;y++){
 const factor=data[i][0]==='P13'&&j===0?[.7,.75,.8,1,1][y]:data[i][0]==='P13'&&j===2?[1.3,1.125,1,1,1][y]:1;
 f(scenarios,`${String.fromCharCode(71+y)}${2+i*3+j}`,`=Inputs!${String.fromCharCode(80+y)}${2+i}*${factor}`);
}
const stress=data.map(d=>[d[0],'Severe stress',.65,1.20,1.20,.25,...d[11],1,d[0]==='P11'?0:1,0]);block(scenarios,'A44:N57',stress);
for(let i=0;i<data.length;i++)for(let y=0;y<5;y++)f(scenarios,`${String.fromCharCode(71+y)}${44+i}`,`=Inputs!${String.fromCharCode(80+y)}${2+i}`);
scenarios.getRange('C44:N57').format.font={name:'Arial',size:10,color:'#0055AA'};scenarios.getRange('C44:M57').format.numberFormat='0%';
block(scenarios,'A60:A64',[['Scenarios are assumptions, not forecasts. Downside: 90% benefits, 105% costs, H3 stops after Y2; exit costs retained.'],['Investment factor applies to both capex and launch expense; recurring costs use the opex factor.'],['Ramps link to Inputs; overwrite a scenario formula to change its timing independently.'],['P11 base is the conditional 250 MW case; downside stops. Verify contracts, exit costs and market access.'],['Severe stress is separate and unweighted: 65% benefits, 120% costs, H3 costs continue with no P11 receipts.']]);

block(calc,'A1:H1',[['Project / scenario / USD millions','Y0','Y1','Y2','Y3','Y4','Y5','Metric']]);header(calc,'A1:H1');
const starts={};
const builds=[];for(let i=0;i<data.length;i++)for(let j=0;j<3;j++)builds.push({i,j,conditional:false});for(let i=0;i<data.length;i++)builds.push({i,j:3,conditional:false});
for(let n=0;n<builds.length;n++){
 const {i,j,conditional}=builds[n], sr=j===3?44+i:2+i*3+j, ir=2+i, r=2+n*7, id=data[i][0], name=['Downside','Base','Upside','Severe stress'][j]; starts[`${id}-${conditional?'Conditional ':''}${name}`]=r;
 block(calc,`A${r}:A${r+6}`,[[`${id} / ${name}`],['Gross benefit'],['Operating and launch costs'],['Capital spending'],['Cash tax'],['Net cash flow'],['Cumulative cash flow']]);
 f(calc,`B${r}`,`=Inputs!D${ir}`);f(calc,`H${r}`,`=B${r+5}+NPV(B${r},C${r+5}:G${r+5})`);
 for(let y=0;y<=5;y++){
  const col=String.fromCharCode(66+y), op=String.fromCharCode(73+y), ramp=String.fromCharCode(70+y);
  f(calc,`${col}${r+1}`,y===0?'=0':`=Inputs!O${ir}*Inputs!F${ir}*Scenarios!M${sr}*Scenarios!C${sr}*Scenarios!${ramp}${sr}*Inputs!E${ir}${y>=3?`*Scenarios!L${sr}`:''}`);
  f(calc,`${col}${r+2}`,y===0?'=0':`=(Inputs!${op}${ir}*Scenarios!E${sr}${y>=3?`*Scenarios!L${sr}`:''}${y===1?`+Inputs!I${ir}*Scenarios!D${sr}`:''}${y===3?`+Scenarios!N${sr}`:''})*Inputs!E${ir}`);
  f(calc,`${col}${r+3}`,y===0?`=Inputs!G${ir}*Scenarios!D${sr}*Inputs!E${ir}`:y===1?`=Inputs!H${ir}*Scenarios!D${sr}*Inputs!E${ir}`:'=0');
  f(calc,`${col}${r+4}`,y===0?'=0':`=MAX(0,${col}${r+1}-${col}${r+2}-(Inputs!G${ir}+Inputs!H${ir})*Scenarios!D${sr}*Inputs!E${ir}/5)*Scenarios!F${sr}`);
  f(calc,`${col}${r+5}`,`=${col}${r+1}-${col}${r+2}-${col}${r+3}-${col}${r+4}`);
  f(calc,`${col}${r+6}`,y===0?`=${col}${r+5}`:`=${String.fromCharCode(65+y)}${r+6}+${col}${r+5}`);
 }
}
calc.getRange('B2:H400').format.numberFormat='0.000';
block(metrics,'A1:K1',[['Project','Scenario','Horizon','Hurdle','NPV USD m','IRR','Simple payback (years)','Discounted payback','NPV WACC -1pp','NPV WACC base','NPV WACC +1pp']]);header(metrics,'A1:K1');metrics.getRange('G:K').format.columnWidth=22;
for(let n=0;n<builds.length;n++){
 const {i,j,conditional}=builds[n],id=data[i][0],name=['Downside','Base','Upside','Severe stress'][j],r=2+n*7,m=2+n;
 block(metrics,`A${m}:C${m}`,[[id,(conditional?'Conditional ':'')+name,data[i][2]]]);
 f(metrics,`D${m}`,`=Inputs!D${i+2}`);f(metrics,`E${m}`,`='Cash flow build'!H${r}`);
 f(metrics,`F${m}`,`=IFERROR(IRR('Cash flow build'!B${r+5}:G${r+5}),"n/a")`);
 if(data[i][2]==='H3'||id==='E01')block(metrics,`G${m}:H${m}`,[['n/a','n/a']]);
 else {let expr='"beyond Y5"';for(let y=5;y>=1;y--){const c=String.fromCharCode(66+y),p=String.fromCharCode(65+y);expr=`IF('Cash flow build'!${c}${r+6}>=0,${y-1}-'Cash flow build'!${p}${r+6}/'Cash flow build'!${c}${r+5},${expr})`;}f(metrics,`G${m}`,`=IFERROR(${expr},"n/a")`);}
 if(data[i][2]!=='H3'&&id!=='E01'){
  let expr='"beyond Y5"';const terms=y=>Array.from({length:y+1},(_,t)=>`'Cash flow build'!${String.fromCharCode(66+t)}${r+5}/(1+D${m})^${t}`).join('+');
  for(let y=5;y>=1;y--){const annual=`'Cash flow build'!${String.fromCharCode(66+y)}${r+5}/(1+D${m})^${y}`;expr=`IF((${terms(y)})>=0,${y-1}-(${terms(y-1)})/(${annual}),${expr})`;}
  f(metrics,`H${m}`,`=IFERROR(${expr},"n/a")`);
 }
 for(let k=-1;k<=1;k++){const col=String.fromCharCode(74+k);f(metrics,`${col}${m}`,`='Cash flow build'!B${r+5}+NPV(D${m}${k===0?'':k<0?'-.01':'+.01'},'Cash flow build'!C${r+5}:G${r+5})`);}
}
metrics.getRange('D2:D57').format.numberFormat='0.0%';metrics.getRange('E2:E57').format.numberFormat='0.000';metrics.getRange('F2:F57').format.numberFormat='0.0%';metrics.getRange('G2:K57').format.numberFormat='0.00';
block(summary,'A1:D3',[["TOTALENERGIES | 14-INITIATIVE PORTFOLIO",null,null,null],["Illustrative scenarios; unapproved assumptions; USD million",null,null,null],["Four focus cases + nine estimates + one shared enabler. P11 conditional revenue depends on each scenario.",null,null,null]]);header(summary,'A1:D1');
block(summary,'A5:D5',[['Year','Downside','Base','Upside']]);header(summary,'A5:D5');
for(let y=0;y<=5;y++){const r=6+y;block(summary,`A${r}`,[[`Y${y}`]]);for(let j=0;j<3;j++){const name=['Downside','Base','Upside'][j],col=String.fromCharCode(66+j),ycol=String.fromCharCode(66+y);f(summary,`${col}${r}`,`=SUM(${data.map((d,i)=>`'Cash flow build'!${ycol}${starts[`${d[0]}-${name}`]+6}*Inputs!U${i+2}`).join(',')})`);}}
summary.getRange('B6:D11').format.numberFormat='0.00';
block(summary,'A14:D15',[['Sum of project NPVs at each project hurdle','Downside','Base','Upside'],['USD million',null,null,null]]);header(summary,'A14:D14');
block(summary,'A14',[['NPV at project hurdles']]);summary.getRange('B15:D15').format.numberFormat='0.00';
for(let j=0;j<3;j++){const name=['Downside','Base','Upside'][j],col=String.fromCharCode(66+j);f(summary,`${col}15`,`=SUM(${data.map((d,i)=>`'Cash flow build'!H${starts[`${d[0]}-${name}`]}*Inputs!U${i+2}`).join(',')})`);}
block(summary,'A17:D17',[['Scenario weight',.25,.50,.25]]);summary.getRange('B17:D17').format.numberFormat='0%';summary.getRange('B17:D17').format.font={name:'Arial',size:10,color:'#0055AA'};
block(summary,'A18:A22',[['Weighted NPV USD m'],['Weight total (must be 100%)'],['Cumulative cash flows are undiscounted, including 14 initiatives and E01 once.'],['P11 revenues are conditional assumptions; downside H3 stop retains exit costs.'],['No portfolio approval or validation is implied. Check overlap, tax and scenario weights.']]);
f(summary,'B18','=SUMPRODUCT(B15:D15,B17:D17)');f(summary,'B19','=SUM(B17:D17)');summary.getRange('B18').format.numberFormat='0.00';summary.getRange('B19').format.numberFormat='0%';
block(summary,'A24',[['Severe stress NPV']]);f(summary,'B24',`=SUM(${data.map((d,i)=>`'Cash flow build'!H${starts[`${d[0]}-Severe stress`]}*Inputs!U${i+2}`).join(',')})`);summary.getRange('B24').format.numberFormat='0.00';
block(summary,'A27:C32',[['One-time budget USD m','Amount','Share'],['H1',null,null],['H2',null,null],['H3',null,null],['Enabler',null,null],['Total',null,null]]);header(summary,'A27:C27');
for(let j=0;j<4;j++){const h=['H1','H2','H3','Enabler'][j],r=28+j;f(summary,`B${r}`,`=SUM(${data.map((d,i)=>d[2]===h?`(Inputs!G${i+2}+Inputs!H${i+2}+Inputs!I${i+2})*Inputs!E${i+2}*Inputs!U${i+2}`:'0').join(',')})`);f(summary,`C${r}`,`=IFERROR(B${r}/B32,0)`);}
f(summary,'B32','=SUM(B28:B31)');f(summary,'C32','=SUM(C28:C31)');summary.getRange('B28:B32').format.numberFormat='0.00';summary.getRange('C28:C32').format.numberFormat='0.0%';
const chart=summary.charts.add('line',summary.getRange('A5:D11'));chart.title='14 initiatives: cumulative cash flow';chart.setPosition('F4','P20');
block(focus,'A1:D1',[['FOUR FEATURED PROJECTS | cumulative cash flow (USD million)',null,null,null]]);header(focus,'A1:D1');
const ids=['P01','P03','P11','P13'];
for(let i=0;i<4;i++){const base=3+i*22,id=ids[i];block(focus,`A${base}:D${base}`,[[id+' / Year','Downside','Base','Upside']]);header(focus,`A${base}:D${base}`);
 for(let y=0;y<=5;y++){const r=base+1+y;block(focus,`A${r}`,[[`Y${y}`]]);for(let j=0;j<3;j++){const name=['Downside','Base','Upside'][j];f(focus,`${String.fromCharCode(66+j)}${r}`,`='Cash flow build'!${String.fromCharCode(66+y)}${starts[`${id}-${name}`]+6}`);}}
 const ch=focus.charts.add('line',focus.getRange(`A${base}:D${base+6}`));ch.title=`${id} cumulative cash flow${id==='P11'?' — conditional':''}`;ch.setPosition(`F${base}`,`P${base+17}`);
}
block(notes,'A1:A14',[["READ ME — 10 November 2026"],["Scope: 14 indicative initiatives including E01. Four cases are detailed; other project inputs are rough estimates."],["Inputs: editable assumptions in blue. P13 is EUR million; FX translates it to USD million. Column U includes or excludes each project."],["Scenarios: edit benefit, investment, recurring costs, tax and yearly ramp for each project and scenario."],["Cash flow build: benefit, operating cost, capital, tax, net and cumulative by year; H column is NPV at the hurdle."],["Tax: 25% assumed; no loss carry-forward; 5-year straight-line capital depreciation. No working capital assumed."],["H3: downside stops P11 and P12 after Y2; Y3 exit costs retained. P11 base and upside commercial receipts are conditional."],["P11 base assumes conditional 250 MW commercial success; it is not guaranteed revenue or an observed probability."],["P07 safety benefit is unverified expected risk reduction; excluded from cash unless explicitly enabled."],["All 14 projects are included as an illustrative combined scenario, not an approved or overlap-adjusted budget."],["Sources and formulas: work/finance/discount_rate_policy.md, work/projects/case_p*.md and reserve_cards.md."],["P13 €1m / 100 stores is an indicative assumption informed by local experience; benefits and costs require validation."],["The 5-year valuation window is not the time horizon of H3 options. No H3 payback is inferred."],["Weights are subjective, not measured; severe stress is shown separately and is not included in weighted NPV."]]);header(notes,'A1:A1');
wb.recalculate();
const before=Number(summary.getRange('C11').values[0][0]);
drivers.getRange('B17').values=[[110]];wb.recalculate();
const after=Number(summary.getRange('C11').values[0][0]);
if(!Number.isFinite(before)||!Number.isFinite(after)||Math.abs(after-before)<1e-8)throw Error('Retail input did not propagate to portfolio');
console.log(`Input sensitivity test: Y5 base cumulative ${before} -> ${after} when stores increase 100 to 110`);
drivers.getRange('B17').values=[[100]];wb.recalculate();
console.log((await wb.inspect({kind:'region',sheetId:'Portfolio',range:'A5:D15',maxChars:5000})).ndjson);
const out=await SpreadsheetFile.exportXlsx(wb);await out.save('work/finance/portfolio_model_14_revised.xlsx');
try{const preview=await wb.render({sheetName:'Portfolio',range:'A1:P20',scale:1,format:'png'});await fs.writeFile('work/finance/portfolio_preview.png',new Uint8Array(await preview.arrayBuffer()));}catch(e){console.error('Preview:',e.message)}
