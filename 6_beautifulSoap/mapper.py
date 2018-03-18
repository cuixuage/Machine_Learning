#!/usr/bin/env python
# coding=utf-8
import sys,ujson

queryTitle = ["辰东"]

def mapper():
    for line in sys.stdin:
        line = line[:-1]
        tokens = ujson.loads(line)
        author = tokens["author"]
        strAuthor = author.encode('utf8','ignore')
        if strAuthor in queryTitle:
            print ("{}\t{}".format(strAuthor,line))
        else:
            continue

def reducer():
    for line in sys.stdin:
        line = line.strip().split("\t")
        quertKey = line[0]
        value = line[1]
        print quertKey,"\t",value


if __name__ == '__main__':
    if sys.argv[1] == 'mapper':
        mapper()
    elif sys.argv[1] == 'reducer':
        reducer()


多线程切割文件去寻找