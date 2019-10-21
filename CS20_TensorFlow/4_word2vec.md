1.eager execution写法(TF语言的便捷化API)
2.word2vec
```python
"""关键点
1.所有单词的embedding初始化   (输入层)
2.隐层权重的weights初始化     (隐层)
"""

""" Step 2 + 3: define weights and embedding lookup.
In word2vec, it's actually the weights that we care about 
"""
with tf.name_scope('embed'):
    embed_matrix = tf.get_variable('embed_matrix', 
                                    shape=[VOCAB_SIZE, EMBED_SIZE],
                                    initializer=tf.random_uniform_initializer())
    embed = tf.nn.embedding_lookup(embed_matrix, center_words, name='embedding')

# Step 4: construct variables for NCE loss and define loss function
with tf.name_scope('loss'):
    nce_weight = tf.get_variable('nce_weight', shape=[VOCAB_SIZE, EMBED_SIZE],
                    initializer=tf.truncated_normal_initializer(stddev=1.0 / (EMBED_SIZE ** 0.5)))
    nce_bias = tf.get_variable('nce_bias', initializer=tf.zeros([VOCAB_SIZE]))

    # define loss function to be NCE loss function
    loss = tf.reduce_mean(tf.nn.nce_loss(weights=nce_weight, 
                                        biases=nce_bias, 
                                        labels=target_words, 
                                        inputs=embed, 
                                        num_sampled=NUM_SAMPLED, 
                                        num_classes=VOCAB_SIZE), name='loss')
```
