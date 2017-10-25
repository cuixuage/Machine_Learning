#coding=utf-8
from __future__ import division #整数相除结果保存小数
import pandas as pd

data = pd.read_table('D:\\Pycharm\\projects\\test\\datafromSZ0001.txt')
#print data.head()

feature_cols = ['BOLL', 'UPR', 'DWN']
X = data[feature_cols]
X = data[['BOLL', 'UPR', 'DWN']]
y = data['CLOSE']
y = data.CLOSE
# print type(X)
# for i in range(1/4*len(X))
# print X.head()
# print y.head()

from  sklearn.model_selection  import  train_test_split
X_train,X_test, y_train, y_test = train_test_split(X, y, random_state=1)
# print type(X_train)
# print X_train.shape
# print y_train.shape
# print X_test.shape
# print y_test.shape

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
model=linreg.fit(X_train, y_train)
#close y = 3.35698725045 + 0.31554797762103209*BOLL + 0.33952722983704425*UPR + -0.019662027670535348*DOWN
# print model
# print linreg.intercept_
# print zip(feature_cols, linreg.coef_)


y_pred = linreg.predict(X_test)
#print y_pred
# print type(y_test)
y_test = pd.Series.as_matrix(y_test)
#print type(y_test)
#print y_test

bool_pred = []
for idx, val in enumerate(y_pred):
    if idx < len(y_pred)-1:
        if val < y_pred[idx+1]:   #up
            bool_pred.append(1)
        else:
            bool_pred.append(0)  #down
#print len(bool_pred) , len(y_pred)

bool_test = []
for idx, val in enumerate(y_test):
    if idx < len(y_test)-1:
        if val < y_test[idx+1]:   #up
            bool_test.append(1)
        else:
            bool_test.append(0)  #down
# print len(bool_test) , len(y_test)

correct_count = 0
for i in range(0,len(bool_pred)):
    if bool_pred[i] == bool_test[i]:
        correct_count +=1
print correct_count/len(bool_test)


import matplotlib.pyplot as plt
plt.figure()
plt.plot(range(len(y_pred)),y_pred,'b',label="predict")
plt.plot(range(len(y_pred)),y_test,'r',label="test")
plt.legend(loc="upper right")
plt.xlabel("the number of sales")
plt.ylabel('value of sales')
plt.show()