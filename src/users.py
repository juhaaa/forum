from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
from db import db


def check_login(username, password):
    """ Check credentials
        Retrieves hashed pw from database and compares

    Args:
        username (String): Username
        password (String): PAssword

    Returns:
        Boolean: True if correct credentials
    """
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

    """Checks for users admin staus

    Returns:
        Boolean: True if admin
    """

    sql = text("SELECT is_admin FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if user.is_admin:
        return True
    return False


# Functions for registering user

def check_passwords(password1, password2):

    """ Function for checking user given passwords
        when registering users

    Args:
        password1 (String): Users password proposal
        passowrd2 (String): Should be same password second time

    Returns:
        Boolean: True if passwords match
    """

    if password1 != password2:
        return False
    return True

def check_username_length(username):
    """ Function checks username length

    Args:
        username (String): Users username proposal


    Returns:
        Boolean: True if under 20 chars
    """

    if len(username) <= 20:
        return True
    return False

def check_username_availabillity(username):
    """Checks username availability

    Args:
        username (String): Users username proposal

    Returns:
        Boolean: True if username doesnt exist in db
    """

    sql = text("SELECT * FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return True
    return False

def register_user(username, password):
    """Registers user

    Args:
        username (String): username
        password (String): password

    """

    hash_value = generate_password_hash(password)
    sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()

def get_user_id(username):
    """Retrieves user id from db

    Args:
        username (String): username to be searched

    Returns:
        Int: user_id
    """

    sql = text("SELECT id FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user_id = result.fetchone()
    return user_id

def get_banned_status(username):
    """Retrieves boolean of column banned in table user

    Args:
        username (String): username

    Returns:
        Boolean: True if banned
    """

    sql = text("SELECT banned FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    boolean = result.fetchone()
    return boolean.banned

def ok_to_post(username, csfr1, csfr2):
    """Checks posting rights

    Args:
        username (String): username
        csfr1 (String): session token
        csfr2 (String): token via POST

    Returns:
        Boolean: True if user checks out
    """

    banned, csfr = False, False
    if get_banned_status(username):
        banned = True
    if csfr1 == csfr2:
        csfr = True
    if not banned and csfr:
        return True
    return False
