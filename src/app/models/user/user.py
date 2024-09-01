from typing import List, Optional
from uuid import UUID, uuid4

from sqlalchemy import String, Boolean, Integer, Enum as SQLAEnum
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.app.models.mixin.mixin import CreationDateMixin
from src.app.schemas.user.user import UserRole
from src.database.database_metadata import Base
from src.database.types import UUID_PK


class UserORM(Base):
    __tablename__ = "user"

    id: Mapped[UUID_PK]
    email: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    role: Mapped[UserRole] = mapped_column(
        SQLAEnum(UserRole), nullable=False, default=UserRole.PersonRole
    )
    company: Mapped[Optional[bool]] = mapped_column(
        Boolean, nullable=True, default=False
    )

    photos: Mapped[List["UserPhotoORM"]] = relationship(
        "UserPhotoORM", back_populates="user"
    )
    baskets: Mapped[List["ProductBasketORM"]] = relationship(
        "ProductBasketORM", back_populates="user"
    )
    natural_users: Mapped[List["NaturalUserORM"]] = relationship(
        "NaturalUserORM", back_populates="user"
    )
    company_users: Mapped[List["CompanyUserORM"]] = relationship(
        "CompanyUserORM", back_populates="user"
    )
