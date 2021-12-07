import numpy as np
from scipy import sparse
from fast_pagerank import pagerank
from fast_pagerank import pagerank_power

def as_num(x):
    y = "{:.10f}".format(x)  # .10f 保留10位小数
    return y

f = open("pageRankValue.txt")
pageRank = f.read().split("\n")
pageRank=pageRank[:-1]
print(len(pageRank))
for i in range(0,len(pageRank)):
	pageRank[i]=float(as_num(float(pageRank[i])))
f.close()


# print(pageRank)


########### 现在成功把pageRankValue读入line而且是float类型的。 #######################




########### 现在来把这个列表和link连接起来，放在字典里。 #######################

link=[]

# 目录页----------------------------------------------------------------------------------------

category=1
pageNumList=[73,5,8,15,7,5]
link=[]
for category in range(1,7):
	for index in range(1,pageNumList[category-1]):
		url="http://12club.nankai.edu.cn/programs?category_id="+str(category)+"&order=update&page="+str(index)
		link.append(url)
		# print(url)

# 详情页获取----------------------------------------------------------------------------------------

f = open("detailUrls.txt")
line = f.readline()
# print(line)
f.close()

# 获取
line=line.split("http")
for i in range(0,len(line)):
    line[i]="http"+line[i]
line.remove(line[0])

for i in line:
	link.append(i)

dic={}
for i in range(0,len(link)):
	dic[link[i]]=pageRank[i]
	print(str(link[i])+":"+str(pageRank[i]))


# 好了现在已经把链接和pageRank做了映射了-------------------------------------------------------------------------------------------

with open("./pageRankDic.txt",'w',encoding='utf-8') as fp:
	for i in range(0,len(link)):
		fp.writelines(str(link[i]))
		fp.writelines("\n")
		fp.writelines(str(pageRank[i]))
		fp.writelines("\n")

