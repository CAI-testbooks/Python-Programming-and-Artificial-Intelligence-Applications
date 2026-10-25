import re

time_text = "现在是2024-10-26 21:15"
pattern = r'(?:\d{4})-(\d{2})-(\d{2}) (?:\d{2}:\d{2})'
match = re.search(pattern, time_text)
if match:
    print(match.groups())
    # 输出：('10', '26')
    print(f"{match.group(1)}月{match.group(2)}日")
    # 输出：10月26日
