# 来源：书页 P275，PDF 287
from bs4 import BeautifulSoup  # 导入 BeautifulSoup 库

# 要解析的 HTML 代码
html_doc = """
<html>
<head>
    <title>演示代码标题</title>
    <meta charset="utf-8"/>
</head>
<body>
<p class="p-1" value="1"><a href="https://item.jd.com/12353915.html">零基础学Python</a></p>
第一个p节点下文本
<div class="div-1" value="2"><a href="https://item.jd.com/12451724.html">Python从入门到项目实践</a></div>
<p class="p-3" value="3"><a href="https://item.jd.com/12512461.html">Python项目开发案例集锦</a></p>
<div class="div-2" value="4"><a href="https://item.jd.com/12550531.html">Python编程锦囊</a></div>
</body>
</html>
"""

# 创建一个 BeautifulSoup 对象，传入 HTML 代码并指定解析器
soup = BeautifulSoup(html_doc, features="lxml")

print(soup.p.next_sibling)                  # 打印第一个 p 节点的下一个兄弟节点（文本内容）
div = soup.p.next_sibling.next_sibling      # 获取文本内容的下一个节点，也就是同级的第一个 div 节点
print(div)                                  # 打印该 div 节点的标签代码
print(div.previous_sibling)                 # 打印第一个 div 节点的上一个兄弟节点（文本内容）

print(f"第一个p节点之前的所有兄弟节点如下:\n{list(soup.p.previous_siblings)}\n")
print(f"第一个p节点之后的所有兄弟节点如下:\n{list(soup.p.next_siblings)}\n")
