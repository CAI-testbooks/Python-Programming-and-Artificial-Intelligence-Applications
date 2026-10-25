# 来源：书页 P271，PDF 283
from bs4 import BeautifulSoup  # 导入BeautifulSoup 库
from bs4.element import Tag    # 导入bs 的标签类Tag

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

# 获取包含直接子节点对象的列表
child_list = soup.head.contents
print(type(child_list))
print(child_list)
# 使用列表遍历head 下的所有子节点
for child in child_list:
    print(child)

# 获取可用于遍历直接子节点对象的迭代器
child_iterator = soup.head.children
print(type(child_iterator))
print(child_iterator)
# 使用迭代器遍历head 下的所有直接子节点
for child in child_iterator:
    print(child)
    if isinstance(child, Tag):                # 如果对象类型是标签
        # 使用child.prettify() 得到节点的结构并去除换行符和多余空格
        cleaned_str = ' '.join(child.prettify().split())
        print(cleaned_str)
    elif child.string and child.string.strip(): # 不是标签，那就是文本内容了
        cleaned_str = ' '.join(child.string.split())
        print(cleaned_str)
