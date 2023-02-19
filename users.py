from db import db
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash

def check_login(username, password):

    # Checking credentials
    sql = text("SELECT password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    hash_value = user.password
    if check_password_hash(hash_value, password):
        return True
    return False

def check_admin(username):

    # Check admin status

    sql = text("SELECT is_admin FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if user.is_admin == True:
        return True
    return False


# Functions for registering user

def check_passwords(password1, password2):

    # checks that passwords match
    
    if password1 != password2:
        return False
    return True

def check_username_length(username):

    # checks username length

    if len(username) <= 20:
        return True
    return False

def check_username_availabillity(username):
    
    # Checks if username exists

    sql = text("SELECT * FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if not user:
        return True
    return False

def register_user(username, password):

    # registers user

    hash_value = generate_password_hash(password)
    sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()
    return True

def get_user_id(username):

    # given username, returns id

    sql = text("SELECT id FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user_id = result.fetchone()
    return user_id