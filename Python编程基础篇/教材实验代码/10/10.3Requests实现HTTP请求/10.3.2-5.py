# 来源：书页 P242，PDF 254
import requests    # 导入网络请求模块requests

# 发送网络请求
resp = requests.get("https://httpbin.org/get?school=nuaa&book=python")
print(resp.text)             # 打印响应结果
