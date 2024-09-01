from src.app.models.user.user import UserORM
from src.app.utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = UserORM
    user = UserORM
