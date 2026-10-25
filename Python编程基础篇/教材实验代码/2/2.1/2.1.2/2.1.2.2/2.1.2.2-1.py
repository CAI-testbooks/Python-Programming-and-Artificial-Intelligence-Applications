# 无参数序号隐式顺序
print('{}, {}'.format('Hello', 'world'))

# 显式设置参数序号
print('{1}, {0}'.format('world', 'Hello'))

# 设置对齐方式，其中的10表示最小宽度为10（此处为了更加直观地显示输出，用单引号将输出内容括起来了）
print('{:<10}'.format('hi'))        # 左对齐
print('{:>10}'.format('hi'))        # 右对齐
print('{:^10}'.format('hi'))        # 居中对齐
print('{:*=+8d}'.format(5))         # 将 * 填充到符号与数字之间

# 设置填充字符
print('{:_>10}'.format('hi'))          # 用下划线填充，右对齐
print('{:0<10}'.format('hi'))          # 用0填充，右对齐

# 设置数字符号
print('{:+d}, {:+d}'.format(5, -5)) # 显示正负符号
print('{:-d}, {:-d}'.format(5, -5))    # 仅显示负号
print('{: d}, {: d}'.format(5, -5))    # 正数加空格，负数显示负号

# 显示数字前缀
print('{:#o}'.format(10))              # 八进制
print('{:#x}'.format(10))              # 十六进制
print('{:#X}'.format(10))              # 十六进制(大写)

# 设置最小宽度(此处为了更加直观地显示输出，用单引号将输出内容括起来了)
print('{:10}'.format('test'))

# 设置数字的千位分隔符(逗号)
print('{:,}'.format(1000000))

# 设置精度
print('{:.2f}'.format(3.1459))         # 保留两位小数
