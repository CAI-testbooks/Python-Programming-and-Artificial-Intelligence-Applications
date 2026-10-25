with open("note.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
    print("第一行：", line1)
    print("第二行：", line2)
