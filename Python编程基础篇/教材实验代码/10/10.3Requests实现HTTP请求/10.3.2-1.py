# 来源：书页 P238，PDF 250
import requests  # 导入网络请求模块 requests

# 发送网络请求
resp = requests.get("https://www.baidu.com")
print(f"响应状态码为：{resp.status_code}")       # 打印响应状态码
print(f"响应 URL 为：{resp.url}")                # 打印响应 URL
print(f"响应头为：{resp.headers}")               # 打印响应头信息
print(f"响应 Cookie 信息为：{resp.cookies}")     # 打印响应 Cookie 信息
