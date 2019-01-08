# 过度拟合的危害  
  
*定义*   
bad generation某一点Ein趋于零,Eout非常大   
overfitting: Ein很小Eout很大   
造成过拟合的主要因素:   
VC Dimension自由度,Noise噪声,N训练样本数量  
Noise分为:stochastic noise随机和 determinstic noise确定性   

*Learning Curve*
横轴是样本数量N,纵轴是Error
纵轴NoiseLevel,横轴N 的overfitting程度的描述图形
纵轴TargetComplexity,横轴N 的overfitting程度的描述图形
note:
目标(真实的)函数target function复杂度很高 <==> 当做noise理解
determinstic noise 类似于伪随机数发生器

*compat overfitting*
1.start from simple model
2.data cleaning/pruning
3.data hinting
4.regularization
5.validation

本节课只讲了前三种避免过拟合的方法
note:
1.data cleaning/pruning就是对于数据集中明显错误的label样本进行修正,或者剔除
2.data hinting是数据提示,类似于数据增强？
对于样本数据不够多的情况下,进行平移或旋转,从而获得更多样本(virtual examples)
