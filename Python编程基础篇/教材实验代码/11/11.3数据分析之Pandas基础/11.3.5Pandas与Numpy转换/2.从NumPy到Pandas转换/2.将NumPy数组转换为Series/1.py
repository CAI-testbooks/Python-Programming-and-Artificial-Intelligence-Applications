import numpy as np
import pandas as pd

# 创建一个NumPy数组
array = np.array([10, 20, 30, 40, 50])

# 将NumPy数组转换为Pandas Series
series = pd.Series(array)

# 打印转换后的Series
print(series)
# 输出：
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64