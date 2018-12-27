#coding:utf-8
#**********************************https://ljalphabeta.gitbooks.io/python-/content/ch2section3.html
#pərˈsepträn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import ListedColormap
import Perceptron as perceptron_class
df = pd.read_csv('D:\Pycharm\Projects\Perceptron_1\iris.data', header=None)
#print df.tail()

#抽取出前100条样本，这正好是Setosa和Versicolor对应的样本，我们将Versicolor对应的数据作为类别1，Setosa对应的作为-1。
# 对于特征，我们抽取出sepal length和petal length两维度特征，然后用散点图对数据进行可视化

y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [0, 2]].values
# plt.scatter(X[:50, 0], X[:50, 1],color='red', marker='o', label='setosa')
# plt.scatter(X[50:100, 0], X[50:100, 1],color='blue', marker='x', label='versicolor')
# plt.xlabel('sepal length')
# plt.ylabel('petal length')
# plt.legend(loc='upper left')
# plt.show()

#这里是对于感知机模型进行训练
ppn = perceptron_class.Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)

#画出分界线
def plot_decision_regions(X, y, classifier, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
    np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
        alpha=0.8, c=cmap(idx),
        marker=markers[idx], label=cl)

plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()