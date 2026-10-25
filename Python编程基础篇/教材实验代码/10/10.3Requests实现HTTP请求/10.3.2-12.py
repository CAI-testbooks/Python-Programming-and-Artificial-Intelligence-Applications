# 来源：书页 P247，PDF 259
import requests                    #

# 仅包含ASCII 字符的字符串可以直接发送
data_str_ascii = "Python"
# 发送网络请求
resp = requests.post("http://httpbin.org/post", data=data_str_ascii)
print(resp.json())                 # 打印解析后的Python 对象

# 含有非ASCII 字符（ 例如中文 ）的字符串必须要进行encode("utf-8") 操作
data_str_nascii = "Python 程序设计与交叉应用".encode("utf-8")
# 发送网络请求
resp = requests.post("http://httpbin.org/post", data=data_str_nascii)
print(resp.json())                 # 打印解析后的Python 对象
