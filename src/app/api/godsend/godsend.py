from fastapi import APIRouter


router = APIRouter(prefix="/godsend", tags=["godsend"])


@router.get("/")
async def root():
    return {"message": "Hello World"}
