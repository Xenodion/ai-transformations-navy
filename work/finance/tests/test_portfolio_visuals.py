"""Check that the chart dataset and financial workbook stay reconciled."""
import json
from pathlib import Path
import unittest
import openpyxl

WORK = Path(__file__).resolve().parents[2]


class PortfolioVisuals(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((WORK/'projects'/'assets'/'notebook_chart_data.json').read_text(encoding='utf-8'))
        cls.book=openpyxl.load_workbook(WORK/'finance'/'portfolio_model_14_revised.xlsx',data_only=True)

    def test_project_coverage_and_budget(self):
        ids=[p['id'] for p in self.data['project_plot_inputs']]
        self.assertEqual(ids,[f'P{i:02}' for i in range(1,14)]+['E01'])
        self.assertAlmostEqual(sum(self.data['capital'].values()),self.book['Portfolio']['B32'].value,places=8)

    def test_net_value_and_probability_weighted_benefits(self):
        self.assertAlmostEqual(sum(self.data['net_5y_weighted_npv'].values()),self.book['Portfolio']['B18'].value,places=8)
        self.assertEqual(self.data['gross_5y']['Enabler'],0)
        self.assertLess(self.data['net_5y_weighted_npv']['H3'],0)
        by_project=self.data['long_term_gross_benefits_by_project_and_year']
        self.assertEqual(len(by_project),14)
        self.assertTrue(all(len(values)==15 for values in by_project.values()))
        self.assertAlmostEqual(sum(sum(values) for values in by_project.values()),sum(self.data['gross_15y_illustrative'].values()),places=8)
        h3=sum(sum(by_project[p]) for p in ('P11','P12'))
        self.assertAlmostEqual(h3,self.data['gross_15y_illustrative']['H3'],places=8)

    def test_long_term_discounted_cash_bridge(self):
        schedule=self.data['long_term_net_cash_y6_y15']
        projected=self.data['long_term_npv_by_project']
        inputs=self.book['Inputs']
        metrics=self.book['Metrics']
        weights=self.data['weights']
        totals={h:0 for h in ('H1','H2','H3','Enabler')}
        for n in range(14):
            row=n+2;ident=inputs.cell(row,1).value;horizon=inputs.cell(row,3).value
            rate=inputs.cell(row,4).value;flag=inputs.cell(row,21).value
            initial=sum(weights[j]*metrics.cell(2+n*3+j,5).value*flag for j in range(3))
            future=sum(cf/(1+rate)**year for year,cf in enumerate(schedule[ident],6))
            self.assertAlmostEqual(initial+future,projected[ident],places=8)
            totals[horizon]+=projected[ident]
        for h in totals:
            self.assertAlmostEqual(totals[h],self.data['net_15y_illustrative'][h],places=8)


if __name__=='__main__':
    unittest.main()
