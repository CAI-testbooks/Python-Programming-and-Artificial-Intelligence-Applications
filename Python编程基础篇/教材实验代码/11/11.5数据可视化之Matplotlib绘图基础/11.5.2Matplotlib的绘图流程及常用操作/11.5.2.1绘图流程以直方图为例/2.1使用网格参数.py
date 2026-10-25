import matplotlib.pyplot as plt

# 创建画布
fig = plt.figure(figsize=(8, 6))

#在2行2列的网格中添加子图
ax1 = fig.add_subplot(2, 2, 1) # 第1行第1列
ax2 = fig.add_subplot(2, 2, 2) # 第1行第2列
ax3 = fig.add_subplot(2, 2, 3) # 第2行第1列
ax4 = fig.add_subplot(2, 2, 4) # 第2行第2列

