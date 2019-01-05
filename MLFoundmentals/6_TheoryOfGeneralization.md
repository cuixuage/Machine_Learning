# why can machines learn？
一般化理论

术语:
1. shatter 对于N个点,能够分解为2^N中dichotomies
*shatter every dichotomy can be implemented*
e.g. 
对于样本数量N=2来说,如果break point=2,那么任意两个点都不能被shatter

2. 对于某个值N,成长函数mH(N)被break point影响(*小于breakpoint的点是shatter的*)

3.bounding Function
上界函数B(N,k): 当break point=k时,成长函数mH(N)可能的最大值
mH(N): 成长函数 分成多少种dichotomy(二分类)

4.结论
对于2D perceptrons感知机,break point=4, mH(N)的上界是N^(k-1)
如果能找到一个模型的breakpoint,且是有限大的 那么就可以推断出其成长函数mH(N)有界

==》 只要break point存在,那么机器学习就是可行的
