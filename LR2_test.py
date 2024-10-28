
import unittest
from unittest.mock import MagicMock, patch
import io
from LR2 import Logger, ConsoleLogStrategy, FileLogStrategy, UpperFileLogStrategy


class TestLogger(unittest.TestCase):

    def setUp(self):
        # Создаем экземпляр Logger перед каждым тестом
        self.logger = Logger()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_console_logging(self, mock_stdout):
        # Тестируем логирование в консоль
        strategy = ConsoleLogStrategy()
        self.logger.info("Тестовое сообщение в консоль", strategy)

        output = mock_stdout.getvalue()
        # Проверяем, что вывод содержит нужные строки
        self.assertIn("INFO", output)
        self.assertIn("Тестовое сообщение в консоль", output)

    def test_file_logging_creation(self):
        """Тестирование создания файла логов."""
        logger = Logger(FileLogStrategy(self.test_dir))
        logger.info("Тестовое сообщение для создания файла")

        log_file_name = logger._strategy._file.name
        self.assertTrue(os.path.isfile(os.path.join(self.test_dir, log_file_name)))


if __name__ == "__main__":
    unittest.main(exit=False)
