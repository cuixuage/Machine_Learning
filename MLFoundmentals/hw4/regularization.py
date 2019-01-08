#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/1/8 0008 上午 9:03
# @Author   : cuixuange
# @FileName : regularization.py
# @Contact  : cuixuange1995@gmail.com

import pandas as pd
import numpy as np

"""
加入正则项的线性回归,公式求解Wreg
Wreg=(XtX + λI)^-1 .dot( XTY)
λ越大,阈值C越小,越倾向低纬度的Weight
"""


def load_data(filename):
    data = pd.read_csv(filename, sep='\s+', header=None)
    row, col = data.shape
    data = data.values
    X = np.c_[np.ones((row, 1)), data[:, 0:col - 1]]
    Y = data[:, col - 1:col]
    return X, Y


def mistake(X, Y, weight):
    y_pred = np.sign(X.dot(weight))
    y_pred[np.where(y_pred == 0)] = -1
    err = np.sum(y_pred != Y) / len(Y)
    return err


def single_lambda(lamda=10):
    X, Y = load_data("./hw4_train.dat")
    Xtest, Ytest = load_data("./hw4_test.dat")
    # print(type(X), type(Y), X.shape, Y.shape)
    row, col = X.shape

    # np.eye(K) 对角线为1,其他位置为0的k*K矩阵
    Wreg = np.linalg.inv(X.T.dot(X) + lamda * np.eye(col)).dot(X.T).dot(Y)
    Ein = mistake(X, Y, Wreg)
    Eout = mistake(Xtest, Ytest, Wreg)
    print("Ein=", Ein, " Eout=", Eout)


def multi_lambda():
    """
    log10 lamda∈[-10,2]  lamda越大,对高维度weight惩罚越大
    """
    X, Y = load_data("./hw4_train.dat")
    Xtest, Ytest = load_data("./hw4_test.dat")
    row, col = X.shape
    arr = np.arange(-10, 3, 1)
    # print(type(arr))
    lamda = [10.0 ** i for i in arr]
    # print(lamda)
    for i in range(len(arr)):
        Wreg = np.linalg.inv(X.T.dot(X) + lamda[i] * np.eye(col)).dot(X.T).dot(Y)
        Ein = mistake(X, Y, Wreg)
        Eout = mistake(Xtest, Ytest, Wreg)
        print("lambda=", lamda[i], " Ein=", Ein, " Eout=", Eout)


def validation():
    X, Y = load_data("./hw4_train.dat")
    Xtest, Ytest = load_data("./hw4_test.dat")
    Xtrain = X[0:120, :]
    Ytran = Y[0:120, :]
    Xval = X[120:, :]
    Yval = Y[120:, :]
    row, col = Xtrain.shape
    arr = np.arange(-10, 3, 1)
    lamda = [10.0 ** i for i in arr]
    for i in range(len(arr)):
        Wreg = np.linalg.inv(Xtrain.T.dot(Xtrain) + lamda[i] * np.eye(col)).dot(Xtrain.T).dot(Ytran)
        Ein = mistake(Xtrain, Ytran, Wreg)
        Eval = mistake(Xval, Yval, Wreg)
        print("lambda=", lamda[i], " Ein=", Ein, " Eval=", Eval)

    # 选择Eval 最小的lamda
    # 这里有多个  重新计算Wreg
    # 我这里随便选一个λ=0的情况计算
    row, col = X.shape
    Wreg = np.linalg.inv(X.T.dot(X) + 0 * np.eye(col)).dot(X.T).dot(Y)
    Ein = mistake(X, Y, Wreg)
    Eout = mistake(Xtest, Ytest, Wreg)
    print("lambda=", 0, " Ein=", Ein, " Eout=", Eout)


def V_fold_cross():
    # 取5份进行交叉验证
    # 注意cross
    print("V-fold-cross")


if __name__ == "__main__":
    single_lambda()
    multi_lambda()
    validation()
    V_fold_cross()