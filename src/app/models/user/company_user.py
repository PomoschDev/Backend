from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.app.models.user.user import UserORM
from src.database.types import str_256


class CompanyUserORM(UserORM):
    __tablename__ = "company_user"

    __mapper_args__ = {
        "polymorphic_identity": "company_user",
        "inherit_condition": id == UserORM.id,
    }

    title: Mapped[str] = mapped_column(String, nullable=True)
    phone: Mapped[str] = mapped_column(String, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    site: Mapped[str] = mapped_column(String, nullable=True)
    inn: Mapped[str] = mapped_column(String, nullable=True)
    kpp: Mapped[str] = mapped_column(String, nullable=True)
    okpo: Mapped[str] = mapped_column(String, nullable=True)
    card_number: Mapped[str_256]
