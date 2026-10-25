import pandas as pd

# 创建带标签索引的序列
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# 使用标签访问元素
print("标签'c'对应的值：", series['c'])  # 输出：30

# 使用标签访问多个元素
print("标签'a'和'e'对应的值：")
print(series[['a', 'e']])
# 输出：
# a    10
# e    50
# dtype: int64

#使用标签访问不存在的元素(会抛出KeyError)
try:
    print("标签'f'对应的值：", series['f'])
except KeyError as e:
    print("错误： ", e)
# 输出：
# 错误： 'f'
