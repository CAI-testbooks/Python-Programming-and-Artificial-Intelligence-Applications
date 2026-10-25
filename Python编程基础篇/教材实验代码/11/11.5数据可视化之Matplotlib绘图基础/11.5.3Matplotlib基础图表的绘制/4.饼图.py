import matplotlib.pyplot as plt
import pandas as pd
from sklearn. datasets import load_iris

plt.rcParams['font.sans-serif'] = ['SimHei']    # Matplotlib 正确显示中文,黑体
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号

# 加载数据集
data = load_iris()
target = pd.Series(data.target)                 # 将目标变量转换为pandas Series
# 选择一个特征进行绘图,例如特征0
x = target.value_counts()                       # 各类别的数量
labels = data.target_names                      # 类别名称
# 创建饼图
plt.pie(x, labels=labels, autopct='$1.1f%%', startangle=140)
# 添加标题
plt.title('鸢尾花数据集的类别分布')
# 显示图形
plt.show()
