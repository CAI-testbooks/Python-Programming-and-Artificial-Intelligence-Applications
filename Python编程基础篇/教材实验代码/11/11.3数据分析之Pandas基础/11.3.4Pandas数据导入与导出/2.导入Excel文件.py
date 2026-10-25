import pandas as pd

# 假设Excel文件名为'data.xlsx'
# 加载第一个工作表
df = pd.read_excel('data.xlsx')

# 查看加载的数据
print (df.head())                                             # 输出前五行数据

# 如果要指定加载特定的工作表,可以使用sheet_name参数
df_sheet2 = pd.read_excel('data.xlsx', sheet_name=' Sheet2')

# 查看加载的第二个工作表数据
print(df_sheet2.head())

#加载包含多个工作表的Excel文件,并使用工作表名称作为键来访问
xls = pd.read_excel('data.xlsx', sheet_name=None)

# 访问不同的工作表
print (xls['Sheet1'])                                       # 输出第一个工作表的数据
print (xls['Sheet2'])                                       # 输出第二个工作表的数据