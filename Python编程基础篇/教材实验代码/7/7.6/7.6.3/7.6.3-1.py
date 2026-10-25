import json

# 读取json文件
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data["name"])


# 修改字典中的age字段
data["age"] = 19
# 给courses列表追加元素"AI"
data["courses"].append("AI")

# 写回json文件，w模式会覆盖原有文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
