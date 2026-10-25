import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']    # Matplotlib 正确显示中文,黑体
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号

# 创建数据
x = np.linspace(0, 9, 100)
y = np.exp(x)
# 创建图形
plt.figure()
plt.plot(x, y, label='$y = e^x$')
# 启用自动缩放
plt.autoscale(enable=True, axis='both', tight = False)
# 添加标签和图例
plt.xlabel('x')
plt.ylabel('y')
plt.title('自动缩放坐标轴')
plt.legend()
# 显示图形
plt.show()
