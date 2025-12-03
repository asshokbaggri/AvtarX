import cv2

def enhance_avatar(image_path):
    img = cv2.imread(image_path)

    # Sharpen
    blur = cv2.GaussianBlur(img, (0, 0), 3)
    sharpen = cv2.addWeighted(img, 1.6, blur, -0.6, 0)

    # Smooth skin
    smooth = cv2.bilateralFilter(sharpen, 15, 75, 75)

    out = image_path.replace("styled", "final")
    cv2.imwrite(out, smooth)
    return out
