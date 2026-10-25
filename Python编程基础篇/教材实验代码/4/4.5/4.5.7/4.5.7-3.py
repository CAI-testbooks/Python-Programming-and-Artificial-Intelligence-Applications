import re

qq_number = "1234567"
pattern = r"[1-9][0-9]{4,10}"
results = re.search(pattern, qq_number)
if results is not None:
    print(results.group())
else:
    print("No match")
# 运行结果: 1234567

qq_info = "QQ:1234567"
results = re.search(pattern, qq_info)
if results is not None:
    print(results.group())
else:
    print("No match")
# 运行结果: 1234567
