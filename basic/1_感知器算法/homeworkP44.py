# import numpy as np
#多分类问题 广义的线性可分 三维空间中判别面
# 用多类感知器算法求下列模式的判别函数：
# 		ω1: (-1 -1)T
# 		ω2: (0 0)T
# 		ω3: (1 1)T

# x1 = np.mat([-1,-1,1])
# x2 = np.mat([0,0,1])
# x3 = np.mat([1,1,1])
# x = [x1.T,x2.T,x3.T]
# w1 = np.mat([0,0,0])
# w2 = np.mat([0,0,0])
# w3 = np.mat([0,0,0])
# w = [w1.T,w2.T,w3.T]
# w2 = [w1,w2,w3]
# f = True
# count = 0
# while f:
#     f = False
#     for i in range(len(x)):
#         count += 1
#         d = []
#         for j in range(len(w)):
#             d.append(w[j].T * x[i])
#         print(d)
#         print(w2)
#         if (count % 3 == 1):
#             if d[0] <= d[1] or d[0] <= d[2]:
#                 w[0] += x[0]
#                 w[1] -= x[0]
#                 w[2] -= x[0]
#                 f = True
#     # d = np.array(d)
#         if(count%3==2):
#             if d[1] <= d[0] or d[1] <= d[2]:
#                 w[0] -= x[1]
#                 w[1] += x[1]
#                 w[2] -= x[1]
#                 f = True
#         if(count%3==0):
#             if  d[2] <= d[1] or d[2] <= d[1]:
#                 w[0] -= x[2]
#                 w[1] -= x[2]
#                 w[2] += x[2]
#                 f = True
#         print count,"**********"
# print w
# print w2
#
#
#
#
#
#
#
#
