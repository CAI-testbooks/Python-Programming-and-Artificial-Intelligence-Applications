# 来源：书页 P245，PDF 257
import requests   # 导入网络请求模块requests

# 字典类型的数据对象
dict_data = {
    ' 校训': ' 智周万物、道济天下',
    ' 校风': ' 团结、俭朴、唯实、创新',
}
# 发送网络请求
resp = requests.post("http://httpbin.org/post", json=dict_data)
print(resp.json())  # 打印解析后的Python 对象
