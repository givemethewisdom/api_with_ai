"""logger config"""
import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

from app.core.deps import settings


def setup_logging():
    """Настраивает логирование с ежедневной ротацией"""
    # Создаём директорию для логов
    log_dir = Path(settings.LOG_FILE).parent
    log_dir.mkdir(parents=True, exist_ok=True)

    # Создаём форматтер с именем функции
    formatter = logging.Formatter(
        fmt=settings.LOG_FORMAT,
        datefmt=settings.LOG_DATE_FORMAT
    )

    # --- Хендлер для консоли (все уровни) ---
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, settings.LOG_LEVEL.upper()))
    console_handler.setFormatter(formatter)

    # --- Хендлер для файла с ротацией ПО ДНЯМ (только WARNING и выше) ---
    file_handler = TimedRotatingFileHandler(
        settings.LOG_FILE,
        when="midnight",           # <-- ротация в полночь
        interval=1,                # <-- каждые 1 день
        backupCount=settings.LOG_BACKUP_COUNT,  # сколько файлов хранить
        encoding="utf-8"
    )
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(formatter)

    # --- Настройка корневого логгера ---
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.handlers.clear()
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # --- Подавляем лишние логи от сторонних библиотек ---
    #logging.getLogger("uvicorn").setLevel(logging.WARNING)
    #logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    #logging.getLogger("sqlalchemy").setLevel(logging.WARNING)

    return logging.getLogger(__name__)
