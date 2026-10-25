# 来源：书页 P247，PDF 259
import requests                    # 导入网络请求模块requests

bd = open("baidu_logo.png", "rb")  # 以二进制只读方式打开目标文件
files_data = {"logo": bd}          # 设置该文件的表单字段名为logo，字段值为该文件流
# 发送上传文件请求
resp = requests.post("http://httpbin.org/post", files=files_data)
print(resp.json())                 # 打印解析后的Python 对象
