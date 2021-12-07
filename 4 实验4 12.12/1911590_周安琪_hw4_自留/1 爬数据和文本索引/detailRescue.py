# 无语！我昨天晚上爬到一半出现网络问题了！得重新看看！这是最后一
# 个爬到的链接：
# http://12club.nankai.edu.cn/programs/1228#intro

# 哈哈无语了我的detailUrls.txt也清空了，真是见鬼

from elasticsearch.client import Elasticsearch
from selectolax.parser import HTMLParser
import re
import requests
import json
import time

##########################################
# 恢复detailUrls.txt
##########################################

"""
爬取12社区的页面数据--全部

新增标签处理

"""

# def find_all(html="hello"):
#     '''
#     抽取html中的链接
#     '''
#     compile_rule=re.compile(r"<a.*?href=https://|http://.*? ")
#     url_list=re.findall(compile_rule, html)
#     return url_list;

# es=Elasticsearch()

# category=1

# # 在处理文字信息的时候会用到
# endTagList=["72页","4页","7页","14页","6页","4页"]

# pageNumList=[73,5,8,15,7,5]

# idNum=1

# allUrlList=[]


# # 爬目录页，目标是获取detailUrls.txt-------------------------------------------------------------------------------------------------------
# # 这是因为有72页。
# for category in range(1,7):
# 	for index in range(1,pageNumList[category-1]):
# 		# 获取html页面-----------------------------------------------------------------------------
# 		url="http://12club.nankai.edu.cn/programs?category_id="+str(category)+"&order=update&page="+str(index)
# 		headers={
# 			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
# 		}
# 		response=requests.get(url=url,headers=headers)
# 		page_text=response.text # 得到html的源码
# 		# 获取html页面-----------------------------------------------------------------------------



# 		# 动漫详情url------------------------------------------------------------------------------
# 		url_list=find_all(page_text)
# 		for i in url_list:
# 			allUrlList.append(i)
# 		# print(url_list)

# 		print("page "+str(index)+" end.")
# 		time.sleep(10)

# 		# 动漫详情url------------------------------------------------------------------------------
# 	print("category "+str(category)+" end.")

# print("menuend.")
# # 爬目录页-------------------------------------------------------------------------------------------------------


# # 拿到详情页url列表-------------------------------------------------------------------------------------------------------
# print(len(allUrlList))#2080

# detailUrl=[]
# for oneUrl in allUrlList:
# 	detailUrl.append(oneUrl[0:-2]+"#intro")


# with open("./detailUrls.txt",'w',encoding='utf-8') as fp:
# 	fp.writelines(detailUrl)
# # 拿到详情页url列表-------------------------------------------------------------------------------------------------------



# print("end")


es=Elasticsearch()


f = open("detailUrls.txt")
line = f.readline()
# print(line)
print("end")
f.close()

line=line.split("http")
for i in range(0,len(line)):
    line[i]="http"+line[i]
    # print(line[i])
line.remove(line[0])


beginIndex=0
for i in range(0,len(line)):
	if line[i] == "http://12club.nankai.edu.cn/programs/1228#intro":
		beginIndex=i
		# print(line[i])
for index in range(beginIndex,len(line)):
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

