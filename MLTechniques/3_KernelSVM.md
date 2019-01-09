# kernel彻底摆脱维度d的关系
# kernel用来解决非线性的问题？？
*基础*
dual svm求解问题转化成计算N个拉格朗日α,但是在二次规划中需要计算Z域的内积.
如何避免在Z域计算矩阵内积？
note:
原来算法实现时候,在Z域空间中我们需要把所有常数项,一次项,两次项的个数都作为Z域的维度d
使得Z域的d很大

*Kernel hard-margin*
*目的: 内积计算转化为X域的d+1维,而非Z域的d+1维。*
1.kernel trick
当我们使用kernel替换了Z域的内积计算,QP二次规划求解α因子
同时参数b,矩gsvm = sign(WTZx + b) 都通过kernel function计算得到
整个计算过程都在X域中操作,称之为kernel trick

2.polynomial kernel
KQ(x,x') = (ζ + γXTX')^Q    s.t. γ>0;ζ>=0
三个超参数=ζ常数项缩放比例,γ内积缩放比例,Q多项式最高次方
当Q=1,ζ=0,γ=1,是linear SVM。通过Q,large-margin限制overfit。

3.gaussian kernel
解决: Q阶多项式的kernel是有限的特征转换,如何通过无限的Z域空间做特征转换呢？
K(x,x') = exp(-γ(x-x')^2)
一个超参数 γ缩放因子
note: 矩gsvm是由N个高斯函数线性组合,每个高斯函数的中心都对应着support vector

*kernel comparison*
linear kernel
polynomial kernel
gaussian kernel (又称之为RBF,径向基函数,powerful)
自定义kernel
