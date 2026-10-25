# 来源：书页 P282，PDF 294
from bs4 import BeautifulSoup    # 导入BeautifulSoup 库

# 要解析的HTML 代码
html_doc = """
<html>
<head>
    <title> 关联获取演示</title>
    <meta charset="utf-8"/>
</head>
<body>
    <div class="test_1 test_2" id="id_1">
        <p class="p-1 test_1" value="1"><a href="https://item.jd.com/
        <p class="p-2" value="1"><a> 人工智能
        <p class="p-3" value="3"><a href="https://item.jd.com/13790739.html">
        <p class="p-4" value="4"><a href="https://item.jd.com/14348480.html">
    </div>
    <div class="test_2" id="class_2">
        <p class="p-5"><a href="https://item.jd.com/14419018.html">
        <p class="p-6"><a href="https://item.jd.com/12627795.html">
        <p class="p-7"><a href="https://item.jd.com/13527222.html">
    </div>
    <div class="test_1 test_2">
    </div>
</body>
</html>
"""

# 创建一个BeautifulSoup 对象，传入HTML 代码并指定解析器
soup = BeautifulSoup(html_doc, features="lxml")

print(f' 所有p 标签:\n{soup.select("p")}')
print(f' 第二个p 标签:\n{soup.select("p")[1]}')
print(f' 嵌套访问html 下的head 下的title 节点:\n{soup.select("html head title")}')
print(f'class 包含test_2 的节点有:\n{soup.select(".test_2")}')
print(f'id 值为id_1 的节点是:\n{soup.select("#id_1")}')

print("=============================================================")
print(f'''嵌套访问第一个 class 值为“test_1 test_2”的 div 标签下的第一个 p 标签:\n{soup.select("div[class='test_1 test_2']")[0].select("p")[0]}''')
print(f' 第一个p 标签的value 属性( 方式1):\n{soup.select("p")[0]["value"]}')
print(f' 第一个p 标签的value 属性( 方式2):\n{soup.select("p")[0].attrs["value"]}')
print(f' 第一个p 标签下的文本节点( 方式1):\n{soup.select("p")[0].get_text()}')
print(f' 第一个p 标签下的文本节点( 方式2):\n{soup.select("p")[0].string}')
print(f' 从第二个p 标签开始的所有p 标签:\n{soup.select("p")[1:]}')
print(f' 所有class 值包含“p-1”或“p-5”的标签:\n{soup.select(".p-1, .p-5")}')
print(f' 所有class 值包含“test_1”的div 标签:\n{soup.select("div.test_1")}')
print(f' 所有具有href 属性的a 标签:\n{soup.select("a[href]")}')
