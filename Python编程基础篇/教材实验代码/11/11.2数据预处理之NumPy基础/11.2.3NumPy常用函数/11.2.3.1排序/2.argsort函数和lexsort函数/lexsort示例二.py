import numpy as np

# 表示A列
a = [2, 5, 1, 8, 1]
# 表示B列
b = [9, 0, 3, 2, 0]

# 先按A列然后按B列进行排序
ind = np. lexsort ( (b, a))
print ( "ind: ", ind)
# 输出:
# ind:  [4 2 0 1 3]

# 根据排序后的索引重新排列A列和B列
tmp = [ (a[i], b[i]) for i in ind]
print ( "tmp:", tmp)
# 输出:
# tmp: [(1, 0), (1, 3), (2, 9), (5, 0), (8, 2)]