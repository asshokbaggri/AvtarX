import cv2

def apply_style(image_path, style_id="model_1"):
    # Later: add real IP-Adapter inference
    image = cv2.imread(image_path)

    # Temporary: add color tint based on style
    if style_id == "model_1":
        tint = (20, 0, 40)
    else:
        tint = (0, 40, 20)

    styled = cv2.add(image, tint)

    out = image_path.replace("instant_id", "styled")
    cv2.imwrite(out, styled)
    return out
