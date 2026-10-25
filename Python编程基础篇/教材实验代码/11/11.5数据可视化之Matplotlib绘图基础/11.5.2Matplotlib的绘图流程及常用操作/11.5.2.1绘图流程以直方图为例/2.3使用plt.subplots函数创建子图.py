import matplotlib.pyplot as plt
import numpy as np

# 创建画布和2×2的子图网格
fig, axes = plt.subplots(2, 2, figsize=(8, 6))

# 在第一个子图中绘制数据
axes[0, 0].plot(np.random.rand(10))
axes[0, 0].set_title('Subplot 1')

# 在第二个子图中绘制数据
axes[0, 1].scatter(np.random.rand(10), np.random.rand(10))
axes[0, 1].set_title('Subplot 2')

# 在第三个子图中绘制数据
axes[1, 0].hist(np.random.randn(100), bins=20)
axes[1, 0].set_title('Subplot 3')

# 在第四个子图中绘制数据
axes[1, 1].bar(['A', 'B', 'C'], [3, 7, 2])
axes[1, 1].set_title('Subplot 4')

# 调整子图之间的间距
plt.tight_layout ()

# 显示图形
plt.show()
