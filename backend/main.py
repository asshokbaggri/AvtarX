from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.router import router as auth_router
from avatar.router import router as avatar_router
from chat.router import router as chat_router
from voice.router import router as voice_router
from video.router import router as video_router

app = FastAPI(
    title="AvtarX Backend",
    version="1.0.0",
    description="AI Avatar + AI Chat + AI Voice + AI Video"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

@app.get("/")
def root():
    return {"status": "running", "service": "AvtarX API"}

# Register routers
app.include_router(auth_router, prefix="/auth")
app.include_router(avatar_router, prefix="/avatar")
app.include_router(chat_router, prefix="/chat")
app.include_router(voice_router, prefix="/voice")
app.include_router(video_router, prefix="/video")
