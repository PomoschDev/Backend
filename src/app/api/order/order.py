from fastapi import APIRouter


router = APIRouter(prefix="/order", tags=["order"])


@router.get("/")
async def root():
    return {"message": "Hello World"}
