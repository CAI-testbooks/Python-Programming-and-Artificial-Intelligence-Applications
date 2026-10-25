import re

qq_number = "1234567"
pattern = r"[1-9][0-9]{4,10}"
results = re.fullmatch(pattern, qq_number)
if results is not None:
    print(results.group())
else:
    print("No match")
# 运行结果: 1234567

qq_number = "1234567 是我的 qq 号"
results = re.fullmatch(pattern, qq_number)
if results is not None:
    print(results.group())
else:
    print("No match")
# 运行结果: No match
# 因为 fullmatch() 函数要求整个字符串完全匹配正则表达式
