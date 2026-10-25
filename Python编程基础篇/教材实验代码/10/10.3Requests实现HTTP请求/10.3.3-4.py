# 来源：书页 P254，PDF 266
import requests      # 导入网络请求模块requests

url = "https://login2.scrape.center/"   # 目标URL 地址

# 构造Cookie 字典，其中键为cookie 名，值为cookie 值
cookies = {
    "sessionid": "sf37kk1r9001fztrqxogjva0bvdo7hkx",
}

# 发送网络请求
resp = requests.get(url, cookies=cookies) # 通过cookies 参数指定cookie
resp.encoding = "utf-8"                  # 对响应结果进行UTF-8 编码
print(resp.url)            # 打印响应URL
print(resp.text)           # 打印响应结果
