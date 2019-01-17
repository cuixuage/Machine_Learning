# how can machines learn by distilling hidden features?
*motivation*
将perceptrons线性组合起来,实现 and or xor等等操作。使用perceptrons足够多可以实现任意的convex set。
计算全连接Weight数目: (weighted神经元+一个常数项神经元)*下一层神经元个数 (不包括常数项)

*Hypothesis*
对于Output层可以选择linear classificatin, linear regression,logistic regression
本节课采用linear regression和squared error衡量
每一个节点对应一个perceptron,都有一个transform运算。
transformation funciton: tanh(s)
tanh(s)是一个平滑函数,类似于阶梯函数。 和sigmod关系是: 2θ(2S)-1

*Learning*
本节课是linear regression的squared error最优化问题
*如何使得最终的output和yn之间误差最小呢？  => 梯度下降 Backprop on NNet*
e.g. 
mini-batch + SGD
对于向前计算时,batch-size数量并行计算. 回溯时只计算batch-size的均值来更新权重Weight

*Optimization Tricks*
1.initialization
weights初始化为 random + small ones
因为large weight,使得tanh变得saturation饱和,梯度很小,weight变化幅度太小,向山谷移动缓慢
2.regularization
L2 regularizer缺点在于只能等比例所有weight,很难得到值为零的权重
而我们希望某些权重为零,使得矩阵稀疏,减小VC dimension
e.g.
使用weight-elimination regularizer
课件P20   Wij**2 / 1 + wij**2
3.early stopping 避免迭代次数过多导致overfitting
4.backprop计算得到每个神经元的梯度,向梯度的反方向移动一定的步长来更新weight


*总结*
原始数据中的模式即特征，简称为pattern feature extraction。
神经网络模型的关键是计算出每个神经元的权重,
方法就是使用Backpropagation算法,利用GD/SGD,得到每个神经元的梯度(从而得到每个神经元的更新方向 + 更新步长)
