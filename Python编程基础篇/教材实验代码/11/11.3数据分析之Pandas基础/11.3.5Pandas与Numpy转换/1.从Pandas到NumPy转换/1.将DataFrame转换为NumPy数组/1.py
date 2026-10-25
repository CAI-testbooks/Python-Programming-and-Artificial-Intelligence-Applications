import pandas as pd

# 创建一个示例 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# 使用.values属性将DataFrame转换为NumPy数组
array = df.values

print("DataFrame:\n", df)
print("NumPy数组:\n", array)