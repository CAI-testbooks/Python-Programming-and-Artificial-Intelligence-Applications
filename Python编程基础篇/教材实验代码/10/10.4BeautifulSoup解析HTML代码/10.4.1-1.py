# 来源：书页 P265，PDF 277
from bs4 import BeautifulSoup  # 导入BeautifulSoup 库

# 要解析的HTML 代码
html_doc = """
<html>
<head>
<title> 一个HTML 页面</title>
</head>
<body>
<p>body 元素的内容会显示在浏览器中</p>
<p>title 元素的内容会显示在浏览器的标题栏中</p>
</body>
</html>
"""

# 创建一个BeautifulSoup 对象，传入HTML 代码并指定解析器
soup = BeautifulSoup(html_doc, features="lxml")

print(soup)                    # 打印解析的HTML 代码
print(type(soup))              # 打印数据类型
