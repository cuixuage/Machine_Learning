# how can machines learn by distilling hidden features?
# RBF NNet计算样本之间的distance similarity的gaussian函数来替代神经网络的神经元

gaussian kernel = radial basis function kernel
radial径向距离 表示gaussian函数计算结果只和support vector有关

*RBF NNet*
将radial Hypothesis进行linear aggregation
Hypothesis 和 NNet work定义  课件P4
给定RBF和output计算函数,来决定中心点位置μ和权重系数β

*RBF Net learning*
每一个样本点都是中心点,称之为Full RBF Network
full RBF network实际应用不多
但是计算量比较大,往往只有距离x最近的样本点对于x的影响值较大。不如选择k个邻居来得到最终矩
k-nearest-neighbor

*K-means algorithm*
核心:  两组变量交替的更新
分类的分群值Sm,每一类的中心点Um
1.随机选择k个中心点
2.再由初始确定的中心点得到不同的类群(所有的点计算自己的归属类群Sm)
3.每个类群更新自己的中心点(该类群的均值)
4.继续循环迭代计算,交互地对和S值进行最优化计算,不断更新和S值,直到程序收敛,实现Ein最小
note:
1.K-means 对于初始选择的类群个数k值敏感
2.将K-means应用到RBF Network中,合理的k值即可分类效果不错

*总结*
RBF NNet计算样本之间的distance similarity的gaussian函数来替代神经网络的神经元

*exacts Gaussian centers by k-means and aggregate the Gaussian linearly*
