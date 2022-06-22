from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.moviesDB

collection = db.kor_movies

movie_data = { 'title': '범죄도시2',
               'genre': '범죄, 액션',
               'nation': '한국',
               'director': '이상용',
               'release': '2022-05-18',
               'star_score': 9.07 }

collection.delete_one({'Leading actor': '손석구'})
# db.users.update_many({'name': 'bobby'}, {'$set': {'age': 19}})