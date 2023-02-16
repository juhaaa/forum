from app import app
from flask import redirect, render_template, request, session, flash
from sqlalchemy.sql import text
import discussion_querys
import users
from db import db

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/discussion")
def discussion():

    # route for displaying discussion zones

    zones = discussion_querys.get_discussion_zones()
    return render_template("discussion.html", zones=zones)

@app.route("/discussion/<name>")
def zone(name):

    # route for displaying url- parameter zone

    zone = discussion_querys.get_zone_name(name)
    topics = discussion_querys.get_topics(zone.id)
    return render_template("/zone.html", name=name, zone=zone, topics=topics)

@app.route("/discussion/<name>/<topic_id>")
def topic(name, topic_id):

    # Route displaying specific topic undr speicif zone given in url parameters

    topic = discussion_querys.get_first_message(topic_id)
    replies =discussion_querys.get_replies(topic_id)
    return render_template("/topic.html", name=name, topic_id=topic_id, topic=topic, replies=replies)

@app.route("/newzone")
def admin_new_zone():

    # Route for admin to create new discussion zone

    return "newzone"

@app.route("/deletezone/<name>")
def admin_delete_zone(name):

    # Route for admin to delete discussion zone

    return f"delete zone {name}"

@app.route("/deletetopic/<topic_id>")
def admin_delete_topic(topic_id):

    # Route for admin, deleting topics

    return f"delete topic {topic_id}"

@app.route("/deletereply/<reply_id>")
def admin_delete_reply(reply_id):

    # Route for admin to delete replys

    return f"delete reply {reply_id}"

@app.route("/new/<zone_id>")
def new_topic(zone_id):

    # Route for creating new topic

    return f"New topic under zone {zone_id}"

@app.route("/reply/<topic_id>")
def new_reply(topic_id):

    # Route for replying to a topic

    return f"New reply under topic {topic_id}"


@app.route("/login", methods=["GET", "POST"])
def login():

    # Route for login
    
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if users.check_login(username, password):
            session["name"] = username
            if users.check_admin(username):
                session["admin"] = True
            return redirect("/discussion")
        flash("Check your username and password")    
        return render_template("login.html")
    else:
        return render_template("login.html")
        


@app.route("/logout")
def logout():

    # Route for logout

    session["name"] = None
    if "admin" in session:
        session["admin"] = None
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():

    # Route for registering

    if request.method == 'POST':
        username = request.form.get("username")
        password1 = request.form.get("password")
        password2 = request.form.get("password2")

        if not users.check_passwords(password1, password2):
            return "not same passes"
        
        if not users.check_username_lenght(username):
            return "too long username"

        if not users.check_username_availabillity(username):
            return "username taken"
        
        users.register_user(username, password1)
        return redirect("/login")

    return render_template("register.html")


@app.route("/search")
def search():

    # Route for searching messages

    return "SEARCH"