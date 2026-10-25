# 来源：书页 P261，PDF 273
import requests      # 导入网络请求模块requests

url = "https://antispider5.scrape.center/"  # 目标URL 地址

for i in range(1, 101):
    resp = requests.get(url)
    if i % 20 != 0:
        print(resp.status_code, end=" ")
    else:
        print(resp.status_code)
