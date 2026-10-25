import matplotlib.pyplot as plt
import numpy as np
from numpy. random import randn

# 创建画布
fig = plt.figure(figsize=(8, 7))
# 添加一个子图
ax1 = fig.add_subplot(1, 1, 1)          # 令ax1指向子图对象
# 绘制直方图
ax1.hist(randn(50), label='Data')     # 使用label参数为数据添加标签
# 设置坐标轴标签和标题
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Histogram with Legend')
# 添加图例
plt.legend(loc='upper right', fontsize='medium', title='Legend')
# 显示图形
plt.show()
