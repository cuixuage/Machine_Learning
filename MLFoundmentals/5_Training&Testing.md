# why can machines learn?
*Training and Testing*  

*机器学习的核心问题:*
1.Ein(g) ≈ Eout(g)
2.Ein(g) ≈ 0
e.g. PPT 第五章P4

**核心: 证明M数量是有限的 （M是发生bad data的Hypothesis数量）**
**idea: 过度估计 over-estimating 有许多的Hypothesis交集**

1.二分类
Dichotomy H将平面上的N个点用直线分开,可以将H分成不同类型的Hypothesis
try:
将dichotomy H来替代之前可能是无限的M

2.成长函数
growth function mh(H)。 对于N个点组成的不同集合,其中最大数量的Dichotomy的上界
== effective lines数量最大值
== 最多能分成几种类别的Hypothesis
2.1 一维 Positive Rays O(N)
mh(H) = N+1  << 2^N
2.2 一维 positive intervals O(N^2)
mh(H) = 1/2*N*N + 1/2*N + 1  <<2^N
2.3 二维 convex sets (2^N)
mh(H) = 2^N
2.4 2D Perceptrons感知机  (小于2^N)

3.break point
*shatter: every dichotomy can be implemented  hypothesis被分成2^N中情况*
某一个点无法将Hypothesis分成2^N

总结: 用成长函数mH  来替代原有的霍夫丁不等式的M(可能无限的Hypothesis数量)
==》 从而满足了机器学习的条件
