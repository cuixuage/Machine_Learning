# linear model for multiclassificatin
*问题定义*
linear regression 和 logistic regression 都是convec 函数,具有最小解
这两者也都是linear classification的upper bound上界函数
note:
对logistic regression进行缩放,将ln替换成log2

*基础*
三种线性模型的 Error function
关于ys变量,其物理意义是分类正确的得分

*SGD*
stochastic gradient descent随机梯度下降
目的: 逻辑回归算法每次迭代需要计算N个点, 减少计算,random选择一个点作为作为整体的梯度
▽Ein(wt) 1/N的连加  替换成  xn yn点的梯度
==>online学习 ==>缺点不够稳定
note:
1.终止条件需要迭代次数足够多
2.线性回归的W0(很快就能计算得到)  作为 pla/pocket/logistic初始值
3.可设置学习速率=0.1


*多分类问题*
1.OVA
one-versus-all 一对多分解
soft-二分类 使用k次logistic回归,最终选择概率最大的类别
缺点: 每次二分类时,正负类的数据量不平衡,最终分类效果不太好
e.g. 100份类别,每个类别的样本数量相同情形

2.OVO
one-versus-one 一对一分解
每次只选择两种类别进行分类,最终选择所有分类器中最多分类器选择的类别
e.g. 6种类别需要计算30次分类器
缺点: 空间复杂度更高,一般比OVA更快


*总结*
1.线性分类,线性回归,逻辑回归
2.SGD来替换梯度下降
3.multiclass classification
