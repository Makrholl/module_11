import unittest
import logging
from tests_12_2 import Runner

logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("Тестовый", speed=-5)
            runner.walk()
            self.assertEqual(runner.distance, 0)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)

    def test_run(self):
        try:
            runner = Runner(12345, speed=5)
            runner.run()
            self.assertEqual(runner.distance, 10)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)

