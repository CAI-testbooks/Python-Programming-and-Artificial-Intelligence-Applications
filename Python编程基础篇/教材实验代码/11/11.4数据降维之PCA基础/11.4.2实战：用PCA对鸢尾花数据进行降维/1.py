# 导入 PCA
from sklearn.decomposition import PCA
# 导入鸢尾花数据集
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']    # Matplotlib 正确显示中文,黑体
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号

# 加载数据
iris = load_iris()
X = iris.data

# 使用PCA进行降维
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# 可视化降维结果
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target)
plt.xlabel('主成分1')
plt.ylabel('主成分2')

plt.title('鸢尾花数据集的PCA降维结果')
plt.show()