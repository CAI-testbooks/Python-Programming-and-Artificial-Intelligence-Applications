# 来源：书页 P289，PDF 301
import requests

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/130.0.0.0 Safari/537.36"
)
headers = {
    "User-Agent": USER_AGENT
}
resp = requests.get("https://www.douban.com/", headers=headers)
print(resp.status_code)
print(resp.text)
