import pandas as pd
import numpy as np

# 创建一个包含NaN的DataFrame
df_nan = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, 6]
})

# 转换时处理NaN
array_nan = df_nan.to_numpy(dtype='float64') # 使用float64来确保NaN能被正确处理

# 打印转换后的NumPy数组
print(array_nan)
# 输出:
# [[ 1. 4.]
#  [nan 5.]
#  [ 3. 6.]]

