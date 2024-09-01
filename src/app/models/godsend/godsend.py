from datetime import datetime
from typing import Optional, List
from uuid import UUID

from sqlalchemy import Integer, String, Enum as SQLAEnum, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.models.mixin.mixin import CreationDateMixin, IsActiveMixin
from src.app.schemas.godsend.category import CategoryGodSend
from src.database.database_metadata import Base
from src.database.types import UUID_PK, str_256


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

    photos: Mapped[List["GodSendPhotoORM"]] = relationship(
        "GodSendPhotoORM", back_populates="god_send"
    )
    order: Mapped[List["OrderORM"]] = relationship(
        "OrderORM", back_populates="god_send"
    )
    moderator: Mapped["UserORM"] = relationship(
        "UserORM", back_populates="moderated_god_sends"
    )
