from fastapi import APIRouter
from .v1.auth import router as auth_v1
from src.app_config.config_api import settings

router = APIRouter(prefix=settings.APP_PREFIX)

router.include_router(auth_v1)