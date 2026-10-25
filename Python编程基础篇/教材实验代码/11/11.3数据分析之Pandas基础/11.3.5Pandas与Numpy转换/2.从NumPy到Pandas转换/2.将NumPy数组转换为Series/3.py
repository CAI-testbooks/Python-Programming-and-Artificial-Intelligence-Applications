import numpy as np
import pandas as pd

# 创建一个包含NaN的NumPy数组
array_with_nan = np.array([1, 2, np.nan, 4, 5])

# 转换为Series
series_with_nan = pd.Series(array_with_nan)

# 打印转换后的Series
print(series_with_nan)
# 输出：
# 0    1.0
# 1    2.0
# 2    NaN
# 3    4.0
# 4    5.0
# dtype: float64
