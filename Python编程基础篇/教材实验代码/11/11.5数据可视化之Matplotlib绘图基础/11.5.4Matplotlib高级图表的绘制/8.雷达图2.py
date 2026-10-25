import matplotlib.pyplot as plt
import pandas as pd
from math import pi
# 创建数据
df = pd. DataFrame({
    'group': ['A', 'B', 'C', 'D'],
    'var1': [38, 1.5, 30,4],
    'var2': [29, 10, 9, 34],
    'var3': [8, 39, 23, 24],
    'var4': [7, 31, 33, 14],
    'var5': [28, 15, 32, 14]
})
# ------------步骤1创建背景
# 变量类别
categories = list(df)[1:]
# 变量类别个数
N = len(categories)
# 设置每个点的角度值
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
# 初始化极坐标网格
ax = plt.subplot(111, polar=True)
# 设置角度偏移
ax.set_theta_offset(pi / 2)
# 设置顺时针还是逆时针，1或者-1
ax.set_theta_direction(-1)
# 设置x轴的标签
plt.xticks(angles[:-1], categories)
# 画标签
ax.set_rlabel_position(0)
plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=7)
plt.ylim(0, 40)
# ------------步骤2绘制数据
# 单独绘制每一组数据
# Ind1
values = df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="group A")
ax.fill(angles, values, 'b', alpha=0.1)
# Ind2
values = df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="group B")
ax.fill(angles, values, 'r', alpha=0.1)
# 添加图例
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.show()