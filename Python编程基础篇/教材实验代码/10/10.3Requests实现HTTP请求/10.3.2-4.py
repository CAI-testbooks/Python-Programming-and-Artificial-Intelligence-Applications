# 来源：书页 P241，PDF 253
import requests  # 导入网络请求模块requests

# 发送网络请求
resp = requests.get("https://www.baidu.com/img/bd_logo1.png")
print(resp.content)                        # 打印二进制数据
with open("baidu_logo.png", "wb") as f:    # 通过open 函数将二进制数据写入本地文件
    f.write(resp.content)                  # 写入
