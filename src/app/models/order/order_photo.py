from src.database.database_metadata import Base
from sqlalchemy import Integer, String, DateTime, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class OrderPhotoORM(Base):
    __tablename__ = "order_photos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("order.id"), nullable=False)
    photo_url: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now
    )

    order: Mapped["OrderORM"] = relationship("OrderORM", back_populates="photos")
