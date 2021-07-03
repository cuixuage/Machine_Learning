# how can machines Learn   
    
https://wizardforcel.gitbooks.io/ntu-hsuantienlin-ml/content/10.html      
MSE作为Loss函数，最后计算w的偏导数为零的情况    
    
# 线性回归   
*问题定义*  
use hyperplanes to approximate real values  
与线性分类不同,h(x)预测值在整个实数空间   
目标: 预测值和真实值差距最小,residuals残差最小。采用平方差squared error衡量  

*线性回归Algorithm*   
1.平方差Ein  
Ein = 1/N ||X*w - y ||的平方   =》 convex凸函数  =》一阶导数为零  =》最优解  
 
2.▽Ein   
Ein的偏导数function ==》课件P10   
▽Ein=0 推导出W 的表达式  ==》课件P11   
Wlin = (XT * X)^-1 * XT * y (矩阵X的伪逆矩阵 pseudo-inverse)    
   
**3.算法流程**   
3.1   
input matrix X 的形状 N*(d+1)  
output vector y 的形状 N*1   
3.2    
计算 pseudo-inverse X+  的形状 (d+1)*N    
3.3     
得到最佳Weight= X+ * y。Wlin 的形状 d+1维    
     
==》 Hypothesis predictions yn = Wlin * xn     
   
*4.泛化问题*    
hat matrix：X*X+   
预测值y = XX+ * y   
*Eout-Ein = 2(d+1)/N   N越大两者之间的差距越小*   
    
*5.回归和分类*  
```python
"""
1. linear regression得到的Wlin,可以作为PLA、pocket算法的初始weight
2. 线性回归的方法用来解决线性分类问题而且效果不会太差
3. NP-hard的min error的分类问题得到一个更加宽松的上界 也是更有效率的求解方式 
4. 数学原因: 
平方误差squared err 是 err0/1的上界 
"""
```
  
