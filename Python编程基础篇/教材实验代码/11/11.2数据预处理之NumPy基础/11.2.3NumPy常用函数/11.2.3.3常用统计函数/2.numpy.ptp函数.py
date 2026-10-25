import numpy as np

# 创建一个二维数组
a = np.array([[4, 9, 2], [1, 5, 6], [7, 3, 8]])

# 计算整个数组的范围
print(np.ptp(a))                # 输出：8(最大值9-最小值1)

# 沿行方向(axis=1)计算范围
print(np.ptp(a, axis = 1))      # 输出：[7 5 5],即每行最大值和最小值的差

# 沿列方向(axis=0)计算范围
print(np.ptp(a, axis = 0))      # 输出：[6 6 6],即每列最大值和最小值的差





