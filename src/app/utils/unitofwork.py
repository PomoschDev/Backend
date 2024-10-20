from abc import ABC, abstractmethod
from typing import Type, Any

from src.app.repositories.metauser.auth_token import AuthTokenRepository
from src.app.repositories.metauser.auth_user import AuthRepository
from src.database.db_accessor import DatabaseAccessor
from src.app_config.config_db import DBSettings

class IUnitOfWork(ABC):
    """Interface for Unit of Work pattern."""
    auth: Type[AuthRepository]
    token: Type[AuthTokenRepository]
    
    @abstractmethod
    def __init__(self):
        """Initialize the Unit of Work instance."""

    @abstractmethod
    async def __aenter__(self):
        """Enter the context manager."""

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit the context manager."""

    @abstractmethod
    async def commit(self):
        """Commit changes."""

class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.database_accessor = DatabaseAccessor(db_settings=DBSettings())
        self.repositories = {}
        self.auth = AuthRepository(self.database_accessor)  # Инициализация auth
        self.token = AuthTokenRepository(self.database_accessor)  # Инициализация token

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.database_accessor.stop()  # Закрываем gRPC канал

    async def commit(self) -> None:
        # Здесь вы можете реализовать логику фиксации изменений
        pass

    def register_repository(self, name: str, repository: Any) -> None:
        """Register a repository with the unit of work."""
        self.repositories[name] = repository

    def get_repository(self, name: str) -> Any:
        """Get a registered repository."""
        return self.repositories.get(name)