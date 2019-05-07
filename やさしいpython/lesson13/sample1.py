from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
#乱数の初期値を固定する
x, y = datasets.make_regression(n_samples=100, n_features=1, noise=30)
#説明変数(x)の数1、ノイズ30のデータを100個
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
#データをtrainとtestに分ける、7割trainで3割test
e = linear_model.LinearRegression()
#線形回帰を行うためのインスタンスの取得
e.fit(x_train, y_train)
#あてはめを行う

print("回帰係数は", e.coef_, "です")
print("切片は", e.intercept_, "です")

y_pred = e.predict(x_test)
#x_testをモデルに当てはめてyを予測する(これが回帰直線になる)

print("学習データによる決定係数は", e.score(x_train, y_train), "です")
print("テストデータによる決定係数は", e.score(x_test, y_test), "です")
#決定係数が1に近いほど当てはまりがよい
#多分1に近いほどxとyの相関関係は強い

plt.scatter(x_train, y_train, label="train")
plt.scatter(x_test, y_test, label="test")
plt.plot(x_test, y_pred, color="m")
#回帰直線のプロット
plt.legend()

plt.show()
