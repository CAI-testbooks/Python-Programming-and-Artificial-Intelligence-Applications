name = "lisi"
age = 30

# 用 %s 进行字符串格式化输出
print("Name: %s, Age: %s" % (name, age))

# 用 .format() 方法格式化字符串
print("Name: {}, Age: {}".format("lisi", 20))
print("Name: {0}, Age: {1}".format("lisi", 20))  # 指定位置的字符串格式化
print("Name: {name}, Age: {age}".format(name="lisi", age=20)) # 使用关键字参数格式化

# 用 f-string 格式化字符串
print(f"Name: {name}, Age: {age}")
