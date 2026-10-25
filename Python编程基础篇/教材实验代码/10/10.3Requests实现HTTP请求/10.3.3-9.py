# 来源：书页 P261，PDF 273
import requests      # 导入网络请求模块requests
from requests.exceptions import ReadTimeout, Timeout, RequestException # 导入异常类

url = "https://ssr4.scrape.center/"   # 该网站在收到请求后会延迟5s 再做出响应

try:
    resp = requests.get(url, timeout=2)
    print(resp.status_code)
except ReadTimeout as e:
    print(e)
except Timeout as e:
    print(e)
except RequestException as e:
    print(e)
