#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/1/5 0005 下午 16:20
# @Author   : cuixuange
# @FileName : logisticRegression.py
# @Contact  : cuixuange1995@gmail.com
"""
寻找hypothesis使得损失函数最小
最大似然性 => 损失函数,ln为底 =>损失函数的梯度最小
▽Ein => SGD => 更新weight
note: 梯度的形状和权重的形状一样,都是(d+1)*1
"""
import numpy as np
import math
from random import randint
import pandas as pd


# def sigmoid(x):
#     return 1 / (1 + math.exp(-x))


def sigmoid(z):
    zback = 1 / (1 + np.exp(-1 * z))
    return zback


def load_data(filename):
    data = pd.read_csv(filename, sep='\s+', header=None)
    # print(data.head(5))
    row, col = data.shape
    # 添加新的维度 1,便于相乘w0
    X = data[data.columns[0:col - 1]]
    X = np.c_[np.ones((row, 1)), X]
    # print(X.shape)
    Y = data[data.columns[col - 1:col]].values
    # print(Y.shape)
    return X, Y


def mistake(X, Y, weight):
    y_predict = np.sign(X.dot(weight))
    y_predict[np.where(y_predict == 0)] = -1
    return np.sum(y_predict != Y) / len(Y)


def logisticReg(X, Y, eta, numiter):
    """
    note:
    :param X: row*(d+1)
    :param Y: row*1
    :param eta: 步长
    :param numiter: 迭代次数
    :return: 梯度下降更新weight,梯度和weight的维度是相同的
    """
    row, col = X.shape
    weight = np.zeros((col, 1))  # 20+1 维度vector
    for i in range(numiter):
        # 注意: dot是矩阵乘法; *是元素相乘
        derr = sigmoid(-1 * X.dot(weight) * Y)
        derr = (-1 * Y * X).T.dot(derr) / row
        weight -= eta * derr
    return weight


def logisticReg_SGD(X, Y, eta, numiter):
    """
    SGD 随机选择某个点梯度作为全局的梯度
    """
    row, col = X.shape
    weight = np.zeros((col, 1))  # 20+1 维度vector
    for i in range(numiter):
        # 注意: dot是矩阵乘法; *是元素相乘
        tmp = randint(0, row - 1)
        derr = sigmoid(-1 * X[tmp, :].dot(weight)[0] * Y[tmp, 0])
        derr = (-1 * Y[tmp, 0] * X[tmp:tmp + 1, :]).T.dot(derr)
        weight -= eta * derr

        # print(X[tmp:tmp + 1, :].shape)  # (1,21)相当于二维空间
        # print(X[tmp, :].shape)  # (21,)相当于一维空间
        # print(X[tmp, :].dot(weight).shape)  #(21,) * (21,1) = (1,)
        # print(X[tmp:tmp + 1, :].dot(weight).shape)
        # # print(sigmoid(-1 * X[tmp, :].dot(weight)[0] * Y[tmp, 0]))
        # # print((-1 * Y[tmp, 0] * X[tmp:tmp + 1, :]).T.shape)
    return weight


if __name__ == "__main__":
    X, Y = load_data("./hw3_train.dat")
    Xtest, Ytest = load_data("./hw3_test.dat")
    # #Q18
    # weight = logisticReg(X, Y, 0.001, 2000)
    # #Q19
    # weight = logisticReg(X, Y, 0.01, 2000)
    # Q20
    weight = logisticReg_SGD(X, Y, 0.001, 2000)
    Ein = mistake(X, Y, weight)
    Eout = mistake(Xtest, Ytest, weight)
    print("Ein=", Ein, " Eout=", Eout)

    # 结论: eta学习率步长过小 效果不一定好


