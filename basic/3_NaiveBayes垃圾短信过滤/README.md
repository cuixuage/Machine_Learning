**不同特征提取方式对比**  
Recall    被预测正确的垃圾短信 占据所有被预测为垃圾短信的比例  
Precision 被预测正确的垃圾短信 占据所有真实垃圾短信的比例   
Naive Bayes  
CountVectorizer  
Recall: 0.976744186047  
Precision: 0.867826279637  
  
MI  
len_termset： 329322  
(640000, 50000)  
(160000, 50000)  
Recall: 0.835363929045  
Precision: 0.868592057762  
1052.95700002 s 
 
IG  
len_termset： 329322  
(640000, 50000)  
(160000, 50000)  
Recall: 0.983839404078  
Precision: 0.824297879092  
3128.33699989 s  

WLLR  
[u'.', u'x', u'\u4ef7\u94b1', u'xx', u'xxx', u'\u4f18\u60e0', u'\u6253\u6298', u'\u60a8\u597d', u'xxxxxxxxxxx', u'\u6d3b\u52a8']  
len_termset： 329322  
(640000, 50000)  
(160000, 50000)  
Recall: 0.98232434821  
Precision: 0.841954333947  
4560.56900001 s  
 

