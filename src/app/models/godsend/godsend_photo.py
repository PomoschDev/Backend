from uuid import UUID

from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.database_metadata import Base


class GodsSendPhotoORM(Base):
    __tablename__ = "gods_send_photo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    gods_send_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("godsend.id"), nullable=False
    )
    photo_name: Mapped[String] = mapped_column(String, nullable=False)
    photo_url: Mapped[str] = mapped_column(String, nullable=False)

    user: Mapped["GodSendORM"] = relationship("GodSendORM", back_populates="photos")
