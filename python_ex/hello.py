import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# -- requests settings --
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20200303',headers=headers)

# -- pymongo settings --
client = MongoClient('localhost', 27017)
db = client.dbsparta

# -- bs4 settings --
soup = BeautifulSoup(data.text, 'html.parser')
trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    a_tag = tr.select_one('.title > .tit5 > a')
    if a_tag is not None:
        # ac 클래스가 두개 존재함 nth-child 문을 통해 식별
        movie_rating = tr.select_one('td:nth-child(1) > img')['alt']
        movie_score = tr.select_one('td.point').text
        movie_title = a_tag.text

        print("[" + movie_rating + "] " + movie_title + " | " + movie_score)
        doc = {'title': movie_title,
               'rating': movie_rating,
               'score': movie_score}
        db.movies_02.insert_one(doc)

