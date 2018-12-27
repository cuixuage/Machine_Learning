# #coding:utf-8
#二分类问题   假设线性可分
# 用感知器算法求下列模式分类的解向量w:
# 	ω1: {(0 0 0)T, (1 0 0)T, (1 0 1)T, (1 1 0)T}
# 	ω2: {(0 0 1)T, (0 1 1)T, (0 1 0)T, (1 1 1)T}
#
# 编写求解上述问题的感知器算法程序


# import numpy as np
# x1 = np.mat([0,0,0,1])
# x2 = np.mat([1,0,0,1])
# x3 = np.mat([1,0,1,1])
# x4 = np.mat([1,1,0,1])
# #w2区域的全部乘以 -1 作为分类的区分
# x5 = np.mat([0,0,-1,-1])
# x6 = np.mat([0,-1,-1,-1])
# x7 = np.mat([0,-1,0,-1])
# x8 = np.mat([-1,-1,-1,-1])
# x = [x1.T,x2.T,x3.T,x4.T,x5.T,x6.T,x7.T,x8.T]
# #print(x)
# w = np.mat([0,0,0,0])         #初始化取C=1，w(1)= (0 0 0)
# w = w.T
# #print(w)
# bool = True
# while bool:
#     bool = False
#     for i in range(len(x)):
#         d= w.T * x[i]       #得到1*1矩阵
#         print(d.sum())
#         if d <= 0:
#             w = w + x[i]      #惩罚
#             bool = True       #存在惩罚 继续迭代
#     print("***********")
# print(w)
#
#
#
#
#
#
#
#
