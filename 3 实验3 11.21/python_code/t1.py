# 导入索引
from elasticsearch.client import Elasticsearch
import json
import os

es=Elasticsearch()


idNum=1

# 获取本文件夹下所有叶文件的路径
filePath = 'maildir'


for maindir, subdir, file_name_list in os.walk(filePath):
    for filename in file_name_list:
        i = os.path.join(maindir, filename)

        print("processing "+i)
        file=open(i)
        doc={}

        # 前15行是邮件属性
        for w in range(100):
            # 读入一行并且按照冒号分隔
            line=file.readline()
            wordList=line.split(":",1)

            # 加入map
            # 如果这一行没有冒号，那么把内容加到上一行去
            if len(wordList)<2:
                print("This line has not ':', will add it to previous one.")
                if wordList[0]==" ":
                    value+=""
                else:
                    value+=", "
                    value+=wordList[0].strip()
                doc[key]=value # 更新上一条记录
                continue

            # 正常情况有冒号，分为前后两个部分
            key=wordList[0]
            if wordList[1]==" ":
                value=""
            else:
                value=wordList[1].strip()

            # 加入json结构
            doc[key]=value

            # 如果这一行左侧是"X-FileName"，那么说明下面就应该是"Mail-Content"
            # 循环的出口
            if wordList[0]=="X-FileName":
                break


        # 下面的都是邮件内容
        key="Mail-Content"
        value=file.read().strip()
        doc[key]=value


        # 关闭文件
        file.close()


        # 这里有一个问题就是找不着type无法从curl加链接直接获取
        res= es.index(index="enron-email", id=idNum, document=doc)
        res = es.get(index="enron-email", id=idNum)
        print(idNum)
        
        # 导入多少条停止
        if idNum==100:
            os. _exit(0)  

        idNum=idNum+1

        # 转化成json
        js=json.dumps(res, sort_keys=False, indent=4, separators=(',', ':'))
        # print(js)


