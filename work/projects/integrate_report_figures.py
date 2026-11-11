"""Idempotent integration of checked figures and the focus-budget comparison."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[2]
d=json.loads((R/'work/finance/selected_chart_data.json').read_text())
focus=['P01','P03','P12','P13','E01']
cost=sum(sum(d['projects'][k]['annual_cost']) for k in focus)
half=d['portfolio']['gross_cost']/2
paragraph=f'''**Why the half-budget portfolio is not simply the four featured cases.** The featured cases were selected to explain the strategy and its different decision mechanisms, not to fit a 50% spending limit. P01 + P03 + P12 + P13 cost **${cost-sum(d['projects']['E01']['annual_cost']):.3f}m**; retaining the required E01 controls brings that to **${cost:.3f}m**, or **{100*cost/d['portfolio']['gross_cost']:.1f}%** of the full envelope, against **${half:.3f}m** available. Even limiting P12 to Y0–Y2 plus closure gives **${cost-1.25:.3f}m**. Keeping all four at half budget would therefore require redesigned asset/store scopes, fixed-versus-variable costs and benefit ramps. Proportional scaling would be misleading. The constrained alternative instead preserves complete, costed operating cases and one bounded H3 experiment. It is a feasible response, not a claim of an optimized subset across all possible scope redesigns.'''
for rel in ['deliverables/report/full_strategy_report_draft.md','work/finance/half_envelope_alternative.md','work/finance/portfolio_economics.md']:
 p=R/rel;s=p.read_text(encoding='utf-8-sig')
 if '**Why the half-budget portfolio' not in s:
  if '## 8. Cost of inaction' in s:s=s.replace('## 8. Cost of inaction',paragraph+'\n\n## 8. Cost of inaction')
  else:s=s.rstrip()+'\n\n'+paragraph+'\n'
 s=s.replace('**,  (CLM-078','** (CLM-078').replace('drilling economics, power flexibility and customer operations','drilling economics, new energy technologies and customer operations')
 s=s.replace('these four proposals','the selected proposals').replace('2026**\n**Team:', '2026**\n\n**Team:')
 s=s.replace('$-', '−$')
 s=s.replace('Calculation: `work/finance/industrial_case_models.py`.','Active calculations: `work/finance/portfolio_model_selected.xlsx`, independently checked by `work/finance/reconcile_selected.py`.')
 s=s.replace('The pilot does not assume the 800- or 1,500-station footprint of the discarded draft.','Expansion beyond the 100-store scope requires a separate investment decision.')
 s=s.replace('The report is the source for the two-page memo, then slides. Retired graphics are not evidence for this version. Chart production remains a separate rendering task; no old figure should be copied into the memo or slides. No internal approvals, asset eligibility or observed business returns are asserted.','The report is the source for the two-page memo, then slides. All figures use the selected workbook and its checked data export. No internal approvals, asset eligibility or observed business returns are asserted.')
 p.write_text(s,encoding='utf-8')
p=R/'deliverables/report/full_strategy_report_draft.md';s=p.read_text(encoding='utf-8')
def figure(name,caption):
 path=R/f'deliverables/report/assets/{name}.png'
 assert path.exists(),path
 return f'\n\n![{caption}](assets/{name}.png)\n\n*{caption} All values are calculations on explicit assumptions.*\n\n'
if 'assets/selected_portfolio_map.png' not in s:
 s=s.replace('## 6. Four detailed cases',figure('selected_portfolio_map','Portfolio map: cash-led cases and a separately identified learning option.')+figure('selected_horizon_mix','Capital allocation by horizon; one-time and full programme costs have different denominators.')+figure('selected_net_contributions','Signed weighted NPV by horizon at 10%; H3 includes learning costs and no forecast commercial receipts.')+'## 6. Four detailed cases')
 for ident,heading in [('p01','### 6.2'),('p03','### 6.3'),('p12','### 6.4'),('p13','## 7.')]:
  idx=s.index('\n'+heading)+1
  s=s[:idx]+figure(f'selected_{ident}_jcurve',f'{ident.upper()} cumulative net cash by scenario; '+('EUR million.' if ident=='p13' else 'USD million.'))+s[idx:]
 s=s.replace('### Cost-category allocation',figure('selected_portfolio_jcurve','Portfolio cumulative cash, USD million; scenario weights are subjective and no inaction uplift is included.')+'### Cost-category allocation')
 s=s.replace('## 8. Cost of inaction',figure('selected_half_budget','Full versus constrained portfolio: spending and expected net value on the same five-year basis.')+'## 8. Cost of inaction')
p.write_text(s.rstrip()+'\n',encoding='utf-8')
print(f'Focus plus E01: {cost:.5f}; half cap: {half:.5f}. Nine figures integrated without changing model assumptions.')
