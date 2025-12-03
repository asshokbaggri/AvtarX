from fastapi import APIRouter, UploadFile, File
from .engine import generate_avatar

router = APIRouter()

@router.post("/create")
async def create_avatar(image: UploadFile = File(...), style_id: str = "model_1"):
    result = await generate_avatar(image, style_id)
    return result
