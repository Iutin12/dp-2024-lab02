import pathlib
from app.writer import Writer

class ConsoleWriter(Writer):
    """
    Стратегия для логирования в консоль
    """

    def log(self, message: str) -> None:
        """
        Выводит сообщение в консоль
        """
        print(message)

class FileWriter(Writer):
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

class UpperFileWriter(FileWriter):
    """
    Стратегия для логирования в файл в верхнем регистре
    """


    def log(self, message: str) -> None:
        """
        Записывает сообщение в файл в верхнем регистре
        """
        super().log(message.upper())
