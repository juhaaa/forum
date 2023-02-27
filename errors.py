from flask import redirect, render_template, request, session, flash
from app import app

@app.errorhandler(404)
def handle_404(e):
    flash("The page your looking for doesn't exist")
    message = "Please check your URL"
    return render_template("error.html", message=message)

@app.errorhandler(403)
def handle_403(e):
    flash("You are either banned or overstepping your user rights")
    message = "You can't post or modify messages if you are banned"
    return render_template("error.html", message=message)

@app.errorhandler(500)
def handle_500(e):
    flash("We seem to be experiencing some problems server-side")
    message = "Try reloading the page or check your URL"
    return render_template("error.html", message=message)
