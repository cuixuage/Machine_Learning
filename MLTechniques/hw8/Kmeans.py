#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/1/18 0018 下午 15:05
# @Author   : cuixuange
# @FileName : Kmeans.py
# @Contact  : cuixuange1995@gmail.com
"""
K-means
核心: 两组变量交替更新
"""
import numpy as np
import pandas as pd


# 加载数据函数
def loadData(filename):
    data = pd.read_csv(filename, sep='\s+', header=None)
    data = data.values
    return data


def Kmeans(K, X):
    row, col = X.shape
    pos = np.random.permutation(row)
    mu = X[pos[0:K], :]  # 随机选择两个点 作为两个类别的中心点
    epsilon = 1e-5
    simi = 1
    while simi > epsilon:
        # S保存所有样本点和类别中心点的距离
        S = np.zeros((row, K))
        for i in range(K):
            S[:, i] = np.sum((X - mu[i, :]) ** 2, 1)
        tempmu = mu.copy()
        # 样本点选择距离最小距离的中心点 记录自己的类别
        pos = np.argmin(S, 1)
        # 同类别的更新自己的中心点坐标
        for i in range(K):
            mu[i, :] = np.mean(X[pos == i, :], 0)
        simi = np.sum(tempmu - mu)
    return mu


def mistake(X, mu):
    """
    kmeas误差定义:  样本点xn和其所属分类的中心点的平方误差
    """
    row, col = X.shape
    k = mu.shape[0]
    err = 0
    S = np.zeros((row, k))
    for i in range(k):
        S[:, i] = np.sum((X - mu[i, :]) ** 2, 1)
    pos = np.argmin(S, 1)
    for i in range(k):
        err += np.sum((X[pos == i, :] - mu[i, :]) ** 2)
    return err / row


if __name__ == '__main__':
    # 导入数据
    X = loadData('hw4_kmeans_train.dat')
    err = 0
    iteration = 500
    for i in range(iteration):
        mu = Kmeans(2, X)  # return 所有类别的中心点
        err += mistake(X, mu)
        # break
    print(err / iteration)
