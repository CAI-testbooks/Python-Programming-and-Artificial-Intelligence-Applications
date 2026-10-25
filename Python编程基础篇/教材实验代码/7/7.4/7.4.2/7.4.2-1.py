with open("sample.txt", "r", encoding="utf-8") as f:
    f.seek(8)
    data = f.read(5)
    print(data)
