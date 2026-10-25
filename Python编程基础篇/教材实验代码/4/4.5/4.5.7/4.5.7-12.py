import re

time_text = "现在是2024-10-26 21:15"
pattern = r'(\d{4})-(\d{2})-(\d{2}) (\d{2}:\d{2})'
match = re.search(pattern, time_text)
if match:
    print(match.group())    # 等价 match.group(0)，完整匹配内容
    # 输出：2024-10-26 21:15
    print(f"{match.group(1)}年{match.group(2)}月{match.group(3)}日 {match.group(4)}")
    # 输出：2024年10月26日 21:15
