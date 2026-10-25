import json

json_str = '{"name": "Alice", "age": 20}'
obj = json.loads(json_str)   # 字符串 → Python对象(字典)
print(obj["age"])

new_str = json.dumps(obj)    # Python对象(字典) → JSON字符串
print(new_str)
