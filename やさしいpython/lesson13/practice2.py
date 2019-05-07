from sklearn import cluster
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

#np.random.seed(0)

data, label = datasets.make_blobs(n_samples=1000, n_features=2, centers=7, cluster_std=10)

e = cluster.KMeans(n_clusters=7)
e.fit(data)
#クラスタリングを行う

print(e.labels_)
#各データの属するラベルの表示
print(e.cluster_centers_)
#各クラスタの中心を表示

plt.scatter(data[:, 0], data[:, 1], marker="o", c=e.labels_, edgecolor="k")
#スライス、すべての0列目(多分各x)とすべての1列目(多分各y) 
plt.scatter(e.cluster_centers_[:, 0], e.cluster_centers_[:, 1], marker="x")

plt.show()