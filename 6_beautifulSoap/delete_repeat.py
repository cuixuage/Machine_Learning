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

resultDict = {}
def readStoryDict():
    for line in fo_filestory:
        line = line.rstrip()
        tokens = ujson.loads(line)
        title = tokens["title"]
        strTitle = title.encode('utf8', 'ignore')
        # resultDict[strTitle].append(line)
        resultDict[strTitle] = line

readStoryDict()
print len(resultDict)
# for key in resultDict:
#     if len(resultDict[key]) > 1:
#         print len(resultDict[key])," ",key
