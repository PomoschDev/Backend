from typing import Optional
from uuid import UUID

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.models.user.user import UserORM
from src.database.types import str_256


class CompanyUserORM(UserORM):
    __tablename__ = "company_user"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"), primary_key=True)
    title: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    address: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    site: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    inn: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    kpp: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    okpo: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    card_number: Mapped[str_256]

    user: Mapped[UserORM] = relationship("UserORM", back_populates="company_users")
