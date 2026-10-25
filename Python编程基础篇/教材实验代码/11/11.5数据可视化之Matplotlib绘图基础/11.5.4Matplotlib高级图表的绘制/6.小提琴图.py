import matplotlib.pyplot as plt
from sklearn. datasets import load_iris

plt.rcParams['font.sans-serif'] = ['SimHei']    # Matplotlib 正确显示中文,黑体
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号

# 加载数据集
data = load_iris()
features = data.data
target = data.target
petal_lengths = features[:, 2]
# 为不同种类的鸢尾花准备数据
data_to_plot = [petal_lengths[target == i] for i in range (3) ]
# 创建小提琴图
plt.violinplot (data_to_plot, showmeans=True, showmedians=True)
plt.xlabel('鸢尾花种类')
plt.ylabel('花瓣长度 (cm)')
plt.title('鸢尾花不同种类的花瓣长度小提琴图')
plt.xticks([1, 2, 3], ['Setosa', 'Versicolor', 'Virginica'])
# 显示图形
plt.show()

