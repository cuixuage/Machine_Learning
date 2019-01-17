# 终曲 finale
*feature exploitation techniques*
特征提取
1.kernel
polynomial,gaussian,stump. kernel相加或者相乘,满足Mercer condition
处理非线性问题
2.aggregation
blending(已知矩,三种方式).  bagging adaboost decision Tree(未知矩)
3.hidden features
NeuralMetwork(adaboost),RBF Network(k-means),Matrix Factorization(autoencoder)提取hidden features隐藏特征
or compress raw data(维度压缩 PCA)

*optimization techniques*
1.gradient descent
SGD,steepest descent,functional GD都使用了梯度下降的技巧
对于更复杂的最优化问题,无法直接使用梯度下降来完成,需要数学推导:
e.g. Dual SVM,kernel LogReg,kernel ridgeReg,PCA
2.multi-stage
将问题划分多个步骤求解以简化计算
或者交叉迭代优化,alternating optimization

*overfitting*
1.large-margin,denoising,pruning
SVM,adaboost,autoencoder,decision tree
2.L2 regularizer,weight-decay,early stopping
SVR,kernel models,Neural neteork
3.voting/averaging,constraining
blending,bagging,random forest,autoencoder(weights),RBF(centers)
note：
使用validation消除overfitting
e.g. Support vectors, OOB(random forest),internal validation

*machine learning in action*
1.介绍林轩田老师在近几年的KDD CUP所使用的思路
2.最常见的十大数据挖掘算法 课件P8
3.机器学习的jungle 课件P10
