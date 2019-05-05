
# skip-gram算法原理

**1.input,output,target**
input的某个单词的one-hot编码（1*1000 词汇量的总数目）
output其他所有单词的概率（softmax  输出也是1*1000）
target是相近单词的one-hot形式

**2.Loss**   
target和output的矩阵的交叉熵最小 or 平方差最小    
    
**3.NNet**   
3.1 隐层    
300个神经元,需要训练的权重矩阵大小是1000*300    
本层的输出是:  1*1000 . 1000*300 = 1*300;    
单词的词汇向量表示为1*300; 单词的vector,embedding.    
3.2 输入层    
输入层是one-hot,并不需要实际计算矩阵运算,只需按照ont-hot的特点对于隐层权重值做lookup table"查找表"    
（输入层相当于投影层, https://zhuanlan.zhihu.com/p/27234078）  
3.3 输出层  
softmax回归分类器  
对于每一个节点的输出一个概率,output 1*1000  
3.4 意义  
两个单词拥有相似的“上下文”, 这两个词语的embedding features vector也会非常近似  
  
**4.优化**  
word2vec是一个权重规模非常大的神经网络 => gradient descent slowly  
1.word pairs and "phases"  
单词组合pair作为单个word来处理. e.g. "New York"  
2.高频词抽样来减少训练样本   
e.g. 在windows_size中遇到的每一个单词都有被删除的概率,词频越大越容易被删除   
超参:    
采样率阈值sample,默认0.001 词频大于0.001的会有一定可能被删除？   
https://zhuanlan.zhihu.com/p/27234078   
3.负采样   
negative sampling每个训练样本只更新对应target的节点+随机5-10个negative节点   
target节点: 目标的ont-hot编码形式中值为1对应的神经元(此节点期望输出1)   
negative节点: 其余的9999个节点(这些节点我们都期望其输出0)    
3.1如何随机选择negative节点呢？   
一元分布模型 unigram distribution来选择negative_words    
一个单词被选作negative sample的概率跟它出现的频次有关，出现频次越高的单词越容易被选作negative words    
https://zhuanlan.zhihu.com/p/27234078    