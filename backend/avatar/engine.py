import uuid
import tempfile
from .instant_id import apply_instant_id
from .ip_adapter import apply_style
from .enhancer import enhance_image
from utils.storage import upload_file

async def generate_avatar(image_file, style_id="model_1"):
    # Save uploaded image
    temp_dir = tempfile.mkdtemp()
    input_path = f"{temp_dir}/input.jpg"

    with open(input_path, "wb") as f:
        f.write(await image_file.read())

    # Step 1 — FACE ID (Instant-ID)
    id_output = apply_instant_id(input_path)

    # Step 2 — Apply Style (IP-Adapter)
    styled_output = apply_style(id_output, style_id)

    # Step 3 — Enhancement (Face Cleanup, Glow)
    final_avatar = enhance_image(styled_output)

    # Step 4 — Upload final avatar
    file_key = f"avatars/{uuid.uuid4()}.png"
    uploaded_url = upload_file(final_avatar, file_key)

    return {
        "status": "success",
        "style_id": style_id,
        "avatar_url": uploaded_url
    }
