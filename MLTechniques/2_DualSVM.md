# SVM对偶问题
非线性SVM在Z域空间的维度可以被设计的很高,如果模型越复杂那么Z域的d+1越大
*如何求解非线性SVM二次规划时,不依赖Z域的维度呢？*

*对偶问题*
origin SVM: 变量个数d+1,限制条件N(每个点都要被正确分类)
equivalent SVM: 变量个数N,限制条件N+1

*推导*
1.构造拉格朗日函数
SVM目标1/2WT * W + sum(αn*约束条件 1-yn(WT *Zn + b))
约束条件: yn(WT*Zn + b)>=1
2.构造非条件问题
对拉格朗日函数执行min(max L_funciton) <==> 原目标min 1/2WT*W
SVM = min(b,w) (max L(b,w,α)) 证明: 课件P6
3.min max对调
原式 >=max(min L_funciton)
lagarange dual problem,QP转变成强对偶问题
原式 ==max(min L_funciton)
4.梯度求导
初始条件αn>=0;分别对b,w计算微分;课件P6"哈利-伏地魔"条件
KKT- Karush-Kuhn-Tucker条件
5.QP二次规划
只和α有关的SVM目标式子;QP计算拉格朗日因子α
参数b通过某一个support vector(α!=0的点)
dense稠密的q矩阵,一般使用QP的special slover

*其他*
1.support vector
"哈利-伏地魔" 两个条件至少有一个为零
当αn>0时,1-yn(WTZn+b)=0成立。此时这些点一定落在 fat boundary上 
只有support vector才支撑起fat boundary,有物理意义
2.Dual SVM
一般当N不是很大时,一般使用Dual SVM求解问题
3.Z域d+1
我们并没有真的消除掉d的依赖,因为我们计算二次规划的Q时引入的变量Z,Z包含了d的维度

*总结*
1.引入拉格朗日因子α,转为min max非条件形式
2.只和α有关的SVM目标式子
3.QP计算拉格朗日因子α
4.通过KKT条件,反解w,b
