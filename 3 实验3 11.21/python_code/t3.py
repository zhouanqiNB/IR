# 用于更新、删除
from elasticsearch.client import Elasticsearch
import json
es=Elasticsearch()
# es.indices.delete(index='enron-email', id=1,ignore=[400, 404])

es.update(index="enron-email",id=2,body={"doc":{"a2":1}})
res = es.get(index="enron-email", id=2)
js=json.dumps(res, sort_keys=False, indent=4, separators=(',', ':'))
print(js)

es.update(index="enron-email",id=2,body={"script" : "ctx._source.a2 += 5"})
res = es.get(index="enron-email", id=2)
js=json.dumps(res, sort_keys=False, indent=4, separators=(',', ':'))
print(js)