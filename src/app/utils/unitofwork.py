from abc import ABC, abstractmethod
from typing import Type

from src.app.repositories.donat.donat import DonatRepository
from src.app.repositories.order.order_photo import OrderPhotoRepository
from src.database.database import database_accessor
from ..repositories.godsend.godsend import GodSendRepository
from ..repositories.godsend.godsend_photo import GodSendPhotoRepository
from ..repositories.order.order import OrderRepository
from ..repositories.product.product import ProductShopRepository
from ..repositories.product.product_basket import ProductBasketRepository
from ..repositories.product.product_photo import ProductPhotoRepository
from ..repositories.user.company_user import CompanyUserRepository
from ..repositories.user.natural_user import NaturalUserRepository
from ..repositories.user.user import UserRepository
from ..repositories.user.user_photo import UserPhotoRepository
from ...database.db_accessor import DatabaseAccessor


class IUnitOfWork(ABC):
    """Interface for Unit of Work pattern."""

    product_shop: Type[ProductShopRepository]
    user: Type[UserRepository]
    godsend: Type[GodSendRepository]
    godsend_photo: Type[GodSendPhotoRepository]
    order: Type[OrderRepository]
    product_basket: Type[ProductBasketRepository]
    product_photo: Type[ProductPhotoRepository]
    company_user: Type[CompanyUserRepository]
    natural_user: Type[NaturalUserRepository]
    user_photo: Type[UserPhotoRepository]
    order_photo: Type[OrderPhotoRepository]
    donat: Type[DonatRepository]

    @abstractmethod
    def __init__(self):
        """Initialize the Unit of Work instance."""

    @abstractmethod
    async def __aenter__(self):
        """Enter the context manager."""

    @abstractmethod
    async def __aexit__(self, *args):
        """Exit the context manager."""

    @abstractmethod
    async def commit(self):
        """Commit changes."""

    @abstractmethod
    async def rollback(self):
        """Rollback changes."""


class UnitOfWork:
    def __init__(self, database_accessor_p: None | DatabaseAccessor = None):
        if database_accessor_p is None:
            database_accessor_p = database_accessor
        self.session_fabric = database_accessor_p.get_async_session_maker()

    async def __aenter__(self):
        """Enter the context manager."""
        self.product_shop = ProductShopRepository(self.session)
        self.user = UserRepository(self.session)
        self.godsend = GodSendRepository(self.session)
        self.godsend_photo = GodSendPhotoRepository(self.session)
        self.order = OrderRepository(self.session)
        self.product_basket = ProductBasketRepository(self.session)
        self.product_photo = ProductPhotoRepository(self.session)
        self.company_user = CompanyUserRepository(self.session)
        self.natural_user = NaturalUserRepository(self.session)
        self.user_photo = UserPhotoRepository(self.session)
        self.order_photo = OrderPhotoRepository(self.session)
        self.donat = DonatRepository(self.session)

    async def __aexit__(self, *args) -> None:
        await self.rollback()
        await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
