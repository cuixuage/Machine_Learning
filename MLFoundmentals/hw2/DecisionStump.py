#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/1/15 0015 下午 14:30
# @Author   : cuixuange
# @FileName : DecisionStump.py
# @Contact  : cuixuange1995@gmail.com
import numpy as np
import pandas as pd

"""
单维: h(x) = s * sign(x-θ)
多维: h(x) = s * sign(xi-θ)
"""


def generateData():
    """
    X是[-1,1]之间的均匀分布
    Y是sign(X)+noise，20%的概率反转Y的结果
    """
    X = np.random.uniform(-1, 1, 20)  # [low, high) 20个随机数值
    Y = np.sign(X)
    Y[np.where(Y == 0)] = 1
    prop = np.random.uniform(0, 1, 20)
    Y[prop >= 0.8] *= -1
    return X, Y


def decision_stump(X, Y):
    """
    :return: S属于{-1,1},theta,Ein
    """
    theta = np.sort(X);
    num = len(theta)
    Xtemp = np.tile(X, (num, 1))  # X按照(20,1)形状做重复操作
    thetaTemp = np.tile(np.reshape(theta, (num, 1)), (1, num))
    # print(thetaTemp.shape)
    # print(Xtemp.shape)
    y_pred = np.sign(Xtemp - thetaTemp)
    y_pred[y_pred == 0] = -1
    # print(y_pred.shape)           #shape=20*20
    err = np.sum(y_pred != Y, axis=1)  # 其他维度加到维度1，类似于横着压缩为1列
    if np.min(err) <= num - np.max(err):
        return 1, theta[np.argmin(err)], np.min(err) / num
    else:
        return -1, theta[np.argmax(err)], (num - np.max(err)) / num


def decision_stump_multi(X, Y):
    row, col = X.shape
    err = np.zeros((col,))
    s = np.zeros((col,))
    theta = np.zeros((col,))
    for i in range(col):
        s[i], theta[i], err[i] = decision_stump(X[:, i], Y[:, 0])
    pos = np.argmin(err)
    return pos, s[pos], theta[pos], err[pos]


def loadData(filename):
    data = pd.read_csv(filename, sep='\s+', header=None)
    data = data.values
    col, row = data.shape
    X = np.c_[np.ones((col, 1)), data[:, 0: row - 1]]
    Y = data[:, row - 1:row]
    return X, Y


def data_test():
    X, Y = loadData('./hw2_train.dat')
    Xtest, Ytest = loadData('./hw2_test.dat')
    pos, s, theta, err = decision_stump_multi(X, Y)
    print('Ein: ', err)
    ypred = s * np.sign(Xtest[:, pos] - theta)
    ypred[ypred == 0] = -1
    row, col = Ytest.shape
    errout = np.sum(ypred != Ytest.reshape(row, )) / len(ypred)
    print('Eout: ', errout)


if __name__ == "__main__":
    # X, Y = generateData()
    # s,theta,Ein = decision_stump(X, Y)
    # print(Ein)
    data_test()
