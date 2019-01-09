# soft-margin
目的: 允许存在noise,总共的违反margin值尽量少

*基础*
1. ξn,来记录每一个点犯错误的程度值,ξn>=0
2. 超参数C,Sum(ξn)的权重,C越大则违反边界值越小,margin越窄;  反之,margin更宽,更不容易overfit

*对偶问题*
soft-margin SVM的dual problem
1.两个约束条件,添加到拉格朗日函数中,所以有两组因子 = αn和βn
2.对参数ξn,参数b,参数w微分+两个"哈利-伏地魔"条件 = KKT条件
3.几乎和hard-margin对偶问题一致
区别: αn∈( 0,C ) ; βn=C-αn
4.二次规划QP求解拉格朗日因子α
5.note:
参数b "哈利-伏地魔"条件
参数b求解类似于hard,只不过需要寻找free support vector代入等式 
free support vector是α∈(0,C)此时ξ=0的support vector

*支撑向量*
1.Non-SV
α=0,导致ξ=0的点. 这些点是分类正确的点(or刚好位于fat boundary)
2.free-SV
α∈(0,C),导致ξ=0的点. 这些点刚好位于fat boundary
3.bounded-SV
α=C,ξ=1-yn(WTZn+b). 这些点是分类错误值为ξ的点(ξ=0,分类正确刚好位于fat boundary;)

*高斯kernel+soft-margin*
这是最常用的SVM形式,超参数是C和γ。
其中C,γ越大,越容易过拟合。
==》
cross-validation
support vector越多,Error-leave-one-out上界越大,越容易过拟和。

*总结*
1.我们增加ξn作为分类错误的惩罚项,超参数C平衡目标和惩罚项。推导出soft-margin
SVM的二次规划QP形式。得到拉格朗日因子αn需要满足上界C
2.区分三种support vector
3.通过cross-validation和SV数量选择合适超参数
