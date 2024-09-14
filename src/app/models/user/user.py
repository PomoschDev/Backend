from typing import List, Optional
from uuid import UUID, uuid4

from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    Boolean,
    Integer,
    Enum as SQLAEnum,
    Table,
)
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.app.models.mixin.mixin import CreationDateMixin
from src.app.schemas.user.user import UserSchema
from src.app.schemas.user.user_role import UserRole
from src.database.database_metadata import Base
from src.database.types import UUID_PK

user_photos = Table(
    "user_photos",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("photo_id", ForeignKey("photo.id"), primary_key=True),
)


class UserORM(Base, CreationDateMixin):
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

    baskets: Mapped[List["ProductBasketORM"]] = relationship(  # type: ignore
        "ProductBasketORM", back_populates="user"
    )
    natural_users: Mapped[List["NaturalUserORM"]] = relationship(  # type: ignore
        "NaturalUserORM", back_populates="user"
    )
    company_users: Mapped[List["CompanyUserORM"]] = relationship(  # type: ignore
        "CompanyUserORM", back_populates="user"
    )
    moderated_god_sends: Mapped[List["GodSendORM"]] = relationship(  # type: ignore
        "GodSendORM", back_populates="moderator"
    )
    order: Mapped[List["OrderORM"]] = relationship("OrderORM", back_populates="user")  # type: ignore

    donats: Mapped[List["DonatORM"]] = relationship("DonatORM", back_populates="user")  # type: ignore

    photos = relationship("PhotoORM", secondary=user_photos, back_populates="users")

    def get_schema(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            email=self.email,
            username=self.username,
            status=self.status,
            role=self.role,
            company=self.company,
            photos=self.photos,
        )
