# 来源：书页 P257，PDF 269
import requests     # 导入网络请求模块requests

session = requests.Session()   # 获取一个session 对象

url = "https://login2.scrape.center/login?next=/"
# 构造表单数据
data = {
    "username": "admin",
    "password": "admin",
}
resp = session.post(url, data=data) # 发送登录请求
print(resp.text)
print("===========================")

url = "https://login2.scrape.center/detail/1"
resp = session.get(url)  # 不指定cookies 参数，直接访问需要登录的资源
print(resp.text)
