"""Exception handlers"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
import traceback

from app.core.exceptions import BusinessLogicError

logger = logging.getLogger(__name__)


def register_exception_handlers(app: FastAPI):
    """Регистрирует все глобальные обработчики ошибок"""

    @app.exception_handler(BusinessLogicError)
    async def business_logic_error_handler(request: Request, exc: BusinessLogicError):
        """обработчик для ошибок валидации в pydentic моделях связанных с бизнес логикой"""
        if exc.log:
            logger.error(
                f"Business logic error | "
                f"Field: {exc.field} | "
                f"Message: {exc.message} | "
                f"Details: {exc.details} | "
                f"Path: {request.url.path}"
            )
        else:
            logger.info(
                f"Business logic error (no log) | "
                f"Field: {exc.field} | "
                f"Message: {exc.message}"
            )

        # Возвращаем ответ клиенту
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.detail
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        """Глобальный обработчик для всех необработанных исключений"""
        # Логируем ошибку
        logger.error(f"Unhandled exception: {exc}")
        logger.error(traceback.format_exc())

        # Возвращаем безопасный ответ
        return JSONResponse(
            status_code=500,
            content={"error": "Internal server error"}
        )