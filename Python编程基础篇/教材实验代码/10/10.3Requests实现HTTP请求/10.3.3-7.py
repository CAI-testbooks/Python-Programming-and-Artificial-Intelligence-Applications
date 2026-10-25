# 来源：书页 P259，PDF 271
import requests                       #
from requests.auth import HTTPBasicAuth # 导入HTTPBasicAuth 类

url = "https://ssr3.scrape.center/"   # 启用了HTTP 简单身份认证的网站

# 不做认证直接访问
resp = requests.get(url)
print(resp.status_code)    # 打印响应状态码

# 使用错误的用户名或密码访问
auth = HTTPBasicAuth("123", "456")
resp = requests.get(url, auth=auth)
print(resp.status_code)

# 使用正确的用户名和密码访问
auth = HTTPBasicAuth("admin", "admin")
resp = requests.get(url, auth=auth)
print(resp.status_code)
