import pandas as pd

# 1.分组
data = {
    'City': ['New York', 'Los Angeles', 'New York', 'San Francisco',
        'Los Angeles', 'New York', 'San Francisco', 'Los Angeles'],
    'Month': ['January', 'January', 'February', 'February', 'March', 'March',
        'January', 'February' ],
    'Sales': [200, 250, 450, 300, 400, 500, 350, 220]
}
df = pd.DataFrame(data)
print(df)
# 输出:
#         City     Month  Sales
# 0       New York   January    200
# 1    Los Angeles   January    250
# 2       New York  February    450
# 3  San Francisco  February    300
# 4    Los Angeles     March    400
# 5       New York     March    500
# 6  San Francisco   January    350
# 7    Los Angeles  February    220

# 按照城市进行分组
grouped = df.groupby('City')
for name, group in grouped:
    print("\nGroup name: ", name)
    print(group)
# 输出:
# Group name:  Los Angeles
#           City     Month  Sales
# 1  Los Angeles   January    250
# 4  Los Angeles     March    400
# 7  Los Angeles  February    220

# Group name:  New York
#        City     Month  Sales
# 0  New York   January    200
# 2  New York  February    450
# 5  New York     March    500

# Group name:  San Francisco
#            City     Month  Sales
# 3  San Francisco  February    300
# 6  San Francisco   January    350

# 2.查看分组
# 使用 .groups 属性查看分组索引
groups_indices = grouped.groups
print ("\nGroup indices: ")
for city, indices in groups_indices.items () :
    print (f" {city} : {indices} ")
# 输出:
# Group indices:
# Los Angeles: Index([1, 4, 7], dtype='int64')
# New York: Index([0, 2, 5], dtype='int64')
# San Francisco: Index([3, 6], dtype='int64')

# 3.选择特定分组
# 选择特定的分组数据,比如New Work 的数据
group_ny = grouped.get_group('New York')
print ("\nNew York Group:")
print (group_ny)
# 输出:
# New York Group:
#        City     Month  Sales
# 0  New York   January    200
# 2  New York  February    450
# 5  New York     March    500