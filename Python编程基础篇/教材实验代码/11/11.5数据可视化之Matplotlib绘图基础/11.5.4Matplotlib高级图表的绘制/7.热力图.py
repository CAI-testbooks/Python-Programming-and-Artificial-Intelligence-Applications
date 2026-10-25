import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris

plt.rcParams['font.sans-serif'] = ['SimHei']    # Matplotlib 正确显示中文,黑体
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号

# 加载鸢尾花数据集
data = load_iris()
features = data.data.T
# 计算特征之间的相关系数
correlation_matrix = np.corrcoef(features)
# 创建热力图
plt.imshow(correlation_matrix, cmap='hot', interpolation='nearest')
plt.colorbar()
# 使用中文标签
chinese_labels=['萼片长度(cm)', '萼片宽度(cm)', '花瓣长度 (cm)', '花瓣宽度(cm)']
plt.xticks(ticks=np.arange(len(chinese_labels) ), labels=chinese_labels)
plt.yticks(ticks=np.arange(len(chinese_labels) ), labels=chinese_labels)
# 添加标题
plt.title('鸢尾花数据集特征相关性热力图')
# 显示图形
plt.show()