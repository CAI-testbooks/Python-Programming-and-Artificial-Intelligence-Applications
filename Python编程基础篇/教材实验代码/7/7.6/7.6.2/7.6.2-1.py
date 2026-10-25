import json

# 读取json文件
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data["name"])
