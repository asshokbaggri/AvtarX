from fastapi import APIRouter
from .engine import process_message

router = APIRouter(tags=["Chat"])

@router.post("/message")
async def chat_message(body: dict):
    user_text = body.get("message", "")
    user_id = body.get("user_id", "unknown")

    return await process_message(user_id, user_text)
