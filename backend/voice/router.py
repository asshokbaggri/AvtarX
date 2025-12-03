from fastapi import APIRouter

router = APIRouter()

@router.post("/generate")
def generate_voice():
    return {"audio_url": "voice-pending"}
