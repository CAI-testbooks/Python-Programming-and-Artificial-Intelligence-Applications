import pandas as pd

# 创建带标签索引的序列
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# 使用.loc进行标签切片访问
print("使用.loc进行标签切片访问：")
print(series.loc['b':'d'])
# 输出:
# b    20
# c    30
# d    40
# dtype: int64

# 使用.iloc进行位置切片访问
print("\n使用.iloc进行位置切片访问：")
print(series.iloc[1:4])
# 输出:
# b    20
# c    30
# d    40
# dtype: int64

# 使用.loc访问单个标签
print("\n使用.loc访问单个标签'c'：")
print(series.loc['c'])          # 输出:30

# 使用.iloc 访问单个位置
print("\n使用.iloc访问位置2：")
print(series.iloc[2])           # 输出:30
