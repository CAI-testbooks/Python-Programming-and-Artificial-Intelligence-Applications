import pandas as pd
import numpy as np

# 创建一个包含NaN的Series
s_nan = pd.Series([1, np.nan, 3, 4, 5])

# 转换为NumPy数组
array_nan = s_nan.to_numpy()

# 打印转换后的NumPy数组
print(array_nan)
# 输出：
# [ 1. nan  3.  4.  5.]