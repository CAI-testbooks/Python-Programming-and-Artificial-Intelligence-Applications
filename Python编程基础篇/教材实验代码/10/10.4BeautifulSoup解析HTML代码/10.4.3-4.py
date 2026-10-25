# 来源：书页 P280，PDF 292
from bs4 import BeautifulSoup    # 导入BeautifulSoup 库
import re                        # 导入正则表达式模块

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
