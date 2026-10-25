import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

plt.rcParams['font.sans-serif'] = ['SimHei']    # Matplotlib 正确显示中文,黑体
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号

# 加载数据集
data = load_iris()
# 选择一个特征进行绘图,例如特征0
x = data.data[:,0]                              # 特征0
# 创建直方图
plt.hist (x, bins=20, color='blue', edgecolor='black', alpha=0.7)
# 添加标签和标题
plt.xlabel("花萼长度")
plt.ylabel("频数")
plt.title("鸢尾花数据集的直方图")
# 显示图形
plt.show ()
