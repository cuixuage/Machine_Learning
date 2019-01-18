#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/1/18 0018 上午 10:11
# @Author   : cuixuange
# @FileName : KNN.py
# @Contact  : cuixuange1995@gmail.com
"""
K-nearest-neighbor algorithm
idea:  每一个样本的label是通过最近的k个样本点的label进行voting决定的
distance: 通过欧式距离计算(X1的所有特征向量和X2的所有特征向量平方差)
"""
import numpy as np
import pandas as pd


def loadData(filename):
    data = pd.read_csv(filename, sep='\s+', header=None)
    data = data.values
    col, row = data.shape
    X = data[:, 0:row - 1]
    Y = data[:, row - 1:row]
    # print(X.shape,Y.shape)  # train (100, 9) (100, 1)
    return X, Y


def KNNeighber(k, xpred, X, Y):
    """
    待预测的点xpred 和 X中所有样本的距离选择最小的K个值
    """
    xmin = np.sum((xpred - X) ** 2, 1)  # 横着压缩,所有平方的和
    pos = np.argsort(xmin, 0)
    Ypred = Y[pos[0:k]]
    Ypred = np.sum(Ypred)  # 最近的k样本 voting
    Ypred = 1 if Ypred >= 0 else -1
    return Ypred


def predict(Xtest, X, Y, k):
    row, col = Xtest.shape
    Ypred = np.zeros((row, 1))
    # 预测每行(每个样本)的类别
    for i in range(row):
        Ypred[i] = KNNeighber(k, Xtest[i, :], X, Y)
    return Ypred


if __name__ == "__main__":
    X, Y = loadData("hw4_knn_train.dat")
    Xtest, Ytest = loadData("hw4_knn_test.dat")

    ## 测试K值=1  K值=5的效果
    # Yhat = predict(Xtest, X, Y, 1)
    Yhat1 = predict(X, X, Y, 5)
    Yhat2 = predict(Xtest, X, Y, 5)
    ein = np.sum(Yhat1 != Y) / Y.shape[0]
    eout = np.sum(Yhat2 != Ytest) / Ytest.shape[0]
    print(ein, eout)
