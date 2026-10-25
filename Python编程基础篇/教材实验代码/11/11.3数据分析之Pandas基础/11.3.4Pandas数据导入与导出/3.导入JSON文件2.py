from pandas import json_normalize

# 假设复杂的嵌套JSON数据,如下所示:
# {
# "name" : "Alice",
# "info": {
#       "age" : 25,
#       "city": "New York"
#   }
# }
# 这样的数据结构在读取时需要展平
data = [
    {"name": "Alice", "info": {"age": 25, "city": "New York"}},
    {"name": "Bob", "info": {"age": 30, "city": "San Francisco"}}
]

# 使用json_normalize来展平嵌套的JSON数据
df_flat = json_normalize(data)

# 查看展平后的数据
print(df_flat)
# 输出:
#    name  info.age       info.city
# 0  Alice        25       New York
# 1    Bob        30  San Francisco