from fastapi import APIRouter


router = APIRouter(prefix="/company_user", tags=["company_user"])


@router.get("/")
async def root():
    return {"message": "Hello World"}
