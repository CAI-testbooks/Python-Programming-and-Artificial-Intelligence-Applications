import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']    # Matplotlib 正确显示中文,黑体
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号

# 数据定义
data = np.array( [(-1.5, 0.5, -6, -6),
                (1, -1, -46, 46),
                (-3, -1, 11, -11),
                (1, 1.5, 80, 80),
                (0.5, 0.25, 25, 15),
                (-1.5, -0.5, -5, 40)], dtype=[('x', np.float32), ('y', np.float32),
                ('u', np.float32), ('v', np.float32)])
# 绘图
fig, ax = plt.subplots(figsize=(6, 6))          # 创建画布和坐标轴对象
#绘制风羽图,改变风羽的枢轴点为中间
ax.barbs (data['x' ], data['y'], data['u'], data['v'], length=8, pivot='middle')
# 设置图表标题和坐标轴标签
ax.set_title("风速风向风羽图展示")
ax.set_xlabel("X坐标")
ax.set_ylabel("Y坐标")
plt.show()
