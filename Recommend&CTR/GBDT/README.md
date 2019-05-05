0.训练过程
"放大"错误样本,基学习器的个数==训练的迭代次数

1.输出形式
二分类:
每个基学习器输出one-hot向量(长度==num_leaves)
one-hot to int
prediction = num_boost_iteration个整数(每个整数是来自一个基学习器的输出)

思考: 
1.多分类 || 回归
GBDT的树的输出还是one-hot吗？？  
2.第一个基学习器的特征的最明显,最后一个基学习器的是分类结果最准确的 ？？？（每棵树会不会用到同一个特征呢）


2.FM
输入:libsvm格式,index:value
对于GBDT的int输出加以offset([我的CSDN博客](https://blog.csdn.net/u014297722/article/details/89293404))

3.其他问题:
Xgboost: 输入的类别特征如何指定？（lightgbm指定类别特征十分方便）