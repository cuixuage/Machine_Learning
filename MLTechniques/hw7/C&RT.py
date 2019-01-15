#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/1/15 0015 下午 20:19
# @Author   : cuixuange
# @FileName : C&RT.py
# @Contact  : cuixuange1995@gmail.com
import numpy as np
import pandas as pd


# 决策树的树节点
class Node:
    """
    theta 划分的阈值 index 选用的维度 value 根节点的值
    """

    def __init__(self, theta, index, value=None):
        self.theta = theta
        self.index = index
        self.value = value
        self.leftNode = None
        self.rightNode = None


def gini(Y):
    # 统计子集的purify
    allY = Y.shape[0]
    if allY == 0:
        return 1
    u1 = np.sum(Y == 1) / allY
    u2 = np.sum(Y == -1) / allY
    return 1 - u1 ** 2 - u2 ** 2


def one_stump(X, Y, thres):
    # 寻找每一个维度的划分阈值和对应的branch分支条件值
    thresRow = thres.shape[0]
    mini = Y.shape[0]
    for i in range(thresRow):
        Y1 = Y[X < thres[i]]
        Y2 = Y[X >= thres[i]]
        judge = Y1.shape[0] * gini(Y1) + Y2.shape[0] * gini(Y2)
        if mini > judge:
            mini = judge;
            b = thres[i]
    return mini, b


# 找出最佳划分的阈值和对应的维度
# 结合全部维数的决策树桩
def decision_stump(X, Y):
    row, col = X.shape
    Xsort = np.sort(X, 0)
    thres = (np.r_[Xsort[0:1, :] - 0.1, Xsort] + np.r_[Xsort, Xsort[-1:, :] + 0.1]) / 2
    mpurity = row;
    mb = 0;
    index = 0
    for i in range(col):
        purity, b = one_stump(X[:, i], Y[:, 0], thres[:, i])
        if mpurity > purity:
            mpurity = purity;
            mb = b;
            index = i
    return mb, index


def stop_cond(X, Y):
    # fully-grown tree终止条件
    if np.sum(Y != Y[0]) == 0 or X.shape[0] == 1 or np.sum(X != X[0, :]) == 0:
        return True
    return False


def dTree(X, Y):
    if stop_cond(X, Y):
        node = Node(None, None, Y[0])
        return node
    b, index = decision_stump(X, Y)
    pos1 = X[:, index] < b
    pos2 = X[:, index] >= b
    leftX = X[pos1, :];
    leftY = Y[pos1, 0:1]
    rightX = X[pos2, :];
    rightY = Y[pos2, 0:1]
    node = Node(b, index)
    node.leftNode = dTree(leftX, leftY)
    node.rightNode = dTree(rightX, rightY)
    return node


# 对于单个样本的预测
def predict_one(node, X):
    if node.value is not None:
        return node.value[0]
    thre = node.theta
    index = node.index
    if X[index] < thre:
        return predict_one(node.leftNode, X)
    else:
        return predict_one(node.rightNode, X)


# 决策树的预测结果 和 错误衡量
def err_fun(X, Y, node):
    row, col = X.shape
    Yhat = np.zeros(Y.shape)
    for i in range(row):
        Yhat[i] = predict_one(node, X[i, :])
    return Yhat, np.sum(Yhat != Y) / row


# 定义搜索树的拥有多少节点  叶子结点不计入
def internal_node(node):
    if node == None: return 0
    if node.leftNode == None and node.rightNode == None: return 0
    l = 0;
    r = 0
    if node.leftNode != None:
        l = internal_node(node.leftNode)
    if node.rightNode != None:
        r = internal_node(node.rightNode)
    return 1 + l + r


def loadData(filename):
    data = pd.read_csv(filename, sep='\s+', header=None)
    data = data.as_matrix()
    col, row = data.shape
    X = data[:, 0: row - 1]
    Y = data[:, row - 1:row]
    return X, Y


# bagging函数
def bagging(X, Y):
    row, col = X.shape
    pos = np.random.randint(0, row, (row,))
    return X[pos, :], Y[pos, :]


# 随机森林算法---没有加入feature的随机选择
def random_forest(X, Y, T):
    nodeArr = []
    for i in range(T):
        Xtemp, Ytemp = bagging(X, Y)
        node = dTree(Xtemp, Ytemp)
        nodeArr.append(node)
    return nodeArr


# 定义只进行一次划分的决策树（夸张的剪枝）
def dTree_one(X, Y):
    b, index = decision_stump(X, Y)
    pos1 = X[:, index] < b;
    pos2 = X[:, index] >= b
    node = Node(b, index)
    value1 = 1 if np.sign(np.sum(Y[pos1])) >= 0 else -1
    value2 = 1 if np.sign(np.sum(Y[pos2])) >= 0 else -1
    node.leftNode = Node(None, None, np.array([value1]))
    node.rightNode = Node(None, None, np.array([value2]))
    return node


# 基于剪枝后的随机森林算法
def random_forest_pruned(X, Y, T):
    nodeArr = []
    for i in range(T):
        Xtemp, Ytemp = bagging(X, Y)
        node = dTree_one(Xtemp, Ytemp)
        nodeArr.append(node)
    return nodeArr


if __name__ == "__main__":
    X, Y = loadData('hw3_train.dat')
    Xtest, Ytest = loadData('hw3_test.dat')
    node = dTree(X, Y)
    print("fully-grown Tree nodes' number=", internal_node(node))

    _, ein = err_fun(X, Y, node)
    _, eout = err_fun(Xtest, Ytest, node)
    print('Ein: ', ein, '\nEout: ', eout)
