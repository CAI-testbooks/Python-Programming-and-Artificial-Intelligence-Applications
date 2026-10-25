set1 = set()
tmp = {}
print(type(set1), type(tmp))
# 运行结果: <class 'set'> <class 'dict'>
set2 = {1, 2, 3, 4, 5, 5, 5, 5}
print(set2)
# 运行结果: {1, 2, 3, 4, 5} # 自动去重
set3= set([1, 2, 3, 4, 5, 5, 5, 5])
print(set3)
# 运行结果: {1, 2, 3, 4, 5}
