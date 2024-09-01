from src.app.models.godsend.godsend import GodSendORM
from src.app.utils.repository import SQLAlchemyRepository


class GodSendRepository(SQLAlchemyRepository):
    model = GodSendORM
    godsend = GodSendORM
