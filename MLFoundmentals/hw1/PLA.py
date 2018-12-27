#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2018/12/26 0026 下午 14:15
# @Author   : cuixuange
# @FileName : PLA.py
# @Contact  : cuixuange1995@gmail.com

import pandas as pd
import numpy as np


def loadfile(f):
    data = pd.read_csv(f, sep='\s+', header=None)
    row, col = data.shape
    # 添加新的维度 1,便于相乘w0
    X = data[data.columns[0:col - 1]]
    X = np.c_[np.ones((row, 1)), X]
    # label Y的维度(400,1)
    Y = data[data.columns[col - 1:col]].values
    print(type(X), X.shape,type(Y), Y.shape)
    return X, Y


def perceptron(X, Y, weight,alpha=1):
    callNum = 0
    prepos = 0  # 保存上次出错的位置
    while (True):
        ytmp = np.sign(X.dot(weight))
        # 要求：将预测为0的yn 设置为-1
        ytmp[np.where(ytmp == 0)] = -1

        # 找出预测错误的点
        # 保存行索引,where return 列索引都是0
        index = np.where(ytmp != Y)[0]
        if index.size == 0:
            break
        if index[index >= prepos].size == 0: # 寻找上次出错位置
            prepos = 0
        # 改为单纯大于号 可能出错 对于恰好在0的位置有mistake的问题导致越界
        prepos = index[index >= prepos][0]

        # e.g. alpha可以设置为0.5
        # 由于w 初始值为0 所以alpha不影响迭代次数
        weight = weight + alpha * Y[prepos, 0] * X[prepos].reshape(-1, 1)
        callNum += 1
    return weight, callNum


"""
    h(x) = w0*1 + w1x1 + w2x2 + ...+w4x4
    init w = 0
"""
if __name__ == "__main__":
    X, Y = loadfile("./hw1_15.dat")
    print("X,Y",X.shape,Y.shape)
    row, col = X.shape

    weight = np.zeros((col, 1))  # shape(5,1)向量
    weight, callNum = perceptron(X, Y, weight)

    # weight第一维数据是thesold
    print(weight, callNum)

    ##  test np.where
    # np1 = [1,2,3]
    # np2 = [4,5,6]
    # index = np.where(np1!=np2)
    # print(index[0].size)
