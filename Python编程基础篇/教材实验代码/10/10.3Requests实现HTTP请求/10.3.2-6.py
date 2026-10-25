# 来源：书页 P243，PDF 255
import requests

params = {"school": "nuaa", "book": "python"}
# 发送网络请求
resp = requests.get("https://httpbin.org/get", params=params)
print(resp.text)             # 打印响应结果
