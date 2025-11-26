import hashlib
from datetime import datetime

from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://root:123456@localhost:3306/flask-demo?charset=utf8mb4"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))

class Account(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    passw = db.Column(db.String(256))
    username = db.Column(db.String(256))

class Article(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(256))
    content = db.Column(db.String(1024))
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime,default=db.func.now())

class Comment(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    article_id = db.Column(db.Integer,db.ForeignKey('article.id'))
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    content = db.Column(db.String(1024))
    created_at = db.Column(db.DateTime,default=db.func.now())

@app.route('/')
def index():
    return "ok"

@app.route('/users',methods=['POST'])
def list_users():
    users = User.query.order_by(User.id.asc()).all()
    return jsonify([{"id":u.id,"name":u.name} for u in users])


@app.route('/login',methods=["POST"])
def login():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error":"args"}),400
    acc = Account.query.filter_by(username=username).first()
    if not acc:
        print("Account not exist")
        return jsonify({"error":"Account not exist"}),400
        return jsonify({"error":"unknow username"}),400
    password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    print('password:',password_hash)
    print('acc.password:',acc.passw)
    if password_hash!=acc.passw:
        return jsonify({"error":"password err"})
    u = User.query.get(acc.user_id)
    return jsonify({"token":datetime.now().timestamp(),"id":acc.user_id,"username":acc.username})

@app.route("/articles",methods=["POST"])
def list_articles():
    items = Article.query.order_by(Article.id.asc()).all()
    result = []
    for item in items:
        userInfo = User.query.get(item.author_id)
        result.append({
            "id":item.id,
            "title":item.title,
            "content":item.content,
            "author_id":item.author_id,
            "author_name":userInfo.name if userInfo else None,
            "created_at":item.created_at.isoformat() if item.created_at else None
        })
    print(result)
    return jsonify(result)

@app.route("/create_article",methods=["POST"])
def create_article():
    data = request.get_json() or {}
    title=data.get('title')
    content=data.get('content')
    author_name=data.get('username')
    if not title or not content or not author_name:
        return jsonify({"error":"args"}),400
    acc = Account.query.filter_by(username=author_name).first()
    if not acc:
        return jsonify({"error":"Account not exist"}),440
    a=Article(title=title,content=content,author_id=acc.user_id)
    db.session.add(a)
    db.session.commit()
    return jsonify({"id":a.id}),201

def ensure_table():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    ensure_table()
    app.run(host='0.0.0.0',port=5000,debug=True)
    