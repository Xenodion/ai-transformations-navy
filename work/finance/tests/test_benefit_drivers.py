"""Checks on economic drivers and failure cases, not validation of assumptions."""
import unittest
from benefit_drivers import drilling_cash_saving, refinery_margin, retail_writeoff_reduction


class BenefitDriversTests(unittest.TestCase):
    def test_retail_reconciles_at_consistent_cost_basis(self):
        self.assertAlmostEqual(retail_writeoff_reduction(180, 375000, .045, .2, 1), 607500)
        self.assertAlmostEqual(retail_writeoff_reduction(180, 375000, .045, .2, .5), 303750)

    def test_fixed_rig_contract_does_not_create_cash(self):
        self.assertEqual(drilling_cash_saving(10, 0, .193), 0)
        self.assertEqual(drilling_cash_saving(10, 450000, .193, 100000), 768500)

    def test_refinery_value_respects_realized_output(self):
        self.assertEqual(refinery_margin(365000000, .0055, 0, 7.1), 0)

    def test_invalid_fractions_rejected(self):
        with self.assertRaises(ValueError): retail_writeoff_reduction(10, 50, .1, 1.5, 1)
        with self.assertRaises(ValueError): drilling_cash_saving(10, 50, -1)


if __name__ == '__main__':
    unittest.main()
