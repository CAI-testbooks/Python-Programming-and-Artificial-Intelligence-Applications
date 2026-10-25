# 来源：书页 P248，PDF 260
import requests                       # 导入网络请求模块requests

dict_data = {"action": "upload_logo"} # 字典类型的数据对象
bd = open("baidu_logo.png", "rb")     # 以二进制只读方式打开目标文件
files_data = {"logo": bd}             # 设置该文件的表单字段名为logo，字段值为该文件流
# 同时指定data 和files 参数
resp = requests.post("http://httpbin.org/post", data=dict_data, files=files_data)
print(resp.json())                    # 打印解析后的Python 对象
