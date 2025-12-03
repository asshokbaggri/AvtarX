from fastapi import APIRouter
from .lipsync.sadtalker import generate_motion
from .lipsync.wav2lip import generate_lipsync
from .formatter import format_video
from .caption_gen import add_captions

import uuid

router = APIRouter(tags=["Video"])

@router.post("/generate")
async def generate_video(body: dict):
    avatar_url = body.get("avatar_url")
    audio_url = body.get("audio_url")
    captions = body.get("captions", True)

    job_id = str(uuid.uuid4())

    # STEP 1 — motion (SADTALKER)
    motion_path = generate_motion(avatar_url, audio_url)

    # STEP 2 — lipsync (Wav2Lip)
    synced_video = generate_lipsync(motion_path, audio_url)

    # STEP 3 — captions
    if captions:
        captioned_video = add_captions(synced_video)
    else:
        captioned_video = synced_video

    # STEP 4 — format to vertical 1080x1920
    final_video = format_video(captioned_video)

    return {
        "status": "success",
        "job_id": job_id,
        "video_url": final_video
    }
