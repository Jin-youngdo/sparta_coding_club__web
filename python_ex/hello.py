import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20220612',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')
for tr in trs:
    a_tag = tr.select_one('.title > .tit5 > a')
    if a_tag is not None:
        title = a_tag.text
        print(title)
