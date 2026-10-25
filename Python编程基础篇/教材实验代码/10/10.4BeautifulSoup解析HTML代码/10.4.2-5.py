# 来源：书页 P274，PDF 286
from bs4 import BeautifulSoup     # 导入BeautifulSoup 库
from bs4.element import Tag       # 导入bs 的标签类Tag

# 要解析的HTML 代码
html_doc = """
<html>
<head>
    <title> 演示代码标题</title>
    <meta charset="utf-8"/>
</head>
</html>
"""
# 创建一个BeautifulSoup 对象，传入HTML 代码并指定解析器
soup = BeautifulSoup(html_doc, features="lxml")
print(soup.title.parent)          # 打印title 节点的父节点内容
