from src.app.models.product.product_basket import ProductBasketORM
from src.app.utils.repository import SQLAlchemyRepository


class ProductBasketRepository(SQLAlchemyRepository):
    model = ProductBasketORM
    user = ProductBasketORM
