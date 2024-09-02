from src.app.models.donat.donat import DonatORM
from src.app.utils.repository import SQLAlchemyRepository


class DonatRepository(SQLAlchemyRepository):
    model = DonatORM
    donat = DonatORM
