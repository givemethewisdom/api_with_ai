from typing import Any

from fastapi import HTTPException, status


class BusinessLogicError(HTTPException):
    """
    Кастомная ошибка для бизнес-логики.

    Args:
        field: поле, в котором произошла ошибка (например, "email", "name")
        message: текст ошибки для пользователя
        log: нужно ли логировать эту ошибку (True/False)
        details: дополнительные детали (опционально)
    """

    def __init__(
            self,
            field: str,
            message: str,
            log: bool = True,
            details: None | dict[str, Any] = None
    ):
        # Сохраняем данные для логирования
        self.field = field
        self.message = message
        self.log = log
        self.details = details or {}

        # Создаём тело ответа для клиента
        content = {
            "success": False,
            "error": {
                "field": field,
                "message": message,
                "details": self.details if self.details else None
            }
        }

        # Вызываем конструктор HTTPException с кодом 400
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=content
        )
