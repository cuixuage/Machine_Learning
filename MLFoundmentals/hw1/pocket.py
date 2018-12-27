#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2018/12/26 0026 下午 20:40
# @Author   : cuixuange
# @FileName : pocket.py
# @Contact  : cuixuange1995@gmail.com

from PLA import loadfile
import numpy as np
from random import randint


# 对于最优函数的判读  定义所有点的错误率
def mistake(ytmp, Y):
    row, col = Y.shape
    tmp = [ytmp[i, 0] for i in range(row) if ytmp[i, 0] != Y[i, 0]]
    return len(tmp) / float(row)


def initmistake(X, Y, weight):
    ytmp = np.sign(X.dot(weight))
    ytmp[np.where(ytmp == 0)] = -1
    error = mistake(ytmp, Y)
    return error, ytmp


def pocket(X, Y, weight, iternum):
    err_old, ytmp = initmistake(X, Y, weight)
    weight_best = np.zeros(weight.shape)
    for t in range(iternum):
        index = np.where(ytmp != Y)[0]  # mistake的索引
        if index.size == 0:
            break
        pos = index[randint(0, len(index)-1)]   # 范围在[0,len-1]
        weight = weight + Y[pos, 0] * X[pos].reshape(-1, 1)

        # 得到新的错误率
        ytmp = np.sign(X.dot(weight))
        ytmp[np.where(ytmp == 0)] = -1
        errnow = mistake(ytmp, Y)
        if (errnow < err_old):
            weight_best = weight.copy()  # 注意不要指向同一空间 使得best不断被更改
            err_old = errnow

    return weight_best, weight


if __name__ == "__main__":
    X, Y = loadfile("./hw1_18_train.dat")
    weight = np.zeros((X.shape[1], 1))
    weight_best, weight_bad = pocket(X, Y, weight, 100)

    Xtest, Ytest = loadfile("./hw1_18_test.dat")
    ytmp = np.sign(Xtest.dot(weight_best))
    ytmp[np.where(ytmp == 0)] = -1
    err = mistake(ytmp, Ytest)
    print(err)
