# pymongo 라이브러리 import
from pymongo import MongoClient

# 접속할 클라이언트 주소 설정
client = MongoClient('localhost', 27017)
# 해당 클라이언트의 dbsparta 라는 DB에 접근 (DB가 존재하지 않을 시 자동 생성)
db = client.dbsparta

# 데이터 삽입 : insert() 예제
# doc = {"name":"jane", "age":"21"}
# db의 users collection(==table?)에  doc(딕셔너리형 데이터) 삽입
# db.users.insert_one(doc)

# 데이터 탐색 : find() 예제
# {'_id': False}를 해주지 않으면 해당 데이터의 _id 값인 ObjectId까지 불러옴
# find() : 조건에 부합하는 한가지 데이터만 추출
# find_one() : 조건에 부합하는 데이터 모두 추출
# 특정 콜렉션의 전체 데이터를 확인할 경우 : print(list(db.users.find({}, {'_id': False})))
# same_ages = list(db.users.find({'age': "21"}, {'_id': False}))
#
# for person in same_ages:
#     print(person)

# 데이터 수정 : update() 예제
# update_one() : 해당 조건에 부합하는 수정 사항을 한번 수행
# update_many() : 해당 조건을 부합하는 수정 사항을 모두 수행
# db.users.update_one({'name': 'bobby'}, {'$set': {'age': 19}})
# db.users.update_many({'name': 'bobby'}, {'$set': {'age': 19}})


# 데이터 삭제 : delete() 예제
# delete_one() : 해당 조건에 부합 하는 데이터 한개 삭제
db.users.delete_one({'name': 'bobby'})
