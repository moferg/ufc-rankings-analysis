# Marshall Ferguson - 11/2020

# Imports

import unittest
import ufc_rankings_analysis
from pandas import DataFrame

class TestUfcRankingsAnalysis(unittest.TestCase):

    def test_variable_types(self):
        self.assertEqual(type(ufc_rankings_analysis.df), DataFrame)

if __name__ == "__main__":
    unittest.main()