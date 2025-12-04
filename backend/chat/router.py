# router.py

from fastapi import APIRouter
from pydantic import BaseModel
from .engine import process_chat

router = APIRouter(tags=["ChatGPT5"])

class ChatRequest(BaseModel):
    message: str
    history: list = []

@router.post("/chat")
async def chat_api(req: ChatRequest):
    result = await process_chat(req.message, req.history)
    return result

# test deployed
