import pathlib
from abc import ABC, abstractmethod

class Writer(ABC):
    """
    Абстрактный класс для выбора стратегий логирования
    """

    @abstractmethod
    def log(self, message: str) -> None:
        """
        Записывает сообщение
        """
        pass

class ConsoleLogStrategy(Writer):
    """
    Стратегия для логирования в консоль
    """

    def log(self, message: str) -> None:
        """
        Выводит сообщение в консоль
        """
        print(message)

class FileLogStrategy(Writer):
    """
    Стратегия для логирования в файл
    """

    def __init__(self, file_path: pathlib.Path):
        """
        Инициализирует стратегию логирования в файл
        """
        self.file_path = file_path

    def log(self, message: str) -> None:
        """
        Записывает сообщение в файл
        """
        with open(self.file_path, 'a', encoding='utf-8') as file:
            file.write(message + '\n')

class UpperFileLogStrategy(FileLogStrategy):
    """
    Стратегия для логирования в файл в верхнем регистре
    """


    def log(self, message: str) -> None:
        """
        Записывает сообщение в файл в верхнем регистре
        """
        super().log(message.upper())
