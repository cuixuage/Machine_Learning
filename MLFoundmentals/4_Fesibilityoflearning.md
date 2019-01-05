# 学习不可解性
1. learning is impossible
对于inside有效的algorithm对于outside不一定有效

2.probability to the rescue
Hoeffding inequality 霍夫丁不等书
当N很大时候,V和μ相差很小
结论V==μ叫做PAC probably approximately correct 大概接近的正确

3.connection to learning
Ein(h) 抽样样本中,h(x)和yn不相等的错误概率
Eout(h) 所有实际的测试中,预测错误的概率

4.bad sample
导致Ein 和 Eout差距很大的情况的数据集D,bad data

对于某个h 当N足够大的时候  Ein等于Eout。 PAC
对于h有限的m且N足够大 那么就能保证Ein≈Eout  ML是可行的

note:
当Hypothesis的数量有限,样本数量无限大的时候,不好的数据集出现的概率更低,说明模型的泛化能力不错。

Hypothesis -》矩  e.g. PLA算法中选择的直线函数
(此时Hypothesis是无限大的  这时候霍夫丁不等式还成立吗？ lecture 5 )
