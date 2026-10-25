# 来源：书页 P289，PDF 301
import requests

resp = requests.get("https://www.douban.com/")
print(resp.status_code)
print(resp.text)
