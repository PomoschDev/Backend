from fastapi import APIRouter

from src.app.repositories.user.user import UserRepository
from src.app.schemas.user.user import UserSchema


router = APIRouter(prefix="/user", tags=["user"])


@router.post("/")
async def create_user(user: UserSchema):
    user = await UserRepository.add_one(user)
    return user.get_schema()
