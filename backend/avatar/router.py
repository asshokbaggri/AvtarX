from fastapi import APIRouter, UploadFile

router = APIRouter()

@router.post("/avatar")
async def create_avatar(file: UploadFile):
    return {"status": "avatar_disabled"}
