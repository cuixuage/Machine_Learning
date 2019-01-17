# how can machines learn by distilling hidden features?
*deep learning challenges*
1.difficult structural decisions
比如使用Convolutional NNet for images
2.high model complexity
big enough data + regularizer(dropout,denoising)
3.hard optimization problem
careful initialization(pre-trained)
4.huge computational complexity
mini-batch with GPU

*pre-trained*
定义: 好的权重初始值尽可能的包含该层信息,权重信息是一种encoding
autoencoder,满足information preserving
即 gi(X) ≈ Xi
basic autoencoder只有三层网络,需要输入和输出个数相同
目标:输入值和输出值尽可能接近,e.g. squared error
限制条件: Wij == Wji,即编码权重和解码权重要保持一致(类似于regularizer)
autoencoder中的神经元个数和自定义网络结构中的下一层的神经元个数相同(这样使得Wij能用于自定义的网络结构)

*denoising Autoencoder*
混入一些noise数据,经过autoencoder后得到robust的权重,称之为denosing,去噪
这也起到了regularizer作用
note:
input有一部分是 noise+Xn,但是对应的output要求和Xn近似

*linear autoencoder*
之前神经网络模型中使用tanh()函数,autoencoder是非线性的
Principal component analysisPCA和linear autoencoder相关紧密
""跳过""
这里我没听明白


*总结*
1.autoencoder得到较好的初始化的权重,pre-trained
2.denoising通过引入噪声,使得weight robust。类似于data hint
3.介绍linear autoencoder(不太明白)
4.pre-training with denoising autoencoder (non-linear PCA) and fine-tuning with backprop for NNet with many layers
