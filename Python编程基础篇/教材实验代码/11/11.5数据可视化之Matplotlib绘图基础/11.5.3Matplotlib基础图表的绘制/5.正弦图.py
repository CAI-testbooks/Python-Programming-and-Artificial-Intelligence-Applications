import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris

plt.rcParams['font.sans-serif'] = ['SimHei']    # Matplotlib 正确显示中文,黑体
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号

# 生成正弦波数据
x = np.linspace(0, 2 * np.pi, 100)              # 生成0到2的100个点
y = np.sin(x)                                   # 计算正弦值
# 创建正弦图
plt.plot(x, y, label='正弦波')
# 添加标签和图例
plt.xlabel("角度(弧度)")
plt.ylabel("正弦值")
plt.title('正弦波形图')
plt.legend()
# 显示图形
plt.show()
