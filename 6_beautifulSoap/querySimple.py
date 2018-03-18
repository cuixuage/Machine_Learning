#!/usr/bin/env python
# coding=utf-8
import os
import threading
import logging
import ujson
from collections import defaultdict

filequery = "/data08/cuixuange/cuixuange_storyfile/search.dat"
filestory = "/data08/cuixuange/cuixuange_storyfile/log_3_day.log"
fileoutput = "/data08/cuixuange/cuixuange_storyfile/outputsearch.dat"
# filequery = "/Users/cuixuange/falcon_plugin/mapreduce/head100_search.dat"
# filestory = "/Users/cuixuange/falcon_plugin/mapreduce/head20000_log.log"
# fileoutput = "/Users/cuixuange/falcon_plugin/mapreduce/outputsearch.dat"

logpath = fileoutput
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
ch = logging.FileHandler(logpath)
ch.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(ch)

fo_filestory = open(filestory, "r")

resultDict = defaultdict(list)
def readStoryDict():
    for line in fo_filestory:
        line = line.rstrip()
        tokens = ujson.loads(line)
        title = tokens["title"]
        strTitle = title.encode('utf8', 'ignore')
        # resultDict[strTitle].append(line)
        resultDict[strTitle] = line

# print len(resultDict)
# for key in resultDict:
#     if len(resultDict[key]) > 1:
#         print len(resultDict[key])," ",key

class myThread(threading.Thread):
    def __init__(self, threadID, filestart, fileend):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.filestart = filestart
        self.fileend = fileend
    def run(self):
        currentId = 0
        fin = open(filequery,"r")
        fin.seek(self.filestart,0)
        for line in fin.readlines(self.fileend - self.filestart):
            line = line.rstrip().strip()
            try:
                tokens = ujson.loads(line)
            except Exception, e:
                continue
            query = tokens["query"]
            strQuery = query.encode('utf8', 'ignore').strip()
            if resultDict[strQuery]:
                currentId += 1
                # logger.info("%d\t%d\t%s\t%s\t%s",self.threadID,currentId,strQuery,line,resultDict[strQuery])
                logger.info("%s\t%s", strQuery, line)


queryFileSize = os.path.getsize(filequery)
everySize = queryFileSize/100
readStoryDict()
threadList = []

try:
    for i in range(0, 100):
        thread = myThread(i, i * everySize, (i + 1) * everySize)
        threadList.append(thread)
        thread.start()
except Exception, e:
   print e

#
# ftest = open("./queryResult.simple","r")
# for line in ftest:
#     line = line.split("\t")
#     print len(line)
#     print line[4]
