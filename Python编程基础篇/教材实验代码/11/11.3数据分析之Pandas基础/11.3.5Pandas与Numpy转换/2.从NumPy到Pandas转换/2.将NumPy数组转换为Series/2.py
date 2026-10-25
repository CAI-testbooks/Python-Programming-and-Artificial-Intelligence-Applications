import numpy as np
import pandas as pd

array = np.array([10, 20, 30, 40, 50])
# 自定义索引
custom_index = ['a', 'b', 'c', 'd', 'e']

# 将numpy数组转换为Series，并指定自定义索引
series_custom = pd.Series(array, index=custom_index)

# 打印转换后的Series
print(series_custom)
# 输出：
# a    10
# b    20
# c    30
# d    40
# e    50
# dtype: int64