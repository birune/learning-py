import random
import matplotlib.pyplot as plt

data = [8, 17, 0, 11, 6, 21, 16, 6, 17, 11, 7, 9, 6, 13, 12, 16, 3, 14, 13, 12]

x = []
y = []

for i in range(100):
    x.append(random.uniform(0, 50))
    y.append(random.uniform(0, 50))
    #0-50のランダムな数を取得しリストに追加

plt.scatter(x, y)
#散布図を作成
plt.show()

