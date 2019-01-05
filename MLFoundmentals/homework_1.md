参考链接:
https://acecoooool.github.io/blog/2017/02/06/MLF&MLT/MLF1-1/

基础题目:
1.样本外误差分析
2.容器模型

编程题目:
1.PLA 感知机算法
对于可分数据集的perceptron
```python
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
```

2.pocket PLA 
对于不可分的数据集(noise data) 的感知机算法
```python
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
```
