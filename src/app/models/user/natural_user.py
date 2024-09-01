from typing import Optional
from uuid import UUID

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.models.user.user import UserORM
from src.database.types import str_256


class NaturalUserORM(UserORM):
    __tablename__ = "natural_user"

    # Теперь добавлен внешний ключ, который ссылается на id родительского UserORM
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"), primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    address: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    card_number: Mapped[str_256]

    # Обратная связь
    user: Mapped[UserORM] = relationship("UserORM", back_populates="natural_users")
