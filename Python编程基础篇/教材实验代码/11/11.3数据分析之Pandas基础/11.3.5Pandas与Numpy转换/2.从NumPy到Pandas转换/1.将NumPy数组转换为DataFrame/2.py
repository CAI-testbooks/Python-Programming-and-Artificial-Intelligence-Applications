import numpy as np
import pandas as pd

# 创建一维NumPy数组
array_1d = np.array([1, 2, 3, 4, 5])

# 将NumPy数组转换为DataFrame
df_1d = pd.DataFrame(array_1d, columns=['SingleColumn'])
print(df_1d)
# 输出：
#    SingleColumn
# 0       1
# 1       2
# 2       3
# 3       4
# 4       5