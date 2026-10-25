import numpy as np

dt = np.dtype([('name', 'U10'), ('age', int)])
a = np.array([ ("raju", 21), ("ani1", 25), ("ravi", 17), ("amar", 27) ], dtype=dt)

# 按name 字段排序
print('按name排序:')
print (np.sort (a, order='name') )
# 输出:
# 按name排序:
# [ ('amar', 27) ('ani1', 25) ('raju', 21) ('ravi', 17) ]

# 按age 字段排序
print('按age排序:')
print (np.sort (a, order='age'))
# 输出:
# 按age排序:
# [('ravi', 17) ('raju', 21) ('ani1', 25) ('amar', 27)]
