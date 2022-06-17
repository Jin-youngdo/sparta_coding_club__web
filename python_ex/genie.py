# 2020-04-03 기준 지니뮤직 1-50위 차트 크롤링 예제
import requests
from bs4 import BeautifulSoup

# -- requests settings --
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# -- bs4 settings --
soup = BeautifulSoup(data.text, 'html.parser')
trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for tr in trs:
    rating = list(tr.select_one('td.number'))[0].text.strip()
    info = tr.select_one('td.info')
    title = info.select_one('a.title').text.strip()
    artist = info.select_one('a.artist').text
    print(rating + " " + title + " " + artist)