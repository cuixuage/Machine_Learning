#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/1/4 0004 下午 16:31
# @Author   : cuixuange
# @FileName : featureTransform.py
# @Contact  : cuixuange1995@gmail.com
"""
非线性问题转化到高维空间的线性问题
e.g.
二维空间的非线性转化为二次多项式的6维空间
1, x1, x2, x1x2, x1^2, x2^2
"""
import numpy as np
from linearRegression import load_data

def feature_tansform(X):
    row, col = X.shape
    Xback = np.zeros((row, 6))
    # 1 x1 x2 保存入Xback
    Xback[:, 0:col] = X
    Xback[:, col] = X[:, 1] * X[:, 2]
    Xback[:, col + 1] = X[:, 1] ** 2
    Xback[:, col + 2] = X[:, 2] ** 2
    return Xback


if __name__ == "__main__":
    N = 1000
    X,Y = load_data(N)
    Xtrans = feature_tansform(X)
    # print(Xtrans.shape)

    weight = np.linalg.pinv(Xtrans).dot(Y)
    print(weight.shape)
    print(weight)

    y_predict = np.sign(Xtrans.dot(weight))      # 加权分数值
    error = np.sum(y_predict != Y)/N
    print("Ein=",error)
    Xtest, Ytest = load_data(N)
    Xback = feature_tansform(Xtest)
    ypred = np.sign(Xback.dot(weight))
    err = np.sum(ypred!=Ytest)/N
    print("Eout=",err)