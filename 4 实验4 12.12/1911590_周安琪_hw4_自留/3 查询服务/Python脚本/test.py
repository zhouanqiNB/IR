# -*- coding: UTF-8 -*-


import sys  
import codecs
from elasticsearch.client import Elasticsearch
import json

def as_num(x):
    y = "{:.10f}".format(x)  # .10f 保留10位小数
    return y



es=Elasticsearch()


# 解决乱码问题###########################################################################################

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
# sys.stdout = codecs.getwriter('GBK')(sys.stdout.detach())

# 解决乱码问题###########################################################################################



# 接收前端的参数###########################################################################################

params = sys.argv[1] #即为获取到的PHP传入python的入口参数

# 接收前端的参数###########################################################################################
 



# ES查询###########################################################################################
print("这是关键字<font color='LightYellow'><b>"+params+"</b></font>的搜索结果：")
print("<br>")
print("<br>")

body = {
    "query": {
        "match": { "content": params } 
    },
}


res=es.search(index="club12_detail", body=body)
# js=json.dumps(res, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
# print(js)

# ES查询###########################################################################################




# 读字典###########################################################################################

# link->PageRankValue
dic={}

# 这是一个问题，因为我的xampp在wsl的根目录里，然后似乎yii的view文件夹下面是不可以放py的
# 所以我只好用绝对路径。
f = open("/mnt/c/Users/16834/Desktop/NKUSearch/pageRankDic.txt")
pageRankDic = f.read().split("\n")
pageRankDic=pageRankDic[:-1]


# print(len(pageRankDic))

for i in range(0,int(len(pageRankDic)/2)):
    dic[pageRankDic[i*2]]=float(as_num(float(pageRankDic[i*2+1])))
    # print(pageRankDic[i*2])
    # print(pageRankDic[i*2+1])



# print(dic)

# pageRank=pageRank[:-1]
# print(len(pageRank))
# for i in range(0,len(pageRank)):
#     pageRank[i]=float(as_num(float(pageRank[i])))
# f.close()



# 读字典###########################################################################################



# 处理数据###########################################################################################

a=res["hits"]

# b=a["hits"]
# js=json.dumps(b, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
# print(js)

a=a["hits"]



for i in range(0,len(a)):
    a[i]["_source"]["score"]=a[i]["_score"]
    a[i]=a[i]["_source"]
    del(a[i]["content"])
# print(a[0]["link"])

for i in range(0,len(a)):
    a[i]["pageRank"]=dic[a[i]["link"]]

for i in range(0,len(a)):
    a[i]["finalScore"]=a[i]["pageRank"]+a[i]["score"]

# js=json.dumps(a, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
# print(js)

# 加reverse因为是倒序
a = sorted(a, key=lambda k: k['finalScore'],reverse=True) 
# print("sorted.")


# js=json.dumps(a, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
# print(js)

# 处理数据###########################################################################################



# 前端输出###########################################################################################


# 按照ESscore+pageRank排序完了之后再输出。
print('<div class="row gutter"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12"><div class="panel panel-red">')
print('<div class="panel-body"><table class="table table-hover no-margin">')

print("<thead>")
print("<tr><th>标题</th>")
# print("<th>打分</th>")
print("<th>打分</th></tr>")
print("</thead>")

print("<tbody>")

for i in range(0,len(a)):
    print("<tr>")

    print("<td>")
    print("<a href= '"+a[i]["link"]+"'>")
    print("<u>"+a[i]["title"]+"</u>")
    print("</a>")
    print("</td>")

    print("<td>")
    print(a[i]["finalScore"])
    print("</td>")
    print("</tr>")

print("</tbody>")
print("</table>")
print("</div>")
print("</div>")
print("</div>")

# 前端输出###########################################################################################

# 日志记录############################################################################################
with open("/mnt/c/Users/16834/Desktop/NKUSearch/history.txt",'a',encoding='utf-8') as fp:
    fp.writelines('<div class="row gutter"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12"><div class="panel panel-red">')
    fp.writelines('<div class="panel-body"><table class="table table-hover no-margin">')

    fp.writelines("<thead>")
    fp.writelines("<tr><th>标题</th>")
    # print("<th>打分</th>")
    fp.writelines("<th>打分</th></tr>")
    fp.writelines("</thead>")

    fp.writelines("<tbody>")

    for i in range(0,len(a)):
        fp.writelines("<tr>")

        fp.writelines("<td>")
        fp.writelines("<a href= '"+a[i]["link"]+"'>")
        fp.writelines("<u>"+a[i]["title"]+"</u>")
        fp.writelines("</a>")
        fp.writelines("</td>")

        fp.writelines("<td>")
        fp.writelines(str(a[i]["finalScore"]))
        fp.writelines("</td>")
        fp.writelines("</tr>")

    fp.writelines("</tbody>")
    fp.writelines("</table>")
    fp.writelines("</div>")
    fp.writelines("</div>")
    fp.writelines("</div>")

# 日志记录############################################################################################
#########################################
# print("<font color='LightYellow'><u>This is some text!</u></font>")
# js=json.dumps(a, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
# print(js)