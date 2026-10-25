import pandas as pd

# 假设文件名为'data.csv'
df = pd.read_csv('data.csv')

# 使用read_table来读取csv文件，需要指定分隔符为逗号
df = pd.read_table('data.csv', sep=',')