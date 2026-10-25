import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']    # Matplotlib 正确显示中文,黑体
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号

# 加载数据集
data = load_iris()
# 选择两个特征进行绘图,例如特征0和特征1
x = data.data[:, 0]                             # 花瓣长度
y = data.data[:, 1]                             # 花瓣宽度
# 将数据转换为极坐标系中的角度和半径
theta = np.linspace(0, 2 * np.pi, len(x), endpoint=False)
r = y / x
# 创建玫瑰图
plt.figure(figsize=(8, 8))
plt.polar(theta, r, label='鸢尾花数据集的玫瑰图')
# 添加图例和标题
plt.legend ()
plt.title('鸢尾花数据集的玫瑰图')
# 显示图形
plt.show()