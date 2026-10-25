import re

# re.compile 预编译正则表达式，得到正则对象
pattern = re.compile(r"[1-9][0-9]{4,10}")
qq_info = "QQ:1234567, QQ:7654321"

# 预编译对象调用findall
results = pattern.findall(qq_info)
print(results)
# 运行结果: ['1234567', '7654321']

# 预编译对象调用sub，lambda动态替换
results = pattern.sub(lambda x: '*'.join(f'{c}' for c in x.group()), qq_info)
print(results)
# 运行结果: QQ:1*2*3*4*5*6*7, QQ:7*6*5*4*3*2*1

# 预编译对象调用split，用匹配到的QQ号作为分隔符切割字符串
results = pattern.split(qq_info)
print(results)
# 运行结果: ['QQ:', ', QQ:', '']
