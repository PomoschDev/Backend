from src.app.models.user.company_user import CompanyUserORM
from src.app.utils.repository import SQLAlchemyRepository


class CompanyUserRepository(SQLAlchemyRepository):
    model = CompanyUserORM
    user = CompanyUserORM
