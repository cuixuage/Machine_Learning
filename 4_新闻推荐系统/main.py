#coding=utf-8
"""
Created on Sat Dec 26 14:06:08 2015
@author: Ldy
"""

import argparse
import collections
from operator import itemgetter
import numpy as np
from readfile import get_hot_news_rank_table
import pandas as pd
import sys
import logging

logging.basicConfig(filename='recommend.log', format='(%(levelname)s:%(asctime)%:%(message)s)', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)

def tagssim(SetA, SetB):
    '''
    计算两个关系集之间的相似度
    :param SetA:
    :param SetB:
    :return:
    '''
    sim = 0
    for key in SetA:
        if key in SetB:
            sim = sim + 1
    return sim


def dict_sort(dic):
    return sorted(dic.items(), key=itemgetter(1), reverse=True)


def get_key(dic, k):
    return map(itemgetter(0), sorted(dic.items(), key=itemgetter(1), reverse=True))[:k]


def count_list(a):
    counter = collections.Counter(a)
    return dict(counter)


#导入所有在训练集合中但不在测试集合中的用户id组成的表
diff_user = np.load('./data/diff_user.npy').item()                        #如何得到此文件？

# 导入用户特征表
user_tags = np.load('./data/user_feature.npy').item()

# 导入由新闻及其对应最高TFIDFT值的关键字组成的表
news_tags = np.load('./data/testing_data_freq_dict.npy').item()


# 导入测试数据集中由用户id和用户登录(点击)时间组成的表
user_time = np.load('./data/user_time_test_table.npy').item()

# 导入粉丝用户(数据集中点击新闻次数较多的用户)列表
hot_user = np.load('./data/hot_user.npy').item()                        #如何得到此文件？

U2U_tags = np.load('./data/U2U_tags.npy').item()                       #如何得到此文件？

# 导入测试数据集和训练数据集中同时出现过的用户的集合表
same_user = np.load('./data/same_user.npy').item()                      #如何得到此文件？

# print same_user
# 导入测试集中用户id和新闻id组成的表
user_news_dict = np.load('./data/user_news_dict.npy').item()


def calUUsim(k):
    '''
    计算用户之间的相似度
    :param k: 提取特征关键词的数量
    :return: 返回相似性标签
    '''
    U2U_tags = user_tags
    usei = 0
    for sameuse in same_user:
        usei = usei + 1
        sameusej = 0
        for diffuse in hot_user:

            if sameuse in user_tags.keys() and diffuse in user_tags.keys():
                sim = tagssim(user_tags[sameuse], user_tags[diffuse])
                if sim >= k:
                    sameusej = sameusej + 1
                    # print sameuse,usei,sameusej,sim
                    U2U_tags[sameuse] = set(list(user_tags[sameuse]) + list(user_tags[diffuse]))
                    # print sameuse, usei, len(U2U_tags[sameuse])  # ,U2U_tags[sameuse]==user_tags[sameuse]
    return U2U_tags


# print U2U_tags
def cbr(user_id, tags_data):
    '''
    :param user_id: 用户的id
    :param tags_data: 由calUUsim函数生成的用户相似度标签集合
    :return: 返回与输入用户相似的所有用户
    '''
    sims = {}
    for key in news_tags.keys():
        sims[key] = tagssim(tags_data[user_id], news_tags[key])
    return sims


def content_base(data, user_id, k=5):
    '''
    基于内容的推荐
    :param data: 数据集
    :param user_id: 用户id
    :param k: 需要返回的新闻个数
    :return: 相应用户可能会喜欢的k个新闻
    '''
    if user_id in user_tags.keys():
        sims = cbr(user_id, user_tags)
        return get_key(sims, k)
    else:
        return get_hot_news_rank_table(data, k=k, time_end=user_time[user_id], days=1)


def UUCF(data, user_id, k=5):
    '''
    基于用户的协同过滤
    :param data:
    :param user_id:
    :param k:
    :return:
    '''
    if user_id in U2U_tags.keys():
        sims = cbr(user_id, U2U_tags)
        return get_key(sims, k)
    else:
        return get_hot_news_rank_table(data, k=k, time_end=user_time[user_id], days=1)


def Rs_test(k):
    n1 = 0
    user_num = 0

    for user_id in user_news_dict.keys():
        i = 0
        user_num = user_num + 1
        # print user_num

        result = set(content_base(raw_data, user_id, k))
        for news_id in result:
            if news_id in user_news_dict[user_id]:
                i = i + 1
        m = 0
        if len(user_news_dict[user_id]) > k:
            m = k

        else:
            m = len(user_news_dict[user_id])
        if i >= m/2:
            n1 = n1 + 1
    n2 = 0
    user_num = 0
    for user_id in user_news_dict.keys():
        i = 0
        user_num = user_num + 1
        # print user_num

        result = set(UUCF(raw_data, user_id, k))
        for news_id in result:
            if news_id in user_news_dict[user_id]:
                i = i + 1
        m = 0
        if len(user_news_dict[user_id]) > k:
            m = k
        else:

            m = len(user_news_dict[user_id])
        if i >= m / 2:
            n2 = n2 + 1
    return n1, n2


if __name__ == '__main__':
    # parse = argparse.ArgumentParser(description=u'呵呵')
    parse = argparse.ArgumentParser()
    parse.add_argument('-m', '--method', help='Method of Recommend\n cb: contentbased\ncf: Collaborative filtering')
    parse.add_argument('-i', '--userid', type=int, help="The user's id to be recommended, such as 3506171 436906")

    args = parse.parse_args()


    users = user_tags.keys()
    if (args.method not in ['cb', 'cf']) or (args.userid not in users):
        print parse.print_help()
        sys.exit()

    raw_data = pd.read_csv('./data/news_id_time_table.csv').loc[:, ['news_id', 'read_time']]                    #这个文件又是如何得到的呢?

    if args.method == 'cf':
        news_ids = UUCF(raw_data, args.userid)
    elif args.method == 'cb':
        news_ids = content_base(raw_data, args.userid)
    news_id_title = np.load('./data/news_id_title.npy').item()
    print "向用户`{id}`推荐如下{k}篇新闻".format(id=args.userid, k=5).decode("utf8")
    string = '{num}.新闻id:`{id}`\t标题:{title}'
    for item, news_id in enumerate(news_ids):
        outputstr = string.format(num=item, id=news_id, title=news_id_title[news_id])
        print outputstr.decode("utf8")
        logging.debug(outputstr)

    # print Rs_test(20)