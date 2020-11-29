from pprint import pprint
import requests
import urllib
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from elasticsearch.serializer import JSONSerializer
import os,sys

#ES 서버와 연결
res = requests.get('http://localhost:9200')   
print (res.content)

es = Elasticsearch([{'host': '', 'port': }])    #es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

#JSON 파일 경로 설정
directory = '/home/Documents/folder/myfile.json'



#try1
with open(directory, 'r', encoding='utf-8') as f:
    data=json.loads(f.read())
pprint(data)

es.index(index='my_index', doc_type='doc', body=data)




#try2
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        f = open(filename)
        docket_content = f.read()
        # Send the data into es
        es.index(index='myindex', ignore=400, doc_type='docket', 
        id=i, body=json.loads(docket_content))
        i = i + 1
