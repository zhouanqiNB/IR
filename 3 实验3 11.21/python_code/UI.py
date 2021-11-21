from elasticsearch.client import Elasticsearch
import json


es=Elasticsearch()


def PrintUserInterfaceMenu():
	print("-------------------------------")
	print("输入编号选择一个操作：")
	print("1. 增加文档")
	print("2. 删除文档")
	print("3. 修改文档")
	print("4. 查询文档")
	print("6. 退出程序")

def UserInterface():
	while(True):
		PrintUserInterfaceMenu()
		s=input()
		if s=='1':
			AddFile()
		elif s=='2':
			DeleteFile()
		elif s=='3':
			UpdateFile()
		elif s=='4':
			SearchFile()
		elif s=='6':
			break

def PrintAddFileMenu():
	print("-------------------------------")
	print("输入编号选择一个操作：")
	print("1. 继续添加")
	print("6. 返回上一级菜单")

def AddFile():
	while(True):
		PrintAddFileMenu()
		s=input()
		if s=='1':
			AddAFile()
		elif s=='6':
			break

def AddAFile():
	print("为你的文档指定一个id吧，如果已经存在了我们会把它覆盖掉。")
	userid=int(input())
	print("下面开始创建该文档的键值对吧，输入end返回上级菜单。")

	doc={}

	i=1

	while(True):
		print("key"+str(i))
		key=input()
		if key=="end":
			break
		
		print("value"+str(i))
		value=input()
		if value=="end":
			break
		
		doc[key]=value
		
		i=i+1
	print(doc)
	res=es.index(index="enron-email",id=userid, document=doc)
	res = es.get(index="enron-email", id=userid)
	js=json.dumps(res, sort_keys=False, indent=4, separators=(',', ':'))
	print(js)

	print("成功创建文档"+str(userid))



def PrintDeleteFileMenu():
	print("-------------------------------")
	print("输入编号选择一个操作：")
	print("1. 指定id删除")
	print("2. 指定条件删除")
	print("6. 返回上一级菜单")

def DeleteFile():
	while(True):
		PrintDeleteFileMenu()
		s=input()
		if s=='1':
			IdDelFile()
		elif s=='2':
			CondDelFile()
		elif s=='6':
			break

def IdDelFile():
	while(True):
		print("输入你想删除的id，按6返回上一级菜单")
		userid=input()
		if userid=='6':
			break
		es.delete(index='enron-email', id=userid)
		print("id为"+str(userid)+"的文件已经被删除")

def CondDelFile():
	print("还没有实现QAQ")



def PrintUpdateFileMenu():
	print("-------------------------------")
	print("输入编号选择一个操作：")
	print("1. 继续更改")
	print("6. 返回上一级菜单")

def UpdateFile():
	while(True):
		PrintUpdateFileMenu()
		s=input()
		if s=='1':
			UpdateAFile()
		elif s=='6':
			break

def UpdateAFile():
	print("指定你想要更改的文档id。")
	userid=input()
	print("下面开始输入该文档需要更新的键值对吧，输入end返回上级菜单。")

	doc={}

	i=1

	while(True):
		print("key"+str(i))
		key=input()
		if key=="end":
			break
		
		print("value"+str(i))
		value=input()
		if value=="end":
			break
		
		doc[key]=value
		
		i=i+1
	body={
	"doc":doc
	}
	print(body)

	es.update(index="enron-email",id=userid,body=body)
	res = es.get(index="enron-email", id=userid)
	js=json.dumps(res, sort_keys=False, indent=4, separators=(',', ':'))
	print(js)
	print("成功更改文档"+str(userid))



def PrintSearchFileMenu():
	print("-------------------------------")
	print("输入编号选择一个操作：")
	print("1. 指定id查询")
	print("2. 简单match")
	print("3. 布尔查询")
	print("6. 返回上一级菜单")

def SearchFile():
	while(True):
		PrintSearchFileMenu()
		s=input()
		if s=='1':
			IdSearchAFile()
		if s=='2':
			SimpleMatchUpdateAFile()
		if s=='3':
			BoolMatchUpdateAFile()
		elif s=='6':
			break

def IdSearchAFile():
	while(True):
		print("指定你想要查看的文档id，输入end返回上级菜单。")
		userid=input()

		if userid=="end":
			break

		res = es.get(index="enron-email", id=userid)
		
		js=json.dumps(res, sort_keys=False, indent=4, separators=(',', ':'))
		print(js)
		print("输出文档"+str(userid))

def SimpleMatchUpdateAFile():
	while(True):
		print("指定你的match条件。")
		print("key:")
		key=input()
		if key=='end':
			break
		print("value:")
		value=input()
		if value=='end':
			break
		doc={key:value}
		body={
		  "query": { 
		      "match": doc
		  }
		}

		res=es.search(index="enron-email", body=body)
		js=json.dumps(res, sort_keys=False, indent=4, separators=(',', ':'))
		print(js)
		print("输出文档符合键值对：")
		print(doc)

def PrintBoolMatchUpdateAFileMenu():
	print("-------------------------------")
	print("输入编号选择运算方式：")
	print("1. must")
	print("2. should")
	print("3. must_not")
	print("6. 返回上一级菜单")

def BoolMatchUpdateAFile():
	print("还没有实现QAQ")

	# body={
	#   "query": {
	#     "bool": {
	#       "must": [],
	#       "should":[],
	#       "must_not": []
	#     }
	#   }
	# }
	# doc1={"match":{}}
	# doc2={"match":{}}
	# doc3={"match":{}}
	# while(True):
	# 	PrintBoolMatchUpdateAFileMenu()
	# 	s=input()
	# 	if s=='1':
	# 		must(doc1)
	# 		body["query"]["bool"]["must"].append(doc1)
	# 	if s=='2':
	# 		should(doc2)
	# 	if s=='3':
	# 		must_not(doc3)
	# 	elif s=='6':
	# 		break




	# res = es.get(index="enron-email", id=userid)
	# js=json.dumps(res, sort_keys=False, indent=4, separators=(',', ':'))
	# print(js)




print("这里存储着安然数据集部分数据，你可以对它们进行增删改查等操作，但是我们并不支持过于复杂的操作哦！")

UserInterface()