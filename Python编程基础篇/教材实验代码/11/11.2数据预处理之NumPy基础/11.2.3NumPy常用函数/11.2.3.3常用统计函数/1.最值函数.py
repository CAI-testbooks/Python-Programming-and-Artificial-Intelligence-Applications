import numpy as np

# 创建一个二维数组
a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])

# 计算整个数组的最小值
print(np.amin(a))                                 # 输出：2

# 沿着列方向(axis=0)计算最小值
print(np.amin(a, axis=0))                         # 输出：[2 4 3]

# 沿着行方向(axis=1)计算最小值
print(np.amin(a, axis=1))                         # 输出：[3 3 2]

# 使用keepdims保持原始维度
print(np.amin(a, axis=1, keepdims=True) )
# 输出：
# [[3]
# [3]
# [2]]

# 使用initial参数设定初始最小值为5
print (np.amin(a, initial=5) )                   # 输出：2

# 使用where 参数选择部分元素参与计算
mask = np.array([[True, False, True], [False, True, True], [True, False, False]])
print(np.amin(a, where=mask, initial=10))        # 输出：2

