import re

qq_info = "QQ:1234567, QQ:7654321"
pattern = r"[1-9][0-9]{4,10}"

# re.sub：替换所有匹配内容，返回替换后的字符串
results = re.sub(pattern, "*****", qq_info)
print(results)
# 运行结果: QQ:*****, QQ:*****

# re.subn：替换，返回元组(新字符串, 替换次数)
results = re.subn(pattern, "*****", qq_info)
print(results)
# 运行结果: ('QQ:*****, QQ:*****', 2)

# 替换内容可以是lambda函数，动态处理每一个匹配对象
repl = lambda x: '*'.join(f'{c}' for c in x.group())
results = re.sub(pattern, repl, qq_info)
print(results)
# 运行结果: QQ:1*2*3*4*5*6*7, QQ:7*6*5*4*3*2*1
