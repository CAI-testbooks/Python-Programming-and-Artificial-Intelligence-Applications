import pandas as pd

# 创建一个序列
series = pd.Series([10, 20, 30, 40, 50])

# 条件过滤：筛选大于20的元素
filtered_series = series[series > 20]
print("大于20的元素：")
print (filtered_series)
# 输出：
# 大于20的元素：
# 2    30
# 3    40
# 4    50
# dtype: int64

# 条件过滤：筛选小于等于30的元素
filtered_series = series[series <= 30]
print("\n小于等于30的元素：")
print(filtered_series)
# 输出：
# 0    10
# 1    20
# 2    30
# dtype: int64

# 条件过滤：筛选等于40的元素
filtered_series = series[series == 40]
print("\n等于40的元素：")
print(filtered_series)
# 输出：
# 等于40的元素：S
# 3    40
# dtype: int64