"""SUPERSEDED core-only calculation: not the 14-initiative portfolio.

Use portfolio_model_14.xlsx for the complete 14-initiative working scenario.
This file is retained temporarily for comparison with the original four cases.

No reserve candidates are automatically funded. P11's learning/operating costs
are included; commercial cash is excluded unless explicitly requested. E01 is
included once and is not assigned fictitious standalone benefit. No further
overlap adjustment is assumed, so project baselines still require validation.
"""
from decision_cashflows import conventional_irr, npv, payback
from industrial_case_models import CASES as FEATURED, model as industrial_model
from reserve_case_models import CASES as RESERVE
from retail_case_model import SCENARIOS as RETAIL_SCENARIOS, model as retail_model

USD_PER_EUR = 1.1165  # 6 Nov 2026 ECB reference (CLM-071), constant assumption
RATES = {'P01': .095, 'P03': .11, 'P11': .11, 'P13': .09, 'E01': .09}


def components(scenario='base', include_p11_commercial=False):
    if scenario not in {'downside', 'base', 'upside'}:
        raise ValueError('Unknown scenario')
    scale = {'downside': (.65, 1.2, 1.2), 'base': (1, 1, 1), 'upside': (1.15, 1, 1)}[scenario]
    costs = (scale[1], scale[2])
    result = {}
    for case in FEATURED:
        benefit = scale[0] if case.ident != 'P11' or include_p11_commercial else 0
        result[case.ident] = tuple(row[-1] for row in industrial_model(case, benefit, *costs))
    retail_scenario = RETAIL_SCENARIOS[{'downside': 0, 'base': 1, 'upside': 2}[scenario]]
    result['P13'] = tuple(row[-1] * USD_PER_EUR for row in retail_model(retail_scenario))
    enabler = next(c for c in RESERVE if c.ident == 'E01')
    result['E01'] = tuple(row[-1] for row in industrial_model(enabler, 0, *costs))
    return result


def portfolio(scenario='base', include_p11_commercial=False):
    parts = components(scenario, include_p11_commercial)
    cash = tuple(sum(part[t] for part in parts.values()) for t in range(6))
    # Sum each case at its own specified rate, including enabler and H3 cost.
    risk_adjusted_npv = sum(npv(RATES[k], flow) for k, flow in parts.items())
    return cash, risk_adjusted_npv


def main():
    print('ILLUSTRATIVE: four featured projects and E01; USD million')
    for name in ('downside', 'base', 'upside'):
        cash, value = portfolio(name)
        irr = conventional_irr(cash)
        print(name, 'cash=', [round(x, 4) for x in cash],
              'sum NPV at case hurdles=', round(value, 4),
              'IRR=', round(100 * irr, 2) if irr is not None else 'undefined',
              'payback=', payback(cash))
    cash, value = portfolio('base', include_p11_commercial=True)
    print('P11 commercial illustration (conditional, not programme base):',
          'sum project NPV=', round(value, 4), 'cash=', [round(x, 4) for x in cash])


if __name__ == '__main__':
    main()
