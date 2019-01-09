# embedding numbers features:kernel models
support SVM
*从视觉的角度使得所有的点离直线尽可能远,再通过推导margin,转化为求解二次规划的问题*

*基础*
fatness: 距离直线距离最小的点的distance,称之为margin
目标: Max margin
约束条件: hard-margin,每一点都分类正确(真实值预测值相同),即 yn(WTXn)>0
w = (w1,w2,w3,w4.....)
b = w0

*推导*
1.
distance(x,b,w) = 1/||W|| * |Wtx + b| ==> 1/||w|| * yn(WTXn +b)
2.
缩放,令距离最近的点距离满足 yn(WTXn +b)=1。目标转化为 Max 1/||w||
3.
新的约束
松弛约束yn(WTXn +b) >=1 证明:松弛约束不影响结果
4.
Max转化为 MIn,remove ,add 1/2.    新的目标:Min 1/2*WT*W

*求解*
二次规划QP方程求解
目标是关于W的二次函数,约束条件是关于w,b的一次函数
1.计算对应的二次规划参数 Q,p,A,c
2.根据工具规划库函数,计算w,b
note: 对于非线性问题,W替换成Z,非线性的映射空间

*其他*
1.regularizer 和 hard-margin svm关系
正则化: minimize Ein, WTW<=C
向量机: minimize WTW, Ein=0（hard-margin）

2.large-margin
得到的二分的种类的变少,VC Dimension(break point前一点),拥有更好的泛化能力
