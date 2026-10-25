# int() 转为整数
print(int("123"))         # 将字符串转为整数
print(int(2.99))          # 将浮点数转为整数(向下取整)

# 2. float() 转为浮点数
print(float("1.23"))      # 将字符串转为浮点数
print(float(1))           # 将整数转为浮点数

# 3. complex() 转为复数
print(complex(1.23,4.5))  # 两个参数：实部、虚部
print(complex(6))         # 一个参数：实部，虚部默认为0

# 4. str() 转为字符串
print(str(1.23))          # 将浮点数转为字符串
print(str(4))             # 将整数转为字符串
print(str(True))          # 将布尔值转为字符串

# bool() 转为布尔值
print(bool(1.23))         # 将浮点数转为布尔值
print(bool(4))            # 将整数转为布尔值
print(bool('python'))     # 将字符串转为布尔值
print(bool(0))            # 0对应的布尔值为False
print(bool(''))           # 空字符串对应的布尔值为False
