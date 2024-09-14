from fastapi import APIRouter


router = APIRouter(prefix="/natural_user", tags=["natural_user"])


@router.get("/")
async def root():
    return {"message": "Hello World"}
