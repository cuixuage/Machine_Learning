# matrix factorization 矩阵因式分解

*abstract features*
e.g. 电影推荐。用户是数字编号,用户对于序号m的电影评分rate
encoding(transform) from categorical to numerical => binary vector encoding
input: N维的binary vector,表示第n个用户。 
output: M维的向量,表示该用户对于M部电影的排名数值的大小。
hidden: 隐藏神经元可以用来表示影片的类型,比如动作,喜剧...

*linear network*
中间隐藏层的转换函数是线性的,其Hypothesis=WT* V *X
其中V的shape是 N*delta, W的shape是 delta*M
weight’s shape是 前一层神经元*后一层神经元

*basic matrix factorization*
目标: 最优化余数的平方差问题
即Rnm ≈ WmTVn,即矩阵R ≈ VTW,
将实际排名情况R分解成两个矩阵（V和W）的乘积形式,称之为matrix factorization
Ein包含了两组待优化的参数,分别是vn和Wm - altering-update
==> alternating least squares
*究竟求解的什么问题？？*
SGD for matrix factorization / time-deterministic

*Extraction Models*
对应关系
adaptive/gradient Boosting<==>functional gradiental descent
neural NNet/deep learning<==>SGD,autoencoder
RBF NNet<==>k-means clustering
matrix factorization<==>SGD,alternating leastSQR

*总结*
我们介绍了基本的Matrix Factorization算法,即alternating least squares,
不断地在用户和电影之间交互地做linear regression进行优化
