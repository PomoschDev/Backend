from typing import List, Optional

from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.schemas.product.product_shop import ProductShopSchema
from src.database.database_metadata import Base
from src.app.models.mixin.mixin import IsActiveMixin, CreationDateMixin

product_photos = Table(
    "product_photos",
    Base.metadata,
    Column("product_id", ForeignKey("product_shop.id"), primary_key=True),
    Column("photo_id", ForeignKey("photo.id"), primary_key=True),
)


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

    photos = relationship(
        "PhotoORM", secondary=product_photos, back_populates="product_shop"
    )

    def get_schema(self) -> ProductShopSchema:
        return ProductShopSchema(
            id=self.id,
            product_name=self.product_name,
            price=self.price,
            title=self.title,
            description=self.description,
            quantity=self.quantity,
            creator_id=self.creator_id,
        )
