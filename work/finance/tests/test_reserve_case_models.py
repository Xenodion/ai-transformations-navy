import unittest
from decision_cashflows import npv
from industrial_case_models import model
from reserve_case_models import CASES


class ReserveCaseTests(unittest.TestCase):
    def test_complete_unique_candidate_set_and_correct_rates(self):
        rates = {'P02': .10, 'P04': .10, 'P05': .09, 'P06': .095,
                 'P07': .10, 'P08': .095, 'P09': .10, 'P10': .10,
                 'P12': .12, 'E01': .09}
        self.assertEqual({c.ident for c in CASES}, set(rates))
        self.assertEqual(len(CASES), len(rates))
        for case in CASES:
            self.assertEqual(case.hurdle, rates[case.ident])

    def test_expected_safety_value_is_not_automatically_guaranteed_cash(self):
        p07 = next(c for c in CASES if c.ident == 'P07')
        self.assertEqual(p07.gross_steady, .5)
        self.assertGreater(npv(p07.hurdle, [r[-1] for r in model(p07)]),
                           npv(p07.hurdle, [r[-1] for r in model(p07, benefit_factor=0)]))

    def test_h3_and_shared_governance_have_no_invented_receipts(self):
        for case in CASES:
            if case.ident in {'P12', 'E01'}:
                self.assertEqual(case.gross_steady, 0)
                self.assertTrue(all(row[1] == 0 for row in model(case)))


if __name__ == '__main__':
    unittest.main()
