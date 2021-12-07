"""
爬取12社区的页面数据--目录

新增标签处理

"""
from elasticsearch.client import Elasticsearch
from selectolax.parser import HTMLParser
import re
import requests
import json
import time

def find_all(html="hello"):
    '''
    抽取html中的链接
    '''
    compile_rule=re.compile(r"<a.*?href=https://|http://.*? ")
    url_list=re.findall(compile_rule, html)
    return url_list;

es=Elasticsearch()

category=1

# 在处理文字信息的时候会用到
endTagList=["72页","4页","7页","14页","6页","4页"]

pageNumList=[73,5,8,15,7,5]

idNum=0

allUrlList=[]

tag=["","动画","漫画","音乐","游戏","轻小说","视频"]

# 爬目录页-------------------------------------------------------------------------------------------------------
# 这是因为有72页。
for category in range(1,7):
# for category in range(1,2):
	for index in range(1,pageNumList[category-1]):
	# for index in range(1,2):
		# 获取html页面-----------------------------------------------------------------------------
		url="http://12club.nankai.edu.cn/programs?category_id="+str(category)+"&order=update&page="+str(index)
		headers={
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
		}
		response=requests.get(url=url,headers=headers)
		page_text=response.text # 得到html的源码
		# 获取html页面-----------------------------------------------------------------------------

		# 数据处理

		# 拿到按行分隔的字符列表--------------------------------------------------------------------
		text = HTMLParser(page_text).text()	# 提取文字
		text=text.replace("\n","`")
		text=text.replace(" ","")
		text=text.replace("：",":")
		text=text.split("`")	# 按行分隔


		newList=[]
		for i in text:
			if i==endTagList[category-1]:	# 把不需要的信息删掉
				break
			if i!='':	# 把多余的行删掉
				newList.append(i)
		newList=newList[9:-67]
		text=""
		for i in newList:
			text=text+i
		print(text)

		# 拿到按行分隔的字符列表--------------------------------------------------------------------

		# 按照动漫来分隔---------------------------------------------------------------------------

		dic={}
		dic["title"]="12社区"+tag[category]+"目录第"+str(index)+"页"
		dic["url"]=url
		dic["content"]=text
		print(dic)

		es.index(index="club12_menu", id=idNum, document=dic) # 建索引
		idNum=idNum+1

		time.sleep(1)

		# 现在咱就是可以输出json形式的数据了！
		# 创建键值对json输出-------------------------------------------------------------



print("menuend.")
# 爬目录页-------------------------------------------------------------------------------------------------------


# 拿到详情页url列表-------------------------------------------------------------------------------------------------------
# print(len(allUrlList))#2080

# detailUrl=[]
# for oneUrl in allUrlList:
# 	detailUrl.append(oneUrl[0:-2]+"#intro")


# with open("./detailUrls.txt",'w',encoding='utf-8') as fp:
# 	fp.writelines(detailUrl)
# 拿到详情页url列表-------------------------------------------------------------------------------------------------------



# print("end")
