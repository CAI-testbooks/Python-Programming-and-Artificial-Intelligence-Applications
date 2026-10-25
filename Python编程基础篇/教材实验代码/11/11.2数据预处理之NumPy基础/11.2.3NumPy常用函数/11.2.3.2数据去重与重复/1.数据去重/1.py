import numpy as np

# 创建一个包含重复元素的数组
names= np.array(['红色','蓝色','蓝色','白色','红色','红色','蓝色'])
print('原数组:',names)
# 输出:
# 原数组: ['红色' '蓝色' '蓝色' '白色' '红色' '红色' '蓝色']

# 去重后的排序结果
unique_names = np. unique (names)
print('去重后的数组：',unique_names)
# 输出:
# 去重后的数组： ['白色' '红色' '蓝色']

# 返回每个值出现的次数
unique_names, counts = np. unique (names, return_counts=True)
print('数据出现次数：',(unique_names,counts))
# 输出:
# 数据出现次数： (array(['白色', '红色', '蓝色'], dtype='<U2'), array([1, 3, 3]))
