# 来源：书页 P250，PDF 262
import requests                                # 导入网络请求模块requests

url = "https://www.nuaa.edu.cn/"               # 目标URL 地址

response = requests.get(url)                   # 发送网络请求
print(response.status_code)                    # 打印响应状态码
