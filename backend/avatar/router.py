from fastapi import APIRouter, UploadFile, File, HTTPException
import requests
import uuid
import os

router = APIRouter(tags=["Avatar"])

RUNPOD_ENDPOINT = os.getenv("GPU_WORKER_URL")  # from Render ENV

@router.post("/create")
async def create_avatar(image: UploadFile = File(...)):
    try:
        # 1️⃣ Save uploaded image temporarily
        file_id = str(uuid.uuid4())
        temp_path = f"/tmp/{file_id}.jpg"

        with open(temp_path, "wb") as f:
            f.write(await image.read())

        # 2️⃣ Upload to RunPod Worker
        payload = {
            "input": {
                "file_path": temp_path
            }
        }

        response = requests.post(
            RUNPOD_ENDPOINT + "/run",
            json=payload,
            timeout=20
        )

        return response.json()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
