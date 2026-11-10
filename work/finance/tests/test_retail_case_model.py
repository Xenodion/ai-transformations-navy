import unittest
from decision_cashflows import conventional_irr, npv, payback
from retail_case_model import HURDLE, SCENARIOS, annual_full_scale_benefits, model


class RetailModelTests(unittest.TestCase):
    def test_base_investment_and_disjoint_drivers(self):
        rows = model(SCENARIOS[1])
        self.assertAlmostEqual(sum(row[3] + row[4] for row in rows), 1.0)
        self.assertEqual(annual_full_scale_benefits(),
                         {'waste': .245, 'markdown': .2, 'availability': .14, 'deliveries': .24})

    def test_tax_and_cash_reconcile_year_by_year(self):
        rows = model(SCENARIOS[1])
        for year, benefit, recurring, implementation, capex, tax, cash in rows:
            self.assertAlmostEqual(cash, benefit - recurring - implementation - capex - tax)
            self.assertGreaterEqual(tax, 0)

    def test_scenario_order_and_cash_flow_timing(self):
        downside, base, upside = [tuple(row[-1] for row in model(s)) for s in SCENARIOS]
        self.assertLess(npv(HURDLE, downside), npv(HURDLE, base))
        self.assertLess(npv(HURDLE, base), npv(HURDLE, upside))
        self.assertAlmostEqual(payback(base), 2.32967032967)
        self.assertAlmostEqual(conventional_irr(base), .49546169962)


if __name__ == '__main__':
    unittest.main()
