lines = ["第一行\n", "第二行\n", "第三行\n"]
with open("multi.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
