from fastapi import APIRouter


router = APIRouter(prefix="/product_photo", tags=["product_photo"])


@router.get("/")
async def root():
    return {"message": "Hello World"}
