#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/1/4 0004 上午 10:31
# @Author   : cuixuange
# @FileName : linearRegression.py
# @Contact  : cuixuange1995@gmail.com
"""
input matrix X 的形状 N*(d+1) ; output vector y 的形状 N*1
计算 pseudo-inverse X+  的形状 (d+1)*N
得到最佳Weight= X+ * y。Wlin 的形状 d+1维
"""

import numpy as np


def load_data(num=3):
    """num是数据样本数量"""
    axeX = np.random.uniform(-1, 1, num)  # x1
    axeY = np.random.uniform(-1, 1, num)  # x2
    Xtemp = np.c_[axeX, axeY]  # 链接列column
    # x0=1 w0常数项
    X = np.c_[np.ones((num, 1)), Xtemp]
    # 圆圈里面的Y等于-1
    Ytemp = np.sign(np.power(axeX, 2) + np.power(axeY, 2) - 0.6)
    Ytemp[Ytemp == 0] = -1
    # pos是随机的排列 ; 随机选择0.1概率的Y进行反转
    pos = np.random.permutation(num)
    Ytemp[pos[0:round(0.1 * num)]] *= -1
    Y = Ytemp.reshape((num, 1))
    return X, Y


if __name__ == "__main__":
    """
    直接将线性回归W  应用到0/1分类问题效果不太好
    利用square error求得Wlin
    图形: 非线性问题如何进行feature transform？
    """
    # 1.
    N = 10000
    X, Y = load_data(N)
    # 2.
    weight = np.linalg.pinv(X).dot(Y)
    print(weight.shape)  # shape (d+1)*N
    print(weight)
    # 3.
    y_predict = np.sign(X.dot(weight))      # 加权分数值
    # print(y_predict)
    error = np.sum(y_predict != Y)/N
    print("Ein=",error)