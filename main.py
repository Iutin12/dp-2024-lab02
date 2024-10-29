import datetime
import pathlib
import os
from app.logger import Logger
from app.log_strategy import FileLogStrategy, ConsoleLogStrategy, UpperFileLogStrategy

def main():
    save_folder_path = os.getcwd()
    log_file_name = f"DP.P1.{datetime.datetime.now().strftime('%Y-%m-%d.%H-%M-%S')}.log"
    log_file_path = pathlib.Path(save_folder_path) / log_file_name

    # Логирую в файл
    logger = Logger(FileLogStrategy(log_file_path))
    logger.trace("Начало работы программы")
    logger.info("Программа запущена успешно")

    # Логирование в консоль
    logger.set_writer(ConsoleLogStrategy())
    logger.warn("возможно проблемы")
    logger.error("Ошибка ")
    logger.fatal("Фатальная ошибка")

    # Логирую в верхнем регистре
    logger.set_writer(UpperFileLogStrategy(log_file_path))
    logger.info("Сообщение для верхнего регистра")

if __name__ == "__main__":
    main()
