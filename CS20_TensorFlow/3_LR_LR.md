#世界银行出生率和生命周期的线性回归模型
1.读取数据
2.X,Y创建placeholder(步骤1的数据通过feed_dict传入)
3.创建tf var:w,b
4.定义最优化的函数(huber loss)
5.定义梯度下降的优化方法(min_Loss & Learning rate)
6.train model
```python
"""关键点
1.placeholder or dataset
2.optimizer是最小化损失函数的运算符
TF做执行优化器时,依赖于Loss函数,依赖于输入的X,Y ==> 构件计算图优化Weight,Bias
"""
```

#MNIST手写数字识别逻辑回归
Loss = cross_entropy(softmax + 交叉熵)
```python
#定义输入数据的形状
X = tf.placeholder(tf.float32, [batch_size, 784], name='image') 
Y = tf.placeholder(tf.int32, [batch_size, 10], name='label')
#隐层矩阵weights
w = tf.get_variable(name='weights', shape=(784, 10), initializer=tf.random_normal_initializer())
b = tf.get_variable(name='bias', shape=(1, 10), initializer=tf.zeros_initializer())
#定义Loss   
logits = tf.matmul(X, w) + b 
entropy = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y, name='loss')
```