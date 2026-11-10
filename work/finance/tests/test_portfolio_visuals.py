"""Check that the chart dataset and financial workbook stay reconciled."""
import json
from pathlib import Path
import unittest
import openpyxl

WORK = Path(__file__).resolve().parents[2]


class PortfolioVisuals(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((WORK/'projects'/'assets'/'visuals_data.json').read_text(encoding='utf-8'))
        cls.book=openpyxl.load_workbook(WORK/'finance'/'portfolio_model_14_revised.xlsx',data_only=True)

    def test_project_coverage_and_budget(self):
        ids=[p['id'] for p in self.data['projects']]
        self.assertEqual(ids,[f'P{i:02}' for i in range(1,14)]+['E01'])
        self.assertAlmostEqual(self.data['one_time_total'],self.book['Portfolio']['B32'].value,places=8)
        self.assertAlmostEqual(sum(self.data['investment_by_horizon'].values()),self.data['one_time_total'],places=8)

    def test_net_value_and_probability_weighted_benefits(self):
        self.assertAlmostEqual(sum(self.data['weighted_net_npv_by_horizon'].values()),self.book['Portfolio']['B18'].value,places=8)
        self.assertAlmostEqual(sum(self.data['expected_gross_benefits_by_horizon'].values()),self.data['expected_gross_benefits_total'],places=8)
        self.assertEqual(self.data['expected_gross_benefits_by_horizon']['Enabler'],0)
        self.assertLess(self.data['weighted_net_npv_by_horizon']['H3'],0)


if __name__=='__main__':
    unittest.main()
