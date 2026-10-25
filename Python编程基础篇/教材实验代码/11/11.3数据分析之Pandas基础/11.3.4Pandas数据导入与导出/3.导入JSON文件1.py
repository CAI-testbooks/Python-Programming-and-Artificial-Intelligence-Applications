import pandas as pd

# 假设JSON文件名为'data.json'
# 以下是一个假设的JSON文件的内容结构示例:
# [
#   {"name": "Alice", "age": 25, "city": "New York"},
#   {"name": "Bob", "age": 30, "city": "San Francisco"}
# ]

# 从JSON文件读取数据
df = pd.read_json('data.json')

# 查看加载的数据
print(df)
# 输出:
#     name  age           city
# 0  Alice   25       New York
# 1    Bob   30  San Francisco

# 如果JSON数据是以不同的格式嵌套或结构化的,需要调整‘orient’参数来正确解析
# 例如,如果JSON数据是列式结构,可以这样读取:
# df = pd.read_json('data.json', orient='columns')