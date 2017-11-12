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
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA
from sklearn import metrics
# import gensim

def loadClassData(filename):
    dataList  = []
    for line in codecs.open('../data/'+filename,'r',encoding = "utf-8").readlines():#读取分类序列
        dataList.append(int(line.strip()))
    return dataList

def loadTrainData(filename):
    dataList  = []
    for line in codecs.open('../data/'+filename,'r',encoding = "utf-8").readlines():#读取分类序列
        dataList.append(line.strip())
    return dataList

def loadTestData(filename):
    dataList  = []
    for line in codecs.open('../data/'+filename,'r',encoding = "utf-8").readlines():#读取分类序列
        dataList.append(line.strip())
    return dataList

def writeFinalRes(preLabel,filename):
    fr = codecs.open("../NolabelTestData.txt",encoding = "utf-8")
    fout = codecs.open('../data/' + filename, 'a+',encoding = "utf-8")
    arrayOfLines = fr.readlines()
    count =0
    for line in arrayOfLines:
        if count < len(preLabel):
            line = line.strip()  #移除字符串头尾指定的字符 默认为空格
            # if len(line) == 1:
            #     line += '空'.encode('UTF-8')
            appendTestLabel(fout,preLabel,line,count, filename)
            count +=1
            # print type(preLabel[count])
    fout.close()

def appendTestLabel(fout,preLabel,line,count,filename):
    # wordList = list(preLabel)
    outStr=""
    outStr += str(preLabel[count])+'\t'+line
    # outStr +=line
    fout.write(outStr + '\n')


# #navie bayes classifier
# def nbClassifier(trainData,testData,trainLabel):
#     vectorizer = CountVectorizer(binary=True)
#     fea_train = vectorizer.fit_transform(trainData)  #标记和计算一个语料的词频
#     fea_test = vectorizer.transform(testData);    #在训练语料中没有出现的词在后续调用转化方法时将被完全忽略  Not use the fit_transform
#
# #     tv=TfidfVectorizer()#该类会统计每个词语的tf-idf权值
# #     fea_train = tv.fit_transform(trainData)    #return feature vector 'fea_train' [n_samples,n_features]
# #     fea_test = tv.transform(testData);
#
#     # print 'Size of fea_train:' + repr(fea_train.shape)
#     # print 'Size of fea_test:' + repr(fea_test.shape)
#     # print fea_train.nnz
#     # print fea_test.nnz
#
#     clf = MultinomialNB(alpha = 0.01)
#     clf.fit(fea_train,np.array(trainLabel))
#     pred = clf.predict(fea_test)
#     writeFinalRes(pred, 'FinalResult.txt')


def nbClassifier(trainData,testData,trainLabel,testLabel):
    vectorizer = CountVectorizer(binary=True)
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

    rb_pr = 1.0 * D / (B + D)
    rb_re = 1.0 * D / (C + D)
    rt_pr = 1.0 * A / (A + C)
    rt_re = 1.0 * A / (A + B)
    print  "Recall:",rb_re
    print  "Precision:",rb_pr
    # Frb = 0.65 * rb_pr + 0.35 * rb_re
    # Frt = 0.65 * rt_pr + 0.35 * rt_re
    # Ftotal = 0.7 * Frb + 0.3 * Frt
    # # print Ftotal

if __name__ == "__main__":
    t1 = time.time()
    trainCorpus = []
    classLabel = []

    classLabel = loadClassData('classLabel.txt')
    trainCorpus = loadTrainData('trainLeft.txt')  # trainleftstop.txt'
    testCorpus = loadTestData('testLeft.txt')
    length = len(classLabel)
    # trainData, testData, trainLabel, testLabel = train_test_split(trainCorpus, classLabel, test_size=0.2)

    # trainData=trainCorpus
    # trainLabel=classLabel
    # testData=testCorpus

    # logisticReg(trainData,testData,trainLabel,testLabel)  #98.5
    # ldaClassifier(trainData,testData,trainLabel,testLabel) #53.5

    print '*************************\nNaive Bayes'
    # create the Multinomial Naive Bayesian Classifier
    # nbClassifier(trainData, testData, trainLabel, testLabel)
    # nbClassifier(trainData, testData, trainLabel)
    # t2 = time.time()
    # print t2 - t1, 's'

    trainData, testData, trainLabel, testLabel = train_test_split(trainCorpus, classLabel, test_size=0.2)
    nbClassifier(trainData, testData, trainLabel,testLabel)