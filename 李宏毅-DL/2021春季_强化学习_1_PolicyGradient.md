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
  
  
  


#############################################################  以下是2018年PPO策略的课程
https://youtu.be/z95ZYgPgXOY  Policy Gradient(Review)    
https://youtu.be/OAKAZhFmYoI  PPO   (**再次听一遍**) 
  
**1.Policy Gradient**  
    i.基础知识:  
        Policy = 输入:机器的观察环境的特征  输出:actor目前执行的行为    
        Expected Reward = 奖励的"期望值" （因为由于action、environment的随机性，导致奖励值具有随机性）  
![dot-product](./DL_picture/PPO_1.png)      
  
    ii.如何优化"Reward"的最大值呢？    
        Policy Gradient  
![dot-product](./DL_picture/PPO_2.png)   
        直观理解: 如果State1采用action1，导致最终的Reward是负数，那么就要减少State1采用Action1的概率；否则就增加Action1的概率  
        直观理解: action作为分类问题来选择。  
    
**2.训练技巧tips**    
    i.Reward总是正数,会存在哪些问题？ ==> Add a Baseline Score   
![dot-product](./DL_picture/PPO_3.png)     
    
    ii."Reward"作为Action的权重，会存在哪些问题？ ==> Assign Suitable Credit   
![dot-product](./DL_picture/PPO_4.png)

**Proximal Policy Optimization (PPO)**
3.On-Policy Off-Policy
    i. 两者的区别?
        Actor for interacting, 行为策略——不是当前策略，用于产出数据 
        Actor to train, 目标策略——会更新的策略，是需要被优化的策略
        如果两个策略是同一个策略，那么我们称为On Policy，在线策略。如果不是同一个策略，那么Off Policy，离线策略

    ii. 转化为off-policy策略
        off-policy的训练数据可以反复使用，训练时长更少。 PPO的作用就是将On-Policy策略转化为Off-Policy策略。
        a.importance sampling


