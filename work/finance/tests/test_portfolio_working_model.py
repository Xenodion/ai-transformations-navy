import unittest
from decision_cashflows import npv
from portfolio_working_model import RATES, USD_PER_EUR, components, portfolio
from retail_case_model import SCENARIOS, model


class PortfolioWorkingTests(unittest.TestCase):
    def test_per_project_and_portfolio_sum_reconcile(self):
        parts = components()
        cash, value = portfolio()
        self.assertEqual(set(parts), set(RATES))
        self.assertAlmostEqual(value, sum(npv(RATES[k], v) for k, v in parts.items()))
        for t in range(6):
            self.assertAlmostEqual(cash[t], sum(v[t] for v in parts.values()))

    def test_retail_currency_conversion_is_applied_once(self):
        self.assertAlmostEqual(components()['P13'][0], model(SCENARIOS[1])[0][-1] * USD_PER_EUR)

    def test_h3_receipts_are_conditionally_added_costs_never_removed(self):
        base = components()['P11']
        conditional = components(include_p11_commercial=True)['P11']
        self.assertEqual(base[:2], conditional[:2])
        self.assertLess(sum(base), 0)
        self.assertGreater(sum(conditional), sum(base))

    def test_downside_worsens_npv_without_claiming_actual_frequency(self):
        self.assertLess(portfolio('downside')[1], portfolio('base')[1])
        self.assertLess(portfolio('base')[1], portfolio('upside')[1])


if __name__ == '__main__':
    unittest.main()
