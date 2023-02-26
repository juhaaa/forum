from secrets import token_hex
from flask import redirect, render_template, request, session, flash, abort
from app import app
import discussion_querys
import discussion_insert
import discussion_update
import users
import admin_sql

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/discussion")
def discussion():

    # route for displaying discussion zones

    if session["name"]:
        zones = discussion_querys.get_discussion_zones()
        return render_template("discussion.html", zones=zones)
    return render_template("discussion.html")

@app.route("/discussion/<name>")
def discussion_zone(name):

    # route for displaying url- parameter zone
    if session["name"]:
        zone = discussion_querys.get_zone_name(name)
        topics = discussion_querys.get_topics(zone.id)
        return render_template("/zone.html", name=name, zone=zone, topics=topics)
    return render_template("zone.html")

@app.route("/discussion/<name>/<topic_id>")
def discussion_topic(name, topic_id):

    # Route displaying specific topic under specific zone given in url parameters
    if session["name"]:
        topic = discussion_querys.get_first_message(topic_id)
        user_id = users.get_user_id(session["name"])
        replies = discussion_querys.get_replies(topic_id, user_id[0])
        return render_template("topic.html",
                                name=name,
                                topic_id=topic_id,
                                topic=topic,
                                replies=replies,
                                user_id=user_id[0])
    return render_template("topic.html")

@app.route("/newzone", methods=["GET", "POST"])
def admin_new_zone():

    # Route for admin to create new discussion zone
    if session["admin"]:
        if request.method == 'POST':
            if session["csrf_token"] != request.form.get("csrf_token"):
                abort(403)
            zone_name = request.form.get("zone_name")
            if admin_sql.add_new_zone(zone_name):
                flash(f"Zone {zone_name} created", "success")
                return redirect("/discussion")
            flash("Zone not created", "error")
            return render_template("newzone.html")
    return render_template("newzone.html")

@app.route("/deletezone/<zone_id>/<name>", methods=["GET", "POST"])
def admin_delete_zone(zone_id, name):

    # Route for admin to delete discussion zone

    if session["admin"]:
        if request.method == 'POST':
            if session["csrf_token"] != request.form.get("csrf_token"):
                abort(403)
            if request.form.get("yes_no") == "yes":
                admin_sql.delete_zone(zone_id)
                flash(f"Zone {name} deleted.", "success")
                return redirect("/discussion")
            return redirect("/discussion")
    return render_template("/deletezone.html", name=name, zone_id=zone_id)

@app.route("/deletetopic/<zone_name>/<topic_id>/<title>", methods=["GET", "POST"])
def admin_delete_topic(topic_id, title, zone_name):

    # Route for admin, deleting topics

    if session["admin"]:
        if request.method == 'POST':
            if session["csrf_token"] != request.form.get("csrf_token"):
                abort(403)
            url = "/discussion/" + zone_name
            if request.form.get("yes_no") == "yes":
                admin_sql.delete_topic(topic_id)
                flash(f"Topic \"{title}\" deleted.", "success")
                return redirect(url)
            return redirect(url)
    return render_template("/deletetopic.html", title=title, topic_id=topic_id, zone_name=zone_name)


@app.route("/deletereply/<zone_name>/<topic_id>/<reply_id>/<username>", methods=["GET", "POST"])
def admin_delete_reply(zone_name, topic_id, reply_id, username):

    # Route for admin to delete replys

    if session["admin"]:
        if request.method == 'POST':
            if session["csrf_token"] != request.form.get("csrf_token"):
                abort(403)
            url = "/discussion/" + zone_name + "/" + topic_id
            if request.form.get("yes_no") == "yes":
                admin_sql.delete_reply(reply_id)
                flash(f"{username}'s reply deleted.", "success")
                return redirect(url)
            return redirect(url)

    return render_template("deletereply.html",
                            zone_name=zone_name,
                            topic_id=topic_id,
                            reply_id=reply_id,
                            username=username)

@app.route("/newtopic/<zone_name>", methods=["GET", "POST"])
def new_topic(zone_name):

    # Route for creating new topic
    if session["name"]:
        zone = discussion_querys.get_zone_name(zone_name)
        if request.method == 'POST':
            if session["csrf_token"] != request.form.get("csrf_token"):
                abort(403)
            title = request.form.get("title")
            content = request.form.get("content")
            user_id = users.get_user_id(session["name"])
            url = "/discussion/" + zone_name
            if discussion_insert.post_new_topic(zone.id, title, content, user_id.id):
                flash("New topic created", "success")
                return redirect(url)
            flash("Topic not created", "error")
            return redirect(url)
        return render_template("newtopic.html", zone=zone)
    return render_template("newtopic.html")


@app.route("/reply/<topic_id>", methods=["GET", "POST"])
def new_reply(topic_id):

    # Route for replying to a topic

    if session["name"]:
        title, zone = discussion_querys.get_title_and_zone(topic_id)
        if request.method == 'POST':
            if session["csrf_token"] != request.form.get("csrf_token"):
                abort(403)
            user = users.get_user_id(session["name"])
            content = request.form.get("content")
            url = "/discussion/" + zone + "/" + topic_id
            if discussion_insert.reply_to_topic(user.id, content, topic_id):
                flash("You replied successfully", "success")
                return redirect(url)
            flash("Reply not posted", "error")
            return redirect(url)
        return render_template("reply.html", title=title, zone=zone, topic_id=topic_id)
    return render_template("reply.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    # Route for login

    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if users.check_login(username, password):
            session["name"] = username
            session["csrf_token"] = token_hex(16)
            if users.check_admin(username):
                flash("Admin logged in", "success")
                session["admin"] = True
            else:
                session["admin"] = False
            return redirect("/discussion")
        flash('Check your username and password', 'error')
        return render_template("login.html")
    return render_template("login.html")



@app.route("/logout")
def logout():

    # Route for logout

    session["name"] = None
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


@app.route("/search", methods=["GET"])
def search():

    # Route for searching messages
    if session["name"]:
        q = request.args.get("q")
        print(q)
        if q:
            topics = discussion_querys.search(q)

            return render_template("search.html", topics=topics)
    return render_template("search.html")

@app.route("/editreply/<name>/<topic_id>/<reply_id>/", methods=["GET", "POST"])
def edit_reply(name, topic_id, reply_id):

    # Route for modifying messages

    username, content = discussion_querys.get_username_and_content(reply_id)
    if session["name"] == username or session["admin"]:
        if request.method == 'POST':
            if session["csrf_token"] != request.form.get("csrf_token"):
                abort(403)
            content = request.form.get("content")
            discussion_update.edit_reply(reply_id, content)
            url = "/discussion/" + name + "/" + topic_id
            flash("Message updated", "success")
            return redirect(url)
        elif request.method == "GET":
            return render_template("editreply.html",
                                    topic_id=topic_id,
                                    reply_id=reply_id,
                                    username=username,
                                    content=content,
                                    name=name)
    return render_template("editreply.html")

@app.route("/edittopic/<name>/<topic_id>", methods=["GET", "POST"])
def edit_topic(name, topic_id):

    # Route for modifying topics

    title, content, username = discussion_querys.get_topic(topic_id)
    if session["name"] == username or session["admin"]:
        if request.method == 'POST':
            if session["csrf_token"] != request.form.get("csrf_token"):
                abort(403)
            content = request.form.get("content")
            title = request.form.get("title")
            discussion_update.edit_topic(topic_id, content, title)
            url = "/discussion/" + name
            flash("Topic updated", "success")
            return redirect(url)
        elif request.method == "GET":
            return render_template("edittopic.html",
                                    username=username,
                                    name=name,
                                    topic_id=topic_id,
                                    title=title,
                                    content=content)
    return render_template("edittopic.html")
                            
@app.route("/addlike/<user_id>/<reply_id>", methods=["POST"])
def add_like(user_id, reply_id):

    # Route for liking replies
    if session["name"]:
        if discussion_querys.check_like(user_id, reply_id):
            flash("You have already liked this post", "error")
            return redirect(request.form.get('next'))
        discussion_insert.like_post(user_id, reply_id)
        flash("Post liked", "success")
    return redirect(request.form.get('next'))
