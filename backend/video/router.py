from fastapi import APIRouter

router = APIRouter()

@router.post("/generate")
def generate_video():
    return {"video_url": "video-pending"}
