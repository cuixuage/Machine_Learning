# why can machines Learn?   
  
1.Noise   
结论: 如果存在noise vcdimension依然成立  
noise满足分布P(y|x)  
  
**2.pointwise error**    
对于数据集中的每一个点计算错误  
错误衡量方式：  
2.1 avg 通常用于分类classification问题  
2.2 squared error通常用于回归regression问题  
==》通过错误衡量 来判断当前矩的评判  
  
3.错误类型  
false accept 预测值将负类当做正类; false reject预测值将正类当做负类  
==》对于CIA安保 false accept的惩罚权重要加大  
  
4.weighted classification  
PLA:  virtual copying  
对于error惩罚权重的mistake 进行相应倍数的计算  
  
结论:  
机器学习cost function常用 0/1error 和 squared error   
