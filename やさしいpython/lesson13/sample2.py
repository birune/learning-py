from sklearn import cluster
from sklearn import datasets
import matplotlib.pyplot as plt

data, label = datasets.make_blobs(n_samples=500, n_features=2, centers=5)
#説明変数が2個、クラスタの中央の数5個のデータを500
e = cluster.KMeans(n_clusters=5)
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