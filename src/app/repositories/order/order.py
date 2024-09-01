from src.app.models.order.order import OrderORM
from src.app.utils.repository import SQLAlchemyRepository


class OrderRepository(SQLAlchemyRepository):
    model = OrderORM
    godsend = OrderORM
