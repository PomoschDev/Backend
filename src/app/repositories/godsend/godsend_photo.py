from src.app.models.godsend.godsend_photo import GodSendPhotoORM
from src.app.utils.repository import SQLAlchemyRepository


class GodSendPhotoRepository(SQLAlchemyRepository):
    model = GodSendPhotoORM
    godsend_photo = GodSendPhotoORM
