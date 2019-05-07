import random
import matplotlib.pyplot as plt

data  = []

for i in range(1000):
    data.append(random.normalvariate(0, 10))

plt.title("Histogram")
plt.hist(data, bins=50)
#dataからヒストグラムを作成
plt.show()

#正規分布とは平均と標準偏差からデータがどのように分布するかをいい感じに想定するやつ
#平均をグラフの中央としていい感じにシンメトリな山形になる
#標準偏差の値が高いほど山が高く鋭くなる