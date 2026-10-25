import pandas as pd

# 创建一个示例 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# 使用to_numpy()方法转换DataFrame，并指定数据类型为float32
array = df.to_numpy(dtype='float32')

# 打印转换后的NumPy数组及其数据类型
print(array)
# 输出:
# [[1. 4. 7.]
#  [2. 5. 8.]
#  [3. 6. 9.]]

print(array.dtype)
# 输出:
# float32
