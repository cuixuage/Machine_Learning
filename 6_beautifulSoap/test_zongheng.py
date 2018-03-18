# coding=utf-8
import requests
import re
import time
import threading
import ujson as json
from bs4 import BeautifulSoup
newsary=[]
ans = {}
import logging

logpath = "./log_zongheng.log"
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
ch = logging.FileHandler(logpath)
ch.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(ch)

def getBrief(contains):
    str = json.dumps(contains, ensure_ascii=False)
    str = str + ""
    str = re.sub('\"', '', str)
    str = re.sub(",", '', str)
    str = re.sub("\s", '', str)
    str = str[3:]
    str = str[:-3]
    return str

class myThread(threading.Thread):
    def __init__(self, threadID,page1,page2):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.page1 = page1
        self.page2 = page2
    def run(self):
        for i in range(self.page1, self.page2):
            res = requests.get('http://book.zongheng.com/ranknow/male/r1/c0/q0/' + str(i)+'.html')
            # print res
            soup = BeautifulSoup(res.text, 'html.parser')
            for news in soup.select('.main_con li'):
                if  news.select('a') :
                    ans["stytle"] = news.select('a')[0].text
                    # print news.select('a')[0].text
                    ans["title"] = news.select('a')[1].text
                    # print ans["title"]
                    ans["newchapter"] = news.select('a')[2].text
                    print news.select('a')[2].text
                    ans["status"] = news.select('em')[0].text
                    # print news.select('em')[2].text
                    ans["author"] = news.select('span')[4].text
                    # print news.select('span')[4].text
                    ans["time"] = news.select('span')[5].text
                    # print news.select('span')[5].text
                string = json.dumps(ans, ensure_ascii=False)
                # print string
                logger.info(string)


thread1 = myThread(1, 1, 2)
try:
    thread1.start()
except:
   print "Error: unable to start thread"


