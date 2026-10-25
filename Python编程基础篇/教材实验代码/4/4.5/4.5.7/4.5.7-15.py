import re

text = 'This is a test TEST. We ARE . are testing regular expressions.'
pattern = (r'\b(\w+)\b'          # 捕获完整单词到分组1
           r'(?:\s|,|\.)*'       # 非捕获组：中间分隔符（空格/逗号/点）任意次
           r'\1\b')              # 反向引用 \1，和分组1单词相同
results = re.sub(pattern, r'\1', text, flags=re.I)
print(results)
# 输出：This is a test. We ARE testing regular expressions.
