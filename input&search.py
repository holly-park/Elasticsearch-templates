from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch('http://127.0.0.1:9200')
es.info()

#함수생성
def make_index(es, index_name):
index_name = 'goods'
if es.indices.exists(index=index_name):   #동일한 이름의 인덱스가 있을 경우(exists) 삭제하고(delete) 생성(create) 
     es.indices.delete(index=index_name)
     es.indices.create(index=index_name)
 
#데이터 준비
doc1 = {'goods_name': '삼성 노트북 9',    'price': 1000000}
doc2 = {'goods_name': '엘지 노트북 그램', 'price': 2000000}
doc3 = {'goods_name': '애플 맥북 프로',   'price': 3000000}
doc4 = {'goods_name': '맥북',   'price': 100000}
doc5 = {'goods_name': '맥복',   'price': 100000}


#함수 실행
make_index(es, index_name)


#값입력
es.index(index=index_name, doc_type='string', body=doc1)
es.index(index=index_name, doc_type='string', body=doc2)
es.index(index=index_name, doc_type='string', body=doc3)
es.index(index=index_name, doc_type='string', body=doc4)
es.index(index=index_name, doc_type='string', body=doc5)
es.index(index=index_name, doc_type='string', body=doc4)
es.index(index=index_name, doc_type='string', body=doc4)


#검색
results = es.search(index=index_name, body={'from':0, 'size':100, 'query':{'match':{'goods_name':'맥북'}}})
for result in results['hits']['hits']:
    print('score:', result['_score'], 'source:', result['_source'])
    
    
