import json

try:
    # JSON末尾多了逗号，属于非法JSON格式
    json.loads('{"name": "Tom", }')
except json.JSONDecodeError as e:
    print("解析错误：", e)
