import re

html_code = r"<div>Hello, world!</div><div>Welcome to my blog.</div>"
results = re.findall(r"<div>.*</div>", html_code)
print(results)
# 运行结果: ['<div>Hello, world!</div><div>Welcome to my blog.</div>']
