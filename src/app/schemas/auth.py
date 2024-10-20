from src.app.schemas.types import UserBase, UserRole, Password, ID
from pydantic import BaseModel, UUID4
import uuid
from typing import Optional
from datetime import datetime, timedelta


class UserCreate(BaseModel):
    email: str  
    username: str    
    password: str    
    phone: str      

    class Config:
        json_schema_extra = {
            "example": {
                "email": "example@example.com",
                "username": "example_user",
                "password": "example_password",
                "phone": "1234567890",
            }
        }


class UserUpdate(UserBase):
    password: Optional[Password] = None


class User(UserBase):
    id: int
    password: str = None

    class Config:
        from_attributes = True


class RefreshSessionCreate(BaseModel):
    refresh_token: UUID4 
    expires_in: int
    id: UUID4 

    class Config:
        json_schema_extra = {
            "example": {
                "refresh_token": str(uuid.uuid4()),
                "expires_in": 3600,
                "id": str(uuid.uuid4()),
            }
        }


class Token(BaseModel):
    access_token: str
    refresh_token: UUID4
    token_type: str


class AuthTokenORMSchema(RefreshSessionCreate):
    id: ID
    created_at: datetime

    class Config:
        json_schema_extra = {
            "example": {
                "refresh_token": str(uuid.uuid4()),
                "expires_in": 3600,
                "id": str(uuid.uuid4()),
                "id": str(uuid.uuid4()),
                "created_at": "2023-05-17T00:00:00Z",
            }
        }


class PaginateSchema(BaseModel):
    offset: int = 0
    limit: int = 100


class UsersListFilter(BaseModel):
    role: Optional[UserRole] = None
    clinic_id: Optional[int] = None
    is_active: Optional[bool] = None


class UsersFindRequest(BaseModel):
    paginate: Optional[PaginateSchema] = None
    filters: Optional[UsersListFilter] = None


class UserCreateDB(UserBase):
    hashed_password: Optional[str] = None


class DependentToken(BaseModel):
    token: str
    id: ID
    role: UserRole
    is_active: bool


class TokenAccessRefreshCreate(BaseModel):
    access_token: str
    refresh_token_expires: timedelta
    refresh_token: uuid.UUID