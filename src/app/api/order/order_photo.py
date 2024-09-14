from fastapi import APIRouter


router = APIRouter(prefix="/order_photo", tags=["order_photo"])


@router.get("/")
async def root():
    return {"message": "Hello World"}
