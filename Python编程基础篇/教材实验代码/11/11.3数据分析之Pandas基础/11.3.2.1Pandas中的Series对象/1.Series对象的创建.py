import pandas as pd

# 通过列表创建Series
data_list = [1, 2, 3, 4, 5]
series_from_list = pd.Series(data_list)
print("通过列表创建的Series：")
print (series_from_list)
# 输出：
# 通过列表创建的 Series：
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# 通过字典创建Series
data_dict = {'a': 1, 'b': 2, 'c': 3}
series_from_dict = pd.Series(data_dict)
print("\n通过字典创建的Series：")
print(series_from_dict)
# 输出：
# 通过字典创建的Series：
# a    1
# b    2
# c    3
# dtype: int64

# 创建Series时指定索引
data = [1, 2, 3]
index = ['x', 'y', 'z']
series_with_index = pd.Series(data, index=index)
print("\n指定索引创建的Series：")
print(series_with_index)
# 输出：
# 指定索引创建的Series：
# x    1
# y    2
# z    3
# dtype: int64