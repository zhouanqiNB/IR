"""
爬取12社区的页面数据--详情页

页面链接来自nku12club.py

"""
from elasticsearch.client import Elasticsearch
from selectolax.parser import HTMLParser
import re
import requests
import json
import time

es=Elasticsearch()

# 获取列表--------------------------------------------
f = open("detailUrls.txt")
line = f.readline()
# print(line)
f.close()

line=line.split("http")
for i in range(0,len(line)):
    line[i]="http"+line[i]
    # print(line[i])
line.remove(line[0])
# print(line[0])

# 获取列表--------------------------------------------



idNum=0


# 按照列表顺序一个一个爬
for index in range(0,len(line)):
    url=line[index]
    print(url)
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    response=requests.get(url=url,headers=headers)
    page_text=response.text # 得到html的源码


    # 处理数据---------------------------------------
    text = HTMLParser(page_text).text() # 提取文字
    text=text.replace("\n","`")
    text=text.replace(" ","")
    text=text.replace("：",":")
    text=text.split("`")    # 按行分隔

    newList=[]
    for i in text:
        # if i==endTagList[category-1]:   # 把不需要的信息删掉
        #     break
        if i!='':   # 把多余的行删掉
            newList.append(i)
    newList=newList[9:-19]

    for i in range(0,4):
        newList.remove(newList[1])



    # 存进elasticsearch-------------------------------
    dic={}

    dic["title"]=newList[0]
    dic["link"]=url
    content=""
    for i in newList:
        content=content+i+","
    dic["content"]=content

    es.index(index="club12_detail", id=index+1, document=dic) # 建索引

    js=json.dumps(dic, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
    print(js)

    # print(newList)

    time.sleep(15)
