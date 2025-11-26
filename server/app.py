import os
import hashlib
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())

@app.route("/")
def index():
    return "OK"

@app.route("/users", methods=["GET"]) 
def list_users():
    users = User.query.order_by(User.id.asc()).all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])

@app.route("/users", methods=["POST"]) 
def create_user():
    data = request.get_json(silent=True) or {}
    name = data.get("name") or request.args.get("name")
    if not name:
        return jsonify({"error": "name required"}), 400
    if User.query.filter_by(name=name).first():
        return jsonify({"error": "user exists"}), 409
    user = User(name=name)
    db.session.add(user)
    db.session.flush()

    username = data.get("username") or name
    password = data.get("password")
    if password:
        if Account.query.filter_by(username=username).first():
            return jsonify({"error": "username exists"}), 409
        password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
        acc = Account(
            user_id=user.id,
            username=username,
            password_hash=password_hash
        )
        db.session.add(acc)

    db.session.commit()
    return jsonify({"id": user.id, "name": user.name}), 201

@app.route("/login", methods=["POST"]) 
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username") or request.args.get("username")
    password = data.get("password") or request.args.get("password")
    if not username or not password:
        return jsonify({"error": "username and password required"}), 400
    acc = Account.query.filter_by(username=username).first()
    if not acc:
        return jsonify({"error": "invalid credentials"}), 401
    input_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    if acc.password_hash != input_hash:
        return jsonify({"error": "invalid credentials"}), 401
    user = User.query.get(acc.user_id)
    return jsonify({"ok": True, "user": {"id": user.id, "name": user.name, "username": acc.username}})

def ensure_tables():
    with app.app_context():
        db.create_all()

@app.route("/articles", methods=["GET"]) 
def list_articles():
    items = Article.query.order_by(Article.id.desc()).all()
    result = []
    for a in items:
        u = User.query.get(a.author_id)
        result.append({
            "id": a.id,
            "title": a.title,
            "content": a.content,
            "author_id": a.author_id,
            "author_name": u.name if u else None,
            "created_at": a.created_at.isoformat() if a.created_at else None
        })
    return jsonify(result)

@app.route("/articles", methods=["POST"]) 
def create_article():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    content = data.get("content")
    username = data.get("username") or request.args.get("username")
    if not title or not content or not username:
        return jsonify({"error": "title, content, username required"}), 400
    acc = Account.query.filter_by(username=username).first()
    if not acc:
        return jsonify({"error": "unknown username"}), 404
    a = Article(title=title, content=content, author_id=acc.user_id)
    db.session.add(a)
    db.session.commit()
    return jsonify({"id": a.id, "title": a.title, "content": a.content}), 201

@app.route("/articles/<int:article_id>", methods=["PUT"]) 
def update_article(article_id):
    a = Article.query.get(article_id)
    if not a:
        return jsonify({"error": "not found"}), 404
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    content = data.get("content")
    if title:
        a.title = title
    if content:
        a.content = content
    db.session.commit()
    return jsonify({"id": a.id, "title": a.title, "content": a.content})

@app.route("/articles/<int:article_id>", methods=["DELETE"]) 
def delete_article(article_id):
    a = Article.query.get(article_id)
    if not a:
        return jsonify({"error": "not found"}), 404
    Comment.query.filter_by(article_id=article_id).delete()
    db.session.delete(a)
    db.session.commit()
    return jsonify({"ok": True})

@app.route("/articles/<int:article_id>/comments", methods=["GET"]) 
def list_comments(article_id):
    a = Article.query.get(article_id)
    if not a:
        return jsonify({"error": "not found"}), 404
    items = Comment.query.filter_by(article_id=article_id).order_by(Comment.id.asc()).all()
    result = []
    for c in items:
        u = User.query.get(c.author_id)
        result.append({
            "id": c.id,
            "article_id": c.article_id,
            "author_id": c.author_id,
            "author_name": u.name if u else None,
            "content": c.content,
            "created_at": c.created_at.isoformat() if c.created_at else None
        })
    return jsonify(result)

@app.route("/articles/<int:article_id>/comments", methods=["POST"]) 
def create_comment(article_id):
    a = Article.query.get(article_id)
    if not a:
        return jsonify({"error": "not found"}), 404
    data = request.get_json(silent=True) or {}
    content = data.get("content")
    username = data.get("username") or request.args.get("username")
    if not content or not username:
        return jsonify({"error": "content and username required"}), 400
    acc = Account.query.filter_by(username=username).first()
    if not acc:
        return jsonify({"error": "unknown username"}), 404
    c = Comment(article_id=article_id, author_id=acc.user_id, content=content)
    db.session.add(c)
    db.session.commit()
    return jsonify({"id": c.id, "content": c.content}), 201

@app.route("/comments/<int:comment_id>", methods=["DELETE"]) 
def delete_comment(comment_id):
    c = Comment.query.get(comment_id)
    if not c:
        return jsonify({"error": "not found"}), 404
    db.session.delete(c)
    db.session.commit()
    return jsonify({"ok": True})

if __name__ == "__main__":
    ensure_tables()
    app.run(host="0.0.0.0", port=5000)
