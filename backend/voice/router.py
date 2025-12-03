from fastapi import APIRouter
from .tts.xtts_v2 import text_to_speech
from .voice_mapper import map_voice

router = APIRouter(tags=["Voice"])

@router.post("/generate")
async def generate_voice(body: dict):
    text = body.get("text", "")
    avatar_type = body.get("avatar_type", "neutral")

    # Step 1: choose correct voice
    voice_id = map_voice(avatar_type)

    # Step 2: TTS generation
    audio_url = text_to_speech(text, voice_id)

    return {
        "status": "success",
        "voice_id": voice_id,
        "audio_url": audio_url
    }
