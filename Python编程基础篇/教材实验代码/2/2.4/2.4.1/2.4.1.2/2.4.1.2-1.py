import numpy as np

# 单精度浮点数
single_precision = np.float32(3.141592653589793)
print("单精度浮点数：", single_precision)
print("有效数字位数：", np.finfo(np.float32).precision)

# 双精度浮点数
double_precision = np.float64(3.141592653589793)
print("双精度浮点数：", double_precision)
print("有效数字位数：", np.finfo(np.float64).precision)

# 输出结果
# 单精度浮点数： 3.1415927
# 有效数字位数： 6
# 双精度浮点数： 3.141592653589793
# 有效数字位数： 15
