from sqlalchemy import Integer, ForeignKey, String, UUID
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.database_metadata import Base


class GodSendPhotoORM(Base):
    __tablename__ = "god_send_photo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    gods_send_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("god_send.id"), nullable=False
    )
    photo_name: Mapped[String] = mapped_column(String, nullable=False)
    photo_url: Mapped[str] = mapped_column(String, nullable=False)

    god_send: Mapped["GodSendORM"] = relationship("GodSendORM", back_populates="photos")
