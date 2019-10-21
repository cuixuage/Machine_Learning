1. tf.zeros(shape, dtype=tf.float32, name=None)
2. tf.zeros_like(input_tensor, dtype=None, name=None, optimize=True)
3. python all integers are the same type, but TensorFlow has 8-bit, 16-bit, 32-bit, and 64-bit integers available
注意:
Python native types: TensorFlow has to infer Python type
NumPy arrays: NumPy is not GPU compatible
numpy是无法在GPU上计算的
#4. 初始化
```python
# create variables with tf.get_variable
s = tf.get_variable("scalar", initializer=tf.constant(2)) 
m = tf.get_variable("matrix", initializer=tf.constant([[0, 1], [2, 3]]))
W = tf.get_variable("big_matrix", shape=(784, 10), initializer=tf.zeros_initializer())
with tf.Session() as sess:
	sess.run(W.initializer)
	print(W.eval())
#tf.constant is an op
#tf.Variable is a class with many ops
```
#5. Placeholders
