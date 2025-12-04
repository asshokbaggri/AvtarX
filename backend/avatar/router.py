from fastapi import APIRouter, UploadFile, File, Form
from .engine import process_avatar

router = APIRouter(tags=["Avatar"])

@router.post("/create")
async def create_avatar(
    image: UploadFile = File(...),
    style_id: str = Form("model_1")
):
    return await process_avatar(image, style_id)
