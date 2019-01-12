# adaptive boosting 自适应的提升

*基础*
Ui作为犯错样本的权重因子,base algorithm来最小化包含Ui的error funciotn
Ui越大则惩罚多大,最小化error更需要重视这些点
类似于基石课程中的 example-weighted learning

*diversity by re-weighting*
通过放大和缩小weight的思想,第t轮将犯错的Ui和正确分类的Ui做乘积操作,使两者值变得相等
更新惩罚因子Ut,re-sample时来获得不同的gt
e.g.
1.对于SVM,对于其Error惩罚项ξ乘以权重因子Un,那么最后αn的上界变成C*Un
note: Unt+1是通过上一轮Unt计算得到的
2.对于logistic regression,基石第八讲Un改变每次采样的权重

*Adaptive*
通过不断迭代计算gt+1,不断组合G  ??
新的尺度因子 方块t
==> 放大错误点  scaling-up incoorrect来保证得到不同于gt的gt+1
每次迭代,利用方块t将Ut更新为Ut+1
1.初始值?
保证Ein最小, U=1/N 
2.如何聚合G(x)?
gt+1是在gt基础上得到的,一般使用linear,non-linear组合

*Aggregate on the fly*
线性组合时,如何在计算gt时就得到权重系数α？
α = ln(方块t)
含义: 
预测错误率=1/2,则方块t=1,则矩gt相当于random,则α设置=0.
预测错误率趋于零,则α趋于无限大
```python
"""
Adaboost算法流程:
1.获取矩gt,gt是不同Ut下re-sample不同
2.更新Ut为Ut+1,Ut+1=Ut*方块t or Ut+1=Ut/方块t。 方块t = 根号下((1-错误率)/错误率)
3.聚合时权重α=ln(方块t)
return G(x)=sign(sum(αt*gt(x)))
"""
三个核心部分:
1.base algorithm A,相当于学生
2.re-weirhting factor方块t,相当于老师,来放大错误
3.linear regression αn,线性聚合gt
```

**总结**
1.如何获取多样性的矩？
Un改变正则项的权重 or 改变采样权重
2.如何聚合多样性的矩？
Adaboost线性组合小矩,即时计算权重系数α=ln(方块t)
