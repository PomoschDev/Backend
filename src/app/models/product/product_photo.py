from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.models.mixin.mixin import CreationDateMixin


class ProductPhotoORM(CreationDateMixin):
    __tablename__ = "product_photos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("product_shop.id"), nullable=False
    )
    photo_name: Mapped[str] = mapped_column(String, nullable=False)
    photo_link: Mapped[str] = mapped_column(String, nullable=False)

    product: Mapped["ProductShopORM"] = relationship(
        "ProductShopORM", back_populates="photos"
    )
