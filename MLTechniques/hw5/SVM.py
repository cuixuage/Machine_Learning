#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/1/10 0010 下午 21:24
# @Author   : cuixuange
# @FileName : SVM.py
# @Contact  : cuixuange1995@gmail.com
import pandas as pd
import numpy as np
import sklearn as skl
from sklearn.svm import SVC

"""
SVC函数:C-Support Vector Classification，分类问题
soft-margin SVM的自带超参数C,平衡ξn和目标WTW. C越大,margin更窄,越容易过拟合
"""


def load_data(filename):
    """
    :return: X=常数项,手写数字的密度,对称度特征  Y=手写数字值
    """
    data = pd.read_csv(filename, sep='\s+', header=None)
    row, col = data.shape
    data = data.values
    X = np.c_[np.ones((row, 1)), data[:, 1:col]]  # X0是W0的常数项,1
    Y = data[:, 0:1]  # shape(7291,1)
    return X, Y.reshape(Y.shape[0], )


def mistake(yhat, y):
    err = np.sum(yhat != y) / len(y)
    return err


def linear_SVM():
    """
    linear soft-margin SVM , 做分类问题将数字零和其他数字分开
    只有线性SVM获取的weight才是有意义的,non-linear的weight都在Z域空间,和X域不在同一空间
    """
    X, Y = load_data('features_train.dat')
    pos1 = np.where(Y == 0)
    pos2 = np.where(Y != 0)
    for i in pos1[0]:
        Y[i] = 1
    for i in pos2[0]:
        Y[i] = -1
    # print(Y[:10], Y.shape)

    # shrinking=True 用来加速模型训练
    model_svm = SVC(C=0.01, kernel='linear', shrinking=False)
    # print("Xshape", X.shape, " Yshape", Y.shape)  # X(7291,3) Y(7291,)
    model_svm.fit(X, Y)

    weight = model_svm.coef_
    print(weight)  # X域d+1维
    print("|W|=", np.linalg.norm(weight))  # 向量weight的范数,长度,|W|
    Y_pred = model_svm.predict(X)
    Ein = mistake(Y, Y_pred)
    print("Ein=", Ein)
    print()


def poly_SVM():
    """
    non-linear(kernel=poly) soft-margin SVM , 将数字零和其他数字分开
    soft-margin超参数C
    poly超参数,degree多项式次方,gama内积的缩放比例,coef0常数项的值？

    note: 当degree=1,gama=1,coef0=1相当于linear-SVM，经测试Error_in一致
    """
    X, Y = load_data('features_train.dat')
    pos1 = np.where(Y == 0)
    pos2 = np.where(Y != 0)
    for i in pos1[0]:
        Y[i] = 1
    for i in pos2[0]:
        Y[i] = -1
    model_svm = SVC(C=0.01, kernel='poly', degree=2, gamma=1, coef0=1, shrinking=False)
    # print("Xshape", X.shape, " Yshape", Y.shape)  # X(7291,3) Y(7291,)
    model_svm.fit(X, Y)

    Y_pred = model_svm.predict(X)
    Ein = mistake(Y, Y_pred)
    alpha = model_svm.dual_coef_
    print("Ein=", Ein)
    print("sum_alpha=", np.sum(np.abs(alpha)))  # α因子的绝对值得和
    print()


def rbf_SVM():
    """
    non-linear(kernel=rbf,gaussian) soft-margin SVM , 将数字零和其他数字分开
    soft-margin超参数C
    gaussian超参数γ,内积缩放比例
    :return:本实验C=0.1,γ=10 Eout是最好的
    """
    X, Y = load_data('features_train.dat')
    pos1 = np.where(Y == 0)
    pos2 = np.where(Y != 0)
    for i in pos1[0]:
        Y[i] = 1
    for i in pos2[0]:
        Y[i] = -1
    model_svm = SVC(C=0.1, kernel='rbf', gamma=10, shrinking=False)
    # print("Xshape", X.shape, " Yshape", Y.shape)  # X(7291,3) Y(7291,)
    model_svm.fit(X, Y)

    Y_pred = model_svm.predict(X)
    Ein = mistake(Y, Y_pred)
    alpha = model_svm.dual_coef_
    nsv = model_svm.n_support_  # return每一个类别的support vector
    print("Ein=", Ein)
    print("sum_alpha=", np.sum(np.abs(alpha)))  # α因子的绝对值得和
    print("number of support vector=", np.sum(nsv))


if __name__ == "__main__":
    # linear_SVM()
    # poly_SVM()
    rbf_SVM()
