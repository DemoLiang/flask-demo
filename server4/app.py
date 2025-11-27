import os
import hashlib
from crypt import methods
from datetime import datetime
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from pycparser.ply.yacc import resultlimit

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/flask_demo?charset=utf8mb4"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    # email = db.Column(db.String(255))

class Account(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"))
    username=db.Column(db.String(255))
    password = db.Column(db.String(255))

@app.route("/")
def index():
    return "ok"

@app.route('/login',methods=["POST"])
def login():
    data = request.get_json() or {}
    username = data.get("username")
    passw = data.get("password")
    if not username or not passw:
        return jsonify({"error":"args err"}),400
    acc = Account.query.filter_by(username=username).first()
    if not acc:
        return jsonify({"error":"user record not find"}),400
    passw_hash = hashlib.sha256(passw.encode("utf-8")).hexdigest()
    if acc.password != passw_hash:
        return jsonify({"error":"password err"})
    user_info = User.query.get(acc.user_id)
    return jsonify({"id":user_info.id,"username":acc.username,"token":datetime.now().timestamp()})

@app.route('/users',methods=["POST"])
def users():
    userList = User.query.all()
    result = []
    for user in userList:
        result.append({
            "id":user.id,
            "name":user.name,
        })
    return jsonify(result)


@app.route('/add_user',methods=["POST"])
def add_user():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error":"args err"}),400
    user_info = User(name=username)
    db.session.add(user_info)
    db.session.commit()

    passw_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    acc = Account(user_id=user_info.id,username=username,password=passw_hash)
    db.session.add(acc)
    db.session.commit()

    return jsonify({"success":True}),201

def ensure_table():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    app.run(port=5000,debug=True)
