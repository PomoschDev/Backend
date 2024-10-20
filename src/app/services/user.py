from typing import Optional

from fastapi import HTTPException, status, Request, Response

import uuid

from sqlalchemy.exc import IntegrityError

from src.app.utils.unitofwork import IUnitOfWork, UnitOfWork
from src.app.schemas.auth import (
    UserCreate,
    UserCreateDB,
    User,
    Token,
    RefreshSessionCreate,
    AuthTokenORMSchema,
    UserUpdate,
    UserRole,
    UsersFindRequest,
)
from src.app.utils.static.auth_crypto import (
    TokenUtils,
    PasswordStatic,
    CookieUtils,
)
from src.app.repositories.exceptions import (
    InvalidCredentialsException,
    UserNotActiveException,
    InvalidTokenException,
    TokenExpiredException,
    UserPrivilegesException,
    UserNotFoundException,
    UnavailableLoginException,
    InvalidClinicID,
)
from src.app.schemas.auth import TokenAccessRefreshCreate
from src.app.repositories.metauser.auth_user import AuthRepository

class UserService:
    def __init__(self, auth_repository: AuthRepository):
        self.auth_repository = auth_repository

    async def create_user(self, email: str, username: str, password: str, phone: str):
        return await self.auth_repository.create_user(email, username, password, phone)

    async def get_users(self):
        return await self.auth_repository.users()  # Получите пользователей из репозитория

    async def check_user_role(self, id: str, role: str):
        return await self.auth_repository.is_role(id, role)

    async def compare_user_password(self, id: str, password: str):
        return await self.auth_repository.compare_password(id, password)

    async def user_exists(self, phone: str):
        return await self.auth_repository.user_exists(phone)

    async def find_user_by_id(self, id: int):
        user_data = await self.auth_repository.find_user_by_id(id)
        if user_data:
            return User(**user_data)  # Убедитесь, что вы возвращаете объект User
        return None  # Если пользователь не найден, возвращаем None

    async def find_user_by_email(self, email: str):
        return await self.auth_repository.find_user_by_email(email)

    async def find_user_by_phone(self, phone: str):
        return await self.auth_repository.find_user_by_phone(phone)
