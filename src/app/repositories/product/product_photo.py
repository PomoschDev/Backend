from src.app.models.product.product_photo import ProductPhotoORM
from src.app.utils.repository import SQLAlchemyRepository


class ProductPhotoRepository(SQLAlchemyRepository):
    model = ProductPhotoORM
    user = ProductPhotoORM
