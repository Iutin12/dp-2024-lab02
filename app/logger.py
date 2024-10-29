import datetime
import threading
from app.log_strategy import Writer
from app.logger_interface import LoggerInterface

class Logger(LoggerInterface):
    """
    Класс, представляющий логгер для записи сообщений с различными уровнями важности
    """

    _instance = None
    _file_lock = threading.Lock()
    _init_lock = threading.Lock()

    def __new__(cls, *args):
        """
        Создает экземпляр класса
        """
        with cls._init_lock:
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self, log_strategy: Writer):
        """
        Инициализирует Logger с заданной стратегией логирования
        """
        self._log_strategy = log_strategy

    def set_writer(self, log_strategy: Writer):
        """
        Устанавливает новую стратегию логирования
        """
        self._log_strategy = log_strategy

    def _create_log_message(self, level: str, message: str) -> str:
        """
        Создает форматированное сообщение для логирования
        """
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        return f"{timestamp} [{level}] {message}"

    def _log(self, level: str, message: str) -> None:
        """
        Записывает сообщение с заданным уровнем важности
        """
        log_message = self._create_log_message(level, message)
        self._log_strategy.log(log_message)

    def trace(self, message: str) -> None:
        """
        Записывает сообщение уровня TRACE
        """
        self._log("TRACE", message)

    def info(self, message: str) -> None:
        """
        Записывает сообщение уровня INFO
        """
        self._log("INFO", message)

    def warn(self, message: str) -> None:
        """
        Записывает сообщение уровня WARN
        """
        self._log("WARN", message)

    def error(self, message: str) -> None:
        """
        Записывает сообщение уровня ERROR
        """
        self._log("ERROR", message)

    def fatal(self, message: str) -> None:
        """
        Записывает сообщение уровня FATAL
        """
        self._log("FATAL", message)
