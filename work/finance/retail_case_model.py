"""P13 pilot cash-flow model. EUR million, annual periods, 2026 decision.

The investment is an indicative calibration assumption (CLM-078). All allocation, benefit,
adoption, operating-cost and tax inputs are explicit modeling assumptions,
not statements of Argedis actuals. No rollout beyond 100 stores is included.
"""
from dataclasses import dataclass
from decision_cashflows import conventional_irr, npv, payback

HURDLE = .09  # P13, discount_rate_policy.md
STORES = 100


@dataclass(frozen=True)
class Scenario:
    name: str
    benefit_factor: float
    investment_factor: float
    opex_factor: float
    ramp: tuple[float, ...]


SCENARIOS = (
    Scenario('Downside', .70, 1.15, 1.20, (.35, .60, .80, 1, 1)),
    Scenario('Base', 1, 1, 1, (.50, .80, 1, 1, 1)),
    Scenario('Upside', 1.15, 1, 1, (.65, .90, 1, 1, 1)),
)


def annual_full_scale_benefits():
    """Separate disjoint items; EUR million/year, assumed full adoption."""
    # 350k perishable sales/store * 70% inventory-cost share * 4% waste
    # * 25% reduction. Markdown benefit below applies to different items.
    waste = STORES * 350_000 * .70 * .04 * .25 / 1_000_000
    # 1,000 distinct markdown items/store * EUR 2 incremental net recovery.
    markdown = STORES * 1_000 * 2 / 1_000_000
    # EUR 50k lost sales/store * 8% recapture * 35% incremental margin.
    availability = STORES * 50_000 * .08 * .35 / 1_000_000
    # 80 urgent deliveries/store/year * 50% reduction * EUR 60 variable cost.
    # Both baseline and achievable reduction require invoice-level validation.
    deliveries = STORES * 80 * .50 * 60 / 1_000_000
    return {'waste': waste, 'markdown': markdown,
            'availability': availability, 'deliveries': deliveries}


def model(scenario):
    gross = sum(annual_full_scale_benefits().values()) * scenario.benefit_factor
    # EUR 1m pilot split: EUR .8m capitalised equipment/software, EUR .2m
    # implementation expense. Half of capex paid at t0; the rest plus
    # implementation is spent in Y1. Classification is provisional.
    capex = .8 * scenario.investment_factor
    implementation = .2 * scenario.investment_factor
    depreciation = capex / 5  # straight-line, available from Y1
    annual_opex = (.06, .10, .12, .12, .12)
    rows = [(0, 0.0, 0.0, 0.0, capex / 2, 0.0, -capex / 2)]
    for year in range(1, 6):
        benefit = gross * scenario.ramp[year - 1]
        recurring = annual_opex[year - 1] * scenario.opex_factor
        initial_expense = implementation if year == 1 else 0
        capital = capex / 2 if year == 1 else 0
        taxable = max(0.0, benefit - recurring - initial_expense - depreciation)
        # Illustrative 25% rate; no loss carryforward or use of existing tax
        # capacity. Confirm actual corporate tax treatment and amortisation.
        tax = taxable * .25
        cash = benefit - recurring - initial_expense - capital - tax
        rows.append((year, benefit, recurring, initial_expense, capital, tax, cash))
    return rows


def main():
    print('P13: annual model, EUR million; inputs are assumptions, not actual results')
    print('Full-scale benefit components:', annual_full_scale_benefits())
    for scenario in SCENARIOS:
        rows = model(scenario)
        flows = tuple(row[-1] for row in rows)
        print(scenario.name, 'cash=', [round(x, 4) for x in flows],
              'NPV=', round(npv(HURDLE, flows), 4),
              'IRR=', conventional_irr(flows),
              'payback=', payback(flows), 'discounted=', payback(flows, HURDLE))


if __name__ == '__main__':
    main()
