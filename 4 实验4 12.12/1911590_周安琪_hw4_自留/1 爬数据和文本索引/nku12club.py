"""
爬取12社区的页面数据--全部

新增标签处理

"""
from elasticsearch.client import Elasticsearch
from selectolax.parser import HTMLParser
import re
import requests
import json

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

idNum=1

allUrlList=[]


# 爬目录页-------------------------------------------------------------------------------------------------------
# 这是因为有72页。
for category in range(1,7):
	for index in range(1,pageNumList[category-1]):
		# 获取html页面-----------------------------------------------------------------------------
		url="http://12club.nankai.edu.cn/programs?category_id="+str(category)+"&order=update&page="+str(index)
		headers={
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
		}
		response=requests.get(url=url,headers=headers)
		page_text=response.text # 得到html的源码
		# 获取html页面-----------------------------------------------------------------------------



		# 动漫详情url------------------------------------------------------------------------------
		url_list=find_all(page_text)
		for i in url_list:
			allUrlList.append(i)
		# print(url_list)
		# 动漫详情url------------------------------------------------------------------------------


		# 存进文件里
		# fileName=str(index)+".html"


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
		newList=newList[9:-1]
		# print(newList)

		# 拿到按行分隔的字符列表--------------------------------------------------------------------

		# 按照动漫来分隔---------------------------------------------------------------------------


		# 这一部分是这样的，双指针，一个在总list一个在namelist，当在总list里面有匹配上namelist的时候认为是匹配上了
		# 一个新的动漫，nameListPtr++，当没匹配的时候就认为还是上一个动漫，加到原来的list里面。
		nameList=[]
		for i in range(0,len(newList)-1):
			if newList[i]=='最新更新:':
				nameList.append(newList[i-1])
		# print(len(allUrlList))
		# print(allUrlList)

		# print(nameList)
		oneAniList=[]

		# 指向nameList
		nameListPtr=0

		tmp=[]

		for i in newList:
			if i==nameList[nameListPtr]:
				oneAniList.append(tmp)
				tmp=[]
				tmp.append(i)
				if nameListPtr!=len(nameList)-1:
					nameListPtr=nameListPtr+1
			else:
				tmp.append(i)


		oneAniList.remove([])


		# 删掉标签项
		tmp=[]
		for oneAni in oneAniList:
			for j in range(0,len(oneAni)):
				if oneAni[j]=="标签:":
					for k in range(j+1,len(oneAni)):
						oneAni[j]=oneAni[j]+oneAni[k]+","
					oneAni=oneAni[0:j+1]
					tmp.append(oneAni)
					break
		
		oneAniList=tmp


		# 弄成键值对的样子
		for oneAni in oneAniList:
			oneAni[0]="标题:"+oneAni[0]
			oneAni[1]=oneAni[1]+oneAni[2]
			oneAni.remove(oneAni[2])


		# 按照动漫来分隔---------------------------------------------------------------------------


		# 创建键值对json输出-------------------------------------------------------------
		oneAniDicList=[]
		tmpPtr=0
		for i in oneAniList:
			dicTmp={}
			for j in i:
				a=j.split(":",1)
				dicTmp[a[0]]=a[1]
			dicTmp["链接"]=url_list[tmpPtr]

			es.index(index="club12", id=idNum, document=dicTmp)	# 建索引
			idNum=idNum+1

			tmpPtr=tmpPtr+1	
			oneAniDicList.append(dicTmp)
		js=json.dumps(oneAniDicList, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
		# print(oneAniDicList)
		# print(js)
		print("this page end."+str(index))
	print("this category end.")



		# 现在咱就是可以输出json形式的数据了！
		# 创建键值对json输出-------------------------------------------------------------



print("menuend.")
# 爬目录页-------------------------------------------------------------------------------------------------------


# 拿到详情页url列表-------------------------------------------------------------------------------------------------------
print(len(allUrlList))#2080

detailUrl=[]
for oneUrl in allUrlList:
	detailUrl.append(oneUrl[0:-2]+"#intro")


with open("./detailUrls.txt",'w',encoding='utf-8') as fp:
	fp.writelines(detailUrl)
# 拿到详情页url列表-------------------------------------------------------------------------------------------------------



print("end")
