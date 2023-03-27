李宏毅老师课程主页:http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML19.html     
或者FastAI课程主页: https://www.fast.ai/2019/07/08/fastai-nlp/      
     

# 0.前置基础    
RNN: 优点:可以获取全局信息  缺点:不能并行计算   
CNN: 优点:GPU并行计算  缺点:bigram仅能观察到本地信息   
self-attention层:  
x1: input sequence item   
a1: item embedding   
q1: query(match others), ==Wq * a1   
k1: key(to be matched by query), ==Wk * a1  
v1: information(to be exacted), ==Wv *a1   
   
# 1.self-attention   
1.1 scaled dot-product attention   
那每一个query，去对每一个key\value做attention   
![dot-product](./DL_picture/transformer1.png)  
1.2 aij softmax   
1.3 get bi     
b1 = sum(a1i * vi),相当于item i包含了全局信息   
![dot-product](./DL_picture/transformer2.png)  
1.4 矩阵运算   
self_attention转化为Q,K,V之间的矩阵运算,便于并行计算   
![dot-product](./DL_picture/transformer3.png)   
   
# 2.multi-head self-attention  
将输入ai,得到multi的Q,K,V矩阵   
相当于原来同一个位置的bi,产生多个。期望他们关注"不同"的全局信息   
![dot-product](./DL_picture/transformer4.png)   
   
# 3.position Encoding   
原有的selft-attention layer是没有位置信息,如何补充上位置信息呢?   
输入ai = ai+ei,ei embeddig是人为指定的。原理:   
![dot-product](./DL_picture/transformer5.png)    
   
# 4.Transformer   
Encoder的模块:    
4.1 input encoding & positional encoding   
4.2 multi-head attention   
4.3 add & norm    
add: 将输入ai 和 self-attention输出bi相加(而非concat), ==> ai + bi   
norm: layer_norm(ai+bi)    
备注: layer_num是将每一条数据的embedding归一化;   batch_num是将同一个维度数据做归一化   
   
Decoder的模块:   
4.4 masked multi-head attention    
decoder的输入是one step - one step的,需要做maskd矩阵以免无效的计算   
![dot-product](./DL_picture/transformer6.png)   
  
# 5.其它   
self-attention如何仅仅使用本地信息?   
计算bi时，将非本地的token的vi设置为0? 