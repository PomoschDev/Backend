from fastapi import APIRouter


router = APIRouter(prefix="/product_basket", tags=["product_basket"])


@router.get("/")
async def root():
    return {"message": "Hello World"}
