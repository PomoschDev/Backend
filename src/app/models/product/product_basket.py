from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.app.models.user.user import UserORM
from src.database.database_metadata import Base


class ProductBasketORM(Base):
    __tablename__ = "product_basket"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    product_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("product_shop.id"), nullable=False
    )
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    product: Mapped["ProductShopORM"] = relationship(
        "ProductShopORM", back_populates="baskets"
    )

    user: Mapped[UserORM] = relationship("UserORM", back_populates="baskets")
