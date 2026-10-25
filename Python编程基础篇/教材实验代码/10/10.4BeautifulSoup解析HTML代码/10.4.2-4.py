# 来源：书页 P273，PDF 285
from bs4 import BeautifulSoup     # 导入BeautifulSoup 库
from bs4.element import Tag       # 导入bs 的标签类Tag

# 要解析的HTML 代码
html_doc = """
<html>
<body>
<div id="test1">
    <div id="test2">
        <ul>
            <li class="test3" value = "user1234">
                此处为演示信息
            </li>
        </ul>
    </div>
</div>
</body>
</html>
"""

# 创建一个BeautifulSoup 对象，传入HTML 文件，指定lxml 解析器
soup = BeautifulSoup(html_doc, features="lxml")

# 获取可用于遍历所有子孙节点对象的迭代器
desc_iterator = soup.body.descendants

# 通过迭代器遍历body 节点下的所有子孙节点
for desc in desc_iterator:
    # 采用优化输出方法
    if isinstance(desc, Tag):     # 标签节点
        # 使用desc.prettify() 得到节点的结构并去除换行符和多余空格
        cleaned_str = ' '.join(desc.prettify().split())
        print(cleaned_str)
    elif desc.string and desc.string.strip():   # 文本节点且非空白
        cleaned_str = ' '.join(desc.string.split())
        print(cleaned_str)
