```bash
curl -XPOST 'localhost:9200/club12/_search?pretty' -H 'Content-Type: application/json' -d '{"query": { "match_all": {} }}'
curl -XPOST 'localhost:9200/club12_detail/_search?pretty' -H 'Content-Type: application/json' -d '{"query": { "match_all": {} }}'
curl -XPOST 'localhost:9200/club12_menu/_search?pretty' -H 'Content-Type: application/json' -d '{"query": { "match_all": {} }}'
```



