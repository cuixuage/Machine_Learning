# coding=utf-8
import requests
import ujson as json
import re
from bs4 import BeautifulSoup
newsary=[]
ans = {}
fo = open("./story.file", "w")

def getBrief(contains):
    str = json.dumps(contains, ensure_ascii=False)
    str = str + ""
    str = re.sub('\"', '', str)
    str = re.sub(",", '', str)
    str = re.sub("\s", '', str)
    str = str[3:]
    str = str[:-3]
    return str

for i in range(1):
    res=requests.get('http://r.qidian.com/yuepiao?chn=-1&page='+str(i))
    soup=BeautifulSoup(res.text,'html.parser')
    for news in soup.select('.rank-view-list li'):
        ans["title"] = news.select('a')[1].text
        ans["author"] = news.select('a')[2].text
        ans["stytle"] = news.select('a')[3].text
        ans["update"] = news.select('p')[2].text
        # ans["url"] = news.select('a')[0]['href']
        ans["brief"] = getBrief(news.select('p')[1].contents[0])
        storyString = json.dumps(ans, ensure_ascii=False)
        newsary.append(storyString)

for val in newsary:
    # print val
    fo.write(val)
    fo.write("\n")
fo.close()

import pandas
newsdf = pandas.DataFrame(newsary)
# print newsdf


