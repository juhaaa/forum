from app import app
from flask import redirect, render_template, request, session
from sqlalchemy.sql import text
import discussion_querys
from db import db

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/discussion")
def discussion():
    zones = discussion_querys.get_discussion_zones()
    return render_template("discussion.html", zones=zones)

@app.route("/discussion/<name>")
def zone(name):
    zone = discussion_querys.get_zone_name(name)
    topics = discussion_querys.get_topics(zone.id)
    return render_template("/zone.html", name=name, zone=zone, topics=topics)

@app.route("/discussion/<name>/<topic_id>")
def topic(name, topic_id):
    topic = discussion_querys.get_first_message(topic_id)
    replies =discussion_querys.get_replies(topic_id)
    return render_template("/topic.html", name=name, topic_id=topic_id, topic=topic, replies=replies)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
      session["name"] = request.form.get("username")
      return redirect("/discussion")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")