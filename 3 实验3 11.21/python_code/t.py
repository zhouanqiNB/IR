# origin test.py
from datetime import datetime
from elasticsearch.client import Elasticsearch
es=Elasticsearch()
doc={
	'author':'Information Retrieval',
	'text':'Text for Elasticsearch',
	'timestamp':datetime.now(),
}

res= es.index(index="test-index", id=1, document=doc)
print(res['result'])
res = es.get(index="test-index", id=1)
print(res['_source'])
es.indices.refresh(index="test-index")
res = es.search(index="test-index", query={"match_all": {}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
	print("%(timestamp)s %(author)s: %(text)s"%hit["_source"])
print("Test OK")