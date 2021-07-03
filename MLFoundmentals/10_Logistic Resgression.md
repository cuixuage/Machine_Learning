# how can machines Learn

1. Logistics regression逻辑回归   
https://wizardforcel.gitbooks.io/ntu-hsuantienlin-ml/content/11.html
https://huxuzhe.github.io/2018/11/20/    Logistical-regression-%E9%80%BB%E8%BE%91%E5%9B%9E%E5%BD%92-%E5%85%AC%E5%BC%8F%E6%8E%A8%E5%AF%BC/   
核心点:   
i.score function和线性回归、线性分类算法一样，都是使用W*Xi   
ii.激活函数是sigmod，求其一阶导数函数   
   
# 逻辑回归
*问题定义*
e.g. 0/1的资料data下,计算患者有多大的几率患心脏病？
soft binary classification

*基础准备*
logistic function: 用来将加权score 分布到(0,1)之间
区别linear regression得到结果output范围是整个实数空间
相当于sigmod激活函数
形式: h(x) = 1 / 1+exp(-S)   S=WT*x

*Logistic Error*
最大似然性得出的Error衡量被称作cross-entropy error

将P(+1|x)作为目标函数  将θ(WTX)作为hypothesis  在通过似然性作为Ein评判
==> hypothesis 和 target function最大似然likelihood
连乘符号
==>max likelihood 课件P12
==>min 1/N err(w,xn,yn)
目标:  寻找w使得Ein最小  对上式求一阶导数

==》最终梯度表达式:  课件P23

*W更新*
课件P33
基于梯度下降的逻辑回归算法:
1.初始化w0
2.计算梯度 ▽Ein(wt) = 公式(变量是wt、 xn 、yn)   详细理解：课件11节 随机梯度SGD？？
3.迭代更新 Wt+1 = wt - λ▽Ein(wt)
4.▽Ein(wt)梯度=0 或者 足够迭代次数结束


```python
"""
note:
1.逻辑回归的error function,称之为cross-entropy error

2.Weight向着梯度的反方向更新
画图理解 convex凸函数(纵坐标是Ein error,横轴是Weight迭代轮数)

3.output yn
yn = θ(d+1 weight vector * Xn)  yn∈(0,1)
θ函数logistic function
"""
```
