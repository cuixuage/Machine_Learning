# Gradient Boosted Decision Tree
# 将Adaboost延伸到GBDT
# gradient boost不断迭代,做residual fitting

*Adaboost DecisionTree*
每轮bootstrap得到D'的样本有不同的权重re-weight,通过DecisionTree训练得到的gt,
gt分配不同的权重α得到G
问题: 
Ut如何在DecisionTree体现？
e.g. 在SVM中,Ut是对于regularizer/Error的权重
在DecisionTree中如果对于当前分支的犯错误点加以Ut的惩罚权重过于复杂,所以根据Ut对于Drain进行re-sample
总结: Adaboost-DecisionTree结合了这两者,唯一改变就是weighted samppling替代权重Ut
关键点:
如果使用完全长成的树,会导致Ein(gt)=0,方块t=∞,导致权重ln(方块t) αt=∞
1.pruned Tree('week' Tree)
2.或者限制树的高度
AdaBoost-DTree = Adaboost + weighted-sampling(Ut) + PrunedTree

*Optimization of Adaboost*
e.g. binary classification
1.voting score
Ut+1=1/N*exp(-yn*sum(αtgt(xn)))
其中αtgt(xn)称之为voting score,相当于该点到分类边界的一种衡量。随着voting score越大,Ut+1越小,所有Un(t+1)之和应该也是最小的
==> 目标:在t+1轮,所有样本的Un(t+1)之和尽可能小
2.ErrADA
ErrADA = exp(-ys),s是voting score. 此函数是err0/1的上界
3.gradient descent
对ErrADA做梯度下降处理。注意公式中gt是函数 而非以前遇到的Weight vector
结论:  optimal 小矩gt就是ErrADA梯度下降的反方向
得到gt即确定了梯度方向,再选择合适的步长η,使得ErrADA取得最小值
==> after finding gt,寻找η使得ErrADA最小
推导得到 steepest decent = α = ln(方块t)
结论:
Adaboost其实在梯度上找到下降最快的方向(gt)和最大的步进长度(αt)
==AdaBoost中确定gt和αt的过程就相当于在gradient descent上寻找最快的下降方向和最大的步进长度

*Gradient Boosting*
regression Gradient Boosting
经推导,最小化Err要求=> h(xn)尽可能接近余数yn-sn => squared Error来保证两者尽可能接近
如何引入DecisionTree？
在对于N个点(xn,yn-sn)做squared-error时,使用C&RT做regression
```python
"""
GBDT算法流程:
sn初始值全部设置为0
for t=1,2,3...,T:
    1.通过C&RT算法做regression得到方向函数gt
    2.αt通过单参数线性回归(gt(xn),yn-sn)求解
    3.更新sn=sn+αtgt(xn)
return sum(αtgt(x))
"""
```
GBDT相当于Adaboost-DTree的regression版本

*各类模型总结*
1. blending建立在多样性的gt已知的前提下
2. Learning边学习gt边结合gt:
2.1 bagging 通过bootstrap得到不同gt,计算gt voting/average
2.2 AdaBoost 通过bootstrap得到不同gt,计算gt线性组合
2.3 DecisionTree 通过数据分割得到不同的gt,非线性组合gt
3.GBDT
将Adaboost延伸到GBDT,使用residual fitting解决regression问题
GBDT = GradientBoost + DTree
RandomForest = Bagging + "strong" DTree
AdaBoost-Dtree = AdaBoost + "week" DTree  (sampling and pruning)
4.
我们从binary
classification的0/1 error推广到其它的error function，从Gradient Boosting角度推导了
regression的squared error形式。Gradient Boosting其实就是不断迭代，做residual
fitting。并将其与Decision Tree算法结合，得到了经典的GBDT算法
