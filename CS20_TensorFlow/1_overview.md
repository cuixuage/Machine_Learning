1. graph & session
2. sessions deal with memory allocation (处理内存空间的分配)
3. scalar,vector,matrix
```py
import tensorflow as tf
a = tf.add(3, 5)
# print(a)
with tf.Session() as sess:
	print(sess.run(a)) #如果没有session_run,得到是 add operator
```
4. 多GPU计算是把计算图做分割？ e.g. AlexNet是把96个Kernel划分到两个GPU
5. Distributed Computation
6. multi graph require multi session
7. 