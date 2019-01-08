1.determinstic noise的理解
值越大,Hypothesis的维度越低,即和target funtion接近程度越低
3.正则项  λ/N*(WT*W)
4.Wreg是关于λ的非增函数
9.hoeffding不等式 2exp(-2  N)
11~12. virtual examples虚拟样本 data hinting

13~20编程作业:
1.regularizer
linear regression的正则化regularization
通过公式求解Wreg
2.leave-one-out
验证集选择lamda集合中optimal λ,再重新计算Wreg
3.V-fold cross
交叉验证,注意Cross计算
