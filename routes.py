from app import app
from flask import redirect, render_template, request, session, flash
import discussion_querys
import users
import admin_sql
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

@app.route("/newzone", methods=["GET", "POST"])
def admin_new_zone():

    # Route for admin to create new discussion zone

    if request.method == 'POST':
        zone_name = request.form.get("zone_name")
        if admin_sql.add_new_zone(zone_name):
            flash(f"Zone {zone_name} created", "success")
            return redirect("/discussion")
        else:
            flash("Zone not created", "error")
            return render_template("newzone.html")

    return render_template("newzone.html")

@app.route("/deletezone/<id>/<name>", methods=["GET", "POST"])
def admin_delete_zone(id, name):

    # Route for admin to delete discussion zone

    if request.method == 'POST':
        if request.form.get("yes_no") == "yes":
            admin_sql.delete_zone(id)
            flash(f"Zone {name} deleted.", "success")
            return redirect("/discussion")
        else:
            return redirect("/discussion")
    return render_template("/deletezone.html", name=name, id=id)

@app.route("/deletetopic/<zone_name>/<topic_id>/<title>", methods=["GET", "POST"])
def admin_delete_topic(topic_id, title, zone_name):

    # Route for admin, deleting topics

    if request.method == 'POST':
        url = "/discussion/" + zone_name
        if request.form.get("yes_no") == "yes":
            admin_sql.delete_topic(topic_id)
            flash(f"Topic \"{title}\" deleted.", "success")
            return redirect(url)
        else:
            return redirect(url)
    return render_template("/deletetopic.html", title=title, topic_id=topic_id, zone_name=zone_name)


@app.route("/deletereply/<zone_name>/<topic_id>/<reply_id>/<username>", methods=["GET", "POST"])
def admin_delete_reply(zone_name, topic_id, reply_id, username):

    # Route for admin to delete replys

    if request.method == 'POST':
        url = "/discussion/" + zone_name + "/" + topic_id
        if request.form.get("yes_no") == "yes":
            admin_sql.delete_reply(reply_id)
            flash(f"{username}'s reply deleted.", "success")
            return redirect(url)
        else:
            return redirect(url)

    return render_template("deletereply.html", zone_name=zone_name, topic_id=topic_id, reply_id=reply_id, username=username)

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
                flash("Admin logged in", "success")
                session["admin"] = True
            return redirect("/discussion")
        flash('Check your username and password', 'error')    
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
            flash("Check your passwords", "error")
            return render_template("register.html")
        
        if not users.check_username_length(username):
            flash("Username too long", "error")
            return render_template("register.html")
        
        if not users.check_username_availabillity(username):
            flash(f"Username {username} is already in use", "error")
            return render_template("register.html")
        
        users.register_user(username, password1)
        flash(f"You are now registered, {username}!", "success")
        return redirect("/login")
    
    return render_template("register.html")
    


@app.route("/search")
def search():

    # Route for searching messages

    return "SEARCH"