李宏毅老师课程主页:http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML19.html     
或者FastAI课程主页: https://www.fast.ai/2019/07/08/fastai-nlp/   



# 0. 前置基础   
word can have multiple sense.   
e.g. bank is word type, can be multiple word tokens   
contextalized embedding: 同一个word type，在不同的上下文中，有不同的word embedding   
   
# 1. ELMO   
embedding from Language Model 语言模型   
RNN-based language models(trained from lots of sentences)  
e.g.对于某个句子，如何计算某个token的embedding？   
A:将bi-RNN的某个token的前后两个hidden states,拼接起来作为当前token的embedding  
![dot-product](./DL_picture/bert1.png)   
    
# 2. BERT   
bi-directional encoder representation for transformer   
bert = encoder of transformer   
备注:训练bert是不需要label的;半监督的==其实还是有label的; learned from a large amount of text without annotaion   
![dot-product](./DL_picture/bert2.png)   
**如何训练bert呢？**   
2.1 方法: masked LM   
predicting the masked word ; linear multi-class classifier   
线性分类器预测被masked的词汇,该masked token输出是一个embedding ==> 分类问题   
![dot-product](./DL_picture/bert3.png)   
2.2 方法: nexted sentence prediction
CLS: the position that outputs classification results  
SEP: the boundary of two sentences   
预测两个句子是否是相连的; CLS是句子的首端,其输出的embedding再过一个线性分类器,判断是否相连   
![dot-product](./DL_picture/bert4.png)   
**有哪些应用场景呢？**    
2.1 情感分析,文档分类  
CLS单词作为输出,再过linear classifier  
2.2 Slot filling   
2.3 自然语言推理  
premise,hypothesis。类似应用场景2.1    
2.4 问答场景    
**各种场景,那些layer更有效？"   
![dot-product](./DL_picture/bert5.png)   
    
# 3. ERNIE   
enhanced representation through knowledge integration   
为了中文所设计的模型   
训练ernie时,采用"masked prase"; 训练bert时,采用"masked character"    
    
# 4. GPT   
generative pre-training; 生成式预训练模型    
GPT = transformer decoder; 给一个单词输入,可以不断去生成一篇文章 :)   
![dot-product](./DL_picture/bert6.png)   
![dot-product](./DL_picture/bert7.png)   


• Unified Language Model Pre-training for Natural Language Understanding and Generation   
• https://arxiv.org/abs/1905.03197   
• BERT has a Mouth, and It Must Speak: BERT as a Markov Random Field Language Model    
• https://arxiv.org/abs/1902.04094   
• Insertion Transformer: Flexible Sequence Generation via Insertion Operations   
• https://arxiv.org/abs/1902.03249  
• Insertion-based Decoding with automatically Inferred Generation Order   
• https://arxiv.org/abs/1902.01370    