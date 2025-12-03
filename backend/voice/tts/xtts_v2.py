import uuid
from utils.storage import upload_file

def text_to_speech(text, voice_id):
    """
    REAL VERSION:
    - Load XTTS v2 model
    - Infer speech
    - Save WAV/MP3
    - Upload to R2

    Current: placeholder voice generation.
    """

    # TEMPORARY — Generate sample file
    file_path = f"/tmp/{uuid.uuid4()}.txt"
    with open(file_path, "w") as f:
        f.write(f"VOICE({voice_id}): {text}")

    key = f"voice/{uuid.uuid4()}.txt"
    audio_url = upload_file(file_path, key)

    return audio_url
