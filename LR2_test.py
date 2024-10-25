from contextlib import redirect_stdout
from LR2 import Logger, ConsoleLogStrategy, FileLogStrategy
import unittest
import os
from io import StringIO


class TestLogger(unittest.TestCase):

    def setUp(self):
        """Настройка тестов, создаем временные директории и файлы."""
        self.test_dir = "test_logs"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        """Очистка после тестов."""
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def test_console_logging(self):
        """Тестирование логирования в консоль."""
        logger = Logger(ConsoleLogStrategy())

        with StringIO() as buf, redirect_stdout(buf):
            for i in range(3):
                logger.info(f"Тестовое сообщение {i + 1}")
            output = buf.getvalue()

        self.assertEqual(output.count("Тестовое сообщение"), 3)

    def test_file_logging_creation(self):
        """Тестирование создания файла логов."""
        logger = Logger(FileLogStrategy(self.test_dir))
        logger.info("Тестовое сообщение для создания файла")

        log_file_name = logger._strategy._file.name
        self.assertTrue(os.path.isfile(os.path.join(self.test_dir, log_file_name)))


if __name__ == "__main__":
    unittest.main(exit=False)