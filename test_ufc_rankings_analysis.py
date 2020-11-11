# Marshall Ferguson - 11/2020

# Imports

import unittest
import ufc_rankings_analysis

class TestUfcRankingsAnalysis(unittest.TestCase):

    def test_len_of_csv(self):
        self.assertEqual(ufc_rankings_analysis.line_count, 41431)

if __name__ == "__main__":
    unittest.main()