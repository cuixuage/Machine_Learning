# coding:utf-8
import time
import codecs
import sys
import string
import numpy as np

def writeFinalRes(filename):
    fr = codecs.open('./data/' + filename, 'a+',encoding = "utf-8")
    fout = codecs.open('./data/' + 'user_click_data_brief.txt', 'a+', encoding="utf-8")
    arrayOfLines = fr.readlines()
    count =0
    for line in arrayOfLines:
        if count < 5000:
            line = line.strip()  #移除字符串头尾指定的字符 默认为空格
            count +=1
            fout.write(line + '\n')
    fr.close()
    fout.close()

if __name__ == "__main__":
    writeFinalRes("user_click_data.txt");
    print "Main ok"