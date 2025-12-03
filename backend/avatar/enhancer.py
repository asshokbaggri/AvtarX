import cv2

def enhance_image(image_path):
    img = cv2.imread(image_path)

    # Smooth + sharpen
    blur = cv2.GaussianBlur(img, (0, 0), 3)
    sharpen = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

    out = image_path.replace("styled", "final")
    cv2.imwrite(out, sharpen)
    return out
