import re

qq_number = "1234567 是我的 qq 号 "
pattern = r"[1-9][0-9]{4,10}"
results = re.match(pattern, qq_number)
if results is not None:
    print(results.group())
else:
    print("No match")
# 运行结果: 1234567

qq_info = "QQ:1234567"
results = re.match(pattern, qq_info)
if results is not None:
    print(results.group())
else:
    print("No match")
# 运行结果: No match
# 因为 match() 是从字符串的开头开始匹配的，而 qq_info 字符串的开头是“QQ:”
