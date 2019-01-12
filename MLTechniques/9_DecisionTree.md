# classification and regression Tree(C&RT)

*对比聚合模型*
课件P2
aggregation分为:uniform,non-uniform,conditional
uniform: voting/averaging = bagging
non-uniform: linear = Adaboost
conditional: stacking = Decision Tree

*CartTree 基础*
DecisionTree: 分支个数,分支条件,终止条件,基本的算法(叶子节点)
cartTree:
1.分支个数=2, binary Tree二分查找树
2.gt(x)是常数constant,树的叶子
C&RT: 分类问题选择占比例最多的yn; 回归取所有的yn平均值
Decision Tree通过递归形式构建(注意终止条件)

*impurity 不纯度*
课件P10
分类问题常用Gini index: 1- 所有类别占据样本N的比例平方和
回归问题常用: squared-error
note:
1.使用purify来选择最佳的decision stump
分支条件通过分类后的纯度选择:将分类后的两部分数据集按照比例分配对应的权重,选择最小的不纯度的Hypothesis作为分支条件
2.“被迫”终止条件
Yn都是同类 or Xn特征全部相同

*Trick巧思*
1.regularizer
pruned修剪。从fully-grown tree中不断减少叶子,通过validation选择这些所有的gt中最优的Tree
2.categorical  features
类别特征如何处理？  将某几类归为一颗子树,剩下的归为另外的子树
3.缺失特征
使用相似的特征替代。如果两个feature的切割结果是类似的,那么第二个feature保存下来,遇到第一个feature缺失情况使用第二个feature替代
4.efficient non-linear training and testing

*对比*
1.Decision Tree是有条件下的直线切割,Adaboost是线性组合
课件P18   图形化不同
