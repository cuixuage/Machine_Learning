# kernel logistic regression-KLR
通常使用 soft-margin Dual SVM

*L2 regularizer comparison*
惩罚项ξn通过 max(1-yn(WTzN+b),0)替换,类似于错误估计err
note:
1.hard-margin目标是最小化WTW,条件是Ein=0;
2.regularization目标是最小化Ein,条件是WTW<=C
==>
构造拉格朗日函数,将目标和约束条件相结合。这两者是类似的
3.large margin = fewer hyperplanes = L2 regularization of short W
regularizer_C,soft-margin_C越大,相当于更小的regularization,更容易过拟合

*SVM扩展logisticRegression*
Err_svm 定义为最优化问题后面的第二项,惩罚项
Err_svm 是convex函数;是err0/1的上界函数;和以log2为底的logistic Error function接近
1.两种简单思路 课件P11
*2.添加缩放因子A,平移因子B*
(bsvm,Wsvm)来建立加权分数值,乘以缩放因子A,加上平移因子B,随后使用θ function分布
两个未知参数A,B,通过Z域空间运行logistic funciton来确定A,B
核心: 通过Z域空间计算kernel SVM来求得Logistic function的近似解
*3.通过kernel直接Z域计算LR*
经证明,任何L2-regularized linear model都可以使用kernel来解决(课件P16)
最佳解W*一定是Z的线性组合,将kernel引入logistic,
W* = sum(βnZn),转换为QP二次规划求解βn的问题
note:βn大部分不为零,而SVM的αn大部分都是零(support vector的αn!=0)
βn非零相当于计算代价
