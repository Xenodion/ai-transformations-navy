"""Behavioral checks for decision cash-flow semantics, not project economics."""
import unittest
from decision_cashflows import Period, Project, aggregate, conventional_irr, expected_value, npv, payback


class DecisionCashFlowTests(unittest.TestCase):
    def test_h3_learning_cost_remains_without_speculative_revenue(self):
        p = Project('H3 learning', (Period(capital_cost=2), Period(operating_cost=1)))
        self.assertEqual(p.cash(), (-2, -1))

    def test_reserve_is_not_funded_until_approved(self):
        p = Project('reserve', (Period(capital_cost=10), Period(benefit=50)), approved=False)
        self.assertEqual(p.cash(), (0, 0))

    def test_stop_retains_sunk_and_unavoidable_costs_without_later_benefits(self):
        p = Project('pilot', (Period(capital_cost=3), Period(benefit=7, exit_cost=2, unavoidable_cost=1),
                              Period(benefit=20, unavoidable_cost=0.5)), stop_at=1)
        self.assertEqual(p.cash(), (-3, -3, -0.5))

    def test_unrelated_project_continues(self):
        a = Project('failed', (Period(capital_cost=1), Period(benefit=10)), stop_at=1)
        b = Project('independent', (Period(capital_cost=2), Period(benefit=5)))
        self.assertEqual(aggregate((a, b)), (-3, 5))

    def test_npv_and_expected_value(self):
        self.assertAlmostEqual(npv(.10, (-100, 110)), 0)
        self.assertAlmostEqual(expected_value(((.25, -10), (.75, 6))), 2)
        with self.assertRaises(ValueError): expected_value(((.2, 4), (.2, 6)))

    def test_payback_distinguishes_no_recovery_and_interpolated_time(self):
        self.assertAlmostEqual(payback((-100, 50, 100)), 1.5)
        self.assertIsNone(payback((-100, 20, 20)))
        self.assertAlmostEqual(payback((-100, 110), .10), 1)

    def test_tax_refund_and_working_capital_release_are_cash_inflows(self):
        p = Project('release', (Period(capital_cost=3), Period(tax_cash=-1, working_capital=-2)))
        self.assertEqual(p.cash(), (-3, 3))

    def test_irr_handles_negative_return_no_recovery_and_multiple_sign_changes(self):
        self.assertAlmostEqual(conventional_irr((-100, 110)), .10)
        self.assertAlmostEqual(conventional_irr((-100, 80)), -.20)
        self.assertIsNone(conventional_irr((-100, -10, 0)))
        with self.assertRaises(ValueError): conventional_irr((-100, 250, -160))


if __name__ == '__main__':
    unittest.main()
