from fastapi import APIRouter
from src.app.api.donat import donat
from src.app.api.godsend import godsend, godsend_photo
from src.app.api.order import order, order_photo
from src.app.api.product import product, product_basket, product_photo
from src.app.api.user import company_user, natural_user, user, user_photo
from src.app_config.config_api import settings

router = APIRouter(prefix=settings.APP_PREFIX)

router.include_router(user.router)
router.include_router(user_photo.router)
router.include_router(company_user.router)
router.include_router(natural_user.router)
router.include_router(donat.router)
router.include_router(godsend.router)
router.include_router(godsend_photo.router)
router.include_router(order.router)
router.include_router(order_photo.router)
router.include_router(product.router)
router.include_router(product_basket.router)
router.include_router(product_photo.router)
