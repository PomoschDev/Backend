from curses.ascii import US
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from src.app.schemas.auth import UserCreate, Token, User 
from src.app.services.user import UserService
from src.app.utils.unitofwork import UnitOfWork

router = APIRouter(prefix="/auth", tags=["Authorisation"])


@router.post("/register", response_model=Token)
async def register_user(user_create: UserCreate, uow: UnitOfWork = Depends(UnitOfWork)):
    user_service = UserService(auth_repository=uow.auth)
    
    try:
        user = await user_service.create_user(
            email=user_create.email,
            username=user_create.username,
            password=user_create.password,
            phone=user_create.phone
        )
        token = "some_generated_token"
        return {"access_token": token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/users", response_model=list[User])
async def get_users(uow: UnitOfWork = Depends(UnitOfWork)):
    user_service = UserService(auth_repository=uow.auth)
    users = await user_service.get_users()
    return users 

@router.get("/user/{id}", response_model=User)  # Убедитесь, что response_model установлен
async def get_user(id: int, uow: UnitOfWork = Depends(UnitOfWork)):
    user_service = UserService(auth_repository=uow.auth)
    user = await user_service.find_user_by_id(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.post("/check-role", response_model=dict)
async def check_user_role(id: int, role: str, uow: UnitOfWork = Depends(UnitOfWork)):
    user_service = UserService(auth_repository=uow.auth)
    result = await user_service.check_user_role(id, role)
    return {"has_role": result}

@router.post("/compare-password", response_model=dict)
async def compare_password(id: int, password: str, uow: UnitOfWork = Depends(UnitOfWork)):
    user_service = UserService(auth_repository=uow.auth)
    result = await user_service.compare_user_password(id, password)
    return {"password_matches": result}

@router.get("/user-exists", response_model=dict)
async def user_exists(phone: str, uow: UnitOfWork = Depends(UnitOfWork)):
    user_service = UserService(auth_repository=uow.auth)
    exists = await user_service.user_exists(phone)
    return {"exists": exists}

@router.get("/find-by-email", response_model=User)
async def find_user_by_email(email: str, uow: UnitOfWork = Depends(UnitOfWork)):
    user_service = UserService(auth_repository=uow.auth)
    user = await user_service.find_user_by_email(email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.get("/find-by-phone", response_model=User)
async def find_user_by_phone(phone: str, uow: UnitOfWork = Depends(UnitOfWork)):
    user_service = UserService(auth_repository=uow.auth)
    user = await user_service.find_user_by_phone(phone)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

