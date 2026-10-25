import numpy as np

# 创建一个数组
a = np.array([7, 9, 5, 2, 8, 4, 3, 1, 4, 3])
print('原数组:',a)
# 输出:
# 原数组: [7 9 5 2 8 4 3 1 4 3]

# 获取排序后的索引
sorted_indices = a.argsort()
print('排序后索引:',sorted_indices)
# 输出:
# 排序后索引: [7 3 6 9 8 5 2 0 4 1]

# 返回数组索引排序后显示较大的5个数
top_5_largest = a[sorted_indices][-5:]
print("显示较大的5个数:",top_5_largest)
# 输出:
# 显示较大的5个数: [4 5 7 8 9]