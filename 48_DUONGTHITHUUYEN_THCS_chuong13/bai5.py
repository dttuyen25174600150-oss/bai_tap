with open("nguon.bin", "rb") as src:
    with open("dich.bin", "wb") as dst:
        while True:
            chunk = src.read(1024)
            if not chunk:
                break
            dst.write(chunk)