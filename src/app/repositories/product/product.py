from src.app.models.product.product_shop import ProductShopORM
from src.app.utils.repository import SQLAlchemyRepository


class ProductShopRepository(SQLAlchemyRepository):
    model = ProductShopORM
    user = ProductShopORM
