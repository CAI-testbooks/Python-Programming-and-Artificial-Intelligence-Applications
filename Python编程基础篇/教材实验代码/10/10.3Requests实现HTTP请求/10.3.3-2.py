# 来源：书页 P250，PDF 262
import requests                                # 导入网络请求模块requests

url = "https://www.nuaa.edu.cn/"               # 目标URL 地址

# 把较长的字符串常量分行定义
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/130.0.0.0 Safari/537.36"
)
# 指定自定义请求头的字典
headers = {
    "User-Agent": USER_AGENT
}
response = requests.get(url, headers=headers)  # 发送网络请求
print(response.status_code)                    # 打印响应状态码
