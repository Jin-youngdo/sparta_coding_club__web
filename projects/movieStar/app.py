from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

# -- Flask Setting --
app = Flask(__name__)

# -- pyMongo Settings --
client = MongoClient('localhost', 27017)
db = client.dbsparta

## -- Routings --
# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
# Show Table API
@app.route('/api/list', methods=['GET'])
def show_stars():
    # mystar 콜렉션에서 모든 DB 가져오기 ['like'수 내림차순 정렬 : sort() ]
    movie_star = list(db.mystar.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'movie_stars': movie_star})

# Plus Like API
@app.route('/api/like', methods=['POST'])
def like_star():
    name_receive = request.form['name_give']

    target_star = db.mystar.find_one({'name': name_receive})
    current_like = target_star['like']
    new_like = current_like + 1

    db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': '좋아요 완료!'})

# Delete Card API
@app.route('/api/delete', methods=['POST'])
def delete_star():
    name_receive = request.form['name_give']
    db.mystar.delete_one({'name': name_receive})

    return jsonify({'msg': 'delete 완료되었습니다!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)