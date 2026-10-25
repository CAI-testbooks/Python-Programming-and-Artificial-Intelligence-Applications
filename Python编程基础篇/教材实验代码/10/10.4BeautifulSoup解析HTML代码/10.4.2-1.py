# 来源：书页 P267，PDF 279
from bs4 import BeautifulSoup     # 导入BeautifulSoup 库

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

# 获取节点的标签代码
print(f"head 节点的代码为:\n{soup.head}\n")      # 打印head 节点的标签代码
print(f"body 节点的代码为:\n{soup.body}\n")     # 打印body 节点的标签代码
print(f"title 节点的代码为:\n{soup.title}\n")  # 打印title 节点的标签代码
print(f"p 节点的代码为:\n{soup.p}\n")               # 打印p 节点的标签代码
