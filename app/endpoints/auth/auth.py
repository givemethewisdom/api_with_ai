import logging

from fastapi import APIRouter

from app.core.deps import settings
from app.domain.shemas.auth_shemas import RegisterModel

router = APIRouter(prefix="/auth", tags=["auth"])
logger = logging.getLogger(__name__)

@router.post("/register")
async def register(data: RegisterModel) -> dict:
    logger.info(settings.SECRET)
    logger.info(settings.DB_USER)
    return {'код отправлен на почту': data.email}
