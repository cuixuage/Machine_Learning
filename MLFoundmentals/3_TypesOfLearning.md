# 机器学习的分类
1.out space
对于输出空间的不同可以分为:
离散值: 二元分类 多元分类
连续值: 回归(e.g. 预测 估计问题)
结构化学习: nlp的句法分析

2.data label
supervised: 可以是二元,多元,分类问题. 但是要求给定所有的label yn
un-supervised: 聚类 e.g.话题topic 异常检测
semi-supervised: expensive data label e.g. 药物检测
reinforcement: 输入x,输出y,评判y的优劣reward。"反馈-修正" e.g. 根据用户点击,选择而不断改进的广告系统

3.protocol
batch-learning    最广泛
online-learning   PLA\Reinforcement  两种算法十分适合在线学习  不断修正mistake
active-learning   机器主动地提问 减少标记的时间成本

4.input space
concrete Features: 具体的特征  e.g.硬币分类的尺寸 重量;手写数字的对称性,密度(slides P31)  这也是Machine最容易理解的特征
raw Features: e.g.数字所在图像的像素,音频的频谱等等   经常需要人或机器来转换为concrete Features 这个过程就是Feature Transform
abstract Features: e.g. 资料编号ID  这些特征十分抽象 没有实际物理含义 需要更多的转换和提取

本节课按照输出空间,数据标签,协议,输入空间四种来介绍ML的问题情形
