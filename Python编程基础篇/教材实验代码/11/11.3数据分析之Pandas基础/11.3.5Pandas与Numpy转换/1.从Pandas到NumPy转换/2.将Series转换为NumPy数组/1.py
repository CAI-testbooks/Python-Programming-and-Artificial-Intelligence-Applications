import pandas as pd

# 创建一个示例Series
s = pd.Series([1, 2, 3, 4, 5])

# 使用.values属性将Series转换为NumPy数组
array = s.values

# 打印转换后的NumPy数组
print(array)
# 输出：
# [1 2 3 4 5]

# 使用to_numpy()方法将Series转换为NumPy数组，并指定数据类型为float32
array = s.to_numpy(dtype='float32')

# 打印转换后的NumPy数组及其数据类型
print(array)
# 输出：
# [1. 2. 3. 4. 5.]

print(array.dtype)
# 输出：
# float32
