def temp_save(path, bytes_data):
    with open(path, "wb") as f:
        f.write(bytes_data)
