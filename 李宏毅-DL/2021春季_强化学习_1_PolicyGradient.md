强化学习-PPO基础概念   
https://speech.ee.ntu.edu.tw/~hylee/ml/2021-spring.php   2021春季RL课程  
  
**1.RL基础概念**    
    i.policy Network(Actor)  
    ii.Define Loss损失函数 (Maximize Reward)  
    iii.Optimization  
        由于Reward、ENV存在随机性，因此优化模型的步骤是RL的最主要的挑战    
  
**2.Policy-Gradient**  
挑战点: How to control your actor?  ==> 选择合适的Loss  
    i. 采取action1, 用交叉熵, 使得两者分布越近约好  
    ii. 避免采取action1, 采用交叉熵的负数, 使得两者分布越远越好  
  
挑战点: Training Data?  
    i. Version 0, 没有考虑后续Action的影响，导致Reward过于单一, Actor仅仅学会"开火", 无法学习到左右移动  
    ii. Version 1, 当前Action的Reward等于后续所有步骤的Reward之和。  
    iii. Version 3, Reward是相对的，如果全部都是正数，需要对Reward做"标准化"，减去"baseline"值  
训练耗时:  
    通常训练方式，a.先收集训练语料  b.接着For循环-Iteration训练  
    RL模型的训练方式:  a.For循环-Iteration训练    b.每次迭代过程中，重新收集训练语料  （缺点: 反复收集新的训练资料）  
  
On-Policy， Off-Policy（PPO策略，提升训练速度）  
  


