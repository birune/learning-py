import numpy as np
import matplotlib.pyplot as plt

x = []
s = []
c = []

x = np.arange(-8, 8, 0.01)
y1 = 3*x+5
y2 = x*x

plt.title("functions")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.plot(x, y1, label = "y1")
plt.plot(x, y2, label = "y2")
plt.legend()
#ラベルから凡例を作成(ラベル名を表示)
plt.show()