from typing import List, Optional

from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database_metadata import Base
from src.app.models.mixin.mixin import IsActiveMixin, CreationDateMixin


class ProductShopORM(Base, IsActiveMixin, CreationDateMixin):
    __tablename__ = "product_shop"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_name: Mapped[str] = mapped_column(
        String, nullable=False, default="ProductName"
    )
    price: Mapped[Optional[float]] = mapped_column(Float, nullable=True, default=None)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(
        String, nullable=True, default="Product Description"
    )
    quantity: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    creator_id: Mapped[int] = mapped_column(Integer, nullable=False)

    photos: Mapped[List["ProductPhotoORM"]] = relationship(
        "ProductPhotoORM", back_populates="product"
    )
