from flask import Flask, render_template, jsonify, request
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
@app.route('/orderInfo', methods=['GET'])
def listing():
    orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'all_orders': orders})

# Ordering API
@app.route('/orderInfo', methods=['POST'])
def saving():
    name_receive = request.form['name_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    # pyMongo set
    doc = {'order_name': name_receive,
           'order_amount': amount_receive,
           'order_address': address_receive,
           'order_phone': phone_receive}

    db.orders.insert_one(doc)

    return jsonify({'msg': '주문이 완료되었습니다.'})

# Delete API
@app.route('/delete', methods=['POST'])
def delete_article():
    name = request.form['order_name']
    amount = request.form['order_amount']

    # pyMongo set
    collection = db.orders
    target_data = collection.find_one({'order_name': name, 'order_amount': amount}, {'_id': False})
    collection.delete_one(target_data)

    return jsonify({'msg': '주문 정보가 제거되었습니다.'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)