"""Indicative limited-scope candidate models; USD million, not forecasts.

The same simplified accounting convention as industrial_case_models applies.
P12 and E01 are cost/learning-only in the programme base; they have no invented
standalone benefit or payback. P07's benefit is expected incident cost, not a
guaranteed accounting saving. All unit economics are assumptions.
"""
from industrial_case_models import Case, model
from decision_cashflows import conventional_irr, npv, payback


CASES = (
    # 2 hubs * 150 recovered barrels/day * 365 * $15/b contribution.
    Case('P02', .10, .35, .25, .30, (.18, .25, .30, .30, .30),
         2 * 150 * 365 * 15 / 1e6, (.10, .40, .70, 1, 1)),
    # 2 GW * 8,760 hours * 30% capacity factor * .3% availability * $25/MWh.
    Case('P04', .10, .15, .15, .10, (.05, .07, .10, .10, .10),
         2_000 * 8760 * .30 * .003 * 25 / 1e6, (.20, .50, .80, 1, 1)),
    # 10k paid licenses * 15% removed * $30/month * 12 months.
    Case('P05', .09, .10, .10, .10, (.05, .08, .10, .10, .10),
         10_000 * .15 * 30 * 12 / 1e6, (.25, .60, 1, 1, 1)),
    # $50m eligible spend * 1% incremental cash saving; excludes existing plan.
    Case('P06', .095, .20, .20, .10, (.08, .10, .12, .12, .12),
         50 * .01, (.10, .40, .70, 1, 1)),
    # Expected incident cost: four annual incidents * $0.5m direct cost * 25%.
    Case('P07', .10, .20, .20, .20, (.10, .15, .18, .18, .18),
         4 * .5 * .25, (.10, .40, .70, 1, 1)),
    # 500k eligible accounts * 10% churn * 10% relative reduction * $150 margin.
    Case('P08', .095, .20, .20, .20, (.10, .15, .20, .20, .20),
         500_000 * .10 * .10 * 150 / 1e6, (.10, .40, .70, 1, 1)),
    # 30 controllable voyages * $1m eligible fuel cost/voyage * 2% saving.
    Case('P09', .10, .15, .15, .20, (.08, .10, .12, .12, .12),
         30 * 1 * .02, (0, .35, .70, 1, 1)),
    # 2 plants * 500k tonnes/year * 1% improvement * $50/t incremental margin.
    Case('P10', .10, .25, .25, .25, (.10, .15, .20, .20, .20),
         2 * 500_000 * .01 * 50 / 1e6, (0, .30, .70, 1, 1)),
    # H3 research has no monetized base receipts; staged learning cost only.
    Case('P12', .12, .30, .30, .40, (.20, .30, .40, .45, .50),
         0, (0, 0, 0, 0, 0)),
    # Shared register is a cost enabler, not a standalone benefit.
    Case('E01', .09, .05, .05, .20, (.10, .12, .14, .14, .14),
         0, (0, 0, 0, 0, 0)),
)


def main():
    print('Indicative scoped cases: USD million, assumption-driven')
    for c in CASES:
        flows = [r[-1] for r in model(c)]
        if c.ident in {'P12', 'E01'}:
            print(c.ident, 'one-time investment=', c.capex_y0 + c.capex_y1 + c.launch_opex_y1,
                  'cash flows=', [round(x, 4) for x in flows], 'no standalone benefit or payback')
            continue
        irr = conventional_irr(flows)
        print(c.ident, 'gross=', round(c.gross_steady, 4), 'NPV=', round(npv(c.hurdle, flows), 4),
              'IRR=', round(irr * 100, 2) if irr is not None else 'undefined',
              'payback=', payback(flows), 'rate=', c.hurdle)


if __name__ == '__main__':
    main()
