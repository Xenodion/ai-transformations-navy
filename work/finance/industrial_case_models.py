"""Provisional P01/P03/P11 scenarios, USD million, year-end cash flows.

Amounts and adoption ramps are explicit assumptions, not TotalEnergies facts.
Refer to the individual project cards for evidence and limitations.
"""
from dataclasses import dataclass
from decision_cashflows import conventional_irr, npv, payback


@dataclass(frozen=True)
class Case:
    ident: str
    hurdle: float
    capex_y0: float
    capex_y1: float
    launch_opex_y1: float
    recurring_opex: tuple[float, ...]
    gross_steady: float
    ramp: tuple[float, ...]


# P01: 250k b/day * 365 * .5% availability * 70% sale realization
# * $6/b contribution + $0.20m independently verified repair savings.
# P03: 2 operated rigs * 6 avoidable days/rig * $0.4m/day * 60% cash capture.
# P11: conditional 250 MW * $15,000/MW/year retained margin after customers.
CASES = (
    Case('P01', .095, .50, .50, .40, (.20, .35, .40, .40, .40),
         250_000 * 365 * .005 * .70 * 6 / 1e6 + .20, (.20, .60, .85, 1, 1)),
    Case('P03', .11, .40, .40, .60, (.30, .45, .50, .50, .50),
         2 * 6 * .4 * .60, (0, .30, .70, 1, 1)),
    Case('P11', .11, .40, .40, .70, (.35, .55, .75, .90, 1.00),
         250 * .015, (0, .10, .30, .60, 1)),
)


def model(case, benefit_factor=1, investment_factor=1, opex_factor=1, ramp=None):
    ramp = case.ramp if ramp is None else ramp
    if len(ramp) != 5:
        raise ValueError('Exactly five annual realization fractions required')
    capex = (case.capex_y0 + case.capex_y1) * investment_factor
    depreciation = capex / 5  # assumption: straight-line, commissioning Y1
    rows = [(0, 0., 0., 0., case.capex_y0 * investment_factor, 0., -case.capex_y0 * investment_factor)]
    for year in range(1, 6):
        benefit = case.gross_steady * benefit_factor * ramp[year - 1]
        recurring = case.recurring_opex[year - 1] * opex_factor
        launch = case.launch_opex_y1 * investment_factor if year == 1 else 0.
        capital = case.capex_y1 * investment_factor if year == 1 else 0.
        tax = max(0., benefit - recurring - launch - depreciation) * .25
        cash = benefit - recurring - launch - capital - tax
        rows.append((year, benefit, recurring, launch, capital, tax, cash))
    return rows


def main():
    print('Illustrative project scenarios; USD million, not company forecasts')
    for case in CASES:
        flows = [row[-1] for row in model(case)]
        irr = conventional_irr(flows)
        print(case.ident, 'gross_steady=', round(case.gross_steady, 4),
              'flows=', [round(f, 4) for f in flows],
              'NPV=', round(npv(case.hurdle, flows), 4),
              'IRR=', round(irr * 100, 2) if irr is not None else 'undefined',
              'payback=', 'not reported for H3' if case.ident == 'P11' else payback(flows))


if __name__ == '__main__':
    main()
