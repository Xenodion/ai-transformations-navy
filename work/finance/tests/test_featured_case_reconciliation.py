"""Independent numerical controls for the four documented base cases.

These tests verify arithmetic and hurdle mapping, not whether assumptions are
empirically correct. Period cash amounts below are rounded as shown in cards.
"""
import unittest
from industrial_case_models import CASES, model as industrial_model
from retail_case_model import HURDLE, SCENARIOS, model as retail_model


class CaseReconciliationTests(unittest.TestCase):
    def test_case_values_match_documented_flows_and_rates(self):
        expected = {
            'P01': (.095, [-.5, -.67675, .7398125, 1.099109375, 1.3371875, 1.3371875], 2.1156),
            'P03': (.11, [-.4, -1.3, .3505, 1.177, 1.825, 1.825], 1.8591),
            'P11': (.11, [-.4, -1.45, -.175, .32125, 1.0525, 2.1025], .3276),
        }
        for case in CASES:
            rate, expected_flows, expected_npv = expected[case.ident]
            self.assertEqual(case.hurdle, rate)
            actual_flows = [row[-1] for row in industrial_model(case)]
            for actual, expected_cash in zip(actual_flows, expected_flows):
                self.assertAlmostEqual(actual, expected_cash, places=6)
            independently_discounted = sum(cf / ((1 + rate) ** year)
                                           for year, cf in enumerate(expected_flows))
            self.assertAlmostEqual(independently_discounted, expected_npv, places=4)

    def test_retail_documented_flows_and_discounting(self):
        expected = [-.4, -.2475, .46, .56875, .56875, .56875]
        actual = [row[-1] for row in retail_model(SCENARIOS[1])]
        self.assertEqual(HURDLE, .09)
        for a, b in zip(actual, expected):
            self.assertAlmostEqual(a, b, places=6)
        independent_npv = sum(cf / 1.09 ** year for year, cf in enumerate(expected))
        self.assertAlmostEqual(independent_npv, .9719, places=4)


if __name__ == '__main__':
    unittest.main()
