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
