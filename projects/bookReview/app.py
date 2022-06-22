from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

# -- Flask Server Run --
app = Flask(__name__)

# -- MongoDB Settings --
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
# 클라이언트로부터 리뷰 데이터를 전달받아 DB로 전달
@app.route('/review', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    doc = { 'title':  title_receive,
            'author': author_receive,
            'review': review_receive }
    db.bookreview.insert_one(doc)

    return jsonify({'msg': '리뷰 저장 완료'})

# DB내 collection의 데이터를 가져와 클라이언트로 전달
@app.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.bookreview.find({}, {'_id': False}))
    return jsonify({'all_reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)