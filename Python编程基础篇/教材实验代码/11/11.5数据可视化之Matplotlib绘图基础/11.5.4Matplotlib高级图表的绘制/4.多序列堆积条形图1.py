import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']    # Matplotlib 正确显示中文,黑体
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号

# 数据数组
series1 = np.array([3, 4, 5, 1])
series2 = np.array([2, 5, 6, 3])
series3 = np.array([5, 3, 3, 2])
index = np.arange(4)
colors = ['#6aabd1', '#b6d957','#ffcc5c'] # 蓝绿色,淡绿色,淡黄色
# 创建图形和轴
fig, ax = plt.subplots ()
# 调整柱状图参数
width =0.35 #柱子的宽度
ax.bar(index, series1, width, color=colors [0], label='序列1')
ax.bar(index, series2, width, bottom=series1, color=colors [1], label='序列2')
ax.bar(index, series3, width, bottom=series1 + series2, color=colors[2], label='序列3')
# 添加标签、标题和图例
ax.set_xlabel('类别')
ax.set_ylabel('值')
ax.set_title('多序列堆积条形图')
ax.set_xticks(index)
ax.set_xticklabels(['一','二','三','四'])
ax.legend ()
# 展示图形
plt.show()