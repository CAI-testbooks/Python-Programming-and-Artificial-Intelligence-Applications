name = 'Alice'
age = 22

# 方式1：% 格式化（旧写法）
str5 = 'My name is %s, and I am %d years old.' % (name, age)
print(str5)
# 运行结果: My name is Alice, and I am 22 years old.

# 方式2：.format() 格式化
str6 = 'My name is {}, and I am {} years old.'.format(name, age)
print(str6)
# 运行结果: My name is Alice, and I am 22 years old.

# 方式3：f-string（Python3.6+ 推荐，最简单）
str7 = f'My name is {name}, and I am {age} years old.'
print(str7)
# 运行结果: My name is Alice, and I am 22 years old.
