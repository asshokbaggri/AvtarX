def save_temp(image_bytes, path):
    with open(path, "wb") as f:
        f.write(image_bytes)
