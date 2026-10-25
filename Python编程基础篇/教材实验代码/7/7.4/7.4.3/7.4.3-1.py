with open("image.jpg", "rb") as f:
    f.seek(-10, 2)        # 从末尾向前10字节
    tail = f.read()
    print(tail)
