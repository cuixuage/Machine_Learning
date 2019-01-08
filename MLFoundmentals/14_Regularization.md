# 约束weight vector规则化

*限制性*
限定Weight中非零元素的个数  ==》限定Weight的平方和小于等于某个阈值
即: ||W||^2 = WT*W <= C,对应记为H(C)
当C无限大的时候,相当于没有加上任何限制,regularized Hypothesis Set
满足限定条件的W,记为Wreg
note:
*约束描述: Ein最小的情况下,加上限定条件H(C). 求解最优的weight*

*最终公式*
图形理解: 终止条件 -▽Ein的方向和W的法向量的方向平行
拉格朗日比例尺
-▽Ein(Wreg) = 2λ/N * Wreg, 求解线性方程,得到Wreg
note:
约束问题相当于在原有的min Ein error问题上,新添加一项regularizer λ/N*Wt*W

*结论*
λ∈[0,1] λ越大,给高阶值更大的惩罚,Hypothesis希望得到更短的W,相当于约束值C更小

*通用约束化*
在Ein最小的情况下,加限制条件Ω(w)<=C
相当于回降VC dimension

1.L2 regularizer(更常用)
Ω(W) = ||W||^2,计算W的平方和,convex funciton
2.L1 regularizer
Ω(W) = ||W||,计算W的绝对值和,围成正方形,解释稀疏的,计算速度快


如何选择合适的λ建立最优的Hypothesis？？  下一节课
