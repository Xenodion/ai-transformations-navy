import unittest
from counterfactual import incremental_path, waiting_gap
from decision_cashflows import npv


class CounterfactualTests(unittest.TestCase):
    def test_comparison_uses_same_baseline_once(self):
        # Both paths include the effects of existing initiatives and baseline drift.
        program = (-3, 8, 12)
        baseline = (0, 5, 7)
        delta = incremental_path(program, baseline)
        self.assertEqual(delta, (-3, 3, 5))
        self.assertAlmostEqual(npv(.1, delta), npv(.1, program) - npv(.1, baseline))

    def test_delaying_does_not_mean_stopping_existing_programmes(self):
        self.assertEqual(waiting_gap((-2, 3, 6), (0, -1, 3)), (-2, 4, 3))

    def test_missing_periods_or_nonfinite_values_fail(self):
        with self.assertRaises(ValueError): incremental_path((1,), (1, 2))
        with self.assertRaises(ValueError): incremental_path((float('nan'),), (0,))


if __name__ == '__main__':
    unittest.main()
