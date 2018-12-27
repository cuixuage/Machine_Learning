#coding=utf-8
import pandas as pd
import numpy as np
import time
import os
import jieba
import jieba.analyse                            #避免jieba找不到analyse
from collections import Counter


def get_data(filename, sep, headers=None, names=None, septime="2014-03-06 20:38:35"):
    '''
    从filename获取数据去重之后返回训练集和测试集
    :param filename: 数据集文件名
    :param sep: 数据之间的分隔符
    :param headers: headers
    :param names: 数据列名
    :param septime: 分隔训练集和测试集的时间界
    :return: 整个数据集 训练集 测试集合 pandas.DataFrame格式
    '''

    raw_data = pd.read_table(filename, sep='\t', header=None, names=names).dropna(how='any')

    read_times = raw_data['read_time']
    #sep_time = "2014-03-20 23:59:00"
    sep_time = "2014-03-06 20:38:35"
    time_array = time.strptime(sep_time, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(time_array))

    index_before_sep_time = read_times.index[read_times < timestamp]
    index_after_sep_time = read_times.index[read_times >= timestamp]

    training_data = raw_data.drop(index_after_sep_time)
    testing_data = raw_data.drop(index_before_sep_time)

    return raw_data, training_data, testing_data


def create_TFIDF_table(file_name, data):
    '''
    计算新闻的TFIDF值,返回每个新闻值最大的前10个关键词
    :param data:  The DataFrame where id and content exist
    :param id: The id of news
    :param content: The content of news
    :return: The frequence dict of each news
    '''

    id = 'news_id'
    content = 'news_content'
    news_id_content = data.loc[:, [id, content]].drop_duplicates().values

    freq_dict = {}
    for id, content in news_id_content:
        freq_dict[id] = set(jieba.analyse.extract_tags(content, topK=10))

    np.save(file_name, freq_dict)


def create_user_feature_table(file_name, training_data):
    '''
    返回每个用户的读过的新闻中最重要的关键词
    :param file_name:
    :param training_data:
    :return:
    '''
    user_id_news = training_data.loc[:, ['user_id', 'news_content']]
    grouped = user_id_news.groupby('user_id')
    user_dict = {}

    for name, df in grouped:
        strs = [content for id, content in df.values]
        strs = '.'.join(strs)
        features = set(jieba.analyse.extract_tags(strs, topK=10))

        user_dict[name] = features
    np.save(file_name, user_dict)


def create_test_user_time_table(file_name, testing_data):
    '''
    返回测试集中用户id和最后一次阅读时间组成的表
    :param file_name:
    :param testing_data:
    :return:
    '''

    user_id_news = testing_data.loc[:, ['user_id', 'read_time']]

    user_dict = {}

    for userid, readtime in user_id_news.values:
        user_dict[userid] = readtime

    np.save(file_name, user_dict)


def create_news_id_read_time_table(file_name, data):
    '''
    返回新闻id和阅读时间对应的表
    :param file_name:
    :param data:
    :return:
    '''
    id_time = data.loc[:, ['news_id', 'read_time']]
    id_time.to_csv(file_name)


def get_hot_news_rank_table(data, k=3, time_end=1394788902, days=1):
    '''
    :param data:
    :param time_start:
    :param time_range:
    :return: 返回新闻在给定时间出现次数的Counter计数器
    '''
    time_range = days * 24 * 3600
    news_id_pubtime = data.loc[:, ['news_id', 'read_time']]
    news = news_id_pubtime[news_id_pubtime['read_time'] < time_end]
    news = news[news['read_time'] > time_end - time_range]
    newsid = news.loc[:, 'news_id']
    counter = Counter(newsid.values)
    result = [ituple[0] for ituple in counter.most_common(k)]
    return result


if __name__ == '__main__':
    filename = './data/user_click_data_brief.txt'
    sep = '\t'
    names = ['user_id', 'news_id', 'read_time', 'news_title', 'news_content', 'news_publi_time']
    raw_data, training_data, testing_data = get_data(filename, sep, names=names)

    news_id_title = raw_data.loc[:, ['news_id', 'news_title']].drop_duplicates()

    news_id_title = news_id_title.values.tolist()
    idtitledict = {}
    for value in news_id_title:
        idtitledict[value[0]] = value[1]

    np.save('./data/news_id_title.npy', idtitledict)

    # import jieba.analyse

    filepath = './data/testing_data_freq_dict.npy'
    if not os.path.exists(filepath):
        create_TFIDF_table(file_name=filepath, data=testing_data)
    test_news_id = list(testing_data['news_id'].values)
    test_user_id = list(testing_data['user_id'].values)
    test_news_title = list(testing_data['news_title'].values)

    news_id_title = zip(test_news_id, test_news_title)

    news_id_title_dict = {}
    for news_id in set(test_news_id):
        news_id_title_dict[news_id] = set()
    for i in xrange(len(news_id_title)):
        news_id_title_dict[news_id_title[i][0]].add(news_id_title[i][1])

    # test_read_time = list(testing_data['read_time'].values)
    # test_newstotimes = zip(test_news_id, test_read_time)
    # user_news = zip(test_user_id, test_news_id)
    # user_news_dict = {}
    # for user in set(test_user_id):
    #     user_news_dict[user] = set()
    # for i in xrange(len(user_news)):
    #     user_news_dict[user_news[i][0]].add(user_news[i][1])
    np.save('./data/news_id_title_dict.npy', news_id_title_dict)
    # np.save('./data/user_news_dict.npy', user_news_dict)
    # print user_news
    # np.save('../data/user_news.npy', user_news)

    test_news_id = list(testing_data['news_id'].values)
    test_read_time = list(testing_data['read_time'].values)
    test_newstotimes = zip(test_news_id, test_read_time)
    # print len(test_newstotimes)

    test_user_id = set(list(testing_data['user_id'].values))
    # np.save('../data/test_user_id.npy', test_user_id)

    tran_news_id = list(training_data['news_id'].values)
    tran_user_id = set(list(training_data['user_id'].values))
    # np.save('../data/tran_user_id.npy', tran_user_id)
    tran_read_time = list(training_data['read_time'].values)
    tran_newstotimes = zip(tran_news_id, tran_read_time)
    # print len(tran_newstotimes)
    newstotimes = test_newstotimes + tran_newstotimes
    # print len(newstotimes)

    # np.save('../data/newstotimes.npy', newstotimes)

    tran_user_fre = list(training_data['user_id'].values)
    # np.save('../data/tran_user_fre.npy', tran_user_fre)

    feature_path = './data/user_feature.npy'
    if not os.path.exists(feature_path):
        create_user_feature_table(feature_path, training_data)
    user_feature = np.load(feature_path).item()

    # np.save('../data/newstotimes.npy', newstotimes)
    #    feature_path = '../data/user_feature.npy'
    #    if not os.path.exists(feature_path):
    #        create_user_feature(feature_path, training_data)
    #    user_feature = np.load(feature_path).item()

    # filepath = '../data/testing_data_freq_dict.npy'
    # if not os.path.exists(filepath):
    #     createFreqDict(file_name=filepath, data=testing_data)
    #
    # feature_path = '../data/user_feature.npy'
    # if not os.path.exists(feature_path):
    #     create_user_feature(feature_path, training_data)
    # user_feature = np.load(feature_path).item()

    get_hot_news_rank_table(training_data)
    filename = './data/user_time_test_table.npy'
    create_test_user_time_table(filename, testing_data)
    # filename = '../data/news_id_time_table.csv'
    # create_news_id_read_time_table(filename, raw_data)