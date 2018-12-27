#coding=utf-8
import pandas as pd
data = pd.read_csv('D:\\Pycharm\\projects\\test\\Advertising.csv')
#print data.head()

#create a python list of feature names
feature_cols = ['TV', 'radio', 'newspaper']
# use the list to select a subset of the original DataFrame
X = data[feature_cols]
# equivalent command to do this in one line
X = data[['TV', 'radio', 'newspaper']]
# # print the first 5 rows
# print X.head()
# # check the type and shape of X
# print type(X)
# print X.shape

# select a Series from the DataFrame
y = data['sales']
# equivalent command that works if there are no spaces in the column name
y = data.sales
# print the first 5 values
# print y.head()

from  sklearn.model_selection  import  train_test_split  #这里是引用了交叉验证
X_train,X_test, y_train, y_test = train_test_split(X, y, random_state=1)
# print X_train.shape
# print y_train.shape
# print X_test.shape
# print y_test.shape

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
model=linreg.fit(X_train, y_train)
# print model
# print linreg.intercept_
# print linreg.coef_
# pair the feature names with the coefficients
#y=2.668+0.0464∗TV+0.192∗Radio-0.00349∗Newspaper
print zip(feature_cols, linreg.coef_)

y_pred = linreg.predict(X_test)
print y_pred
print type(y_pred)

import matplotlib.pyplot as plt
plt.figure()
plt.plot(range(len(y_pred)),y_pred,'b',label="predict")
plt.plot(range(len(y_pred)),y_test,'r',label="test")
plt.legend(loc="upper right") #显示图中的标签
plt.xlabel("the number of sales")
plt.ylabel('value of sales')
plt.show()