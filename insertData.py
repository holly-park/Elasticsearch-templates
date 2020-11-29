from elasticsearch import Elasticsearch

es = Elasticsearch('[엘라스틱_서버_IP_주소]:9200')


# mapping 없이 자동 인덱스 생성

def insertDataDirect():
    es = Elasticsearch('[엘라스틱_서버_IP_주소]:9200')
    
    index="product_list"
    
    doc = {
        "category" : "skirt",
        "c_key" : "1234",
        "price" : 11,400,
        "status" : 1,
        "@timestamp" : datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    }
    
    es.index(index="product_list", doc_type="_doc", body=doc)
    
# mapping이 정의된 상태에서 데이터 삽입

  def insertData():
    es = Elasticsearch('[엘라스틱_서버_IP_주소]:9200')
    
    index="product_list"
    
    with open('mapping.json', 'r') as f:      #파일열기
        mapping = json.load(f)
        
    es.indices.create(index=index, body=mapping)    #맵핑하기

    doc = {
        "category" : "skirt",
        "c_key" : "1234",
        "price" : 11,400,
        "status" : 1,
        "@timestamp" : datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    }
    
    es.index(index="product_list", doc_type="_doc", body=doc)
