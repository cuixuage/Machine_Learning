# 如何将不同Hypothesis和features结合起来
# Aggregation Models
Aggregation两个优势:features transform和regularization相结合

*uniform blending*
1.classification,每一个矩同权重下进行投票
2.regression,所有矩gt的预测值求均值 
理论:弱化方差variance影响 
(bias偏差=所有gt达成的共识,variance方差=所有gt意见不同的程度)

*linear blending*
利用validation从Dtrain中得到g1,g2....gt. 代入linear blending迭代计算最优的αn权重系数
αn 取值范围在整个实数空间
note:
1.类似于 two-level-learning的思路
2.any blending是可以采用任意形式来堆积小矩gt
==> 得到线性或者非线性的Hypothesis组合

*Bagging*
如何利用一份数据集来构造不同形式的gt？
通过bootstrapping思路,有放回的re-sample样本数据
e.g.
通过bootstrapping得到25个不同的样本集,再使用packet得到25个不同的gt
最后使用blending,将所有gt融合起来
note: 当演算法对于数据的分布比较敏感的情况下才有比较好的表现

*总结*
1.blending就是将已经得到的矩gt进行线性or非线性aggregate操作。
2.bagging从已有数据集模拟其他类似的样本来得到不同的gt
(如果没有那么多bootstrap,通过已有数据集得到新的数据集构造不同的gt)
