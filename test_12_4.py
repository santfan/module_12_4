# Импортируем класс из файла rt_with_exceptions и нужные модули
from idlelib.iomenu import encoding
from stat import filemode

import rt_with_exceptions
import unittest
import logging

# Объявим класс тестера класса
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner_walk = rt_with_exceptions.Runner(5, 10)
            for __ in range(10):
                runner_walk.walk()
            self.assertEqual(runner_walk.distance, 100)
            logging.info(f'"test_walk" выполнен успешно {runner_walk}')
        except :
            logging.warning('Неверная скорость для Runner', exc_info=True)
    def test_run(self):
        try:
            runner_run = rt_with_exceptions.Runner('Will', -5)
            for __ in range(10):
                runner_run.run()
            self.assertEqual(runner_run.distance, 100)
            logging.info(f'"test_run" выполнен успешно {runner_run}')
        except :
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_chalenge(self):
        runner_1 = rt_with_exceptions.Runner('Max')
        runner_2 = rt_with_exceptions.Runner('Serg')
        for __ in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

# logging.basicConfig(level=logging.INFO, filemode='a', filename='runner_tests.log',
#                     format="%(asctime)s | %(levelname)s | %(message)s")
# Создаем обработчик для записи в файл с нужной кодировкой
handler = logging.FileHandler('runner_tests.log', 'w', encoding='utf-8')
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
handler.setFormatter(formatter)

# Настраиваем логгер
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# Логируем сообщения
# logger.info("Тестовое сообщение на кириллице")
# logger.info("Another message")