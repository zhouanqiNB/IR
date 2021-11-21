# 用于查询
from elasticsearch.client import Elasticsearch
import json
import os

es=Elasticsearch()

# body = {
#   "query": {
#     "bool": {
#       "must": [
#         { "match": { "Mail-Content": "Philip" } }
#       ],
#       "must_not": [
#         { "match": { "Mail-Content": "Andrew" } }
#       ]
#     }
#   },
#   "_source": ["Message-ID", "Mail-Content"]
# }


# res=es.search(index="enron-email", body=body)

# # 转化成json格式
# js=json.dumps(res, sort_keys=False, indent=4, separators=(',', ':'))
# print(js)

res = es.get(index="enron-email", id=1)
js=json.dumps(res, sort_keys=False, indent=4, separators=(',', ':'))
print(js)
