import re
from flask import Flask, g, request, abort, jsonify, make_response
from flask_cors import CORS, cross_origin
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

from FDataBase import FDataBase

DATABASE = '/tmp/server_db.db'
DEBUG = True
SECRET_KEY = 'vsdghjklagsdghfjlksdknglw'

app = Flask(__name__)
app.config.from_object(__name__)
cors = CORS(app)


app.config.update(dict(DATABASE=os.path.join(app.root_path, 'server_db.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(x):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.before_request
def make_db_connection():
    global dbase
    db = get_db()
    dbase = FDataBase(db)


@app.route('/api/v1.0/', methods=['POST'])
def check():
    return jsonify({'server_status': 'online'})


@app.route('/api/v1.0/add', methods=['POST'])
def add():
    print(request.json)
    if request.json:
        new = {
            'organisation': request.json['organisation'],
            'until': request.json['until'],
            'category': request.json['category'],
            'load_date': request.json['load_date'],
            'unload_date': request.json['unload_date'],
            'responsible': request.json['responsible'],
            'comment': request.json['comment']
        }
        res = dbase.add(new)
        if res:
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 400})
    else:
        return jsonify({'status': 400})


@app.route('/api/v1.0/suppliers', methods=["GET"])
def get_suppliers_list():
    return jsonify({'suppliers': dbase.get_suppliers_list()})


@app.route('/api/v1.0/suppliers/<int:id_supplier>', methods=['DELETE'])
def delete(id_supplier):
    res = dbase.delete(id_supplier)
    return jsonify({'status': res})


@app.route('/api/v1.0/suppliers/<int:id_supplier>', methods=['PUT'])
def change(id_supplier):
    res = dbase.change(id_supplier, request.json)
    if res:
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 400})


@app.route('/api/v1.0/register', methods=['POST'])
def registration():
    if request:
        user_names = dbase.get_users()
        if not (request.json['user_name'] in user_names):
            pswrd_hash = generate_password_hash(request.json['password'])
            res_data = dbase.add_user(request.json['user_name'], pswrd_hash)
            return jsonify({'data': res_data, 'status': 'success'})
        else:
            return jsonify({'status': 400})
    else:
        return jsonify({'status': 400})


@app.route('/api/v1.0/login', methods=['POST'])
def login():
    if request:
        user_data = dbase.get_user_data(request.json['user_name'])
        if user_data:
            if check_password_hash(user_data[2], request.json['password']):
                data = {'user_name': user_data[1], 'role': user_data[3]}
                print('Все ок')
                return jsonify({'data': data, 'status': 'success'})
            else:
                return jsonify({'status': 400})
        return jsonify({'status': 400})
    else:
        return jsonify({'status': 400})

@app.route('/api/v1.0/getColumns', methods=['GET'])
def getColumns():
    return jsonify(dbase.getColums(request.json()['table_name']))


if __name__ == '__main__':
    app.run(debug=True, port=5050)
