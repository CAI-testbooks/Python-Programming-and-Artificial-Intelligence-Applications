"""10.2.4 在 HTML 页面中直接嵌入 JavaScript

教材中的非 Python 代码片段以字符串保存；运行本文件可输出原片段。
"""

snippet = '<!DOCTYPE html>\n<html>\n    <head>\n        <meta charset="utf-8">\n        <title>在HTML页面中直接嵌入JavaScript代码</title>\n    </head>\n    <body>\n        <script type="text/javascript">\n            alert(\'在HTML页面中直接嵌入JavaScript代码\');\n        </script>\n    </body>\n</html>'

print(snippet)
