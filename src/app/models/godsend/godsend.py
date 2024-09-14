from datetime import datetime
from typing import Optional, List
from uuid import UUID

from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum as SQLAEnum,
    ForeignKey,
    Boolean,
    DateTime,
    Table,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.models.mixin.mixin import CreationDateMixin, IsActiveMixin
from src.app.schemas.godsend.category import CategoryGodSend
from src.app.schemas.godsend.godsend import GodSendSchema
from src.database.database_metadata import Base
from src.database.types import UUID_PK, str_256

godsend_photos = Table(
    "godsend_photos",
    Base.metadata,
    Column("godsend_id", ForeignKey("god_send.id"), primary_key=True),
    Column("photo_id", ForeignKey("photo.id"), primary_key=True),
)


class GodSendORM(Base, CreationDateMixin, IsActiveMixin):
    __tablename__ = "god_send"

    id: Mapped[UUID_PK]
    creator_id: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    passport: Mapped[str_256]
    card_number_gods: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    card_number: Mapped[str_256]
    country: Mapped[str] = mapped_column(String, nullable=False)
    city_id: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    phone: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[CategoryGodSend] = mapped_column(
        SQLAEnum(CategoryGodSend), nullable=False, default=CategoryGodSend.OtherCategory
    )
    moderator_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"), nullable=False)
    check: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    data_check: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    order: Mapped[List["OrderORM"]] = relationship(  # type: ignore
        "OrderORM", back_populates="god_send"
    )
    moderator: Mapped["UserORM"] = relationship(  # type: ignore
        "UserORM", back_populates="moderated_god_sends"
    )

    photos = relationship(
        "PhotoORM", secondary=godsend_photos, back_populates="god_send"
    )

    def get_schema(self):
        return GodSendSchema(
            id=self.id,
            name=self.name,
            passport=self.passport,
            card_number=self.card_number,
            country=self.country,
            city_id=self.city_id,
            address=self.address,
            phone=self.phone,
            email=self.email,
        )
