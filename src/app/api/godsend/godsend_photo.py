from fastapi import APIRouter


router = APIRouter(prefix="/godsend_photo", tags=["godsend_photo"])


@router.get("/")
async def root():
    return {"message": "Hello World"}
