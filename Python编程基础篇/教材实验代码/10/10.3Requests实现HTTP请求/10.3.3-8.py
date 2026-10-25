# 来源：书页 P259，PDF 271
import requests      # 导入网络请求模块requests

url = "https://ssr4.scrape.center/"   # 该网站在收到请求后会延迟5s 再做出响应

try:
    resp = requests.get(url, timeout=2)
    print(resp.status_code)
except Exception as e:
    print(type(e))
    print(e)

try:
    resp = requests.get(url, timeout=10)
    print(resp.status_code)
except Exception as e:
    print(type(e))
    print(e)
