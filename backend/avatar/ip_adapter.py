import cv2
import numpy as np

STYLE_MAP = {
    "model_1": (30, 0, 40),
    "model_2": (0, 40, 20),
    "beauty_glow": (15, 10, 50),
    "rich_tone": (20, 20, 20)
}

def apply_ip_style(image_path, style_id):
    img = cv2.imread(image_path)

    tint = STYLE_MAP.get(style_id, (0, 0, 0))
    r, g, b = tint

    # TEMP STYLE EFFECT
    styled = cv2.add(img, (r, g, b))

    out = image_path.replace("id", "styled")
    cv2.imwrite(out, styled)
    return out
