import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.datasets import make_swiss_roll

plt.rcParams['font.sans-serif'] = ['SimHei']    # Matplotlib 正确显示中文,黑体
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号

# 生成数据
X, color = make_swiss_roll(n_samples=800)
# 创建图形和子图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 数据点
x = X[:,0]
y = X[:,1]
z = X[:,2]
# 绘制三维散点图
scatter = ax.scatter(x, y, z, c=color, cmap='viridis')
# 添加颜色条
fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=5)
# 设置标签
ax.set_xlabel('X坐标')
ax.set_ylabel('Y坐标')
ax.set_zlabel('Z坐标')
ax.set_title('瑞士卷三维散点图')
# 显示图形
plt.show()