# 来源：书页 P239，PDF 251
import requests  # 导入网络请求模块requests

# 发送网络请求
resp = requests.get("https://www.baidu.com/")
resp.encoding = "utf-8"         # 对响应结果进行UTF-8 编码
print(resp.text)                # 以文本形式打印网页源码
