#coding=utf-8
import numpy as ny
import pandas as pd
import matplotlib as mp
import scipy as sp
import sklearn as sl

# 本金10万元  初始股票价格9.22元  买入100000/9.22=10846支股票
#
# 注意:	由于计算过程中没有考虑复利情况(不考虑由于获得利润或者亏本的情况下导致的股票动态增加、减少)
# 	故此假设在后续计算利润中均按照10846支股票进行计算利润和

N = 100000/9.22;
data = pd.read_table('D:\\Pycharm\\projects\\test\\datafromSZ0001_day.txt')
feature_cols = ['BOLL', 'UPR', 'DWN']
X = data[['BOLL', 'UPR', 'DWN']]
y = data['CLOSE']
y = data.CLOSE
y_CLOSE = pd.Series.as_matrix(y)
# print type(y_CLOSE),len(y_CLOSE)
# print y_CLOSE

average_close=[]   ################close_price  average
for i in range(0,len(y_CLOSE)-1):
   temp = 0
   if i<len(y_CLOSE)-7:
      for j in range(0,7):
         temp += y_CLOSE[i+j]
      average_close.append(temp/8)
   else:
      for j in range(0,i-(len(y_CLOSE)-7)-3):
         temp += y_CLOSE[i+j]
         average_close.append(temp/(i-(len(y_CLOSE)-7)-3))
# print average_close
# print type(average_close),len(average_close)

def rule_1(week_idx):
   "time: week_idx  : average down and close_price > averge"
   if((average_close[week_idx] > average_close[week_idx-1]) \
              and (y_CLOSE[week_idx]>=average_close[week_idx])):
      return 1
   else:
      return 0

def rule_2(week_idx):
   "time: week_idx  : close-price < averge and average up"
   if((y_CLOSE[week_idx]<=average_close[week_idx]) \
              and(average_close[week_idx]>average_close[week_idx-1])):
       return 1
   else:
       return 0

def rule_3(week_idx):
    "time: week_idx: average >> close"
    if(average_close[week_idx] > y_CLOSE[week_idx]*1.2):
        return 1
    else:
        return 0

def rule_4(week_idx):
    "time: week_idx: close_price << average"
    if(y_CLOSE[week_idx] < average_close[week_idx]*0.8):
        return 1
    else:
        return 0

def rule_5(week_idx):
    "time: week_idx  : average_prive down and close_price down"
    if((average_close[week_idx] <= average_close[week_idx-1]) \
               and(y_CLOSE[week_idx] <= y_CLOSE[week_idx-1])):
        return  0
    else:
        return 1

def rule_6(week_idx):
    "time week_idx : average_price down and  close_price < average_price"
    if((average_close[week_idx] <= average_close[week_idx-1]) \
               and(y_CLOSE[week_idx] <= average_close[week_idx-1])):
        return 0
    else:
        return 1

def rule_7(week_idx):
    "time: week_idx : close << average_price and average down"
    if((average_close[week_idx] <= average_close[week_idx-1]) \
                and (y_CLOSE[week_idx] <= average_close[week_idx]*0.8)):
        return 0
    else:
        return 1

def rule_8(week_idx):
    "time : week_idx : close_price up and close_price >> average-price "
    if((y_CLOSE[week_idx] >= y_CLOSE[week_idx-1]) \
               and(y_CLOSE[week_idx] >= average_close[week_idx]*1.2)):
        return 0
    else:
        return 1

def choose_rule_final(week_idx):
    "count 1 0 to get final choose : if count(1) > count(0) bought ;else throw "
    count_1 = 0
    count_0 = 0
    ######################################rule 1 2 3 4
    if(rule_1(week_idx) == 1):
        count_1 +=1;
    if(rule_2(week_idx) == 1):
        count_1 +=1;
    if(rule_3(week_idx) == 1):
        count_1 +=1;
    if(rule_4(week_idx) == 1):
        count_1 +=1;
    ######################################rule 5 6 7 8
    if(rule_5(week_idx) == 0):
        count_0 +=1;
    if(rule_6(week_idx) == 0):
        count_0 +=1;
    if(rule_7(week_idx) == 0):
        count_0 +=1;
    if(rule_8(week_idx) == 0):
        count_0 +=1;
    ###########################result to bought or through
    if(count_1 >= count_0):
        return 1
    else:
        return  0

for week_idx in range(0,len(average_close)):
    temp = choose_rule_final(week_idx)
    profit = 0
    if(temp == 1):   #to buy and calculate profit
        profit -= (y_CLOSE[week_idx] - y_CLOSE[week_idx-1])*N
    else:
        profit += (y_CLOSE[week_idx] - y_CLOSE[week_idx-1])*N

print "股票个数:",N;
print "最终利润:",profit
#本金10万元 最终获取利润值为2060.73752711  大约为2千元