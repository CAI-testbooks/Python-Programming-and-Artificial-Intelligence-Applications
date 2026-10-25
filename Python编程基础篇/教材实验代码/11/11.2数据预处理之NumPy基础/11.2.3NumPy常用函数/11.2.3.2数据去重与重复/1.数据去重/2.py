import numpy as np

# 创建一个二维数组
data = np.array([[1, 8, 3, 3, 4],
                [1, 8, 9, 9, 4],
                [1, 8, 3, 3, 4]])

# 删除整个数组中的重复元素
uniques = np.unique(data)
print("删除重复元素后的数组：",uniques)
# 输出:
# 删除重复元素后的数组： [1 3 4 8 9]

# 删除重复的行
uniques = np.unique(data, axis=0)
print("删除重复行后的数组：")
print(uniques)
# 输出:
# 删除重复行后的数组：
# [[1 8 3 3 4]
#  [1 8 9 9 4]]

# 删除重复的列
uniques = np.unique(data, axis=1)
print("删除重复列后的数组：")
print(uniques)
# 输出:
# 删除重复列后的数组：
# [[1 3 4 8]
#  [1 9 4 8]
#  [1 3 4 8]]
