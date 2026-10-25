from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

# 示例数据:假设我们有一个四维的数据集

data = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# 1. 数据标准化(零均值化)
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# 2. 创建PCA对象,指定保留2个主成分
pca = PCA(n_components=2)

# 3. 拟合数据并计算主成分
pca.fit(data_scaled)

# 4. 将数据转换到主成分空间
data_reduced = pca.transform(data_scaled)

# 输出降维后的数据
print("降维后的数据：")
print(data_reduced)
# 输出：
# 降维后的数据:  
# [[-2.68328157e+00  9.99200722e-16]
#  [-8.94427191e-01  3.88578059e-16]
#  [ 8.94427191e-01 -3.88578059e-16]
#  [ 2.68328157e+00 -9.99200722e-16]]

# 输出主成分(特征向量)
print("主成分(特征向量)：")
print(pca.components_)
# 输出：
# 主成分(特征向量):
# [[ 0.5         0.5         0.5         0.5       ]
#  [ 0.8660254  -0.28867513 -0.28867513 -0.28867513]]

# 输出解释方差比例
print("解释方差比例：")
print(pca.explained_variance_ratio_)
# 输出：
# 解释方差比例:
# [1.00000000e+00 6.06718323e-33]]