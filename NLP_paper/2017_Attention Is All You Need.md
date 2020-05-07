论文原文: https://arxiv.org/abs/1706.03762  
代码实现:https://github.com/Kyubyong/transformer   
按照原文结构记录总结

#1.Model Architecture    
**1.1.Encoder&Decoder stacks**  
stacks = 6 transformer      
sublayers = multi-head attention + FeedFormward     
Embedding dimension = 512      
主要学习代码实现: 1.self-attention 2.positional encoding 3.Masked     
Encoder input = [batchsize,seq_length,512]  
Encoder output =  [batchsize,seq_length,512] ？？？？ key？  

**1.2.Attention**  
multi-heads = 8   
```
a. Decoder Layer = 3 sublayers    
self-attention + Encoder-Decoder-attention + FeedwardNet   
Encoder-Decoder-attention = Keys,Values来自于Encoder; query来自于上一层的Decoderlayer   

b.Encoder self-attention,keys+values+querys来自于相同的位置      

c.Decoder self-attention,训练过程中masked操作,保证当前时间步的Decoder仅能看到左侧的单词信息   
```   
代码实现,主要关注self-attention的实现:  


**1.3 position-wise Feed-Forward Net**  
前向网络对于每一个位置的embedding进行两次线性变换  
原文描述:可以把它想象成两次kernel size=1的卷积网络  (???)  
  
**1.4 Embedding&softmax**  
embedding layer共享权重,但是额外乘以参数根号dmodel  (???)  
比如: embedding dimension=512, 需要乘以22  

**1.5 positional Encoding**  
位置编码,提前计算的数值,直接加到相应位置的embedding即可  
  
**2.Why self-attention**  
探讨时间复杂度问题 seq_length=N; representation dimension=d; CNN kernel width=k  
self-attention = N^2*d  
RNN = N*d^2  
CNN = k*N*d^2  
1.只有当N<D时，seq_length比较小的时候,self-attention才存在计算优势   
2.CNN kernel区分距离的远近;self-attention所有单词距离都是1   

#3.Traning    
```
1.update weight = Adam optimizer * 衰减Learning rate  

2.正则项 = dropout + label smoothing
embedding layer也会进行dropout
标签平滑超参=0.1
```     

#4.Results  
1.mutli-head不宜过多   
2.更复杂的模型一般表现更好,dropout很关键   
3.自学习的position encoding没有明显帮助   


#参考引用
1.seq2seq https://github.com/NLP-LOVE/ML-NLP/tree/master/NLP/16.5%20seq2seq     
每一层Decoder的输入= encoder的输出向量 + Decoder的上一时间步的输出     
2.Transformer http://jalammar.github.io/illustrated-transformer/     
3.官方API https://github.com/tensorflow/tensor2tensor      
4.本文参考的实现代码 https://www.cnblogs.com/zhouxiaosong/p/11032431.html

#代码引用
1.self-attention    
具体参见代码:   https://github.com/Kyubyong/transformer/blob/fb023bb097e08d53baf25b46a9da490beba51a21/modules.py#L153    
```
注意点:   
1.输入: [N, T_q, d_model]   输出: [N, T_q, d_model]   
2.multi-head   
3.decoder self-attention用到padding_mask + senquence_mask   
```
   
2.encoder-decoder attention   
query: previous decoder output [N, T_q, d_model]   
key=value：encoder output [N, T_q, d_model]   
具体参见代码:
https://github.com/Kyubyong/transformer/blob/fb023bb097e08d53baf25b46a9da490beba51a21/model.py#L111  
```
注意点:
1.padding mask是key_mask
```

3.Others
3.1 LR warmup实现
3.2 add&normalization实现
3.3 label smoothing实现

后续计划学习bert论文，学习其代码实现的create_mask。 以上的代码实现的padding_mask,sequence_mask感觉不够通用