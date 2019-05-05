#0.Reference  
美团FFM: https://tech.meituan.com/2016/03/03/deep-understanding-of-ffm-principles-and-practices.html     
CMUpdf: http://www.cs.cmu.edu/~wcohen/10-605/2015-guest-lecture/FM.pdf    
CSDN: http://www.52caml.com/head_first_ml/ml-chapter9-factorization-family/    
知乎: https://zhuanlan.zhihu.com/p/37963267    
  
#1.FM   
核心思想: 二阶特征组合;    
特征之间的隐向量的内积为特征之间的关联度(Wij)       
FM = LR + Wij<xi,xj> 对于特征xi,xj的组合   
Wij只能被xi，xj非零项计算,而原始类别转为的ont-hot数据非常稀疏   
**如何有效计算Wij？**   
W矩阵 = VT*V, W(n*n大小)用V(n*K计算)  
转化为N*K的权重矩阵
1.W矩阵的参数量减少为n*k个,原来是n*(n-1)/2
2.推导化简:   
转化线性求解问题  
http://www.algo.uni-konstanz.de/members/rendle/pdf/Rendle2010FM.pdf   
3.FM 和 二次多项式的SVM区别在哪里？  
**超参数k（隐向量长度）,反映FM模型的表达力**   

#2.FFM
核心:每一位特征和其他field关系都用一个隐向量表征  
FM: 属于FFM的特殊情况,每一维特征都相当于一个field   
e.g. 特征i,对于特征j的组合关系为:  
**特征i对于类别j的隐向量Vi,fj  (dot点乘)  特征j对于类别i的隐向量Vj,fi**  
隐向量的参数矩阵可以理解为:  
f个field,n维原始特征,隐向量的长度是k;  参数数量=f*n*k   
  
note:  
1.一个类别特征可能意味着500维的one-hot特征,非常稀疏    
2.FFM输入可以省去值为0的特征index(其对于模型的训练不起作用)     
**3.将源特征归一化,主要使得数值特征归一化到(0,1)之间 (归一化方法？？)**  

```python
# demo0: https://www.jiqizhixin.com/articles/2018-07-16-17
# demo1:  https://realxuan.github.io/2018/10/18/FM(Factorization%20Machine)%E6%A8%A1%E5%9E%8B/  
# demo2: http://nowave.it/factorization-machines-with-tensorflow.html
class FM(Model):
    def __init__(self,input_dim=None,output_dim=1,factor_orider=10,opt_algo='gd',learning_rate=le-2,l2_w=0,l2_v=0,random_seed=23):
        super().__init__(self)	
        #定义计算图
        self.graph = tf.Graph()
        with self.graph.as_default():
            if random_seed is not None:
                tf.set_random_seed(random_seed)
        #定义参数节点
        self.X = tf.sparse_placeholder(tf.float32, shape=[None, input_dim], name="X")
        self.y = tf.placeholder(tf.float32, shape=[None, output_dim], name="y")
        self.V = tf.get_variable("v", shape=[input_dim, factor_orider], dtype=tf.float32, initializer=tf.truncated_normal_initializer(stddev=0.3))
        self.W = tf.get_variable("Weights", shape=[n, 1], dtype=tf.float32, initializer=tf.truncated_normal_initializer(stddev=0.3))
        self.b = tf.get_variable("Biases", shape=[1, 1], dtype=tf.float32, initializer=tf.zeros_initializer())
        #定义模型
        #一阶部分
        xw = tf.sparse_tensor_dense_matmul(self.X, self.W)
        xv = tf.square(tf.sparse_tensor_dense_matmul(self.X, self.V))
        #二阶部分 multiply是矩阵对应元素相乘，matmul是矩阵乘法
        fm_hat = tf.reduce_sum(tf.square(tf.sparse_tensor_dense_matmul(self.X ,self.V)) - (tf.sparse_tensor_dense_matmul(tf.multiply(self.X,self.X), tf.multiply(self.V,self.V))), axis=1, keep_dims=True) / 2
        #fm函数
        logits = tf.reshape(b+xw+fm_hat,[-1])
        #通过sigmoid函数计算预测值
        self.y_ = tf.sigmoid(logits)
        #Loss = 交叉熵Error + l2正则
        self.loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logits, labels=self.y)) +l2_w * tf.nn.l2_loss(xw) + l2_v * tf.nn.l2_loss(xv)
        #模型的优化器
        self.optimizer = get_optimizer(opt_algo, learning_rate, self.loss)
        #初始化模型参数
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
```