# 来源：书页 P266，PDF 278
from bs4 import BeautifulSoup   # 导入BeautifulSoup 库

# 创建一个BeautifulSoup 对象，传入HTML 文件对象并指定解析器
soup = BeautifulSoup(open("html_doc.html", encoding="utf-8"), features="lxml")
print(soup.prettify())   # 打印格式化的HTML 代码
