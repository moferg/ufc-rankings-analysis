# Marshall Ferguson - 11/2020

# Imports

import unittest
import ufc_rankings_analysis

class TestUfcRankingsAnalysis(unittest.TestCase):

    def test_len_of_csv(self):
        self.assertEqual(ufc_rankings_analysis.line_count, 41431)

    def test_len_of_lists(self):
        self.assertEqual(len(ufc_rankings_analysis.date), ufc_rankings_analysis.line_count - 1)
        self.assertEqual(len(ufc_rankings_analysis.weight_class), ufc_rankings_analysis.line_count - 1)
        self.assertEqual(len(ufc_rankings_analysis.fighter_name), ufc_rankings_analysis.line_count - 1)
        self.assertEqual(len(ufc_rankings_analysis.rank), ufc_rankings_analysis.line_count - 1)

if __name__ == "__main__":
    unittest.main()