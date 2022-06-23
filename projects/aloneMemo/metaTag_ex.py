# meta 태그 크롤링 예제
import requests
from bs4 import BeautifulSoup

# -- requests settings --
url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=171539'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

# -- bs4 settings --
soup = BeautifulSoup(data.text, 'html.parser')

# -- meta tag crawling --
og_title = soup.select_one('meta[property="og:title"]')['content']
og_image = soup.select_one('meta[property="og:image"]')['content']
og_description = soup.select_one('meta[property="og:description"]')['content']

print(og_title)
print(og_image)
print(og_description)
