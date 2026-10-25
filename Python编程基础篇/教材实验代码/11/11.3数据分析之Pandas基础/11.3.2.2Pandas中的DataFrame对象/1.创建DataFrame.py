import pandas as pd

# 1.使用字典列表
data = [{'A': 1, 'B': 2}, {'A': 5, 'B': 10, 'C': 20}]
df = pd.DataFrame(data)
print(df)
# 输出：
#    A   B     C
# 0  1   2   NaN
# 1  5  10  20.0

# 2.使用字典的字典
data = {'A': {0: 1, 1: 2}, 'B': {0: 5, 1: 10}}
df = pd.DataFrame(data)
print(df)
# 输出：
#    A   B 
# 0  1   5
# 1  2  10

# 3.使用二维数组
import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'], index=['x', 'y'])
print(df)
# 输出：
#    A  B  C
# x  1  2  3  
# y  4  5  6

# 4.使用Series对象
s1 = pd.Series([1, 3, 5])
s2 = pd.Series([2, 4, 6])

df = pd.DataFrame({'A': s1, 'B': s2})
print(df)
# 输出：
#    A  B
# 0  1  2
# 1  3  4
# 2  5  6

# 5.使用元组列表
data = [(1, 2), (3, 4), (5, 6)]
df = pd.DataFrame(data, columns=['A', 'B'])
print(df)
# 输出：
#    A  B
# 0  1  2
# 1  3  4
# 2  5  6

# 6.使用csv或其他文件类型
df = pd.read_csv('data.csv')
print(df)
# 输出：
#    A  B  C
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9