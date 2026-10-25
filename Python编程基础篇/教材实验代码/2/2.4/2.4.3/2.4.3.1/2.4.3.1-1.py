# 反斜杠、单引号和双引号的转义
s1 = 'a\\b'                    # 使用 \ 来转义反斜杠
s2 = 'I\'m a Python developer.' # 使用 \ 来转义单引号
s3 = "He said, \"Python is awesome!\"" # 使用 \ 来转义双引号
print(s1)
print(s2)
print(s3)

# 换行符
s4 = 'Hello,\n world'
print(s4)

# 退格符
s5 = "Hello, Wo\b\bWorld"      # 退格两次，删除 "Wo"
print(s5)

# 制表符
s6 = "Name\tAge\tCity"         # 使用水平制表符
print(s6)
s7 = "zhang\vli"               # 使用垂直制表符
print(s7)

s8 = "Name\tAge\tCity\vzhang\t20\tbeijing\vli\t30\tshanghai"
print(s8)
