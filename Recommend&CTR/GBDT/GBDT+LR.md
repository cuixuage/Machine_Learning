# 0. 基础准备     
论文: Practical Lessons from Predicting Clicks on Ads at Facebook     
参考资料:   
https://github.com/aragorn/home/wiki/Study-:-Practical-Lessons-from-Predicting-Clicks-on-Ads-at-Facebook   

https://zhuanlan.zhihu.com/p/34770123   

https://blog.csdn.net/Dby_freedom/article/details/84971658

```
把GBDT看作特征的转换器，从树根到叶子的路径，可以理解为特征的规则。
把转换后的特征向量输入到线性分类器中，本质上是学习这些规则集合的权重.
```

# 1.论文阅读   
1.1. GBDT特征转换   (连续特征离散化,构造组合特征)
1.2. LR对于GBDT的输出one-hot特征做权重训练   
1.3 评估data fressnes   
1.4 评估用户历史特征（特征重要性排序topK 75%） 和 上下文特征   
NOTE: 少量的特征贡献了大部分的模型影响力
NOTE: 上下文特征对于冷启动问题很有用
1.5 negative down sampling   
e.g. 统一子采样 (10%的统一采样率即可收敛~,性能降低1%)
e.g. 只对于负样本采样（目的: 样本类别的平衡性问题 + 减少样本训练时间）   
 
   
# 2.思考   
2.0 连续特征离散化（方法1: mmr 确定离散的边界 方法2:k-d树）
2.1 LR的权重个数等于GBDT树的个数,还是所有叶子节点的个数？？    
2.2 GBDT特征的重要性是如何评估的？？   

2.2 负采样后的CTR如何转化到原样本空间？？   
q = p/(p + (1-p)/w) 
p是采样空间的CTR,w是采样率。 q是近似于真实空间的CTR值

2.3 归一化的交叉熵计算？？   
   
# 3.代码实现   
https://zhuanlan.zhihu.com/p/37522339    
https://github.com/wangru8080/gbdt-lr?tdsourcetag=s_pctim_aiomsg   