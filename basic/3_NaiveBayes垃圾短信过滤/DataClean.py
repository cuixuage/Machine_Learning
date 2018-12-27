# -*- coding: utf-8 -*-
# 预处理短信信息

import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#from langconv import *
import jieba
import re


# 加载数据
def LoadData(file):
    print "Loading file " + file
    # input_data = codecs.open(file, 'r', 'UTF-8')
    input_data = codecs.open(file, 'r', "utf-8")
    return input_data.readlines()


# 加载数据，并分离垃圾短信与非垃圾短信
# train.utf8:文本内容
# feature.utf8:类别信息
# normal.utf8: 正常短信文本
# sms.utf8: 垃圾短信
# def get80w(input_data):
#     print "Get content of 80w"
#     #     output_class = codecs.open("../content/feature.utf8",'w','utf-8')
#     #     output_data = codecs.open("../content/80W.utf8", 'w', 'utf-8')
#     output_sms = codecs.open("../NormalAndSMS/sms.utf8", 'w', 'utf-8')
#     output_normal = codecs.open("../NormalAndSMS/normal.utf8", 'w', 'utf-8')
#     num = 0
#     for line in input_data:
#         num += 1
#         content = line.split("\t")
#         #         output_class.write(content[1] + "\n")
#         #         content = tradition2simple(content[2])
#         #         output_data.write(content)
#         if content[1] == '1':
#             output_sms.write(content[2])
#         else:
#             output_normal.write(content[2])
#
#         # if num % 200000 == 0:
#         #     t = num * 100 / 800000
#         #     print "Normal " + str(t) + "%" + "over!"
#
#             #     output_class.close()
#             #     output_data.close()
#     output_sms.close()
#     output_normal.close()
#     print "Get 80w end!"


# 加载数据，处理测试数据
# test.utf8:文本内容
# def get20w(input_data):
#     print "Get content of 20w"
#     output_content = codecs.open("../content/20W.utf8", 'w', 'utf-8')
#
#     num = 0
#     for line in input_data:
#         num += 1
#         content = line.split("\t")
#         content = tradition2simple(content[1])
#         output_content.write(content)
#
#         if num % 50000 == 0:
#             t = num * 100 / 200000
#             print "SMS " + str(t) + "%" + "over!"
#
#     output_content.close()
#     print "Get 20w end!"


# 繁体转换为简体
# def tradition2simple(line):
#     # 将繁体转换成简体
#     line = Converter('zh-hans').convert(line.decode('utf-8'))
#     line = line.encode('utf-8')
#     return line


# 结巴分词
def jie(content):
    r = '[.【 】/《 》=☆*}{]'
    temp = re.findall(r.decode(), content)
    content = re.sub(r.decode(), "".decode(), content)
    content = jieba.cut(content)
    content = " ".join(content) + " ".join(temp)
    #     content = jieba.cut(content)
    return content


# 去除标点符号
def deleteSymbol(content):
    #     r= '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
    r = '[：、]+'
    content = re.sub(r.decode("utf-8"), ' '.decode("utf-8"), content)
    return content


# 提出点.
def deleteDoc(content):
    r = '[.【 】/《 》=☆*}{]'
    # ●（）。:！
    temp = re.findall(r.decode(), content)
    content = re.sub(r.decode(), "".decode(), content)
    content = content + ' ' + " ".join(temp)
    return content


# 替换银行卡号
def changeNumber(content):
    #     r = '\\d{23,}'         #去掉长度大于23位的数字
    #     content = re.sub(r.decode(), "".decode(),content)
    #     r = '\\d{22}'    #电话号码
    #     content = re.sub(r.decode(), "ttttttttttt:ttttttttttt".decode(),content)
    #     r = '\\d{20}'    #订单号
    #     content = re.sub(r.decode(), "dddddddddddddddddddd".decode(),content)
    #     r = '\\d{19}'    #银行卡号
    #     content = re.sub(r.decode(), "yyyyyyyyyyyyyyyyyyy".decode(),content)
    #     r = '\\d{17,}'    #身份证号
    #     content = re.sub(r.decode(), "iiiiiiiiiiiiiiiiii".decode(),content)
    #     r = '\\d{16}'    #订单号
    #     content = re.sub(r.decode(), "dddddddddddddddd".decode(),content)
    #     r = '\\d{12}'    #号码
    #     content = re.sub(r.decode(), "dddddddddddd".decode(),content)
    #     r = '\\d{11}'    #电话号码
    #     content = re.sub(r.decode(), "ttttttttttt".decode(),content)
    #     r = '\\d{9,}'    #微信号QQ号
    #     content = re.sub(r.decode(), "QQQQQQQQQ".decode(),content)
    #     r = '\\d{8}'    #微信号QQ号
    #     content = re.sub(r.decode(), "tttttttt".decode(),content)
    #     r = '\\d{7}'    #FMFMFM
    #     content = re.sub(r.decode(), "fffffff".decode(),content)
    # content = content.lower()
    # r = '[\\d{}]'
    # content = re.sub(r.decode(), "x".decode(), content)
    return content


# 去除空格
def deleteBlank(content):
    #content = content.replace('\r', ' ').replace('\t', ' ').replace('\n', ' ').strip()
    content = content.replace('\n', ' ').strip()
    content = content.replace(" ", "").replace("", "").replace("", "").replace("", "")
    return content

#不用进行数据的预处理了  原始数据已经足够完善
if __name__ == '__main__':

    NormalContent = LoadData("./data_origin/OriginTrainData.txt")
    #NormalContent = LoadData("./data_origin/OriginTrainData_brief.txt")
    fwNormal = codecs.open("./data_origin/LabelData.txt", "w", encoding = "utf-8")
    #fwNormal = codecs.open("./data_origin/LabelData_brief.txt", "w", encoding="utf-8")
    for content in NormalContent:
        #         content = deleteDoc(content)
        content = deleteBlank(content)
        # content = changeNumber(content)
        #         content = deleteSymbol(content)
        #         fwNormal.write(jie(content) + "\n")
        content = " ".join(jieba.cut(content))
        fwNormal.write(content + "\n")
    #
    fwNormal.close()
    print "Main end!"