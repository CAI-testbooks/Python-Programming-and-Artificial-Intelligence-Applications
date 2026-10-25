import numpy as np
import pandas as pd

# 创建一个的NumPy数组
array = np.array([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])
# 将NumPy数组转换为DataFrame
df = pd.DataFrame(array)
print(df)
# 输出：
#    0  1  2
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9