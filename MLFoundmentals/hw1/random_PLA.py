#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2018/12/26 0026 下午 19:33
# @Author   : cuixuange
# @FileName : random_PLA.py
# @Contact  : cuixuange1995@gmail.com

from PLA import loadfile,perceptron
import numpy as np

if __name__ == "__main__":
    X, Y = loadfile("./hw1_15.dat")
    row, col = X.shape
    total = 0
    for i in range(2000):
        randpos = np.random.permutation(row)
        # print(randpos.shape)    # (400,) 打乱原numpy顺序
        weight = np.zeros((col, 1))
        randomX = X[randpos,:]
        randomY = Y[randpos,0:1]
        # print(randomX.shape,randomY.shape)
        _,num = perceptron(randomX,randomY,weight)
        total += num
    print(total/2000)