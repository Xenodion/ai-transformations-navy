"""Publish reconciled model tables into the report while retaining case narratives."""
from pathlib import Path
import json,re
from decision_cashflows import npv
R=Path(__file__).resolve().parents[2]
d=json.loads((R/'work/finance/selected_chart_data.json').read_text())
ps=d['projects']; port=d['portfolio']; half=d['half']
old=(R/'work/archive/pre_selection_2026_11_10/deliverables/report/full_strategy_report_draft.md').read_text(encoding='utf-8')
def money(v):return f'{v:+.3f}'
def pct(v):return 'n/a' if v is None else f'{100*v:.1f}%'
def table(head,rows):return '| '+' | '.join(head)+' |\n| '+' | '.join(['---']*len(head))+' |\n'+''.join('| '+' | '.join(map(str,r))+' |\n' for r in rows)
def scenarios(p,native=False):
    fx=p['fx'] if native else 1
    return table(['Scenario','NPV at project hurdle','IRR','Simple payback'],[[n,money(p['scenarios'][n]['npv']/fx),pct(p['scenarios'][n]['irr']),('n/a' if p['scenarios'][n]['payback'] is None else f"{p['scenarios'][n]['payback']:.2f}")] for n in ['Downside','Base','Upside']])
def cash_table(p,native=False):
    fx=p['fx'] if native else 1; rows=p['scenarios']['Base']['rows']
    return table(['Base cash flow','Y0','Y1','Y2','Y3','Y4','Y5'],[[label]+[f'{r[k]*sign/fx:.4f}' for r in rows] for label,k,sign in [('Gross benefit',0,1),('Operating and launch expense',1,-1),('CAPEX',2,-1),('Cash tax',3,-1),('Net cash',4,1)]])
scenario_text='''**Scenario assumptions:** downside has 75% of central unit benefits, 115% of capital, launch and recurring costs, and benefits delayed one year (no catch-up outside Y5). Base retains the original ramp. Upside has 115% unit benefits and each central adoption fraction multiplied by 1.15, capped at 100%, at base costs. These are judgments, not calibrated frequencies. The H3 downside stops after Y2 and retains a $0.10m Y3 exit allowance. H1/H2 downside conservatively retains full operating spending: gate savings are not assumed. A separate severe stress also delays benefits one year, uses 65% benefits and 120% costs, and retains H3 spending. It measures failed cost control, not the expected gated response.'''

p12='''### 6.3 P12 — AI-assisted e-SAF technology licensing option (H3)

**Decision:** fund a staged experiment in a third-party technology business, reusing the catalyst research concept and its existing cost envelope. Do not approve a production plant or forecast royalty receipts.

**Business-model hypothesis:** combine AI-assisted catalyst/process discovery with a licensable process package for independent e-fuel developers. The proposed buyer is a third-party plant developer; potential consideration would be development fees, technology royalties and technical support, rather than only margin on fuel produced in company-owned plants. Pricing, addressable buyers, IP ownership and technical differentiation are unknown. No such receipts enter the five-year model.

**Existing capability and disconfirmation:** TotalEnergies already has CO2 Techno Hub, BioHub and SAF research partnerships. This is not a proposal to create those capabilities again. Infinium describes a third-party technology licensing arrangement in Southeast Asia; that establishes a possible commercial structure, not demand for a competing TotalEnergies package or an achievable return. Before spending, map existing TotalEnergies licensing, partner IP and funded e-fuel research. If this merely improves an internal fuel-production process or duplicates an existing offer, its H3 thesis fails. Stop or reclassify it; do not preserve H3 by relabelling duration.

**Why AI:** rank candidate formulations and experiments using uncertainty-aware models, then validate with physical tests. Compare against conventional design of experiments using the same laboratory budget. Prediction accuracy alone is not an investment milestone. Blend existing research infrastructure, specialist laboratory partners and commercial/IP expertise. No new foundation model or plant construction is funded.

**Costs [Assumptions]:** preserve $0.30m CAPEX in Y0, $0.30m CAPEX and $0.40m launch expense in Y1; recurring Y1–Y5 costs are $0.20m/$0.30m/$0.40m/$0.45m/$0.50m. Total gross ceiling is $2.85m. This is a narrow feasibility and laboratory envelope, not funding for certification, a demonstration plant, industrial warranties or commercialization. Existing lab access is a hard condition. The $0.40m launch allowance must cover commercial/IP work and experiment design as well as integration; reprice or stop if it cannot.

**Gates [Proposed assumptions]:** before Y0, OneTech and Legal establish non-duplication, data and licensing rights. Before Y2, identify at least two qualified third-party developers willing to discuss a defined application and benchmark. Before Y3, require a repeatable result from three independent experimental runs, a pre-registered improvement target against the conventional method, a preliminary freedom-to-operate assessment and at least one documented willingness to enter a paid evaluation (not booked as revenue). The experiment protocol must set the technical improvement threshold before testing. If any commercial or technical condition fails, stop avoidable spending; retain spent cash and a $0.10m closure allowance. No automatic industrial scale-up follows a laboratory pass.

**H3 rationale:** the proposed transformation is a technology-licensing revenue model serving external developers. The lab work is the means, not the reason for H3 classification. H3 is conditional on this novelty being established at G0. The five-year NPV below measures the cost of exploration only; IRR and payback are inapplicable. No long-term option valuation is asserted.

Sources: [TotalEnergies innovation and existing research](https://totalenergies.com/company/strength/innovation-rd); [Infinium projects, Southeast Asia licensing](https://infinium.energy/projects), accessed 10 November 2026. See the [H3 evidence note](../../sources/synthesis/2026-11-10_h3_licensing_option.md) for scope and limits.

'''+cash_table(ps['P12'])+'\n'+scenarios(ps['P12'])

cases=[]
for ident,start,end in [('P01','### 6.1','### 6.2'),('P03','### 6.2','### 6.3'),('P13','### 6.4','## 7.')]:
    text=old[old.index(start):old.index(end,old.index(start))]
    # Retain problem, alternatives, scope, sourcing, dependencies and cost explanation.
    text=re.sub(r'\*\*Decision at a glance:\*\*.*?\n\n','',text,flags=re.S)
    text=re.sub(r'!\[[^\]]*\]\([^\n]*\)\n','',text)
    if ident in ['P01','P03']:
        a=text.index('#### 5.'); b=text.index('#### 7.')
        text=text[:a]+'#### 5. Reconciled cash and scenarios\n\nAmounts USD m.\n\n'+cash_table(ps[ident])+'\n'+scenario_text+'\n\n'+scenarios(ps[ident])+'\n'+text[b:]
    else:
        a=text.index('#### 5.')
        text=text[:a]+'''#### 5. Benefit drivers and revised financial case

All inputs are assumptions for 100 eligible stores. The central annual benefit is **€0.585m**: €0.245m waste reduction + €0.200m incremental markdown recovery + €0.140m stock-out recovery. Urgent-delivery savings are excluded until invoices establish avoidable cash. No 2–3 year payback target is used to solve the benefit assumptions.

- Waste: 100 × €350,000 perishable sales × 70% inventory cost × 4% baseline waste × 25% reduction = €245,000/year.
- Markdowns: 100 × 1,000 at-risk items × €2 net incremental recovery = €200,000/year. These items must be outside the waste pool. Define SKU/day cohorts and measure net margin after cannibalization, discounts and extra handling. If this cannot be demonstrated, remove the markdown stream.
- Stock-outs: 100 × €50,000 missed sales × 8% recovery × 35% contribution = €140,000/year. Measure incremental category contribution, not substitution between products.

These equations are transparent planning hypotheses, not observed baselines. A pilot must compare forecasting only, rules-based ordering and forecasting plus labels using matched stores and seasonality. The €1m remains the 100-store rollout ceiling; release only a small instrumented slice before buying all hardware.

Amounts EUR m below. Costs and the central adoption ramp are preserved.

'''+cash_table(ps[ident],True)+'\n'+scenario_text+'\n\n'+scenarios(ps[ident],True)+'''

**Attribution sensitivity:** without the €0.200m markdown stream, annual benefit falls to €0.385m, below the existing approximately €0.446m full-project break-even threshold at 9%. The case therefore requires evidence of incremental markdown value or a lower-cost forecasting-only design. It is not robust merely because all drivers are labelled assumptions. The previous delivery-saving assumption is an unbooked upside lead, not an offset to this risk.

**Release rule:** retail sponsor and Finance pre-register the matched-store protocol, baseline waste cohorts, margin and paid delivery invoices before Y0 release. Before Y2 hardware expansion, require positive prospective NPV at 9% using measured incremental margin and remaining avoidable costs. Stop hardware rollout if labels do not outperform forecasting-only after their incremental costs. Store managers retain pricing authority. Count training, installation and staff backfill inside the cost envelope or reprice the case.

**Sources and limits:** local calibration CLM-074/078/079 establishes neither a group baseline nor a realized saving. The €1m/100-store envelope is an explicit planning assumption. The source register and retail case preserve these distinctions.
'''
    text=text.replace('portfolio_model_14_revised.xlsx','portfolio_model_selected.xlsx')
    text=text.replace('60% cash realization after fixed-contract restrictions, partner terms and other leakage','80% assumed economic share × 75% payment avoidability = 60% combined realization')
    text=text.replace('The 60% factor is a single combined assumption; do not also apply an unverified ownership discount to the same amount.','Both factors are explicit hypotheses for the same eligible campaigns, not verified contract terms. Do not apply ownership a second time. If the actual economic share is 40%, otherwise unchanged benefit halves to $1.440m/year, below the $1.660m break-even reference.')
    text=text.replace('and a **2–3 year payback objective**','')
    cases.append(text)

selection='''## 5. Selected portfolio and capital allocation

Select seven business initiatives plus one shared control enabler. This is a bounded incremental programme, not TotalEnergies' entire AI transformation budget. It reuses established platforms. The four detailed cases are P01, P03, P12 and P13. Geographic and asset eligibility remain G0 conditions.

H1 monetizes existing operations, H2 redesigns adjacent decision workflows, H3 tests a new business model. P03 and P09 qualify as H2 only if the scoped workflow changes planning/operating decisions across teams; a monitoring-only implementation is H1. P12 requires external licensing novelty, not simply a long research cycle. The course's 70/20/10 mix is a heuristic, not an optimization constraint.

'''
reasons={'P01':'Operational reliability; explicit sold-throughput mechanism.','P02':'Production surveillance, distinct assets/events from drilling.','P03':'Planning-to-execution workflow and avoidable rig payments.','P05':'Workflow and licence rationalisation; no monetized employee time.','P09':'LNG voyage planning; only controllable fuel invoices.','P12':'External technology-licensing experiment; no booked commercial return.','P13':'Retail margin capture with an observable matched-store trial.','E01':'Shared baseline, model and value controls, counted once.'}
selection+=table(['ID','Horizon','One-time USD m','Five-year gross USD m','Selection rationale'],[[k,p['horizon'],f"{p['one_time']:.3f}",f"{sum(p['annual_cost']):.3f}",reasons[k]] for k,p in ps.items()])
mix={h:sum(p['one_time'] for p in ps.values() if p['horizon']==h) for h in ['H1','H2','H3','Enabler']}; total=sum(mix.values())
selection+='\n'+table(['Allocation','One-time USD m','Share'],[[h,f'{v:.3f}',f'{100*v/total:.1f}%'] for h,v in mix.items()])+'''

E01 remains separate so business horizon shares plus governance sum to 100%. One-time allocation is distinct from the full gross envelope, which includes recurring OPEX. Four industrial/commercial cash mechanisms finance a bounded option; no H3 return share is manufactured. The chart data and rendering specification use the same selected set.

For shorter cases: P02 assumes 2 hubs × 150 barrels/day × 365 × $15/barrel contribution; P05 assumes 10,000 paid licences × 15% permanently cancelled × $30/month × 12; P09 assumes 30 controlled voyages × $1m eligible fuel cost × 2% savings. These are unverified scopes and rates. P05 is an enabling workflow redesign with a modest cancellation benefit, not evidence that AI itself generates licence savings. Require procurement-confirmed cancellability without loss of needed functionality. P02 requires signed production entitlement and separation from P03; P09 requires charter/fuel payment rights and separation from baseline voyage optimization.

'''
def portfolio_table(p):return table(['Scenario','NPV at 10%, USD m','IRR'],[[n,money(p[n]['npv']),pct(p[n]['irr'])] for n in ['Downside','Base','Upside','Weighted','Severe stress']])
finance=f'''## 7. Consolidated financial decision

**Calculation on assumptions:** gross base programme cost **${port['gross_cost']:.3f}m**, covering Y0 and five operating years. Y0 is the decision period; Y1–Y5 are annual periods after it. Gross cost excludes cash tax; NPV includes modelled tax. All cash is nominal, post-tax, unlevered and translated at the unchanged 1.1165 USD/EUR assumption. The 10% common screen is a team assumption (7% published impairment WACC proxy plus 3pp), not a disclosed corporate investment hurdle. Project screens retain 9–12% rates.

{portfolio_table(port)}

{scenario_text}

Weights are subjective 25%/50%/25%. Weighted IRR is computed from weighted annual cash, never an average of IRRs. No terminal value, H3 receipts or avoided-inaction uplift is booked. H3 costs are retained in base and upside even though revenue is zero. The severe stress is unweighted and is not a maximum-loss estimate.

'''+table(['Annual cash, USD m','Y0','Y1','Y2','Y3','Y4','Y5'],[[n]+[f'{v:.3f}' for v in port[n]['cash']] for n in ['Downside','Base','Upside','Weighted']])+ '\n'+table(['Base gross cost','Y0','Y1','Y2','Y3','Y4','Y5'],[['Annual release ceiling']+[f'{v:.3f}' for v in port['annual_cost']]])+f'''

Weighted cumulative cash trough is ${min(sum(port['Weighted']['cash'][:t+1]) for t in range(6)):.3f}m; simple interpolated payback is {port['Weighted']['payback']:.2f} years. Fund the trough, not just CAPEX. A base gross ceiling is not a promise that overruns are funded: the downside quantifies an overrun requiring a stop, resize or new approval.

**Accounting limits:** 25% cash tax on positive annual surplus after straight-line depreciation of CAPEX over five years; no loss carry-forward, working capital, financing or terminal value. This simplified tax convention and unchanged cost assumptions need jurisdictional and procurement validation. Costs include launch training but do not prove all staff backfill is funded. Before G0, reconcile vendor quotes and staff days against the ceiling; do not treat existing employee time as free. The initial spending is not a contractual loss cap.

### 7.1 If only half the budget is available

Half of the selected gross envelope is **${port['gross_cost']/2:.3f}m**. Retain P01, P05, P09, E01 and the initial P12 experiment through Y2, with $0.10m closure/transfer in Y3. This costs **${half['gross_cost']:.3f}m**, leaving **${port['gross_cost']/2-half['gross_cost']:.3f}m** unallocated. P02, P03 and P13 are deferred in this constrained alternative. No proportional haircut to benefits is used; retained scopes retain their original costs and benefits. P12 receives no automatic continuation beyond the funded experiment.

{portfolio_table(half)}

The half-budget weighted NPV is only marginally positive. This is a feasible constrained response, not equally attractive performance at half cost. It sacrifices upstream/drilling and retail learning and most of the full portfolio's expected net value. Its remaining headroom is not a forecast saving. The H1/H2/H3 mix remains present, while the H3 commitment is limited to an interpretable experiment. Dependencies and shared governance costs are retained, not halved.

## 8. Cost of inaction

The baseline includes existing AI, maintenance, trading, retail and research programmes. Doing nothing here means not funding these incremental experiments, not abandoning AI. Potential consequences are slower capture of eligible operating margin, delayed learning and difficulty retaining scarce delivery capability. The magnitude and programme-specific causality are unverified.

**Decision treatment:** zero additional avoided-erosion cash is booked. The project benefits already compare against continuation; adding the same missed margin as an inaction loss would double count. Talent and customer losses require distinct cohorts, causal effects, economic ownership and incremental prevention costs before any uplift is recognized. A course example or a percentage of group revenue does not validate these inputs. Present the opportunity cost qualitatively and the unadjusted scenarios quantitatively. This meets the inaction discussion without manufacturing a positive downside.

## 9. Release gates, accountability and adoption

Segment sponsors own operating change; Finance signs baseline and incremental cash; Digital Line/Digital Factory owns reusable technical controls; HSE, cyber and Legal retain veto rights. P01 belongs to refining, P02/P03 to upstream, P09 to LNG, P13 to Marketing & Services, P05/E01 to Corporate and P12 to OneTech with a commercial/IP sponsor. These are proposed roles, not claimed internal appointments.

| Gate | Metric, threshold and deadline | Owner and action |
| --- | --- | --- |
| G0 before each Y0 purchase order | 100% selected scopes have existing-solution inventory, economic/data rights, vendor/staff cost build and signed comparison protocol | Segment sponsor + Finance; no order for an unready scope. P12 also needs a distinct external licensing hypothesis and usable IP. |
| G1 before Y2 release | Zero unresolved critical safety/privacy issues; at least 90% pilot users trained and 60% eligible decisions recorded over the last four weeks, or a workflow-specific threshold agreed before launch | Operations + HSE; pause new spend for unsafe or unused workflows. Finance records cash separately from usage. |
| Cash scale gate before each expansion | Positive prospective NPV at the project's hurdle using measured effects and remaining avoidable costs; no duplicate benefit pools | Sponsor + Finance; stop or resize on failure. No automatic rollout from a positive original NPV. |
| P12 before Y3 | Technical replication, IP clearance and documented third-party paid-evaluation interest as defined in §6.3 | OneTech + Legal + commercial sponsor; stop or reclassify when the external-business thesis fails. |
| Quarterly portfolio review | Actual spending, commitments, cash attribution, adoption, exceptions and cost-to-complete | Finance and sponsors; unapproved overruns receive no next tranche. Retain sunk and non-cancellable costs in the forecast. |

Monthly business dashboards and quarterly portfolio reviews track the J-curve and leading indicators. Protect 20–40% champion time only where priced into the project staffing plan; managers approve participation and backfill before pilot launch. Staff practice, employee consultation and safe exception handling precede live deployment. Dates are relative to investment approval, not claims of signed internal schedules.

**Downside discipline:** the model does not assume that general gates magically avoid every loss. H1/H2 downside retains planned spending; P12 explicitly stops with exit cost. Before contracts, obtain cancellation schedules and calculate committed exposure at each gate. Y0 authorisation limits initial purchases, but is not a guarantee of total programme loss. A production plant, new hardware estate or commercial warranty outside these scopes requires a separate approval.

## 10. Recommendation and defense

Approve the **${port['gross_cost']:.2f}m gross planning ceiling** and release **up to ${port['annual_cost'][0]:.2f}m at Y0** only for G0-ready slices. Subsequent spending is conditional. The central return clears the assumed hurdle, and the weighted case remains positive after paying for H3 exploration and removing unsupported retail delivery cash. The downside is negative; the proposal relies on measured continuation decisions, not a claim of risk-free investment.

The core thesis is to improve value capture in selected workflows using existing capabilities, with an explicit experiment in external technology licensing. This is a bounded programme within TotalEnergies, not proof of a group-wide maturity deficit. The reduced-budget response sacrifices meaningful value and learning; it is an alternative if capital is constrained, not the recommended default.

## Appendix A. Sources and model controls

- Group facts, published impairment-WACC proxy and local observations: [source register](../../sources/register.md), [2025 URD](../../sources/primary/totalenergies_universal-registration-document-2025_2026_en.pdf), and the linked syntheses in §§2–4.
- Course: [professor's PDF](../../course/lectures/AI%20Strategy%20-%20Albert%20School%20-%20Master%202026.pdf), pp. 188–206 for decision, scenarios, gates and memo requirements.
- Active financial source: [selected workbook](../../work/finance/portfolio_model_selected.xlsx). The model retains the established tax and cost architecture; commercial inputs remain assumptions.
- [Model methods and verification](../../work/finance/portfolio_economics.md); [scenario data](../../work/finance/selected_chart_data.json); [chart production specification](../../work/projects/chart_regeneration_spec.md).

The report is the source for the two-page memo, then slides. Retired graphics are not evidence for this version. Chart production remains a separate rendering task; no old figure should be copied into the memo or slides. No internal approvals, asset eligibility or observed business returns are asserted.
'''
intro=f'''# TotalEnergies: a selective, gated AI transformation programme

**Full analytical report — revised decision draft, 10 November 2026**  
**Team:** Alexandre Waerniers, Vincent Lamy, Yoni Mahieddine, Nahel Bachriri

## 1. Decision and strategic logic

**Proposed resolution [Judgment]:** approve a **${port['gross_cost']:.2f}m gross planning ceiling** across Y0 and five operating years for seven initiatives and one shared enabler. Release **up to ${port['annual_cost'][0]:.2f}m at Y0**, subject to verified scope, baseline and contractual eligibility. Fund subsequent tranches only against value, adoption, safety and learning gates.

**Decision economics [Calculation on assumptions]:** central NPV **+${port['Base']['npv']:.3f}m**, central IRR **{pct(port['Base']['irr'])}**; probability-weighted NPV **+${port['Weighted']['npv']:.3f}m** and weighted-cash IRR **{pct(port['Weighted']['irr'])}**, at an assumed 10% common screen. Downside NPV is **${port['Downside']['npv']:.3f}m**. No avoided-inaction uplift, H3 commercial receipts or post-Y5 value supports these results.

**Mechanism:** use the existing Digital Line, Digital Factory and segment platforms to improve measurable operating decisions; business owners and Finance sign the incremental cash. Preserve a bounded H3 experiment in third-party e-SAF technology licensing. The proposal is an external team's hypothesis, not a claim that TotalEnergies lacks AI or already approved these scopes. All project amounts are assumptions unless expressly marked as facts.

'''
baseline=old[old.index('## 2.'):old.index('## 5.')]
report=intro+baseline+selection+'## 6. Four detailed cases\n\n'+cases[0]+cases[1]+p12+'\n'+cases[2]+finance
(R/'deliverables/report/full_strategy_report_draft.md').write_text(report,encoding='utf-8')
for ident,text in [('P01',cases[0]),('P03',cases[1]),('P12',p12),('P13',cases[2])]:
    fname={'P01':'case_p01_refining_pdm.md','P03':'case_p03_deepwater_drilling.md','P12':'case_p12_esaf_licensing.md','P13':'case_p13_retail_station_demand.md'}[ident]
    (R/'work/projects'/fname).write_text(text.replace('../../sources/','../../sources/'),encoding='utf-8')
(R/'work/finance/half_envelope_alternative.md').write_text('# Half-budget response\n\n'+finance.split('### 7.1')[1].split('## 8.')[0],encoding='utf-8')
(R/'work/finance/cost_of_inaction.md').write_text('# Cost of inaction\n\n'+finance.split('## 8.')[1].split('## 9.')[0],encoding='utf-8')
(R/'work/finance/portfolio_economics.md').write_text('# Selected portfolio economics\n\n'+finance.split('## 7.')[1].split('## 8.')[0]+'''\n## Reproduction and limits

Run `node work/finance/build_workbook.mjs`, then bundled Python `work/finance/reconcile_selected.py`. The checker independently recomputes all 960 annual benefit/OPEX/CAPEX/tax/net cells from workbook inputs and scenarios, checks the 18 consolidated cumulative flows, scans cached formula errors and verifies the half-budget limit. JSON is a derived chart export, not an editable second model. Re-run after any change. Native Excel recalculation has not been performed for this version.
''',encoding='utf-8')
(R/'work/finance/portfolio_model_14_notes.md').write_text('# Active model\n\nThe active source is [portfolio_model_selected.xlsx](portfolio_model_selected.xlsx). See [economics and verification](portfolio_economics.md). Previous selection and calculations are archived under `work/archive/pre_selection_2026_11_10/`. Do not run archived builders for current outputs.\n',encoding='utf-8')
(R/'work/projects/reserve_cards.md').write_text('# Selected complementary cases\n\n'+selection+'\nAll amounts are assumptions; full scenario flows are in the selected workbook.\n',encoding='utf-8')


