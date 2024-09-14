from fastapi import APIRouter


router = APIRouter(prefix="/product", tags=["product"])


@router.get("/")
async def root():
    return {"message": "Hello World"}
