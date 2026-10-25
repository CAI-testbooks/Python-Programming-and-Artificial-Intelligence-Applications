import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']    # Matplotlib 正确显示中文,黑体
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号

# 生成数据
x = np.arange(10)                               # 创建一个包含10个点的x轴数据
y = np.random.rand(10)                          # 为这些点生成一些随机的y轴数据
# 创建折线图
plt.plot(x, y, marker='o')                      # 在图中标记每个点
# 添加标题和标签
plt.title("折线图示例")
plt.xlabel("X")
plt.ylabel("Y")
# 显示图形
plt.show()





