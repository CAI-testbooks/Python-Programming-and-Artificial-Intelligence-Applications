import re

qq_info = "QQ:1234567, QQ:7654321"
pattern = r"[1-9][0-9]{4,10}"
results = re.findall(pattern, qq_info)
if results is not None:
    print(results)
else:
    print("No match")
# 运行结果: ['1234567', '7654321']
