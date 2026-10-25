import pandas as pd

# 创建一个简单的序列
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index, name='MySeries')

# 访问属性
print ("Index：", series.index)              # 输出：Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
print ("Values：", series.values)            # 输出：[10 20 30 40 50]
print ("Data Type：", series.dtype)          # 输出：int64
print ( "Shape：", series. shape)            # 输出：(5,)
print ("Size：", series.size)                # 输出：5
print ("Is Empty：", series.empty)           # 输出：False
print ("Name：", series.name)                # 输出：MySeries







