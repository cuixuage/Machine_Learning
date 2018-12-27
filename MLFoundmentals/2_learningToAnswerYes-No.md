# When to use ML
learning to answer Yes-No  二元分类问题
感知机算法

1. Hypothesis
选择最佳的H对应的函数作为target function。H在二维平面上相当于直线

2.PLA思路
随机起点  不断修正mistake直到没有mistake
注意: 分类正确也会做修正(加速收敛)
note:
实际操作中，可以一个点一个点地遍历，发现分类错误的点就进行修正，直到所有点
全部分类正确。这种被称为Cyclic PLA

3.PLA停止
非线性可分数据==>PLA不会停止
3.1证明PLA停止
1.如果Wf有效更新
==》WfWt的内积会越来越大
需要证明：  Wf*Wt+1 > Wf*Wt
2.证明内积的增大和长度无关
如果令初始权值，那么经过T次错误修正后:
Cosθ(Wf,Wt) >= T的根号 * constant

4.非线性可分数据
=> 我们可以认为数据集中加入了噪声noise
=> 不要求每个点都分类正确而是容忍有错误的点,取错误点个数最少的Wf
=> Wg = Min(yn != sign(W*Xn))
=> NP-hard问题

packet-algorithm
足够多次迭代中选取最好的分类直线
note:
packet算法慢于PLA的原因:
1.packet需要额外的存储
2.packet每次修正后 都需要遍历所有点来判断当前的分类直线
