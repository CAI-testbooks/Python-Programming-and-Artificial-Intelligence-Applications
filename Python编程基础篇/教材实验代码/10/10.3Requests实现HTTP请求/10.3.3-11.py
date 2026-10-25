# 来源：书页 P262，PDF 274
import requests     # 导入网络请求模块

# 设置代理服务
proxies = {
    "http": "http://60.210.128.203:9000",
    "https": "https://60.210.128.203:9000",
}

try:
    # 发送GET 请求（ 其中proxies 参数用于指定代理服务，verify=False表示关闭SSL 证书验证 ）
    resp = requests.get("https://antispider5.scrape.center/", proxies=proxies,
                        verify=False, timeout=30)
    print(resp.status_code)    # 打印响应状态码
except Exception as e:
    print(e)                   # 打印异常信息
