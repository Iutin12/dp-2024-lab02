from abc import ABC, abstractmethod


class LoggerInterface(ABC):
    """
    Интерфейс для логирования сообщений разного уровня
    """

    @abstractmethod
    def trace(self, message: str) -> None:
        """
        Записывает сообщение уровня TRACE
        """
        pass

    @abstractmethod
    def info(self, message: str) -> None:
        """
        Записывает сообщение уровня INFO
        """
        pass

    @abstractmethod
    def warn(self, message: str) -> None:
        """
        Записывает сообщение уровня WARN.
        """
        pass

    @abstractmethod
    def error(self, message: str) -> None:
        """
        Записывает сообщение уровня ERROR.
        """
        pass

    @abstractmethod
    def fatal(self, message: str) -> None:
        """
        Записывает сообщение уровня FATAL.
        """
        pass
