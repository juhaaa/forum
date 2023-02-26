from sqlalchemy.sql import text
from db import db

def add_new_zone(zone_name):

    """Function allows admin to insert new discussion zone

    Returns:
        Boolean: Returns boolean
    """

    if len(zone_name) <= 50:
        sql = text("INSERT INTO discussion_zones (name) VALUES (:zone_name)")
        db.session.execute(sql, {"zone_name":zone_name})
        db.session.commit()
        return True
    return False

def delete_zone(zone_id):

    """ Function for deleting zones
    """

    sql = text("DELETE FROM discussion_zones WHERE id=:zone_id")
    db.session.execute(sql, {"zone_id":zone_id})
    db.session.commit()

def delete_topic(topic_id):

    """Function for deleting topics
    """

    sql = text("DELETE FROM topics WHERE id=:topic_id")
    db.session.execute(sql, {"topic_id":topic_id})
    db.session.commit()

def delete_reply(reply_id):

    """Function for deleting replies
    """
    sql = text("DELETE FROM replies WHERE id=:reply_id")
    db.session.execute(sql, {"reply_id":reply_id})
    db.session.commit()



def get_users_list():
    """Retrieves list of all users

    Returns:
        List: list of tuples (id, username, is_admin, banned)     
    """

    sql = text("SELECT id, username, is_admin, banned FROM users ORDER BY banned DESC, username")
    result = db.session.execute(sql)
    users = result.fetchall()
    return users

def ban_user(id):
    """ Function sets users banned column to True 

    Args:
        id (Int): User ID
    """

    sql = text("UPDATE users SET banned=True WHERE id=:id")
    db.session.execute(sql, {"id":id})
    db.session.commit()

def unban_user(id):
    """ Function sets users banned column to False 

    Args:
        id (Int): User ID
    """

    sql = text("UPDATE users SET banned=False WHERE id=:id")
    db.session.execute(sql, {"id":id})
    db.session.commit()