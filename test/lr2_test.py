import unittest
from unittest.mock import MagicMock, patch
import io
from app.log_strategy import ConsoleWriter, FileWriter, UpperFileWriter
from app.logger import Logger

class TestLogger(unittest.TestCase):

    def setUp(self):
        """Создаем экземпляр Logger перед каждым тестом."""
        self.log_file_path = 'dummy_path.log'  # Путь к файлу для тестов
        self.logger = Logger(FileWriter(self.log_file_path))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_console_logging(self, mock_stdout):
        """Тестируем логирование в консоль."""
        self.logger.set_writer(ConsoleWriter())
        self.logger.info("Тестовое сообщение в консоль")

        output = mock_stdout.getvalue()

        self.assertIn("INFO", output)
        self.assertIn("Тестовое сообщение в консоль", output)

    def test_file_logging(self):
        """Тестируем логирование в файл."""
        with patch('builtins.open', new_callable=MagicMock) as mock_open:
            mock_file = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_file

            self.logger.error("Тестовое ошибочное сообщение")

            mock_open.assert_called_once_with(self.log_file_path, 'a', encoding='utf-8')
            mock_file.write.assert_called()
            written_message = mock_file.write.call_args[0][0]
            self.assertIn("ERROR", written_message)
            self.assertIn("Тестовое ошибочное сообщение", written_message)

    def test_upper_file_logging(self):
        """Тестируем логирование в файл в верхнем регистре."""
        with patch('builtins.open', new_callable=MagicMock) as mock_open:
            mock_file = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_file

            self.logger.set_writer(UpperFileWriter(self.log_file_path))
            self.logger.info("Тестовое сообщение с верхним регистром")

            mock_open.assert_called_once_with(self.log_file_path, 'a', encoding='utf-8')
            mock_file.write.assert_called()
            written_message = mock_file.write.call_args[0][0]
            self.assertIn("INFO", written_message)
            self.assertIn("ТЕСТОВОЕ СООБЩЕНИЕ С ВЕРХНИМ РЕГИСТРОМ", written_message)

if __name__ == '__main__':
    unittest.main()
