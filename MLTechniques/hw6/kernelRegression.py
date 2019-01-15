#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/1/15 0015 下午 18:59
# @Author   : cuixuange
# @FileName : kernelRegression.py
# @Contact  : cuixuange1995@gmail.com
# kernel ridge regression

import numpy as np
import pandas as pd
import scipy.linalg as lin

"""
kernel ridge regression类似于linear regression的"公式解"
采用高斯kernel
"""
#####FIXME   返工

# ----------- Q19-20 --------------
# 获得对偶矩阵K
def matK(X, X1, gamma):
    row, col = X.shape
    r, c = X1.shape
    K = np.zeros((row, r))
    for i in range(r):
        K[:, i] = np.sum((X - X1[i:i + 1, :]) ** 2, 1)
    K = np.exp(-gamma * K)
    return K


def loadData(filename):
    data = pd.read_csv(filename, sep='\s+', header=None)
    data = data.values
    col, row = data.shape
    X = data[:, 0: row - 1]
    Y = data[:, row - 1:row]
    return X, Y


# 加载数据
X, Y = loadData('hw2_lssvm_all.dat')
Xtrain = X[0:400, :];
Ytrain = Y[0:400, :]
Xtest = X[400:, :];
Ytest = Y[400:, :]
row, col = Xtest.shape

# 测试
# gamma是因为使用高斯kernel
gamma = [32, 2, 0.125]
lamb = [0.001, 1, 1000]
Ein = np.zeros((len(gamma), len(lamb)))
Eout = np.zeros((len(gamma), len(lamb)))
for i in range(len(gamma)):
    K = matK(Xtrain, Xtrain, gamma[i])
    K2 = matK(Xtrain, Xtest, gamma[i])
    for j in range(len(lamb)):
        beta = lin.pinv(lamb[j]*np.eye(400)+K).dot(Ytrain)
        yhat = np.sign(K.dot(beta))
        Ein[i, j] = np.sum(yhat != Ytrain)/400
        yhat2 = np.sign(K2.T.dot(beta))
        Eout[i, j] = np.sum(yhat2 != Ytest)/row
print('最小的Ein: ', np.min(Ein))
print('最小的Eout: ', np.min(Eout))