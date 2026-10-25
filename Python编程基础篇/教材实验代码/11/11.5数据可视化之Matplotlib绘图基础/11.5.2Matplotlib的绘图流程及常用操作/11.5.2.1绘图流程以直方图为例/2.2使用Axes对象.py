import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure()
gs = gridspec.GridSpec(3, 3)
ax1 = fig.add_subplot(gs[0, :])          # 第1行,占据所有列
ax2 = fig.add_subplot(gs[1, :- 1] )      # 第2行,占据前两列
ax3 = fig.add_subplot(gs[1:, 2])         # 第2行和第3行,占据第3列
ax4 = fig.add_subplot(gs[2, 0])          # 第3行第1列
ax5 = fig.add_subplot(gs[2, 1])          # 第3行第2列
plt.tight_layout()
plt.show()





