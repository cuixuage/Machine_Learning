# Nonlinear Transform
*基础*
feature transform特征转换
将x空间的点映射到高维Z空间,Z空间线性可分。

*非线性转换*
在Z域空间中利用线性分类模型进行分类训练
e.g. 计算二次项个数
如果x特征维度是d,那么二次多项式的Z域的特征维度是 d(d-1)/2 +d+d+1
参见课件习题
如果阶数更大的Z域,最高阶数是Q,其特征维度是 C Q/Q+d
note：
1.如果Q,d很大,虽然Ein会变小,但是模型的复杂度也会上升,使得Eout不一定下降
2.Z域的Weight维度越小,VC dimension越小,Hypothesis的自由度越小

*结论*
非线性分类问题:  将非线性模型映射到高维空间,再转换为线性分类问题
