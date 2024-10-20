from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String

from src.app.schemas.auth import User
from src.app.schemas.types import UserRole
from src.app.models.mixin import IsActiveMixin, CreationDateMixin

from src.database.database_metadata import Base
from src.database.types import UUID_PK, str_20, str_64
from datetime import date

from sqlalchemy import Date, func


class UserORM(Base, IsActiveMixin, CreationDateMixin):
    __tablename__ = "auth_user"

    id: Mapped[UUID_PK]
    email: Mapped[str] = mapped_column(
        String(20), default=str, index=True, nullable=False
    )
    
    username: Mapped[str] = mapped_column(String, default=str, nullable=False)

    password: Mapped[str_64]
    
    role: Mapped[UserRole | None] = mapped_column(nullable=True, default=None)

    type: Mapped[str] = mapped_column(String, nullable=False)

    updated_at: Mapped[date] = mapped_column(Date(), server_default=func.current_date())
    
    def get_schema(self) -> User:
        return User(
            id=self.id,
            login=self.login,
            hashed_password=self.hashed_password,
            role=self.role,
            is_active=self.is_active,
        )