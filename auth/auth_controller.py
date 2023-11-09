from fastapi import APIRouter

router = APIRouter()


@router.get("/auth", tags=["auth"])
async def test_auth():
    return {"message": "auth_test"}
