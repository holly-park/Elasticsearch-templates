# Elasticsearch-templates

<b>인덱스(index)</b>   --색인
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





