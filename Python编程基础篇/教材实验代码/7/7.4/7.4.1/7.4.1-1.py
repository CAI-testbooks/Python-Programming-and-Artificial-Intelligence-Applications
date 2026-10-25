with open("sample.txt", "r", encoding="utf-8") as f:
    f.read(5)
    pos = f.tell()
    print("当前指针位置：", pos)
