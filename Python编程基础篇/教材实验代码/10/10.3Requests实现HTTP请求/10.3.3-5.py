# 来源：书页 P255，PDF 267
import requests

url = "https://login2.scrape.center/"   # 目标URL 地址

# 发送网络请求
resp = requests.get(url)       # 不带Cookie 直接请求
resp.encoding = "utf-8"        # 对响应结果进行UTF-8 编码
print(resp.status_code)     # 打印响应状态码
print(resp.url)             # 打印响应URL
print(resp.text)            # 打印响应结果
