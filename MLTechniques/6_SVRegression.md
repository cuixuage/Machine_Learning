# support vector regression

*基础*
对于任何包含正则项的L2-regularized linear model,其最优的W* 都可以写成Z的线性组合
如何将kernel引入ridge regression中,squared error
==>
关于βn的最优化问题
类似于linear regression"一步登天", βn=公式P2,dense matrix
通过kernel来解决了non-linear regresssion
==>
linear regression、kernel regression比较,平衡效率和灵活
kernel对于大数据N,计算的复杂度很大

*LSSVM*
将kernel ridge regression应用于classification,least-squares最小平方差
区别:
soft-margin gaussian SVM: αn大部分是零,SV个数较少
gaussian LSSVM: βn非零,dense matirx,SV个数较多。导致矩很大,降低计算速度
我们更常用soft-margin SVM做分类

*LSSVM改进*
稀疏化βn,减少support vector
tube regression在分类线上划定中立区,只有中立区以外的样本点才算error
==>
*linear SVR,使用errtube,转换为QP问题进行求解*
