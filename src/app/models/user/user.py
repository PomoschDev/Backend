from typing import List

from sqlalchemy import String, Boolean
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.app.models.mixin.mixin import CreationDateMixin
from src.app.models.user.user_photo import UserPhotoORM
from src.app.schemas.user.user import UserRole
from src.database.database_metadata import Base
from src.database.types import UUID_PK


class UserORM(Base, CreationDateMixin):
    __tablename__ = "user"

    id: Mapped[UUID_PK]
    email: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=True)
    role: Mapped[UserRole | None] = mapped_column(nullable=True, default=None)
    company: Mapped[bool] = mapped_column(Boolean, nullable=True, default=False)

    photos: Mapped[List["UserPhotoORM"]] = relationship(
        "UserPhotoORM", back_populates="user"
    )
