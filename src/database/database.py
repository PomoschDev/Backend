from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from src.app_config.config_db import db_settings
from .db_accessor import DatabaseAccessor

database_accessor = DatabaseAccessor(db_settings=db_settings)

async def get_async_session() -> AsyncGenerator:
    await database_accessor.run()  # Убедитесь, что run вызывается асинхронно
    stub = database_accessor.get_stub()  # Получаем gRPC стуб
    yield stub  # Возвращаем стуб для использования в других методах
