import unittest
from decision_cashflows import conventional_irr, npv
from industrial_case_models import CASES, model


class IndustrialCasesTests(unittest.TestCase):
    def test_flows_reconcile(self):
        for case in CASES:
            for _, benefit, recurring, launch, capex, tax, cash in model(case):
                self.assertAlmostEqual(cash, benefit - recurring - launch - capex - tax)
                self.assertGreaterEqual(tax, 0)

    def test_downside_is_lower_than_base_with_given_assumptions(self):
        for case in CASES:
            base = [r[-1] for r in model(case)]
            downside = [r[-1] for r in model(case, benefit_factor=.65, investment_factor=1.2, opex_factor=1.2)]
            self.assertLess(npv(case.hurdle, downside), npv(case.hurdle, base))
            self.assertIsNotNone(conventional_irr(base))

    def test_no_inferred_revenue_before_flexibility_is_live(self):
        case = next(c for c in CASES if c.ident == 'P11')
        self.assertEqual(model(case)[1][1], 0)


if __name__ == '__main__':
    unittest.main()
