#CNN解决手写数字识别的分类问题  
1.MINIST with CNN    
tf.nn.conv2d(image,kernel,stride=[1,1,1,1],padding='SAME')  
步长维度: batchsize,height,width,channel   
   
2.Dimension计算   
W−F+2P)/S+ 1    
W: input width	/depth	F: filter width/depth    
P: padding			S: stride    

3.inference写法  
注意变量作用域的问题     
CS20课程的例子:       https://github.com/chiphuyen/stanford-tensorflow-tutorials/blob/master/examples/07_convnet_mnist.py    

使用tf.layers   
https://github.com/chiphuyen/stanford-tensorflow-tutorials/blob/master/examples/07_convnet_layers.py