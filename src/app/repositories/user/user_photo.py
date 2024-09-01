from src.app.models.user.user_photo import UserPhotoORM
from src.app.utils.repository import SQLAlchemyRepository


class UserPhotoRepository(SQLAlchemyRepository):
    model = UserPhotoORM
    user = UserPhotoORM
