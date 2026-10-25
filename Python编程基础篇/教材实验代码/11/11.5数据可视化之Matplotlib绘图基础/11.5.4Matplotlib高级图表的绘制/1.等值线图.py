import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification

plt.rcParams['font.sans-serif'] = ['SimHei']    # Matplotlib 正确显示中文,黑体
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号

# 创建数据
dx = 0.05
dy = 0.005
x = np.arange(-1.0, 1.0, dx)
y = np.arange(-1.0, 1.0, dy)
X, Y = np.meshgrid(x, y)
def Z(x,y):
    return (1.5-y**5+x**5)*np.exp(x**2-y-1)     # 设置绘制函数
# 绘制等值线图
C = plt.contour(X, Y, Z(x, Y), levels=8, cmap='RdGy')
plt.contourf(X, Y, Z(X,Y), 8)
plt.clabel(C, inline=1, fontsize=10)
# 添加标签和图例
plt.title('二维数据的等值线图')
plt.colorbar(label='高度值')                    # 添加颜色条
# 显示图形
plt. show()
