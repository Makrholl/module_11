import unittest
from tests_12_3 import RunnerTest, TournamentTest

suite = unittest.TestSuite()

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

