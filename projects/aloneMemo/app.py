from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# -- flask settings --
app = Flask(__name__)

# -- pyMongo settings --
client = MongoClient('localhost', 27017)
db = client.dbsparta

## -- flask APP Routing --
@app.route('/')
def home():
   return render_template('index.html')

# Listing API
@app.route('/memo', methods=['GET'])
def listing():
    articles = list(db.articles.find({}, {'_id': False}))
    return jsonify({'all_articles': articles})

# Posting API
@app.route('/memo', methods=['POST'])
def saving():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    # request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    # bs4 set
    soup = BeautifulSoup(data.text, 'html.parser')
    og_title = soup.select_one('meta[property="og:title"]')['content']
    og_image = soup.select_one('meta[property="og:image"]')['content']
    og_description = soup.select_one('meta[property="og:description"]')['content']

    # pyMongo set
    doc = {'title': og_title,
           'image': og_image,
           'description': og_description,
           'url': url_receive,
           'comment': comment_receive}

    db.articles.insert_one(doc)

    return jsonify({'msg': '기사 저장이 완료되었습니다.'})

# Delete API
@app.route('/delete', methods=['POST'])
def delete_article():
    title = request.form['article_title']
    comment = request.form['article_comment']

    # pyMongo set
    collection = db.articles
    target_data = collection.find_one({'title': title, 'comment': comment}, {'_id': False})
    collection.delete_one(target_data)

    return jsonify({'msg': '기사가 제거되었습니다.'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)