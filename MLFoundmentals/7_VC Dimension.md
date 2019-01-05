# why can machines Learn?
VC bound and VC dimension
*shatter: every dichotomy can be implemented  hypothesis被分成2^N中情况*

1.VC dimension定义
maxium non-breakout point
VC Dimension = break point -1 
假设空间H有break point k,且N足够大,根据VC bound理论,算法有良好的泛化能力

2.dvc
当样本集的dvc确定后,就能满足ML的第一个条件Eout = Ein 
这个条件和算法、样本数据分布、和目标函数都没有关系

3.2D perceptrons的Hypothesis维度
经证明: dvc = d+1
dvc等于样本集的维度数目+1  dvc就是Hypothesis的参数的数量 
e.g. H = w0 + w1*x1 + w2*x2 +......+ Wn*xn
e.g. 假如我们固定直线要过原点 w0被固定为0  则Hypothesis的自由度就成为d 而非d-1
**代码实现PLA时候 w0是不固定的 Hypothesis自由度是d+1 = dvc**

4.深入探索Dvc
**Eout(g) <= Ein + model_complexity(N,H,dvc)**
dvc  Ein model_complexity之间的关系
dvc变大 Ein会减小 但是模型复杂度会增大 == Eout并不会一直减小
结论:  随着dvc的增大 Eout会先减小后增大
==》选择合适dvc 
==》选择feature的个数要合适  

5.结论
**选定一个dvc 样本数据D一般选择10倍dvc即可**
1.物理意义: dvc==自由度
2.dvc不能过大也不能过小 才能使得Eout足够小 使得Hypothesis具有良好的泛化能力
