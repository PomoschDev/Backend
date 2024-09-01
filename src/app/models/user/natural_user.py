from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.app.models.user.user import UserORM
from src.database.types import str_256


class NaturalUserORM(UserORM):
    __tablename__ = "natural_user"

    __mapper_args__ = {
        "polymorphic_identity": "natural_user",
        "inherit_condition": id == UserORM.id,
    }

    name: Mapped[str] = mapped_column(String, nullable=True)
    phone: Mapped[str] = mapped_column(String, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    card_number: Mapped[str_256]
