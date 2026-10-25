import re

# 中文字符的Unicode编码范围大致在\u4e00到\u9fff之间，这包括简体和繁体中文的所有字符
pattern = r'[^\w\u4e00-\u9fff]+'   # 匹配非中文字符和非单词字符
info = r"我 @#$ 会 ) ( 写 - */Python=\ 代 .` 码 "
results = re.split(pattern, info)
print(results)
# 运行结果: ['我', '会', '写', 'Python', '代', '码']
