import pandas as pd

# 1.sum函数
# 创建一个包含多列的DataFrame
data = {
    'A': [10, 20, 30, 40, 50],
    'B': [5, 10, 15, 20, 25]
}
df = pd.DataFrame(data)

print ("原始DataFrame: \n", df)
# 输出:
# 原始DataFrame: 
#      A   B
# 0  10   5
# 1  20  10
# 2  30  15
# 3  40  20
# 4  50  25

# 计算每列的总和
total_sum = df.sum()
print("每列的总和:\n", total_sum)
# 输出:
# 每列的总和:
# A    150
# B     75
# dtype: int64

# 2.cumsum函数
data = {'values': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)
print("原始DataFrame: \n", df)
# 输出:
# 原始DataFrame: 
#     values
# 0      10
# 1      20
# 2      30
# 3      40
# 4      50

# 计算累积和
df['cumulative_sum'] = df['values'].cumsum( )
print("添加累积和后的 DataFrame:\n",df)
# 输出:
# 添加累积和后的 DataFrame:
#     values  cumulative_sum
# 0      10              10
# 1      20              30
# 2      30              60
# 3      40             100
# 4      50             150
