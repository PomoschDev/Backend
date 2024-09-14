from fastapi import APIRouter


router = APIRouter(prefix="/donat", tags=["donat"])


@router.get("/")
async def root():
    return {"message": "Hello World"}
