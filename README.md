# Elasticsearch-templates

<b>인덱스(index) =색인</b>  
RDBMS의 데이터베이스와 유사한 개념.
비슷한 특성을 가진 문서(document)의 모음.
*타입(유형)이 있다

<b>유형(type)</b>
RDBMS의 테이블과 유사한 개념.
인덱스의 파티션.
하나의 인덱스에 도큐먼트를 넣을 때 타입을 분리해서 인덱싱(indexing)이 가능하다.

<b>샤드(shard)</b>
인덱스의 데이터를 나누는 단위.
많은 양의 데이터를 넣게 되면 문제가 발생할 수 있기 때문에 RDBMS처럼 column별로 나누지 않고, row로 나눠서 샤드에 저장한다.(샤딩)

<b>문서(document)</b>
색인할 수 있는 기본 정보단위

<b>세그먼트(segment)</b>
도큐먼트가 인덱싱 될 때 데이터는 시스템 버퍼 캐시 영역으로 적재가 되고, 
이 후 디스크의 세그먼트에 기록된다

<b>맵핑(mapping)</b>
RDBMS의 스키마(schema)와 비슷한 개념. index에 들어가는 데이터 타입을 정의한다.
Mapping이 정해지지 않은 index에 무작정 문서를 넣어도 Elasticsearch는 자동으로 문서의 내용을 보고, 최선의 Data type을 지정해준다.


