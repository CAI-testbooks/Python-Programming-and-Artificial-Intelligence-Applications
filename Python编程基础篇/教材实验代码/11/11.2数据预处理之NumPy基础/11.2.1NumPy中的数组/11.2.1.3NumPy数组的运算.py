import numpy as np

# 1.基础运算
arr = np.array([1, 2, 3, 4, 5])
print (arr + 1)                     # 输出:[2 3 4 5 6]
print (arr - 1)                     # 输出:[0 1 2 3 4]
print (arr * 2)                     # 输出:[ 2  4  6  8 10]
print (arr / 2)                     # 输出:[0.5 1.  1.5 2.  2.5]

arr = np.array([1, 2, 3, 4, 5])
arr_1 = np.array([6, 7, 8, 9, 10])
print (arr + arr_1)         # 输出:[7 9 11 13 15]
print (arr - arr_1)         # 输出:[-5 -5 -5 -5 -5]
print (arr * arr_1)         # 输出:[6 14 24 36 50]
print (arr / arr_1)         # 输出:[0.16666667 0.28571429 0.375 0.44444444 0.5]

# 2.比较运算
arr = np.array ([1, 2, 3, 4, 5])
arr_1 = np.array( [6, 7, 8, 9, 10])
print (arr < arr_1)         # 输出: [ True True True True True]
print (arr > arr_1)         # 输出: [False False False False False]
print (arr >= arr_1)        # 输出: [False False False False False]
print (arr <= arr_1)        # 输出: [ True True True True True]
print (arr == arr_1)        # 输出: [False False False False False]
print (arr != arr_1)        # 输出: [ True True True True True]
