from sklearn.decomposition import PCA

# 创建PCA对象，指定保留2个主成分，并启用白化处理
pca = PCA(n_components=2, copy=True, whiten=True, svd_solver='auto')

# 创建PCA对象，指定保留95%的累积方差
pca_variance = PCA(n_components=0.95)

# 创建PCA对象，使用随机化SVD求解器，并设置随机种子
pca_randomized = PCA(n_components=2, svd_solver='randomized', random_state=42)