1~2: 计算错误率
题目: 近似函数h来当做目标函数f,输出错误的概率是μ。 如果使用h近似含有噪声的目标函数f.噪声的分布p(y|x) = λ, y=f(x)(预测正确)
则错误情况分为两种:
1.1. h=f时,f≠y。 P= (1-μ)*(1-λ)
1.2 h≠y时,f=y。 P=μλ
P_error = p1+p2 = 相加化简 = (2λ-1)μ - λ + 1. 当λ=0.5时 似然函数的h和μ无关

3~4
概率的计算
已知dvc=10,泛化误差Eout Ein的差距不超过0.05的概率大于95%,计算至少需要多少的N样本数量？ 
通过vc bound函数计算得到46w左右数据量

其他多种bounds准则 来通过dvc N 来计算泛化误差的上界
e.g. origin VC bound
    Rademacher Penalty bound

**后面题目我没有做**

参考链接:
https://acecoooool.github.io/blog/2017/02/07/MLF&MLT/MLF2-1/
