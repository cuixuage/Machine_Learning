# 验证集validation

1.Dataset分为Dtrain,Dval
通过Dval当做Dtest,选择Eval最小的Hypothesis,再将Hypothesis在全部训练集合Dataset训练

2.leave-one-out cross validation
每次只留下一个点做为验证集合,循环N次。再将验证集合的Eval做平均

3.V-fold cross
e.g. 将V设置为10,固定10份。 cross交叉验证
