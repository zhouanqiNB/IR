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

title = sys.argv[1] #即为获取到的PHP传入python的入口参数
updateNum = sys.argv[2] #即为获取到的PHP传入python的入口参数
date = sys.argv[3] #即为获取到的PHP传入python的入口参数
fansub = sys.argv[4] #即为获取到的PHP传入python的入口参数
tag = sys.argv[5] #即为获取到的PHP传入python的入口参数

# 统计参数的数目
paramNum=5
if title=="empty":
    paramNum=paramNum-1
if updateNum=="empty":
    paramNum=paramNum-1
if date=="empty":
    paramNum=paramNum-1
if fansub=="empty":
    paramNum=paramNum-1
if tag=="empty":
    paramNum=paramNum-1

# print(paramNum)
# print("title:"+title)
# print("updateNum:"+updateNum)
# print("date:"+date)
# print("fansub:"+fansub)
# print("tag:"+tag)


# 接收前端的参数###########################################################################################
 



# # ES查询###########################################################################################
# print("<br>")
# print("<br>")
body = {
    "query": {
        "match_all": {} 
    },
}


paramList=[title,updateNum,date,fansub,tag]

strList=["标题","最新更新","更新日期","字幕组","标签"]


if paramNum==0:
    pass
elif paramNum==1:
    del(body["query"]["match_all"])
    for i in range(0,5):
        if paramList[i]!="empty":
            body["query"]["match"]={strList[i]:paramList[i]}
            break
else:
    del(body["query"]["match_all"])
    body["query"]["bool"]={}
    body["query"]["bool"]["must"]=[]
    for i in range(0,5):
        if paramList[i]!="empty":
            body["query"]["bool"]["must"].append({"match":{strList[i]:paramList[i]}})

# print(body)

# body = {
#     "query": {
#         "match": { "title": params } 
#     },
# }


res=es.search(index="club12", body=body)
# res=es.get(index="club12", id=1)
# js=json.dumps(res, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
# print(js)

# ES查询###########################################################################################




# 处理数据###########################################################################################

a=res["hits"]

a=a["hits"]
js=json.dumps(a, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
# print(js)




for i in range(0,len(a)):
    a[i]=a[i]["_source"]
    a[i]["链接"]=a[i]["链接"][:-2]# 一些莫名的bug
# js=json.dumps(a, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
# print(js)

# 处理数据###########################################################################################



# 前端输出###########################################################################################


# 按照ESscore+pageRank排序完了之后再输出。
print('<div class="row gutter"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12"><div class="panel panel-red">')
print('<div class="panel-body"><table class="table table-hover no-margin">')

print("<thead>")
print("<tr><th>标题</th>")
print("<th>最新更新</th>")
print("<th>更新日期</th>")
print("<th>字幕组</th>")
print("<th>下载量</th>")
print("<th>标签</th></tr>")
print("</thead>")

print("<tbody>")

for i in range(0,len(a)):
    print("<tr>")

    print("<td>")
    if "标题" in a[i].keys():
        print("<a href= '"+a[i]["链接"]+"'>")
        print("<u>"+a[i]["标题"]+"</u>")
        print("</a>")
    print("</td>")

    print("<td>")
    if "最新更新" in a[i].keys():
        print(a[i]["最新更新"])
    print("</td>")

    print("<td>")
    if "更新日期" in a[i].keys():
        print(a[i]["更新日期"])
    print("</td>")

    print("<td>")
    if "字幕组" in a[i].keys():
        print(a[i]["字幕组"])
    print("</td>")

    print("<td>")
    if "下载量" in a[i].keys():
        print(a[i]["下载量"])
    print("</td>")

    print("<td>")
    if "标签" in a[i].keys():
        print(a[i]["标签"])
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
    fp.writelines("<th>最新更新</th>")
    fp.writelines("<th>更新日期</th>")
    fp.writelines("<th>字幕组</th>")
    fp.writelines("<th>下载量</th>")
    fp.writelines("<th>标签</th></tr>")
    fp.writelines("</thead>")

    fp.writelines("<tbody>")

    for i in range(0,len(a)):
        fp.writelines("<tr>")

        fp.writelines("<td>")
        if "标题" in a[i].keys():
            fp.writelines("<a href= '"+a[i]["链接"]+"'>")
            fp.writelines("<u>"+a[i]["标题"]+"</u>")
            fp.writelines("</a>")
        fp.writelines("</td>")

        fp.writelines("<td>")
        if "最新更新" in a[i].keys():
            fp.writelines(a[i]["最新更新"])
        fp.writelines("</td>")

        fp.writelines("<td>")
        if "更新日期" in a[i].keys():
            fp.writelines(a[i]["更新日期"])
        fp.writelines("</td>")

        fp.writelines("<td>")
        if "字幕组" in a[i].keys():
            fp.writelines(a[i]["字幕组"])
        fp.writelines("</td>")

        fp.writelines("<td>")
        if "下载量" in a[i].keys():
            fp.writelines(a[i]["下载量"])
        fp.writelines("</td>")

        fp.writelines("<td>")
        if "标签" in a[i].keys():
            fp.writelines(a[i]["标签"])
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