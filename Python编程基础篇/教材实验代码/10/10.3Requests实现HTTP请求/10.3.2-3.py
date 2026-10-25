# 来源：书页 P240，PDF 252
import requests     # 导入网络请求模块requests

# 发送网络请求
resp = requests.get("https://httpbin.org/get")
resp_json = resp.json()       # 将JSOn 格式的响应数据解析为Python 对象
print(type(resp_json))        # 打印resp_json 的数据类型
print(resp_json)              # 打印resp_json 的内容

print()
print(type(resp_json["origin"]))    # 打印字典resp_json 的origin 字段的数据类型
print(resp_json["origin"])        # 打印字典resp_json 的origin 字段的内容
print(type(resp_json["headers"]))   # 打印字典resp_json 的headers 字段的数据类型
print(resp_json["headers"])       # 打印字典resp_json 的headers 字段的内容
