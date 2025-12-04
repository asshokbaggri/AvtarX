import tempfile
import uuid
from utils.storage import upload_file
from .instant_id import apply_instant_id
from .ip_adapter import apply_ip_style
from .enhancer import enhance_avatar

async def process_avatar(image_file, style_id):
    # Save input image
    temp_dir = tempfile.mkdtemp()
    input_path = f"{temp_dir}/input.jpg"

    with open(input_path, "wb") as f:
        f.write(await image_file.read())

    # STEP 1 — Instant-ID (Identity Extraction)
    id_output = apply_instant_id(input_path)

    # STEP 2 — Style Apply (IP-Adapter)
    styled_output = apply_ip_style(id_output, style_id)

    # STEP 3 — Enhancement (Glow, Sharpness)
    final_output = enhance_avatar(styled_output)

    # STEP 4 — Upload CDN (Cloudflare R2)
    file_key = f"avatars/{uuid.uuid4()}.png"
    uploaded_url = upload_file(final_output, file_key)

    return {
        "status": "success",
        "avatar_url": uploaded_url,
        "style_id": style_id
    }
