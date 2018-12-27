# coding=utf-8
import requests
import re
import fcntl
import threading
import ujson as json
from bs4 import BeautifulSoup
newsary=[]
ans = {}
import logging

logpath = "./log_3_day.log"
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
            res = requests.get('http://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=' + str(i))
            soup = BeautifulSoup(res.text, 'html.parser')
            for news in soup.select('.all-book-list li'):
                ans["title"] = news.select('a')[1].text
                ans["author"] = news.select('a')[2].text
                ans["stytle"] = news.select('a')[3].text
                ans["status"] = news.select('span')[0].text
                ans["word"] = news.select('p')[2].text
                ans["brief"] = getBrief(news.select('p')[1].contents[0])
                string = json.dumps(ans, ensure_ascii=False)
                # print string
                logger.info(string)


thread1 = myThread(1, 1, 5000)
thread2 = myThread(2, 5001, 10000)
thread3 = myThread(3, 10001, 15000)
thread4 = myThread(4, 15001, 20000)
thread5 = myThread(5, 20001, 25000)
thread6 = myThread(6, 25001, 30000)
thread7 = myThread(7, 30001, 35000)
thread8 = myThread(8, 35001, 40000)
thread9 = myThread(9, 40001, 42269)
try:
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
except:
   print "Error: unable to start thread"


