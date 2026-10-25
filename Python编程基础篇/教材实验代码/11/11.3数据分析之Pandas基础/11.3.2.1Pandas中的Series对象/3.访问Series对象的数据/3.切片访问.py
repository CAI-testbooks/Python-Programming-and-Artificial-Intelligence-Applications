import pandas as pd

# 创建一个带标签索引的序列
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# 位置切片：从索引位置1到3(左闭右开)
print("位置切片：")
print(series[1:4])
# 输出：
# 位置切片：
# b    20
# c    30
# d    40
# dtype: int64

# 标签切片：从标签'b'到'e'(闭区间)
print("\n标签切片：")
print (series['b':'e'])
# 输出：
# 标签切片：
# b    20
# c    30
# d    40
# e    50
# dtype: int64
