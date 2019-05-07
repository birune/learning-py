import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 2.5, 0.05) * np.pi
#arangeは浮動小数点数の間隔を持つ要素を作成することができる
#要素に対して一度に演算を行うことができる
s = np.sin(x)
c = np.cos(x)
#こういうのも一気にできる

plt.title("sin/cos functions")
plt.xlabel("rad")
plt.ylabel("value")
plt.grid(True)

plt.plot(x, s, label = "sin")
plt.plot(x, c, label = "cos")
plt.legend()
#ラベルから凡例を作成(ラベル名を表示)
plt.show()