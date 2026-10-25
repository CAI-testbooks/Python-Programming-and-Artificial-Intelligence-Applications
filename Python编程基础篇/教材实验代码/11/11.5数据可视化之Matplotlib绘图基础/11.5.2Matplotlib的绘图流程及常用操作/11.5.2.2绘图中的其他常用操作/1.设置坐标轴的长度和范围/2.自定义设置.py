import matplotlib.pyplot as plt
import numpy as np
# 创建数据
x = np.linspace(0, 9, 100)
y = np.exp(x)
# 创建图形
plt.figure()
plt.plot(x, y, label='$y = e^x$')
# 手动设置坐标轴的范围
plt.xlim(0, 9)          # 设置x轴的范围为0到9
plt.ylim(0, 5000)       # 设置y轴的范围为0到5000，截断高值
# 添加标签和图例
plt.xlabel('x')
plt.ylabel('y')
plt.title('手动缩放坐标轴')
plt.legend()
# 显示图形
plt.show()


