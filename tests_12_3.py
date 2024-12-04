import unittest
from tests_12_2 import Runner, Tournament


def frozen_test(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return func(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner = Runner("Тестовый", speed=5)

    @frozen_test
    def test_run(self):
        self.runner.run()
        self.assertEqual(self.runner.distance, 10)

    @frozen_test
    def test_walk(self):
        self.runner.walk()
        self.assertEqual(self.runner.distance, 5)

    @frozen_test
    def test_challenge(self):
        self.runner.run()
        self.runner.walk()
        self.assertEqual(self.runner.distance, 15)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.nick = Runner("Ник", speed=3)

    @frozen_test
    def test_first_tournament(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == "Ник")

    @frozen_test
    def test_second_tournament(self):
        tournament = Tournament(90, Runner("Андрей", speed=9), self.nick)
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == "Ник")

    @frozen_test
    def test_third_tournament(self):
        tournament = Tournament(90, self.usain, Runner("Андрей", speed=9), self.nick)
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == "Ник")
