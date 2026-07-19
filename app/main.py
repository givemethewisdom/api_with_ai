import logging

from fastapi import FastAPI

from app.core.logger_config import setup_logging
from app.endpoints.auth import auth
from app.middlwares.error_handlers import register_exception_handlers

app = FastAPI(title='AI API')


logger = logging.getLogger(__name__)
logger = setup_logging()


register_exception_handlers(app)


app.include_router(auth.router)

