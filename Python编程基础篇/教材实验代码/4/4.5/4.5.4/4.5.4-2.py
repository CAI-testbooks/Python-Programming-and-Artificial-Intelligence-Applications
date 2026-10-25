table = str.maketrans('aeiou', '12345')
context = 'I love Python, Python is my favorite language.'
print(context.translate(table))
# I l4v2 Pyth4n, Pyth4n 3s my f1v4r3t2 l1ng51g2.

# 第三个参数：指定要直接删除的字符（空格、逗号、句号）
table = str.maketrans('aeiou', '12345', ' ,.')
print(context.translate(table))
# Il4v2Pyth4nPyth4n3smyf1v4r3t2l1ng51g2
