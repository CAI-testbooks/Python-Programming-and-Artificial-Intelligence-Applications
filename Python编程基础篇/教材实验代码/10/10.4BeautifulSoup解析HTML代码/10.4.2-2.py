# 来源：书页 P268，PDF 280
from bs4 import BeautifulSoup     # 导入BeautifulSoup 库

# 要解析的HTML 代码
html_doc = """
<html>
<head>
    <title> 横排响应式登录</title>
    <meta http-equiv="Content-Type" content="text/html" charset="utf-8"/>
    <meta name="viewport" content="width=device-width"/>
    <link href="font/css/bootstrap.min.css" type="text/css" rel="stylesheet">
    <link href="css/style.css" type="text/css" rel="stylesheet">
</head>
<body>
    <h3> 登录</h3>
    <div class="glyphicon glyphicon-envelope"><input type="text" placeholder=
    <div class="glyphicon glyphicon-lock"><input type="password" placeholder=
</body>

"""

# 创建一个BeautifulSoup 对象，传入HTML 代码并指定解析器
soup = BeautifulSoup(html_doc, features="lxml")

# 获取节点的所有标签属性
print(f"meta 节点的属性有: {soup.meta.attrs}")
print(f"link 节点的属性有: {soup.link.attrs}")
print(f"div 节点的属性有: {soup.div.attrs}")
