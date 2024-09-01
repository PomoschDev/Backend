from src.app.models.user.natural_user import NaturalUserORM
from src.app.utils.repository import SQLAlchemyRepository


class NaturalUserRepository(SQLAlchemyRepository):
    model = NaturalUserORM
    user = NaturalUserORM
