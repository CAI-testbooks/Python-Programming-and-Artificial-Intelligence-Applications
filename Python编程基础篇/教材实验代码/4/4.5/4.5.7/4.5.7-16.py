import re

text = "Alice is 30 and Bob is 25"
pattern = r"(?P<name>\w+) is (?P<age>\d+)"
matches = re.finditer(pattern, text)

for match in matches:
    print(f"{match.group('name')}:{match.group('age')};", end=" ")
# 输出：Alice:30; Bob:25;

print()
modified_text = re.sub(pattern, r"\g<name>", text)  # \g<name>引用命名分组name
print(modified_text)
# 输出：Alice and Bob
