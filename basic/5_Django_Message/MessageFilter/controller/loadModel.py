#coding:utf-8
import time
import codecs
import sys
import string
import numpy as np
from sklearn import feature_extraction
# from sklearn.cross_validation import train_test_split
from  sklearn.model_selection  import  train_test_split
from sklearn.metrics import precision_recall_curve
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import  CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.externals import joblib                                #模型本地化保存
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA
from sklearn import metrics

class Borg(object):
    _state = {}

    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Borg):                           #Myclass2类只会实例化一次？？？？
    tv = joblib.load("./static/trainmodel/TfidfVectorizer_model.m")
    clf = joblib.load("./static/trainmodel/NaiveBayes_model.m")

_instance = MyClass2()                          #_instance其实相当于全局变量  一直存放在静态常量区

##获取最终结果 写入FinalResult.txt
def nbClassifier_getresult(testData):
    # tv = joblib.load("./static/trainmodel/TfidfVectorizer_model.m")
    fea_test = _instance.tv.transform(testData);
    print "nbClassifier_getresult", testData[0]

    # clf = joblib.load("./static/trainmodel/NaiveBayes_model.m")
    pred = _instance.clf.predict(fea_test)
    # print type(pred)," ",len(pred)
    print "predict",pred[0]
    if  pred[0]==0:
        return "正常短信"
    else:
        return "垃圾短信"


#navie bayes classifier
def nbClassifier(trainData,testData,trainLabel,testLabel):
    vectorizer = CountVectorizer(binary=True)       #文本特征提取CountVectorizer
    fea_train = vectorizer.fit_transform(trainData)  #标记和计算一个语料的词频
    fea_test = vectorizer.transform(testData);    #在训练语料中没有出现的词在后续调用转化方法时将被完全忽略  Not use the fit_transform
    clf = MultinomialNB(alpha = 0.01)
    clf.fit(fea_train,np.array(trainLabel))
    pred = clf.predict(fea_test)
    totalScore(pred,testData,testLabel)


# 计算F值
def totalScore(pred, x_test, y_test):
    A = 0
    C = 0
    B = 0
    D = 0
    #     foutR= open('../data/R1.txt','a+')
    #     foutE = open('../data/E1.txt','a+')
    for i in range(len(pred)):
        if y_test[i] == 0:
            if pred[i] == 0:   #real:msg  pre:msg
                A += 1
            # foutR.write('%s\n' %x_test[i])
            elif pred[i] == 1:   #real:msg  pre:rubbish
                B += 1
            #foutE.write('%s\n' %x_test[i])
        elif y_test[i] == 1:    #real:rubbish  pre:msg
            if pred[i] == 0:
                C += 1
            # foutE.write('%s\n' %x_test[i])
            elif pred[i] == 1:  #real:rubbish  pre:rubbish
                D += 1
                # outR.write('%s\n' %x_test[i])
                # foutR.close()
                # foutE.close()
    # print  A, B, C, D, A + B + C + D

    rb_pr = 1.0 * D / (B + D)           #被预测正确的垃圾短信 占据所有被预测为垃圾短信的比例
    rb_re = 1.0 * D / (C + D)           #被预测正确的垃圾短信 占据所有真实垃圾短信的比例
    rt_pr = 1.0 * A / (A + C)
    rt_re = 1.0 * A / (A + B)
    print  "Recall:",rb_re
    print  "Precision:",rb_pr
    # Frb = 0.65 * rb_pr + 0.35 * rb_re
    # Frt = 0.65 * rt_pr + 0.35 * rt_re
    # Ftotal = 0.7 * Frb + 0.3 * Frt
    # # print Ftotal


