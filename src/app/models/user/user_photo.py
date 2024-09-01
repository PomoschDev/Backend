from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from src.app.models.user.user import UserORM
from src.database.database_metadata import Base


class UserPhotoORM(Base):
    __tablename__ = "user_photo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("user.id"), nullable=False)
    photo_name: Mapped[String] = mapped_column(String, nullable=False)
    photo_url: Mapped[str] = mapped_column(String, nullable=False)

    user: Mapped["UserORM"] = relationship("UserORM", back_populates="photos")
