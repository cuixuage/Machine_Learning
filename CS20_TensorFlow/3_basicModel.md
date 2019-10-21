https://github.com/chiphuyen/stanford-tensorflow-tutorials

1. overview
tf.constant and tf.Variable  常量和变量
tf.placeholder and feed_dict 占位符和feed_dict

2. Huber Loss
```python
def huber_loss(labels, predictions, delta=14.0):
    residual = tf.abs(labels - predictions)
    def f1(): return 0.5 * tf.square(residual)
    def f2(): return delta * residual - 0.5 * tf.square(delta)
    return tf.cond(residual < delta, f1, f2)
```

3. tf.data
DataSet,iterator,shuffle\repreat\batch
4. optimizer

代码实现:
# 5.线性回归 出生率和死亡率
# 6.逻辑回归 手写字符识别 