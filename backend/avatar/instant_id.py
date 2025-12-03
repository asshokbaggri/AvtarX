import cv2

def apply_instant_id(input_path):
    """
    REAL MODEL: Instant-ID pipeline
    - Load SD + InstantID plugin
    - Encode face identity
    - Return conditioned identity image

    CURRENT: Placeholder (copies image)
    """

    img = cv2.imread(input_path)
    out = input_path.replace("input", "id")
    cv2.imwrite(out, img)

    return out
