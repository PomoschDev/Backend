from fastapi import APIRouter


router = APIRouter(prefix="/user_photo", tags=["user_photo"])


@router.get("/")
async def root():
    return {"message": "Hello World"}
