tmp1 = ('Python')
print(type(tmp1))
# 输出结果: <class 'str'>

tmp2 = ('Python',)
print(type(tmp2))
# 输出结果: <class 'tuple'>

weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
print(weekdays[-2])        # 支持正向和反向索引
# 运行结果: Thursday

print(weekdays[1:4])       # 支持切片操作
# 运行结果: ('Tuesday', 'Wednesday', 'Thursday')

for day in weekdays:       # 支持迭代
    print(day, end=' ')
# 运行结果: Monday Tuesday Wednesday Thursday Friday
weekdays[2] = 0
# 运行结果: TypeError: 'tuple' object does not support item assignment

del weekdays[2]
# 运行结果: TypeError: 'tuple' object doesn't support item deletion

weeks = weekdays + ('Saturday', 'Sunday')  # 支持连接操作
print(weeks)
# 运行结果: ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

two_weekdays = weekdays * 2                # 支持重复操作
print(two_weekdays)
# 运行结果: ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

del weekdays  # 支持删除整个元组
