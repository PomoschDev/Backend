from src.app.models.order.order_photo import OrderPhotoORM
from src.app.utils.repository import SQLAlchemyRepository


class OrderPhotoRepository(SQLAlchemyRepository):
    model = OrderPhotoORM
    order = OrderPhotoORM
