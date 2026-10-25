import pandas as pd

# 假设我们有一个DataFrame'df'
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)

# 导出DataFrame到CSV文件,不包含索引列
df.to_csv('output.csv', index=False)

# 如果想要指定分隔符,比如使用制表符代替默认的逗号分隔符
df.to_csv('output.tsv', sep='\t', index=False)
