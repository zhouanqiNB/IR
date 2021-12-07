import numpy as np
from scipy import sparse
from fast_pagerank import pagerank
from fast_pagerank import pagerank_power

# 我简单粗暴地人工算了矩阵大小……
# 目录页一共有 72+4+7+14+6+4=107页，详情页有2080页，加起来就是2187
# 因为目录页是循环就可以得出的，详情页链接我已经保存在本地了，所以就不再去爬了。
# 毕竟站长不希望被爬。


f = open("detailUrls.txt")
line = f.readline()
# print(line)
f.close()


# ----------------------------------
pageRankVector=[]

# ----------------------------------

# 获取
line=line.split("http")
for i in range(0,len(line)):
    line[i]="http"+line[i]
    # print(line[i])
line.remove(line[0])
# for i in line:
# 	print(i)

# 0-106号是目录页
# 107-2186号是详情页

category=1
pageNumList=[73,5,8,15,7,5]
menuUrlList=[]
for category in range(1,7):
	for index in range(1,pageNumList[category-1]):
		url="http://12club.nankai.edu.cn/programs?category_id="+str(category)+"&order=update&page="+str(index)
		menuUrlList.append(url)
# 为menuUrlList构建字典：
menuDic={}

for i in range(0,len(menuUrlList)):
	menuDic[i]=menuUrlList[i]



# for i in menuUrlList:
# 	print(i)

lastPageNumber=[16,17,7,14,3,3]# 这是我自己去看的，因为再爬不好。


# 首先构建目录与目录之间的==============================

# root->类型->目录->详情

tmpNum=0

animateMenu=[]
comicMenu=[]
musicMenu=[]
gameMenu=[]
novelMenu=[]
videoMenu=[]

for i in range(0,pageNumList[0]-1):
	animateMenu.append(tmpNum)
	tmpNum=tmpNum+1
for i in range(0,pageNumList[1]-1):
	comicMenu.append(tmpNum)
	tmpNum=tmpNum+1	
for i in range(0,pageNumList[2]-1):
	musicMenu.append(tmpNum)
	tmpNum=tmpNum+1	
for i in range(0,pageNumList[3]-1):
	gameMenu.append(tmpNum)
	tmpNum=tmpNum+1	
for i in range(0,pageNumList[4]-1):
	novelMenu.append(tmpNum)
	tmpNum=tmpNum+1	
for i in range(0,pageNumList[5]-1):
	videoMenu.append(tmpNum)
	tmpNum=tmpNum+1	


for i in range(0,6):
	lastPageNumber[i]=lastPageNumber[i]+(pageNumList[i]-2)*20
# print(lastPageNumber)


animateDetail=[]
comicDetail=[]
musicDetail=[]
gameDetail=[]
novelDetail=[]
videoDetail=[]

tmpNum=107

for i in range(0,lastPageNumber[0]):
	animateDetail.append(tmpNum)
	tmpNum=tmpNum+1
for i in range(0,lastPageNumber[1]):
	comicDetail.append(tmpNum)
	tmpNum=tmpNum+1	
for i in range(0,lastPageNumber[2]):
	musicDetail.append(tmpNum)
	tmpNum=tmpNum+1	
for i in range(0,lastPageNumber[3]):
	gameDetail.append(tmpNum)
	tmpNum=tmpNum+1	
for i in range(0,lastPageNumber[4]):
	novelDetail.append(tmpNum)
	tmpNum=tmpNum+1	
for i in range(0,lastPageNumber[5]):
	videoDetail.append(tmpNum)
	tmpNum=tmpNum+1	

# print(animateMenu)
	# print(comicMenu)
	# print(musicMenu)
	# print(gameMenu)
	# print(novelMenu)
	# print(videoMenu)
	# print(animateDetail)
	# print(comicDetail)
	# print(musicDetail)
	# print(gameDetail)
	# print(novelDetail)
	# print(videoDetail)

# 六种类型，每个类型有n页目录

# 同类型下的目录页互相引用-----------------------

# [0,0]
	# [0,1]
	# ...
	# [0,71]
	# [1,0]
	# [1,1]
	# ...
	# [1,71]
# print(len(pageRankVector))

for i in animateMenu:
	for j in animateMenu:
		pageRankVector.append([i,j])
# print(len(pageRankVector))

for i in comicMenu:
	for j in comicMenu:
		pageRankVector.append([i,j])
# print(len(pageRankVector))

for i in musicMenu:
	for j in musicMenu:
		pageRankVector.append([i,j])
# print(len(pageRankVector))

for i in gameMenu:
	for j in gameMenu:
		pageRankVector.append([i,j])
# print(len(pageRankVector))

for i in novelMenu:
	for j in novelMenu:
		pageRankVector.append([i,j])
# print(len(pageRankVector))

for i in videoMenu:
	for j in videoMenu:
		pageRankVector.append([i,j])

# print(pageRankVector)
# print(len(pageRankVector))


# A可以跳转到不同标签页的第一页-------------------
# A->videoMenu[0]
# A->gameMenu[0]
# A->novelMenu[0]

for i in animateMenu:
	pageRankVector.append([i,comicMenu[0]])
	pageRankVector.append([i,musicMenu[0]])
	pageRankVector.append([i,gameMenu[0]])
	pageRankVector.append([i,novelMenu[0]])
	pageRankVector.append([i,videoMenu[0]])
for i in comicMenu:
	pageRankVector.append([i,animateMenu[0]])
	pageRankVector.append([i,musicMenu[0]])
	pageRankVector.append([i,gameMenu[0]])
	pageRankVector.append([i,novelMenu[0]])
	pageRankVector.append([i,videoMenu[0]])
for i in musicMenu:
	pageRankVector.append([i,comicMenu[0]])
	pageRankVector.append([i,animateMenu[0]])
	pageRankVector.append([i,gameMenu[0]])
	pageRankVector.append([i,novelMenu[0]])
	pageRankVector.append([i,videoMenu[0]])
for i in gameMenu:
	pageRankVector.append([i,comicMenu[0]])
	pageRankVector.append([i,musicMenu[0]])
	pageRankVector.append([i,animateMenu[0]])
	pageRankVector.append([i,novelMenu[0]])
	pageRankVector.append([i,videoMenu[0]])
for i in novelMenu:
	pageRankVector.append([i,comicMenu[0]])
	pageRankVector.append([i,musicMenu[0]])
	pageRankVector.append([i,gameMenu[0]])
	pageRankVector.append([i,animateMenu[0]])
	pageRankVector.append([i,videoMenu[0]])
for i in videoMenu:
	pageRankVector.append([i,comicMenu[0]])
	pageRankVector.append([i,musicMenu[0]])
	pageRankVector.append([i,gameMenu[0]])
	pageRankVector.append([i,novelMenu[0]])
	pageRankVector.append([i,animateMenu[0]])
# print(len(pageRankVector))

# print(pageRankVector)

# 然后构建目录与详情之间的==============================

# 详情可以跳到任意所有类型的首页------------------

for i in animateDetail:
	pageRankVector.append([i,comicMenu[0]])
	pageRankVector.append([i,musicMenu[0]])
	pageRankVector.append([i,gameMenu[0]])
	pageRankVector.append([i,novelMenu[0]])
	pageRankVector.append([i,videoMenu[0]])
for i in comicDetail:
	pageRankVector.append([i,animateMenu[0]])
	pageRankVector.append([i,musicMenu[0]])
	pageRankVector.append([i,gameMenu[0]])
	pageRankVector.append([i,novelMenu[0]])
	pageRankVector.append([i,videoMenu[0]])
for i in musicDetail:
	pageRankVector.append([i,comicMenu[0]])
	pageRankVector.append([i,animateMenu[0]])
	pageRankVector.append([i,gameMenu[0]])
	pageRankVector.append([i,novelMenu[0]])
	pageRankVector.append([i,videoMenu[0]])
for i in gameDetail:
	pageRankVector.append([i,comicMenu[0]])
	pageRankVector.append([i,musicMenu[0]])
	pageRankVector.append([i,animateMenu[0]])
	pageRankVector.append([i,novelMenu[0]])
	pageRankVector.append([i,videoMenu[0]])
for i in novelDetail:
	pageRankVector.append([i,comicMenu[0]])
	pageRankVector.append([i,musicMenu[0]])
	pageRankVector.append([i,gameMenu[0]])
	pageRankVector.append([i,animateMenu[0]])
	pageRankVector.append([i,videoMenu[0]])
for i in videoDetail:
	pageRankVector.append([i,comicMenu[0]])
	pageRankVector.append([i,musicMenu[0]])
	pageRankVector.append([i,gameMenu[0]])
	pageRankVector.append([i,novelMenu[0]])
	pageRankVector.append([i,animateMenu[0]])
# print(len(pageRankVector))

# 目录可以跳到它所包含的详情页--------------------

# pageNumList=[73,5,8,15,7,5]

detailPtr=0
for i in animateMenu:
	#[0,detail[0]]....[0,detail[19]]
	#[1,detail[20]]....[1,detail[39]]
	if detailPtr==71:
		for j in range(20*detailPtr,20*detailPtr+16):
			pageRankVector.append([i,animateDetail[j]])
			# print(str(i)+","+str(animateDetail[j]))
	else:
		for j in range(20*detailPtr,20*detailPtr+20):
			pageRankVector.append([i,animateDetail[j]])
			# print(str(i)+","+str(animateDetail[j]))
	detailPtr=detailPtr+1

detailPtr=0
for i in comicMenu:
	#[0,detail[0]]....[0,detail[19]]
	#[1,detail[20]]....[1,detail[39]]
	if detailPtr==3:
		for j in range(20*detailPtr,20*detailPtr+17):
			pageRankVector.append([i,comicDetail[j]])
			# print(str(i)+","+str(comicDetail[j]))
	else:
		for j in range(20*detailPtr,20*detailPtr+20):
			pageRankVector.append([i,comicDetail[j]])
			# print(str(i)+","+str(comicDetail[j]))
	detailPtr=detailPtr+1
detailPtr=0
for i in musicMenu:
	#[0,detail[0]]....[0,detail[19]]
	#[1,detail[20]]....[1,detail[39]]
	if detailPtr==6:
		for j in range(20*detailPtr,20*detailPtr+7):
			pageRankVector.append([i,musicDetail[j]])
			# print(str(i)+","+str(musicDetail[j]))
	else:
		for j in range(20*detailPtr,20*detailPtr+20):
			pageRankVector.append([i,musicDetail[j]])
			# print(str(i)+","+str(musicDetail[j]))
	detailPtr=detailPtr+1
detailPtr=0
for i in gameMenu:
	#[0,detail[0]]....[0,detail[19]]
	#[1,detail[20]]....[1,detail[39]]
	if detailPtr==13:
		for j in range(20*detailPtr,20*detailPtr+14):
			pageRankVector.append([i,gameDetail[j]])
			# print(str(i)+","+str(gameDetail[j]))
	else:
		for j in range(20*detailPtr,20*detailPtr+20):
			pageRankVector.append([i,gameDetail[j]])
			# print(str(i)+","+str(gameDetail[j]))
	detailPtr=detailPtr+1
detailPtr=0
for i in novelMenu:
	#[0,detail[0]]....[0,detail[19]]
	#[1,detail[20]]....[1,detail[39]]
	if detailPtr==5:
		for j in range(20*detailPtr,20*detailPtr+3):
			pageRankVector.append([i,novelDetail[j]])
			# print(str(i)+","+str(novelDetail[j]))
	else:
		for j in range(20*detailPtr,20*detailPtr+20):
			pageRankVector.append([i,novelDetail[j]])
			# print(str(i)+","+str(novelDetail[j]))
	detailPtr=detailPtr+1
detailPtr=0
for i in videoMenu:
	#[0,detail[0]]....[0,detail[19]]
	#[1,detail[20]]....[1,detail[39]]
	if detailPtr==3:
		for j in range(20*detailPtr,20*detailPtr+3):
			pageRankVector.append([i,videoDetail[j]])
			# print(str(i)+","+str(videoDetail[j]))
	else:
		for j in range(20*detailPtr,20*detailPtr+20):
			pageRankVector.append([i,videoDetail[j]])
			# print(str(i)+","+str(videoDetail[j]))
	detailPtr=detailPtr+1

# print(len(pageRankVector))


# 这是向量
A = np.array(pageRankVector)
weights=[]
for i in range(0,len(pageRankVector)):
	weights.append(1)

# shape是说是m*n的矩阵
print(len(pageRankVector))
G = sparse.csr_matrix((weights, (A[:,0], A[:,1])), shape=(2187, 2187))
pr=pagerank(G, p=0.85)
# for i in range(108,200):
# 	print(i+1)
	# print(pr[i])

print(len(pr))
with open("./pageRankValue.txt",'w',encoding='utf-8') as fp:
	for i in pr:
		fp.writelines(str(i))
		fp.writelines("\n")
# print(pr)


# array([0.37252685, 0.19582391, 0.39414924, 0.0375    ])