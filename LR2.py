import datetime
import threading
import pathlib
import os


class AbstractLog:
    """Базовый класс для стратегий логирования."""

    def log(self, level: str, message: str) -> None:
      pass


class ConsoleLogStrategy(AbstractLog):
    """Класс для логирования в консоль."""

    def log(self, level: str, message: str) -> None:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"{timestamp} [{level}] {message}")


class FileLogStrategy(AbstractLog):
    """Стратегия логирования в файл с заданным шаблоном имени файла."""

    def __init__(self, directory_path: str):
        self._file = pathlib.Path(directory_path) / self._get_log_file_name()

        with open(self._file, 'w'):
            pass

    def _get_log_file_name(self) -> str:
        """Метод для создания имени файла по заданному шаблону."""
        now = datetime.datetime.now()
        return f"DP.P1.{now.strftime('%Y-%m-%d.%H-%M-%S')}.log"

    def log(self, level: str, message: str) -> None:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{timestamp} [{level}] {message}\n"
        with open(self._file, 'a', encoding='utf-8') as file:
            file.write(log_message)


class UpperCaseFileLogStrategy(FileLogStrategy):
    """Класс для логирования в файл с сообщениями в верхнем регистре."""

    def log(self, level: str, message: str) -> None:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{timestamp} [{level}] {message.upper()}\n"
        with open(self._file, 'a', encoding='utf-8') as file:
            file.write(log_message)


class Logger:
    """Класс для создания логгера."""

    def __init__(self, strategy: AbstractLog):
        """Инициализатор с выбранной стратегией логирования."""
        self._lock = threading.Lock()
        self._strategy = strategy

    def _log(self, level: str, message: str) -> None:
        with self._lock:
            self._strategy.log(level, message)

    def trace(self, message: str) -> None:
        self._log("TRACE", message)

    def info(self, message: str) -> None:
        self._log("INFO", message)

    def warn(self, message: str) -> None:
        self._log("WARN", message)

    def error(self, message: str) -> None:
        self._log("ERROR", message)

    def fatal(self, message: str) -> None:
        self._log("FATAL", message)


def main():
    print("Выберите способ логирования:")
    print("1. Логировать в консоль")
    print("2. Логировать в файл")
    print("3. Логировать в файл (в верхнем регистре)")

    choice = input("Введите номер выбранного способа: ")
    save_folder_path = os.getcwd()

    if choice == "1":
        logger = Logger(ConsoleLogStrategy())
    elif choice == "2":
        logger = Logger(FileLogStrategy(save_folder_path))
    elif choice == "3":
        logger = Logger(UpperCaseFileLogStrategy(save_folder_path))
    else:
        print("Неверный выбор. Используется логирование в консоль по умолчанию.")
        logger = Logger(ConsoleLogStrategy())

    # Примеры записи логов
    logger.trace("Начало работы программы")
    logger.info("Программа запущена успешно")
    logger.warn("Возможны проблемы с соединением с базой данных")
    logger.error("Ошибка выполнения операции")
    logger.fatal("Критическая ошибка, программа завершается")


if __name__ == "__main__":
    main()
