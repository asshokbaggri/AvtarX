from fastapi import APIRouter

router = APIRouter()

@router.post("/create")
def create_avatar():
    return {"status": "avatar-engine-pending"}
