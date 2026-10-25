import matplotlib.pyplot as plt
import numpy as np
from sklearn. datasets import load_breast_cancer

plt.rcParams['font.sans-serif'] = ['SimHei']    # Matplotlib 正确显示中文,黑体
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号

# 加载数据集
data = load_breast_cancer()
# 选择两个特征进行绘图，例如特征0和特征1
x = data.data[:, 0]                             # 特征 0
y = data.data[:, 6]                             # 特征 1
# print (data.data[:10,:])
labels = data.target                            # 标签
# 创建散点图：良性肿瘤(标签为0)为绿色，恶性肿瘤(标签为1)为红色，s参数控制点的大小，alpha参数控制透明度
plt.scatter(x[labels == 0], y[labels == 0], c='green', marker='o', label='良性', s=30, alpha=0.8)
plt.scatter(x[labels == 1], y[labels == 1], c='red', marker='o', label='恶性', s=30, alpha=0.8)
plt.xlabel("平均半径")
plt.ylabel("平均凹度")
plt.title('乳腺癌数据集的散点图')
plt.legend()
plt.show()




