# random forest
bagging 通过bootstrap从原始数据集中re-sample获取不同的gt
Decision Tree 是利用分支条件将原始数据集分割成子树结构
bagging减少不同gt之间的方差,而DecisionTree完全长成的gt方差很大
*random forest将bagging和decisionTree相结合,达到优势互补的目的*

1.RF=bagging + fully-grown C&RT
G=uniform{gt} 对于所有的C&RT进行voting or average
C&RT是在Dtrain中re-sample的部分数据集上训练,返回gt

2.RF=bagging + random-subsapce C&RT
随机抽取资料 + 随机抽取d'特征来得到多样性的gt
note: 随机抽取特征来建立C&RT,相当于X域d维到d'维的特征转换

3.RF=bagging + random-combination C&RT
现有特征进行线性组合,每次分支得到的是各种子特征的线性组合(有权重)
每次只选择一部分特征做线性组合

*out-of-bag*
bagging操作中没有被涵盖的样本可以用来做self-validation
e.g. bootstrap的次数N'=N,每次选择一个样本,则某个样本OOB概率= 1/e 约等于 1/2.72
note:
1.Dataset切割出validation选择最优gt,需要将全部数据集重复一次得到最终G。而random forest采用Eoob来评估gt,最后并不需要重复训练
2.Eoob计算
课件P9  
(xn,yn)在RF中所有子树C&RT中没有作为分支条件,那么(xn,yn)是此子树的out-of-bag样本

*feature selection*
目的: 删除冗余特征和不相关特征
方法: 将特征的重要性进行排序 ==> 如何计算feature的重要性？
1.线性模型通过Weight即可获得
2.非线性模型例如RF如何计算？
permutation-test
将N个样本的第i个特征重新随机排列,如果模型前后表现performance差距很大,说明该特征是重要的。
3.衡量performance？
天真想法: 对于重新洗牌第i个特征后重新训练得到G,再通过Eout比较前后两种模型
缺点: 繁琐耗时需要不断重复训练
改进: Eoob相当于validation,将oob样本进行重新洗牌第i个特征,再评价G
优点: 应用广泛

*总结*
1.三个直观样例都说明足够多的随机森林模型的稳定越好,更平滑,margin越大
2.RF将众多的decisionTree进行投票做分类结果
3.三种random操作使得RandomForest更加强大
*4.通过permutation test来进行feature selection*
