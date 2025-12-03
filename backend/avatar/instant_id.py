import cv2
import numpy as np

def apply_instant_id(input_path):
    # Placeholder until you load actual model
    # Later → load Instant-ID weights

    image = cv2.imread(input_path)

    # Return same image for now
    # (Model integration will replace this)
    out_path = input_path.replace("input", "instant_id")

    cv2.imwrite(out_path, image)
    return out_path
