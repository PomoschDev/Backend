from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from src.app.schemas.photo.photo import PhotoSchema
from src.database.database_metadata import Base
from src.app.models.mixin.mixin import CreationDateMixin


class PhotoORM(Base, CreationDateMixin):
    __tablename__ = "photo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)

    def get_schema(self):
        return PhotoSchema(
            id=self.id,
            name=self.name,
            url=self.url,
        )
