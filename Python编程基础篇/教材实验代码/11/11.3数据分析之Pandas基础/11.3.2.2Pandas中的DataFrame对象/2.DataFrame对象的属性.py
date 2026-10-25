import pandas as pd

# 创建一个示例 DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City':
['New York', 'Paris', 'London']}
df = pd.DataFrame(data)

# 输出 DataFrame 的各种属性
print ("Data Types: \n", df.dtypes)
# 输出:
# Name object
# Age int64
# City object
# dtype: object

print ("Index: \n", df.index)
# 输出:
# RangeIndex(start=0, stop=3, step=1)

print ( "Columns : \n", df.columns)
# 输出:
# Index( ['Name', 'Age', 'City'], dtype='object')

print ("Values: \n", df.values)
# 输出:
# [['Alice' 25 'New York']
#  ['Bob' 30 'Paris']
#  ['Charlie' 35 'London']]

print ("Shape: \n", df.shape)
# 输出:
# (3, 3)

print ("Size: \n", df.size)
# 输出:
# 9
