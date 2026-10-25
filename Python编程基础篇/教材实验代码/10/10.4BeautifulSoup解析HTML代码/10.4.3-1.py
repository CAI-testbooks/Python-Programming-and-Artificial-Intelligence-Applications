# 来源：书页 P277，PDF 289
from bs4 import BeautifulSoup    # 导入BeautifulSoup 库

# 要解析的HTML 代码
html_doc = """
<html>
<head>
    <title>find_all() 方法演示</title>
    <meta charset="utf-8"/>
</head>

<body>
<p class="p-1" value = "1"><a href="https://item.jd.com/10121830040484.html">
<p class="p-2" value = "2"><a href="https://item.jd.com/14419018.html">
<p class="p-3" value = "3"><a href="https://item.jd.com/12627795.html">
<div class="div-2" value = "4"><a href="https://item.jd.com/13527222.html">
</body>
</html>
"""

# 创建一个BeautifulSoup 对象，传入HTML 代码并指定解析器
soup = BeautifulSoup(html_doc, features="lxml")

print(soup.find_all(name="p"))          # 打印所有p 标签
print(type(soup.find_all(name="p")))    # 打印find_all() 返回的数据类型
