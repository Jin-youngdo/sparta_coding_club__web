# pymongo 라이브러리 import
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# Quiz 01. 영화 제목 '매트릭스'의 평점을 가져오기
print('《 Quiz 01 》')
movies__Matrix = db.movies_02.find_one({'title': '매트릭스'}, {'_id': False})
Matrix_score = movies__Matrix['score']
print(Matrix_score)

# Quiz 02. '매트릭스'의 평점과 같은 영화들의 제목을 가져오기
print('\n《 Quiz 02 》')
movies_list = list(db.movies_02.find({'score': Matrix_score}, {'_id': False}))
for movie in movies_list:
    print(movie['title'])

# Quiz 03. '매트릭스' 영화의 평점을 0으로 만들기
print('\n《 Quiz 03 》')
db.movies_02.update_one({'title': '매트릭스'}, {'$set': {'score': 0}})