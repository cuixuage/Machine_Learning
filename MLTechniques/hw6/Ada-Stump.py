#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/1/15 0015 下午 16:32
# @Author   : cuixuange
# @FileName : Ada-Stump.py
# @Contact  : cuixuange1995@gmail.com

import numpy as np
import pandas as pd
import scipy.linalg as lin


def loadData(filename):
    data = pd.read_csv(filename, sep='\s+', header=None)
    data = data.values
    col, row = data.shape
    X = data[:, 0: row - 1]
    Y = data[:, row - 1:row]
    return X, Y


#################FIXME 不是很懂  记得返工
# 决策树桩
def decision_stump(X, Y, thres, U):
    row, col = X.shape
    r, c = thres.shape;
    besterr = 1
    btheta = 0;
    bs = 0;
    index = 0
    for i in range(col):
        Yhat1 = np.sign(np.tile(X[:, i:i + 1], (1, r)).T - thres[:, i:i + 1]).T
        err1 = (Yhat1 != Y).T.dot(U)
        err2 = (-1 * Yhat1 != Y).T.dot(U)
        s = 1 if np.min(err1) < np.min(err2) else -1
        if s == 1 and np.min(err1) < besterr:
            besterr = np.min(err1);
            bs = 1
            index = i;
            btheta = thres[np.argmin(err1), i]
        if s == -1 and np.min(err2) < besterr:
            besterr = np.min(err2);
            bs = -1
            index = i;
            btheta = thres[np.argmin(err2), i]
    return besterr, btheta, bs, index


# AdaBoost---Stump 算法
# 需要说明: 与PPT上有点不同，始终保证sum(U)=1
def ada_boost(X, Y, T):
    row, col = X.shape
    U = np.ones((row, 1)) / row
    Xsort = np.sort(X, 0)
    thres = (np.r_[Xsort[0:1, :] - 0.1, Xsort[0:row - 1, :]] + Xsort) / 2
    theta = np.zeros((T,));
    s = np.zeros((T,));
    index = np.zeros((T,)).astype(int);
    alpha = np.zeros((T,))
    err = np.zeros((T,))
    for i in range(T):
        err[i], theta[i], s[i], index[i] = decision_stump(X, Y, thres, U)
        yhat = s[i] * np.sign(X[:, index[i]:index[i] + 1] - theta[i])
        delta = np.sqrt((1 - err[i]) / err[i])
        U[yhat == Y] /= delta
        U[yhat != Y] *= delta
        # Q14运行时，解除注释
        #        if i == T-1:
        #            print('sum(U): ', np.sum(U))
        alpha[i] = np.log(delta)
        U /= np.sum(U)
    # Q15运行时，解除注释
    #    print('最小的eta: ', np.min(err))
    return theta, index, s, alpha


if __name__ == "__main__":
    # 导入数据
    X, Y = loadData('hw2_adaboost_train.dat')
    Xtest, Ytest = loadData('hw2_adaboost_test.dat')
    row, col = X.shape
    r, c = Xtest.shape
