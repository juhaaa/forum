from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SESSION_PERMANENT"] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("//discussion")
def discussion():
    sql = text("SELECT id, name FROM discussion_zones ORDER BY id")
    result = db.session.execute(sql)
    zones =  result.fetchall()
    return render_template("discussion.html", zones=zones)

@app.route("/discussion/<name>")
def zone(name):
    sql = text("SELECT name, id FROM discussion_zones WHERE name=:name")
    result = db.session.execute(sql,  {"name":name})
    zone =  result.fetchone()
    sql2 = text("SELECT topics.id, topics.user_id, topics.title, topics.content, users.username, created_at FROM topics LEFT JOIN users ON users.id=topics.user_id WHERE topics.discussion_zone_id=:zoneid ORDER BY topics.created_at DESC")
    result2 = db.session.execute(sql2, {"zoneid":zone.id})
    topics = result2.fetchall()
    return render_template("/zone.html", name=name, zone=zone, topics=topics)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
      session["name"] = request.form.get("username")
      return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")
