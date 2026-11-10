"""Independent numeric reconciliation of all workbook scenario cash flows."""
from pathlib import Path
import unittest
import openpyxl

FILE = Path(__file__).resolve().parents[1] / 'portfolio_model_14_revised.xlsx'


class WorkbookReconciliation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.w = openpyxl.load_workbook(FILE, data_only=True)

    def test_every_project_scenario_and_portfolio(self):
        inputs, scenarios = self.w['Inputs'], self.w['Scenarios']
        build, portfolio = self.w['Cash flow build'], self.w['Portfolio']
        sums = {s: [0.0] * 6 for s in ('Downside', 'Base', 'Upside', 'Severe stress')}
        npvs = {s: 0.0 for s in sums}
        for n in range(56):
            i, j = (n // 3, n % 3) if n < 42 else (n - 42, 3)
            ir, sr, r = i + 2, 2 + i * 3 + j if j < 3 else 44 + i, 2 + 7*n
            name = ('Downside', 'Base', 'Upside', 'Severe stress')[j]
            rate, fx, flag = (inputs.cell(ir,c).value for c in (4,5,6))
            cap0, cap1, launch = (inputs.cell(ir,c).value for c in (7,8,9))
            annual_opex = [inputs.cell(ir,c).value for c in range(10,15)]
            gross = inputs.cell(ir,15).value
            benefit, invest, opex, tax = (scenarios.cell(sr,c).value for c in (3,4,5,6))
            ramps = [scenarios.cell(sr,c).value for c in range(7,12)]
            run, realisation, stop = (scenarios.cell(sr,c).value for c in (12,13,14))
            flows = [-cap0*invest*fx]
            for y in range(1,6):
                period_run = run if y >= 3 else 1
                sales = gross*flag*realisation*benefit*ramps[y-1]*fx*period_run
                costs = (annual_opex[y-1]*opex*period_run + (launch*invest if y == 1 else 0)
                         + (stop if y == 3 else 0))*fx
                capital = cap1*invest*fx if y == 1 else 0
                depreciation = (cap0+cap1)*invest*fx/5
                cash_tax = max(0,sales-costs-depreciation)*tax
                flows.append(sales-costs-capital-cash_tax)
            cumulative = 0
            for y, cash in enumerate(flows):
                self.assertAlmostEqual(build.cell(r+5,y+2).value,cash,places=8)
                cumulative += cash
                self.assertAlmostEqual(build.cell(r+6,y+2).value,cumulative,places=8)
                sums[name][y] += cash*inputs.cell(ir,21).value
            value = sum(cash/(1+rate)**y for y,cash in enumerate(flows))
            self.assertAlmostEqual(build.cell(r,8).value,value,places=8)
            npvs[name] += value*inputs.cell(ir,21).value
        for col,name in enumerate(('Downside','Base','Upside'),2):
            cumulative=0
            for y in range(6):
                cumulative += sums[name][y]
                self.assertAlmostEqual(portfolio.cell(y+6,col).value,cumulative,places=8)
            self.assertAlmostEqual(portfolio.cell(15,col).value,npvs[name],places=8)
        self.assertAlmostEqual(portfolio['B24'].value,npvs['Severe stress'],places=8)
        expected=sum(portfolio.cell(15,c).value*portfolio.cell(17,c).value for c in (2,3,4))
        self.assertAlmostEqual(portfolio['B18'].value,expected,places=8)


if __name__ == '__main__':
    unittest.main()
